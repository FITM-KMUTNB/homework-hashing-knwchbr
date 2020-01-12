def xhash():
    more = 'y'
    #mydict = dict()
    while more == 'y'or'Y':
        name = input('Name :')
        #print('hash is : %d' %hash(name)

        y_dict={'TAN':'00001','MAC':'00002','NUT':'00003','PAK':'00004','FAS':'00005','ZAX':'00006','NEX':'00007','PEN':'00008','PHU':'00009','CHO':'00010'}
        sum = 0
        result = 0
        for i in range(len(name)):
            sum = sum + ord(name[i]) 
            result = (sum % 10)
        print(result)
        print(y_dict.get(name))
        more = input('Add more (y): ')
xhash()

'''def rehash():
    print((sum+1)%10) 
rehash()'''

   
