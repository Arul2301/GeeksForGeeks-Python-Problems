def check_status(a, b, flag):
    ##Either True or False is returned
    if((a>0 and b<0) or (a<0 and b>0)):
        return not flag
    elif(a<0 and b<0):
        return flag
    else:
        return False

def main():
    
    # Testcase input
    testcases = int(input())
    
    # Looping through testcases
    while(testcases > 0):
        a = int(input())
        b = int(input())
        flag = input()
        
        if(flag == "True"):
            flag = True
        else:
            flag = False
        
        if(check_status(a, b, flag) is True):
            print ("True")
        else:
            print ("False")
        
        testcases -= 1
        print("~")
 
if __name__ == '__main__':
    main()
