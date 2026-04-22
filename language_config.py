"""
Language configuration for supported translation pairs.
Maps language names to Helsinki-NLP model codes.
"""

# Supported languages with their codes
SUPPORTED_LANGUAGES = {
    "English": "en",
    "Tamil": "ta",
    "Hindi": "hi",
    "French": "fr",
    "Spanish": "es",
    "German": "de",
    "Arabic": "ar",
    "Chinese": "zh",
    "Japanese": "ja",
    "Portuguese": "pt",
}

# Helsinki-NLP translation model naming pattern
# Model format: Helsinki-NLP/opus-mt-{src}-{tgt}
TRANSLATION_MODEL_BASE = "Helsinki-NLP/opus-mt"

def get_translation_model_name(src_lang: str, tgt_lang: str) -> str:
    """
    Returns the Hugging Face model name for a given language pair.
    
    Args:
        src_lang: Source language code (e.g., 'ta')
        tgt_lang: Target language code (e.g., 'en')
    
    Returns:
        str: Full model name string
    """
    return f"{TRANSLATION_MODEL_BASE}-{src_lang}-{tgt_lang}"