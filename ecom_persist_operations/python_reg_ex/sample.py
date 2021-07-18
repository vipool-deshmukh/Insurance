import re

values = "asdhja    120.102.301.23 dasjkd   382129 289.238.03.12  asda adashj 012.012.120.120 1238"

for item in values[::2]:
    print(item)

import sys
sys.exit(0)


ans =re.findall('[\d]{1,3}[\.]{1}[\d]{1,3}[\.]{1}[\d]{1,3}[\.]{1}[\d]{1,3}',values)
#print(ans)

for item in ans:                            #r'\n'      --> '\\n'
    records = re.split(r'.',item)       # . meaning--. given inside re --> re meaning cha meaing
    if len(records)>4:
        print('invalid')
    else:
        for item in records:
            print(int(item),end='.')
    print('\n')


import sys
sys.exit(0)


print(len(values))

                                                        #4 grps
ans1 = re.findall('[a]{5,9}',values)  #min 2 or max 5           #AAAAAA CHAR SEARCH--> MIN 2 CHARS --> AA
ans2 = re.findall('[a]{2,}',values)   #min or max --> n     # 2 grps

print(ans1)
print(ans2)
import sys
sys.exit(0)
ans3 = re.findall('[a]{3}',values)    #STRICT 3
ans4 = re.findall('[a]?',values)      #0|1 -->
ans5 = re.findall('[a]*',values)    #0 OR MORE
ans6 = re.findall('[a]+',values)    #1 OR MORE

print(ans1)
print(ans2)
#print(ans3)
print(ans4)
print(ans5)
print(ans6)

import sys
sys.exit(0)



ans = re.split('@','921212312@2192@xxx.in2414455')
print(ans)

import sys
sys.exit(0)


ans = re.findall('[\w]+@[a-z A-Z]+[\.]{1}[\w]+',values)
#print(ans)

for item in ans:
    records = re.split('@',item)        #[part1,part2]
    #print(records)
    if len(records)>2 or records[0].isnumeric():
        print('\tInvalid Email ',item)
    else:
        print('Valid EMail',item)


#ans = re.findall('[\w]+[@]{1}[a-z A-Z 0-9]{2,}[\.]{1}[\w]+',values) # or codition --> 2 patterns -->   {} + {} -->  +Ve/-ve lookahead / lookbehind..
#print(ans)
import sys
sys.exit(0)

#ans = re.findall('\w+@\w{2,}.\w{2,}',values)  #strictly one-->
#print(ans)

import sys
sys.exit(0)
import sys



ans = re.findall("[a]*",values)
print(ans)

import sys
sys.exit(0)


#email address --> 1@2.2        --> min len --> 7           --> min -- 7 letters
    # shri@gmail.com                s@gmail.com

#ans = re.findall('\d+',values)


ans = re.findall('[\d]{5}',values)
print(ans)

import sys
sys.exit(0)

ans = re.findall('\w+@\w{2,}.\w{2,}',values)
print(ans)
import sys
sys.exit(0)


for ch in values:
    if ord(ch) >=48 and ord(ch)<=56:
        print(ch)

