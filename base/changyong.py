from datetime import datetime, timedelta, timezone
import hashlib
import json
from urllib import request

tz_utc_8 = timezone(timedelta(hours=2))
now = datetime.now()
dt = now.replace(tzinfo=tz_utc_8)
print(dt)

utc_dt = datetime.utcnow().replace(tzinfo=timezone.utc)
print(utc_dt)
bj_dt = utc_dt.astimezone(timezone(timedelta(hours=8)))
print(bj_dt)

datetimestmp = datetime.timestamp(datetime.now())
print(datetimestmp)
# md5 = hashlib.md5()

with request.urlopen('https://api.douban.com/v2/book/2129650') as f:
    data = f.read()
    print(json.loads(data))
    # print('Status:', f.status, f.reason)
    # for k, v in f.getheaders():
    #     print('%s: %s' % (k, v))
    # print(f.get)
    # print('Data:', data.decode('utf-8'))

