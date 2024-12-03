import { NextResponse } from "next/server";

export async function POST(req: Request) {
  const { patent_id, company_name } = await req.json();

  // Replace with actual backend URL
  const backendUrl = `${process.env.NEXT_PUBLIC_API_URL}/check-infringement`;

  try {
    const response = await fetch(backendUrl, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ patent_id, company_name }),
    });

    const data = await response.json();
    return NextResponse.json(data);
  } catch (error) {
    return NextResponse.json(
      { error: "Failed to fetch results" },
      { status: 500 }
    );
  }
}
