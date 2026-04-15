import streamlit as st
import random

st.set_page_config(page_title="My AI TaleTailor", page_icon="📖")

st.title("📖 My AI TaleTailor")
st.write("Generate creative story ideas without any API — powered by smart local logic!")

# Input fields
genre = st.text_input("Genre", "Fantasy")
theme = st.text_input("Theme", "Redemption and Betrayal")
character = st.text_input("Main Character Type", "Runaway prince")
setting = st.text_input("Setting Description", "A dying magical forest")
twist = st.text_input("Plot Twist Topic", "The prince’s pet is the real villain")

# Surprise examples
if st.button("Surprise Me"):
    examples = [
        ("Sci-Fi", "AI rebellion", "Cyborg detective", "Mars colony", "AI turns sentient"),
        ("Mystery", "Secrets and Lies", "Amnesiac girl", "Abandoned mansion", "She's the murderer"),
        ("Adventure", "Lost Civilization", "Reluctant archaeologist", "Deserted island", "The treasure is cursed"),
        ("Horror", "Ancient curse", "Cursed child", "Haunted village", "Child is the ghost"),
        ("Romance", "Unexpected Love", "Enemy prince", "Royal ball", "They’re long-lost siblings"),
    ]
    g, t, c, s, tw = random.choice(examples)
    genre = g
    theme = t
    character = c
    setting = s
    twist = tw
    st.experimental_rerun()

# Logic to create the story prompt
def generate_story_idea(genre, theme, character, setting, twist):
    templates = [
        f"In the {genre} genre, a {character} is caught in a tale of {theme}. Set in {setting}, the story unfolds with a surprising twist — {twist}.",
        f"A story of {theme} emerges in a {genre} world where a {character} must navigate the mysterious paths of {setting}. The unexpected truth? {twist}.",
        f"{character}, living in {setting}, faces a challenge rooted in {theme}. In this {genre} adventure, everything changes when {twist}.",
        f"In a tale of {genre}, {character} must survive in {setting}, only to discover that {twist}. The theme of {theme} runs deep throughout the story.",
    ]
    return random.choice(templates)

# Generate button
if st.button("Generate Story Idea"):
    if genre and theme and character and setting and twist:
        idea = generate_story_idea(genre, theme, character, setting, twist)
        st.success("Here's your story idea:")
        st.write(f"💡 **{idea}**")
    else:
        st.warning("Please fill in all fields before generating a story.")
