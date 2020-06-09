import discord
import random
import os
import datetime
import openpyxl
from discord.ext import commands, tasks
from itertools import cycle

player_dict = dict()
client = discord.Client()
status = cycle (['Welcome to Felix Soft', '코인자동충전 시스템 탑재', '관리자가없을땐? !충전신청'])

@client.event
async def on_ready():
    change_message.start()
    print(client.user.id)
    print("How to Code a Python?")

def is_not_pinned(mess):
    return not mess.pinned
@client.event
async def on_member_join(member):
    if not member.bot:
        embed = discord.Embed(title='Welcome to Felix Soft'.format(member.name),
                              description='구매문의는 오직 Unknown에게만 해주세요 \n 관리자가 답변이 늦을수있으니 양해바랍니다.',
                              color=0xff8080)
        try:
            if not member.dm_channel:
                await member.create_dm()
            await member.dm_channel.send(embed=embed);
        except discord.errors.Forbidden:
            print(''.format(member.name))


@client.event
async def on_message(message):
    if message.content.startswith("안녕"):
        await message.channel.send("반가워요!")
    if message.content.startswith("잘가"):
        await message.channel.send("다음에 또 만나요. ^^b")

    if message.content.startswith("!정보"):
        date = datetime.datetime.utcfromtimestamp(((int(message.author.id) >> 22) + 1420070400000) / 1000)
        embed = discord.Embed(color=0xff8080)
        embed.add_field(name="Name", value=message.author.name, inline=True)
        embed.add_field(name="Nickname", value=message.author.display_name, inline=True)
        embed.add_field(name="Birthday", value=str(date.year) + "년" + str(date.month) + "월" + str(date.day) + "일", inline=True)
        embed.set_thumbnail(url=message.author.avatar_url)
        await message.channel.send(embed=embed)

    if message.content.startswith("!개발자"):
        embed = discord.Embed(colour=0x22a7f0)
        embed.add_field(name='Devloperment', value='Unknown님이 절 만들어주셨어요.', inline=False)
        await message.channel.send(embed=embed)

    if message.content.startswith("!초대링크"):
        embed = discord.Embed(colour=0x22a7f0)
        embed.add_field(name='invite', value='https://discord.gg/Dx5rDbN', inline=False)
        await message.channel.send(embed=embed)

    if message.content.startswith("!도움말"):
        embed = discord.Embed(colour=0x22a7f0)
        embed.add_field(name='초대링크', value='!초대링크 : 서버초대 링크를 보여줍니다.', inline=False)
        embed.add_field(name='청소', value='!청소 : 정수제한없이 메세지 삭제가 가능합니다.', inline=False)
        embed.add_field(name='정보', value='!정보 : 자신의 이름/별명/디스코드 가입날짜를 보여줍니다.', inline=False)
        embed.add_field(name='개발자', value='!개발자 : 이봇을누가 개발했는지 알수있습니다.', inline=False)
        await message.channel.send(embed=embed)

    if message.content.startswith('!코인추가'):
        if message.author.permissions_in(message.channel).manage_messages:
         author = message.guild.get_member(int(message.content[9:27]))
        file = openpyxl.load_workbook('코인.xlsx')
        sheet = file.active
        why = str(message.content[28:])
        i = 1
        while True:
            if sheet["A" + str(i)].value == str(author):
                sheet['B' + str(i)].value = int(sheet["B" + str(i)].value) + 1
                file.save("코인.xlsx")
                if sheet["B" + str(i)].value == 2:
                    await message.channel.send(str(author) + "님에게 코인이 추가되었습니다.")
                else:
                    await message.channel.send(str(author) + "님에게 코인이 추가되었습니다.")
                    sheet["c" + str(i)].value = why
                break
            if sheet["A" + str(i)].value == None:
                sheet["A" + str(i)].value = str(author)
                sheet["B" + str(i)].value = 1
                sheet["c" + str(i)].value = why
                file.save("코인.xlsx")
                await message.channel.send(str(author) + "님에게 코인이 추가되었습니다.")
                break
            i += 1

    if "discord.gg" in message.content.lower():
        await message.delete()
        embed = discord.Embed(colour=0xff8080)
        embed.add_field(name='Anti advertisement Detected', value='안타깝게도 Anti advertisement(앞메방지)기능 넣어놨는데?', inline=False)
        await message.channel.send(embed=embed)
    if "everyone" in message.content.lower():
        await message.delete()
        embed = discord.Embed(colour=0xff8080)
        embed.add_field(name='Anti advertisement Detected', value='everyone 쓸려고하네 어림도없지 에베베벱베벱?~', inline=False)
        await message.channel.send(embed=embed)
    if "here" in message.content.lower():
        await message.delete()
        embed = discord.Embed(colour=0xff8080)
        embed.add_field(name='Anti advertisement Detected', value='everyone 막혀서 here할려함? 내가 그것도 생각못했을까봐? 좀더 분발해라 ㅋㅋㅋㅋ', inline=False)
        await message.channel.send(embed=embed)

    if message.content.startswith('!청소'):
        if message.author.permissions_in(message.channel).manage_messages:
            args = message.content.split(' ')
            if len(args) == 2:
                if args[1].isdigit():
                    count = int(args[1]) + 1
                    deleted = await message.channel.purge(limit=count, check=is_not_pinned)
                    await message.channel.send('{}개의 메세지가 삭제되었습니다.'.format(len(deleted) - 1))

    if message.content.startswith('!충전신청'):
        embed = discord.Embed(colour=0xff8080)
        embed.add_field(name='주의사항', value='관리자에게 핀번호를 보내주세요. \n Unknown을 제외한 다른분과 거래하다 생긴일은 책임지지않습니다.', inline=False)
        embed.add_field(name='충전안내', value='문화상품권(컬쳐랜드)만 받습니다 수수료는 없습니다.', inline=False)
        embed.add_field(name='거래완료', value='관리자가 확인을하면 코인을 지급합니다 \n 1코인당 5,000KRW이며 DB에 기록이남습니다. \n 이를 악용할시에 바로 밴입니다.', inline=False)
        await message.author.send(embed=embed)

@tasks.loop(seconds=5)
async def change_message():
    await client.change_presence(activity=discord.Game(next(status)))
access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
