def stringJumper(str):
    for i in range(len(str)):
      if(i%2==0):
        print(str[i], end="") ##printing character and separating characters by nothing
def main():
    testcases = int(input()) #testcases
    while(testcases>0):
        str = (input())
        stringJumper(str)
        print()##separating testcases outputs by newlines
        testcases -= 1

        print("~")
if __name__=='__main__':
    main()
