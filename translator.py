"""
Translation module using deep-translator (Google Translate).
Handles language detection and bidirectional translation.
"""

from deep_translator import GoogleTranslator
from langdetect import detect
import streamlit as st
from language_config import SUPPORTED_LANGUAGES


def detect_language(text: str) -> str:
    """
    Detects the language of the input text automatically.
    Returns language code like 'ta', 'hi', 'fr', 'en'
    """
    try:
        return detect(text)
    except Exception:
        return "en"  # Default to English if detection fails


def translate_to_english(text: str, src_lang: str) -> str:
    """
    Translates any language text to English.
    Uses 'auto' detection if source language is unknown.
    """
    if src_lang == "en":
        return text
    try:
        translated = GoogleTranslator(source="auto", target="en").translate(text)
        return translated
    except Exception as e:
        return text  # Return original text if translation fails


def translate_from_english(text: str, tgt_lang: str) -> str:
    """
    Translates English text to the target language.
    """
    if tgt_lang == "en":
        return text
    try:
        translated = GoogleTranslator(source="en", target=tgt_lang).translate(text)
        return translated
    except Exception as e:
        return text  # Return original English if translation fails