from base.models import Ticket, Court
from datetime import datetime, timedelta
import random

courts = []
with open('courts.csv','r') as court_file:
    for line in court_file:
        c = Court()
        c.name = line.split(',')[0]
        if c.name == "":
            continue
        if not c.name.endswith('Court'):
            c.name = c.name + ' Court'
        c.key = 'pass'
        c.save()
        courts.append(c)

with open('citations.csv', 'r') as name_file:
    for line in name_file:
        t = Ticket()
        s = line.split(',')
        t.name = s[3] + ' ' + s[4]
        if t.name == ' ':
            continue;
        m = random.randrange(1,12)
        d = random.randrange(1,28)
        if m != 2:
            d += random.randrange(3)
        t.request_stamp = datetime(2015, m, d, hour=random.randrange(24), minute=random.randrange(60), second=random.randrange(60))
        t.served_stamp = request_stamp + timedelta(minutes=random.randrange(1,75))
        t.message = s[6] + ' ' + s[7] + ' ' + s[8]
        t.email = 'lynfhan@gmail.com'
        t.court = random.choice(courts)
        t.save()
