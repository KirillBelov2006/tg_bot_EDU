import telebot
from telebot import types


API = "6716839285:AAELAqJWFuytN68ckJzacZNEdVDYWwYSpxk"
bot = telebot.TeleBot(API)


@bot.message_handler(commands=['start'])
def lang(message):
    markup = types.InlineKeyboardMarkup()
    item1 = types.InlineKeyboardButton("🇬🇧 English", callback_data='English')
    item2 = types.InlineKeyboardButton("🇷🇺 Русский", callback_data='Russian')
    markup.add(item1, item2)
    bot.send_message(message.chat.id, "Choose your language/Выберите свой язык", reply_markup=markup)



@bot.callback_query_handler(func=lambda call: call.data == 'English' or call.data == 'Russian')
def handle_language_selection(call):
    if call.data == 'English':
            markup1 = types.InlineKeyboardMarkup(row_width=2)
            item1 = types.InlineKeyboardButton("⁉️ FAQ", callback_data='FAQ_us')
            item2 = types.InlineKeyboardButton("📲 Сontact us",callback_data='Contact_us')
            item3 = types.InlineKeyboardButton("💬 Chat",url="https://t.me/+Zqjqtu_KXTdiNmM6")
            item4 = types.InlineKeyboardButton("👨‍💻️ Tech.assistance",url='https://t.me/Kirill_DAT')
            item5 = types.InlineKeyboardButton("🌍 Change language",callback_data='Return_us_main')
            markup1.add(item1, item2, item3, item4, item5)
            bot.edit_message_text(
                chat_id=call.message.chat.id,
                message_id=call.message.message_id,
                text="Hey! I'm the official EduCity bot  💻",
                reply_markup=markup1
            )




    elif call.data == 'Russian':
            markup = types.InlineKeyboardMarkup(row_width=2)
            item1_ru = types.InlineKeyboardButton("⁉️ FAQ", callback_data='FAQ_ru')
            item2_ru = types.InlineKeyboardButton("📲 Контакты", callback_data='Contact_ru')
            item3_ru = types.InlineKeyboardButton("💬 Чат", url="https://t.me/+Zqjqtu_KXTdiNmM6")
            item4_ru = types.InlineKeyboardButton("👨‍💻️ Тех.Помощь",url='https://t.me/Kirill_DAT')
            item5_ru = types.InlineKeyboardButton("🌍 Изменить язык", callback_data='Return_ru_main')
            markup.add(item1_ru, item2_ru, item3_ru, item4_ru, item5_ru)
            bot.edit_message_text(
                chat_id=call.message.chat.id,
                message_id=call.message.message_id,
                text="Привет! Я официальный бот EduCity 💻",
                reply_markup=markup
            )


@bot.callback_query_handler(func=lambda call: call.data == 'Return_ru_main' or call.data == 'Return_us_main')
def callback_return(call):
    if call.data == 'Return_ru_main':
        markup = types.InlineKeyboardMarkup()
        item1_r = types.InlineKeyboardButton("🇬🇧 English", callback_data='English')
        item2_r = types.InlineKeyboardButton("🇷🇺 Русский", callback_data='Russian')
        markup.add(item1_r, item2_r)
        bot.edit_message_text(
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            text="Choose your language/Выберите свой язык",
            reply_markup=markup
        )
    elif call.data == 'Return_us_main':
        markup = types.InlineKeyboardMarkup()
        item1_s = types.InlineKeyboardButton("🇬🇧 English", callback_data='English')
        item2_s = types.InlineKeyboardButton("🇷🇺 Русский", callback_data='Russian')
        markup.add(item1_s, item2_s)
        bot.edit_message_text(
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            text="Choose your language/Выберите свой язык",
            reply_markup=markup
        )





@bot.callback_query_handler(func=lambda call: call.data == 'Return_ru1' or call.data == 'Return_us1')
def callback_return2(call):
    if call.data == 'Return_ru1':
        markup = types.InlineKeyboardMarkup(row_width=2)
        item1_ru = types.InlineKeyboardButton("⁉️ FAQ", callback_data='FAQ_ru')
        item2_ru = types.InlineKeyboardButton("📲 Контакты", callback_data='Contact_ru')
        item3_ru = types.InlineKeyboardButton("💬 Чат", url="https://t.me/+Zqjqtu_KXTdiNmM6")
        item4_ru = types.InlineKeyboardButton("👨‍💻️ Тех.Помощь", url='https://t.me/Kirill_DAT')
        item5_ru = types.InlineKeyboardButton("🌍 Изменить язык", callback_data='Return_ru_main')
        markup.add(item1_ru, item2_ru, item3_ru, item4_ru, item5_ru)
        bot.edit_message_text(
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            text="Привет! Я официальный бот EduCity 💻",
            reply_markup=markup
        )
    elif call.data == 'Return_us1':
        markup = types.InlineKeyboardMarkup(row_width=2)
        item1 = types.InlineKeyboardButton("⁉️ FAQ", callback_data='FAQ_us')
        item2 = types.InlineKeyboardButton("📲 Сontact us", callback_data='Contact_us')
        item3 = types.InlineKeyboardButton("💬 Chat", url="https://t.me/+Zqjqtu_KXTdiNmM6")
        item4 = types.InlineKeyboardButton("👨‍💻️ Tech.assistance", url='https://t.me/Kirill_DAT')
        item5 = types.InlineKeyboardButton("🌍 Change language", callback_data='Return_us_main')
        markup.add(item1, item2, item3, item4, item5)
        bot.edit_message_text(
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            text="Hey! I'm the official EduCity bot  💻",
            reply_markup=markup
        )



@bot.callback_query_handler(func=lambda call: call.data == 'Contact_ru' or call.data == 'Contact_us')
def contacts(call):
    contact_info_en = "📲 Website: https://educity.tech/\n\n📲 Email: da@educity.tech\n\n📲 Insta: https://www.instagram.com/da.technologies"
    contact_info_ru = "📲 Сайт: https://educity.tech/\n\n📲 Почта: da@educity.tech\n\n📲 Инста: https://www.instagram.com/da.technologies"
    if call.data == 'Contact_us':
        markup = types.InlineKeyboardMarkup(row_width=1)
        item_backup = types.InlineKeyboardButton("🔁 Back",callback_data="Back_Contacts_us")
        markup.add(item_backup)
        bot.edit_message_text(
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            text=contact_info_en,
            reply_markup=markup
        )
    elif call.data == 'Contact_ru':
        markup_ru = types.InlineKeyboardMarkup(row_width=1)
        item_backup_ru = types.InlineKeyboardButton("🔁 Назад", callback_data="Back_Contacts_ru")
        markup_ru.add(item_backup_ru)
        bot.edit_message_text(
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            text=contact_info_ru,
            reply_markup=markup_ru
        )


@bot.callback_query_handler(func=lambda call: call.data == "Back_Contacts_us" or call.data == "Back_Contacts_ru")
def callback_backup(call):
    if call.data == "Back_Contacts_us":
        markup = types.InlineKeyboardMarkup(row_width=2)
        item1 = types.InlineKeyboardButton("⁉️ FAQ", callback_data='FAQ_us')
        item2 = types.InlineKeyboardButton("📲 Сontact us", callback_data='Contact_us')
        item3 = types.InlineKeyboardButton("💬 Chat", url="https://t.me/+Zqjqtu_KXTdiNmM6")
        item4 = types.InlineKeyboardButton("👨‍💻️ Tech.assistance", url='https://t.me/Kirill_DAT')
        item5 = types.InlineKeyboardButton("🌍 Change language", callback_data='Return_us_main')
        markup.add(item1, item2, item3, item4, item5)
        bot.edit_message_text(
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            text="Hey! I'm the official EduCity bot  💻",
            reply_markup=markup
        )
    elif call.data == "Back_Contacts_ru":
        markup = types.InlineKeyboardMarkup(row_width=2)
        item1_ru = types.InlineKeyboardButton("⁉️ FAQ", callback_data='FAQ_ru')
        item2_ru = types.InlineKeyboardButton("📲 Контакты", callback_data='Contact_ru')
        item3_ru = types.InlineKeyboardButton("💬 Чат", url="https://t.me/+Zqjqtu_KXTdiNmM6")
        item4_ru = types.InlineKeyboardButton("👨‍💻️ Тех.Помощь", url='https://t.me/Kirill_DAT')
        item5_ru = types.InlineKeyboardButton("🌍 Изменить язык", callback_data='Return_ru_main')
        markup.add(item1_ru, item2_ru, item3_ru, item4_ru, item5_ru)
        bot.edit_message_text(
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            text="Привет! Я официальный бот EduCity 💻",
            reply_markup=markup
        )


@bot.callback_query_handler(func=lambda call: call.data =="Back_info_us1" or call.data == "Back_info_ru1")
def backup_info(call):
    if call.data == "Back_info_us1":
        markup_us = types.InlineKeyboardMarkup(row_width=2)
        faq1_us = types.InlineKeyboardButton("What is EduCity", callback_data='q1_us')
        faq2_us = types.InlineKeyboardButton("Presentation", url='https://disk.yandex.ru/i/7M2xtXTqzPkF4Q')
        faq3_us = types.InlineKeyboardButton("Metaverse", url='https://www.youtube.com/watch?v=jFUVZDPrB7U')
        faq4_us = types.InlineKeyboardButton("White Paper", url='https://educity.tech/')
        # Добавьте сюда другие кнопки, если нужно.
        back_us = types.InlineKeyboardButton("🔁 Back", callback_data='Return_us1')
        markup_us.add(faq1_us, faq2_us, faq3_us, faq4_us, back_us)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Find out more about project and get a White Paper", reply_markup=markup_us)
    elif call.data == "Back_info_ru1":
        markup_ru = types.InlineKeyboardMarkup(row_width=2)
        faq1_ru = types.InlineKeyboardButton("Что такое EduCity", callback_data='q1_ru')
        faq2_ru = types.InlineKeyboardButton("Презентация", url= 'https://disk.yandex.ru/i/7M2xtXTqzPkF4Q')
        faq3_ru = types.InlineKeyboardButton("Метавселенная", url='https://www.youtube.com/watch?v=znX1Hdyq9l8')
        faq4_ru = types.InlineKeyboardButton("White Paper", url='https://educity.tech/')
        # Добавьте сюда другие кнопки, если нужно.
        back_ru = types.InlineKeyboardButton("🔁 Назад", callback_data='Return_ru1')
        markup_ru.add(faq1_ru, faq2_ru, faq3_ru, faq4_ru, back_ru)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Узнайте больше о проекте и получите White Paper", reply_markup=markup_ru)



@bot.callback_query_handler(func=lambda call: call.data == 'q1_us' or call.data == 'q1_ru')
def getinfo_Edu(call):
    if call.data == 'q1_us':
        markup_us = types.InlineKeyboardMarkup(row_width=2)
        item_backup_coop_us = types.InlineKeyboardButton("🤝 Сollaboration",callback_data="Collab_us")
        item_achievements_us = types.InlineKeyboardButton("🏆 Achievements", callback_data="Achievements_us")
        item_backup_us = types.InlineKeyboardButton("🔁 Back", callback_data="Back_info_us1")
        markup_us.add(item_backup_coop_us, item_achievements_us, item_backup_us)
        bot.edit_message_text(
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            text='<b>Educity</b> is a product for teaching foreign languages using VR technologies, by immersing the user in a virtual environment with the effect of maximum presence.'
                 '\n\n<b>The Educity project is unique and allows users to:</b>\n- Increase motivation when learning foreign languages'
                 '\n- Avoid embarrassment and fear when learning'
                 '\n- Practice your skills using real examples'
                 '\n- Adapt faster when moving or a one-time trip to another country'
                 '\n- Diversify the teacher’s lesson with the use of virtual reality'
                 '\n- Become more familiar with the culture and habits of the countries of the language you are learning, as well as interact with them directly',
            reply_markup=markup_us,
            parse_mode='html'
        )
    elif call.data == 'q1_ru':
        markup_ru = types.InlineKeyboardMarkup(row_width=2)
        item_backup_coop_ru = types.InlineKeyboardButton("🤝 Сотрудничество",callback_data="Collab_ru")
        item_achievements_ru = types.InlineKeyboardButton("🏆 Достижения",callback_data="Achievements_ru")
        item_backup_ru = types.InlineKeyboardButton("🔁 Назад", callback_data="Back_info_ru1")
        markup_ru.add(item_backup_coop_ru, item_achievements_ru, item_backup_ru)
        bot.edit_message_text(
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            text='<b>Educity</b> это продукт, по обучению иностранным языкам на базе VR технологий, путем погружения пользователя в виртуальную среду с эффектом максимального присутствия. '
                 '\n\n<b>Проект Educity уникальный и позволяет пользователям:</b> '
                 '\n- Повысить мотивацию при изучении иностранных языков '
                 '\n- Избежать стеснения и страха при обучении'
                 '\n- Отрабатывать свои навыки на реальных примерах'
                 '\n- Быстрее адаптировать при переезде или разовой поездке в другую страну '
                 '\n- Разнообразить урок педагога с применение виртуальной реальности'
                 '\n- Ближе ознакомиться с культурой и привычками стран изучаемого языка, а также повзаимодействовать с ними напрямую',
             reply_markup= markup_ru,
             parse_mode='html'
        )


@bot.callback_query_handler(func=lambda call: call.data == "Collab_backup_ru" or call.data == "Collab_backup_us")
def backup_Collab(call):
    if call.data == "Collab_backup_ru":
        markup = types.InlineKeyboardMarkup(row_width=2)
        item1_ru = types.InlineKeyboardButton("⁉️ FAQ", callback_data='FAQ_ru')
        item2_ru = types.InlineKeyboardButton("📲 Контакты", callback_data='Contact_ru')
        item3_ru = types.InlineKeyboardButton("💬 Чат", url="https://t.me/+Zqjqtu_KXTdiNmM6")
        item4_ru = types.InlineKeyboardButton("👨‍💻️ Тех.Помощь", url='https://t.me/Kirill_DAT')
        item5_ru = types.InlineKeyboardButton("🌍 Изменить язык", callback_data='Return_ru_main')
        markup.add(item1_ru, item2_ru, item3_ru, item4_ru, item5_ru)
        bot.edit_message_text(
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            text="Привет! Я официальный бот EduCity 💻",
            reply_markup=markup
        )
    elif call.data == "Collab_backup_us":
        markup = types.InlineKeyboardMarkup(row_width=2)
        item1 = types.InlineKeyboardButton("⁉️ FAQ", callback_data='FAQ_us')
        item2 = types.InlineKeyboardButton("📲 Сontact us", callback_data='Contact_us')
        item3 = types.InlineKeyboardButton("💬 Chat", url="https://t.me/+Zqjqtu_KXTdiNmM6")
        item4 = types.InlineKeyboardButton("👨‍💻️ Tech.assistance", url='https://t.me/Kirill_DAT')
        item5 = types.InlineKeyboardButton("🌍 Change language", callback_data='Return_us_main')
        markup.add(item1, item2, item3, item4, item5)
        bot.edit_message_text(
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            text="Hey! I'm the official EduCity bot  💻",
            reply_markup=markup
        )




@bot.callback_query_handler(func=lambda call: call.data == "Collab_ru" or call.data == "Collab_us")
def getcollab(call):
    if call.data == "Collab_ru":
        markup = types.InlineKeyboardMarkup(row_width=3)
        collab1_ru = types.InlineKeyboardButton('Партнёрам', url='https://docs.google.com/forms/d/e/1FAIpQLSeCuRZKJun1hMI3ZADaXjdvdeDLDeU1J1KrZI1YmTc10i_SfA/viewform')
        collab2_ru = types.InlineKeyboardButton('Клиентам', url='https://educity.tech/')
        collab3_ru = types.InlineKeyboardButton('Сотрудникам', url='https://educity.tech/')
        backup_ru = types.InlineKeyboardButton('🔁 Вернуться в меню', callback_data='Collab_backup_ru')
        markup.add(collab1_ru,collab2_ru,collab3_ru,backup_ru)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Начните работать с нами", reply_markup=markup)
    elif call.data == "Collab_us":
        markup = types.InlineKeyboardMarkup(row_width=3)
        collab1_us = types.InlineKeyboardButton('Partners', url='https://forms.gle/eXXn8WWaav7ks9W5A')
        collab2_us = types.InlineKeyboardButton('Сlients', url='https://educity.tech/')
        collab3_us = types.InlineKeyboardButton('Employees', url='https://forms.gle/HdK6WwLUwKoG66wm9')
        backup_us = types.InlineKeyboardButton('🔁 Back to menu', callback_data='Collab_backup_us')
        markup.add(collab1_us, collab2_us, collab3_us, backup_us)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Start working with us", reply_markup=markup)




@bot.callback_query_handler(func=lambda call: call.data == "Back_Achievements_us" or call.data == "Back_Achievements_ru")
def back_achievements(call):
    if call.data == "Back_Achievements_us":
        markup_us = types.InlineKeyboardMarkup(row_width=2)
        item_backup_coop_us = types.InlineKeyboardButton("🤝 Сollaboration", callback_data="Collab_us")
        item_achievements_us = types.InlineKeyboardButton("🏆 Achievements", callback_data="Achievements_us")
        item_backup_us = types.InlineKeyboardButton("🔁 Back", callback_data="Back_info_us1")
        markup_us.add(item_backup_coop_us, item_achievements_us, item_backup_us)
        bot.edit_message_text(
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            text='<b>Educity</b> is a product for teaching foreign languages using VR technologies, by immersing the user in a virtual environment with the effect of maximum presence.'
                 '\n\n<b>The Educity project is unique and allows users to:</b>\n- Increase motivation when learning foreign languages'
                 '\n- Avoid embarrassment and fear when learning'
                 '\n- Practice your skills using real examples'
                 '\n- Adapt faster when moving or a one-time trip to another country'
                 '\n- Diversify the teacher’s lesson with the use of virtual reality'
                 '\n- Become more familiar with the culture and habits of the countries of the language you are learning, as well as interact with them directly',
            reply_markup=markup_us,
            parse_mode='html'
        )
    elif call.data == "Back_Achievements_ru":
        markup_ru = types.InlineKeyboardMarkup(row_width=2)
        item_backup_coop_ru = types.InlineKeyboardButton("🤝 Сотрудничество", callback_data="Collab_ru")
        item_achievements_ru = types.InlineKeyboardButton("🏆 Достижения", callback_data="Achievements_ru")
        item_backup_ru = types.InlineKeyboardButton("🔁 Назад", callback_data="Back_info_ru1")
        markup_ru.add(item_backup_coop_ru, item_achievements_ru, item_backup_ru)
        bot.edit_message_text(
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            text='<b>Educity</b> это продукт, по обучению иностранным языкам на базе VR технологий, путем погружения пользователя в виртуальную среду с эффектом максимального присутствия. '
                 '\n\n<b>Проект Educity уникальный и позволяет пользователям:</b> '
                 '\n- Повысить мотивацию при изучении иностранных языков '
                 '\n- Избежать стеснения и страха при обучении'
                 '\n- Отрабатывать свои навыки на реальных примерах'
                 '\n- Быстрее адаптировать при переезде или разовой поездке в другую страну '
                 '\n- Разнообразить урок педагога с применение виртуальной реальности'
                 '\n- Ближе ознакомиться с культурой и привычками стран изучаемого языка, а также повзаимодействовать с ними напрямую',
            reply_markup=markup_ru,
            parse_mode='html'
        )


@bot.callback_query_handler(func=lambda call: call.data == "Achievements_us" or call.data == "Achievements_ru")
def get_achievements(call):
    if call.data == "Achievements_us":
        markup_ru = types.InlineKeyboardMarkup(row_width=1)
        item_backup_ru = types.InlineKeyboardButton("🔁 Back", callback_data="Back_Achievements_us")
        markup_ru.add(item_backup_ru)
        bot.edit_message_text(
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            text=" ✅  Winners of the regional grand in the medical field."
                 "\n✅  We specialize in developments in the fields of education, medicine, and construction."
                 "\n✅  We have been successfully implementing projects since 2021."
                 "\n✅  We are residents of IT Park",
            reply_markup=markup_ru
        )

    elif call.data == "Achievements_ru":
        markup_ru = types.InlineKeyboardMarkup(row_width=1)
        item_backup_ru = types.InlineKeyboardButton("🔁 Назад", callback_data="Back_Achievements_ru")
        markup_ru.add(item_backup_ru)
        bot.edit_message_text(
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            text=" ✅  Победители регионального гранда в медицинской сфере."
                 "\n✅  Специализируемся на разработках в областях образования, медицины, строительства."
                 "\n✅  Успешно реализовываем проекты с 2021 года."
                 "\n✅  Являемся резидентами ИТ Парка",
            reply_markup=markup_ru
        )




@bot.callback_query_handler(func=lambda call: call.data == 'FAQ_us' or call.data == 'FAQ_ru')
def callback_handler(call):
    if call.data == 'FAQ_us':
        markup_us = types.InlineKeyboardMarkup(row_width=2)
        faq1_us = types.InlineKeyboardButton("What is EduCity", callback_data='q1_us')
        faq2_us = types.InlineKeyboardButton("Presentation", url='https://disk.yandex.ru/i/7M2xtXTqzPkF4Q')
        faq3_us = types.InlineKeyboardButton("Metaverse", url='https://www.youtube.com/watch?v=jFUVZDPrB7U')
        faq4_us = types.InlineKeyboardButton("White Paper", url='https://educity.tech/')
        # Добавьте сюда другие кнопки, если нужно.
        back_us = types.InlineKeyboardButton("🔁 Back", callback_data='Return_us1')
        markup_us.add(faq1_us, faq2_us, faq3_us, faq4_us, back_us)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Find out more about project and get a White Paper",reply_markup=markup_us)

    elif call.data == 'FAQ_ru':
        markup_ru = types.InlineKeyboardMarkup(row_width=2)
        faq1_ru = types.InlineKeyboardButton("Что такое EduCity", callback_data='q1_ru')
        faq2_ru = types.InlineKeyboardButton("Презентация", url='https://disk.yandex.ru/i/7M2xtXTqzPkF4Q')
        faq3_ru = types.InlineKeyboardButton("Метавселенная", url='https://www.youtube.com/watch?v=znX1Hdyq9l8')
        faq4_ru = types.InlineKeyboardButton("White Paper", url='https://educity.tech/')
        back_ru = types.InlineKeyboardButton("🔁 Назад", callback_data='Return_ru1')
        markup_ru.add(faq1_ru, faq2_ru, faq3_ru, faq4_ru, back_ru)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text="Узнайте больше о проекте и получите White Paper", reply_markup=markup_ru)





@bot.message_handler(content_types=['photo', 'audio', 'document', 'video', 'text' ])
def wrong(message):
    markup = types.InlineKeyboardMarkup()
    item1 = types.InlineKeyboardButton("🇬🇧 English", callback_data='English')
    item2 = types.InlineKeyboardButton("🇷🇺 Русский", callback_data='Russian')
    markup.add(item1, item2)
    bot.send_message(message.chat.id, "Choose your language/Выберите свой язык", reply_markup=markup)


bot.polling(none_stop=True)