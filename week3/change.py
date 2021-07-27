# python3


def money_change(money):
    assert 0 <= money <= 10 ** 3
    #type here
    a=money//10
    b=(money-a*10)//5
    c=(money-a*10-b*5)
    return(a+b+c)

if __name__ == '__main__':
    input_money = int(input())
    print(money_change(input_money))

