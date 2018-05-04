fp = open("./master/log.txt")
for i, line in enumerate(fp):
    if i > 5 and i < 11:
        print(line)
