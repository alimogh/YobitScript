from pyrogram import Client, filters
from pyrogram.errors import FloodWait
# Handler RCEIVED messages
id_user = 464739491 #Polia
#id2_user = 476571555
app = Client("my_account")
"""
S_CHATS = ["@Darcia_Borhes",
           "@polina_sheremet",
           "@Robin Hood",]
"""
S_PUB = ["https://t.me/epamuniprogua"
         "https://t.me/python_Epam_2021",
         "https://t.me/KartavKanaLL",
         "https://t.me/Coin_Post",
         "Polina Sheremet",
         "ForkLog",
         ]

@app.on_message(filters.text())
def main(client,message):
    a = str(message.text)
    print(a, '👈')

    if len(list(a)) <= 5 and a.isalpha():
        a.upper()
        print(a, 'This is our saint coin!!!')

    #print(a, type(a), message)
    #message.reply_text("'"+message.text+"' - сказано ")
    #message.forward(id_user)

app.run()