export async function askQuestion(question: string) {
  const response = await fetch("/api/question", {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify({
      question: question
    })
  });

  if (!response.ok) {
    throw new Error("خطا در دریافت پاسخ از سرور");
  }

  return response.json();
}
