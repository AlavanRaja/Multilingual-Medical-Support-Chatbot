"""
Multilingual Medical Support Chatbot
Built with Streamlit + Hugging Face Transformers
Author: [Your Name]
"""

import streamlit as st
from translator import detect_language, translate_to_english, translate_from_english
from medical_model import generate_medical_response
from utils import get_language_code, get_language_name, format_chat_message
from language_config import SUPPORTED_LANGUAGES


# ─── Page Configuration ──────────────────────────────────────────────────────

def configure_page():
    """Sets Streamlit page title, icon, and layout."""
    st.set_page_config(
        page_title="Multilingual Medical Chatbot",
        page_icon="🏥",
        layout="wide",
        initial_sidebar_state="expanded"
    )

configure_page()


# ─── Custom CSS Styling ───────────────────────────────────────────────────────

def apply_custom_styles():
    """Injects custom CSS for improved UI appearance."""
    st.markdown("""
    <style>
        .main-title {
            font-size: 2rem;
            font-weight: 700;
            color: #01696f;
            text-align: center;
            margin-bottom: 0.5rem;
        }
        .subtitle {
            text-align: center;
            color: #7a7974;
            margin-bottom: 2rem;
        }
        .disclaimer-box {
            background-color: #fff3cd;
            border-left: 4px solid #ffc107;
            padding: 12px 16px;
            border-radius: 6px;
            color: #856404;
            font-size: 0.9rem;
            margin-bottom: 1rem;
        }
        .chat-user {
            background-color: #e8f4f8;
            border-radius: 12px;
            padding: 10px 14px;
            margin: 6px 0;
        }
        .chat-bot {
            background-color: #f0faf0;
            border-radius: 12px;
            padding: 10px 14px;
            margin: 6px 0;
        }
    </style>
    """, unsafe_allow_html=True)

apply_custom_styles()


# ─── Session State Initialization ─────────────────────────────────────────────

def initialize_session_state():
    """Initializes chat history and settings in session state."""
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []
    if "selected_language" not in st.session_state:
        st.session_state.selected_language = "English"

initialize_session_state()


# ─── Sidebar Configuration ────────────────────────────────────────────────────

def render_sidebar():
    """Renders the sidebar with language selection and options."""
    with st.sidebar:
        st.image("https://img.icons8.com/color/96/000000/caduceus.png", width=60)
        st.title("⚙️ Settings")
        st.divider()

        selected_lang = st.selectbox(
            "🌐 Select Your Language",
            options=list(SUPPORTED_LANGUAGES.keys()),
            index=0,
            help="Choose the language you want to chat in"
        )
        st.session_state.selected_language = selected_lang

        st.divider()
        st.markdown("### 📋 About")
        st.info(
            "This chatbot answers medical queries in multiple languages. "
            "Powered by Helsinki-NLP (Translation) + Flan-T5 (Medical QA)."
        )

        st.divider()
        if st.button("🗑️ Clear Chat History", use_container_width=True):
            st.session_state.chat_history = []
            st.success("Chat cleared!")

    return selected_lang


# ─── Chat Display ─────────────────────────────────────────────────────────────

def display_chat_history():
    """Renders all chat messages from session state."""
    for message in st.session_state.chat_history:
        if message["role"] == "user":
            with st.chat_message("user", avatar="🧑"):
                st.markdown(message["content"])
        else:
            with st.chat_message("assistant", avatar="🏥"):
                st.markdown(message["content"])


# ─── Core Pipeline ────────────────────────────────────────────────────────────

def process_medical_query(user_input: str, user_lang_code: str) -> str:
    """
    Full pipeline: Detect → Translate to EN → Get Medical Answer → Translate Back.
    
    Args:
        user_input: Raw user query text
        user_lang_code: User's selected language code
    
    Returns:
        str: Final translated medical response
    """
    # Step 1: Translate input to English
    with st.spinner("🔄 Translating your query..."):
        english_query = translate_to_english(user_input, user_lang_code)

    # Step 2: Generate medical response in English
    with st.spinner("🧠 Generating medical response..."):
        english_response = generate_medical_response(english_query)

    # Step 3: Translate response back to user's language
    with st.spinner("🔄 Translating response back..."):
        final_response = translate_from_english(english_response, user_lang_code)

    return final_response


# ─── Main App ─────────────────────────────────────────────────────────────────

def main():
    """Main app entry point."""

    # Header
    st.markdown('<div class="main-title">🏥 Multilingual Medical Support Chatbot</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle">Ask medical questions in your language — get accurate answers instantly</div>', unsafe_allow_html=True)

    # Disclaimer
    st.markdown("""
    <div class="disclaimer-box">
    ⚠️ <strong>Disclaimer:</strong> This chatbot provides general health information only.
    It is NOT a substitute for professional medical diagnosis or treatment.
    Always consult a qualified doctor for medical advice.
    </div>
    """, unsafe_allow_html=True)

    # Sidebar
    selected_language = render_sidebar()
    user_lang_code = get_language_code(selected_language)

    # Show current language
    st.caption(f"💬 Currently chatting in: **{selected_language}** (Code: `{user_lang_code}`)")

    st.divider()

    # Display existing chat messages
    display_chat_history()

    # Input area
    user_input = st.chat_input(f"Type your medical question in {selected_language}...")

    if user_input:
        # Save user message to history
        st.session_state.chat_history.append(format_chat_message("user", user_input))

        # Display user message
        with st.chat_message("user", avatar="🧑"):
            st.markdown(user_input)

        # Process and display response
        with st.chat_message("assistant", avatar="🏥"):
            response = process_medical_query(user_input, user_lang_code)
            st.markdown(response)

        # Save bot response to history
        st.session_state.chat_history.append(format_chat_message("assistant", response))


if __name__ == "__main__":
    main()