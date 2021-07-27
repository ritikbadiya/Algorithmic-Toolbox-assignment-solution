# python3
import numpy as np



def compute_optimal_summands(n):
    assert 1 <= n <= 10 ** 9


    # type here
    a=int(((1+8*n)**(0.5)-1)/2)
    summands=list(np.arange(1,a))
    summands.append(n-sum(summands))
    #return ("".join([str(i) for i in summands]))
    return(summands)



if __name__ == '__main__':
    input_n = int(input())
    output_summands = compute_optimal_summands(input_n)
    print(len(output_summands))
    print(*output_summands)

