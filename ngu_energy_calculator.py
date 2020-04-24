



def user_choice(user_choice):
    switcher = {
        5: adventure_alpha_calc,
        1: augment_calc,
    }
    func = switcher.get(user_choice, lambda: "Invalid User Choice")
    print (func())
    # pass



def adventure_alpha_calc():
    print ("NGU Adventure α Calculator Choosen\n")
    print("1: If you want to set a target percentage")
    print("2: If you want to set a certain amount of levels")
    user_choice = int(input("What is your pick \n"))
    # user_choice = 1

    if(user_choice == 1):
        print("You picked to set a target percentage for Adventure stats")
        percent = int(input("What target percentage for Adventure Levels would you like ? \n"))
        # percent = 213
        # percent = percent - 100

        if(percent <= 200):
            tar_level =  (percent - 100) / 0.1
        else:
            tar_level = ((percent - 100) / 3.17) ** (2)
        
        return("You will require {} levels for your pick of {} percentage adventure stats".format(round(tar_level), (percent)))
        # print("You will require {} levels for your pick of {} percentage adventure stats".format(round(tar_level), (percent)))
    else:
        print("You picked to set a target level amount")
        tar_level = int(input("How many levels do you want input for your choice ? \n"))
        # tar_level = 1281

        if(tar_level <= 1000):
            percent = tar_level * 0.1
        else:
            percent = (tar_level ** 0.5) * 3.17
        
        return("You will get {} adventure percentage based on {} levels input".format( round(percent + 100), tar_level))
    

def augment_calc():
    print("You have chosen Augment Calculator\n")
    print("1: Choose to Select Augment Percentage")
    print("2: Choose to Select Augment Level Target")
    user_choice2 = int(input("What is your pick \n"))

    if(user_choice2 == 1):
        print("You selected Augment Percentage")
        percentage = int(input("Enter your Augment percentage \n"))
        tar_level = percentage - 100
        return("Your level will be {} for the target percentage of {}".format(tar_level, percentage))
    else:
        print("You have chosen to select the Augment Level Target")
        tar_level = int(input("Enter the Level of Augments you wish to select\n"))
        percentage = tar_level  + 100
        return("Your Augment bonus Percentage will be {} based on {} levels of this NGU".format(percentage, tar_level))
    
def wandoos_calc():
    print("Should not print if it did then it ran in the wandoos function")
    # pass

def respawn_calc():
    pass

def main():
    print("Welcome to the NGU Energy Calculator \n")
    print("Choose your option")
    print("1: NGU Auguments")
    print("2: NGU Wandoos")
    print("3: NGU Respawn")
    print("4: NGU Gold")
    print("5: NGU Adventure α")
    print("6: NGU Power α")
    print("7: NGU Drop Chance")
    print("8: NGU  Magic NGU")
    print("9: NGU PP")
    user_pick = int(input("Pick the Energy Ritual \n"))
    # user_pick = 2


    user_choice(user_pick)
    # print (numbers_to_strings(user_pick)) 
    # print(switch_test(user_pick))
    # print(switch_test(55))

    # if (choice == 1):
    #     pass
    # elif(choice == ):
    #     pass
    # elif(choice == ):
    #     pass
    # elif(choice == ):
    #     pass
    # elif(choice == ):
    #     pass
    # elif(choice == ):
    #     pass
    # elif(choice == ):
    #     pass
    # choice = 2
    # choice = 3


if __name__== "__main__":
  main()