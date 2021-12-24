import sys,string,os;


#----------------INPUT--------------------------

#Read Input
N=int(input("Enter value of N for N-queen problem: "));

#Creating a cnf file to store generated encodings
inputfile="/Users/mujingjing/Downloads/nqueen.txt";
outputfile="/Users/mujingjing/Downloads/nqueen_result.txt";
input= open(inputfile,"w");
input.write("c SAT Expression for N="+str(N)+"\n");
spots = N*N;
input.write("c Board has "+str(spots)+" positions" + "\n");


print("c SAT Expression for N="+str(N))
spots = N*N
print("c Board has "+str(spots)+" positions")



#-----FUNCTIONS TO CALCULATE ENCODING VALUES------------------------
#Function to generate encodings of exactly one queen
def exactlyone(list):
    encoding=""
    encoding=encoding+condition_A(list)
    encoding=encoding+condition_B(list)
    return encoding

#Function to generate encodings of condition_A which returns the entire sequence of r/column/diagonal
def condition_A(list):
    encoding=""
    for x in list:
        encoding = encoding +" " +str(x)
    encoding=encoding+" 0\n"
    return encoding

#Function to generate encodings of condition_B which returns the possible combinations for condition_A

def condition_B(list):
    encoding=""
    for x in list:
        for y in list[list.index(x)+1:]:
            encoding = encoding +" -"+str(x)+" -"+str(y)+" 0\n"
    return encoding

def position(r,c,N):
    return r*N+c+1


#---------------GENERATING ENCODING VALUES---------------
#Exactly 1 queen in a row
encoding=""
for r in range(0,N):
    list=[]
    for c in range(0,N):
        location = position(r,c,N)
        list.append(location)
    encoding = encoding+exactlyone(list)

    
#Exactly 1 queen in a column
for c in range(0,N):   
    list=[]
    for r in range(0,N):
        location = position(r,c,N)
        list.append(location)
    encoding = encoding+exactlyone(list)

#Exactly one queen in K+ diagonal
for r in range(N-1,-1,-1):
    list=[]
    for x in range(0,N-r):
        list.append(position(r+x,x,N))
    encoding=encoding+condition_B(list)
    
for c in range(1,N):
    list=[]
    for x in range(0,N-c):
        list.append(position(x,c+x,N))
    encoding=encoding+condition_B(list)
    
#Exactly one queen in K- diagonal
for r in range(N-1,-1,-1):
    list=[]
    for x in range(0,N-r):
        list.append(position(r+x,N-1-x,N))
    encoding=encoding+condition_B(list)

for c in range(N-2,-1,-1):
    list=[]
    for x in range(0,c+1):
        list.append(position(x,c-x,N))
    encoding=encoding+condition_B(list)



print(encoding)
input.write('p cnf ' + str(N*N) + ' ' + str(encoding.count('\n')) + '\n')
input.write(encoding)




