class Mandelbrot4:
    def __init__(self, dictionary):
        self.__dictionary = dictionary
        self.__c = complex(0.0, 0.0)

    def count(self, n):
        for i in range(self.__dictionary['iteration']):
            self.__c = self.__c * self.__c * self.__c + n
            if abs(self.__c) > 2:
                return i
        return self.__dictionary['iteration'] - 1