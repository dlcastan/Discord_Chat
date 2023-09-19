import openai
from config import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY

def gpt(entrada):
    completion = openai.ChatCompletion.create(
                model = "gpt-3.5-turbo", # Modelo de OPENAI
                messages = [ 
                    {"role": "user", "content": entrada} 
                    ], 
                temperature = 0,
                max_tokens = 200) 
    
    return completion.choices[0].message.content