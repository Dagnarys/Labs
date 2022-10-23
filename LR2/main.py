from lab_python_oop.rectangle import Rectangle
from lab_python_oop.circle import Circle
from lab_python_oop.square import Square


def main():
    r = Rectangle("синего", 1, 1)
    c = Circle("зеленого", 1)
    s = Square("красного", 1)
    print(r)
    print(c)
    print(s)

if __name__ == "__main__":
    main()