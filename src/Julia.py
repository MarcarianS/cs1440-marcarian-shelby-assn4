class Julia:

    def __init__(self, dictionary):
        self.__dictionary = dictionary
        self.__c = complex(self.__dictionary['creal'], self.__dictionary['cimag'])

    def count(self, n):
        for i in range(self.__dictionary['iterations']):
            n = n * n + self.__c
            if abs(n) > 2:
                return i
        return self.__dictionary['iterations'] - 1
