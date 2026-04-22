"""
Utility helper functions for the chatbot application.
"""

from language_config import SUPPORTED_LANGUAGES


def get_language_code(language_name: str) -> str:
    """
    Converts a display language name to its language code.
    
    Args:
        language_name: Full language name (e.g., 'Tamil')
    
    Returns:
        str: Language code (e.g., 'ta')
    """
    return SUPPORTED_LANGUAGES.get(language_name, "en")


def get_language_name(language_code: str) -> str:
    """
    Converts a language code to its display name.
    
    Args:
        language_code: Language code (e.g., 'ta')
    
    Returns:
        str: Display name (e.g., 'Tamil')
    """
    reverse_map = {v: k for k, v in SUPPORTED_LANGUAGES.items()}
    return reverse_map.get(language_code, "English")


def format_chat_message(role: str, content: str) -> dict:
    """
    Formats a message for chat history storage.
    
    Args:
        role: 'user' or 'assistant'
        content: Message text
    
    Returns:
        dict: Formatted message dict
    """
    return {"role": role, "content": content}


def truncate_text(text: str, max_length: int = 500) -> str:
    """
    Truncates long text with ellipsis if needed.
    
    Args:
        text: Input text
        max_length: Maximum allowed characters
    
    Returns:
        str: Truncated or original text
    """
    if len(text) > max_length:
        return text[:max_length] + "..."
    return text