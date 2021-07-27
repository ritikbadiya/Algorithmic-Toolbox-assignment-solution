# python3


def compute_min_number_of_refills(d, m, stops):
    assert 1 <= d <= 10 ** 5
    assert 1 <= m <= 400
    assert 1 <= len(stops) <= 300
    assert 0 < stops[0] and all(stops[i] < stops[i + 1] for i in range(len(stops) - 1)) and stops[-1] < d
    cc=m
    cl=0
    nf=0
    stops.append(d)

    for j,i in enumerate(stops):
        if i-cl<=cc:
            cc=cc-(i-cl)
            cl=i
            
            if(not j==len(stops)-1 and stops[j+1]-i>cc):
                cc=m
                nf+=1
        else:
            return -1
    return nf



if __name__ == '__main__':
    input_d = int(input())
    input_m = int(input())
    input_n = int(input())
    input_stops = list(map(int, input().split()))
    assert len(input_stops) == input_n

    print(compute_min_number_of_refills(input_d, input_m, input_stops))

