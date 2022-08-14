#By MaxProgramm
#https://github.com/MaxProgramm
#The Bot's job is, to sort new rules on the discord server of the asocial network.
#The bot token can be entered in the config.json.
#The id's for the input and output channels can be entered in the config.json.
#The Prefix for the bot, can be changed in the config.json, standard is "!X"

import discord
import json

def get_config(key):
    f = open("config.json", "r")
    json_file = json.load(f)
    f.close()
    return json_file[key]

bot_token = get_config("bot_token")
command_prefix = get_config("command_prefix")
user_input_channel = get_config("channels")["user_input_channel_id"]
bot_output_channel = get_config("channels")["bot_output_channel_id"]


def get_info(msg):
    text = str(msg.content)
    list = text.split(maxsplit=2)
    x_num = str(list[1])
    content = str(list[2])
    author = msg.author
    return (x_num, content, author)


class MyClient(discord.Client):
    #Login
    async def on_ready(self):
        print("The bot has started successfully and is now ready!")


    #gets message
    async def on_message(self, message):
        if message.author != client.user:
            print("Received a message from " + str(message.author) + ", which contains the following content " + str(message.content))
            if message.channel == client.get_channel(id=user_input_channel):
                if message.content[0:2] == command_prefix:
                    #print("message starts correct")
                    x_num, content, author = get_info(message)
                    await client.get_channel(bot_output_channel).send("Gebot " + x_num + " von " + str(author) + ": " + content)
                else:
                    print("The message does not start with the correct prefix. The correct prefix is the following text: " + command_prefix)



client = MyClient()
client.run(bot_token)

