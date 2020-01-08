from sentiment_analysis import compute_tweets
#Asking the user to input which files they would like to use
tweets = str(input("Which tweet list do you want?"))
keylist = str(input("Which keylist do you want?"))
#If the name they entered does not contain .txt then you would add it for them
if ".txt" not in tweets:
    tweets = tweets + ".txt"
if ".txt" not in keylist:
    keylist = keylist + ".txt"

#Creating the list of timezones and computing it for all of them
#Output each item in the list and what they are
mass_list = compute_tweets(tweets,keylist)


for n in range(len(mass_list)):
    if n == 0:
        print("Eastern time: ")
        print("Happiness Score:",mass_list[n][0])
        print("Number of keyword tweets",mass_list[n][1])
        print("Number of tweets",mass_list[n][2])
    if n == 1:
        print("Central time: ")
        print("Happiness Score:", mass_list[n][0])
        print("Number of keyword tweets", mass_list[n][1])
        print("Number of tweets", mass_list[n][2])
    if n == 2:
        print("Mountain time: ")
        print("Happiness Score:", mass_list[n][0])
        print("Number of keyword tweets", mass_list[n][1])
        print("Number of tweets", mass_list[n][2])
    if n == 3:
        print("Pacific time: ")
        print("Happiness Score:", mass_list[n][0])
        print("Number of keyword tweets", mass_list[n][1])
        print("Number of tweets", mass_list[n][2])
