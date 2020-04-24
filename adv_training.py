

def user_choice(choice):
    switcher = {
        1: pow_tough_calc,
        2: block_calc,
        3: wandoos_calc,
    }
    func = switcher.get(choice, lambda: "Invalid User Choice")
    # print(func())
    print(func())



def block_calc():
    print("Block Calculator Choosen")

def wandoos_calc():
    print("Wandoos Calculator Choosen")

def pow_tough_calc():
    print("Power Toughness Calculator Chosen")
    print("1: Target Level for Calculator")
    print("2: Percentage Target for Training")
    user_choice = int(input("Select Your option\n"))
    # user_choice = 2

    if(user_choice == 1):
        print("Target Level Calculator Choosen")
        tar_level = int(input("Enter the Advanced Training Level you would like to check \n"))
        percentage = (tar_level ** (1/2.5)) * 10
        return("With a target level of {} you will get a percentage bonus of {}".format(tar_level, round(percentage)))

    else:
        print("Advance Training Percentage Target Selected")
        percentage = int(input("Enter the Percentage Level you would like to check \n"))
        tar_level =  (percentage / 10) **(2.5)
        return ("With a Advance training Percentage Level of {} you will need a target level of {}".format(percentage, tar_level))



def main():
    print("hello world")
    print("You have chosen the Adv Training Calculator")
    print("1: Power Toughness Calculator ")
    print("2: Block Calculator")
    print("3: Wandoos Calculator")

    # choice = int(input("Enter Selection\n"))
    choice = 1

    user_choice(choice)



if __name__ == "__main__":
    main()