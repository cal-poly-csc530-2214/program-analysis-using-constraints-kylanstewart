class Precondition:
    def __init__(self, entry, exit):
        self.entry = entry
        self.exit = exit

class NeighborhoodStructure:
    def __init__(self, exps, n):
        self.exps = exps
        self.n = n
        assert(len(self.exps) == n)

def WPreFromPre(I):
    print("WPreFromPre: ", I)

def WPre(N):
    print("WPre: ", N)

def SPost(N):
    print("WPre: ", N)

def main():
    I = ""
    N = NeighborhoodStructure([], 0)
    WPreFromPre(I)
    WPre(N)
    SPost(N)

main()
