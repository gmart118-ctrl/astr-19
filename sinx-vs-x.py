#This program will write out a table of
#the function sin(x) vs x
import numpy as np

def main():
	x = np.linspace(0,2*np.pi,10)
	y = np.sin(x)
	print("x", "sin(x)")
	for i in range(10):
		print(x[i], y[i])

if __name__ == "__main__":
	main()