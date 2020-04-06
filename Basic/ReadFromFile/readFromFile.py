filename = input("Enter filename to read it: ")
fp = open(filename, 'r')
lst = list()
line = " "
for line in fp:
    if(line.startswith("He")):
        lst.append(line.split())
fp.close()
for i in range(0, len(lst)):
    print(lst[i][2])
