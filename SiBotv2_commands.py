import random
import discord
import datetime
from discord.ext import commands
from discord import FFmpegPCMAudio

intents = discord.Intents.default()
intents.members = True
client = commands.Bot(command_prefix='!', intents=intents)

darth_vader = ['DarthVader', 'darthvader', 'DARTHVADER', 'VADER', 'vader', 'Vader']

response_darth_vader = ['I Find Your Lack Of Faith, DISTURBING.',
                        "When I left you, I was But The Learner. Now I Am The Master",
                        'He\'s As Clumsy As He Is Stupid.',
                        'You Don’t Know The Power Of The Dark Side! I Must Obey My Master.',
                        'This Will Be A Day Long Remembered. It Has Seen The End Of Kenobi. It Will Soon See The End Of The Rebellion.',
                        'Be Careful Not To Choke On Your Aspirations.', 'I Find Your Lack Of Faith Disturbing.',
                        'You Have Controlled Your Fear. Now, Release Your Anger. Only Your Hatred Can Destroy Me.']

batman = ['Batman', 'BATMAN', 'batman', 'bat', 'Bat', 'BAT']

response_batman = ['I Am The Vengeance. I Am The Knight. I Am Batman', 'I\'m The Goddamn Batman',
                   'I Wear A Mask. And That Mask, It’s Not To Hide Who I Am, But To Create What I Am.',
                   'You Can Never Escape Me. Bullets Don\'t Harm Me. Nothing Harms Me. But I Know Pain. I KNOW Pain. Sometimes I Share It. With Someone Like You.'
                   'No Miracles. No Mercy. No Redemption. No Heaven. No Hell. No Higher Power. Just Life. Just... Us.',
                   'All Men Have Limits. They Learn What They Are And Learn Not To Exceed Them. I Ignore Mine.',
                   'People Think It\'s An Obsession. A Compulsion. As If There Were An Irresistible Impulse To Act. It\'s Never Been Like That. I Chose This Life. I Know What I\'m Doing.',
                   'It’s Not Who I Am Underneath, But What I Do That Defines Me.',
                   'The World Only Makes Sense If You Force It To.',
                   'Yes, Father. I Shall Become A Bat',
                   'The Night Is Darkest Just Before The Dawn. And I Promise You, The Dawn Is Coming.',
                   'You Either Die A Hero Or Live Long Enough To See Yourself Become The Villain.',
                   'He’s The Hero Gotham Deserves, But Not The One It Needs Right Now.',
                   'As A man; I Am Flesh And Blood; I Can Be Ignored, I Can Be Destroyed. But As A symbol, I Can Be Incorruptible. I Can Be Everlasting.',
                   'No Miracles. No Mercy. No Redemption. No Heaven. No Hell. No Higher Power. Just Life, Just…Us.',
                   'A Hero Can Be Anyone. Even A Man Doing Something As Simple And Reassuring As Putting A Coat Around A Little Boy’s Shoulders To Let Him Know That The World Hadn’t Ended.']

joker = ['joker', 'Joker', 'JOKER']

response_joker = ['Why So Serious', 'The Only Sensible Way To Live In This World Is Without Rules.',
                  'Smile, Because It Confuses People. Smile, Because It’S Easier Than Explaining What Is Killing You Inside.',
                  'What Doesn’T Kill You, Simply Makes You Stranger!',
                  'As You Know, Madness Is Like Gravity…All It Takes Is A Little Push.',
                  'Let’S Put A Smile On That Face!',
                  'We Stopped Checking For Monsters Under Our Bed, When We Realized They Were Inside Us.',
                  'If You’Re Good At Something, Never Do It For Free.',
                  'When The Chips Are Down, These Civilized People, They’ll Eat Each Other.',
                  'Nobody Panics When Things Go “According To Plan”. Even If The Plan Is Horrifying!',
                  'They Laugh At Me Because I’M Different. I Laugh At Then Because The’Re All The Same',
                  'Why Don’T We Cut You Up Into Little Pieces And Feed You To Your Pooches? Hm? And Then We’ll See How Loyal A Hungry Dog Really Is.',
                  'Do I Really Look Like A Guy With A Plan? You Know What I Am? I’m A Dog Chasing Cars. I Wouldn’t Know What To Do With One If I Caught It! You Know, I Just… Do Things.',
                  'And I Won’t Kill You Because You’re Just Too Much Fun. I Think You And I Are Destined To Do This Forever.',
                  'See I’M A Man Of Simple Taste. I Like Things Such As Gunpowder…Dynamite And…Gasoline!',
                  'You See, I’M Not A Monster. I’M Just Ahead Of The Curb.',
                  'Ding Dong, The Bat Is Dead! Which Old Bat? The Dumb Old Bat! Ding Dong, The Dumb Old Bat Is Dead! Hahaha!']

master_chief = ['MasterChief', 'masterchief', 'MASTERCHIEF', 'chief', 'CHIEF', 'Chief', 'Demon', 'demon', 'DEMON']

response_master_chief = ['I Need A Weapon.', 'Sir, Finishing This Fight.', 'To Give The Covenant Back Their Bomb.',
                         'She Said That To Me Once... About Being A Machine.', 'Wake Me. When You Need Me.'
                                                                               'No, I Think We\'Re Just Getting Started.',
                         'We\'ll Make It.', 'Ready To Get Back To Work?',
                         'Our Duty, As Soldiers, Is To Protect Humanity... Whatever The Cost.']

cortana = ['Cortana', 'CORTANA', 'cortana']

response_cortana = ['Don\'t Make A Girl A Promise... If You Know You Can\'t keep It.',
                    'Like The Others, You Were Strong And Swift And Brave. A Natural Leader. But You Had Something They Didn\'t. Something No One Saw... But Me. Can You Guess? Luck. Was I Wrong?',
                    'Welcome Home, John.', 'It\'s Been An Honor Serving With You, John.', 'Wake Up, Chief. I Need You.',
                    'I Am Your Shield... I Am Your Sword.']

arbiter = ['arbiter', 'ARBITER', 'Arbiter']

response_arbiter = ['Where It So Easy', 'Release Me Or Kill Me, Parasite, But Do Not Waste My Time With Talk!',
                    'The Prophets Have Betrayed Us']

labuba = ['Tushi', 'tushi', 'TUSHI', 'tuhsi', 'TUHSI', 'Tuhsi']

response_lubaba = ['Cham Dia Par Pea Gelo', 'Chunni', 'Soitan',
                   'Tonjih, Meye Taa Khali Chup Kore Thake, Kono Kotha Bole na',
                   'Felix, Amar Janu Phaki Ta', 'Felix, Ore Amr Sona Taa Re', 'Simon, Amk Patta Dei Na',
                   'Simon Hates Me',
                   'Arthi Er Jamai, Sadman', 'Guys.............Gone', 'Amar Dara Kiccu Hobe Na',
                   'Mondira Amar Besty, Ami Orr Saate Sob Share Kori', 'Ajke Raat Ee Hobe Naki',
                   'Ami R Farhan Just Friend',
                   'Tumi Too Patta Dila Na', 'Afridi, I Am Missing You', 'Rabana Akta Bosti', 'Amr Kiccu Valo Laage Na',
                   'Ami R Nite Partesi Na', 'Simon, Khali Amr Pecce Laage', 'Fuck You', 'Love You',
                   'Guys, Jaa Kaise Sob Bomi Hoie Gese',
                   'Amr Kiccu Kaite Vallage Na', 'Amr Lovely Dovey Movies Vallage',
                   'Akta Tappor Dibo', 'Jongli & Janowar', 'Besi Besi']


@client.event
async def on_ready():
    print("Let Finish The Fight Together")


@client.command()
async def info(ctx):
    await ctx.send(ctx.guild)
    await ctx.send(ctx.author)
    await ctx.send(ctx.message.id)


@client.command()
async def today(ctx):
    current_time = datetime.datetime.now()
    time1 = current_time.strftime('%I:%M:%S')
    time2 = current_time.strftime('%H:%M:%S')
    date = current_time.strftime('%m/%d/%Y')
    day = current_time.today().strftime('%A')
    await ctx.send(f'Hello Master.\n'
                   f'Time In 12Hour Format : {time1}\n'
                   f'Time In 24Hour Format : {time2}\n'
                   f'Date: {date}\n'
                   f'Day: {day}')

    if str(ctx.message.author) == 'Chief#6121':
        # print(ctx.message.author)
        if current_time.today().strftime('%A') == 'Tuesday':
            if current_time.hour == 11:
                if current_time.minute >= 0 & current_time.minute <= 60:
                    await ctx.send(f'You Have CSE422 Lab Class Right Now. \n'
                                   f'Meet Link: https://meet.google.com/qpn-qdcu-hva')

            elif current_time.hour == 12:
                if current_time.minute >= 0 & current_time.minute <= 60:
                    await ctx.send(f'You Have CSE422 Lab Class Right Now. \n'
                                   f'Meet Link: https://meet.google.com/qpn-qdcu-hva')

            elif current_time.hour == 13:
                if current_time.minute >= 0 & current_time.minute <= 50:
                    await ctx.send(f'You Have CSE422 Lab Class Right Now. \n'
                                   f'Meet Link: https://meet.google.com/qpn-qdcu-hva')

            elif current_time.hour == 14:
                if current_time.minute >= 0 & current_time.minute <= 60:
                    await ctx.send(f'You Have CSE423 Lab Class Right Now. \n'
                                   f'Meet Link: https://meet.google.com/riz-wvcg-cnr')

            elif current_time.hour == 15:
                if current_time.minute >= 0 & current_time.minute <= 60:
                    await ctx.send(f'You Have CSE423 Lab Class Right Now. \n'
                                   f'Meet Link: https://meet.google.com/riz-wvcg-cnr')

            elif current_time.hour == 16:
                if current_time.minute >= 0 & current_time.minute <= 50:
                    await ctx.send(f'You Have CSE423 Lab Class Right Now. \n'
                                   f'Meet Link: https://meet.google.com/riz-wvcg-cnr')

            else:
                await ctx.send(f'You Have CSE422 Lab Class From 11:00AM - 1:50PM\n'
                               f'You Have CSE423 Lab Class From 2:00AM - 4:50PM.\n')

        elif current_time.today().strftime('%A') == 'Thursday':
            if current_time.hour == 11:
                if current_time.minute >= 0 & current_time.minute <= 60:
                    await ctx.send(f'You Have ANT101 Theory Class Right Now. \n'
                                   f'Meet Link: https://meet.google.com/vnb-acab-ybg')

            elif current_time.hour == 12:
                if current_time.minute >= 0 & current_time.minute <= 20:
                    await ctx.send(f'You Have ANT101 Theory Class Right Now. \n'
                                   f'Meet Link: https://meet.google.com/vnb-acab-ybg')

            elif current_time.hour == 12:
                if current_time.minute >= 30 & current_time.minute <= 60:
                    await ctx.send(f'You Have CSE421 Theory Class Right Now. \n'
                                   f'Class Will Be On Discord')

            elif current_time.hour == 13:
                if current_time.minute >= 30 & current_time.minute <= 50:
                    await ctx.send(f'You Have CSE421 Theory Class Right Now. \n'
                                   f'Class Will Be On Discord')

            elif current_time.hour == 14:
                if current_time.minute >= 0 & current_time.minute <= 60:
                    await ctx.send(f'You Have CSE423 Theory Class Right Now. \n'
                                   f'Meet Link: https://meet.google.com/riz-wvcg-cnr')

            elif current_time.hour == 15:
                if current_time.minute >= 0 & current_time.minute <= 20:
                    await ctx.send(f'You Have CSE423 Theory Class Right Now. \n'
                                   f'Meet Link: https://meet.google.com/riz-wvcg-cnr')

            elif current_time.hour == 15:
                if current_time.minute >= 30 & current_time.minute <= 60:
                    await ctx.send(f'You Have CSE422 Theory Class Right Now. \n'
                                   f'Meet Link: https://meet.google.com/edx-agqe-tyu')

            elif current_time.hour == 16:
                if current_time.minute >= 0 & current_time.minute <= 50:
                    await ctx.send(f'You Have CSE422 Theory Class Right Now. \n'
                                   f'Meet Link: https://meet.google.com/edx-agqe-tyu')

            else:
                await ctx.send(f'You Have ANT101 Class From 11:00AM - 12:20PM\n'
                               f'You Have CSE421 Theory Class From 12:30AM - 1:50PM\n'
                               f'You Have CSE423 Theory Class From Class 2:00AM - 3:20PM\n'
                               f'You Have CSE422 Theory Class From Class 3:30AM - 4:50PM.\n')

        elif current_time.today().strftime('%A') == 'Saturday':
            if current_time.hour == 8:
                if current_time.minute >= 0 & current_time.minute <= 60:
                    await ctx.send(f'You Have CSE421 Lab Class Right Now. \n'
                                   f'Class Will Be On Discord')

            elif current_time.hour == 9:
                if current_time.minute >= 0 & current_time.minute <= 60:
                    await ctx.send(f'You Have CSE421 Lab Class Right Now. \n'
                                   f'Class Will Be On Discord')

            elif current_time.hour == 10:
                if current_time.minute >= 0 & current_time.minute <= 50:
                    await ctx.send(f'You Have CSE421 Lab Class Right Now. \n'
                                   f'Class Will Be On Discord')

            elif current_time.hour == 11:
                if current_time.minute >= 0 & current_time.minute <= 60:
                    await ctx.send(f'You Have ANT101 Theory Class Right Now. \n'
                                   f'Meet Link: https://meet.google.com/vnb-acab-ybg')

            elif current_time.hour == 12:
                if current_time.minute >= 0 & current_time.minute <= 20:
                    await ctx.send(f'You Have ANT101 Theory Class Right Now. \n'
                                   f'Meet Link: https://meet.google.com/vnb-acab-ybg')

            elif current_time.hour == 12:
                if current_time.minute >= 30 & current_time.minute <= 60:
                    await ctx.send(f'You Have CSE421 Theory Class Right Now. \n'
                                   f'Class Will Be On Discord')

            elif current_time.hour == 13:
                if current_time.minute >= 30 & current_time.minute <= 50:
                    await ctx.send(f'You Have CSE421 Theory Class Right Now. \n'
                                   f'Class Will Be On Discord')

            elif current_time.hour == 14:
                if current_time.minute >= 0 & current_time.minute <= 60:
                    await ctx.send(f'You Have CSE423 Theory Class Right Now. \n'
                                   f'Meet Link: https://meet.google.com/riz-wvcg-cnr')

            elif current_time.hour == 15:
                if current_time.minute >= 0 & current_time.minute <= 20:
                    await ctx.send(f'You Have CSE423 Theory Class Right Now. \n'
                                   f'Meet Link: https://meet.google.com/riz-wvcg-cnr')

            elif current_time.hour == 15:
                if current_time.minute >= 30 & current_time.minute <= 60:
                    await ctx.send(f'You Have CSE422 Theory Class Right Now. \n'
                                   f'Meet Link: https://meet.google.com/edx-agqe-tyu')

            elif current_time.hour == 16:
                if current_time.minute >= 0 & current_time.minute <= 50:
                    await ctx.send(f'You Have CSE422 Theory Class Right Now. \n'
                                   f'Meet Link: https://meet.google.com/edx-agqe-tyu')

            else:
                await ctx.send(f'You Have CSE421 Lab From 8:00AM - 10:50PM\n'
                               f'You Have ANT101 Class From 11:00AM - 12:20PM\n'
                               f'You Have CSE421 Theory Class From 12:30AM - 1:50PM\n'
                               f'You Have CSE423 Theory Class From Class 2:00AM - 3:20PM\n'
                               f'You Have CSE422 Theory Class From Class 3:30AM - 4:50PM.\n')

        else:
            await ctx.send(f'You Have No Class Today, Have Fun')

    else:
        await ctx.send(f'You Are Not Authorized For This Action')

@client.command()
async def be(ctx, arg):
    if arg in darth_vader:
        number = random.randint(0, len(response_darth_vader) - 1)
        await ctx.send(f'{response_darth_vader[number]}')

    elif arg in batman:
        number = random.randint(0, len(response_batman) - 1)
        await ctx.send(f'{response_batman[number]} \U0001F987')

    elif arg in joker:
        number = random.randint(0, len(response_joker) - 1)
        await ctx.send(f'{response_joker[number]} \U0001F0CF')

    elif arg in master_chief:
        number = random.randint(0, len(response_master_chief) - 1)
        await ctx.send(f'{response_master_chief[number]}')

    elif arg in cortana:
        number = random.randint(0, len(response_cortana) - 1)
        await ctx.send(f'{response_cortana[number]} \U0001F916')

    elif arg in arbiter:
        number = random.randint(0, len(response_arbiter) - 1)
        await ctx.send(f'{response_arbiter[number]} \U0001F98E')

    elif arg in labuba:
        number = random.randint(0, len(response_lubaba) - 1)
        await ctx.send(f'{response_lubaba[number]}')


@client.command()
async def punch(ctx, arg):
    await ctx.send(f'SiBot Punched {arg} \U0001F44A.')


@client.command()
async def double_punch(ctx, arg1, arg2):
    await ctx.send(f'SiBot Punched Both {arg1} And {arg2} \U0001F44A.')


@client.command()
async def multi_punch(ctx, *args):
    everyone = ', '.join(args)
    await ctx.send(f'Sibot Punched {everyone} \U0001F44A.')


@client.command()
async def fuck(ctx, arg):
    await ctx.send(f'SiBot Fucked {arg} \U0001F595.')


@client.command()
async def threesome(ctx, arg1, arg2):
    await ctx.send(f'SiBot Fucked Both {arg1} And {arg2} \U0001F595.')


@client.command()
async def infintesome(ctx, *args):
    everyone = ', '.join(args)
    await ctx.send(f'Sibot Fucked {everyone} \U0001F595.')


@client.command(pass_context=True)
async def join(ctx):
    if ctx.author.voice:
        channel = ctx.message.author.voice.channel
        voice = await channel.connect()
        source = FFmpegPCMAudio('Halo 4 OST  117_1080p.wav')
        player = voice.play(source)

    else:
        await ctx.send("You Are Not In Voice, Master.")


@client.command(pass_context=True)
async def leave(ctx):
    if ctx.voice_client:
        await ctx.guild.voice_client.disconnect()
        await ctx.send(f'Goodbye Master \U0001F61E.')

    else:
        await ctx.send(f"You Are Not In Voice \U0001F613.")


@client.command(pass_context=True)
async def pause(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_playing:
        voice.pause()
    else:
        await ctx.send("Sorry Nothing To Play, Master.")


@client.command(pass_context=True)
async def resume(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_paused:
        voice.resume()
    else:
        await ctx.send("Sorry Nothing to pause, Master.")


@client.command(pass_context=True)
async def stop(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    voice.stop()


@client.command(pass_context=True)
async def play(ctx, arg):
    voice = ctx.guild.voice_client
    source = FFmpegPCMAudio(arg + '.mp3')
    player = voice.play(source)


with open('token.0', 'r', encoding='utf-8') as f:
    bot_token = f.read()

client.run(bot_token)
