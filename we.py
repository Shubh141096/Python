import urllib2
import urllib
from bs4 import BeautifulSoup as BS
import pyttsx
import lxml.html

import unicodedata  # for unicode error

def wea(cntry,city):
    we  = open('we.txt','w')
    url = "http://www.timeanddate.com/weather"
    we.write(url+"/"+cntry+"/"+city)
    we.close()
    #print url+"/"+cntry+"/"+city
    #data = {}
    #data['country'] = cntry
    #data[cntry] = city
    #url_values = urllib.urlencode(data)

    we  = open('we.txt','r')
    full_url = we.readline()
    #print full_url
    we.close()
    we  = open('we.txt','w')
    src = urllib2.urlopen(full_url).read()
    bs = BS(src,"lxml")
    list1 = [0]
    list2 = [0]
    list3 = [0]
    a,b,c = 0,0,0
    for n in bs.find_all("div", {"id": "qlook"}):
        for i in n.find_all("div"):
            Value1 =  i.text
            tmp = unicodedata.normalize('NFKD', Value1).encode('ascii','ignore')
            list1.insert(a,tmp)
            a = a+1
    for n in bs.find_all("div", {"id": "qlook"}):
        for i in n.find_all("p"):
            Value1 = i.text
            tmp = unicodedata.normalize('NFKD', Value1).encode('ascii','ignore')
            list2.insert(b,tmp)
            b = b+1
    for n in bs.find_all("div", {"id": "qfacts"}):
        for i in n.find_all("p"):
            Value1 = i.text
            tmp = unicodedata.normalize('NFKD', Value1).encode('ascii','ignore')
            list3.insert(c,tmp)
            c = c+1
    engine = pyttsx.init()
    voice = engine.setProperty('rate',140)
    # print list1
    # print list2
    # print list3
    we.write(list3[0]+"\n")
    we.write("Current Temperature : "+list1[1]+"\n")
    engine.say(list3[0])
    engine.say("weather is "+list2[0])
    engine.say("Current Temperature : "+list1[1])
    for i in range(1,len(list2)-1):
        we.write(list2[i]+"\n")
        engine.say(list2[i])
    for i in range(1,len(list3)-1):
        we.write(list3[i]+"\n")
        engine.say(list3[i])
    engine.runAndWait()


if __name__ == "__main__":
    cntry,city = map(str,raw_input().split())  #usa,india,australia,uk,japan
    wea(cntry,city)