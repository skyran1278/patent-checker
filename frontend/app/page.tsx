"use client";

import React, { useState } from "react";
import InputForm from "./components/InputForm";
import ResultsDisplay from "./components/ResultsDisplay";

const HomePage: React.FC = () => {
  const [results, setResults] = useState(null);

  return (
    <div className="max-w-2xl mx-auto p-4">
      <h1 className="text-2xl font-bold mb-4">Patent Infringement Checker</h1>
      <InputForm onSubmit={(data) => setResults(data)} />
      <ResultsDisplay results={results} />
    </div>
  );
};

export default HomePage;
