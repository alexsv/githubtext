from copy import copy
from datetime import datetime, timedelta
from random import randint
import os



MESSAGE = [ 
"                ",
"                ",
"** xxx** xx *x x",
"* *x  * *x x*x x",
"** xx ** xx * x ",
"* *x  * *x x*x x",   
"* *xxx** xx *x x",
]



FILENAME = 'counter'

START_MONTH = '2012-04'

COMMITS_MAPPING = {
  '*': 16,
  'x': 7,
}

start_date = datetime.strptime(START_MONTH, '%Y-%m')
if start_date.weekday() != 6: #if not a sunday to start with
    start_date = start_date + timedelta(days=6-start_date.weekday())

xlen = len(MESSAGE[0])

res = [[' '] * 60 for i in range(8)]



for x in xrange(xlen):
    for y in xrange(7):
        start_date = start_date.replace(hour=13, minute=0)

        char = MESSAGE[y][x]
        commits = COMMITS_MAPPING.get(char, 0)

        for i in xrange(commits):
            start_date = start_date + timedelta(minutes=5)
            cnt = open(FILENAME).read()
            cnt = str(int(cnt) + 1)
            f = open(FILENAME, 'w')
            f.write(cnt)
            f.close()

            cmd = 'git add {filename} && git commit -a -m "fix #{num}-{rand}" --date="{date}"'.\
                    format(filename=FILENAME, num= y * 7 + x, rand=randint(0,1000), date=start_date.isoformat())
            os.system(cmd)

            _y, _w, _d = start_date.isocalendar()
            res[_d][_w] = '*'
        
        start_date = start_date + timedelta(days=1)

print "\n".join(map(lambda x: ''.join(x), res))
