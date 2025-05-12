# 🚫 Before:
from datetime import datetime
import pytz
dt = datetime.now().replace(tzinfo=pytz.timezone('Asia/Yekaterinburg'))
print(dt)  # 2025-05-07 12:11:18.312381+04:03


# ✅ After
from datetime import datetime
import pytz
tz = pytz.timezone('Asia/Yekaterinburg')
now = datetime.now(tz)
print(now) # 025-05-07 12:11:18.312381+05:00

# 🧠 ➤ Uses proper timezone-aware now(tz) to avoid incorrect offsets.
