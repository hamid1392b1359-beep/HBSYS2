 "use client";

import { useState } from "react";
import { askHB } from "../lib/api";

export default function HomePage() {
  const [question, setQuestion] = useState("");
  const [language, setLanguage] = useState<"fa" | "en">("fa");
  const [answer, setAnswer] = useState("");
  const [loading, setLoading] = useState(false);

  const submit = async () => {
    if (!question.trim()) return;

    setLoading(true);
    setAnswer("");

    try {
      const data = await askHB({
        question,
        language,
        output_mode: "triple"
      });
      setAnswer(data.answer);
    } catch (error) {
      setAnswer(language === "fa" ? "خطا در دریافت پاسخ." : "Failed to get answer.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <main style={{ maxWidth: 900, margin: "40px auto", padding: 20 }}>
      <h1 style={{ marginBottom: 8 }}>H.B-SYST</h1>
      <p style={{ color: "#555" }}>
        {language === "fa" ? "سامانه پرسش از هسته H.B-SYST" : "Ask the H.B-SYST core"}
      </p>

      <div style={{ margin: "16px 0" }}>
        <select
          value={language}
          onChange={(e) => setLanguage(e.target.value as "fa" | "en")}
          style={{ padding: 10 }}
        >
          <option value="fa">فارسی</option>
          <option value="en">English</option>
        </select>
      </div>

      <textarea
        rows={7}
        value={question}
        onChange={(e) => setQuestion(e.target.value)}
        placeholder={language === "fa" ? "سؤال خود را بنویسید..." : "Write your question..."}
        style={{
          width: "100%",
          padding: 14,
          borderRadius: 12,
          border: "1px solid #ccc",
          background: "white"
        }}
      />

      <button
        onClick={submit}
        disabled={loading}
        style={{
          marginTop: 12,
          padding: "12px 18px",
          borderRadius: 10,
          border: "none",
          background: "#111",
          color: "white",
          cursor: "pointer"
        }}
      >
        {loading
          ? (language === "fa" ? "در حال پردازش..." : "Processing...")
          : (language === "fa" ? "پرسش" : "Ask")}
      </button>

      <div
        style={{
          marginTop: 24,
          background: "white",
          border: "1px solid #ddd",
          borderRadius: 12,
          padding: 16,
          whiteSpace: "pre-wrap",
          lineHeight: 1.9
        }}
      >
        {answer || (language === "fa" ? "پاسخ اینجا نمایش داده می‌شود." : "Answer will appear here.")}
      </div>
    </main>
  );
}
