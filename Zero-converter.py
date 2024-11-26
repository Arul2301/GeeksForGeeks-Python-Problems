def pos(n):
   while(n!=0):
        n = n-1
        print(n,end=" ")
            
        
    
def neg(n):
  while(n<=0):
    print(n,end=" ")
    n = n+1
        
def main():
    testcases=int(input()) #testcases
    while(testcases>0):
        n = int(input())
        if(n > 0):
            pos(n)
        elif(n < 0):
            neg(n)
        else:
            print("already Zero",end="")
        print()
        testcases-=1
        


        print("~")
if __name__=='__main__':
    main()
