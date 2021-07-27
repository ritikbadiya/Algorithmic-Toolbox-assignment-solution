#Uses python3

import sys

def tie(a,b):
    if(a+b>b+a):
        return a
    return b
                   
        
    
def largest_number(a):
    #write your code here
    for k in range(len(a)):
        for i,j in enumerate(a[:-1]):
            #print(a[i+1],j,tie(a[i+1],j))
            if(a[i+1]==tie(a[i+1],j)):
                a[i],a[i+1]=a[i+1],a[i]
    return "".join(a)       
            
              
        
      
if __name__ == '__main__':
    input = sys.stdin.read()
    data = input.split()
    a = data[1:]
    print(largest_number(a))
    
