class Mathematics():
    def __init__(self, arg1):
        self.arg1=arg1

    def calculate(self):
        raise NotImplementedError('Abstract Class example!')

class Sum(Mathematics):

    def calculate(self):
        print(self.arg1+1)
