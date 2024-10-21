#function to solve the collatz conjecture
#The Collatz Conjecture (from 1937) states that, no matter what number you start with, 
# if you follow two simple rules, you will always (eventually) end up at 1. 

def collatz():
    '''Solving the Collatz conjecture'''
    try:
        number=input('Enter a number: ')
        A=int(number)
        while True:
            if A==1:
                break
            if A%2==0:
                A=A//2
                print(A)
                continue
            if A%2==1:
                A=3*A + 1
                print(A)
                continue
    except ValueError:
        print('only integers')
        
    
    # except ValueError:
    #     print('Your input must be a string')
    
if __name__=='__main__':
    '''calls the main function'''
    collatz()
