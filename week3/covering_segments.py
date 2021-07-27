# Uses python3
import sys
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')

def optimal_points(segments):
    segments=sorted(segments,key=lambda x:x[0])

    no=[segments[-1][0]]

    for i in segments[::-1]:
        f=False
        for j in no:

            if(i[0]<=j and i[1]>=j):
                f=True
                break
        if(not f):
            no.append(i[0])
            f=False
            
    return no[::-1]        
    
  
if __name__ == '__main__':
    input = sys.stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    print(*points)
