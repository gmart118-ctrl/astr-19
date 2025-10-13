#This program will descibe my favoirte animal

#define a class for a animal
class Animal:
	#The following function runs when you create a new Animal
	def __init__(self, name, arm_length, leg_length, num_eyes, has_tail, furry):
		#These are the planet's "attributes"
		self.name = name
		self.arm_length = arm_length
		self.leg_length = leg_length
		self.num_eyes = num_eyes
		self.has_tail = has_tail
		self.furry = furry

#This function prints out the information of the Animal
	def describe(self):
		print(f"Animal name: {self.name}")
		print(f"Length of arms: {self.arm_length}")
		print(f"Length of legs: {self.leg_length}")
		print(f"Number of eyes: {self.num_eyes}")
		print(f"Has a tail: {self.has_tail}")
		print(f"Is furry: {self.furry}")

#Main program
def main():
	turtle = Animal("Turtle", 51.0, 51.0, 2, True, False)
	turtle.describe()

	#Run the program
if __name__=="__main__":
		main()