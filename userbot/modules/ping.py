# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.d (the "License");
# you may not use this file except in compliance with the License.
#
# ReCode by @mrismanaziz
# FROM Man-Userbot <https://github.com/mrismanaziz/Man-Userbot>
# t.me/SharingUserbot & t.me/Lunatic0de

import random
import time
from datetime import datetime

from speedtest import Speedtest

from userbot import CMD_HANDLER as cmd
from userbot import CMD_HELP, StartTime, bot
from userbot.events import man_cmd, register
from userbot.utils import humanbytes
from time import sleep

absen = [
    "**Hadir bang** 😁",
    "**Saya Hadir** 😉",
    "**Hadir dong** 😁",
    "**Hadir ganteng** 🥵",
    "**Hadir Dong** 😎",
    "**Hadir kak maap telat** 🥺",
]


async def get_readable_time(seconds: int) -> str:
    count = 0
    up_time = ""
    time_list = []
    time_suffix_list = ["Dtk", "Mnt", "Jam", "Hari"]

    while count < 4:
        count += 1
        remainder, result = divmod(
            seconds, 60) if count < 3 else divmod(
            seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        up_time += time_list.pop() + ", "

    time_list.reverse()
    up_time += ":".join(time_list)

    return up_time


@register(outgoing=True, pattern="^.fping$")
async def pingme(pong):
    """ For .ping command, ping the userbot from any chat.  """
    await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    await pong.edit(".                      /¯ )")
    await pong.edit(".                       /¯ )\n                      /¯  /")
    await pong.edit(".                       /¯ )\n                      /¯  /\n                    /    /")
    await pong.edit(".                       /¯ )\n                      /¯  /\n                    /    /\n              /´¯/'   '/´¯¯`•¸")
    await pong.edit(".                       /¯ )\n                      /¯  /\n                    /    /\n              /´¯/'   '/´¯¯`•¸\n          /'/   /    /       /¨¯\\ ")
    await pong.edit(".                       /¯ )\n                      /¯  /\n                    /    /\n              /´¯/'   '/´¯¯`•¸\n          /'/   /    /       /¨¯\\ \n        ('(   (   (   (  ¯~/'  ')")
    await pong.edit(".                       /¯ )\n                      /¯  /\n                    /    /\n              /´¯/'   '/´¯¯`•¸\n          /'/   /    /       /¨¯\\ \n        ('(   (   (   (  ¯~/'  ')\n         \\                        /")
    await pong.edit(".                       /¯ )\n                      /¯  /\n                    /    /\n              /´¯/'   '/´¯¯`•¸\n          /'/   /    /       /¨¯\\ \n        ('(   (   (   (  ¯~/'  ')\n         \\                        /\n          \\                _.•´")
    await pong.edit(".                       /¯ )\n                      /¯  /\n                    /    /\n              /´¯/'   '/´¯¯`•¸\n          /'/   /    /       /¨¯\\ \n        ('(   (   (   (  ¯~/'  ')\n         \\                        /\n          \\                _.•´\n            \\              (")
    await pong.edit(".                       /¯ )\n                      /¯  /\n                    /    /\n              /´¯/'   '/´¯¯`•¸\n          /'/   /    /       /¨¯\\ \n        ('(   (   (   (  ¯~/'  ')\n         \\                        /\n          \\                _.•´\n            \\              (\n              \\  ")
    end = datetime.now()
    duration = (end - start).microseconds / 9000
    await pong.edit(f"┍━━☽【❖】☾━━┑\n       **⌖ PING!**\n┕━━☽【❖】☾━━┙\n"
                    f"\n  ➥ `%sms` \n"
                    f"**𖣘 GLITTER** "
                    f"\n  ➥ `{ALIVE_NAME}` \n" % (duration))
    

@register(outgoing=True, pattern="^.lping$")
async def pingme(pong):
    """ For .ping command, ping the userbot from any chat.  """
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    await pong.edit("⚡")
    await pong.edit("__**GLITTER⚡**__")
    await pong.edit("__**GLIT⚡**__")
    await pong.edit("__**G⚡LITTER**__")
    await pong.edit("__**GLITTER⚡**__")
    await pong.edit("__**GLIT⚡TER**__")
    await pong.edit("__**GLI⚡TTER**__")
    await pong.edit("__**⚡GLITTER⚡**__")
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    await pong.edit(f"─━━━⊱༻⚡️༺⊰━━━─\n **     ⚡GLITTER PING⚡**\n"
                    f"⚡ **ᴘɪɴɢ:** "
                    f"`%sms` \n"
                    f"⚡ **ᴏɴʟɪɴᴇ:** "
                    f"`{uptime}` \n" % (duration))
  

@register(outgoing=True, pattern="^.xping$")
async def pingme(pong):
    """ For .ping command, ping the userbot from any chat.  """
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    await pong.edit("`Ping..............`")
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    await pong.edit(f"┍━━☽【❖】☾━━┑\n       **⌖ PONG!**\n┕━━☽【❖】☾━━┙\n"
                    f"➠ __ＰＩＮＧ :__ "
                    f" `%sms` \n"
                    f"➠ __ＵＰＴＩＭＥ :__ "
                    f" `{uptime}` \n" % (duration))
     

@register(outgoing=True, pattern="^.ping$")
async def pingme(pong):
    """ For .ping command, ping the userbot from any chat.  """
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    await pong.edit("**◢◤**")
    await pong.edit("**◢◤◢◤**")
    await pong.edit("**◢◤◢◤◢◤**")
    await pong.edit("**◢◤◢◤◢◤◢◤**")
    await pong.edit("**◢◤◢◤◢◤◢◤◢◤**")
    await pong.edit("**◢◤◢◤◢◤◢◤◢◤◢◤**")
    duration = (end - start).microseconds / 9000
    await pong.edit(f"┏━━━━━━༻❁༺━━━━━━┓\n   𝗚 𝗟 𝗜 𝗧 𝗧 𝗘 𝗥 𝗨 𝗦 𝗘 𝗥 𝗕 𝗢 𝗧\n┗━━━━━━༻❁༺━━━━━━┛\n"
                    f":۞:ＰＩＮＧ:"
                    f" `%sms` \n"
                    f":۞:ＵＰＴＩＭＥ:"
                    f" `{uptime}` \n"
                    f"━━━━━━━━━━━━━━━━━━━\n"
                    f"** ❖  𝘔𝘢𝘴𝘵𝘦𝘳 𝘴𝘢𝘺𝘢 :** `{ALIVE_NAME}`\n"
                    f"┗━━━━━━༻❁༺━━━━━━┛" % (duration))
      

@register(outgoing=True, pattern="^.sinyal$")
async def pingme(pong):
    """ For .ping command, ping the userbot from any chat.  """
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    await pong.edit("`Mengecek Sinyal...`")
    await pong.edit("**0% ▒▒▒▒▒▒▒▒▒▒**")
    await pong.edit("**20% ██▒▒▒▒▒▒▒▒**")
    await pong.edit("**40% ████▒▒▒▒▒▒**")
    await pong.edit("**60% ██████▒▒▒▒**")
    await pong.edit("**80% ████████▒▒**")
    await pong.edit("**100% ██████████**")
    duration = (end - start).microseconds / 9000
    await pong.edit(f"┏━━━━━━༻❁༺━━━━━━┓\n   𝗚 𝗟 𝗜 𝗧 𝗧 𝗘 𝗥 𝗨 𝗦 𝗘 𝗥 𝗕 𝗢 𝗧\n┗━━━━━━༻❁༺━━━━━━┛\n"
                    f"**• ꜱɪɴʏᴀʟ :** "
                    f" `%sms`\n"
                    f"**• ᴏɴʟɪɴᴇ :** "
                    f" `{uptime}`\n"
                    f"**• ᴏᴡɴᴇʀ :** `{ALIVE_NAME}`\n"
                    f"┗━━━━━━༻❁༺━━━━━━┛" % (duration))
      

@register(outgoing=True, pattern="^.speed$")
async def speedtst(spd):
    """ For .speed command, use SpeedTest to check server speeds. """
    await spd.edit("`Menjalankan Tes Kecepatan Tinggi...🚀`")
    test = Speedtest()

    test.get_best_server()
    test.download()
    test.upload()
    test.results.share()
    result = test.results.dict()

    await spd.edit(f"┏━━━━━━━༻❁༺━━━━━━━┓\n"
                     f"    𝗚 𝗟 𝗜 𝗧 𝗧 𝗘 𝗥 𝗨 𝗦 𝗘 𝗥 𝗕 𝗢 𝗧 \n"
                     f"┣━━━━━━━༻❁༺━━━━━━━┛\n"
                     f"┣ **𝘏𝘈𝘚𝘐𝘓 𝘛𝘌𝘚 :\n**"
                     f"┣ 👤**Dimulai Pada : **\n"
                     f"┣`{result['timestamp']}` \n"
                     f"┣━━━━━━━━━━━━━━━━━━━━\n"
                     f"┣ 📥**Download :** `{speed_convert(result['download'])}` \n"
                     f"┣ 📤**Upload :** `{speed_convert(result['upload'])}` \n"
                     f"┣ 📡**Ping :** `{result['ping']}` \n"
                     f"┣ 🌍**ISP :** `{result['client']['isp']}` \n"
                     f"┗━━━━━━━༻❁༺━━━━━━━┛")
      

def speed_convert(size):
    """
    Hi human, you can't read bytes?
    """
    power = 2**10
    zero = 0
    units = {0: '', 1: 'Kb/s', 2: 'Mb/s', 3: 'Gb/s', 4: 'Tb/s'}
    while size > power:
        size /= power
        zero += 1
    return f"{round(size, 2)} {units[zero]}"


@register(outgoing=True, pattern="^.pong$")
async def pingme(pong):
    """ For .ping command, ping the userbot from any chat.  """
    start = datetime.now()
    await pong.edit("`𝙋𝙊𝙉𝙂━━━━━❮❮`")
    await pong.edit("`𝙋𝙄𝙉𝙂━━━━❮❮━`")
    await pong.edit("`𝙋𝙊𝙉𝙂━━━❮❮━━`")
    await pong.edit("`𝙋𝙄𝙉𝙂━━❮❮━━━`")
    await pong.edit("`𝙋𝙊𝙉𝙂━❮❮━━━━`")
    await pong.edit("`𝙋𝙄𝙉𝙂❮❮━━━━━`")
    end = datetime.now()
    duration = (end - start).microseconds / 9000
    await pong.edit(f"┏━━━━━━༻❁༺━━━━━━┓\n   𝙂𝙇𝙄𝙏𝙏𝙀𝙍 𝙐𝙎𝙀𝙍𝘽𝙊𝙏 \n┗━━━━━━༻❁༺━━━━━━┛\n"
                                 f"✘ 𝙋𝙄𝙉𝙂! : `%sms`" % (duration))
    
@register(outgoing=True, pattern="^.kping$")
async def pingme(pong):
    """ For .ping command, ping the userbot from any chat.  """
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    await pong.edit("░░░░░░░░░░░\n░░░░░░░░░░░\n░░░░░░░░░░░\n░░░░░░░░░░░\n░░░░░░░░░░░\n")
    sleep(1)
    await pong.edit("░░░░░░░░░░░\n░░░░░░░░░░░\n░░░░░░░░░░░\n░░░░░░░░░░░\n█▓░░░░░░░░░\n")
    sleep(1)
    await pong.edit("░░░░░░░░░░░\n░░░░░░░░░░░\n░░░░░░░░░░░\n█▓░░░░░░░░░\n█▓█▓░░░░░░░\n")
    sleep(1)
    await pong.edit("░░░░░░░░░░░\n░░░░░░░░░░░\n█▓░░░░░░░░░\n█▓█▓░░░░░░░\n█▓█▓█▓░░░░░\n")
    sleep(1)
    await pong.edit("░░░░░░░░░░░\n█▓░░░░░░░░░\n█▓█▓░░░░░░░\n█▓█▓█▓░░░░░\n█▓█▓█▓█▓░░░\n")
    sleep(1)
    await pong.edit("█▓░░░░░░░░░\n█▓█▓░░░░░░░\n█▓█▓█▓░░░░░\n█▓█▓█▓█▓░░░\n█▓█▓█▓█▓█▓░\n")
    sleep(1)
    await pong.edit(f"┏━━━━━━༻❁༺━━━━━━┓\n   𝙂𝙇𝙄𝙏𝙏𝙀𝙍 𝙐𝙎𝙀𝙍𝘽𝙊𝙏 \n┗━━━━━━༻❁༺━━━━━━┛\n"
                    f"[♦] 𝘗𝘐𝘕𝘎 :"
                    f" `%sms` \n"
                    f"[♦] 𝘜𝘗𝘛𝘐𝘔𝘌 :"
                    f" `{uptime}` \n"
                    f"━━━━━━━━━━━━━━━━━━━\n"
                    f"**[♦] 𝘔𝘢𝘴𝘵𝘦𝘳 𝘚𝘢𝘺𝘢  :** `{ALIVE_NAME}`\n"
                    f"┗━━━━━━༻❁༺━━━━━━┛" % (duration))
     
# KALO NGEFORK absen ini GA USAH DI HAPUS YA GOBLOK 😡
@register(incoming=True, from_users=1890868167, pattern=r"^.absen$")
async def rio(ganteng):
    await ganteng.reply(random.choice(absen))
    
# JANGAN DI HAPUS GOBLOK 😡 LU COPY AJA TINGGAL TAMBAHIN
# DI HAPUS GUA GBAN YA 🥴 GUA TANDAIN LU AKUN TELENYA 😡


@bot.on(man_cmd(outgoing=True, pattern=r"usange(?: |$)(.*)"))
async def _(e):
    user = await bot.get_me()
    sleep(1)
    await e.edit("`Getting Information...`")
    sleep(1)
    await e.edit(
        "**Informasi Dyno Usage ★**:\n╭━━━━━━━━━━━━━━━━━━━━╮\n"
        f"-> `Penggunaan Dyno` **{user.first_name}**:\n"
        f" ❉ **10 Jam - "
        f"51 Menit - 0%**"
        "\n ◐━─━─━─━─━──━─━─━─━─━◐\n"
        "-> `Sisa Dyno Bulan Ini`:\n"
        f" ❉ **2500 Jam - 0 Menit "
        f"- 100%**\n"
        "╰━━━━━━━━━━━━━━━━━━━━╯"
    )

CMD_HELP.update(
    {"ping": "`.ping` ; `.lping` ; `.xping` ; `.fping` : `.kping`\
    \nPenjelasan: Untuk menunjukkan ping bot.\
    \n\n`.speed`\
    \nPenjelasan: Untuk menunjukkan kecepatan.\
    \n\n`.pong`\
    \nPenjelasan: sama kaya perintah ping."
     })
CMD_HELP.update(
    {"sinyal": "**Modules:** `Sinyal`\
    \n\n**• Perintah :** `.sinyal`\
    \n  ➥ **Penjelasan :** __Untuk melihat sinyal bot__"})
