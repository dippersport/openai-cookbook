import telebot

bot = telebot.TeleBot("6751801078:AAGCIMo3gpCy7uUVKlJNQRyKUOU1C__XwNk")

# Словарь для хранения ответов
answers = {}

# Обработка команды /start
@bot.message_handler(commands=['start'])
def get_start(message):
    answers[message.chat.id] = {}  # Создаем запись для нового пользователя
    bot.send_message(message.chat.id, "Привет! Давайте заполним анкету. Как вас зовут?")
    bot.register_next_step_handler(message, get_name)

# Обработка вопроса про имя
def get_name(message):
    chat_id = message.chat.id
    answers[chat_id]['name'] = message.text
    bot.send_message(chat_id, "Сколько вам лет?")
    bot.register_next_step_handler(message, get_age)

# Обработка вопроса про возраст
def get_age(message):
    chat_id = message.chat.id
    answers[chat_id]['age'] = message.text
    bot.send_message(chat_id, "В каком городе вы планируете работать?")
    bot.register_next_step_handler(message, get_city)

# Обработка вопроса о городе
def get_city(message):
    chat_id = message.chat.id
    answers[chat_id]['city'] = message.text
    bot.send_message(chat_id, "Какую вакансию вы выбираете?")
    bot.register_next_step_handler(message, get_vacancy)

# Обработка вопроса о выборе вакансии
def get_vacancy(message):
    chat_id = message.chat.id
    answers[chat_id]['vacancy'] = message.text
    bot.send_message(chat_id, "Ожидайте, пока с вами свяжется менеджер.")
    bot.register_next_step_handler(message, finish)

# Обработка завершения анкеты
def finish(message):
    chat_id = message.chat.id
    answers[chat_id]['contact'] = message.text

    # Сохраняем ответы или отправляем их куда-то
    # В данном примере, просто выводим ответы
    bot.send_message(chat_id, "Спасибо! Ваши ответы:\n" + str(answers[chat_id]))

# Запуск бота
if __name__ == '__main__':
    bot.polling(none_stop=True)




#6325714808:AAEs6OYOzRqdY7hPnCblUABGHvmZHSPkldM