import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def get_car_ai_bio(model, brand, year):
    
    message = f"Me mostre uma descrição para o carro {brand} {model} {year} em apenas 250 caracteres, seja realista e convincente."

    response = client.chat.completions.create(
        model='gpt-3.5-turbo',
        messages=[
            {
                'role': 'user',
                'content': message
            }
        ],
        max_tokens=250,
    )

    return response.choices[0].message.content.strip()
