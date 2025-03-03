from langchain.prompts import PromptTemplate

# Define a prompt template for story generation
story_prompt_template = PromptTemplate(
    input_variables=["genre", "character"],
    template="Write a short story idea in the {genre} genre featuring a character described as {character}."
)

# Function to format the prompt
def get_formatted_prompt(genre: str, character: str) -> str:
    return story_prompt_template.format(genre=genre, character=character)