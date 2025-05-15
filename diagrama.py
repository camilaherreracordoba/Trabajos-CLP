import sys
from railroad import Diagram, Choice
d = Diagram("foo", Choice(0, "bar", "baz"))

with open("diagrama.svg", "w", encoding="utf-8") as f:
    d.writeSvg(f.write)

print("guardado como 'diagrama.svg'")