#Create a function that calculates a user's imc after inputing height and weight

#Method 1
def imc_calculator_1(height, weight):
    imc = weight/(height**2)
    print("Your imc is: " + str(imc))

imc_calculator_1(1.73,60.2)

#Method 2

def imc_calculator_2():
    print("Please input your height and weight\n")
    height = input("Height:")
    weight = input("weight:")
    imc = float(weight) / (float(height) ** 2)
    print("Your imc is: " + str(imc))

imc_calculator_2()