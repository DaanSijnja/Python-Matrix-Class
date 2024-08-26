import PyMatrix as pm

class System:

    def __init__(self,a,b,c,d,input,state):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.state = state
        self.prevState = 0
        self.input = input
        self.output = self.c*self.state + self.d*self.input
        
    def CalculateNext(self):
        self.prevState = self.state
        self.state = self.a*self.prevState + self.b*self.input
        self.output = self.c*self.state + self.d*self.input

    

A = pm.Matrix([[0,1],
               [1,1]])

B = pm.Matrix([[0,0],
               [0,0]])     

C = pm.Matrix([[1,0],
               [0,0]])

D = pm.Matrix([[0,0],
               [0,0]])

input = pm.Matrix([[0],
                   [0]])

state = pm.Matrix([[0],
                   [1]])

system = System(A,B,C,D,input,state)

for i in range(50):
    print((system.output).value[0][0])
    system.CalculateNext()
        