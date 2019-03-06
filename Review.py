class CaesarMachine:
    def __init__(self, k):
        self.key = k

    def encrypt(self, message):
        alpha = "abcdefghijklmnopqrstuvwxyz"
        alpha += alpha.Upper()
        accum = ""
        for c in message:
            if (c in alpha):
                val = ord(c) + self.key
                accum+= char(val)
            else:
                accum +=c
        return accum

#seperate review code
def reverse(colin):
    #for tuples
    colin2 = ()
    for i in colin:
        colin2 += (i,) + colin2
    return colin2
