class Julia:

    def __init__(self, dictionary):
        self.__dictionary = dictionary

    def count(self, n):
        c = complex(self.__dictionary['creal'], self.__dictionary['cimag'])
        for i in range(self.__dictionary['iterations']):
            n = n * n + c
            if abs(n) > 2:
                return i
        return self.__dictionary['iterations'] - 1

    def getDictionary(self):
        return self.__dictionary
