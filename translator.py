"""
Translation module using deep-translator (Google Translate).
Supports Tamil, Hindi, French, Spanish and 100+ languages.
No model download required.
"""

from langdetect import detect
from deep_translator import GoogleTranslator


def detect_language(text: str) -> str:
    """
    Detects the language of input text.
    Returns language code like 'ta', 'hi', 'en', 'fr'.
    """
    try:
        return detect(text)
    except Exception:
        return "en"


def translate_text(text: str, src_lang: str, tgt_lang: str) -> str:
    """
    Translates text from source to target language using Google Translate.
    
    Args:
        text: Text to translate
        src_lang: Source language code (e.g., 'ta', 'hi')
        tgt_lang: Target language code (e.g., 'en')
    
    Returns:
        str: Translated text
    """
    if src_lang == tgt_lang:
        return text
    try:
        translated = GoogleTranslator(source=src_lang, target=tgt_lang).translate(text)
        return translated
    except Exception as e:
        return f"[Translation failed: {str(e)}]"


def translate_to_english(text: str, src_lang: str) -> str:
    """Translates any language to English."""
    if src_lang == "en":
        return text
    return translate_text(text, src_lang, "en")


def translate_from_english(text: str, tgt_lang: str) -> str:
    """Translates English text back to target language."""
    if tgt_lang == "en":
        return text
    return translate_text(text, "en", tgt_lang)