''' PROGRAM TO CHECK FREQUECY OF WORDS IN LINE '''
count = dict()
line = input("Enter string: ")
words = list(line.split())

for i in words:
    count[i] = count.get(i, 0) + 1

for k, v in count.items():
    print(k,v)
    
