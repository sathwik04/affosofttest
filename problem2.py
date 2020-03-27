from collections import defaultdict

d = defaultdict(int)
for word in open('text.txt').read().split():
    d[word] += 1
print()
print(d)