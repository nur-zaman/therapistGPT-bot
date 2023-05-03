import os
import discord
from dotenv import load_dotenv
from revChatGPT.V1 import Chatbot


load_dotenv()


CHATGPT_TOKEN = os.getenv("CHATGPT_TOKEN")
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")


config = {"access_token": CHATGPT_TOKEN}


chatbot = Chatbot(config, conversation_id=None)


def readInitPrompt(file_path):
    with open(file_path, "r") as f:
        content = f.read()
    return content


def generate_response(prompt):
    response = ""
    for data in chatbot.ask(prompt):
        response = data["message"]
    return response


intents = discord.Intents.all()
intents.members = True
intents.message_content = True
client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f"Logged in as {client.user} (ID: {client.user.id})")


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    prompt = message.content
    response = generate_response(prompt)

    reply = f"{response}"
    await message.reply(reply, mention_author=False)
    print("message:", prompt)
    print("response:", response)


if __name__ == "__main__":
    initPrompt = readInitPrompt(r"./prompt.txt")
    print(generate_response(initPrompt))
    client.run(DISCORD_TOKEN)
