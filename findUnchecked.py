import requests
from time import sleep
import random

def isUncheckedMath(link):
	t = requests.get(link)
	q = t.text
	sleep(random.randint(1,10)/100)
	if(q.find("trackErrorPage") != -1):
		return False
	if(q.find("icon-check") != -1):
		return False
	q = q[q.find("<span itemprop=\"name\">")+len("<span itemprop=\"name\">"):]
	q = q[q.find("<span itemprop=\"name\">")+len("<span itemprop=\"name\">"):]
	q = q[:q.find("<")]
	#print(q )
	if(q.find("Математика")== -1):
		return False
	return True
random.seed(20)
lnk = "https://znanija.com/task/"
f = open('links.txt','w')
sl = 0
count = 0
RANGE_START = 600001
RANGE_END = 700001
RANGE_DIF = RANGE_END - RANGE_START
for i in range (RANGE_START,RANGE_END):
    if isUncheckedMath(lnk + str(i)):
        f.write(lnk + str(i) + "\n")
        count = count + 1
        if(not(count % 1000)):
        	f.write("\n")
    rangedif = RANGE_END - RANGE_START
    if(not((i - RANGE_START) % (RANGE_DIF // 10000))):
    	print("%.2f"%((i - RANGE_START)/(RANGE_DIF // 100)) + "% done...")
q = open("count.txt","w")
q.write(str(count))
q.close()
f.close()
