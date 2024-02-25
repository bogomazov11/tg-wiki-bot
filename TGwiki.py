import telebot, wikipedia, re
token = '7174510511:AAF5JIukWk2PAbTFNWdU6br1yWbDgV5-onc'
bot = telebot.TeleBot(token)

wikipedia.set_lang("ru")
def getwiki(s):
    try:
        np = wikipedia.page(s)

        wikitext = np.content[:1000]

        wikimas = wikitext.split('.')

        wikimas = wikimas[:-1]

        wikitext2 = ''

        for x in wikimas:
            if not('==' in x):
                if (len((x.strip())) > 3):
                    wikitext2 = wikitext2 + x + '.'
            else:
                break
        
        wikitext2=re.sub('\([^()]*\)', '', wikitext2)
        wikitext2=re.sub('\([^()]*\)', '', wikitext2)
        wikitext2=re.sub('\([^\{\}]*\}', '', wikitext2)
        return wikitext2
    except Exception as err:
        print('Не нашлось информации по этому запросу')
    
@bot.message_handler(commands=['start'])
def start(m, res=False):
    bot.send_message(m.chat.id, 'Отправьте мне слово, а я найду его значение на вики')

@bot.message_handler(content_types=['text'])
def hande_text(message):
    bot.send_message(message.chat.id, getwiki(message.text))

bot.polling(none_stop=True, interval=0)