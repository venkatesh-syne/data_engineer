class maths:
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z

    def square(self):          # a square function
        return self.x ** 2

    def cube(self):            # a cube function
        return self.x ** 3

    def add(self):
        return self.z + self.y

    def absolute(self):        # an absolute value function
        if self.x >=0:
            return self.x
        else:
            data = -2 + self.x
            return data

res = maths(int(4),int(3),int(2))
print(res.add())