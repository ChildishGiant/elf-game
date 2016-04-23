import pickle
import time
while True:
    username=pickle.load( open( "username.p", "rb" ) )
    highscore=pickle.load( open( "highscore.p", "rb" ) )
    print("The current highscore is {0} and is held by {1}".format(highscore,username))
    time.sleep(.1)
