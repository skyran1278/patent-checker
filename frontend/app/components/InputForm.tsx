"use client";

import React, { useState } from "react";

interface InputFormProps {
  onSubmit: (data: any) => void;
}

const InputForm: React.FC<InputFormProps> = ({ onSubmit }) => {
  const [patentId, setPatentId] = useState("");
  const [companyName, setCompanyName] = useState("");
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setLoading(true);
    setError("");

    try {
      const response = await fetch("/api/check-infringement", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          patent_id: patentId,
          company_name: companyName,
        }),
      });

      if (!response.ok) {
        throw new Error("Failed to check infringement. Please try again.");
      }

      const data = await response.json();
      onSubmit(data);
    } catch (err) {
      setError((err as Error).message);
    } finally {
      setLoading(false);
    }
  };

  return (
    <form className="space-y-4" onSubmit={handleSubmit}>
      <div>
        <label htmlFor="patentId" className="block text-sm font-medium">
          Patent ID:
        </label>
        <input
          type="text"
          id="patentId"
          value={patentId}
          onChange={(e) => setPatentId(e.target.value)}
          required
          className="w-full mt-1 p-2 border rounded"
        />
      </div>
      <div>
        <label htmlFor="companyName" className="block text-sm font-medium">
          Company Name:
        </label>
        <input
          type="text"
          id="companyName"
          value={companyName}
          onChange={(e) => setCompanyName(e.target.value)}
          required
          className="w-full mt-1 p-2 border rounded"
        />
      </div>
      {error && <p className="text-red-500">{error}</p>}
      <button
        type="submit"
        disabled={loading}
        className="px-4 py-2 bg-blue-500 text-white rounded disabled:bg-gray-300"
      >
        {loading ? "Checking..." : "Check Infringement"}
      </button>
    </form>
  );
};

export default InputForm;
