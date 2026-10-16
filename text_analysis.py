import os
import re
from collections import Counter

# Function 
def countTokens(text):
    tokens = re.findall(r'\b\w+\b', text)
    return len(tokens)


def countToken(text, token):
    tokens = re.findall(r'\b\w+\b', text.lower())
    return tokens.count(token.lower())

# Function 
def normalisedFrequency(text, token):
    total_tokens = countTokens(text)
    token_count = countToken(text, token)
    return token_count / total_tokens if total_tokens > 0 else 0


def sentenceCount(text):
    sentences = re.split(r'[.!?]', text)
    return len([s for s in sentences if s.strip()])

# Function 
def sentencesContaining(text, token):
    sentences = re.split(r'[.!?]', text)
    token = token.lower()
    return [s.strip() for s in sentences if re.search(rf'\b{token}\b', s, re.IGNORECASE)]

# Main program
def main():
    file_name = input("Enter the name of the text file (including extension): ").strip()
    
    if not os.path.exists(file_name):
        print("File not found. Please check the file name and try again.")
        return

    with open(file_name, 'r', encoding='utf-8') as file:
        text = file.read()
    
    print("\nDescriptive Statistics:")
    print(f"1. Total tokens: {countTokens(text)}")
    
    token_to_check = input("\nEnter a token to check its frequency and normalised frequency: ").strip()
    print(f"2. Frequency of '{token_to_check}': {countToken(text, token_to_check)}")
    print(f"3. Normalised frequency of '{token_to_check}': {normalisedFrequency(text, token_to_check):.6f}")
    
    print(f"4. Total number of sentences: {sentenceCount(text)}")
    
    sentences_with_token = sentencesContaining(text, token_to_check)
    print(f"5. Sentences containing '{token_to_check}':")
    for i, sentence in enumerate(sentences_with_token, 1):
        print(f"{i}. {sentence}")

if __name__ == "__main__":
    main()
