def printInDecreasing(x):
    
    while(x >= 0):
      print(x,end=" ")       
      x -= 1

def main():
    
    # Testcase input
    testcases = int(input())
    
    # Looping through testcases
    while(testcases > 0):
        x = int(input())
        
        printInDecreasing(x);
        
        print ()
        
        testcases -= 1
        print("~")
 
if __name__ == '__main__':
    main()
