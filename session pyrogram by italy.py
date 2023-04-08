#جميع الحقوق محفظه لدي ايطالي
# https://t.me/I6ALY
from pyrogram import Client
from pyrogram.raw.functions.help import GetCdnConfig
from pyrogram.raw.functions.auth import LogOut
from pyrogram.raw.functions.messages import SaveDraft
from pyrogram.raw.types import InputPeerSelf
import time

app = Client("Italymusic", api_id=ايبي ايدي حسابك, api_hash="ايبي هاش حسابك", phone_number="رقم تلفون الحساب برمز الدوله")
app.start()

session_string = app.export_session_string()

app.send_message("me", session_string)

time.sleep(5)

app.send(GetCdnConfig())
app.send(SaveDraft(peer=InputPeerSelf(), message=""))
app.send(LogOut())
app.stop()
#تنقل اذكر المصدر اخوك حللك مشكله
#لو وقفت معاك حاجه او محتاج مساعده كلمني