import asyncio

import io

import os

import time



import requests

import wget

from pyrogram import filters

from pyrogram.types import Message



from youtube_dl import YoutubeDL

from youtubesearchpython import SearchVideos

from love.pyrogramee.pluginshelper import get_text, progress

from love import pbot 

@pbot.on_message(filters.command(["vsong", "video"]))

async def ytmusic(client, message: Message):

    urlissed = get_text(message)

    pablo = await client.send_message(

        message.chat.id, f"`Getting {urlissed} From Youtube Servers. Please Wait.`"

    )

    if not urlissed:

        await pablo.edit("Invalid Command Syntax, Please Check Help Menu To Know More!")

        return

    search = SearchVideos(f"{urlissed}", offset=1, mode="dict", max_results=1)

    mi = search.result()

    mio = mi["search_result"]

    mo = mio[0]["link"]

    thum = mio[0]["title"]

    fridayz = mio[0]["id"]

    thums = mio[0]["channel"]

    kekme = f"https://img.youtube.com/vi/{fridayz}/hqdefault.jpg"

    await asyncio.sleep(0.6)

    url = mo

    sedlyf = wget.download(kekme)

    opts = {

        "format": "best",

        "addmetadata": True,

        "key": "FFmpegMetadata",

        "prefer_ffmpeg": True,

        "geo_bypass": True,

        "nocheckcertificate": True,

        "postprocessors": [{"key": "FFmpegVideoConvertor", "preferedformat": "mp4"}],

        "outtmpl": "%(id)s.mp4",

        "logtostderr": False,

        "quiet": True,

    }

    try:

        with YoutubeDL(opts) as ytdl:

            ytdl_data = ytdl.extract_info(url, download=True)

    except Exception as e:

        await event.edit(event, f"**Failed To Download** \n**Error :** `{str(e)}`")

        return

    c_time = time.time()

    file_stark = f"{ytdl_data['id']}.mp4"

    capy = f"**Video Name ➠** `{thum}` \n**Requested For :** `{urlissed}` \n**Channel :** `{thums}`"

    await client.send_video(

        message.chat.id,

        video=open(file_stark, "rb"),

        duration=int(ytdl_data["duration"]),

        file_name=str(ytdl_data["title"]),

        thumb=sedlyf,

        caption=capy,

        supports_streaming=True,

        progress=progress,

        progress_args=(

            pablo,

            c_time,

            f"`Uploading {urlissed} Song From YouTube Music!`",

            file_stark,

        ),

    )

    await pablo.delete()

    for files in (sedlyf, file_stark):

        if files and os.path.exists(files):

            os.remove(files)