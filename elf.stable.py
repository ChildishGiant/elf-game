#James Law
#This work is licensed under The MIT License.
#See http://opensource.org/licenses/MIT.
import random
import time
import pickle
import winsound

money=15
elves=10
elvesKilled=0
cheat=1
ran=0
day=0
tryAgain=1
trolls=0
trollsSent=0
forecasts=0
forecastTrue=0
skip=0
username=pickle.load( open( "username.p", "rb" ) )
highscore=pickle.load( open( "highscore.p", "rb" ) )
pixies=0
pixiesSent=0
iHaveCheated=0

print("Welcome to the elf game!")
print("----------")
print("The aim of this game is to make the most money you can in 10 days.")
print("Elves, when not making assorted presents for childen, are miners.")
print("They earn you £15 a day.")
print("But they CANNOT work in the rain, as it is acidic.")
print("Highscore to beat: £{0} ({1})".format(highscore,username))
print("----------")

print("I have been kind and donated £{0} for you to start with.".format(money))
if elves==1:
    print("But then by magic all of the elves died except that one in the corner. He's yours.")
if 1<elves<6:
    print("But then I got bored of being nice so I killed all the elves but {0}.".format(elves))
if elves>5:
    print("I also have given you {0} elves.".format(elves))
print("")
print("=====================")
print("")


#Game
while day<10:
    while elves>0  or pixies>0 or money>=15 or trolls>0:
        if ran==1:
            cheat=1
            print("")
            print("=====================")
            print("")
            trollsBought=0
            trollsSent=0
            elvesSent=0
            elvesBought=0
            pixiesSent=0
            pixiesBought=0

        
        day=day+1
        if day>10:
            break
        print("DAY {0}".format(day))#Printing day
        cheat=1


        rain=random.randint(0,1)#Deciding to rain or not
        forecastChoice=random.randint(0,1)
        
        if forecasts>0:
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

            if forecasts>1:
                print("{0} Weather forecasts left.".format(forecasts))
            if forecasts==1:
                print("1 Weather forecast left.")

        if ran==1:

            if money>0:
                print("Money left: £{0}".format(money))

            if elves>0:
                print("Elves left: {0}".format(elves))

            if trolls>0:
                print("Trolls left: {0}".format(trolls))

            if pixies>0 :
                print("Pixies left: {0}".format(pixies))
            
    #Sending
    #Elves

        while cheat==1 and elves>0:
            while tryAgain==1:
                try:
                    elvesSent=int(input("How many Elves do you want to send out today?: "))
                except ValueError:
                    print("Put a whole number!")
                    tryAgain=1
                else:
                    tryAgain=0
            tryAgain=1

            if elvesSent==909996:
                    skip=1
                    elves=9999
                    forecasts=9999
                    trolls=9999
                    money=9999999999
                    pixies=9999
                    day=9
                    iHaveCheated=1

            if elvesSent<0 or elvesSent>elves and elvesSent!=909996:
                print("You can't do that, CHEATER!")
                cheat=1

            if elvesSent>=0 and elvesSent<=elves:#checking for legit answers
                cheat=0
        cheat=1
        if skip==0:
            time.sleep(.5)
            
    #Trolls

        while trolls>0 and cheat==1:
            while tryAgain==1:
                try:
                    trollsSent=int(input("How many Trolls do you want to send out today?: "))
                except ValueError:
                    print("Put a whole number!")
                    tryAgain=1
                else:
                    tryAgain=0
            tryAgain=1

            if trollsSent<0 or trollsSent>trolls:
                print("You can't do that, CHEATER!")
                cheat=1

            if trollsSent>=0 and trollsSent<=trolls:#checking for legit answers
                cheat=0
        cheat=1
            
        if skip==0:
            time.sleep(.5)

    #Pixies
            
        while pixies>0 and cheat==1:
            while tryAgain==1:
                try:
                    pixiesSent=int(input("How many Pixies do you want to send out today?: "))
                except ValueError:
                    print("Put a whole number!")
                    tryAgain=1
                else:
                    tryAgain=0
            tryAgain=1

            if pixiesSent>pixies or pixiesSent<0: 
                print("You can't do that, CHEATER!")
                cheat=1

            if pixiesSent>=0 and pixiesSent<=pixies:#checking for legit answers
                cheat=0
        cheat=1
        if skip==0:
            time.sleep(.5)

    #Weather
        if skip==0:
            time.sleep(.2)
        if rain==1:
            winsound.Beep(800,200)
            winsound.Beep(200,300)
            print("The weather is rainy.")
            elves=elves-elvesSent
            trolls=trolls-trollsSent
            
        if rain==0:
            print("The weather is good.")
            winsound.Beep(200,200)
            winsound.Beep(800,300)

        if skip==0:
            time.sleep(.5)

    #Outcomes
    #Elves
            
        if rain==1 and elvesSent==1: #Rainy and sent 1
            print("You have lost 1 Elf.")
            elvesKilled=elvesKilled+elvesSent

        if rain==1 and elvesSent>1: #Rainy and sent more than one
            print("You have lost {0} Elves.".format(elvesSent))
            elvesKilled=elvesKilled+elvesSent

        if rain==0 and elvesSent==1: #Sun and sent 1
            print("You sent 1 Elf to work and have earned £15")
            money=money+15

        if rain==0 and elvesSent>1: #Sun and sent more than one
            money=money+elvesSent*15
            print("You sent {0} Elves to work and have earned £{1}".format(elvesSent,elvesSent*15))

    #Trolls
            
        if rain==1 and trollsSent==1: #rain sent 1 troll
            print("You have lost 1 Troll and all your money.")
            money=0

        if rain==1 and trollsSent>1: #rain sent more than 1 troll
            print("You have lost {0} Trolls and all your money.".format(trollsSent))
            money=0

        if rain==0 and trollsSent==1: #Sun and 1 troll sent
            print("You sent 1 Troll to work and have earned £50")
            money=money+50

        if rain==0 and trollsSent>1: #Sun and more than one troll sent
            print("You sent {0} Trolls to work and have earned £{1}".format(trollsSent,trollsSent*50))
            money=money+trollsSent*50

    #Pixies
            
        if rain==1 and pixiesSent==1: #rain sent 1 pixie
            print("You have lost £30.")
            money=money-30

        if rain==1 and pixiesSent>1: #rain sent more than 1 pixie
            print("You have lost £{0}.".format(pixiesSent*30))
            money=money-pixiesSent*30

        if rain==0 and pixiesSent==1: #Sun and 1 pixie sent
            print("You sent 1 Pixie to work and have earned £30")
            money=money+30

        if rain==0 and pixiesSent>1: #Sun and more than one pixie sent
            print("You sent {0} Pixies to work and have earned £{1}".format(pixiesSent,pixiesSent*30))
            money=money+pixiesSent*30

        if money < 0:
            money=0
        
    #SHOP
        if day<10:
            if skip==0:
                time.sleep(2)
            if elves>=0 and money>=10:
                print("----------")
                print("Welcome to the shop!")
                cheat=1

                if ran==0:
                    print("Here You can buy upgrades for your workers and employ new workers.")
                time.sleep(1)
                print("We are currently selling:")
                if money>=15:
                    print("   Elves (£15/day) ~Die if it rains~ |Cost:£15")
                if forecasts+day<10 and money>=10:
                    print("   Weather Forecast for 1 day |Cost:£10")
                if day>1 and money>=30:
                    print("   Troll (£50/day) ~Run away with all your money if it rains~ |Cost:£30")
                if day>=4 and money>=15:
                    print("   Pixies (£30/day) ~Lose £30 if it rains~ |Cost:£15")
                
                if skip==0:
                    time.sleep(2)

        #Elves
                
                while cheat==1 and money>=15:
                    print("You now have £{0}".format(money))
                    elvesCanBuy=money//15
                    while tryAgain==1:
                        try:
                            if elves>1:
                                elvesBought=int(input("How many Elves would you like to buy? You currently own {0} Elves. (You can afford {1}): ".format(elves,elvesCanBuy)))
                            else:
                                elvesBought=int(input("How many Elves would you like to buy? You currently own 1 Elf. (You can afford {0}): ".format(elvesCanBuy)))
                        except ValueError:
                            print("Put a whole number!")
                            tryAgain=1
                        else:
                            tryAgain=0
                    tryAgain=1

                    elvesCost=elvesBought*15

                    if elvesBought<0:
                        print("No.")
                        cheat=1

                    if elvesCost>money:
                        print("Just give up trying to cheat.")
                        cheat=1

                    if elvesBought==0:
                        print("You have bought 0 Elves.")
                        cheat=0


                    if elvesBought>0 and elvesCost<=money:
                        if elvesBought==1:
                            print("You have bought 1 Elf for £15.")
                            elves=elvesBought+elves
                            money=money-elvesCost
                            cheat=0

                        if elvesBought>1:
                            print("You have bought {0} Elves for £{1}.".format(elvesBought,elvesCost))
                            elves=elvesBought+elves
                            money=money-elvesCost
                            cheat=0
                cheat=1

                if skip==0:
                    time.sleep(0.5)

        #Forecasts
                    
                while cheat==1 and money>=10 and forecasts+day<10:

                    forecastsCanBuy=money//10

                    print("You now have £{0}".format(money))

                    while tryAgain==1:
                        try:
                            forecastsBought=int(input("How many forecasts would you like to buy? (You can afford {0}): ".format(forecastsCanBuy)))

                        except ValueError:
                           print("Put a whole number!")
                           tryAgain=1
                        else:
                            tryAgain=0
                    tryAgain=1

                    if forecastsBought<0:
                        print("No.")
                        cheat=1

                    if forecastsBought*10>money:
                        print("Just give up trying to cheat.")
                        cheat=1

                    if forecastsBought==0:
                        print("You have bought 0 forecasts.")
                        cheat=0

                    if forecastsBought>30 or forecastsBought+forecasts>=30:
                        print("You already own enough forecasts for the rest of the game.")

                    if 10>=forecastsBought>0 and forecastsBought*10<=money and forecastsBought+day+forecasts<=10:
                        if forecastsBought==1:
                            print("You have bought 1 forecast for £10.")
                            forecasts=forecasts+1
                            money=money-10
                            cheat=0

                        if forecastsBought>1:
                            print("You have bought {0} forecasts for £{1}.".format(forecastsBought,forecastsBought*10))
                            forecasts=forecastsBought+forecasts
                            money=money-forecastsBought*10
                            cheat=0
                cheat=1

        #Trolls
                
                while day>1 and cheat==1 and money>=30:
                    trollsCanBuy=money//30
                    print("You now have £{0}".format(money))
                    while tryAgain==1:
                        try:
                            if trolls>1:
                               trollsBought=int(input("How many Trolls would you like to buy? You currently own {0} Trolls. (You can afford {1}): ".format(trolls,trollsCanBuy)))

                            if trolls==1:
                               trollsBought=int(input("How many Trolls would you like to buy? You currently own 1 Troll. (You can afford {0}): ".format(trollsCanBuy)))

                            if trolls==0:
                                trollsBought=int(input("How many Trolls would you like to buy? (You can afford {0}): ".format(trollsCanBuy)))

                        except ValueError:
                           print("Put a whole number!")
                           tryAgain=1
                        else:
                            tryAgain=0
                    tryAgain=1

                    if trollsBought<0:
                        print("No.")
                        cheat=1

                    if trollsBought*30>money:
                        print("Just give up trying to cheat.")
                        cheat=1

                    if trollsBought==0:
                        print("You have bought 0 Trolls.")
                        cheat=0


                    if trollsBought>0 and trollsBought*30<=money:
                        if trollsBought==1:
                            print("You have bought 1 troll for £30.")
                            trolls=trolls+1
                            money=money-30
                            cheat=0

                        if trollsBought>1:
                            print("You have bought {0} trolls for £{1}.".format(trollsBought,trollsBought*30))
                            trolls=trollsBought+trolls
                            money=money-trollsBought*30
                            cheat=0
                cheat=1

        #Pixies
                
                while day>=4 and cheat==1 and money>=15:
                    pixiesCanBuy=money//15
                    print("You now have £{0}".format(money))
                    while tryAgain==1:
                        try:
                            if pixies>1:
                               pixiesBought=int(input("How many Pixies would you like to buy? You currently own {0} Pixies. (You can afford {1}): ".format(pixies,pixiesCanBuy)))

                            if pixies==1:
                               pixiesBought=int(input("How many Pixies would you like to buy? You currently own 1 Pixie. (You can afford {0}): ".format(pixiesCanBuy)))

                            if pixies==0:
                                pixiesBought=int(input("How many Pixies would you like to buy? (You can afford {0}): ".format(pixiesCanBuy)))

                        except ValueError:
                           print("Put a whole number!")
                           tryAgain=1
                        else:
                            tryAgain=0
                    tryAgain=1

                    if pixiesBought<0:
                        print("No.")
                        cheat=1

                    if pixiesBought*15>money:
                        print("Just give up trying to cheat.")
                        cheat=1

                    if pixiesBought==0:
                        print("You have bought 0 Pixies.")
                        cheat=0


                    if pixiesBought>0 and pixiesBought*15<=money:
                        if pixiesBought==1:
                            print("You have bought 1 Pixie for £15.")
                            pixies=pixies+1
                            money=money-15
                            cheat=0

                        if pixiesBought>1:
                            print("You have bought {0} Pixies for £{1}.".format(pixiesBought,pixiesBought*15))
                            pixies=pixiesBought+pixies
                            money=money-pixiesBought*15
                            cheat=0

                else:
                    cheat=0
                    ran=1
            else:
                cheat=0
                ran=1
        else:
            cheat=0
            ran=1


#End
else:
    print("")
    print("=====================")
    print("=====================")
    print("")
    if iHaveCheated==1:
        print("You cheated. No highscore for you.")
    if money>highscore and iHaveCheated==0:
        print("HIGHSCORE!")
        username=input("Please type your name: ")
        highscore=money
        pickle.dump( highscore, open( "highscore.p", "wb" ) )
        pickle.dump( username, open( "username.p", "wb" ) )
    print("That was fun while it lasted.")
    if money>0:
        print("Money left: £{0}".format(money))
    if elves>0:
        print("Elves left: {0}".format(elves))
    if trolls>0:
        print("Trolls left: {0}".format(trolls))
    if pixies>0 :
        print("Pixies left: {0}".format(pixies))
    print("You scored {0} days".format(day))
    if elvesKilled==1:
        print("You only killed 1 elf! DISSAPOINTING.")
    else:
        print("You mangaged to kill {0} elves".format(elvesKilled))

