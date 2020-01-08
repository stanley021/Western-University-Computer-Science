shape = 0
#This is Stanley Chen(251093164) I created this program.
#Here I import the file volume and summarize to use their functions
import Volume
import summarize
#Creating a list for all the volumes for the different kind of shapes
cube_list = []
pyramid_list = []
ellipsoid_list = []
#Here i ask for the specific test number for the sake of summarize.
testnumber = int(input("Enter the test case number: "))
#while loop until shape isn't q or quit
while shape != "quit" or shape != 'q':
    #formatting the input to accept any kind input
    shape = input("What kind of shape do you want?").lower().strip()
    #Ends the program if the user enters quit or q
    if shape == "quit" or shape == 'q':
        #sorting the list from smallest to biggest
        cube_list.sort()
        pyramid_list.sort()
        ellipsoid_list.sort()
        #If all the list are empty then a certain message would show
        if len(cube_list) == 0 and len(pyramid_list) == 0 and len(ellipsoid_list) == 0:
            print("You have reached the end of your session.")
            print("You did not perform and volume calculations")
            break
        #Depending of each list if one of the list is empty then it would print "No shapes entered" if not it will print everything in the list
        print("You have reached the end of your session")
        print("The volumes calculated for each shape are:")
        if len(cube_list) == 0:
            print("Cube: No shapes entered")
        else:
            rounded_cube_list = [round(x, 3) for x in cube_list]
            print("Cube:", end=" ")
            print(*rounded_cube_list, sep= ",")
        if len(pyramid_list) == 0:
            print("Pyramid: No shapes entered")
        else:
            rounded_pyramid_list = [round(x, 3) for x in pyramid_list]
            print("Pyramid:", end=" ")
            print(*rounded_pyramid_list, sep=",")
        if len(ellipsoid_list) == 0:
            print("Ellipsoid: No shapes entered")
        else:
            rounded_ellipsoid_list = [round(x,3) for x in ellipsoid_list]
            print("Ellipsoid:", end=" ")
            print(*rounded_ellipsoid_list, sep=",")
        break
#This part depends on the input of the user for the certain shape and for each shape it will ask for certain measurements and calculate the volume in the volume.py file.
#returning the value of volume to this file then it will append the value to the list.
    elif shape == "cube" or shape == "c":
        cube_list.append(Volume.cube())
    elif shape == "pyramid" or shape == "p":
        pyramid_list.append(Volume.pyramid())
    elif shape == "ellipsoid" or shape == "e":
        ellipsoid_list.append(Volume.ellipsoid())
    else:
        print("Enter a valid shape")

#Using the file given to me on owl to summarize all the values and output a file with the volumes of each list.
summarize.summarize(cube_list,pyramid_list,ellipsoid_list,testnumber)


