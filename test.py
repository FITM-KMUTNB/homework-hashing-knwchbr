'''def xhash():
    name = input('Name :')
    sum = 0
    #for pos in range(len(name)):
        #sum = sum + ord(name[pos])
    for pos in range(len(name)):
        sum = (sum<=5) + ord(name[pos])
    print(sum%11)
xhash()

def rehash(j, firstHV, tablesize):
    print((firstHV + j) % 10)
rehash(j,firstHV,tablesize)
'''

class rec:
    def __init__(self, key, data): 
        self.key = key
        self.data = data
    def __str__(self):
        s = '(' + str(self.key) + ',' + str(self.data) + ')' 
        return s
class HashTable:
    def __init__(self): 
        self.size = 11
        self.table = [None]*self.size 
        self.total = 0
    def hash(key):
        sum = 0
        for pos in range(len(key)):
            sum = sum + ord(key[pos]) 
        return sum % 10
    def hash2(str):
        sum = 0
        for pos in range(len(str)):
            sum = (sum<<5) + ord(str[pos]) 
        return sum%t10
    def rehash(j, firstHV): #linear probing ชนครงั้ ที่j 
        return (firstHV + j) % 10
