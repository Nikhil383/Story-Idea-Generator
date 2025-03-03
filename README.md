# Story Idea Generator

A web-based text generation application built using LangChain, Hugging Face Transformers, and Flask. This project generates creative story ideas based on user inputs (genre and character description) by leveraging a Hugging Face LLM (`gpt2-medium` by default). The application features a simple Flask UI for user interaction and is modularized for easy extension.

## Features
- Generate story ideas by providing a genre and character description.
- Uses LangChain for prompt templating and integration with language models.
- Flask-based web UI for an intuitive user experience.
- Modular design with separate files for prompt templates, model handling, and Flask app logic.
- Easy to swap out the underlying model (e.g., switch to a Hugging Face Inference API or other local models).

## Project Structure