
from datetime import date, datetime
import sys


target_day_str = sys.argv[1]

date_format = "%Y.%m.%d"
target_day = datetime.strptime(target_day_str, date_format)
current_day = datetime.now()

delta = target_day - current_day
print(delta.days, "days")
