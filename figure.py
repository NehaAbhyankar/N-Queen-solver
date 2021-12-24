import linecache

#Actual output
file3="/Users/mujingjing/Downloads/result.txt";
line = linecache.getline("nqueen_result.txt",2)
line = list(map(int ,line.split(' ')))
for i in range(len(line)-1):
    if int(line[i]) < 0:
        line[i] = 0
    else:
        line[i] = 1
        
n = int(input("Enter value of n from N-queen: "))
def chunks(l, n):
    for i in range(0, len(l)-1, n):
        yield l[i:i + n]
l = (list(chunks(line, n)))
file3 = open("/Users/mujingjing/Downloads/result.txt", 'w')
for i in range(len(l)):
    file3.write(str(l[i]))
    file3.write("\n")


