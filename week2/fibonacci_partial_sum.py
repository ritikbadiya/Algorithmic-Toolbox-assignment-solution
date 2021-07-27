# Uses python3
import sys

def last_digit_of_the_sum_of_fibonacci_numbers(no):
    no=no%60
    if(no<3):
        return no
    no=no+3
    a,b=0,1
    for i in range(2,no):
        b=b+a
        a=b-a
        b=b%10
        a=a%10
        
    return ((b-1)%10)    
#last_digit_of_the_sum_of_fibonacci_numbers(int(input()))
def fibonacci_partial_sum_naive(from_, to):
    a,b=last_digit_of_the_sum_of_fibonacci_numbers(from_-1),last_digit_of_the_sum_of_fibonacci_numbers(to)
    if(b<a):
        b=10+b
    return(b-a)  

if __name__ == '__main__':
    input = sys.stdin.read();
    from_, to = map(int, input.split())
    print(fibonacci_partial_sum_naive(from_, to))
