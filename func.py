def get_sex(message):
    global coef
    if message.text == 'Мужской':
        coef = 0.69
    elif message.text == 'Женский':
        coef = 0.65
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Полный")
    btn2 = types.KeyboardButton("Пустой")
    markup.add(btn1,btn2)
    bot.send_message(message.chat.id, "Выберите наполненость желудка",reply_markup=markup)
    bot.register_next_step_handler(message, get_stomach)
    
    
def get_stomach(message):
    global stomach_coef
    if message.text == 'Полный':
        stomach_coef = 1
    elif message.text == 'Пустой':
        stomach_coef = 1.14
    bot.send_message(message.chat.id, "Введите вес",reply_markup=types.ReplyKeyboardRemove())
    bot.register_next_step_handler(message, get_weight)



def get_weight(message):
    global weight
    try:
        weight = int(message.text)
    except Exception:
        bot.send_message(message.chat.id, "Неправильный ввод, повторите")
        bot.register_next_step_handler(message, get_weight)
    if weight != 0:
        bot.send_message(message.chat.id, "Введите объем")
        bot.register_next_step_handler(message, get_volume)

        
def get_volume(message):
    global volume
    try:
        volume = int(message.text)
    except:
        bot.send_message(message.chat.id, "Неправильный ввод объема, повторите")
        bot.register_next_step_handler(message, get_volume)

    bot.send_message(message.chat.id, "Введите крепость напитка")
    bot.register_next_step_handler(message, get_spirt)

def get_spirt(message):
    global spirt 
    try:
        spirt = int(message.text)
    except:
        bot.send_message(message.chat.id, "Неправильный ввод крепости, повторите")
        bot.register_next_step_handler(message, get_spirt)
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Получить результат!")
    markup.add(btn1)
    bot.send_message(message.chat.id, "Все готово!", reply_markup=markup)
    bot.register_next_step_handler(message, send_result)
   

def send_result(message):
    if message.text == "Получить результат!":
        global calc_in_blood 
        calc_in_blood = (((spirt/100*volume)/weight*coef)*stomach_coef)
        if 0.3 > calc_in_blood:
            bot.send_message(message.chat.id, text = "Ваше значение: " + str(round(calc_in_blood,3))
            + "\nУ вас нет опьянения")
        elif 0.3 <= calc_in_blood < 0.5:
            bot.send_message(message.chat.id, text = "Ваше значение: " + str(round(calc_in_blood,3))
            + "\nУ вас незначительное опьянение")
        elif 0.5 <= calc_in_blood < 1.5:
            bot.send_message(message.chat.id, text = "Ваше значение: " + str(round(calc_in_blood,3))
            + "\nУ вас легкое опьянение")
        elif 1.5 <= calc_in_blood < 2.5:
            bot.send_message(message.chat.id, text = "Ваше значение: " + str(round(calc_in_blood,3))
            + "\nУ вас среднее опьянение")
        elif 2.5 <= calc_in_blood < 3:
            bot.send_message(message.chat.id, text = "Ваше значение: " + str(round(calc_in_blood,3))
            + "\nУ вас сильное опьянение")
        elif 3 <= calc_in_blood <= 5:
            bot.send_message(message.chat.id, text = "Ваше значение: " + str(round(calc_in_blood,3))
            + "\nУ вас тяжелое опьянение")