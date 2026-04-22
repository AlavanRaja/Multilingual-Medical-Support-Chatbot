# Multilingual Medical Support Chatbot

---

## 📖 Description

A multilingual medical chatbot built with **Streamlit** and **Hugging Face Transformers**.
Users can ask health-related questions in their own language (Tamil, Hindi, French, etc.)
and get medically accurate responses back in the same language — automatically!

The chatbot:
- Detects the user's language automatically
- Translates the query to English
- Generates a medical response using an AI model (Flan-T5)
- Translates the answer back to the user's language

> ⚠️ **Disclaimer:** This chatbot is for general awareness only.
> It is NOT a substitute for professional medical advice.
> Always consult a licensed doctor for medical concerns.

---

## 🛠️ Tech Stack

| Component | Tool / Library |
|---|---|
| Web Framework | Streamlit |
| Language Detection | langdetect |
| Translation | deep-translator (Google Translate) |
| Medical AI Model | google/flan-t5-small (Hugging Face) |
| ML Framework | PyTorch |
| Version Control | Git & GitHub |
| Language | Python 3.13 |
| Deployment | Streamlit Cloud |

---

## 🗂️ Project Structure

```
multilingual-medical-chatbot/
│
├── app.py → Main Streamlit app
├── translator.py → Translation logic
├── medical_model.py → Medical LLM response generator
├── language_config.py → Language settings
├── utils.py → Helper functions
├── requirements.txt → Dependencies
└── README.md → Documentation
```

### Start Chatting!
- Select your language from the **sidebar**
- Type your medical question in your language
- The chatbot will reply in the selected language automatically ✅

---

## 🌍 Supported Languages

| Language | Code |
|---|---|
| English | en |
| Tamil | ta |
| Hindi | hi |
| French | fr |
| Spanish | es |
| German | de |
| Arabic | ar |
| Chinese | zh |
| Japanese | ja |
| Portuguese | pt |

---

## 👤 Author

**ABISHEK RAJA A**
- 📧 Email: abishekraja04121998@gmail.com

---

## 🙏 Acknowledgements

- [Hugging Face](https://huggingface.co) — AI Models
- [Streamlit](https://streamlit.io) — Web Framework
- [deep-translator](https://github.com/nidhaloff/deep-translator) — Translation