import spacy
from spacy.cli import download

# Function to download the English language model for dependency parsing
def download_language_model():
    try:
        # Try to load the model
        nlp = spacy.load('en_core_web_sm')
    except OSError:
        # If the model is not found, download it
        download('en_core_web_sm')
        nlp = spacy.load('en_core_web_sm')
    return nlp

def dependency_parsing(text):
    # Load the English language model for dependency parsing
    nlp = download_language_model()
    
    # Parse the input text
    doc = nlp(text)
    
    # Print the dependencies
    for token in doc:
        print(f"{token.text} --{token.dep_}--> {token.head.text}")

# Example sentence for dependency parsing
sentence = "The quick brown fox jumps over the lazy dog."

# Perform dependency parsing on the example sentence
dependency_parsing(sentence)
