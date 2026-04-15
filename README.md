# AI-Genre-Based-Story-Generator

An AI-powered web app that generates creative stories based on selected genres using OpenAI API and Streamlit.

🚀 Features
🎭 Generate stories based on different genres (Horror, Romance, Sci-Fi, etc.)
🤖 Uses AI for creative and unique storytelling
⚡ Simple and interactive UI using Streamlit
📝 Instant story generation

🛠️ Tech Stack
Python 🐍
Streamlit 🌐
OpenAI API 🤖

📂 Project Structure
My_AI_TaleTailor/
│── storygen.py        # Main Streamlit app
│── requirements.txt   # Dependencies
│── README.md          # Project documentation
│── .streamlit/
│    └── secrets.toml  # API key (not pushed)
⚙️ Setup Instructions
1️⃣ Clone the repository
git clone https://github.com/KhushiG-code/AI-Genre-Based-Story-Generator.git
cd AI-Genre-Based-Story-Generator
2️⃣ Install dependencies
pip install -r requirements.txt
3️⃣ Add OpenAI API Key

Create a file:

.streamlit/secrets.toml


OPENAI_API_KEY = "your_api_key_here"
4️⃣ Run the app
streamlit run storygen.py
🎯 How It Works
User selects a genre
App sends request to OpenAI API
AI generates a story
Story is displayed instantly



⭐ Future Improvements
Add story length control
Add multiple languages
Save/download stories
Voice narration feature
