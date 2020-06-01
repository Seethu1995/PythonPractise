class mycalss:
    def values(self,val1,val2):
        print(val1)
        print(val2)
        self.val1=val1
        self.val2=val2
    def add(self):
        print(self.val1+self.val2)
    def mul(self):
        print(self.val1*self.val2)
c=mycalss()
c.values(3,8)
c.add()
c.mul()
