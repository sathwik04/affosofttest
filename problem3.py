def names():
    counters = {}

    while True:
        name = input('Enter next name:')

        if name == ' ':
            break

        if name in counters:
            counters[name] += 1
        else:
            counters[name] = 1
    for name in counters:
        if counters[name] == 1:
            print('There is {} student named {}'.format(counters[name], name))
        else:
            print('There are {} student named {}'.format(counters[name], name))

names()