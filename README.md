# Story Idea Generator

A web-based text generation application built using LangChain, Hugging Face Transformers, and Flask. This project generates creative story ideas based on user inputs (genre and character description) by leveraging a Hugging Face LLM (`EleutherAI/gpt-neo-1.3B` by default). The application features a simple Flask UI for user interaction and is modularized for easy extension.

## Features
- Generate story ideas by providing a genre and character description.
- Uses LangChain for prompt templating and integration with language models.
- Flask-based web UI for an intuitive user experience.
- Modular design with separate files for prompt templates, model handling, and Flask app logic.
- Easy to swap out the underlying model (e.g., switch to a Hugging Face Inference API or other local models).
- Clean output format displaying the generated prompt and story idea separately.

## Project Structure

text-gen-project/
│
├── main.py           # Flask app to handle routes and UI
├── prompt.py         # Defines prompt templates using LangChain
├── model.py          # Initializes and interacts with the model
├── requirements.txt  # List of dependencies
├── README.md         # Project documentation
├── templates/        # Directory for HTML templates
│   └── index.html    # Main UI template
└── static/           # Directory for static files (optional)
└── style.css     # Optional CSS for styling


## Prerequisites
- Python 3.8 or higher
- A virtual environment (recommended)
- Access to a machine with at least 8 GB of RAM (for running `gpt-neo-1.3B` locally on CPU) or 4 GB GPU memory (if using a GPU)
- Internet connection (for downloading models and dependencies)

## Setup Instructions

### 1. Clone the Repository
If this project is hosted on a git repository, clone it:
git clone <repository-url>
cd text-gen-project

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
![sample3](https://github.com/user-attachments/assets/ace5cb27-0f61-44f6-8d1e-c7fc05a94861) 
![sample4](https://github.com/user-attachments/assets/13d79573-b3ce-47a4-af9f-e527dbe78b62)

### Troubleshooting

- ModuleNotFoundError: Ensure all dependencies are installed (pip install -r requirements.txt) and the virtual environment is active.
- Model Loading Issues: If gpt-neo-1.3B fails to load, check disk space (~2.5 GB for download) and memory (~8 GB RAM for CPU, 4 GB GPU memory). Try a smaller model like gpt2-medium or use a cloud-based API.
- Slow Inference: gpt-neo-1.3B can be slow on CPU (several seconds per generation). Use a GPU, reduce max_length, or enable quantization.
- Flask Errors: Verify that templates/index.html exists and the Flask app is running on an available port (default: 5000).
- Output Quality: If the generated text is incoherent or repetitive, adjust temperature, top_p, or add a repetition_penalty in model.py. Switching to a smaller or larger model may also help.

### Future Improvements

- To add a database to store generated story ideas.
- Implement AJAX for asynchronous text generation with a loading indicator.
- Deploy the app to a cloud platform (e.g., Heroku, Render).
- To Integrate more advanced models like LLaMA or Gemma (if accessible) for better output quality.
- To add input validation and error handling in the UI.

### Acknowledments

- Built with LangChain for prompt templating and LLM integration.
- Uses Hugging Face Transformers for text generation.
- Powered by Flask for the web interface.
- Default model: EleutherAI/gpt-neo-1.3B.
