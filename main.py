import telebot
import requests
from fake_useragent import UserAgent
from bs4 import BeautifulSoup


bot = telebot.TeleBot('5379227949:AAEEFFpTUw968KIz7WyiRF_jWp_Gwg0uWI4')

@bot.message_handler(commands=['start'])
def start(message):
    mess = f'Привет, <b>{message.from_user.first_name}</b>. Введи имя персонажа или его сокращение🙃'
    bot.send_message(message.chat.id,  mess, parse_mode='html')
@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, '''Перед тем как отправить сообщение,убедитесь в правильности написания имени персонажа!
(Пример : pl, sf, Pudge, Dark willow)''')
@bot.message_handler()
def get_text(message):
    msg = message.text.lower().replace(' ','-')
    if msg == 'mereska':
        bot.send_message(message.chat.id , 'Ты даун')
    if msg == '94rix':
            bot.send_message(message.chat.id, 'Win rate : 0%')
    url = 'https://ru.dotabuff.com/heroes/' + str(msg)
    headers = {
        'User-Agent': UserAgent().random
    }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    hero_win_rate = soup.select('body > div.container-outer.seemsgood > div.skin-container > '
                                'div.container-inner.container-inner-content > div.header-content-container > '
                                'div.header-content > div.header-content-secondary > dl:nth-child(2) > dd > span')
    for hero in hero_win_rate:
        hero_win_rate_bot = hero.text
        print(hero_win_rate_bot)


        bot.send_message(message.chat.id, f'Win rate : {hero_win_rate_bot}' )






bot.polling(none_stop=True, interval=0)












