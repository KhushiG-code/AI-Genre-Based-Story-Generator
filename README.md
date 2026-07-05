# AI Genre-Based Story Generator

## Overview

AI Genre-Based Story Generator is a web application that generates creative stories based on the genre selected by the user. The application uses the OpenAI API to generate unique stories and Streamlit to provide a simple and interactive user interface.

## Features

* Generate stories in different genres such as Horror, Romance, Science Fiction, Fantasy, Mystery, and Adventure.
* AI-powered story generation using the OpenAI API.
* Simple and interactive web interface.
* Real-time story generation.
* Easy to use.

## Tech Stack

* Python
* Streamlit
* OpenAI API

## Project Structure

```text
AI-Genre-Based-Story-Generator/
│
├── storygen.py
├── requirements.txt
├── README.md
│
└── .streamlit/
    └── secrets.toml
```

## Installation

### Clone the Repository

```bash
git clone https://github.com/your-username/AI-Genre-Based-Story-Generator.git
cd AI-Genre-Based-Story-Generator
```

### Install the Required Packages

```bash
pip install -r requirements.txt
```

### Add Your OpenAI API Key

Create a file named:

```text
.streamlit/secrets.toml
```

Add your API key:

```toml
OPENAI_API_KEY = "your_api_key_here"
```

## Run the Application

```bash
streamlit run storygen.py
```

## How It Works

1. Select a story genre.
2. Enter a prompt (if applicable).
3. The application sends the request to the OpenAI API.
4. The AI generates a story based on the selected genre.
5. The generated story is displayed on the screen.

## Future Improvements

* Add story length selection.
* Support multiple languages.
* Allow users to download generated stories.
* Add voice narration.
* Improve the user interface.

## Author

**Khushi Gupta**

B.Tech CSE (Cyber Security)
Uttar Pradesh State Institute of Forensic Science (UPSIFS)
