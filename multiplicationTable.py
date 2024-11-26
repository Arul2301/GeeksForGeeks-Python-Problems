def multiplicationTable(N):
    for i in range(1,11): 
        print(i * N, end=" ") ## Separating by spaces using end =" "
        

def main():
    testcases=int(input()) #testcases
    while(testcases>0):
        N = int(input())
        multiplicationTable(N)
        print()
        testcases-=1
        


        print("~")
if __name__=='__main__':
    main()
