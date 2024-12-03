from rapidfuzz import process, fuzz
from parser import load_patents, load_companies

# Load data from the provided JSON files
patents = load_patents("data/patents.json")
companies = load_companies("data/company_products.json")

def normalize_input(text: str) -> str:
    """Normalize user input by converting to lowercase and removing special characters."""
    return text.lower().strip()

def fuzzy_match_patent(patent_id: str):
    """Fuzzy match a patent ID with the patents in the dataset."""
    normalized_input = normalize_input(patent_id)
    patent_numbers = [patent["publication_number"] for patent in patents]
    matches = process.extract(normalized_input, patent_numbers, limit=3, scorer=fuzz.WRatio)

    return matches

def fuzzy_match_company(company_name: str):
    """Fuzzy match a company name with the companies in the dataset."""
    normalized_input = normalize_input(company_name)
    company_names = [company["name"] for company in companies]
    matches = process.extract(normalized_input, company_names, limit=3, scorer=fuzz.WRatio)

    return matches

