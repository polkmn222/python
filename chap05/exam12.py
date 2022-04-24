import glob
print(glob.glob("C:/Users/user/Desktop/python/chap*"))

import tempfile
filename = tempfile.mkstemp()
print(filename)

import tempfile
f = tempfile.TemporaryFile()
f.close()

import time
print(time.time())

print(time.localtime(time.time()))

print(time.asctime(time.localtime(time.time())))

print(time.ctime())


import time
print(time.strftime('%x', time.localtime(time.time())))
print(time.strftime('%c', time.localtime(time.time())))


import time
for i in range(10):
    print(i)
    time.sleep(1)

import calendar
print(calendar.calendar(2022))

calendar.prcal(2022)

calendar.prmonth(2022, 4)

print(calendar.weekday(2022, 12, 31))

print(calendar.monthrange(2022, 12))

import random
print(random.random())

print(random.randint(1, 10))

print(random.randint(1, 55))

import random
def random_pop(data):
    number = random.randint(0, len(data)-1)
    return data.pop(number)

if __name__ == "__main__":
    data = [1, 2, 3, 4, 5]
    while data: print(random_pop(data))

def random_pop(data):
    number = random.choice(data)
    data.remove(number)
    return number

import random
data = [1, 2, 3, 4, 5]
random.shuffle(data)
print(data)


import webbrowser
webbrowser.open("http://google.com")

webbrowser.open_new("http://google.com")

import time

def long_task():
    for i in range(5):
        time.sleep(1)
        print("working:%s\n" % i)

print("Start")

for i in range(5):
    long_task()

print("End")    


import time
import threading

def long_task():
    for i in range(5):
        time.sleep(1)
        print("working:%s\n" % i)

print("Start")

threads = []
for i in range(5):
    t = threading.Thread(target=long_task)
    threads.append(t)

for t in threads:
    t.start()

print("End")    


import time
import threading

def long_task():
    for i in range(5):
        time.sleep(1)
        print("working:%s\n" % i)

print("Start")

threads = []
for i in range(5):
    t = threading.Thread(target=long_task)
    threads.append(t)

for t in threads:
    t.start()

for t in threads:
    t.join()

print("End")    
