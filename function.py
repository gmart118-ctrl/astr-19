#This will define a function f(x) and print the result
#This will also execute an if statement

def main():	

	x=9
	def f(x): 
		function=x**3+8
		return(function)
	math = f(x)
	if math>27:
		print("YAY!")
		print(math)
	else:
		print("Oh NO!")
		print(math)
if __name__== "__main__":
	main()