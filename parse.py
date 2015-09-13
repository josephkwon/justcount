from base.models import Ticket, Court
from datetime import datetime, timedelta, timezone
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
        m = random.randrange(1,10)
        if m != 9:
            m = random.randrange(1,10) #increase probability of current month
        d = 0
        if m != 2 and m != 9:
            d = random.randrange(1,31)
        elif m == 2:
            d = random.randrange(1,29)
        elif m == 9:
            d = random.randrange(1,13)
        t.request_stamp = datetime(2015, m, d, hour=random.randrange(24), minute=random.randrange(60), second=random.randrange(60), tzinfo=timezone.utc)
        t.served_stamp = t.request_stamp + timedelta(minutes=random.randrange(1,75))
        t.message = s[6] + ' ' + s[7] + ' ' + s[8]
        t.email = 'lynfhan@gmail.com'
        t.court = random.choice(courts)
        t.save()


"""
BEGIN;
DROP TABLE base_court;
DROP TABLE base_ticket;

CREATE TABLE "base_court" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "name" varchar(500) NOT NULL);

CREATE TABLE "base_ticket" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "name" varchar(50) NOT NULL, "request_stamp" datetime NOT NULL, "served_stamp" datetime NOT NULL, "message" text NOT NULL, "court_id" integer NOT NULL REFERENCES "base_court" ("id"));
CREATE INDEX "base_ticket_7a46e69c" ON "base_ticket" ("court_id");

COMMIT;
"""
