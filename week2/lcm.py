def lcm(a, b):
    assert 1 <= a <= 2 * 10 ** 9 and 1 <= b <= 2 * 10 ** 9
    def gcd(a, b):
        if(b==0):
            return a
        return gcd(b,a%b)
    return int((a*b)/gcd(max(a,b),min(a,b)))
    # type here


if __name__ == '__main__':
    input_a, input_b = map(int, input().split())
    print(lcm(input_a, input_b))

