import json
from openai import OpenAI
import os
from datetime import datetime
from fuzzy_match import fuzzy_match_company, fuzzy_match_patent

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),  # This is the default and can be omitted
)

def analyze_relevance_with_openai(patent, description):
    """
    Use OpenAI API v1.0.0 to compute relevance between patent claims and a product description.
    """
    # Prepare the prompt
    prompt = f"""
    Return the top two infringing products of the company along with explanations of why these products potentially infringe the patent, specifically detailing which claims are at issue.

    Patent:
    {patent}

    Products:
    {description}
    """

    try:
        completion = client.chat.completions.create(
            model="gpt-4o",  # Replace with desired model
            messages=[{
                "role": "user",
                "content": prompt
            }],
            response_format = {
                "type": "json_schema",
                "json_schema": {
                    "name": "InfringementAnalysis",
                    "description": "An analysis of the relevance between patent and products.",
                    "schema": {
                        "$schema": "http://json-schema.org/draft-07/schema#",
                        "type": "object",
                        "properties": {
                          "patent_id": {
                            "type": "string"
                          },
                          "company_name": {
                            "type": "string"
                          },
                          "top_infringing_products": {
                            "type": "array",
                            "items": {
                              "type": "object",
                              "properties": {
                                "product_name": {
                                  "type": "string"
                                },
                                "infringement_likelihood": {
                                  "type": "string",
                                  "enum": ["High", "Moderate", "Low"]
                                },
                                "relevant_claims": {
                                  "type": "array",
                                  "items": {
                                    "type": "string",
                                    "description": "The claim number with the patent. For example, '1', '2', '3'.",
                                    "pattern": "^[0-9]+$"
                                  }
                                },
                                "explanation": {
                                  "type": "string"
                                },
                                "specific_features": {
                                  "type": "array",
                                  "items": {
                                    "type": "string"
                                  }
                                }
                              },
                              "required": ["product_name", "infringement_likelihood", "relevant_claims", "explanation", "specific_features"]
                            }
                          },
                          "overall_risk_assessment": {
                            "type": "string"
                          }
                        },
                        "required": ["analysis_id", "patent_id", "company_name", "analysis_date", "top_infringing_products", "overall_risk_assessment"],
                    }
                }
            }
        )

        # Parse the response
        result = json.loads(completion.choices[0].message.content)
        result["analysis_date"] = datetime.fromtimestamp(completion.created)
        return result

    except Exception as e:
        print(f"Error using OpenAI API: {e}")
        return 0, "Error in relevance analysis"

def check_infringement(patent_id, company_name, patents, companies):
    """
    Refactored function to use OpenAI for relevance analysis.
    """
    # Find the patent
    patent = next((p for p in patents if p["publication_number"] == patent_id), None)
    if not patent:
        possible_patents = fuzzy_match_patent(patent_id)
        if possible_patents:
            patent = next((p for p in patents if p["publication_number"] == possible_patents[0][0]), None)

    # Find the company
    company = next((c for c in companies if c["name"].lower() == company_name.lower()), None)
    if not company:
        possible_companies = fuzzy_match_company(company_name)
        if possible_companies:
            company = next((c for c in companies if c["name"].lower() == possible_companies[0][0].lower()), None)

    return analyze_relevance_with_openai(
        json.dumps(patent),  # Serialize claims
        json.dumps(company["products"])
    )
