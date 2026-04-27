"""
Medical question-answering using Groq API (Free).
Uses LLaMA-3 model for precise, detailed medical responses.
"""

import streamlit as st
from groq import Groq
import os

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

MEDICAL_DISCLAIMER = (
    "\n\n⚠️ **Medical Disclaimer:** This information is for "
    "general awareness only. It is NOT a substitute for "
    "professional medical diagnosis or treatment. "
    "Please consult a qualified doctor for medical advice."
)

SYSTEM_PROMPT = """You are a professional medical assistant with expert knowledge 
in medicine, symptoms, diseases, treatments, and healthcare.

When answering:
- Give clear, accurate, and detailed answers in 4-6 sentences
- Mention causes, symptoms, and basic treatment/advice
- Use simple language that a patient can understand
- Never refuse a general medical question
- Always be helpful and informative"""


@st.cache_resource(show_spinner=False)
def load_groq_client():
    """Initializes and caches the Groq client."""
    try:
        client = Groq(api_key=GROQ_API_KEY)
        return client
    except Exception as e:
        return None


def generate_medical_response(query: str) -> str:
    """
    Generates a precise medical response using Groq LLaMA-3 model.

    Args:
        query: English-language medical question

    Returns:
        str: Detailed medical response with disclaimer
    """
    client = load_groq_client()

    if client is None:
        return "Failed to connect to medical model. Check your API key." + MEDICAL_DISCLAIMER

    try:
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": SYSTEM_PROMPT
                },
                {
                    "role": "user",
                    "content": query
                }
            ],
            model="llama-3.1-8b-instant",   # Free, fast, high quality
            temperature=0.7,
            max_tokens=500,
        )

        response = chat_completion.choices[0].message.content.strip()
        return response + MEDICAL_DISCLAIMER

    except Exception as e:
        return f"Error generating response: {str(e)}" + MEDICAL_DISCLAIMER