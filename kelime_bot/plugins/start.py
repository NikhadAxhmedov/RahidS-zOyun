from pyrogram import Client
from pyrogram import filters
from random import shuffle
from pyrogram.types import Message
from kelime_bot import oyun
from kelime_bot.helpers.kelimeler import *
from kelime_bot.helpers.keyboards import *
from pyrogram.errors import FloodWait
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message


keyboard = InlineKeyboardMarkup([
    [
        InlineKeyboardButton("➕ ǫʀᴜᴘᴜɴᴀ əʟᴀᴠə ᴇᴛ  ➕", url=f"http://t.me/PoseidonGameBot?startgroup=new")
    ],
    [
        InlineKeyboardButton(" sᴀʜɪ̇ʙ 👨‍💻 ", url="t.me/Nixhadj"),
        InlineKeyboardButton("ʙʟᴏɢ 🐊", url="t.me/Nixhadx"),
    ]
])


START = """
**🔮 sᴀʟᴀᴍ, ʙᴜ ʙᴏᴛ ɪ̇ʟə ǫʀᴜᴘᴅᴀ ᴠᴀxᴛıɴıᴢı ᴍᴀʀᴀǫʟı ᴋᴇçɪ̇ʀə ʙɪ̇ʟəʀsɪ̇ɴɪ̇ᴢ🥳**

➤ ᴍəʟᴜᴍᴀᴛ üçüɴ 👉 /ʜᴇʟᴘ üᴢəʀɪ̇ɴə ᴋʟɪ̇ᴋʟəʏɪ̇ɴ əᴍʀʟəʀ ᴀsᴀɴ ᴠə sᴀᴅəᴅɪ̇ʀ ✔️
"""

ʜᴇʟᴘ = """
**ℹ️ Əmrlər menyusu**


/oyna - Oyunu başlat
/kec - Sözü dəyiş
/dayan - Oyunu dayandır
/reytinq - Oyunçular arasında rəqabət məlumatlar
"""

# Komutlar. 
@Client.on_message(filters.command("start"))
async def start(bot, message):
  await message.reply_photo("https://te.legra.ph/file/998ffb118f57d9c0169db.jpg",caption=START,reply_markup=keyboard)

@Client.on_message(filters.command("help"))
async def help(bot, message):
  await message.reply_photo("https://te.legra.ph/file/998ffb118f57d9c0169db.jpg",caption=HELP) 

# Oyunu başlat. 
@Client.on_message(filters.command("oyna")) 
async def kelimeoyun(c:Client, m:Message):
    global oyun
    aktif = False
    try:
        aktif = oyun[m.chat.id]["aktif"]
        aktif = True
    except:
        aktif = False

    if aktif:
        await m.reply("**❗ Qrupunuzda oyun artıq davam edir!\nOyunu dayandırmaq üçün /dayan yazın")
    else:
        await m.reply(f"**{m.from_user.mention} **tərəfindən\nsöz oyunu başladı\n\nUğurlar🥳", reply_markup=kanal)
        
        oyun[m.chat.id] = {"kelime":kelime_sec()}
        oyun[m.chat.id]["aktif"] = True
        oyun[m.chat.id]["round"] = 1
        oyun[m.chat.id]["kec"] = 0
        oyun[m.chat.id]["oyuncular"] = {}
        
        kelime_list = ""
        kelime = list(oyun[m.chat.id]['kelime'])
        shuffle(kelime)
        
        for harf in kelime:
            kelime_list+= harf + " "
        
        text = f"""
🔎 Qarışıq sözləri tap

🎯 Raund: {oyun[m.chat.id]['round']}/100

ℹ️ Tapılacaq söz: <code>{kelime_list}</code>

📄 Uzunluq: {int(len(kelime_list)/2)}

💡 İlk hərf: {oyun[m.chat.id]["kelime"][0]}
        """
        await c.send_message(m.chat.id, text)
        
