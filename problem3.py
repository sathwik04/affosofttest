def names():
    names = []
    name = input('Enter student name: ').strip() # get first name
    while name != '':
        names.append(name)
        name = input('Enter next student name: ').strip() # get next name

    for n in set(names): # in a set, no values are repeated
        print ('%s is mentioned %s times' % (n, names.count(n)))
        # print output
names()