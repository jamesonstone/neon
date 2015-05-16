"""
how does unit testing work?
"""
class HelloWorld:

    def hello(self, n):
        if type(n) == int:
            return 'hello there, ' + str(n)
        else:
            return 'hello there, ' + n

    def bye(self, n):
        return 'good bye there, ' + n

