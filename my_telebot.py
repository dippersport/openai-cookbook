# Burda biz bot duzeltdik . Open Ai suallara cavab verecek
import openai
import telebot

# Устанавливаем API ключ от OpenAI
openai.api_key = ("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")

# Инициализируем бота
bot = telebot.TeleBot("6325714808:AAEs6OYOzRqdY7hPnCblUABGHvmZHSPkldM")


# Обработчик команды /start
@bot.message_handler(commands=['start'])
def on_start(message):
    bot.reply_to(message, "Привет! Я бот, готовый отвечать на твои вопросы. Просто напиши мне что-нибудь.")

# Обработчик текстовых сообщений
@bot.message_handler(func=lambda message: True)
def on_text(message):
    user_text = message.text
    
    # Посылаем текст сообщения OpenAI для получения ответа на русском языке
    response = openai.Completion.create(
        engine="davinci",
        prompt=user_text,
        max_tokens=50,  # Максимальное количество символов в ответе
        temperature=0.2,  # Это может влиять на креативность ответов
        stop=None,  # Строка для завершения ответа, если не указывать, ответ будет длиннее
        language="ru"  # Указываем язык запроса как "ru" (русский)
    )
    
    # Получаем ответ от OpenAI
    ai_response = response.choices[0].text
    
    # Отправляем ответ пользователю
    bot.send_message(message.chat.id, ai_response)

if __name__ == '__main__':
    bot.polling()



#deactivate

#openai.api_key = "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"
#bot = telebot.TeleBot("6325714808:AAEs6OYOzRqdY7hPnCblUABGHvmZHSPkldM")
            
#pip uninstall telebot
#pip install pyTelegramBotAPI
#pip install translate
#pip install langdetect
#pip freeze
#pip install virtualenv
#pip install requests
#pip install pyTelegramBotAPI


#pip install -r requirements.txt

