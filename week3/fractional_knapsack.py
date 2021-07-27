# Uses python3
import sys

def get_optimal_value(capacity, weights, values):
    ls=list(zip(weights,values))
    ls=sorted(ls,key=lambda x:x[1]/x[0],reverse=True)
    t=0
    c=0
    for i,j in enumerate(ls):
        if(c+j[0]<capacity):
            t+=j[1]
            c+=j[0]
        else:
            t+=(j[1]*(capacity-c)/j[0])
            break
    # write your code here
    return t



if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
