import telebot 
from datetime import datetime
from database import *
from telebot import types
import time
import os


token = 'TOKEN'
bot = telebot.TeleBot(token)
tex = False
tconv = lambda x: time.strftime("%H:%M:%S %d.%m.%Y", time.localtime(x))

def main_menu():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    but1 = types.KeyboardButton('Профиль 👤')
    but2 = types.KeyboardButton('Доход/расход')
    but3 = types.KeyboardButton('Баланс')
    markup.add(but1, but2)
    markup.add(but3)
    return markup

def menu():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    but1 = types.KeyboardButton('Доход')
    but2 = types.KeyboardButton('Расход')
    but3 = types.KeyboardButton('Главная 🔙')
    but4 = types.KeyboardButton('Показать последний доход')
    but5 = types.KeyboardButton('Показать последний расход')
    markup.add(but1, but2)
    markup.add(but4, but5)
    markup.add(but3)
    return markup

def ang_main_menu():
     markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
     but1 = types.KeyboardButton('Profile 👤')
     but2 = types.KeyboardButton('Income/Expense')
     but3 = types.KeyboardButton('Balance')
     markup.add(but1, but2)
     markup.add(but3)
     return markup

def ang_menu():
     markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
     but1 = types.KeyboardButton('Income')
     but2 = types.KeyboardButton('Expense')
     but3 = types.KeyboardButton('Home 🔙')
     but4 = types.KeyboardButton('Show last income')
     but5 = types.KeyboardButton('Show last expense')
     markup.add(but1, but2)
     markup.add(but4, but5)
     markup.add(but3)
     return markup

def adm_menu():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    but1 = types.KeyboardButton('Рассылка')
    but2 = types.KeyboardButton('Техническое Обслуживание')
    but3 = types.KeyboardButton('Администраторы')
    but5 = types.KeyboardButton('Бан')
    but7 = types.KeyboardButton('Системное управление')
    but6 = types.KeyboardButton('Главная 🔙')
    markup.add(but1, but2, but3, but5, but7)
    markup.add(but6)
    return markup

def ang_adm_menu():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    but1 = types.KeyboardButton('Broadcast')
    but2 = types.KeyboardButton('Maintenance')
    but3 = types.KeyboardButton('Administrators')
    but5 = types.KeyboardButton('Ban')
    but7 = types.KeyboardButton('System control')
    but6 = types.KeyboardButton('Home 🔙')
    markup.add(but1, but2, but3, but5, but7)
    markup.add(but6)
    return markup

def TO_menu():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    but1 = types.KeyboardButton('/tex')
    but2 = types.KeyboardButton('/offtex')
    but3 = types.KeyboardButton('Назад 🔙')
    markup.add(but1, but2)
    markup.add(but3)
    return markup

def ang_TO_menu():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    but1 = types.KeyboardButton('/tex')
    but2 = types.KeyboardButton('/offtex')
    but3 = types.KeyboardButton('Back 🔙')
    markup.add(but1, but2)
    markup.add(but3)
    return markup

def admins():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    but1 = types.KeyboardButton('Добавить администратора')
    but2 = types.KeyboardButton('Убрать администратора')
    but3 = types.KeyboardButton('Назад 🔙')
    markup.add(but1, but2)
    markup.add(but3)
    return markup

def ang_admins():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    but1 = types.KeyboardButton('Add Administrator')
    but2 = types.KeyboardButton('Remove Administrator')
    but3 = types.KeyboardButton('Back 🔙')
    markup.add(but1, but2)
    markup.add(but3)
    return markup

def bans():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    but1 = types.KeyboardButton('Заблокировать')
    but2 = types.KeyboardButton('Разблокировать')
    but3 = types.KeyboardButton('Назад 🔙')
    markup.add(but1, but2)
    markup.add(but3)
    return markup

def ang_bans():
     markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
     but1 = types.KeyboardButton('Lock')
     but2 = types.KeyboardButton('Unlock')
     but3 = types.KeyboardButton('Back 🔙')
     markup.add(but1, but2)
     markup.add(but3)
     return markup

def exit():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    but1 = types.KeyboardButton('Назад')
    markup.add(but1)
    return markup

def ang_exit():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    but1 = types.KeyboardButton('Back')
    markup.add(but1)
    return markup

def exit_admin():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    but1 = types.KeyboardButton('Назад 🔙')
    markup.add(but1)
    return markup

def ang_exit_admin():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    but1 = types.KeyboardButton('Back 🔙')
    markup.add(but1)
    return markup

def next_msg(message):
    income_user = message.text
    user_id = message.from_user.id
    data = datetime.today()
    data = data.strftime("%d-%m-%Y")
    if chek_language(user_id=user_id) =='RU':
        if income_user == 'Назад' or income_user == 'назад' or income_user == '/exit':
            bot.send_message(message.chat.id, 'Введите команду', reply_markup=main_menu())
        elif not message.text.isnumeric():
            bot.send_message(message.chat.id, 'Для добавление дохода надо написать ЦИФРАМИ без букв')
            bot.register_next_step_handler(message, next_msg)
        else:
            add_income(user_id=user_id, income=income_user, data=data)
            bot.send_message(message.chat.id,'✅ Доход добавлен в базу', reply_markup=menu())
            bot.send_message(message.chat.id, f'Ваш баланс: {balance(user_id=user_id)}')
    elif chek_language(user_id=user_id) == 'ANG':
        if income_user == 'Back' or income_user == 'back' or income_user == '/exit':
            bot.send_message(message.chat.id, 'Enter command', reply_markup=main_menu())
        elif not message.text.isnumeric():
            bot.send_message(message.chat.id, 'To add income, write in NUMBERS without letters')
            bot.register_next_step_handler(message, next_msg)
        else:
            add_income(user_id=user_id, income=income_user, data=data)
            bot.send_message(message.chat.id,'✅ Income added to base', reply_markup=ang_menu())
            bot.send_message(message.chat.id, f'Your balance: {balance(user_id=user_id)}')
    else:
        bot.send_message(message.chat.id, 'Вы не выбрали язык! Вы не можете продолжить пользоваться ботом. Для выбора языка используйте /language\n\nYou have not selected a language! You cannot continue using the bot. Use /language to select a language')

def next_msg_ex(message):
    expense_user = message.text
    user_id = message.from_user.id
    data = datetime.today()
    data = data.strftime("%d-%m-%Y")
    if chek_language(user_id=user_id) == 'RU':
        if expense_user == 'Назад' or expense_user == 'назад' or expense_user == '/exit':
            bot.send_message(message.chat.id, 'Введите команду', reply_markup=main_menu())
        elif not message.text.isnumeric():
            bot.send_message(message.chat.id, 'Для добавление расхода надо написать ЦИФРАМИ без букв')
            bot.register_next_step_handler(message, next_msg)
        else:
            add_expense(user_id=user_id, expense=expense_user, data=data)
            bot.send_message(message.chat.id,'✅ Расход добавлен в базу', reply_markup=menu())
            bot.send_message(message.chat.id, f'Ваш баланс: {balance(user_id=user_id)}')
    elif chek_language(user_id=user_id) == 'ANG':
        if expense_user == 'Back' or expense_user == 'back' or expense_user == '/exit':
             bot.send_message(message.chat.id, 'Enter command', reply_markup=main_menu())
        elif not message.text.isnumeric():
            bot.send_message(message.chat.id, 'To add an expense, write in NUMBERS without letters')
            bot.register_next_step_handler(message, next_msg)
        else:
            add_expense(user_id=user_id, expense=expense_user, data=data)
            bot.send_message(message.chat.id,'✅ Consumption added to base', reply_markup=ang_menu())
            bot.send_message(message.chat.id, f'Your balance: {balance(user_id=user_id)}')
    else:
        bot.send_message(message.chat.id, 'Вы не выбрали язык! Вы не можете продолжить пользоваться ботом. Для выбора языка используйте /language\n\nYou have not selected a language! You cannot continue using the bot. Use /language to select a language')

def add_msg(message):
    user_id = message.text
    user_adm = message.from_user.id
    if chek_language(user_id=user_adm) == 'RU':
        if user_id == 'Назад 🔙' or user_id == 'назад 🔙':
            bot.send_message(message.chat.id, 'Введите команду', reply_markup=adm_menu())
        elif not message.text.isnumeric():
            bot.send_message(message.chat.id, 'Для добавление администратора нужно написать его ID telegram (состоящий из цифр)')
            bot.register_next_step_handler(message, add_msg)
        else:
            add_admin(user_id=user_id)
            bot.send_message(message.chat.id,'✅ Администратор добавлен.')
            if chek_language(user_id=user_id) == 'RU':
                bot.send_message(user_id, '❗️ Вас поставили администратором бота. Поздравляем!')
            else:
                bot.send_message(user_id, '❗️ You have been made a bot administrator. Congratulations!')
    else:
        if user_id == 'Back 🔙' or user_id == 'back 🔙':
            bot.send_message(message.chat.id, 'Enter command', reply_markup=ang_adm_menu())
        elif not message.text.isnumeric():
            bot.send_message(message.chat.id, 'To add an administrator, you need to write his telegram ID (consisting of numbers)')
            bot.register_next_step_handler(message, add_msg)
        else:
            add_admin(user_id=user_id)
            bot.send_message(message.chat.id,'✅ Administrator added.')
            if chek_language(user_id=user_id) == 'RU':
                bot.send_message(user_id, '❗️ Вас поставили администратором бота. Поздравляем!')
            else:
                bot.send_message(user_id, '❗️ You have been made a bot administrator. Congratulations!')

def clr_msg(message):
    user_id = message.text
    user_adm = message.from_user.id
    if chek_language(user_id=user_adm) == 'RU':
        if user_id == 'Назад 🔙' or user_id == 'назад 🔙':
            bot.send_message(message.chat.id, 'Введите команду', reply_markup=adm_menu())
        elif not message.text.isnumeric():
            bot.send_message(message.chat.id, 'Для удаление администратора нужно написать его ID telegram (состоящий из цифр)')
            bot.register_next_step_handler(message, clr_msg)
        else:
            clr_admin(user_id=user_id)
            bot.send_message(message.chat.id,'✅ Администратор удален.')
            if chek_language(user_id=user_id) == 'RU':
                bot.send_message(user_id, '❗️ Вас убрали из администраторов бота.')
            else:
                bot.send_message(user_id, '❗️ You have been removed from the bot admin.')
    else:
        if user_id == 'Back 🔙' or user_id == 'back 🔙':
            bot.send_message(message.chat.id, 'Enter command', reply_markup=adm_menu())
        elif not message.text.isnumeric():
            bot.send_message(message.chat.id, 'To delete an administrator, you need to write his telegram ID (consisting of numbers)')
            bot.register_next_step_handler(message, clr_msg)
        else:
            clr_admin(user_id=user_id)
            bot.send_message(message.chat.id,'✅ Administrator deleted.')
            if chek_language(user_id=user_id) == 'RU':
                bot.send_message(user_id, '❗️ Вас убрали из администраторов бота.')
            else:
                bot.send_message(user_id, '❗️ You have been removed from the bot admin.')

def ban_msg(message):
    user_id = message.text
    user_adm = message.from_user.id
    if chek_language(user_id=user_adm) == 'RU':
        if user_id == 'Назад 🔙' or user_id == 'назад 🔙':
            bot.send_message(message.chat.id, 'Введите команду', reply_markup=adm_menu())
        elif not message.text.isnumeric():
            bot.send_message(message.chat.id, 'Для добавление пользователя в бан нужно написать его ID telegram (состоящий из цифр)')
            bot.register_next_step_handler(message, ban_msg)
        else:
            ban_admin(user_id=user_id)
            bot.send_message(message.chat.id,'✅ Вы заблокировали человека.')
            if chek_language(user_id=user_id) == 'RU':
                bot.send_message(user_id, '❗️ Вас заблокировали в боте.')
            else:
                bot.send_message(user_id, '❗️ You have been blocked in the bot.')
    else:
        if user_id == 'Back 🔙' or user_id == 'back 🔙':
            bot.send_message(message.chat.id, 'Enter command', reply_markup=adm_menu())
        elif not message.text.isnumeric():
            bot.send_message(message.chat.id, 'To add a user to the ban, you need to write his telegram ID (consisting of numbers)')
            bot.register_next_step_handler(message, ban_msg)
        else:
            ban_admin(user_id=user_id)
            bot.send_message(message.chat.id,'✅ You blocked the person.')
            if chek_language(user_id=user_id) == 'RU':
                bot.send_message(user_id, '❗️ Вас заблокировали в боте.')
            else:
                bot.send_message(user_id, '❗️ You have been blocked in the bot.')


def clr_ban_msg(message):
    user_id = message.text
    if chek_language(user_id=user_id) == 'RU':
        if user_id == 'Назад 🔙' or user_id == 'назад 🔙':
            bot.send_message(message.chat.id, 'Введите команду', reply_markup=adm_menu())
        elif not message.text.isnumeric():
            bot.send_message(message.chat.id, 'Для снятие бана с пользователя нужно написать его ID telegram (состоящий из цифр)')
            bot.register_next_step_handler(message, clr_ban_msg)
        else:
            clr_ban_admin(user_id=user_id)
            bot.send_message(message.chat.id,'✅ Вы разблокировали человека.')
            if chek_language(user_id=user_id) == 'RU':
                bot.send_message(user_id, '❗️ Вас разблокировали в боте. Поздравляем!')
            else:
                bot.send_message(user_id, '❗️ You have been unblocked in the bot. Congratulations!')
    else:
        if user_id == 'Back 🔙' or user_id == 'back 🔙':
            bot.send_message(message.chat.id, 'Enter command', reply_markup=adm_menu())
        elif not message.text.isnumeric():
            bot.send_message(message.chat.id, 'To remove a ban from a user, you need to write his telegram ID (consisting of numbers)')
            bot.register_next_step_handler(message, clr_ban_msg)
        else:
            clr_ban_admin(user_id=user_id)
            bot.send_message(message.chat.id,'✅ You unblocked the person.')
            if chek_language(user_id=user_id) == 'RU':
                bot.send_message(user_id, '❗️ Вас разблокировали в боте. Поздравляем!')
            else:
                bot.send_message(user_id, '❗️ You have been unblocked in the bot. Congratulations!')

def mailings_msg(message):
    global mail
    msg = message.text
    user_adm = message.from_user.id
    if chek_language(user_id=user_adm) == 'RU':
        if msg == 'Назад 🔙' or msg == 'Назад 🔙':
            bot.send_message(message.chat.id, 'Введите команду', reply_markup=adm_menu())
        else:
            mail = mailings()
            bot.send_message(mail, msg)
            bot.send_message(message.chat.id, '✉️ Сообщение отправлено всем пользователем.')
    else:
        if msg == 'Back 🔙' or msg == 'back 🔙':
            bot.send_message(message.chat.id, 'Enter command', reply_markup=adm_menu())
        else:
            mail = mailings()
            bot.send_message(mail, msg)
            bot.send_message(message.chat.id, '✉️ Message sent by all user.')

@bot.callback_query_handler(func=lambda call: True)
def query_handler(call):
    user_id = call.from_user.id
    if chek_language(user_id=user_id) == 'RU':
        if tex == False:
            bot.answer_callback_query(callback_query_id=call.id, text = 'Выполнение операции...\nЗавершение выполнение операции через 5 секунд!')
            time.sleep(5)
            if call.data == '1004':
                bot.send_message(call.message.chat.id, 'Вы успешно остановили бота. Запуск бота только через Системного Администратора!!!')
                bot.stop_polling()
            elif call.data == '1005':
                bot.send_message(call.message.chat.id, 'Вы успешно удалили финансы из базы данных! Вернуть их невозможно.')
                delete_fin(user_id=user_id)
            elif call.data == '1006':
                stopping_markup = types.InlineKeyboardMarkup()
                but = types.InlineKeyboardButton(text='✅ Подтвердить остановку бота', callback_data=1004)
                stopping_markup.add(but)
                bot.send_message(call.message.chat.id, 'Вы уверены что хотите остановить бота? Если Вы остановите бота, то запустить его можно только через Системного Администратора!!!', reply_markup=stopping_markup)
            elif call.data == '1007':
                try:
                    file = open('logs.txt', 'rb')
                    bot.send_document(call.message.chat.id, file)
                except FileNotFoundError:
                    bot.send_message(call.message.chat.id, 'На данный  момент логов нет.')
            elif call.data == '1008':
                try:
                    os.remove(os.path.join('logs.txt'))
                    bot.send_message(call.message.chat.id, 'Файл удален из системы. Возращение файла не возможно!')
                except FileNotFoundError:
                    bot.send_message(call.message.chat.id, 'Нет файла с логами.')
            elif call.data == '1009':
                bot.send_message(call.message.chat.id, '✅ Язык выбран!')
                set_language(user_id=user_id, language='RU')
                bot.send_message(call.message.chat.id, 'Приветствую Вас, {0.first_name}, в боте по учету финансов. Бот работает для Вас круглосуточно и не сбрасывая никаких данных, даже после удаления данного чата – все данные сохранятся.\nПродолжая использование бота, Вы подписываете согласие на обработку и хранение ваших персональных данных.\nУтечка данных не происходит, с каждым обновлением бота наши разработчики пытаются улучшить работу и защиту бота.\nДля того чтобы узнать подробнее о боте, Вы можете прописать команду /help, а также для того, чтобы узнать список команд, которые доступны именно Вам - пропишите команду “команды” без скобочек.\n\nПриятного использование бота.'.format(call.message.from_user), reply_markup=main_menu())
                time.sleep(3)
            elif call.data == '1010':
                bot.send_message(call.message.chat.id, '✅ Language selected!')
                set_language(user_id=user_id, language='ANG')
                bot.send_message(call.message.chat.id, 'Welcome, {0.first_name}, to the finance accounting bot. The bot works for you around the clock and does not drop any data, even after deleting this chat, all data will be saved.\nBy continuing to use the bot, you sign consent to the processing and storage of your personal data.\nData leakage does not occur, with each update of the bot, our developers try improve the work and protection of the bot.\nTo learn more about the bot, you can type the /help command, and to find out the list of commands that are available to you, type the “commands” command without parentheses.\n\nEnjoy using bot.'.format(call.message.from_user), reply_markup=main_menu())
            elif call.data == '1011':
                set_language(user_id=user_id, language='RU')
                bot.send_message(call.message.chat.id, '✅ Язык выбран!')
            elif call.data == '1012':
                set_language(user_id=user_id, language='ANG')
                bot.send_message(call.message.chat.id, '✅ Language selected!')
        else:
            bot.send_message(call.message.chat.id, '⚠️ Приносим свои извинения, но бот отправлен на Техническое Обслуживание, по каким-либо причинам. Ожидайте новостей от команды проекта, либо включения бота. На момент обслуживание бота Вы не можете его использовать, при попытке использовать бота, Вам будет возращено сообщение об ошибке. Наберитесь терпения. Просим прошения! Всего хорошего.')
    elif chek_language(user_id=user_id) == 'ANG':
        if tex == False:
            bot.answer_callback_query(callback_query_id=call.id, text = 'Operation in progress...\nCompletion of operation in 5 seconds!')
            time.sleep(5)
            if call.data == '1004':
                bot.send_message(call.message.chat.id, 'You have successfully stopped the bot. Launching the bot only through the System Administrator!!!')
                bot.stop_polling()
            elif call.data == '1005':
                bot.send_message(call.message.chat.id, 'You have successfully deleted finances from the database! It is impossible to return them.')
                delete_fin(user_id=user_id)
            elif call.data == '1006':
                stopping_markup = types.InlineKeyboardMarkup()
                but = types.InlineKeyboardButton(text='✅ Confirm bot stop', callback_data=1004)
                stopping_markup.add(but)
                bot.send_message(call.message.chat.id, 'Confirm Bot StopAre you sure you want to stop the bot? If you stop the bot, then you can start it only through the System Administrator!!!', reply_markup=stopping_markup)
            elif call.data == '1007':
                try:
                    file = open('logs.txt', 'rb')
                    bot.send_document(call.message.chat.id, file)
                except FileNotFoundError:
                    bot.send_message(call.message.chat.id, 'There are currently no logs.')
            elif call.data == '1008':
                try:
                    os.remove(os.path.join('logs.txt'))
                    bot.send_message(call.message.chat.id, 'The file has been removed from the system. Returning the file is not possible!')
                except FileNotFoundError:
                    bot.send_message(call.message.chat.id, 'There is no log file.')
            elif call.data == '1009':
                bot.send_message(call.message.chat.id, '✅ Язык выбран!')
                set_language(user_id=user_id, language='RU')
                bot.send_message(call.message.chat.id, 'Приветствую Вас, {0.first_name}, в боте по учету финансов. Бот работает для Вас круглосуточно и не сбрасывая никаких данных, даже после удаления данного чата – все данные сохранятся.\nПродолжая использование бота, Вы подписываете согласие на обработку и хранение ваших персональных данных.\nУтечка данных не происходит, с каждым обновлением бота наши разработчики пытаются улучшить работу и защиту бота.\nДля того чтобы узнать подробнее о боте, Вы можете прописать команду /help, а также для того, чтобы узнать список команд, которые доступны именно Вам - пропишите команду “команды” без скобочек.\n\nПриятного использование бота.'.format(call.message.from_user), reply_markup=main_menu())
                time.sleep(3)
            elif call.data == '1010':
                bot.send_message(call.message.chat.id, '✅ Language selected!')
                set_language(user_id=user_id, language='ANG')
                bot.send_message(call.message.chat.id, 'Welcome, {0.first_name}, to the finance accounting bot. The bot works for you around the clock and does not drop any data, even after deleting this chat, all data will be saved.\nBy continuing to use the bot, you sign consent to the processing and storage of your personal data.\nData leakage does not occur, with each update of the bot, our developers try improve the work and protection of the bot.\nTo learn more about the bot, you can type the /help command, and to find out the list of commands that are available to you, type the “commands” command without parentheses.\n\nEnjoy using bot.'.format(call.message.from_user), reply_markup=main_menu())
            elif call.data == '1011':
                set_language(user_id=user_id, language='RU')
                bot.send_message(call.message.chat.id, '✅ Язык выбран!')
            elif call.data == '1012':
                set_language(user_id=user_id, language='ANG')
                bot.send_message(call.message.chat.id, '✅ Language selected!')
        else:
            bot.send_message(call.message.chat.id, '⚠️ We apologize, but the bot has been sent for Maintenance, for some reason. Expect news from the project team, or the inclusion of a bot. At the time of the bot maintenance, you cannot use it, if you try to use the bot, an error message will be returned to you. Be patient. We apologize! Good luck.')
    else:
        if tex == False:
            bot.answer_callback_query(callback_query_id=call.id, text = 'Выполнение операции...\nЗавершение выполнение операции через 5 секунд!\n\nOperation in progress...\nCompletion of operation in 5 seconds!')
            time.sleep(5)
            if call.data == '1004':
                bot.send_message(call.message.chat.id, 'Вы успешно остановили бота. Запуск бота только через Системного Администратора!!!\nYou have successfully stopped the bot. Launching the bot only through the System Administrator!!!')
                bot.stop_polling()
            elif call.data == '1005':
                bot.send_message(call.message.chat.id, 'Вы успешно удалили финансы из базы данных! Вернуть их невозможно.\nYou have successfully deleted finances from the database! It is impossible to return them.')
                delete_fin(user_id=user_id)
            elif call.data == '1006':
                stopping_markup = types.InlineKeyboardMarkup()
                but = types.InlineKeyboardButton(text='✅ Подтвердить остановку бота\nConfirm bot stop', callback_data=1004)
                stopping_markup.add(but)
                bot.send_message(call.message.chat.id, 'Вы уверены что хотите остановить бота? Если Вы остановите бота, то запустить его можно только через Системного Администратора!!!\nConfirm Bot StopAre you sure you want to stop the bot? If you stop the bot, then you can start it only through the System Administrator!!!', reply_markup=stopping_markup)
            elif call.data == '1007':
                try:
                    file = open('logs.txt', 'rb')
                    bot.send_document(call.message.chat.id, file)
                except FileNotFoundError:
                    bot.send_message(call.message.chat.id, 'На данный  момент логов нет.\nThere are currently no logs.')
            elif call.data == '1008':
                try:
                    os.remove(os.path.join('logs.txt'))
                    bot.send_message(call.message.chat.id, 'Файл удален из системы. Возращение файла не возможно!\nThe file has been removed from the system. Returning the file is not possible!')
                except FileNotFoundError:
                    bot.send_message(call.message.chat.id, 'Нет файла с логами.\nThere is no log file.')
            elif call.data == '1009':
                bot.send_message(call.message.chat.id, '✅ Язык выбран!')
                set_language(user_id=user_id, language='RU')
                bot.send_message(call.message.chat.id, 'Приветствую Вас, {0.first_name}, в боте по учету финансов. Бот работает для Вас круглосуточно и не сбрасывая никаких данных, даже после удаления данного чата – все данные сохранятся.\nПродолжая использование бота, Вы подписываете согласие на обработку и хранение ваших персональных данных.\nУтечка данных не происходит, с каждым обновлением бота наши разработчики пытаются улучшить работу и защиту бота.\nДля того чтобы узнать подробнее о боте, Вы можете прописать команду /help, а также для того, чтобы узнать список команд, которые доступны именно Вам - пропишите команду “команды” без скобочек.\n\nПриятного использование бота.'.format(call.message.from_user), reply_markup=main_menu())
                time.sleep(3)
            elif call.data == '1010':
                bot.send_message(call.message.chat.id, '✅ Language selected!')
                set_language(user_id=user_id, language='ANG')
                bot.send_message(call.message.chat.id, 'Welcome, {0.first_name}, to the finance accounting bot. The bot works for you around the clock and does not drop any data, even after deleting this chat, all data will be saved.\nBy continuing to use the bot, you sign consent to the processing and storage of your personal data.\nData leakage does not occur, with each update of the bot, our developers try improve the work and protection of the bot.\nTo learn more about the bot, you can type the /help command, and to find out the list of commands that are available to you, type the “commands” command without parentheses.\n\nEnjoy using bot.'.format(call.message.from_user), reply_markup=main_menu())
            elif call.data == '1011':
                set_language(user_id=user_id, language='RU')
                bot.send_message(call.message.chat.id, '✅ Язык выбран!')
            elif call.data == '1012':
                set_language(user_id=user_id, language='ANG')
                bot.send_message(call.message.chat.id, '✅ Language selected!')
        else:
            bot.send_message(call.message.chat.id, '⚠️ Приносим свои извинения, но бот отправлен на Техническое Обслуживание, по каким-либо причинам. Ожидайте новостей от команды проекта, либо включения бота. На момент обслуживание бота Вы не можете его использовать, при попытке использовать бота, Вам будет возращено сообщение об ошибке. Наберитесь терпения. Просим прошения! Всего хорошего.\nWe apologize, but the bot has been sent for Maintenance, for some reason. Expect news from the project team, or the inclusion of a bot. At the time of the bot maintenance, you cannot use it, if you try to use the bot, an error message will be returned to you. Be patient. We apologize! Good luck.')


@bot.message_handler(commands = ['start'])
def start(message):
    file = open('logs.txt', 'a')
    file.write(f'Новвый ввод: ID: {message.from_user.id}, NAME: {message.from_user.first_name}, USER_NAME: {message.from_user.username}, DATA: {tconv(message.date)}, TEXT: {message.text} \n')
    file.close()
    user_id = message.from_user.id
    if tex == False:
        try:
            user_id = message.from_user.id
            user_name = message.from_user.first_name
            data = datetime.today()
            data = data.strftime("%d-%m-%Y")
            add_user(user_id=user_id, user_name=user_name, data=data)
            language_markup = types.InlineKeyboardMarkup(row_width=1)
            but1 = types.InlineKeyboardButton(text='🇷🇺  Русский (RUS)', callback_data=1009)
            but2 = types.InlineKeyboardButton(text='🇺🇸 English (ENG)', callback_data=1010)
            language_markup.add(but1, but2)
            bot.send_message(message.chat.id, 'Выбирите язык для дальнейшей работы с ним.\nSelect a language for further work with it.', reply_markup=language_markup)
        except sqlite3.IntegrityError:
            if chek_language(user_id=user_id) == 'RU':
                bot.send_message(message.chat.id, '⚠️ Вы уже зарегистрированы в боте.')
            elif chek_language(user_id=user_id) == 'ANG':
                bot.send_message(message.chat.id, '⚠️ You are already registered in the bot.')
            else:
                bot.send_message(message.chat.id, 'Вы не выбрали язык! Вы не можете продолжить пользоваться ботом. Для выбора языка используйте /language\n\nYou have not selected a language! You cannot continue using the bot. Use /language to select a language')
    else:
        bot.send_message(message.chat.id, '⚠️ Извините, бот отправлен на техническое обслуживание!\n ⚠️ Sorry, the bot has been sent for maintenance!')

@bot.message_handler(commands=['help'])
def help(message):
    file = open('logs.txt', 'a', encoding="utf-8")
    file.write(f'Новый ввод: ID: {message.from_user.id}, NAME: {message.from_user.first_name}, USER_NAME: {message.from_user.username}, DATA: {tconv(message.date)}, TEXT: {message.text} \n')
    file.close()
    user_id = message.from_user.id
    if tex == False:
        if chek_ban(user_id=user_id) == 'False':
            if chek_language(user_id=user_id) == 'RU':
                bot.send_message(message.chat.id, 'Дорогой пользователь, благодорим Вас что заинтересовались нашим продуктом. Бот создан исключительно для удобства людей, учитывать их доход и расход. С каждым обновлением бот становиться все лучше и лучше, мы стараемся для ВАС! Все данные (имя, id, user, доход, расход, баланс) будут сохранятся в базу данных данного бота и дальше этого бота и рук команды проекта не уходят. Также команда разработчиков, которая трудится над этим ботом с каждым разом усиливает безопасность нашего продукта. Вы можете не переживать, что Ваши данные попадут в чужие руки и будут использоваться в дальнейшем. \nЕсли у Вас есть предложение по данному проекту, либо же по реализации нового проекта напишите пожалуйста нам  на почту: dimongamedeveloper@yandex.ru, либо в сообществе нашей компании: В разработке. ', reply_markup=main_menu())
                time.sleep(3)
            elif chek_language(user_id=user_id) == 'ANG':
                bot.send_message(message.chat.id, "Dear user, thank you for being interested in our product. The bot was created solely for the convenience of people, taking into account their income and expense. With each update, the bot is getting better and better, we are trying for YOU! All data (name, id, user, income, expense, balance) will be stored in the database of this bot and then this bot and the hands of the project team do not go away. Also, the development team that is working on this bot is strengthening the security of our product every time. You don't have to worry that your data will fall into the wrong hands and will be used in the future. \n If you have a proposal for this project, or for the implementation of a new project, please write to us by email: dimongamedeveloper@yandex.ru , or in the community of our company: In development.", reply_markup=main_menu())
                time.sleep(3)
            else:
                bot.send_message(message.chat.id, 'Вы не выбрали язык! Вы не можете продолжить пользоваться ботом. Для выбора языка используйте /language\n\nYou have not selected a language! You cannot continue using the bot. Use /language to select a language')
        else:
            if chek_language(user_id=user_id) == 'RU':
                bot.send_message(message.chat.id, '❗️ Вы заблокированы в данном боте. Вы не можете им пользоваться')
                time.sleep(3)
            elif chek_language(user_id=user_id) == 'ANG':
                bot.send_message(message.chat.id, "❗️ You are blocked in this bot. You can't use it")
                time.sleep(3)
            else:
                bot.send_message(message.chat.id, 'Вы не выбрали язык! Вы не можете продолжить пользоваться ботом. Для выбора языка используйте /language\n\nYou have not selected a language! You cannot continue using the bot. Use /language to select a language')
    else:
        if chek_language(user_id=user_id) == 'RU':
            bot.send_message(message.chat.id, '⚠️ Приносим свои извинения, но бот отправлен на Техническое Обслуживание, по каким-либо причинам. Ожидайте новостей от команды проекта, либо включения бота. На момент обслуживание бота Вы не можете его использовать, при попытке использовать бота, Вам будет возращено сообщение об ошибке. Наберитесь терпения. Просим прошения! Всего хорошего.')
        elif chek_language(user_id=user_id) == 'ANG':
            bot.send_message(message.chat.id, '⚠️ We apologize, but the bot has been sent for Maintenance, for some reason. Expect news from the project team, or the inclusion of a bot. At the time of the bot maintenance, you cannot use it, if you try to use the bot, an error message will be returned to you. Be patient. We ask for your forgiveness! Good luck.')
        else:
            bot.send_message(message.chat.id, 'Вы не выбрали язык! Вы не можете продолжить пользоваться ботом. Для выбора языка используйте /language\n\nYou have not selected a language! You cannot continue using the bot. Use /language to select a language')

@bot.message_handler(commands=['admlogin'])
def admlogin(message):
    file = open('logs.txt', 'a')
    file.write(f'Новвый ввод: ID: {message.from_user.id}, NAME: {message.from_user.first_name}, USER_NAME: {message.from_user.username}, DATA: {tconv(message.date)}, TEXT: {message.text} \n')
    file.close()
    user_id = message.from_user.id
    if chek_ban(user_id=user_id) == 'False':
        if chek_admin(user_id=user_id) == 'True':
            bot.send_message(message.chat.id, '🔑 Вы авторизовались в админ-панели. {0.first_name}, соблюдайте правила бота.'.format(message.from_user), reply_markup=adm_menu())
        else:
            if chek_language(user_id=user_id) == 'RU':
                bot.send_message(message.chat.id, '🚫 Вы не администратор. Вы не можете авторизоваться в админ-панели!')
            else:
                bot.send_message(message.chat.id, '🚫 You are not an administrator. You cannot log in to the admin panel!')
    else:
        bot.send_message(message.chat.id, '❗️ Вы заблокированы в данном боте. Вы не можете им пользоваться')

@bot.message_handler(commands=['tex'])
def tex(message):
    file = open('logs.txt', 'a')
    file.write(f'Новвый ввод: ID: {message.from_user.id}, NAME: {message.from_user.first_name}, USER_NAME: {message.from_user.username}, DATA: {tconv(message.date)}, TEXT: {message.text} \n')
    file.close()
    global tex
    user_id = message.from_user.id
    if chek_ban(user_id=user_id) == 'False':
        if chek_admin(user_id=user_id) == 'True':
            tex = True
            bot.send_message(message.chat.id, '✅ Вы поставили бота на Техническое Обслуживание... Для снятие бота с ТО пропишите /offtex')
        else:
            if chek_language(user_id=user_id) == 'RU':
                bot.send_message(message.chat.id, '🚫 Вы не администратор. У Вас нет прав доступа!')
            else:
                bot.send_message(message.chat.id, "🚫 You are not an administrator. You don't have access rights!")
    else:
        bot.send_message(message.chat.id, '❗️ Вы заблокированы в данном боте. Вы не можете им пользоваться')

@bot.message_handler(commands=['offtex'])
def offtex(message):
    file = open('logs.txt', 'a')
    file.write(f'Новвый ввод: ID: {message.from_user.id}, NAME: {message.from_user.first_name}, USER_NAME: {message.from_user.username}, DATA: {tconv(message.date)}, TEXT: {message.text} \n')
    file.close()
    global tex
    user_id = message.from_user.id
    if chek_ban(user_id=user_id) == 'False':
        if chek_admin(user_id=user_id) == 'True':
            tex = False
            bot.send_message(message.chat.id, '✅ Вы сняли бота с Технического Обслуживания.')
        else:
            if chek_language(user_id=user_id) == 'RU':
                bot.send_message(message.chat.id, '🚫 Вы не администратор. У Вас нет прав доступа!')
            else:
                bot.send_message(message.chat.id, "🚫 You are not an administrator. You don't have access rights!")
    else:
        bot.send_message(message.chat.id, '❗️ Вы заблокированы в данном боте. Вы не можете им пользоваться')

@bot.message_handler(commands=['language'])
def language(message):
    global tex
    user_id = message.from_user.id
    if tex == False:
        if chek_user(user_id=user_id) == 'True':
            if chek_ban(user_id=user_id) == 'False':
                file = open('logs.txt', 'a', encoding='utf-8')
                file.write(f'Новый ввод: ID: {message.from_user.id}, NAME: {message.from_user.first_name}, USER_NAME: {message.from_user.username}, DATA: {tconv(message.date)}, TEXT: {message.text} \n')
                language = types.InlineKeyboardMarkup(row_width=1)
                but1 = types.InlineKeyboardButton(text='🇷🇺 Русский (RUS)', callback_data=1011)
                but2 = types.InlineKeyboardButton(text='🇺🇸 English (ANG)', callback_data=1012)
                language.add(but1, but2)
                bot.send_message(message.chat.id, 'Для того чтобы изменить язык нужна выбрать в низу подходяшию кнопку.\n\nIn order to change the language, you need to select the appropriate button at the bottom.', reply_markup=language)
            else:
                if chek_language(user_id=user_id) == 'RU':
                    bot.send_message(message.chat.id, '❗️ Вы заблокированы в данном боте. Вы не можете им пользоваться')
                    time.sleep(3)
                else:
                    bot.send_message(message.chat.id, "❗️ You are blocked in this bot. You can't use it")
                    time.sleep(3)
        else:
            bot.send_message(message.chat.id, '⚠️ Вы не зарегистрированы!\nYou are not registered!')
            time.sleep(3)
    else:
        bot.send_message(message.chat.id, '⚠️ Извините, бот отправлен на техническое обслуживание!\n ⚠️ Sorry, the bot has been sent for maintenance!')
    
@bot.message_handler(content_types = ['text'])
def bot_message(message):
    file = open('logs.txt', 'a', encoding='utf-8')
    file.write(f'Новый ввод: ID: {message.from_user.id}, NAME: {message.from_user.first_name}, USER_NAME: {message.from_user.username}, DATA: {tconv(message.date)}, TEXT: {message.text} \n')
    global tex
    user_id = message.from_user.id
    if tex == False:
        if chek_user(user_id=user_id) == 'True':
            if chek_ban(user_id=user_id) == 'False':
                if chek_language(user_id=user_id) == 'RU':
                    if message.text == 'Доход' or message.text == 'доход' or message.text == '/inc':
                        bot.send_message(message.chat.id, 'Отправте сообщение ЦИФРАМИ о Вашем доходе', reply_markup=exit())
                        bot.register_next_step_handler(message, next_msg)
                    elif message.text == 'Расход' or message.text == 'расход' or message.text == '/cost':
                        bot.send_message(message.chat.id, 'Отправте сообщение ЦИФРАМИ о Вашем расходе', reply_markup=exit())
                        bot.register_next_step_handler(message, next_msg_ex)
                    elif message.text == 'Баланс' or message.text == 'баланс' or message.text == '/balance':
                        try:
                            bot.send_message(message.chat.id, f'Ваш баланс с учетом всех доходов и расходов: {balance(user_id=user_id)} рублей', reply_markup=main_menu())
                            time.sleep(3)
                        except TypeError:
                            bot.send_message(message.chat.id, '⚠️ Извините, произошла ошибка')
                            time.sleep(3)
                    elif message.text == 'Профиль 👤' or message.text == 'Профиль' or message.text == 'профиль' or message.text == '/prof':
                        name = '{0.first_name}'.format(message.from_user)
                        bot.send_message(message.chat.id, f'📊 Ваш профиль:\n\n👤 Ваше имя: {name}\n🖥  Ваш Telegram ID: {message.from_user.id}\n🖥  Ваш username: @{message.from_user.username}\nРегестрация в боте: {data_reg(user_id=user_id)}\nБлокировка в боте: {chek_ban(user_id=user_id)}\nАдминистратор бота: {chek_admin(user_id=user_id)}\nВаш баланс: {balance(user_id=user_id)}', reply_markup=main_menu())
                        time.sleep(3)
                    elif message.text == 'Доход/расход':
                        bot.send_message(message.chat.id, 'Выбирете из предложенных кнопок действие... ', reply_markup=menu())
                        time.sleep(3) 
                    elif message.text == 'Показать последний доход' or message.text == 'показать последний доход' or message.text == '/last_inc':
                        bot.send_message(message.chat.id, f'Последний доход был добавлен: {data_income(user_id=user_id)}\nСумма последнего дохода: {last_income(user_id=user_id)}', reply_markup=menu())
                        time.sleep(3)
                    elif message.text == 'Показать последний расход' or message.text == 'показать последний расход' or message.text == '/last_cost':
                        bot.send_message(message.chat.id, f'Последний расход был добавлен: {data_expense(user_id=user_id)}\nСумма последнего расхода: {last_expense(user_id=user_id)}', reply_markup=menu())
                        time.sleep(3)
                    elif message.text == 'Главная 🔙':
                        bot.send_message(message.chat.id, 'Вы в главном меню', reply_markup=main_menu())
                        time.sleep(3)
                    elif message.text == 'Рассылка' or message.text == 'рассылка' or message.text == '/mailing':
                        if chek_admin(user_id=user_id) == 'True':
                            bot.send_message(message.chat.id, 'Напишите сообщение которое будет отправлено всем пользователем бота...', reply_markup=exit_admin())
                            bot.register_next_step_handler(message, mailings_msg)
                        else:
                            bot.send_message(message.chat.id, '🚫 Вы не администратор. У Вас нет прав доступа!')
                            time.sleep(3)
                    elif message.text == 'Техническое Обслуживание' or message.text == 'техническое обслуживание':
                        if chek_admin(user_id=user_id) == 'True':
                            bot.send_message(message.chat.id, 'Вы в панели Технического Обслуживания бота. Управление ниже', reply_markup=TO_menu())
                        else:
                            bot.send_message(message.chat.id, '🚫 Вы не администратор. У Вас нет прав доступа!')
                            time.sleep(3)
                    elif message.text == 'Администраторы' or message.text == 'администраторы':
                        if chek_admin(user_id=user_id) == 'True':
                            bot.send_message(message.chat.id, 'Вы в панели управления администраторами. Управление ниже.', reply_markup=admins())
                        else:
                            bot.send_message(message.chat.id, '🚫 Вы не администратор. У Вас нет прав доступа!')
                            time.sleep(3)
                    elif message.text == 'Бан' or message.text == 'Бан':
                        if chek_admin(user_id=user_id) == 'True':
                            bot.send_message(message.chat.id, 'Вы в панели управления блокировок. Управление ниже.', reply_markup=bans())
                        else:
                            bot.send_message(message.chat.id, '🚫 Вы не администратор. У Вас нет прав доступа!')
                            time.sleep(3)
                    elif message.text == 'Назад 🔙' or message.text == 'назад 🔙':
                        if chek_admin(user_id=user_id) == 'True':
                            bot.send_message(message.chat.id, 'Вы в админ-панели. Управление ниже.', reply_markup=adm_menu())
                        else:
                            bot.send_message(message.chat.id, '🚫 Вы не администратор. У Вас нет прав доступа!')
                            time.sleep(3)
                    elif message.text == 'Добавить администратора' or message.text == 'добавить администратора' or message.text == '/setadmin':
                        if chek_admin(user_id=user_id) == 'True':
                            bot.send_message(message.chat.id, 'Напишите user_id человека кого хотите добавит в администраторы...', reply_markup=exit_admin())
                            bot.register_next_step_handler(message, add_msg)
                        else:
                            bot.send_message(message.chat.id, '🚫 Вы не администратор. У Вас нет прав доступа!')
                            time.sleep(3)
                    elif message.text == 'Убрать администратора' or message.text == 'убрать администратора' or message.text == '/unadmin':
                        if chek_admin(user_id=user_id) == 'True':
                            bot.send_message(message.chat.id, 'Напишите user_id человека кого хотите убрать из администраторов...', reply_markup=exit_admin())
                            bot.register_next_step_handler(message, clr_msg)
                        else:
                            bot.send_message(message.chat.id, '🚫 Вы не администратор. У Вас нет прав доступа!')
                            time.sleep(3)
                    elif message.text == 'Заблокировать' or message.text == 'заблокировать' or message.text == '/ban':
                        if chek_admin(user_id=user_id) == 'True':
                            bot.send_message(message.chat.id, 'Напишите user_id человека которого хотите заблокировать...', reply_markup=exit_admin())
                            bot.register_next_step_handler(message, ban_msg)
                        else:
                            bot.send_message(message.chat.id, '🚫 Вы не администратор. У Вас нет прав доступа!')
                            time.sleep(3)
                    elif message.text == 'Разблокировать' or message.text == 'разблокировать' or message.text == '/unban':
                        if chek_admin(user_id=user_id) == 'True':
                            bot.send_message(message.chat.id, 'Напишите user_id человека которого хотите разблокировать...', reply_markup=exit_admin())
                            bot.register_next_step_handler(message, clr_ban_msg)
                        else:
                            bot.send_message(message.chat.id, '🚫 Вы не администратор. У Вас нет прав доступа!')
                            time.sleep(3)
                    elif message.text == 'Показать всех пользователей' or message.text == 'Показать всех пользователей' or message.text == '/allusers':
                        if chek_admin(user_id=user_id) == 'True':
                            bot.send_message(message.chat.id, f'Количество всех пользователей:\n{all_users()}')
                        else:
                            bot.send_message(message.chat.id, '🚫 Вы не администратор. У Вас нет прав доступа!')
                            time.sleep(3)
                    elif message.text == 'Команды' or message.text == 'команды' or message.text == '/cmd':
                        if chek_admin(user_id=user_id) == 'True':
                            bot.send_message(message.chat.id, 'Команды бота могут быть написаны по разному. Как русскими буквами, так и англискими командами.\nКоманды пользователя: \n/prof - показать профиль пользователя в БОТЕ\n/inc - добавить доход\n/cost - добавить расход\n/balance - показать баланс человека на данный момент\n/last_inc - показывает человеку его последний добавленный доход в базу данных\n/last_cost - показывает человеку его последний добавленый расход в базу данных\n/delete_fin - удаляет все финансы пользователя в базе данных, но данные о пользователе остаются (обнуляется баланс, доход,расход)\n/language - изменить язык\n\nКоманды администратора: \n/setadmin - добавляет администратора\n/unadmin - убирает администратора\n/mailing - делает рассылку всем пользователям\n/tex - ставит бота на техническое обслуживание\n/offtex - снимает бота с технического обслуживания\n/ban - банит человека в боте и человек не имеет доступа к боту\n/unban - снимает бан у пользователя и он может пользоваться\n/allusers - показывает всех пользователей бота\n/stopping - Остановка бота (ОПАСНО!!!)\n/system - системное управление бота\n/users - показать список всех пользователей ')
                            time.sleep(3)
                        else:
                            bot.send_message(message.chat.id, 'Команды бота могут быть написаны по разному. Как русскими буквами, так и англискими командами. \nКоманды пользователя: \n/prof - показать профиль пользователя в БОТЕ\n/inc - добавить доход\n/cost - добавить расход\n/balance - показать баланс человека на данный момент\n/last_inc - показывает человеку его последний добавленный доход в базу данных\n/last_cost - показывает человеку его последний добавленый расход в базу данных\n/delete_fin - удаляет все финансы пользователя в базе данных, но данные о пользователе остаются (обнуляется баланс, доход,расход)\n/language - изменить язык')
                            time.sleep(3)
                    elif message.text == 'Остановить бота' or message.text == 'остановить бота' or message.text == '/stopping':
                        if chek_admin(user_id=user_id) == 'True':
                            stopping_markup = types.InlineKeyboardMarkup()
                            but = types.InlineKeyboardButton(text='✅ Подтвердить остановку бота', callback_data=1004)
                            stopping_markup.add(but)
                            bot.send_message(message.chat.id, 'Вы уверены что хотите остановить бота? Если Вы остановите бота, то запустить его можно только через Системного Администратора!!!', reply_markup=stopping_markup)
                        else:
                            bot.send_message(message.chat.id, '🚫 Вы не администратор. У Вас нет прав доступа!')
                            time.sleep(3)
                    elif message.text == '/delete_fin' or message.text == 'Удалить финансы' or message.text == 'удалить финансы':
                        delete_fin_markup = types.InlineKeyboardMarkup()
                        but = types.InlineKeyboardButton(text='✅ Подтвердить удаление финансов', callback_data=1005)
                        delete_fin_markup.add(but)
                        bot.send_message(message.chat.id, 'Вы действительно хотите удалить все финансы из базы данных? Вернуть данные не получиться больше никогда! Ответсвенность за удаление данных из базы данных Вы берете на себя.', reply_markup=delete_fin_markup)
                    elif message.text == '/logs' or message.text == 'Посмотреть логи' or message.text == 'посмотреть логи':
                        if chek_admin(user_id=user_id) == 'True':
                            file = open('logs.txt', 'rb')
                            bot.send_document(message.chat.id, file)
                        else:
                            bot.send_message(message.chat.id, '🚫 Вы не администратор. У Вас нет прав доступа!')
                            time.sleep(3)
                    elif message.text == 'системное управление' or message.text == 'Системное управление' or message.text == '/system':
                        if chek_admin(user_id=user_id) == 'True':
                            system_markup = types.InlineKeyboardMarkup(row_width=1)
                            but1 = types.InlineKeyboardButton(text='⚠️ Остановить бота', callback_data=1006)
                            but2 = types.InlineKeyboardButton(text='📤 Посмотреть логи', callback_data=1007)
                            but3 = types.InlineKeyboardButton(text='🚫 Удалить логи', callback_data=1008)
                            system_markup.add(but1, but2, but3)
                            bot.send_message(message.chat.id, 'Вы в системном управление бота', reply_markup=system_markup)
                        else:
                            bot.send_message(message.chat.id, '🚫 Вы не администратор. У Вас нет прав доступа!')
                            time.sleep(3)
                    elif message.text =='/language' or message.text == 'Изменить язык' or message.text == 'изменить язык':
                        language = types.InlineKeyboardMarkup(row_width=1)
                        but1 = types.InlineKeyboardButton(text='🇷🇺 Русский (RUS)', callback_data=1011)
                        but2 = types.InlineKeyboardButton(text='🇺🇸 English (ANG)', callback_data=1012)
                        language.add(but1, but2)
                        bot.send_message(message.chat.id, 'Для того чтобы изменить язык нужна выбрать в низу подходяшию кнопку.', reply_markup=language)
                    elif message.text == '/users' or message.text == 'посмотреть пользователей' or message.text == 'Посмотреть пользователей':
                        if chek_admin(user_id=user_id) == 'True':
                            users()
                            file = open('users.txt', 'r')
                            text = file.read()
                            bot.send_message(message.chat.id, f'Список всех пользователей:\nid, user_id, user_name, admin, ban, data_reg, language\n\n{text}')
                            file.close()
                            os.remove(os.path.join('users.txt'))
                        else:
                            bot.send_message(message.chat.id, '🚫 Вы не администратор. У Вас нет прав доступа!')
                            time.sleep(3)
                    else:
                        bot.send_message(message.chat.id, 'Я Вас не понимаю', reply_markup=main_menu())
                elif chek_language(user_id=user_id) == 'ANG':
                    if message.text == 'Income' or message.text == 'income' or message.text == '/inc':
                        bot.send_message(message.chat.id, 'Send a message IN NUMBERS about your income', reply_markup=ang_exit())
                        bot.register_next_step_handler(message, next_msg)
                    elif message.text == 'expense' or message.text == 'Expense' or message.text == '/cost':
                        bot.send_message(message.chat.id, 'Send a message in NUMBERS about your expense', reply_markup=ang_exit())
                        bot.register_next_step_handler(message, next_msg_ex)
                    elif message.text == 'Balance' or message.text == 'balance' or message.text == '/balance':
                        try:
                            bot.send_message(message.chat.id, f'Your balance including all income and expenses: {balance(user_id=user_id)} rubles', reply_markup=ang_main_menu())
                            time.sleep(3)
                        except TypeError:
                            bot.send_message(message.chat.id, '⚠️ Sorry, an error occurred')
                            time.sleep(3)
                    elif message.text == 'Profile 👤' or message.text == 'Profile' or message.text == 'profile' or message.text == '/prof':
                        name = '{0.first_name}'.format(message.from_user)
                        bot.send_message(message.chat.id, f'Your profile:\nYour name: {name}\nYour Telegram ID: {message.from_user.id}\nYour username: @{message.from_user.username}\nRegistration in the bot : {data_reg(user_id=user_id)}\nBot ban: {chek_ban(user_id=user_id)}\nBot admin: {chek_admin(user_id=user_id)}\nYour balance: {balance(user_id=user_id)}', reply_markup=ang_main_menu())
                        time.sleep(3)
                    elif message.text == 'Income/Expense':
                        bot.send_message(message.chat.id, 'Choose an action from the suggested buttons... ', reply_markup=ang_menu())
                        time.sleep(3)
                    elif message.text == 'Show last income' or message.text == 'Show last income' or message.text == '/last_inc':
                        bot.send_message(message.chat.id, f'Last income added: {data_income(user_id=user_id)}\nLast income amount: {last_income(user_id=user_id)}', reply_markup=ang_menu())
                        time.sleep(3)
                    elif message.text == 'Show last expense' or message.text == 'show last expense' or message.text == '/last_cost':
                        bot.send_message(message.chat.id, f'Last expense added: {data_expense(user_id=user_id)}\nLast expense amount: {last_expense(user_id=user_id)}', reply_markup=ang_menu())
                        time.sleep(3)
                    elif message.text == 'Main 🔙':
                        bot.send_message(message.chat.id, 'You are in the main menu', reply_markup=ang_main_menu())
                        time.sleep(3)
                    elif message.text == 'Mailing' or message.text == 'Mailing' or message.text == '/mailing':
                        if chek_admin(user_id=user_id) == 'True':
                            bot.send_message(message.chat.id, 'Write a message to be sent by all bot users...', reply_markup=ang_exit_admin())
                            bot.register_next_step_handler(message, mailings_msg)
                        else:
                            bot.send_message(message.chat.id, '🚫 You are not an administrator. You do not have permissions!')
                            time.sleep(3)
                    elif message.text == 'Maintenance' or message.text == 'maintenance':
                        if chek_admin(user_id=user_id) == 'True':
                            bot.send_message(message.chat.id, "You are in the bot's Maintenance panel. Manage below", reply_markup=ang_TO_menu())
                        else:
                            bot.send_message(message.chat.id, '🚫 You are not an administrator. You do not have permissions!')
                            time.sleep(3)
                    elif message.text == 'Administrators' or message.text == 'administrators':
                        if chek_admin(user_id=user_id) == 'True':
                            bot.send_message(message.chat.id, 'You are in the admin control panel. Manage below.', reply_markup=ang_admins())
                        else:
                            bot.send_message(message.chat.id, '🚫 You are not an administrator. You do not have permissions!')
                            time.sleep(3)
                    elif message.text == 'Ban' or message.text == 'ban':
                        if chek_admin(user_id=user_id) == 'True':
                            bot.send_message(message.chat.id, 'You are in the bans control panel. Manage below.', reply_markup=ang_bans())
                        else:
                            bot.send_message(message.chat.id, '🚫 You are not an administrator. You do not have permissions!')
                            time.sleep(3)
                    elif message.text == 'Back 🔙' or message.text == 'Back 🔙':
                        if chek_admin(user_id=user_id) == 'True':
                            bot.send_message(message.chat.id, 'You are in the admin panel. Manage below.', reply_markup=ang_adm_menu())
                        else:
                            bot.send_message(message.chat.id, '🚫 You are not an administrator. You do not have permissions!')
                            time.sleep(3)
                    elif message.text == 'Add Admin' or message.text == 'add Admin' or message.text == '/setadmin':
                        if chek_admin(user_id=user_id) == 'True':
                            bot.send_message(message.chat.id, 'Write the user_id of the person you want to add as admin...', reply_markup=ang_exit_admin())
                            bot.register_next_step_handler(message, add_msg)
                        else:
                            bot.send_message(message.chat.id, '🚫 You are not an administrator. You do not have permissions!')
                            time.sleep(3)
                    elif message.text == 'Remove Admin' or message.text == 'Remove Admin' or message.text == '/unadmin':
                        if chek_admin(user_id=user_id) == 'True':
                            bot.send_message(message.chat.id, 'Write the user_id of the person you want to remove from admins...', reply_markup=ang_exit_admin())
                            bot.register_next_step_handler(message, clr_msg)
                        else:
                            bot.send_message(message.chat.id, '🚫 You are not an administrator. You do not have permissions!')
                            time.sleep(3)
                    elif message.text == 'Ban' or message.text == 'ban' or message.text == '/ban':
                        if chek_admin(user_id=user_id) == 'True':
                            bot.send_message(message.chat.id, 'Enter the user_id of the person you want to block...', reply_markup=ang_exit_admin())
                            bot.register_next_step_handler(message, ban_msg)
                        else:
                            bot.send_message(message.chat.id, '🚫 You are not an administrator. You do not have permissions!')
                            time.sleep(3)
                    elif message.text == 'Unban' or message.text == 'unban' or message.text == '/unban':
                        if chek_admin(user_id=user_id) == 'True':
                            bot.send_message(message.chat.id, 'Enter the user_id of the person you want to unblock...', reply_markup=ang_exit_admin())
                            bot.register_next_step_handler(message, clr_ban_msg)
                        else:
                            bot.send_message(message.chat.id, '🚫 You are not an administrator. You do not have permissions!')
                            time.sleep(3)
                    elif message.text == 'Show all users' or message.text == 'Show all users' or message.text == '/allusers':
                        if chek_admin(user_id=user_id):
                            bot.send_message(message.chat.id, f'Number of all users:\n{all_users()}')
                    elif message.text == 'Commands' or message.text == 'commands' or message.text == '/cmd':
                        if chek_admin(user_id=user_id) == 'True':
                            bot.send_message(message.chat.id, "Bot commands can be written in different ways. Both in Russian letters and in English commands.\nUser commands: \n/prof - show user profile in BOTA\n/inc - add income\ n/cost - add an expense\n/balance - show a person's current balance\n/last_inc - show a person his last income added to the database\n/last_cost - show a person his last expense added to the database\n/delete_fin - deletes all the user's finances in the database, but the user's data remains (balance, income, expenses are reset)\n/language - change language\n\nAdministrator commands: \n/setadmin - adds an administrator\n/unadmin - removes an administrator\n/mailing - makes mailing to all users \n/tex - puts the bot on maintenance\n/offtex - removes the bot from maintenance\n/ban - bans a person in the bot and the person does not have access to the bot\n/unban - removes the ban from the user and he can use it\ n/allusers - shows all users of the bot\n/stopping - Stopping the bot (DANGER!!!)\n/system - system management of the bot\n/users - show a list of all users")
                            time.sleep(3)
                        else:
                            bot.send_message(message.chat.id, "Bot commands can be written in different ways. Both in Russian letters and in English commands. \nUser commands: \n/prof - show user profile in BOTA\n/inc - add income\ n/cost - add an expense\n/balance - show a person's balance at the moment\n/last_inc - show a person his last added income to the database\n/last_cost - shows the person his last expense added to the database\n/delete_fin - deletes all the user's finances in the database, but the user's data remains (balance, income, expenses are reset)\n/language - change language")
                            time.sleep(3)
                    elif message.text == 'Stop bot' or message.text == 'stop bot' or message.text == '/stopping':
                        if chek_admin(user_id=user_id):
                            stopping_markup = types.InlineKeyboardMarkup()
                            but = types.InlineKeyboardButton(text='✅ Confirm bot stop', callback_data=1004)
                            stopping_markup.add(but)
                            bot.send_message(message.chat.id, 'Are you sure you want to stop the bot? If you stop the bot, you can only start it via System Administrator!!!', reply_markup=stopping_markup)
                        else:
                            bot.send_message(message.chat.id, '🚫 You are not an administrator. You do not have permissions!')
                            time.sleep(3)
                    elif message.text == '/delete_fin' or message.text == 'Delete finance' or message.text == 'delete finance':
                        delete_fin_markup = types.InlineKeyboardMarkup()
                        but = types.InlineKeyboardButton(text='✅ Confirm finance deletion', callback_data=1005)
                        delete_fin_markup.add(but)
                        bot.send_message(message.chat.id, 'Are you sure you want to delete all finances from the database? You will never be able to return the data! You are responsible for deleting data from the database.', reply_markup=delete_fin_markup)
                    elif message.text == '/logs' or message.text == 'View logs' or message.text == 'view logs':
                        if chek_admin(user_id=user_id):
                            file = open('logs.txt', 'rb')
                            bot.send_document(message.chat.id, file)
                        else:
                            bot.send_message(message.chat.id, '🚫 You are not an administrator. You do not have permissions!')
                            time.sleep(3)
                    elif message.text == 'system management' or message.text == 'System management' or message.text == '/system':
                        if chek_admin(user_id=user_id):
                            system_markup = types.InlineKeyboardMarkup(row_width=1)
                            but1 = types.InlineKeyboardButton(text='⚠️ Stop Bot', callback_data=1006)
                            but2 = types.InlineKeyboardButton(text='📤 View logs', callback_data=1007)
                            but3 = types.InlineKeyboardButton(text='🚫 Delete logs', callback_data=1008)
                            system_markup.add(but1, but2, but3)
                            bot.send_message(message.chat.id, 'You are in bot system control', reply_markup=system_markup)
                        else:
                            bot.send_message(message.chat.id, '🚫 You are not an administrator. You do not have permissions!')
                            time.sleep(3)
                    elif message.text =='/language' or message.text == 'Change the language' or message.text == 'change the language':
                        language = types.InlineKeyboardMarkup(row_width=1)
                        but1 = types.InlineKeyboardButton(text='🇷🇺 Русский (RUS)', callback_data=1011)
                        but2 = types.InlineKeyboardButton(text='🇺🇸 English (ANG)', callback_data=1012)
                        language.add(but1, but2)
                        bot.send_message(message.chat.id, 'In order to change the language, you need to select the appropriate button at the bottom.', reply_markup=language)
                    elif message.text == '/users' or message.text == 'view users' or message.text == 'view users':
                        if chek_admin(user_id=user_id) == 'True':
                            users()
                            file = open('users.txt', 'r')
                            text = file.read()
                            bot.send_message(message.chat.id, f'List all users:\nid, user_id, user_name, admin, ban, data_reg, language\n\n{text}')
                            file.close()
                            os.remove(os.path.join('users.txt'))
                        else:
                            bot.send_message(message.chat.id, '🚫 You are not an administrator. You do not have permissions!')
                            time.sleep(3)
                    else:
                        bot.send_message(message.chat.id, "I don't understand you", reply_markup=ang_main_menu())
                else:
                    bot.send_message(message.chat.id, 'Вы не выбрали язык! Вы не можете продолжить пользоваться ботом. Для выбора языка используйте /language\n\nYou have not selected a language! You cannot continue using the bot. Use /language to select a language')
            else:
                if chek_language(user_id=user_id) == 'RU':
                    bot.send_message(message.chat.id, '❗️ Вы заблокированы в данном боте. Вы не можете им пользоваться')
                    time.sleep(3)
                else:
                    bot.send_message(message.chat.id, "❗️ You are blocked in this bot. You can't use it")
                    time.sleep(3)
        else:
            bot.send_message(message.chat.id, '⚠️ Вы не зарегистрированы!\nYou are not registered!')
            time.sleep(3)
    else:
        if chek_language(user_id=user_id) == 'RU':
            if chek_admin(user_id=user_id) == 'True':
                if message.text == 'Доход' or message.text == 'доход' or message.text == '/inc':
                    bot.send_message(message.chat.id, 'Отправте сообщение ЦИФРАМИ о Вашем доходе', reply_markup=exit())
                    bot.register_next_step_handler(message, next_msg)
                elif message.text == 'Расход' or message.text == 'расход' or message.text == '/cost':
                    bot.send_message(message.chat.id, 'Отправте сообщение ЦИФРАМИ о Вашем расходе', reply_markup=exit())
                    bot.register_next_step_handler(message, next_msg_ex)
                elif message.text == 'Баланс' or message.text == 'баланс' or message.text == '/balance':
                    try:
                        bot.send_message(message.chat.id, f'Ваш баланс с учетом всех доходов и расходов: {balance(user_id=user_id)} рублей', reply_markup=main_menu())
                        time.sleep(3)
                    except TypeError:
                        bot.send_message(message.chat.id, '⚠️ Извините, произошла ошибка')
                        time.sleep(3)
                elif message.text == 'Профиль 👤' or message.text == 'Профиль' or message.text == 'профиль' or message.text == '/prof':
                    name = '{0.first_name}'.format(message.from_user)
                    bot.send_message(message.chat.id, f'Ваш профиль:\nВаше имя: {name}\nВаш Telegram ID: {message.from_user.id}\nВаш username: @{message.from_user.username}\nРегестрация в боте: {data_reg(user_id=user_id)}\nБлокировка в боте: {chek_ban(user_id=user_id)}\nАдминистратор бота: {chek_admin(user_id=user_id)}\nВаш баланс: {balance(user_id=user_id)}', reply_markup=main_menu())
                    time.sleep(3)
                elif message.text == 'Доход/расход':
                    bot.send_message(message.chat.id, 'Выбирете из предложенных кнопок действие... ', reply_markup=menu())
                    time.sleep(3)
                elif message.text == 'Главная 🔙':
                    bot.send_message(message.chat.id, 'Вы в главном меню', reply_markup=main_menu())
                    time.sleep(3)
                elif message.text == 'Рассылка' or message.text == 'рассылка' or message.text == '/mailing':
                    bot.send_message(message.chat.id, 'Напишите сообщение которое будет отправлено всем пользователем бота...', reply_markup=exit_admin())
                    bot.register_next_step_handler(message, mailings_msg)
                elif message.text == 'Техническое Обслуживание' or message.text == 'техническое обслуживание':
                    bot.send_message(message.chat.id, 'Вы в панели Технического Обслуживания бота. Управление ниже', reply_markup=TO_menu())
                elif message.text == 'Администраторы' or message.text == 'администраторы':
                    bot.send_message(message.chat.id, 'Вы в панели управления администраторами. Управление ниже.', reply_markup=admins())
                elif message.text == 'Бан' or message.text == 'Бан':
                    bot.send_message(message.chat.id, 'Вы в панели управления блокировок. Управление ниже.', reply_markup=bans())
                elif message.text == 'Назад 🔙' or message.text == 'назад 🔙':
                        bot.send_message(message.chat.id, 'Вы в админ-панели. Управление ниже.', reply_markup=adm_menu())
                elif message.text == 'Добавить администратора' or message.text == 'добавить администратора' or message.text == '/setadmin':
                    bot.send_message(message.chat.id, 'Напишите user_id человека кого хотите добавит в администраторы...', reply_markup=exit_admin())
                    bot.register_next_step_handler(message, add_msg)
                elif message.text == 'Убрать администратора' or message.text == 'убрать администратора' or message.text == '/unadmin':
                    bot.send_message(message.chat.id, 'Напишите user_id человека кого хотите убрать из администраторов...', reply_markup=exit_admin())
                    bot.register_next_step_handler(message, clr_msg)
                elif message.text == 'Заблокировать' or message.text == 'заблокировать' or message.text == '/ban':
                    bot.send_message(message.chat.id, 'Напишите user_id человека которого хотите заблокировать...', reply_markup=exit_admin())
                    bot.register_next_step_handler(message, ban_msg)
                elif message.text == 'Разблокировать' or message.text == 'разблокировать' or message.text == '/unban':
                    bot.send_message(message.chat.id, 'Напишите user_id человека которого хотите разблокировать...', reply_markup=exit_admin())
                    bot.register_next_step_handler(message, clr_ban_msg)
                elif message.text == 'Показать всех пользователей' or message.text == 'Показать всех пользователей' or message.text == '/allusers':
                    bot.send_message(message.chat.id, f'Список всех пользователей:\n{all_users()}')
                elif message.text == 'Команды' or message.text == 'команды' or message.text == '/cmd':
                    bot.send_message(message.chat.id, 'Команды бота могут быть написаны по разному. Как русскими буквами, так и англискими командами. \nКоманды пользователя: \n/prof - показать профиль пользователя в БОТЕ\n/inc - добавить доход\n/cost - добавить расход\n/balance - показать баланс человека на данный момент\n/last_inc - показывает человеку его последний добавленный доход в базу данных\n/last_cost - показывает человеку его последний добавленый расход в базу данных\n/delete_fin - удаляет все финансы пользователя в базе данных, но данные о пользователе остаются (обнуляется баланс, доход,расход)\n/language - изменить язык\n\nКоманды администратора: \n/setadmin - добавляет администратора\n/unadmin - убирает администратора\n/mailing - делает рассылку всем пользователям\n/tex - ставит бота на техническое обслуживание\n/offtex - снимает бота с технического обслуживания\n/ban - банит человека в боте и человек не имеет доступа к боту\n/unban - снимает бан у пользователя и он может пользоваться\n/allusers - показывает всех пользователей бота\n/stopping - Остановка бота (ОПАСНО!!!)\n/system - системное управление бота\n/users - показать список всех пользователей')
                    time.sleep(3)
                elif message.text == 'Показать последний доход' or message.text == 'показать последний доход' or message.text == '/last_inc':
                    bot.send_message(message.chat.id, f'Последний доход был добавлен: {data_income(user_id=user_id)}\nСумма последнего дохода: {last_income(user_id=user_id)}')
                    time.sleep(3)
                elif message.text == 'Показать последний расход' or message.text == 'показать последний расход' or message.text == '/last_cost':
                    bot.send_message(message.chat.id, f'Последний расход был добавлен: {data_expense(user_id=user_id)}\nСумма последнего расхода: {last_expense(user_id=user_id)}', reply_markup=menu())
                    time.sleep(3)
                elif message.text == 'Остановить бота' or message.text == 'остановить бота' or message.text == '/stopping':
                    if chek_admin(user_id=user_id):
                        stopping_markup = types.InlineKeyboardMarkup()
                        but = types.InlineKeyboardButton(text='✅ Подтвердить остановку бота', callback_data=1004)
                        stopping_markup.add(but)
                        bot.send_message(message.chat.id, 'Вы уверены что хотите остановить бота? Если Вы остановите бота, то запустить его можно только через Системного Администратора!!!', reply_markup=stopping_markup)
                    else:
                        bot.send_message(message.chat.id, '🚫 Вы не администратор. У Вас нет прав доступа!')
                        time.sleep(3)
                elif message.text == '/delete_fin' or message.text == 'Удалить финансы' or message.text == 'удалить финансы':
                        delete_fin_markup = types.InlineKeyboardMarkup()
                        but = types.InlineKeyboardButton(text='✅ Подтвердить удаление финансов', callback_data=1005)
                        delete_fin_markup.add(but)
                        bot.send_message(message.chat.id, 'Вы действительно хотите удалить все финансы из базы данных? Вернуть данные не получиться больше никогда! Ответсвенность за удаление данных из базы данных Вы берете на себя.', reply_markup=delete_fin_markup)
                elif message.text == '/logs' or message.text == 'Посмотреть логи' or message.text == 'посмотреть логи':
                        if chek_admin(user_id=user_id):
                            file = open('logs.txt', 'rb')
                            bot.send_document(message.chat.id, file)
                        else:
                            bot.send_message(message.chat.id, '🚫 Вы не администратор. У Вас нет прав доступа!')
                            time.sleep(3)
                elif message.text == 'системное управление' or message.text == 'Системное управление' or message.text == '/system':
                        if chek_admin(user_id=user_id):
                            system_markup = types.InlineKeyboardMarkup(row_width=1)
                            but1 = types.InlineKeyboardButton(text='⚠️ Остановить бота', callback_data=1006)
                            but2 = types.InlineKeyboardButton(text='📤 Посмотреть логи', callback_data=1007)
                            but3 = types.InlineKeyboardButton(text='🚫 Удалить логи', callback_data=1008)
                            system_markup.add(but1, but2, but3)
                            bot.send_message(message.chat.id, 'Вы в системном управление бота', reply_markup=system_markup)
                        else:
                            bot.send_message(message.chat.id, '🚫 Вы не администратор. У Вас нет прав доступа!')
                            time.sleep(3)
                elif message.text =='/language' or message.text == 'Изменить язык' or message.text == 'изменить язык':
                        language = types.InlineKeyboardMarkup(row_width=1)
                        but1 = types.InlineKeyboardButton(text='🇷🇺 Русский (RUS)', callback_data=1011)
                        but2 = types.InlineKeyboardButton(text='🇺🇸 English (ANG)', callback_data=1012)
                        language.add(but1, but2)
                        bot.send_message(message.chat.id, 'Для того чтобы изменить язык нужна выбрать в низу подходяшию кнопку.', reply_markup=language)
                elif message.text == '/users' or message.text == 'посмотреть пользователей' or message.text == 'Посмотреть пользователей':
                    users()
                    file = open('users.txt', 'r')
                    text = file.read()
                    bot.send_message(message.chat.id, f'Список всех пользователей:\nid, user_id, user_name, admin, ban, data_reg, language\n\n{text}')
                    file.close()
                    os.remove(os.path.join('users.txt'))
                else:
                    bot.send_message(message.chat.id, 'Я Вас не понимаю', reply_markup=main_menu())
            else:
                if chek_language(user_id=user_id) == 'RU':
                    bot.send_message(message.chat.id, '⚠️ Приносим свои извинения, но бот отправлен на Техническое Обслуживание, по каким-либо причинам. Ожидайте новостей от команды проекта, либо включения бота. На момент обслуживание бота Вы не можете его использовать, при попытке использовать бота, Вам будет возращено сообщение об ошибке. Наберитесь терпения. Просим прошения! Всего хорошего.')
                    time.sleep(3)
                else:
                    bot.send_message(message.chat.id, "⚠️ We apologize, but the bot has been sent for Maintenance, for some reason. Expect news from the project team, or the inclusion of a bot. At the time of the bot maintenance, you cannot use it, if you try to use the bot, an error message will be returned to you. Be patient. We ask for your forgiveness! Good luck.")
                    time.sleep(3)
        elif chek_language(user_id=user_id) == 'ANG':
            if chek_admin(user_id=user_id) == 'True':
                if message.text == 'Income' or message.text == 'income' or message.text == '/inc':
                    bot.send_message(message.chat.id, 'Send a message IN NUMBERS about your income', reply_markup=ang_exit())
                    bot.register_next_step_handler(message, next_msg)
                elif message.text == 'Cost' or message.text == 'cost' or message.text == '/cost':
                    bot.send_message(message.chat.id, 'Send a message in NUMBERS about your expense', reply_markup=ang_exit())
                    bot.register_next_step_handler(message, next_msg_ex)
                elif message.text == 'Balance' or message.text == 'balance' or message.text == '/balance':
                    try:
                        bot.send_message(message.chat.id, f'Your balance including all income and expenses: {balance(user_id=user_id)} rubles', reply_markup=ang_main_menu())
                        time.sleep(3)
                    except TypeError:
                        bot.send_message(message.chat.id, '⚠️ Sorry, an error occurred')
                        time.sleep(3)
                elif message.text == 'Profile 👤' or message.text == 'Profile' or message.text == 'profile' or message.text == '/prof':
                    name = '{0.first_name}'.format(message.from_user)
                    bot.send_message(message.chat.id, f'Your profile:\nYour name: {name}\nYour Telegram ID: {message.from_user.id}\nYour username: @{message.from_user.username}\nRegistration in the bot : {data_reg(user_id=user_id)}\nBot ban: {chek_ban(user_id=user_id)}\nBot admin: {chek_admin(user_id=user_id)}\nYour balance: {balance(user_id=user_id)}', reply_markup= main_menu())
                    time.sleep(3)
                elif message.text == 'Income/Expense':
                    bot.send_message(message.chat.id, 'Choose an action from the suggested buttons... ', reply_markup=ang_menu())
                    time.sleep(3)
                elif message.text == 'Main 🔙':
                    bot.send_message(message.chat.id, 'You are in the main menu', reply_markup=ang_main_menu())
                    time.sleep(3)
                elif message.text == 'Mailing' or message.text == 'Mailing' or message.text == '/mailing':
                    bot.send_message(message.chat.id, 'Write a message to be sent by all bot users...', reply_markup=ang_exit_admin())
                    bot.register_next_step_handler(message, mailings_msg)
                elif message.text == 'Maintenance' or message.text == 'Maintenance':
                    bot.send_message(message.chat.id, "You are in the bot's Maintenance panel. Manage below", reply_markup=ang_TO_menu())
                elif message.text == 'Administrators' or message.text == 'Administrators':
                    bot.send_message(message.chat.id, 'You are in the admin control panel. Manage below.', reply_markup=ang_admins())
                elif message.text == 'Ban' or message.text == 'Ban':
                    bot.send_message(message.chat.id, 'You are in the bans control panel. Manage below.', reply_markup=ang_bans())
                elif message.text == 'Back 🔙' or message.text == 'Back 🔙':
                        bot.send_message(message.chat.id, 'You are in the admin panel. Manage below.', reply_markup=ang_adm_menu())
                elif message.text == 'Add Admin' or message.text == 'Add Admin' or message.text == '/setadmin':
                    bot.send_message(message.chat.id, 'Write the user_id of the person you want to add as admin...', reply_markup=ang_exit_admin())
                    bot.register_next_step_handler(message, add_msg)
                elif message.text == 'Remove Admin' or message.text == 'Remove Admin' or message.text == '/unadmin':
                    bot.send_message(message.chat.id, 'Write the user_id of the person you want to remove from admins...', reply_markup=ang_exit_admin())
                    bot.register_next_step_handler(message, clr_msg)
                elif message.text == 'Ban' or message.text == 'ban' or message.text == '/ban':
                    bot.send_message(message.chat.id, 'Enter the user_id of the person you want to block...', reply_markup=ang_exit_admin())
                    bot.register_next_step_handler(message, ban_msg)
                elif message.text == 'Unban' or message.text == 'unban' or message.text == '/unban':
                    bot.send_message(message.chat.id, 'Enter the user_id of the person you want to unblock...', reply_markup=ang_exit_admin())
                    bot.register_next_step_handler(message, clr_ban_msg)
                elif message.text == 'Show all users' or message.text == 'Show all users' or message.text == '/allusers':
                    bot.send_message(message.chat.id, f'List all users:\n{all_users()}')
                elif message.text == 'Commands' or message.text == 'commands' or message.text == '/cmd':
                    bot.send_message(message.chat.id, "Bot commands can be written in different ways. Both in Russian letters and in English commands. \nUser commands: \n/prof - show user profile in BOTA\n/inc - add income\ n/cost - add an expense\n/balance - show a person's current balance\n/last_inc - show a person his last income added to the database\n/last_cost - show a person his last expense added to the database\n/delete_fin - deletes all the user's finances in the database, but the user's data remains (balance, income, expenses are reset)\n/language - change language\n\nAdministrator commands: \n/setadmin - adds an administrator\n/unadmin - removes an administrator\n/mailing - makes mailing to all users \n/tex - puts the bot on maintenance\n/offtex - removes the bot from maintenance\n/ban - bans a person in the bot and the person does not have access to the bot\n/unban - removes the ban from the user and he can use it\ n/allusers - shows all users of the bot\n/stopping - Stopping the bot (DANGER!!!)\n/system - system management of the bot\n/users - show a list of all users")
                    time.sleep(3)
                elif message.text == 'Show last income' or message.text == 'Show last income' or message.text == '/last_inc':
                    bot.send_message(message.chat.id, f'Last income added: {data_income(user_id=user_id)}\nLast income amount: {last_income(user_id=user_id)}')
                    time.sleep(3)
                elif message.text == 'Show last cost' or message.text == 'Show last cost' or message.text == '/last_cost':
                    bot.send_message(message.chat.id, f'Last expense added: {data_expense(user_id=user_id)}\nLast expense amount: {last_expense(user_id=user_id)}', reply_markup=ang_menu())
                    time.sleep(3)
                elif message.text == 'Stop bot' or message.text == 'stop bot' or message.text == '/stopping':
                    if chek_admin(user_id=user_id):
                        stopping_markup = types.InlineKeyboardMarkup()
                        but = types.InlineKeyboardButton(text='✅ Confirm bot stop', callback_data=1004)
                        stopping_markup.add(but)
                        bot.send_message(message.chat.id, 'Are you sure you want to stop the bot? If you stop the bot, you can only start it via System Administrator!!!', reply_markup=stopping_markup)
                    else:
                        bot.send_message(message.chat.id, '🚫 You are not an administrator. You do not have permissions!')
                        time.sleep(3)
                elif message.text == '/delete_fin' or message.text == 'Delete finance' or message.text == 'delete finance':
                        delete_fin_markup = types.InlineKeyboardMarkup()
                        but = types.InlineKeyboardButton(text='✅ Confirm finance deletion', callback_data=1005)
                        delete_fin_markup.add(but)
                        bot.send_message(message.chat.id, 'Are you sure you want to delete all finances from the database? You will never be able to return the data! You are responsible for deleting data from the database.', reply_markup=delete_fin_markup)
                elif message.text == '/logs' or message.text == 'View logs' or message.text == 'view logs':
                        if chek_admin(user_id=user_id):
                            file = open('logs.txt', 'rb')
                            bot.send_document(message.chat.id, file)
                        else:
                            bot.send_message(message.chat.id, '🚫 You are not an administrator. You do not have permissions!')
                            time.sleep(3)
                elif message.text == 'system management' or message.text == 'System management' or message.text == '/system':
                        if chek_admin(user_id=user_id):
                            system_markup = types.InlineKeyboardMarkup(row_width=1)
                            but1 = types.InlineKeyboardButton(text='⚠️ Stop Bot', callback_data=1006)
                            but2 = types.InlineKeyboardButton(text='📤 View logs', callback_data=1007)
                            but3 = types.InlineKeyboardButton(text='🚫 Delete logs', callback_data=1008)
                            system_markup.add(but1, but2, but3)
                            bot.send_message(message.chat.id, 'You are in bot system control', reply_markup=system_markup)
                        else:
                            bot.send_message(message.chat.id, '🚫 You are not an administrator. You do not have permissions!')
                            time.sleep(3)
                elif message.text =='/language' or message.text == 'Change the language' or message.text == 'change the language':
                        language = types.InlineKeyboardMarkup(row_width=1)
                        but1 = types.InlineKeyboardButton(text='🇷🇺 Русский (RUS)', callback_data=1011)
                        but2 = types.InlineKeyboardButton(text='🇺🇸 English (ANG)', callback_data=1012)
                        language.add(but1, but2)
                        bot.send_message(message.chat.id, 'In order to change the language, you need to select the appropriate button at the bottom.', reply_markup=language)
                elif message.text == '/users' or message.text == 'view users' or message.text == 'view users':
                        if chek_admin(user_id=user_id) == 'True':
                            users()
                            file = open('users.txt', 'r')
                            text = file.read()
                            bot.send_message(message.chat.id, f'List all users:\nid, user_id, user_name, admin, ban, data_reg, language\n\n{text}')
                            file.close()
                            os.remove(os.path.join('users.txt'))
                        else:
                            bot.send_message(message.chat.id, '🚫 You are not an administrator. You do not have permissions!')
                            time.sleep(3)
                else:
                    bot.send_message(message.chat.id, "I don't understand you", reply_markup=ang_main_menu())
            else:
                bot.send_message(message.chat.id, "⚠️ We apologize, but the bot has been sent for Maintenance, for some reason. Expect news from the project team, or the inclusion of a bot. At the time of the bot maintenance, you cannot use it, if you try to use the bot, an error message will be returned to you. Be patient. We ask for your forgiveness! Good luck.")
                time.sleep(3)
        else:
            bot.send_message(message.chat.id, 'Вы не выбрали язык! Вы не можете продолжить пользоваться ботом. Для выбора языка используйте /language\n\nYou have not selected a language! You cannot continue using the bot. Use /language to select a language')
    
bot.infinity_polling(timeout=10, long_polling_timeout = 5)