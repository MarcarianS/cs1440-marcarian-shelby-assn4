class FractalInformation:
    def __init__(self):
        # This dictionary contains the different views of the fractals you can make
        # with this program.
        # For convenience I have placed these into a dictionary so you may easily
        # switch between them by entering the name of the image you want to generate
        self.__fractalDictionary = {
                                'fulljulia': {
                                    'type': 'julia',
                                    'z': complex(-1.0, 0.0),
                                    'centerX':     0.0,
                                    'centerY':     0.0,
                                    'axisLen':  4.0,
                                    },

                                'hourglass': {
                                    'type': 'julia',
                                    'z': complex(-1.0, 0.0),
                                    'centerX':     0.618,
                                    'centerY':     0.00,
                                    'axisLen':  0.017148277367054,
                                },

                                'lakes': {
                                    'type': 'julia',
                                    'z': complex(-1.0, 0.0),
                                    'centerX': -0.339230468501458,
                                    'centerY': 0.417970758224314,
                                    'axisLen': 0.164938488846612,
                                    },

                                'mandelbrot': {
                                    'type': 'mandelbrot',
                                    'z': complex(0, 0),
                                    'centerX': -0.6,
                                    'centerY': 0.0,
                                    'axisLen': 2.5,
                                },

                                'spiral0': {
                                    'type': 'mandelbrot',
                                    'z': complex(0, 0),
                                    'centerX': -0.761335372924805,
                                    'centerY': 0.0835704803466797,
                                    'axisLen': 0.004978179931102462,
                                },

                                'spiral1': {
                                    'type': 'mandelbrot',
                                    'z': complex(0, 0),
                                    'centerX': -0.747,
                                    'centerY': 0.1075,
                                    'axisLen': 0.002,
                                },

                                'seahorse': {
                                    'type': 'mandelbrot',
                                    'z': complex(0, 0),
                                    'centerX': -0.745,
                                    'centerY': 0.105,
                                    'axisLen': 0.01,
                                },

                                'elephants': {
                                    'type': 'mandelbrot',
                                    'z': complex(0, 0),
                                    'centerX': 0.30820836067024604,
                                    'centerY': 0.030620936230004017,
                                    'axisLen': 0.03,
                                },

                                'leaf': {
                                    'type': 'mandelbrot',
                                    'z': complex(0, 0),
                                    'centerX': -1.543577002,
                                    'centerY': -0.000058690069,
                                    'axisLen': 0.000051248888,
                                }
                            }

    def getDictionary(self):
        return self.__fractalDictionary

    def getFractal(self, key):
        if key in self.__fractalDictionary:
            return key




