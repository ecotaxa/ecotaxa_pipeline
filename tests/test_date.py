# Sebastien Galvagno 

def date(data):
    return data[:4]+data[5:7]+data[8:10]

def time(data):
    # //return str(int(data[11:13])*60)+data[15:17]
    print( data[11:13])
    print( data[14:16])
    print( str(int(data[11:13])*60+int(data[14:16])) )
    return data[11:13]+data[14:16]

t = "2019/11/25 21:50:15.277"
print(t)
d = date(t)
assert d == "20191125"
print(d)
d = time(t)
print(d)
assert d == "2150"


t = "2019/13/25 13:49:15.277"
print(t)
d = date(t)
assert d == "20191325"
print(d)
d = time(t)
print(d)
assert d == "1349"

name = "20191125_215015.277.1.png"
def id(name):
    return name[:-4]

n = id(name)
print(n)
assert n == "20191125_215015.277.1"