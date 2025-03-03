from transformers import pipeline
from langchain.llms.huggingface_pipeline import HuggingFacePipeline

# Initialize the text generation pipeline using Hugging Face
def initialize_model():
    # Load the distilgpt2 model locally
    generator = pipeline(
        "text-generation",
        model="gpt2-medium",
        max_length=150,  # Limit output length
        num_return_sequences=1,  # Number of outputs
        truncation=True,
        temperature=0.9,
        top_p=0.95
    )
    
    # Wrap the pipeline in a LangChain-compatible LLM
    llm = HuggingFacePipeline(pipeline=generator)
    return llm

# Function to generate text using the model
def generate_text(llm, prompt: str) -> str:
    try:
        # Generate the story idea
        result = llm.invoke(prompt)
        return result
    except Exception as e:
        return f"Error generating text: {str(e)}"