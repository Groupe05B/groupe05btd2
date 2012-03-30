"""doc"""

from operators import add, mul
from logic import and_, or_


def main():
    """doc"""

    print "My application starts...."
    a = 2
    b = 3
    x = True
    y = False
    print add(a, b)
    print mul(a, b)
    print and_(x, y)
    print or_(x, y)

if __name__ == "__main__":
    main()
