# disnake 외 타 라이브러리도 같은 방식으로 가능합니다.
import disnake, threading, asyncio
from disnake.ext import commands
TOKENS = ["토큰1", "토큰2"] # 구동할 토큰들

async def Tasks(TOKEN):
    bot = commands.InteractionBot(intents=disnake.Intents.all())
    # 여기에 모든 코드, 인터렉션, 함수, 데코레이터 등등 입력
    # @bot.slash_command(name="테스트", description="테스트 메시지 출력")
    # async def callback(interaction):
    #   embed = disnake.Embed(title='테스트')
    #   await interaction.response.send_message(embed=embed)
    await bot.start(TOKEN)

# 토큰마다 1개의 스레드 생성, asyncio로 토큰마다 비동기 실행
threads = []
for TOKEN in TOKENS:
    thread = threading.Thread(target=asyncio.run, args=(Tasks(TOKEN),))
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()
