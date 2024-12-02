import json

def check_infringement(patent_id, company_name, patents, companies):
    # Find the patent
    patent = next((p for p in patents if p["publication_number"] == patent_id), None)
    if not patent:
        return {"error": "Patent not found"}

    # Find the company
    company = next((c for c in companies["companies"] if c["name"].lower() == company_name.lower()), None)
    if not company:
        return {"error": "Company not found"}

    # Compare claims with product descriptions
    infringing_products = []
    for product in company["products"]:
        relevance_score = compute_relevance(patent["claims"], product["description"])
        if relevance_score > 0.5:  # Assume a threshold for infringement
            infringing_products.append({
                "product_name": product["name"],
                "infringement_likelihood": "High" if relevance_score > 0.75 else "Moderate",
                "relevance_score": relevance_score,
                "explanation": f"Claims overlap detected in product '{product['name']}'"
            })

    # Sort and return top two
    infringing_products.sort(key=lambda x: x["relevance_score"], reverse=True)
    return {
        "patent_id": patent_id,
        "company_name": company_name,
        "top_infringing_products": infringing_products[:2]
    }

def compute_relevance(claims, description):
    """Simple relevance computation for demonstration."""
    matched_claims = sum(1 for claim in json.loads(claims) if claim["text"] in description)
    return matched_claims / len(claims) if claims else 0
