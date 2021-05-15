from pyrogram import Client, filters
# Handler SENT messages
id_user = 464739491
app = Client("my_account")
# вызывается при появлении нового поста в одном из пабликов-доноров
@app.on_message(filters.me)
def main(client,message):
    for i in range (2):
        message.reply_text(message.text)
    message.forward(id_user)

app.run()