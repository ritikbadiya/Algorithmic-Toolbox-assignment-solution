# Uses python3
from sys import stdin

def last_digit_of_the_sum_of_fibonacci_numbers(no):
    no=no%60
    if(no<2):
        return no
    no=no+1
    a,b=0,1
    for i in range(2,no):
        b=b+a
        a=b-a
        b=b%10
        a=a%10
        
    return     b
def fibonacci_sum_squares_naive(n):
    ans=last_digit_of_the_sum_of_fibonacci_numbers(n)*last_digit_of_the_sum_of_fibonacci_numbers(n+1)
    return ans%10

if __name__ == '__main__':
    n = int(stdin.read())
    print(fibonacci_sum_squares_naive(n))
