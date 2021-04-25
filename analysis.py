from math import pow

class Precondition:
    def __init__(self, cutpoint, val):
        self.cutpoint = cutpoint
        self.val = val

class NeighborhoodStructure:
    def __init__(self, exps, n):
        self.exps = exps
        self.n = n
        assert(len(self.exps) == n)

# find a precondition I' s.t. I(D) => I'. If none, returns None
# TODO: Implement me
def findPre(I, D):
    Iprime = I
    return IPrime

def WPreFromPre(I):
    D = 0
    N = n ** 2
    c = 2 # Is this right? Where does c come from?
    MaxD = pow(N, N//2) * pow(c, N)
    MaxN = MaxD
    for i in range(1, I.n):
        for j in range(1, I.n):
            low = 0
            high = MaxN
            while (high - low > (1/MaxD)):
                mid = (high + low) // 2
                D = mid
                if findPre(I, D) not None:
                    low = mid
                else:
                    high = mid
            D = low
    return IPrime

def WPre(N):
    print("WPre: ", N)

def SPost(N):
    print("WPre: ", N)

def main():
    I = Precondition((0,0), True)
    N = NeighborhoodStructure([], 0)
    WPreFromPre(I)
    WPre(N)
    SPost(N)

main()
