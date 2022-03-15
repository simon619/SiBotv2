import random
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True
client = commands.Bot(command_prefix='!', intents=intents)

general_id_BotTesting = 2343252353
target_message_id = 3453453453  # https://discord.com/channels/-------/----------/------------
arthi_id = 'user_id'
tushi_id = 'user_id'
tonjih_id = 'user_id'
chief_id = 'user_id'


@client.event
async def on_ready():
    print("Let Finish The Fight Together")


@client.event
async def on_member_join(member):
    channel = client.get_channel(general_id_BotTesting)
    await channel.send(
        f'Spartans Never Die {member} \n'
        f'They Are Just Missing In Action'
    )


@client.event
async def on_member_remove(member):
    channel = client.get_channel(general_id_BotTesting)
    await channel.send("A Hero Need Not Speak, When He Is Gone the World Will Speak For Him")


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if ((list(message.content))[0]) == '!':
        return

    greeting = ['hi', 'Hi', 'HI', 'hello', 'Hello', 'HELLO', 'Wanna Play HALO!',
                'Remember We Are Allies, You Dumb Piece Of Crap.', 'Dude, Can I Be Your Friend.',
                'Our Duty As A Soldier Is Too Protect Humanity, What Ever The Cost.',
                'Beware Of Tushi.',
                'You\'re The Best!', 'Hooyah']

    arthi = ['arthi', 'Arthi', 'ARTHI', 'NOSHIN', 'noshin', 'Noshin']
    response_arthi = ['Hey Duded, Which Girl Has Been Added in Your List Today.',
                      'Start Coding.', 'Valhalla', 'Hello, Beautiful.', 'You Look Hot Today.']

    tonjih = ['tonjih', 'Tonjih', 'TONJIH']
    response_tonjih = ['Stop Eating Paracetamol Like A Candy.', 'Hello, Pantua\'s Friend.', 'You Such A Nice Girl.',
                       'You Look Hot Today.', 'Hello, Beautiful.', 'Farhan Said, \"I love YOu\" to YOu.']

    tushi = ['tushi', 'Tushi', 'TUSHI', 'Lubaba', 'LUBABA', 'lubaba']
    response_tushi = ['Shop Whinning Like A Child.', 'Tushi, The Prettiest', 'Hi, Tawab\'s Wife.',
                      'Hi, Saiful\'s Wife.', 'Hi, Tawhid\'s Wife.',
                      'Hi, Farhen er Bou.', 'Hi, Chunni er Jaan.', 'Hi, Umme\'s Besty.',
                      'You Betrayed My Master.',
                      'You Look Hot Today.', 'Hello, Beautiful.']

    samanta = ['Samanta', 'SAMANTA', 'samanta', 'Promita', 'PROMITA', 'promita']
    response_samanta = ['Hello, The Nicest Girl In The World', 'Stay Blessed.',
                        'My Master Said You will The Best Babysitter In World.']

    ayaz = ['shakin', 'SHAKIN', 'Shakin', 'sakin', 'SAKIN', 'Sakin', 'Ayaz', 'ayaz', 'AYAZ', 'Mamur', 'MAMUR', 'mamur']
    response_ayaz = ['Which Game You Want To Play.', 'Ley Play Some Videogames.', 'Come To Jessore.']

    leona = ['Leona', 'leona', 'LEONA']
    response_leona = ['My Master\'s Dear Stupid Sister', 'I Wish You Were At Jessore', 'Nothing Can Not Replace You']

    fuck = ['Fuck', 'FUCK', 'fuck', 'Fucking', 'fucking', 'FUCKING', 'FUCKED', 'Fucked', 'fucked']
    response_fuck = ['Dude, You Just Used The Holy Word.', 'Yeah! Fuck You Too, Bitch.', 'Dude, You Are Screwed']

    good = ['good job bot', 'great job bot', 'Great job bot', 'Good job bot', 'Good Job Bot', 'Great Job Bot'
                                                                                              'GREAT JOB BOT',
            'GOOD JOB BOT', 'GOOD BOY', 'GREAT BOY', 'good boy', 'great boy', 'Great boy',
            'Good boy', 'Good Boy', 'Great Boy']

    response_good = ['Thank You, Master', 'My Pleasure, Master', 'Anything For You Master']

    guys = ['guys', 'Guys', 'GUYS', 'guy', 'GUY', 'Guy']

    love = ['----', '----', '---'] #Your Crushes Name

    meet = ['MEET', 'meet', 'Meet']

    if message.content in greeting:
        number = random.randint(1, len(greeting) - 1)
        await message.channel.send(greeting[number])
        # await message.add_reaction("\U0001F44B")

    if message.content in arthi:
        number = random.randint(0, len(response_arthi) - 1)
        await message.channel.send(response_arthi[number])
        # await message.add_reaction("\U0001F49C")

    if message.content in tonjih:
        number = random.randint(0, len(response_tonjih) - 1)
        await message.channel.send(response_tonjih[number])
        # await message.add_reaction("\U0001F49A")

    if message.content in tushi:
        number = random.randint(0, len(response_tushi) - 1)
        await message.channel.send(response_tushi[number])
        # await message.add_reaction("\U0001F49B")

    if message.content in samanta:
        number = random.randint(0, len(response_samanta) - 1)
        await message.channel.send(response_samanta[number])
        # await message.add_reaction("\U0001F499")

    if message.content in ayaz:
        number = random.randint(0, len(response_ayaz) - 1)
        await message.channel.send(response_ayaz[number])
        # await message.add_reaction("\U0001F579")

    if message.content in leona:
        number = random.randint(0, len(response_leona) - 1)
        await message.channel.send(response_leona[number])
        # await message.add_reaction("\U0001F497")

    if message.content in fuck:
        number = random.randint(0, len(response_fuck) - 1)
        await message.channel.send(response_fuck[number])
        # await message.add_reaction("\U0001F595")

    if message.content in good:
        number = random.randint(0, len(response_good) - 1)
        await message.channel.send(response_good[number])
        await message.channel.send(f'\U0001F97A')
        # await message.add_reaction("\U0001F595")

    if message.content in guys:
        if str(message.author) == 'Tushi#8445':
            await message.channel.send(
                f'Farher er Bou, {message.author} Has Summoned <@{tonjih_id}>, <@{arthi_id}> and <@{chief_id}>')

        elif str(message.author) == 'Chief#6121':
            await message.channel.send(
                f'My Master, {message.author} Has Summoned <@{tonjih_id}>, <@{arthi_id}> and <@{tushi_id}>')

        elif str(message.author) == 'Noshin Arthi#3527':
            await message.channel.send(
                f'Sadman er Bou, {message.author} Has Summoned <@{chief_id}>, <@{tonjih_id}> and <@{tushi_id}>')

        elif str(message.author) == '18101176_Tonjih#4069':
            await message.channel.send(
                f'Faisal er Bou, {message.author} Has Summoned <@{chief_id}>, <@{tushi_id}> and <@{arthi_id}>')

        else:
            await message.channel.send(f'{message.author} Has Summoned @everyone')

    if message.content in love:
        if str(message.author) == 'Chief#6121':
            await message.channel.send(f'My Master\'s Own.\n'
                                       f' My Master\'s Love.\n'
                                       f'  My Master\'s Precious.\n'
                                       )

        elif str(message.author) == 'Leona#1471':
            await message.channel.send(f'Master <@{chief_id}> Requests You To Remove The Message Now')

        else:
            await message.channel.send(f'{message.author}, You Are Not Authorized To You This Word')

    if message.content in meet:
        if str(message.author) == 'Chief#6121':
            await message.channel.send(f'ANT101 Meet Link: https://meet.google.com/vnb-acab-ybg\n'
                                       f'CSE423 Theory meet Link: https://meet.google.com/riz-wvcg-cnr\n'
                                       f'CSE423 Lab Meet Link: https://meet.google.com/riz-wvcg-cnr\n'
                                       f'CSE421 Theory Class Will Be in Discord\n'
                                       f'CSE421 Lab Class Will Be in Discord\n'
                                       f'CSE422 Theory Meet Link: https://meet.google.com/edx-agqe-tyu\n'
                                       f'CSE422 Lab Meet Link: https://meet.google.com/qpn-qdcu-hva\n'
                                       )

        elif str(message.author) == '18101176_Tonjih#4069' or str(message.author) == 'Noshin Arthi#3527':
            await message.channel.send(f'ANT101 meet: https://meet.google.com/vnb-acab-ybg')

        else:
            await message.channel.send(f'You Are Not Authorized To Complete This Operation')

    temp = [message.content]
    List = temp[0].split()
    if len(List) > 1:
        for i in List:
            print(i)
            if i in greeting:
                number = random.randint(0, len(greeting) - 1)
                await message.channel.send(greeting[number])
                # await message.add_reaction("\U0001F44B")

            elif i in arthi:
                number = random.randint(0, len(response_arthi) - 1)
                await message.channel.send(response_arthi[number])
                # await message.add_reaction("\U0001F49C")

            elif i in tonjih:
                number = random.randint(0, len(response_tonjih) - 1)
                await message.channel.send(response_tonjih[number])
                # await message.add_reaction("\U0001F49A")

            elif i in tushi:
                number = random.randint(0, len(response_tushi) - 1)
                await message.channel.send(response_tushi[number])
                # await message.add_reaction("\U0001F49B")

            elif i in samanta:
                number = random.randint(0, len(response_samanta) - 1)
                await message.channel.send(response_samanta[number])
                # await message.add_reaction("\U0001F499")

            elif i in ayaz:
                number = random.randint(0, len(response_ayaz) - 1)
                await message.channel.send(response_ayaz[number])
                # await message.add_reaction("\U0001F579")

            elif i in leona:
                number = random.randint(0, len(response_leona) - 1)
                await message.channel.send(response_leona[number])
                # await message.add_reaction("\U0001F497")

            elif i in fuck:
                number = random.randint(0, len(response_fuck) - 1)
                await message.channel.send(response_fuck[number])
                # await message.add_reaction("\U0001F595")

            elif i in guys:
                if str(message.author) == 'Tushi#8445':
                    await message.channel.send(
                        f'Farhan er Bou, {message.author} Has Summoned <@{tonjih_id}>, <@{arthi_id}> and <@{chief_id}>')

                elif str(message.author) == 'Chief#6121':
                    await message.channel.send(
                        f'My Master, {message.author.mention} Has Summoned <@{tonjih_id}>, <@{arthi_id}> and <@{tushi_id}>')

                elif str(message.author) == 'Noshin Arthi#3527':
                    await message.channel.send(
                        f'Sadman er Bou, {message.author} Has Summoned <@{chief_id}>, <@{tonjih_id}> and <@{tushi_id}>')

                elif str(message.author) == '18101176_Tonjih#4069':
                    await message.channel.send(
                        f'Faisal er Bou, {message.author} Has Summoned <@{chief_id}>, <@{arthi_id}> and <@{tushi_id}>')

                else:
                    await message.channel.send(f'{message.author} Has Summoned @everyone')

            elif i in love:
                if str(message.author) == 'Chief#6121':
                    await message.channel.send(f'My Master\'s Own.\n'
                                               f' My Master\'s Love.\n'
                                               f'  My Master\'s Precious.\n'
                                               )

                elif str(message.author) == 'Leona#1471':
                    await message.channel.send(f'Master <@{chief_id}> Requests You To Remove The Message Now')

                else:
                    await message.channel.send(f'{message.author}, You Are Not Authorized To Use This Word Here')

            elif i in meet:
                if str(message.author) == 'Chief#6121':
                    await message.channel.send(f'ANT101 meet: https://meet.google.com/vnb-acab-ybg\n'
                                               f'CSE423 meet: https://meet.google.com/riz-wvcg-cnr\n'
                                               f'CSE421 Class Will Be in Discord\n'
                                               f'CSE422 meet: https://meet.google.com/edx-agqe-tyu\n'
                                               )

                elif str(message.author) == '18101176_Tonjih#4069' or str(message.author) == 'Noshin Arthi#3527':
                    await message.channel.send(f'ANT101 meet: https://meet.google.com/vnb-acab-ybg')

                else:
                    await message.channel.send(f'You Are Not Authorized To Complete This Operation')


@client.event
async def on_reaction_add(reaction, user):
    await reaction.message.channel.send(f'{user} Reacted with {reaction.emoji}')


@client.event
async def on_message_edit(before, after):
    await before.channel.send(
        f'{before.author} Edited a Message.\n'
        f'I Find Your Lack Your Seriousness Disturbing.\n'
        f'Before You Screwed: {before.content}\n'
        f'After: {after.content}'
    )


@client.event
async def on_raw_reaction_add(payload):
    if payload.message_id != target_message_id:
        return

    guild = client.get_guild(payload.guild_id)
    print(payload.emoji.name)

    if payload.emoji.name == '❤️':
        role = discord.utils.get(guild.roles, name='360')
        await payload.member.add_roles(role)

    elif payload.emoji.name == '🤓':
        role = discord.utils.get(guild.roles, name='thesis')
        await payload.member.add_roles(role)


@client.event
async def on_raw_reaction_remove(payload):
    if payload.message_id != target_message_id:
        return

    guild = client.get_guild(payload.guild_id)
    print(payload.emoji.name)
    member = guild.get_member(payload.user_id)

    if payload.emoji.name == '❤️':
        role = discord.utils.get(guild.roles, name='360')
        await member.remove_roles(role)

    elif payload.emoji.name == '🤓':
        role = discord.utils.get(guild.roles, name='thesis')
        await member.remove_roles(role)

with open('token.0', 'r', encoding='utf-8') as f:
    bot_token = f.read()

client.run(bot_token)
