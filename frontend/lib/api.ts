export async function askHB(payload: {
  question: string;
  language: "fa" | "en";
  output_mode: "triple" | "short" | "analytical";
}) {
  const baseUrl = process.env.NEXT_PUBLIC_API_URL || "http://localhost:8000";

  const res = await fetch(`${baseUrl}/ask`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(payload),
  });

  if (!res.ok) {
    throw new Error("Request failed");
  }

  return res.json();
}
