#
# Assignment #4
# Class Country Catalogue
# Use a file to build the data structures to hold the information about countries.
#


from country import *


class CountryCatalogue:
    def __init__(self, countryFile):
        # initializes list of countries
        self._countryCat = []
        # try exception for opening the country file
        try:
            self._countryFile = open(countryFile, encoding="utf‐8")
        except IOError:
            print("cannot open file")
        # opens country file
        with open(countryFile, encoding="utf‐8") as openedCountryFile:
            x = 0
            # adds every line of countries as a new country with given data
            for line in openedCountryFile:
                # splits line based on bars that separate the data
                lineSplit = line.strip("\n").split("|")
                # does not include the first line of data
                if x != 0:
                    # checks to see if there are the right amount of | (if data is in the correct format)
                    try:
                        Country(lineSplit[0], lineSplit[1], lineSplit[2], lineSplit[3])
                        # adds the country as a new country object into list
                        newCountry = Country(lineSplit[0], lineSplit[1], lineSplit[2], lineSplit[3])
                        self._countryCat.append(newCountry)
                    except IndexError:
                        print("Country " + lineSplit[0] + " is in the wrong format in the original data file.")

                x+=1

    # setter methods
    def setPopulationOfCountry(self, country, pop):
        for x in self._countryCat:
            if country == x.getName():
                self._countryCat[self._countryCat.index(x)].setPopulation(pop)
        return

    def setAreaOfCountry(self, country, area):
        for x in self._countryCat:
            if country == x.getName():
                self._countryCat[self._countryCat.index(x)].setArea(area)
        return

    def setContinentOfCountry(self, country, cont):
        for x in self._countryCat:
            if country == x.getName():
                self._countryCat[self._countryCat.index(x)].setContinent(cont)
        return

    # finds if country already exists in the country catalogue
    def findCountry(self, country):
        for x in self._countryCat:
            if country.getName() == x.getName():
                return country
        return None

    # adds country to country catalogue if it doesn't already exist
    def addCountry(self, countryName, cont, pop, area):
        countryObj = Country(countryName, 0, 0, 0)
        if self.findCountry(countryObj) == countryName:
            return False
        newCountry = Country(countryName, cont, pop, area)
        self._countryCat.append(newCountry)
        ## DOESNT ADD THE POPULATION OF ITALLY?? DATA 2
        return True

    # prints the list in an orderly manner
    def printCountryCatalogue(self):
        for country in self._countryCat:
            print(country.__repr__())

    # saves the country catalogue list as a new file called output.txt
    def saveCountryCatalogue(self, fname):
        file = open(fname ,"w+")
        self._countryCat = sorted(self._countryCat, key=lambda c: c.getName())
        file.write("Country|Continent|Population|Area\n")
        for x in self._countryCat:
            file.write(str(x.getName()) + "|"+ str(x.getContinent()) + "|" + str(x.getPopulation()) + "|" + str(x.getArea()) + "\n")


