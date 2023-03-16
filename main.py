h = 0
while 3 > h or 10 < h:
    if h < 3 or h > 10:
        h = int(input('Height of the parallelogram (From 3 to 10): '))
w = 0
while 3 > w or 10 < w:
    if w < 3 or w > 10:
        w = int(input('Width of the parallelogram (From 3 to 10): '))

before = (h - h)
after = (h - 1)
for x in range(0,h):
    for b in range(0,before):
        print('--', end='')
    for y in range(0,w):
        print("*", end="")
    for a in range(0, after):
        print('--', end='')
    print()
    before = before +1
    after = after -1