import blood_calculator
import ngu_energy_calculator

# print("hello world")


def main():
    print("Hello World")
    print("Choose your option")
    print("1: Blood Calculator")
    print("2: NGU ENERGY")
    print("3: NGU Magic")
    choice = int(input("Pick your choice for calculations \n"))

    if (choice == 1):
       blood_calculator.main()

    elif(choice == 2):
        ngu_energy_calculator.main()
        # pass
    elif(choice == 3):
        pass
    # choice = 2
    # choice = 3


if __name__== "__main__":
  main()

