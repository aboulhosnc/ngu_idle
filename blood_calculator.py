import numpy as np  
import math

# print()

# input("Enter the percentage needed")


def num_convert(number):
    """This converts a number to the suffix for long numbers"""
    digits = int(math.log10(number))+1
    counter = 0
    suffix = [ "hundred", "thousand", "million", "billion", "trillion"]
    while( digits > 3):
            number = number / 1000
            counter = counter + 1
            digits = digits - 3
    answer = ("{} {}".format(number, suffix[counter] ))
    return answer
    # print(digits)

    # if(num )


def blood_spag(choice, user_choice):
    if (choice == 1):
        result = 2 ** (user_choice - 1) * 10000
        result_2 =2 ** (user_choice) * 10000
        print(result, result_2)
        return result, result_2
    else:
        user_result = round(math.log2(user_choice/10000) + 1)
        user_result_2 = round(2 ** (user_result ) * 10000)
        # user_result = 50
        print(user_result)
        print (user_result_2)
        return user_result, user_result_2

def blood_spag_choice():
        """ Blood Spagetti Choice """
        print("You selected choice 1")
        print("Choose Additional Choices :")
        print("1: If you want to set a target drop percentage ")
        print("2: If you want to set the amount of blood you used")
        choice_2 = int(input("Pick your choice\n"))
        # choice_2 = 2
        # choice_2 = 1

        if(choice_2 == 1):
            print("You have selected choice to enter a target percentage")
            percent = int(input("Enter your target Drop Chance Percentage\n"))
            # percent = 19
            user_num,user_num2 = (blood_spag(1,percent))
            print("You need between {} and {} blood for {} percent ".format(num_convert(user_num),num_convert(user_num2), percent))
            
        else:
            print("You have selected choice to enter an amount of blood")
            blood_num = int(input("Enter the amount of blood you have \n"))
            # blood_num = 1355000000
            user_num, new_num = (blood_spag(2,blood_num))
            print("You will need {} to get to {} percent".format( num_convert(new_num - blood_num), (user_num + 1)))


def count_gold(choice,user_num):
    """ Select Counterfeit Gold for ritual choice"""
    
    # choice to find specific blood needed for a gps target
    if(choice == 1):
        blood_num = 2 ** (math.sqrt(user_num) - 1) * 1000000
        # blood_num2 = 2 ** (math.sqrt(user_num + 1) - 1) * 1000000
        return blood_num
    
    else:
        percent_num =  (math.log2(user_num/1000000) + 1) ** 2
        blood_num = 2 ** (math.sqrt(percent_num + 1) - 1) * 1000000
        return percent_num, round(blood_num)

def count_gold_choice():
    """ Selected counterfeit gold choice """

    print("You have chosen Counterfeit Gold")
    print("Choose Additional Choices :")
    print("1: If you want to set a GPS Bonus Percentage ")
    print("2: If you want to set the amount of blood you used")


    choice2 = int(input("Pick your choice \n"))
    # choice2 = 1
    # choice2 = 2

    if( choice2 == 1):
        print("You have selected a GPS Bonus Percentage")
        gps_percent = int(input("Enter the target percentage \n"))
        # gps_percent = 128

        user_num = num_convert(count_gold(1,gps_percent))
        user_num2 = num_convert(count_gold(1,gps_percent + 1))
        print("You will need between {} blood and {} blood to get the target of {} percent".format(user_num, user_num2, gps_percent))
    
    else:
        print("You have selected an amount of blood to enter to find the GPS Bonus")
        sel_blood = int(input("Enter the blood amount \n"))
        # sel_blood = 1307000000
        user_percent, blood_num = count_gold(2,sel_blood)
        new_num = num_convert(blood_num - sel_blood)
        print("You will get {} percent bonus gold".format(user_percent))
        print("You need {} blood to get to {} percent".format(new_num, (user_percent + 1)))


def iron_pill(choice, user_num):
    """ Pick iron pill choice"""
    if (choice == 1):
        blood_amount = user_num ** (1 / 0.25)
        blood_2 = (user_num + 1) ** (1/0.25)
        return num_convert(blood_amount), num_convert(blood_2)
    
    else:
        adv_stat = user_num ** (0.25)
        blood_amount = (adv_stat + 1) ** (1/0.25)
        blood_amount = round(blood_amount) - user_num
        # return round(adv_stat)
        return (adv_stat), num_convert(blood_amount)

def iron_pill_choice():
    print("You have picked Iron Pill option")
    print("Choose Additional Choices :")
    print("1: If you want to set a Adveture Stats target ")
    print("2: If you want to set the amount of blood you used")

    choice_2 = int(input("What option will you pick \n"))
    # choice_2 = 2

    if (choice_2 == 1):
        print("You have picked to set an Adventure Stat target")
        print("What will your adventure target be")
        user_choice = int(input("Enter the target Adventure Stat\n"))
        # user_choice = 205
        blood_num, user_num2 = iron_pill(1,user_choice)
        print("You will need between {} blood and {} blood  to get that Adventure target".format(blood_num, user_num2))
    
    else:
        print("You have selected to enter the amount of blood for the ritual")
        print("How much blood will you enter")
        user_choice = int(input("Enter the amount of blood \n"))
        # user_choice = (2.006 * 1000000000)
        adv_stat, user_num2 = iron_pill(2,user_choice)
        # adv_stat = iron_pill(2,user_choice)

        print("You will get an adventure stat bonus of {}".format(adv_stat))
        print("You will need an additional {} blood to get to {} amount of stats".format(user_num2, (adv_stat + 1)))


def main():
    print("Welcome to the Blood Calculator")
    print("Choose your option")
    print("1: Blood Spagetti")
    print("2: Counterfeit Gold")
    print("3: Iron Pill")
    choice = int(input("Pick blood magic ritual \n"))
    # choice = 2
    # choice = 3

    if(choice == 1):
        blood_spag_choice()
    
    elif(choice == 2):
        count_gold_choice()

    else:
        iron_pill_choice()

if __name__== "__main__":
  main()