def xhash():
    #mydict = dict()
    name = input('Name :')
    #print('hash is : %d' %hash(name)

    y_dict={'TAN':'00001','MAC':'00002','NUT':'00003','PAK':'00004','FAS':'00005','ZAX':'00006','NEX':'00007','PEN':'00008','PHU':'00009','CHO':'00010'}
    hash_hash = hash(name)%10
    print(hash_hash)
    print(y_dict.get(name))
xhash()