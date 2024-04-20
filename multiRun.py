import disnake, threading, asyncio
from disnake.ext import commands
TOKENS = ["토큰1", "토큰2"] # 구동할 토큰들

async def Tasks(TOKEN):
    bot = commands.InteractionBot(intents=disnake.Intents.all())
    # @bot.slash_command(name="테스트", description="테스트 메시지 출력")
    # async def callback(interaction):
    #   embed = disnake.Embed(title='테스트')
    #   await interaction.response.send_message(embed=embed)
    await bot.start(TOKEN)

threads = []
for TOKEN in TOKENS:
    thread = threading.Thread(target=asyncio.run, args=(Tasks(TOKEN),))
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()
