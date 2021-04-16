from colour import Color
class GreenScale:
    def __init__(self, iterations):
        self.__originalColors = ['black', '#002600', '#e3ffe3', 'white']
        self.__step = int(iterations / len(self.__originalColors)) + 1
        self.__palette = self.__makePalette()

    def __makePalette(self):
        palette = []
        for colorCode in self.__originalColors:
            palette += self.__makeColor(colorCode)
        return palette

    def __makeColor(self, colorCode):
        color = Color(colorCode)
        colors = list(color.range_to('green', self.__step))
        for i in range(len(colors)):
            colors[i] = colors[i].hex_l
        return colors

    def getColor(self, n):
        return self.__palette[n]
