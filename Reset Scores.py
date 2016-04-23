import pickle
username="N/A"
highscore=0
pickle.dump( highscore, open( "highscore.p", "wb" ) )
pickle.dump( username, open( "username.p", "wb" ) )

print("Username has been set to: {0}".format(username))
print("Highscore has been set to: ${0}".format(highscore))
input("CLOSE ME.")
