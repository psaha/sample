from numpy import pi,exp

class Lemlim:
    H = 4
    W = 2*H-1
    def __init__(self):
        self.M = [ 200+200j , 50+0j , -50+0j ]
        self.r = self.W*[0j]
        self.z = self.W*[self.M[0]]
        for k in range(1,self.H):
            self.r[k] = exp(2j*pi*k/self.H)
            self.r[k+self.W/2] = exp(2j*pi*k/self.H)
    def p(self):
        print self.r

sad = Lemlim()

sad.p()





