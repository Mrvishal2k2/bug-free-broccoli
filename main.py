import os
import time
import datetime
import pytz
import pyrogram

user_session_string = os.environ.get("user_session_string")
bots = [i.strip() for i in os.environ.get("bots").split(' ')]
bot_owner = os.environ.get("bot_owner")
update_channel = os.environ.get("update_channel")
status_message_id = int(os.environ.get("status_message_id"))
api_id = int(os.environ.get("api_id"))
api_hash = os.environ.get("api_hash")

user_client = pyrogram.Client(
    user_session_string, api_id=api_id, api_hash=api_hash)


def main():
    with user_client:
        while True:
            print("[INFO] starting to check uptime..")
            edit_text = f"💗 𝐎𝐮𝐫 𝐀𝐥𝐥 𝐁𝐨𝐭𝐬 𝐋𝐢𝐬𝐭 & 𝐋𝐢𝐯𝐞 𝐒𝐭𝐚𝐭𝐮𝐬💖\n@BotDunia\n\n💡𝘉𝘰𝘵 𝘜𝘱𝘥𝘢𝘵𝘦𝘥 𝘌𝘷𝘦𝘳𝘺 15 𝘔𝘪𝘯𝘶𝘵𝘦𝘴\n\n"
            for bot in bots:
                print(f"[INFO] checking @{bot}")
                snt = user_client.send_message(bot, '/start')

                time.sleep(15)

                msg = user_client.get_history(bot, 1)[0]
                if snt.message_id == msg.message_id:
                    print(f"[WARNING] @{bot} is down")
                    edit_text += f"**➩ @{bot}**    `❌`\n"
                    t_now = datetime.datetime.now(pytz.timezone('Asia/Kolkata')).strftime("%d/%m/%y %I:%M:%S %p")
                    user_client.send_message(bot_owner,
                                             f"@{bot} status: `Down`\n{t_down}")
                else:
                    print(f"[INFO] all good with @{bot}")
                    edit_text += f"**➩ @{bot}**    `✅`\n"
                user_client.read_history(bot)

            utc_now = datetime.datetime.now(pytz.timezone('UTC')).strftime("%d/%m/%y %I:%M:%S %p")

            ist_now = datetime.datetime.now(pytz.timezone('Asia/Kolkata')).strftime("%d/%m/%y %I:%M:%S %p")

            edit_text += f"\n🎯 𝙇𝙖𝙨𝙩 𝙪𝙥𝙙𝙖𝙩𝙚𝙙 & 𝙘𝙝𝙚𝙘𝙠𝙚𝙙 𝙤𝙣: \n\n__{str(ist_now)}__ 🇮🇳 IST\n__{utc_now}__ 🌎 UTC"

            user_client.edit_message_text(update_channel, status_message_id,
                                         edit_text)
            print(f"[INFO] everything done! sleeping for 15 mins...")

            time.sleep(15 * 60)


main()
