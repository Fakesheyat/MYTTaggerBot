import os, logging, asyncio
from telethon import Button
from telethon import TelegramClient, events
from telethon.sessions import StringSession
from telethon.tl.types import ChannelParticipantsAdmins

logging.basicConfig(
    level=logging.INFO,
    format='%(name)s - [%(levelname)s] - %(message)s'
)
LOGGER = logging.getLogger(__name__)

api_id = int(os.environ.get("APP_ID"))
api_hash = os.environ.get("API_HASH")
bot_token = os.environ.get("TOKEN")
client = TelegramClient('client', api_id, api_hash).start(bot_token=bot_token)

emoji_calisan = []

anlik_calisan = []

tekli_calisan = []

@client.on(events.NewMessage(pattern='^(?i)/dayan'))
async def cancel(event):
  global emoji_calisan
  emoji_calisan.remove(event.chat_id)



@client.on(events.NewMessage(pattern="^/start$"))
async def start(event):
  await event.reply("●** 𝚜𝚊𝚕𝚊𝚖 ❤️**\n\n● **𝚖𝚎𝚗 𝚐𝚛𝚞𝚙𝚍𝚊𝚔𝚒 𝚑𝚎𝚛𝚔𝚎𝚜ｪ 𝚝𝚊𝚐 𝚎𝚍𝚎 𝚋ｪ𝚕𝚎𝚗 𝚋𝚘𝚝𝚊𝚖 𝚐𝚛𝚞𝚙𝚊 𝚊𝚝ｪ𝚋 𝚢𝚎𝚝𝚔𝚒 𝚟𝚎𝚛𝚖𝚎𝚢ｪ𝚗ｪ𝚣 𝚔ｪ𝚏𝚊𝚢𝚎𝚝𝚍ｪ elave melumat üçün /help yazın**",
              buttons=(
                      
                    
                                       
	
                      
                  
			   
		      [Button.url(' 𝗕𝗲𝗻𝗶 𝗚𝗿𝘂𝗯𝗮 𝗘𝗸𝗹𝗲  ', 'https://t.me/MytTagBot?startgroup=a')],
                      [Button.url(' 𝗗𝗲𝘀𝘁𝗲𝗸 𝗚𝗿𝘂𝗯𝘂  ',  'https://t.me/lordchattt')], 
                      [Button.url('  𝗗𝗲𝘃𝗲𝗹𝗼𝗽𝗲𝗿  ', 'https://t.me/nevarisoyumiste')],
                    ),
                    link_preview=False
                   )
@client.on(events.NewMessage(pattern="^/help$"))
async def help(event):
  helptext = "📝 **ᴇᴛɪᴋᴇᴛ ᴛᴀɢɢᴇʀ ᴋᴏᴍᴜᴛʟᴀʀɪ **\n\n**» /ctag < ᴍᴇsᴀᴊɪɴɪᴢ > \nɢʀᴜʙᴛᴀᴋɪ ᴋᴜʟʟᴀɴɪᴄɪʟᴀʀᴀ 5-ʟɪ ᴇᴛɪᴋᴇᴛ ᴀᴛᴀʀ .  .  !**\n\n**» /tag  < ᴍᴇsᴀᴊɪɴɪᴢ > \nɢʀᴜʙᴛᴀᴋɪ ᴋᴜʟʟᴀɴɪᴄɪʟᴀʀᴀ ᴛᴇᴋ ᴛᴇᴋ ᴇᴛɪᴋᴇᴛ ᴀᴛᴀʀ . . !**\n\n**» /dayan => ᴇᴛɪᴋᴇᴛʟᴇᴍᴇ ɪsʟᴇᴍɪɴɪ ᴅᴜʀᴅᴜʀᴜʀ . . !**"
  await event.reply(helptext,
                    buttons=(
                      [Button.url('  𝗕𝗲𝗻𝗶 𝗚𝗿𝘂𝗯𝗮 𝗘𝗸𝗹𝗲  ', 'https://t.me/MytTagBot?startgroup=a')],
                      [Button.url('  𝗗𝗲𝘀𝘁𝗲𝗸 𝗚𝗿𝘂𝗯𝘂  ',  'https://t.me/lordchattt')],
                      [Button.url(' 𝗗𝗲𝘃𝗲𝗹𝗼𝗽𝗲𝗿  ', 'https://t.me/nevarisoyumiste')],
                    ),
                    link_preview=False
                   )
	
@client.on(events.NewMessage(pattern="^/reklam$"))
async def help(event):
  helptext = "**📝 ᴇᴛɪᴋᴇᴛ ᴛᴀɢɢᴇʀ ᴋᴏᴍᴜᴛʟᴀʀɪ\n\n» /ctag < ᴍᴇsᴀᴊɪɴɪᴢ > => 𝚐𝚛𝚞𝚙𝚍𝚊𝚔𝚒 𝚞𝚜𝚎𝚛𝚕𝚎𝚛ｪ 5-𝚕ｪ 𝚝𝚊𝚐 𝚎𝚍𝚎𝚛 .  .  !\n» /tag  < ᴍᴇsᴀᴊɪɴɪᴢ > => 𝚐𝚛𝚞𝚙𝚍𝚊𝚔𝚒 𝚞𝚜𝚎𝚛𝚕𝚎𝚛ｪ 𝚝𝚎𝚔 𝚝𝚎𝚔 𝚝𝚊𝚐 𝚎𝚍𝚎𝚛 . . !\n» /dayan => 𝚝𝚊𝚐ｪ 𝚍𝚊𝚢𝚊𝚗𝚍ｪ𝚛𝚊𝚛. . !\n\n✵ ʙɪʀ ᴄᴏᴋ ᴏᴢᴇʟʟɪɢᴇ sᴀʜɪᴘ @CTaggerBot 'ᴜ ɢʀᴜʙᴜɴᴜᴢᴀ ʀᴀʜᴀᴛʟɪᴋʟᴀ ᴇᴋʟᴇʏɪᴘ ᴋᴜʟʟᴀɴᴀʙɪʟɪʀsɪɴɪᴢ . . ! **"
  await event.reply(helptext,
                    buttons=(
                      [Button.url('🎉  𝗕𝗼𝘁𝘂 𝗚𝗿𝘂𝗯𝗮 𝗘𝗸𝗹𝗲  🎉', 'https://t.me/MytTagBot?startgroup=a')],
                    ),
                    link_preview=False
                   )
	
	

@client.on(events.NewMessage(pattern='^(?i)/dayan'))
async def cancel(event):
  global emoji_calisan
  emoji_calisan.remove(event.chat_id)


emoji = " ❤️ 🧡 💛 💚 💙 💜 🖤 🤍 🤎 🙂 🙃 😉 😌 😍 🥰 😘 😗 😙 😚 😋 😛 😝 😜 🤪 🤨 🧐 🤓 😎 🤩 🥳 😏 😒 " \
        "😞 😔 😟 😕 🙁 😣 😖 😫 🧜‍♀️ 🥵 🐸 🐊 🤟 😩 🥺 😢 😭 😤 😠 😡  🤯 😳 🥵 🥶 😱 😨 😰 😥 😓 🤗 🤔 🤭 🤫 🤥 😶 😐 😑 😬 🙄 " \
        "😻 😼 😽 🙀 😿 😾 🔞 🌹 ".split (" ")


@client.on(events.NewMessage(pattern="^/emojitag ?(.*)"))
async def mentionall(event):
  global emoji_calisan
  if event.is_private:
    return await event.respond("**Bu komutu gruplar ve kanallar için geçerli**")
  
  admins = []
  async for admin in client.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.respond("**Bu komutu sadace yoneticiler kullana bilir😐**")
  
  if event.pattern_match.group(1):
    mode = "text_on_cmd"
    msg = event.pattern_match.group(1)
  elif event.reply_to_msg_id:
    mode = "text_on_reply"
    msg = event.reply_to_msg_id
    if msg == None:
        return await event.respond("**Geçmiş mesajlar için etiket ede bilmiom**")
  elif event.pattern_match.group(1) and event.reply_to_msg_id:
    return await event.respond("**𝖤𝗍𝗂𝗄𝖾𝗍 𝗒𝖺𝗉𝗆𝖺𝗄 𝗂𝖼𝗂𝗇 𝗌𝖾𝖻𝖾𝗉 𝗒𝗈𝗄**")
  else:
    return await event.respond("**𝖤𝗍𝗂𝗄𝖾𝗍𝖾 𝖻𝖺𝗌𝗅𝖺𝗆𝖺𝗄 𝗂𝖼𝗂𝗇 sebep 𝗒𝖺𝗓𝗂𝗇...!**")
  
  if mode == "text_on_cmd":
    emoji_calisan.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"[{random.choice(emoji)}](tg://user?id={usr.id}) "
      if event.chat_id not in emoji_calisan:
        await event.respond("** 𝖤𝗍𝗂𝗄𝖾𝗍𝗅𝖾𝗆𝖾 𝗂𝗌𝗅𝖾𝗆𝗂 𝖻𝖺𝗌𝖺𝗋𝗂𝗒𝗅𝖺 𝖽𝗎𝗋𝖽𝗎𝗋𝗎𝗅𝖽𝗎 **")
        return
      if usrnum == 5:
        await client.send_message(event.chat_id, f"{usrtxt}\n\n{msg}")
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""
        
  
  if mode == "text_on_reply":
    emoji_calisan.append(event.chat_id)
 
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"[{random.choice(emoji)}](tg://user?id={usr.id}) "
      if event.chat_id not in emoji_calisan:
        await event.respond("**𝖤𝗍𝗂𝗄𝖾𝗍𝗅𝖾𝗆𝖾 𝗂𝗌𝗅𝖾𝗆𝗂 𝖻𝖺𝗌𝖺𝗋𝗂𝗒𝗅𝖺 𝖽𝗎𝗋𝖽𝗎𝗋𝗎𝗅𝖽𝗎 ...**")
        return
      if usrnum == 5:
        await client.send_message(event.chat_id, usrtxt, reply_to=msg)
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""


@client.on(events.NewMessage(pattern='^(?i)/dayan'))
async def cancel(event):
  global emoji_calisan
  emoji_calisan.remove(event.chat_id)


@client.on(events.NewMessage(pattern="^/ctag ?(.*)"))
async def mentionall(event):
  global anlik_calisan
  if event.is_private:
    return await event.respond("**● ʙᴜ ᴋᴏᴍᴜᴛᴜ ʏᴀʟɴɪᴢᴄᴀ ɢʀᴜʙᴛᴀ ᴋᴜʟʟᴀɴᴀʙɪʟɪʀsɪɴɪᴢ . . !**")
  
  admins = []
  async for admin in client.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.respond("**● ʙᴜ ᴋᴏᴍᴜᴛᴜ ʏᴀʟɴɪᴢᴄᴀ ʏᴏɴᴇᴛɪᴄɪʟᴇʀ ᴋᴜʟʟᴀɴᴀʙɪʟɪʀ . . !**")
  
  if event.pattern_match.group(1):
    mode = "text_on_cmd"
    msg = event.pattern_match.group(1)
  elif event.reply_to_msg_id:
    mode = "text_on_reply"
    msg = event.reply_to_msg_id
    if msg == None:
        return await event.respond("Önceki Mesajlara Cevab Vermeyin")
  elif event.pattern_match.group(1) and event.reply_to_msg_id:
    return await event.respond("**𝖤𝗍𝗂𝗄𝖾𝗍 𝗂𝗌𝗅𝖾𝗆𝗂𝗇𝗂 𝖻𝖺𝗌𝗅𝖺𝗍𝗆𝖺𝗄 𝗂𝖼𝗂𝗇 𝗌𝖾𝖻𝖾𝗉 𝗒𝗈𝗄**")
  else:
    return await event.respond("**● ᴇᴛɪᴋᴇᴛ ɪsʟᴇᴍɪɴɪ ʙᴀsʟᴀᴛᴍᴀᴋ ɪᴄɪɴ \n< sᴇʙᴇᴘ > ɢɪʀɪɴ ʏᴀᴅᴀ ʙɪʀ ᴍᴇsᴀᴊɪ ʏᴀɴɪᴛʟᴀʏɪɴ . . !**")
  
  if mode == "text_on_cmd":
    anlik_calisan.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"**[{usr.first_name}](tg://user?id={usr.id})** , "
      if event.chat_id not in anlik_calisan:
        await event.respond("**● ᴇᴛɪᴋᴇᴛʟᴇᴍᴇ ɪsʟᴇᴍɪ ʙᴀsᴀʀɪʏʟᴀ ᴅᴜʀᴅᴜʀᴜʟᴅᴜ . . !**")
        return
      if usrnum == 5:
        await client.send_message(event.chat_id, f"{msg}\n{usrtxt}")
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""
        
  
  if mode == "text_on_reply":
    anlik_calisan.append(event.chat_id)
 
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"**[{usr.first_name}](tg://user?id={usr.id})** , "
      if event.chat_id not in anlik_calisan:
        await event.respond("**● ᴇᴛɪᴋᴇᴛʟᴇᴍᴇ ɪsʟᴇᴍɪ ʙᴀsᴀʀɪʏʟᴀ ᴅᴜʀᴅᴜʀᴜʟᴅᴜ . . !**")
        return
      if usrnum == 5:
        await client.send_message(event.chat_id, usrtxt, reply_to=msg)
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""

@client.on(events.NewMessage(pattern='^(?i)/dayan'))
async def cancel(event):
  global anlik_calisan
  anlik_calisan.remove(event.chat_id)
	

@client.on(events.NewMessage(pattern="^/tag ?(.*)"))
async def mentionall(event):
  global tekli_calisan
  if event.is_private:
    return await event.respond("**● ʙᴜ ᴋᴏᴍᴜᴛᴜ ʏᴀʟɴɪᴢᴄᴀ ɢʀᴜʙᴛᴀ ᴋᴜʟʟᴀɴᴀʙɪʟɪʀsɪɴɪᴢ . . !**")
  
  admins = []
  async for admin in client.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.respond("**● ʙᴜ ᴋᴏᴍᴜᴛᴜ ʏᴀʟɴɪᴢᴄᴀ ʏᴏɴᴇᴛɪᴄɪʟᴇʀ ᴋᴜʟʟᴀɴᴀʙɪʟɪʀ . . !**")
  
  if event.pattern_match.group(1):
    mode = "text_on_cmd"
    msg = event.pattern_match.group(1)
  elif event.reply_to_msg_id:
    mode = "text_on_reply"
    msg = event.reply_to_msg_id
    if msg == None:
        return await event.respond("**önceki mesajı etiketleye bilmerim*")
  elif event.pattern_match.group(1) and event.reply_to_msg_id:
    return await event.respond("**● ᴇᴛɪᴋᴇᴛ ɪsʟᴇᴍɪɴɪ ʙᴀsʟᴀᴛᴍᴀᴋ ɪᴄɪɴ \n< sᴇʙᴇᴘ > ɢɪʀɪɴ ʏᴀᴅᴀ ʙɪʀ ᴍᴇsᴀᴊɪ ʏᴀɴɪᴛʟᴀʏɪɴ . . !**")
  else:
    return await event.respond("**● ᴇᴛɪᴋᴇᴛ ɪsʟᴇᴍɪɴɪ ʙᴀsʟᴀᴛᴍᴀᴋ ɪᴄɪɴ \n< sᴇʙᴇᴘ > ɢɪʀɪɴ ʏᴀᴅᴀ ʙɪʀ ᴍᴇsᴀᴊɪ ʏᴀɴɪᴛʟᴀʏɪɴ . . !**")
  
  if mode == "text_on_cmd":
    tekli_calisan.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"• [{usr.first_name}](tg://user?id={usr.id})"
      if event.chat_id not in tekli_calisan:
        await event.respond("**● ᴇᴛɪᴋᴇᴛʟᴇᴍᴇ ɪsʟᴇᴍɪ ʙᴀsᴀʀɪʏʟᴀ ᴅᴜʀᴅᴜʀᴜʟᴅᴜ . . !**")
        return
      if usrnum == 1:
        await client.send_message(event.chat_id, f"{usrtxt} \n{msg}")
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""
        
  
  if mode == "text_on_reply":
    tekli_calisan.append(event.chat_id)
 
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"• [{usr.first_name}](tg://user?id={usr.id}) \n"
      if event.chat_id not in tekli_calisan:
        await event.respond("**● ᴇᴛɪᴋᴇᴛʟᴇᴍᴇ ɪsʟᴇᴍɪ ʙᴀsᴀʀɪʏʟᴀ ᴅᴜʀᴅᴜʀᴜʟᴅᴜ . . !**")
        return
      if usrnum == 1:
        await client.send_message(event.chat_id, usrtxt, reply_to=msg)
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""

@client.on(events.NewMessage(pattern='^(?i)/dayan'))
async def cancel(event):
  global tekli_calisan
  tekli_calisan.remove(event.chat_id)
	


@client.on(events.NewMessage(pattern="^/admin ?(.*)"))
async def mentionall(tagadmin):

	if admintag.pattern_match.group(1):
		seasons = tagadmin.pattern_match.group(1)
	else:
		seasons = ""

	chat = await tagadmin.get_input_chat()
	a_=0
	await tagadmin.delete()
	async for i in client.iter_participants(chat, filter=cp):
		if a_ == 500:
			break
		a_+=5
		await tagadmin.client.send_message(tagadmin.chat_id, "**[{}](tg://user?id={}) {}**".format(i.first_name, i.id, seasons))
		sleep(0.5)


print(">> 𝖡𝗈𝗍 𝖼𝖺𝗅𝗂𝗌𝗂𝗒𝗈𝗋 𝗌𝖺𝗄𝗂𝗇 𝗈𝗅 𝖽𝗈𝗌𝗍𝗎𝗆 😃 @lordchattt bilgi alabilirsin <<")
client.run_until_disconnected()
