#
# Assignment #4
# python module processUpdates
# Function that takes two files as parameters: original file and update file, and uses update file to update original country file
#


from catalogue import*
from country import*

def fileExists(fileName, fileType):
    fileWorks = False
    # continues checking if file works
    while not fileWorks:
        try:
            open(fileName, encoding="utf‐8")
            fileWorks = True
        # if the file does not exist, asks the user if they want to input new file or quit program
        except IOError:
            print("cannot open " + fileType)
            quit = input("Do you want to quit? 'Y' for yes and 'N' for no: ")
            # continues asking user for Yes or No until they give a valid answer
            while quit != "Y" and quit != "N":
                quit = input("Invalid input. Do you want to quit? 'Y' for yes and 'N' for no: ")
            # if user chooses to quit, writes update unsuccessful in an output.txt file
            if quit == "Y":
                quitFile = open("output.txt" ,"w+")
                quitFile.write("Update Unsuccessful\n")
                return False
            # if user does not want to quit, asks the user for file name again
            if quit == "N":
                fileName = input("What is the new " + fileType + "? ")
    return fileName


# processes the updates given an original file, and a new update file
def processUpdates(cntryFileName, updateFileName):
    # ensures both files exist using the file exists method before continuing
    cntryFileName = fileExists(cntryFileName, "country file")
    if cntryFileName == False:
        return False
    updateFileName = fileExists(updateFileName, "update file")
    if updateFileName == False:
        return False
    # adds existing file to country catalogue
    newCat = CountryCatalogue(cntryFileName)
    # opens update file and goes through every line
    with open(updateFileName, encoding="utf‐8") as file:
        for line in file:
            # only adds the country if there are ';' in the line to separate data
            if ";" in line:
                country = ""
                # splits the line and only continues if there are less than 4 data pieces
                lineSplit = line.strip("\n").strip(" ").split(";")
                if not len(lineSplit)>4:
                    area = ""
                    population = ""
                    cont = ""
                    counter = 0
                    # processes data for every line and adds corresponding data piece to the correct variable
                    for x in lineSplit:
                        x = x.strip(" ")
                        if counter == 0:
                            country = x
                        elif x[0] == "P":
                            population = x.strip("P=").strip("\n")
                            # checks to make sure that population is all numbers
                            if not population.replace(",", "").replace(" ", "").isnumeric():
                                # if not all numbers, tells the user that the format of population information is wrong and does not update population
                                print("Incorrect format for population of " + country)
                                population = ""
                        elif x[0] == "A":
                            area = x.strip("A=").strip("\n")
                            # checks to make sure area is all numbers
                            if not area.replace(",", "").replace(" ", "").isnumeric():
                                print("Incorrect format for area of " + country)
                                area = ""
                        elif x[0] == "C":
                            cont = x.strip("C=").strip("\n")
                            # checks to make sure continent is all letters
                            if not cont.replace(",", "").replace(" ", "").isalpha():
                                print("Incorrect format for continent of " + country)
                                cont = ""
                        counter += 1
                    # if the country does not already exist, adds it to the catalogue
                    countryObj = Country(country, 0, 0, 0)
                    if newCat.findCountry(countryObj) is None:
                        newCat.addCountry(country, cont, population, area)
                    # if country does exist in the catalogue already, changes the data with the new updated data
                    if newCat.findCountry(countryObj) is not None:
                        if area != "":
                            newCat.setAreaOfCountry(country, area)
                        if cont != "":
                            newCat.setContinentOfCountry(country, cont)
                        if population != "":
                            newCat.setPopulationOfCountry(country, population)
    # saves country catalogue in output.txt file and returns true
    newCat.saveCountryCatalogue("output.txt")
    return True
