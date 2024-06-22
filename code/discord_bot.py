import discord
import g4f
import chatgpt


TOKEN = "your discord token"
intents = discord.Intents(messages=True, guilds=True)
intents.message_content = True
client = discord.Client(intents = intents)

client_chatGPTs = {}


@client.event
async def on_ready():
    print("good boyo online")


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    author_name = message.author.name

    if author_name not in client_chatGPTs.keys():
        client_chatgpt = chatgpt.ChatGpt()
        
        dictionary = {author_name: client_chatgpt}     
        client_chatGPTs.update(dictionary)

    client_chatgpt = client_chatGPTs[author_name]

    if message.content == '!reset':
        client_chatgpt.reset_chat_history()
        await message.channel.send("chat history reset")
    else:    
        response = client_chatgpt.send_message(message.content)    
        await message.channel.send(response)



client.run(TOKEN)    



