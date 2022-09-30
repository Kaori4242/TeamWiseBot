import telebot 
from telebot import types 
NeedMessage = False 
 
 
bot=telebot.TeleBot("5720749157:AAF5VGHzcH6vYzl5nuWrVeQtYA4n3aAmLsY") 
text = 'Привет! На связи команда Teamwise! Ниже, нажав на одну из кнопок, ты можешь выбрать нужные тебе функции. Удачи! ' 
OwnerId =  1480085685
TestId = 495365287
a = ({0})
@bot.message_handler(commands = ["start"]) 
def send_text(message): 
    print(message.chat.id) 
    markup=types.ReplyKeyboardMarkup(resize_keyboard=True) 
    item1=types.KeyboardButton("Анонимно задать свой вопрос") 
    item2 = types.KeyboardButton("Разработчик")
    item3 = types.KeyboardButton("Хочу в клуб!")
    markup.add(item1, item2) 
    bot.send_message(message.chat.id, text , reply_markup=markup) 
 
@bot.message_handler(content_types=['text']) 
def func(message):    
    if(message.text == "Анонимно задать свой вопрос"): 
      msg = bot.send_message(message.chat.id ,"Напиши свой вопрос и совсем скоро мы напишем про него пост! ", parse_mode='Markdown' ) 
      bot.register_next_step_handler(msg, input_promocod)  
    elif(message.text == "Разработчик"): 
      bot.send_message(message.chat.id ,"Привет! Меня зовут Асылхан. Хочешь бота, сайт или же приложение? Тогда тебе ко мне!\n Контакты:\ntelegram: @kaori_42\ninst: @kaori_42 ", parse_mode='Markdown' ) 
    elif(message.text == "Хочу в клуб!"): 
      msg = bot.send_message(message.chat.id ,"Напиши свое имя ", parse_mode='Markdown' ) 
      bot.register_next_step_handler(msg, input_name)  
      a.add(message.text)
      
      
     
        




def input_promocod(message):
    x = "Эй, Димаш! Там пришел новый вопрос. Самое время писать пост. Кстати, вот вопрос:\n"+ message.text    
    bot.send_message(TestId ,x, parse_mode='Markdown' )   
    bot.send_message(message.chat.id ,"Твой вопрос принят!", parse_mode='Markdown' )
    Message(message)
def input_name(message):
    msg = bot.send_message(message.chat.id ,"Напиши свой класс", parse_mode='Markdown' ) 
    bot.register_next_step_handler(msg, input_class)  
    a.add(message.text)
def input_class(message):
    msg = bot.send_message(message.chat.id ,"Напиши свой номер с Whatsapp ", parse_mode='Markdown' ) 
    bot.register_next_step_handler(msg, input_number)  
    a.add(message.text)
def input_number(message):
    bot.send_message(TestId ,"a[0]", parse_mode='Markdown' )   
    bot.send_message(message.chat.id ,"С тобой скоро свяжутся!", parse_mode='Markdown' )

def Message(message):
    bot.send_message(message.chat.id ,"Чтобы не пропускать новости и следить за жизнью клуба, подписывайся на наши странички!\ntelegram: https://t.me/kultuspeha\ninst: https://instagram.com/teamwise.nis?igshid=ZDU1ZDhlY2E=", parse_mode='Markdown' )  
    
     
 
bot.polling()