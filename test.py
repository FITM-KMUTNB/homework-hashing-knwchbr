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