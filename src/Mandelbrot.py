class Mandelbrot:
    def __init__(self, dictionary):
        self.__dictionary = dictionary

    def count(self, n):
        c = complex(0.0, 0.0)
        for i in range(self.__dictionary['iterations']):
            c = c * c + n
            if abs(c) > 2:
                return i
        return self.__dictionary['iterations'] - 1

    def getDictionary(self):
        return self.__dictionary