#!/usr/bin/env python
# coding: utf-8

# In[1]:


##Answer1:

def difference(h1, m1, h2, m2):
    t1 = h1 * 60 + m1

    t2 = h2 * 60 + m2
      
    if (t1 == t2): 
        print("Both are same times")
        return 
    else:

        diff = t2-t1

    h = (int(diff / 60)) % 24

    m = diff % 60
  
    print(h, ":", m)

if __name__ == "__main__":
      
    difference(7, 20, 9, 45)
    difference(15, 23, 18, 54)
    difference(16, 20, 16, 20)


# In[ ]:


##Answer2:

import time

start_time=time.time()
end_time=start_time
lap_num=1

print("Click on ENTER to count laps.\nPress CTRL+C to stop")

try:
   while True:

      input()
      time_laps=round((time.time() - end_time), 2)

      tot_time=round((time.time() - start_time), 2)

      print("Lap No. "+str(lap_num))
      print("Total Time: "+str(tot_time))
      print("Lap Time: "+str(time_laps))

      print("*"*20)

      end_time=time.time()
      lap_num+=1

except KeyboardInterrupt:
   print("Exit!")


# In[ ]:


##Answer3:

import time
import datetime
  
  
string = "24/05/2022"
print(time.mktime(datetime.datetime.strptime(string, "%d/%m/%Y").timetuple()))


# In[ ]:


##Answer4:

from datetime import datetime
  
  
timestamp = 1545730073
dt_obj = datetime.fromtimestamp(1140825600)
  
print("date_time:",dt_obj)
print("type of dt:",type(dt_obj))


# In[ ]:


##Answer5:

import datetime
import calendar
  
def day_occur_time(year):

    days = [ "Monday", "Tuesday", "Wednesday", 
           "Thursday",  "Friday", "Saturday",
           "Sunday" ]

    L = [52 for i in range(7)]

    pos = -1
    day = datetime.datetime(year, month = 1, day = 1).strftime("%A")
    for i in range(7):
        if day == days[i]:
            pos = i

    if calendar.isleap(year):
        L[pos] += 1
        L[(pos+1)%7] += 1
         
    else:
        L[pos] += 1

    for i in range(7):
        print(days[i], L[i])

year = 2019
day_occur_time(year)


# In[ ]:


##Answer6:

import re
  
  
def check(str, pattern):

    if re.search(pattern, str):
        print("Valid String")
    else:
        print("Invalid String")

pattern = re.compile('^[1234]+$')
check('2134', pattern)
check('349', pattern)


# In[ ]:


##Answer7:

import re
 
 
string = "ThisIsGeeksforGeeks !, 123"

uppercase_characters = re.findall(r"[A-Z]", string)
lowercase_characters = re.findall(r"[a-z]", string)
numerical_characters = re.findall(r"[0-9]", string)
special_characters = re.findall(r"[, .!?]", string)
 
print("The no. of uppercase characters is", len(uppercase_characters))
print("The no. of lowercase characters is", len(lowercase_characters))
print("The no. of numerical characters is", len(numerical_characters))
print("The no. of special characters is", len(special_characters))


# In[ ]:


##Answer8:

import re 
from collections import Counter 
  
def most_occr_element(word):

    arr = re.findall(r'[0-9]+', word)    

    maxm = 0  

    max_elem = 0
    
    c = Counter(arr)
    
    for x in list(c.keys()):
  
        if c[x]>= maxm:
            maxm = c[x]
            max_elem = int(x)
                  
    return max_elem

if __name__ == "__main__": 
    word = 'tit55for55tat4ksabc3dr2x'
    print(most_occr_element(word))


# In[ ]:


##Answer9:

import re
  
def extractMax(input):

     numbers = re.findall('\d+',input)

     numbers = map(int,numbers)
  
     print max(numbers)

if __name__ == "__main__":
    input = '100klh564abc365bg'
    extractMax(input)


# In[ ]:


##Answer10:

import re
   
def putSpace(input):
 
    words = re.findall('[A-Z][a-z]*', input)

    for i in range(0,len(words)):
    words[i]=words[i][0].lower()+words[i][1:]
    print(' '.join(words))

if __name__ == "__main__":
    input = 'BruceWayneIsBatman'
    putSpace(input)

