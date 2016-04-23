#James Law
#This work is licensed under The MIT License.
#See http://opensource.org/licenses/MIT.
import random
import time
import pickle
import winsound
tryAgain=1
cheat=1
ran=0
day=0
forecasts=0
forecastTrue=0
skip=0
iHaveCheated=0

print("Welcome to the elf game!")
print("----------")
while tryAgain==1:
    try:
        days=int(input("How many days do you want to play for?: "))
    except:
        print("Put a whole number!")
        tryAgain=1
    else:
        tryAgain=0
print("The aim of this game is to make the most money you can in {0} days.".format(days))
print("Elves, when not making assorted presents for childen, are miners.")
print("They earn you £15 a day.")
print("But they CANNOT work in the rain, as it is acidic.")
print("I have donated 10 elves and £15 for you to start with.")
input("Press enter to start the game")
print("")
print("=====================")
print("")


#Game
while day<days:
    while True:
        if ran==1:
            cheat=1
            print("")
            print("=====================")
            print("")

        
        day=day+1
        if day>days:
            break
        print("DAY {0}".format(day))#Printing day
        cheat=1


        rain=random.randint(0,1)#Deciding to rain or not
        forecastChoice=random.randint(0,1)
        if forecasts>0:
            print("If you haven't bought a forecast decide how many workers to send now.")
            time.sleep(5)
            input("Press enter to view the forecast for today's weather.")
            forecasts=forecasts-1
            if forecastChoice==0:
                print("There is a 75% chance of sun today.")
                forecastTrue=random.randint(0,3)
                if 2>=forecastTrue>=0:
                    rain=0
                else:
                    rain=1

            if forecastChoice==1:
                print("There is a 75% chance of rain today.")
                forecastTrue=random.randint(0,3)
                if 2>=forecastTrue>=0:
                    rain=1
                else:
                    rain=0
            input("Press enter to view today's weather.")
        else:
            print("Decide now how many workers you want to send out.")
            time.sleep(5)
            input("Press enter to view today's weather.")

    #Weather
        if skip==0:
            time.sleep(.2)
        if rain==1:
            winsound.Beep(800,200)
            winsound.Beep(200,300)
            print("The weather is rainy.")
            
        if rain==0:
            print("The weather is good.")
            winsound.Beep(200,200)
            winsound.Beep(800,300)

        if skip==0:
            time.sleep(2)

    #Outcomes

    #SHOP
        if day<days:
            if skip==0:
                time.sleep(2)
            print("----------")
            print("Welcome to the shop!")
            cheat=1

            if ran==0:
                print("Here You can buy upgrades for your workers and employ new workers.")
            time.sleep(1)
            print("We are currently selling:")
            print("   Elves (£15/day) ~Die if it rains~ |Cost:£15")
            print("   Weather Forecast for 1 day |Cost:£10")
            if day>1:
                print("   Troll (£50/day) ~Run away with all your money if it rains~ |Cost:£30")
            if day>=4:
                print("   Pixies (£30/day) ~Lose £30 if it rains~ |Cost:£15")
            forecasts=999
            if skip==0:
                time.sleep(2)
            input("Press enter to continue.")
            print("")
            print("=====================")
            print("")
print("END OF THE GAME")
            



        

