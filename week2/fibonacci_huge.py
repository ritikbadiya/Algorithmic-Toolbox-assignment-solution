# python3


def fibonacci_number_again_naive(n, m):
    assert 0 <= n <= 10 ** 18 and 2 <= m <= 10 ** 3

    if n <= 1:
        return n

    previous, current = 0, 1
    for _ in range(n - 1):
        previous, current = current, (previous + current) % m

    return current


def fibonacci_number_again(n, m):
    assert 0 <= n <= 10 ** 18 and 2 <= m <= 10 ** 3
    if n <= 1:
        return n


    a=0
    b=1
    lst=[0,1]
    while(True):
        lst.append((lst[-1]+lst[-2])%m)
        if(lst[-1]==1 and lst[-2]==0):
            break
    return lst[((n-1)%(len(lst)-2))+1]





    #type here


if __name__ == '__main__':
    input_n, input_m = map(int, input().split())
    print(fibonacci_number_again(input_n, input_m))

