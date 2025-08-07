
import streamlit as st
import random

st.set_page_config(page_title="Synq’d Prompt Generator", page_icon="✨", layout="centered")

st.title("✨ Synq’d Prompt Generator")
st.markdown("Your billion-dollar idea birther—spirit-led, strategy-backed, and ready to drop fire anytime you say ‘Go.’")

prompt_categories = {
    "Vision Engineering": [
        "What would your business look like if God rewrote your vision statement?",
        "If your next product had to heal someone emotionally *and* financially, what would it be?",
    ],
    "Offer Engineering": [
        "Design an offer that solves a problem no one else dares to touch.",
        "How can your current service transform into a movement?",
    ],
    "AI Strategy": [
        "How could AI save you 10 hours this week—without compromising your soul?",
        "Create an AI-powered experience that feels deeply human.",
    ],
    "Branding": [
        "If your brand had a scent, song, and scripture—what would they be?",
        "What’s your brand’s divine fingerprint?",
    ],
    "Licensing": [
        "How can you turn your IP into income while you sleep?",
        "Create a licensing strategy for your top 3 frameworks or tools.",
    ],
    "Client Journey": [
        "Map your client’s transformation from chaos to clarity.",
        "What emotional experience are you truly selling?",
    ]
}

category = st.selectbox("Choose a Strategy Stream", list(prompt_categories.keys()))

if st.button("Give Me My Prompt"):
    st.markdown(f"💡 **Prompt:** {random.choice(prompt_categories[category])}")
