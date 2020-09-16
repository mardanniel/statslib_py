"""
Created by mardanniel - Statistics Library
"""

class Statistics:
    def __init__(self, vallist):
        """
        Takes a list of values.
        """
        self.vallist = sorted(vallist)
    def show_given_list(self):
        """
        Returns sorted values.
        """
        return self.vallist

    def mean(self):
        """
        Returns average value.
        """
        return sum(self.vallist)/len(self.vallist)

    def median(self):
        """
        Returns the middle value.
        """
        print(self.vallist)
        if len(self.vallist) % 2 == 0:
            return (self.vallist[int((len(self.vallist) / 2) - 1)] + self.vallist[int(len(self.vallist) / 2)]) / 2
        else:
            return self.vallist[int((len(self.vallist) / 2))]

    def mode(self):
        """
        Returns the highest count value.
        """
        occurences = list(set(self.vallist))
        count = []
        print(occurences)
        for i in range(len(occurences)):
            count.append(self.vallist.count(occurences[i]))
        return [occurences[i] for i in range(len(count)) if count[i] == max(count)]

    def variance(self):
        """
        Returns a number of how spread out the values.
        """
        difmean = []
        squareval = []
        for i in range(len(self.vallist)):
            difmean.append(self.vallist[i] - self.mean())
            squareval.append(difmean[i]**2)
        return sum(squareval) / len(self.vallist)

    def standard_dev(self):
        """
        Returns the square root of variance.
        """
        x = self.variance()
        epsilon = 0.01
        left = 0
        right = x
        guess = (right + left) / 2.0
        while abs(guess**2 - x) > epsilon:
            if guess**2 < x:
                left = guess
            else:
                right = guess
            guess = (right+left)/2.0
        return guess

    def percentile(self, percent):
        """
        Returns the percentile from percent given.
        """
        return self.vallist[round((percent/100)*len(self.vallist))-1]

