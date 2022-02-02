#!/usr/bin/env python
import sqlite3
import time

HLR_DATABASE = "/usr/src/CalypsoBTS/hlr.sqlite3"
db = sqlite3.connect(HLR_DATABASE)
c = db.cursor()
c.execute("SELECT * FROM Subscriber")

print "ID\t\tIMSI\t\tMSISDN\n"

while 1:
    subscriber = c.fetchone()
    if not subscriber:
        break

    print "{0:1}\t{2:<15}\t\t{4}".format(
            subscriber[0],
            subscriber[1],
            subscriber[3],
            subscriber[7],
            subscriber[5]
            )
db.close()
