import sys

from ImagePainter import ImagePainter

defaultFractal = 'default'
defaultPalette = 'default'

if len(sys.argv) == 1:
    ImagePainter().paint(defaultFractal, defaultPalette)
elif len(sys.argv) == 2:
    ImagePainter().paint(sys.argv[1], defaultPalette)
elif len(sys.argv) == 3:
    ImagePainter().paint(sys.argv[1], sys.argv[2])
else:
    print("Looks like you entered to wrong number of parameter! This program takes 0, 1, or 2 arguments.")
    sys.exit(1)

