# Story Idea Generator

A web-based text generation application built using LangChain, Hugging Face Transformers, and Flask. This project generates creative story ideas based on user inputs (genre and character description) by leveraging a Hugging Face LLM (`gpt2-medium` by default). The application features a simple Flask UI for user interaction and is modularized for easy extension.

## Features
- Generate story ideas by providing a genre and character description.
- Uses LangChain for prompt templating and integration with language models.
- Flask-based web UI for an intuitive user experience.
- Modular design with separate files for prompt templates, model handling, and Flask app logic.
- Easy to swap out the underlying model (e.g., switch to a Hugging Face Inference API or other local models).

## Project Structure


## Prerequisites
- Python 3.8 or higher
- A virtual environment (recommended)
- Access to a machine with at least 4 GB of RAM (for running `gpt2-medium` locally)
- Internet connection (for downloading models and dependencies)

## Setup Instructions

### 1. Clone the Repository
If this project is hosted on a git repository, clone it:
git clone <repository-url>
cd story-gen
### 2. Create and Activate a Virtual Environment
py -m venv env
### 3. Install Dependencies
pip install -r requirements.txt
### 4. Verify Project Files
Ensure the following files are present in the project root:

main.py
prompt.py
model.py
requirements.txt
templates/index.html
static/style.css

## USAGE
### Running the Application
#### 1. Activate your virtual environment (if not already active)
venv\bin\activate.bat

#### 2. run the app
py main.py

### Using the Web Interface
#### 1. On the webpage, enter a genre (e.g., "Fantasy", "Sci-Fi") and a character description (e.g., "a curious young wizard").
#### 2. Click the "Generate Story Idea" button.
#### 3. The generated prompt and story idea will be displayed below the form.

### Example 
