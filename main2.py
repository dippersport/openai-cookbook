from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, filters, ConversationHandler, CallbackContext

# Состояния диалога
START, NAME, AGE, CITY, VACANCY, FINAL = range(6)

# Словарь для хранения данных пользователя
user_data = {}

# Начальная команда
def start(update: Update, context: CallbackContext):
    update.message.reply_text("Добро пожаловать! Я задам вам несколько вопросов. ")
    return START

# Обработка имени
def get_name(update: Update, context: CallbackContext):
    user = update.message.from_user
    user_data['name'] = update.message.text
    update.message.reply_text(f"Спасибо, {user_data['name']}!Первый вопрос: как вас зовут?")
    return NAME

# Обработка возраста
def get_age(update: Update, context: CallbackContext):
    user_data['age'] = update.message.text
    update.message.reply_text("Сколько вам лет?")
    return AGE

# Обработка города
def get_city(update: Update, context: CallbackContext):
    user_data['city'] = update.message.text
    update.message.reply_text("В каком городе планируете работать?")
    return CITY

# Обработка вакансии
def get_vacancy(update: Update, context: CallbackContext):
    user_data['vacancy'] = update.message.text
    update.message.reply_text("Какую вакансию выбираете?")
    return VACANCY

# Завершение диалога
def end(update: Update, context: CallbackContext):
    update.message.reply_text("Спасибо за ответы! Ожидайте, пока с вами свяжется менеджер.")
    return ConversationHandler.END

def main():
    # Замените 'YOUR_TOKEN' на токен вашего бота
    updater = Updater(token='6325714808:AAEs6OYOzRqdY7hPnCblUABGHvmZHSPkldM', use_context=True)

    dp = updater.dispatcher

    # Создание конверсации
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={
            NAME: [MessageHandler(Filters.text & ~Filters.command, get_name)],
            AGE: [MessageHandler(Filters.text & ~Filters.command, get_age)],
            CITY: [MessageHandler(Filters.text & ~Filters.command, get_city)],
            VACANCY: [MessageHandler(Filters.text & ~Filters.command, get_vacancy)],
            FINAL: [MessageHandler(Filters.text & ~Filters.command, end)],
        },
        fallbacks=[],
    )

    dp.add_handler(conv_handler)

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
#pip install python-telegram-bot
#pip install python-telegram-bot --upgrade
