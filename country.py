#
# Assignment #4
# Class Country
# holds information about a single country
#


class Country:
    # constructor, initializes variables
    def __init__(self, name, continent, pop, area):
        self._name = name
        self._pop = pop
        self._area = area
        self._cont = continent

    # getter methods
    def getName(self):
        return self._name

    def getPopulation(self):
        return self._pop

    def getArea(self):
        return self._area

    def getContinent(self):
        return self._cont

    # setter methods
    def setPopulation(self, value):
        self._pop = value

    def setArea(self, value):
        self._area = value

    def setContinent(self, value):
        self._cont = value

    # formats output of country data
    def __repr__(self):
        return self._name + " (pop: " + self._pop + ", size: " + self._area + ") in " + self._cont


