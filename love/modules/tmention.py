
from pyrogram import filters

from love.pyrogramee.pluginshelper import admins_only, get_text
from love import pbot


@pbot.on_message(filters.command("tagall") & ~filters.edited & ~filters.bot)
@admins_only
async def tagall(client, message):
    await message.reply("**Calling to all members** 👀")
    sh = get_text(message)
    if not sh:
        sh = "HEY GUYS..."
    mentions = ""
    async for member in client.iter_chat_members(message.chat.id):
        mentions += member.user.mention + " "
    n = 4096
    kk = [mentions[i : i + n] for i in range(0, len(mentions), n)]
    for i in kk:
        j = f"<b>{sh}</b> \n{i}"
        await client.send_message(message.chat.id, j, parse_mode="html")


__mod_name__ = "Mᴇɴᴛɪᴏɴ@"
__help__ = """
- /tagall : Tag everyone in a chat group
"""
