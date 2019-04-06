#!/usr/bin/python

ROUND = 4

def check(s):
  
  l = []

  for c in s:
    l.append(ord(c))

  for _ in range(ROUND):
    
    for i in range(len(l)-1):
      l[i+1] ^= l[i]

  res = []

  for i in range(len(l)/4):
    m = l[4*i]
    m = (m << 8) + l[4*i+1]
    m = (m << 8) + l[4*i+2]
    m = (m << 8) + l[4*i+3]
    
    res.append(m)

  if res[0] == 0x666c6167 and res[1] == 0x1d090014 and \
     res[2] == 0x6456727b and res[3] == 0x11381606:
    
    return 1
res = bytearray('666c61671d0900146456727b11381606'.decode('hex'))
print res
for _ in range(4):
  for i in range(len(res)-1):
    temp=copy.deepcopy(res)
    for i in range(len(res)-1):
      temp[i+1] ^= res[i]
      res = copy.deepcopy(temp)
print res

if __name__ == "__main__":

  flag = raw_input("input : ")
  
  if len(flag) != 16:
    exit()
  if check(flag):
    print "FLAG is : " + flag
  else:
    print "T__T"
      