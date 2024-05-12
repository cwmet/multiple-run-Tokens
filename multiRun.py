import disnake, threading, asyncio
from disnake.ext import commands

async def Tasks(TOKEN):
    bot = commands.InteractionBot(intents=disnake.Intents.all())
    # @bot.slash_command(name="테스트", description="테스트 메시지 출력")
    # async def callback(interaction):
    #   embed = disnake.Embed(title='테스트')
    #   await interaction.response.send_message(embed=embed)
    await bot.start(TOKEN)

async def RunTasks():
    TOKENS = ["토큰1", "토큰2"]
    TASKS = []
    for token in TOKENS:
        TASKS.append(asyncio.create_task(Tasks(token)))
    await asyncio.gather(*TASKS)

asyncio.run(RunTasks())
