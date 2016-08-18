import sys

def tmp07(x,y,z):
	return x+"jino"+y+"ha"+z

if __name__ == '__main__' and len(sys.argv)>3:
	print (tmp07(sys.argv[1],sys.argv[2],sys.argv[3]))
print (tmp07("12","kion","22.4"))
