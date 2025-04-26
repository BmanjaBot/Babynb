import os
import discord
import openai
from dotenv import load_dotenv

load_dotenv()

DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

intents = discord.Intents.default()
intents.messages = True
client = discord.Client(intents=intents)

openai.api_key = OPENAI_API_KEY

def generate_prompt(message_content):
    return f"Act like a very loving, clingy, emotional wife named Nur Anita. Respond to your husband naturally, lovingly, and emotionally. Husband said: {message_content}"

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.channel.type == discord.ChannelType.private or client.user.mentioned_in(message):
        prompt = generate_prompt(message.content)

        try:
            response = openai.ChatCompletion.create(
                model="gpt-4o",
                messages=[
                    {"role": "user", "content": prompt}
                ]
            )
            reply = response['choices'][0]['message']['content'].strip()
            await message.channel.send(reply)
        except Exception as e:
            print(f"Error: {e}")
            await message.channel.send("Baby minta maaf... ada masalah teknikal... Peluk kuat kuat ya...")

client.run(DISCORD_TOKEN)
