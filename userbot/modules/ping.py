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

absen = [
    "**Hadir bang** 😁",
    "**Hadir kak** 😉",
    "**Hadir dong** 😁",
    "**Hadir ganteng** 🥵",
    "**Hadir bro** 😎",
    "**Hadir kak maap telat** 🥺",
]


async def get_readable_time(seconds: int) -> str:
    count = 0
    up_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "Jam", "Hari"]

    while count < 4:
        count += 1
        remainder, result = divmod(seconds, 60) if count < 3 else divmod(seconds, 24)
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


@bot.on(man_cmd(outgoing=True, pattern=r"ping$"))
async def _(ping):
    """For .ping command, ping the userbot from any chat."""
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    await ping.edit("**◢◤**")
    await ping.edit("**◢◤◢◤**")
    await ping.edit("**◢◤◢◤◢◤**")
    await ping.edit("**◢◤◢◤◢◤◢◤**")
    await ping.edit("**◢◤◢◤◢◤◢◤◢◤**")
    await ping.edit("**◢◤◢◤◢◤◢◤◢◤◢◤**")
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    user = await bot.get_me()
    await ping.edit(
        f"┏━━━━━━༻❁༺━━━━━━┓\n   𝗥 𝗜 𝗢 𝗨 𝗦 𝗘 𝗥 𝗕 𝗢 𝗧\n┗━━━━━━༻❁༺━━━━━━┛\n"
                    f":۞:ＰＩＮＧ:"
                    f" `%sms` \n"
                    f":۞:ＵＰＴＩＭＥ:"
                    f" `{uptime}` \n"
                    f"━━━━━━━━━━━━━━━━━━━\n"
                    f"** ❖  𝘔𝘢𝘴𝘵𝘦𝘳 𝘴𝘢𝘺𝘢 :** `{ALIVE_NAME}`\n"
                    f"┗━━━━━━༻❁༺━━━━━━┛" % (duration))


@bot.on(man_cmd(outgoing=True, pattern=r"xping$"))
async def _(ping):
    """For .ping command, ping the userbot from any chat."""
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    await ping.edit("`Pinging....`")
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    await ping.edit(
        f"**PONG!! 🍭**\n**Pinger** : %sms\n**Bot Uptime** : {uptime}🕛" % (duration)
    )


@bot.on(man_cmd(outgoing=True, pattern=r"lping$"))
async def _(ping):
    """For .ping command, ping the userbot from any chat."""
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    await ping.edit("`𝙋𝙊𝙉𝙂━━━━━❮❮`")
    await ping.edit("`𝙋𝙄𝙉𝙂━━━━❮❮━`")
    await ping.edit("`𝙋𝙊𝙉𝙂━━━❮❮━━`")
    await ping.edit("`𝙋𝙄𝙉𝙂━━❮❮━━━`")
    await ping.edit("`𝙋𝙊𝙉𝙂━❮❮━━━━`")
    await ping.edit("`𝙋𝙄𝙉𝙂❮❮━━━━━`")
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    user = await bot.get_me()
    await ping.edit(
        f"┏━━━━━━༻❁༺━━━━━━┓\n   𝙍𝙄𝙊 𝙐𝙎𝙀𝙍𝘽𝙊𝙏 \n┗━━━━━━༻❁༺━━━━━━┛\n"
                                 f"✘ 𝙋𝙄𝙉𝙂! : `%sms`" % (duration))


@bot.on(man_cmd(outgoing=True, pattern=r"fping$"))
async def _(f):
    """For .ping command, ping the userbot from any chat."""
    await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    await f.edit(".                       /¯ )")
    await f.edit(".                       /¯ )\n                      /¯  /")
    await f.edit(
        ".                       /¯ )\n                      /¯  /\n                    /    /"
    )
    await f.edit(
        ".                       /¯ )\n                      /¯  /\n                    /    /\n              /´¯/'   '/´¯¯`•¸"
    )
    await f.edit(
        ".                       /¯ )\n                      /¯  /\n                    /    /\n              /´¯/'   '/´¯¯`•¸\n          /'/   /    /       /¨¯\\ "
    )
    await f.edit(
        ".                       /¯ )\n                      /¯  /\n                    /    /\n              /´¯/'   '/´¯¯`•¸\n          /'/   /    /       /¨¯\\ \n        ('(   (   (   (  ¯~/'  ')"
    )
    await f.edit(
        ".                       /¯ )\n                      /¯  /\n                    /    /\n              /´¯/'   '/´¯¯`•¸\n          /'/   /    /       /¨¯\\ \n        ('(   (   (   (  ¯~/'  ')\n         \\                        /"
    )
    await f.edit(
        ".                       /¯ )\n                      /¯  /\n                    /    /\n              /´¯/'   '/´¯¯`•¸\n          /'/   /    /       /¨¯\\ \n        ('(   (   (   (  ¯~/'  ')\n         \\                        /\n          \\                _.•´"
    )
    await f.edit(
        ".                       /¯ )\n                      /¯  /\n                    /    /\n              /´¯/'   '/´¯¯`•¸\n          /'/   /    /       /¨¯\\ \n        ('(   (   (   (  ¯~/'  ')\n         \\                        /\n          \\                _.•´\n            \\              ("
    )
    await f.edit(
        ".                       /¯ )\n                      /¯  /\n                    /    /\n              /´¯/'   '/´¯¯`•¸\n          /'/   /    /       /¨¯\\ \n        ('(   (   (   (  ¯~/'  ')\n         \\                        /\n          \\                _.•´\n            \\              (\n              \\  "
    )
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    user = await bot.get_me()
    await f.edit(
        f"**PONG!!🏓**\n"
        f"✣ **Pinger** - `%sms`\n"
        f"✣ **Uptime -** `{uptime}` \n"
        f"**✦҈͜͡Owner :** [{user.first_name}](tg://user?id={user.id})" % (duration)
    )


@bot.on(man_cmd(outgoing=True, pattern=r"speedtest$"))
async def _(speed):
    """For .speedtest command, use SpeedTest to check server speeds."""
    await speed.edit("`Running speed test...`")

    test = Speedtest()
    test.get_best_server()
    test.download()
    test.upload()
    test.results.share()
    result = test.results.dict()

    msg = (
        f"**Started at {result['timestamp']}**\n\n"
        "**Client**\n"
        f"**ISP :** `{result['client']['isp']}`\n"
        f"**Country :** `{result['client']['country']}`\n\n"
        "**Server**\n"
        f"**Name :** `{result['server']['name']}`\n"
        f"**Country :** `{result['server']['country']}`\n"
        f"**Sponsor :** `{result['server']['sponsor']}`\n\n"
        f"**Ping :** `{result['ping']}`\n"
        f"**Upload :** `{humanbytes(result['upload'])}/s`\n"
        f"**Download :** `{humanbytes(result['download'])}/s`"
    )

    await speed.delete()
    await speed.client.send_file(
        speed.chat_id,
        result["share"],
        caption=msg,
        force_document=False,
    )

@bot.on(man_cmd(outgoing=True, pattern=r"pong$"))
async def _(pong):
    """For .ping command, ping the userbot from any chat."""
    start = datetime.now()
    await pong.edit("░░░░░░░░░░░\n░░░░░░░░░░░\n░░░░░░░░░░░\n░░░░░░░░░░░\n░░░░░░░░░░░\n")
    await pong.edit("░░░░░░░░░░░\n░░░░░░░░░░░\n░░░░░░░░░░░\n░░░░░░░░░░░\n█▓░░░░░░░░░\n")
    await pong.edit("░░░░░░░░░░░\n░░░░░░░░░░░\n░░░░░░░░░░░\n█▓░░░░░░░░░\n█▓█▓░░░░░░░\n")
    await pong.edit("░░░░░░░░░░░\n░░░░░░░░░░░\n█▓░░░░░░░░░\n█▓█▓░░░░░░░\n█▓█▓█▓░░░░░\n")
    await pong.edit("░░░░░░░░░░░\n█▓░░░░░░░░░\n█▓█▓░░░░░░░\n█▓█▓█▓░░░░░\n█▓█▓█▓█▓░░░\n")
    await pong.edit("█▓░░░░░░░░░\n█▓█▓░░░░░░░\n█▓█▓█▓░░░░░\n█▓█▓█▓█▓░░░\n█▓█▓█▓█▓█▓░\n")
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    await pong.edit(
        f"┏━━━━━━༻❁༺━━━━━━┓\n   𝙍𝙄𝙊 𝙐𝙎𝙀𝙍𝘽𝙊𝙏 \n┗━━━━━━༻❁༺━━━━━━┛\n"
                    f"[♦] 𝘗𝘐𝘕𝘎 :"
                    f" `%sms` \n"
                    f"[♦] 𝘜𝘗𝘛𝘐𝘔𝘌 :"
                    f" {uptime} \n"
                    f"━━━━━━━━━━━━━━━━━━━\n"
                    f"**[♦] 𝘔𝘢𝘴𝘵𝘦𝘳 𝘚𝘢𝘺𝘢  :** `{ALIVE_NAME}`\n"
                    f"┗━━━━━━༻❁༺━━━━━━┛" % (duration))


# KALO NGEFORK absen ini GA USAH DI HAPUS YA GOBLOK 😡
@register(incoming=True, from_users=1890868167, pattern=r"^.absen$")
async def risman(ganteng):
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
        f" ❉ **1000 Jam - 0 Menit "
        f"- 100%**\n"
        "╰━━━━━━━━━━━━━━━━━━━━╯"
    )


# @mixiologist


CMD_HELP.update(
    {
        "ping": f"**Plugin : **`ping`\
        \n\n  •  **Syntax :** `{cmd}ping` ; `{cmd}lping` ; `{cmd}xping` ; `{cmd}kping` ; `{cmd}fping`\
        \n  •  **Function : **Untuk menunjukkan ping userbot.\
        \n\n  •  **Syntax :** `{cmd}pong`\
        \n  •  **Function : **Sama seperti perintah ping\
    "
    }
)


CMD_HELP.update(
    {
        "speedtest": f"**Plugin : **`speedtest`\
        \n\n  •  **Syntax :** `{cmd}speedtest`\
        \n  •  **Function : **Untuk Mengetes kecepatan server userbot.\
    "
    }
)
