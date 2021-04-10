
THRESHHOLD = 2.0


def count(z, max_iter, c):
    for i in range(max_iter):
        z = z * z + c
        if abs(z) > THRESHHOLD:
            return i
    return max_iter

class Julia:
    def pixelsWrittenSoFar(self, rows, cols):
        pixels = rows * cols
        print(f"{pixels} pixels have been output so far")
        return pixels
