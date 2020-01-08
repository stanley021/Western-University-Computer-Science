#Creating all the timezone lists for the different sentimental values
#My name is stanley chen and my student number is 251093164

#This is where I check for the timezone, I strip what is unnecessary for the checking, determine whether it is eastern, central, mountain or pacific.
#Depending on the location it will return that specific location.
def fix_location(location_list):
    location_list[0] = location_list[0].strip("[],")
    location_list[1] = location_list[1].strip("[],")
    if  24.660845 < float(location_list[0]) < 49.189787 and -87.518395 < float(location_list[1]) <-67.444574:
        return "eastern"
    if  24.660845 < float(location_list[0]) < 49.189787 and -101.998892 < float(location_list[1]) <-87.518395:
        return "central"
    if  24.660845< float(location_list[0]) < 49.189787 and -115.236428< float(location_list[1]) <-101.998892:
        return "mountain"
    if  24.660845< float(location_list[0]) < 49.189787 and -125.242264< float(location_list[1]) <-115.236428:
        return "pacific"
    else:
        return "nowhere"

#This is the most important function, it opens the tweets file and if is unable to then it would tell you that the file does not exist.
def compute_tweets(tweets,keylist):
    stacked = []
    eastern = []
    central = []
    mountain = []
    pacific = []
    location = ""
    sentiment = 0
    central_tweets = 0
    eastern_tweets = 0
    pacific_tweets = 0
    mountain_tweets = 0
    eastern_amount = 0
    central_amount=0
    mountain_amount = 0
    pacific_amount = 0
    matched = False
    central_total=[0,0,0]
    eastern_total = [0,0,0]
    pacific_total = [0,0,0]
    mountain_total = [0,0,0]
    try:
        tweetstocheck = open(tweets,"r") #opening the tweets file
        for n in tweetstocheck:
            keylistmass = open(keylist, "r") #opening the keylist
            seperated = n.split(" ")
            a = seperated[5:] #Selecting the parts where it is containing the tweet words.
            location_list = seperated[:2] #Creates a list for the longitude and latitude.
            location = fix_location(location_list) #Determine the location of the tweet and fixing the format of the numbers.

            #This for loop is used to remove all the punctuation that is not a letter or number
            for x in range(len(a)):
                while len(a[x]) != 0:
                    a[x] = a[x].lower()
                    if a[x][0] == a[x][-1] :
                        break
                    if not a[x][0].isalpha() and not a[x][0].isdigit():
                        a[x] = a[x].replace(a[x][0],'')
                        if a[x] == "":
                            break
                    if not a[x][-1].isalpha() and not a[x][-1].isdigit():
                        a[x] = a[x].replace(a[x][-1],'')
                        if a[x] == "":
                            break
                    else:
                        break
            #This for loop is used to determine inside the tweet which word matches inside of the words inside of the keylist
            count = 0
            for y in keylistmass:
                for q in a:
                    seperation = y.split(",")
                    if seperation[0] == q:
                        matched = True
                        count = count + 1
                        sentiment += int(seperation[1])
                        average = sentiment/count
            #Depending on the location and whether a word was matched it would append it the average to the location list
            if location== "nowhere" and matched == True:
                matched = False
                sentiment = 0

            if location == "eastern" and matched == True:
                eastern_tweets += 1
                eastern_amount+=1
                eastern.append(average)
                eastern_total = [sum(eastern)/eastern_amount,eastern_amount, eastern_tweets]
                matched = False
                sentiment = 0
            elif matched == False and location == "eastern":
                eastern_tweets += 1
                eastern_total[2] = eastern_tweets
                sentiment = 0

            if location == "central" and matched == True:
                central_tweets+=1
                central_amount += 1
                central.append(average)
                central_total = [(sum(central) / central_amount),central_amount,central_tweets]
                matched = False
                sentiment = 0
            elif matched == False and location == "central":
                central_tweets+=1
                central_total[2] = central_tweets
                sentiment = 0

            if location == "mountain" and matched == True:
                mountain_amount += 1
                mountain_tweets+=1
                mountain.append(average)
                mountain_total = [(sum(mountain) / mountain_amount), mountain_amount, mountain_tweets]
                matched = False
                sentiment = 0

            elif matched == False and location == "mountain":
                mountain_tweets+=1
                mountain_total[2] = mountain_tweets
                sentiment = 0

            if location == "pacific" and matched == True:
                pacific_amount += 1
                pacific_tweets += 1
                pacific.append(average)
                pacific_total = [(sum(pacific) / pacific_amount), pacific_amount, pacific_tweets]
                matched = False
                sentiment = 0

            elif matched == False and location == "pacific":
                pacific_tweets+=1
                pacific_total[2] = pacific_tweets
                sentiment = 0


        #The next four lines is used to compile all the information together into one list. This is gives the order of [eastern,central,mountain,pacific]
        stacked.append(eastern_total)
        stacked.append(central_total)
        stacked.append(mountain_total)
        stacked.append(pacific_total)
    #Error when opening file
    except IOError:
        return []

    #Returns all the timezone together in one list.
    return stacked



















