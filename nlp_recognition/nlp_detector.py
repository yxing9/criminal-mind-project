import openai
import os
import pandas as pd
import chardet

from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())

openai.api_key  = os.getenv('OPENAI_API_KEY')

def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0, # this is the degree of randomness of the model's output
    )
    return response.choices[0].message["content"]

# Detect the encoding
with open('text_data-1.csv', 'rb') as f:
    result = chardet.detect(f.read())
    
# Use the detected encoding to read the file
df = pd.read_csv('text_data-1.csv', encoding=result['encoding'])

# Assuming the text data is in a column named 'text'
for text in df['text']:
    prompt = f"""
    Summarize the text delimited by triple backticks into 1 keyword.
    ```{text}```
    """
    response = get_completion(prompt)
    print(response)
