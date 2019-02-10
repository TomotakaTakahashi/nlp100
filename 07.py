import sys

def tmp07(x, y, z):
    return "{}時の{}は{}".format(x, y, z)

if __name__ == '__main__' and len(sys.argv) > 3:
    print (tmp07(sys.argv[1], sys.argv[2], sys.argv[3]))
print (tmp07("12", "気温", "22.4"))
