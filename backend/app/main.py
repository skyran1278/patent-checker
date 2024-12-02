from flask import Flask, request, jsonify
from parser import load_patents, load_companies
from checker import check_infringement

app = Flask(__name__)

# Load data
patents = load_patents("data/patents.json")
companies = load_companies("data/company_products.json")

@app.route('/check', methods=['POST'])
def check():
    data = request.get_json()
    patent_id = data.get('patent_id')
    company_name = data.get('company_name')

    if not patent_id or not company_name:
        return jsonify({"error": "Patent ID and Company Name are required"}), 400

    result = check_infringement(patent_id, company_name, patents, companies)
    return jsonify(result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
