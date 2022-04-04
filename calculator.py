#define class Calculator
class Calculator:
    def __init__(self, input1 , input2): #intialize two object's attributes; input1 and input2
        self.input1 = input1
        self.input2 = input2
    
    def adder(self):
        return self.input1 + self.input2 #add input1 and input2

    def subtractor(self):
        return self.input1 - self.input2 #subtract input1 and input2

    def multiplier(self):
        return self.input1 * self.input2 #multiply input1 and input2

    def divider(self):
        return self.input1 + self.input2 #divide input1 and input2

    def clear(self): #set both numbers to be 0
        self.input1 = 0
        self.input2 = 0

#main program; ask for first and second number
input1 = int(input("Enter the first number: "))
input2 = int(input("Enter the second number: "))

object = Calculator(input1,input2) # create an object for calculator class
choice = -1 #initialises choice

while choice !=0:
    print("==Operations==")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Clear")
    print("0: Exit")

    choice = int(input("Enter choice: "))
    if choice == 1:
        print("Result: ", object.adder()) #prints addition result with adder method
    elif choice == 2:
        print("Result: ", object.subtractor()) #print subtract result with subtractor method
    elif choice == 3:
        print("Result: ", object.multiplier()) # print multiply result with multiplier method
    elif choice == 4:
        print("Result: ", object.divider()) #print divide result with divider method
    elif choice == 5:
        object.clear() #clear input values
        print("Input1:%d Input2:%d" %(object.input1,object.input2)) #print the values of the 2 numbers after clear
    elif choice ==0:
        print("Bye")
    else:
        print("Invalid choice")
