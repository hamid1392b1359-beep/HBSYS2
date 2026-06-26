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
