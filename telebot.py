
import os
import openai
import aiogram
openai.api_key = "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"

completion = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "Ты личный ассистент , Тебя зовут Макс."},
    {"role": "user", "content": "Привет, как тебя зовут как ты можешь мне помочь ?"}
  ]
)

print(completion.choices[0].message)

# pip install aiohttp
# pip install frozenlist
# pip install multidict
# pip install yarl

#pip install --upgrade pip 
#pip install aiogram[fast]

#pip install -U aiogram
#python -m pip install aiogram

#pip install openai