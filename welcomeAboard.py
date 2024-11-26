def welcomeAboard(name):
    print ('Welcome',name) 

def main():
    
    # Testcase input
    testcases = int(input())
    
    # Looping through testcases
    while(testcases > 0):
        name = input()
        
        welcomeAboard(name);
        
        testcases -= 1
        print("~")
 
if __name__ == '__main__':
    main()
