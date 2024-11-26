def printIncreasingPower(x):
    i=1
    while(i**2 <= x):
        print(i**2,end=" ")
        i+=1
    
      
def main():
    
    # Testcase input
    testcases = int(input())
    
    # Looping through testcases
    while(testcases > 0):
        x = int(input())
        
        printIncreasingPower(x);
        print ()
        
        
        testcases -= 1
        print("~")
 
if __name__ == '__main__':
    main()
