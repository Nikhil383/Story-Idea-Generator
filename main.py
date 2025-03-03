from flask import Flask, render_template, request
from prompt import get_formatted_prompt
from model import initialize_model, generate_text

app = Flask(__name__)

# Initialize the model once when the app starts
print("Loading model...")
llm = initialize_model()
print("Model loaded successfully!")

@app.route('/', methods=['GET', 'POST'])
def index():
    story_idea = None
    prompt = None
    
    if request.method == 'POST':
        # Get form inputs
        genre = request.form.get('genre')
        character = request.form.get('character')
        
        if genre and character:
            # Format the prompt
            prompt = get_formatted_prompt(genre, character)
            # Generate the story idea
            story_idea = generate_text(llm, prompt)
    
    return render_template('index.html', story_idea=story_idea, prompt=prompt)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)