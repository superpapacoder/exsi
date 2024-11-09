from datetime import datetime
import pytz

now = datetime.now(pytz.timezone('US/Eastern'))
print(now)
