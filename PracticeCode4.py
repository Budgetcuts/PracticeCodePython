import turtle

class Lsystem:
    def __init__(self, axiom, angle, distance, iterations, rul):
        self.axiom = ''
        self.iteration = 5
        self.distance = 10
        self.angle = 90
        self.rules = rul

    def applyRules(self,ch):
            return self.rules.get(ch, ch)

    def lsystem(self):
        for i in range(self.iterations):
            accum = ''
            for c in result:
                accum += self.applyRules(c)
            result = accum
        self.axiom = result
        self.result = self.axiom
        return axiom

    def drawLSystem(self):
        t = turtle.Turtle
        t.speed(0)
        for ch in result:
            if (ch =='F'):
                t.forward(self.distance)
            elif(ch == '+'):
                t.right(self.angle)
            elif(ch=='-'):
                t.left(self.angle)
            elif(ch == ']'):
                t.__dict__ = state.pop()
            elif(ch == '['):
                state.append({k:v for
                (k,v) in
                t.__dict__.items()})

        wn = turtle.Screen()
        wn.exitonclick()

    def __str__(self):
        return self.result

def main():
    rules = {'X':'F[-X]+X', 'F':'FF'}
    ls = Lsystem("X", 90, 10, 10, rules)
    print(ls)
    ls.drawLSystem()
main()
