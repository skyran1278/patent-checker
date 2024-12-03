import React from "react";

interface Product {
  product_name: string;
  infringement_likelihood: string;
  explanation: string;
  specific_features: string[];
}

interface ResultsDisplayProps {
  results: {
    patent_id: string;
    company_name: string;
    overall_risk_assessment: string;
    top_infringing_products: Product[];
  } | null;
}

const ResultsDisplay: React.FC<ResultsDisplayProps> = ({ results }) => {
  if (!results) return null;

  return (
    <div className="mt-8 p-6 bg-white shadow-lg rounded-lg">
      <h2 className="text-2xl font-bold text-blue-600 mb-4">
        Analysis Results
      </h2>
      <div className="mb-6">
        <p className="text-sm text-gray-500">
          <span className="font-semibold">Patent ID:</span> {results.patent_id}
        </p>
        <p className="text-sm text-gray-500">
          <span className="font-semibold">Company Name:</span>{" "}
          {results.company_name}
        </p>
        <p className="text-sm text-gray-500">
          <span className="font-semibold">Overall Risk Assessment:</span>{" "}
          <span
            className={`inline-block px-2 py-1 text-sm rounded ${
              results.overall_risk_assessment.includes("High")
                ? "bg-red-100 text-red-600"
                : "bg-yellow-100 text-yellow-600"
            }`}
          >
            {results.overall_risk_assessment}
          </span>
        </p>
      </div>

      <h3 className="text-xl font-semibold text-gray-800 mb-4">
        Top Infringing Products
      </h3>
      <ul className="space-y-4">
        {results.top_infringing_products.map((product, index) => (
          <li
            key={index}
            className="p-4 bg-gray-50 border border-gray-200 rounded-lg"
          >
            <div className="flex justify-between items-center">
              <h4 className="text-lg font-semibold text-gray-700">
                {product.product_name}
              </h4>
              <span
                className={`inline-block px-2 py-1 text-sm rounded ${
                  product.infringement_likelihood === "High"
                    ? "bg-red-100 text-red-600"
                    : product.infringement_likelihood === "Moderate"
                    ? "bg-yellow-100 text-yellow-600"
                    : "bg-green-100 text-green-600"
                }`}
              >
                {product.infringement_likelihood}
              </span>
            </div>
            <p className="text-sm text-gray-600 mt-2">
              <span className="font-semibold">Explanation:</span>{" "}
              {product.explanation}
            </p>
            <ul className="mt-2 list-disc list-inside text-sm text-gray-600">
              {product.specific_features.map((feature, i) => (
                <li key={i}>{feature}</li>
              ))}
            </ul>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default ResultsDisplay;
