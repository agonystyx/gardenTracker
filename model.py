# garden has beds
# beds have a location
# beds have tags
# beds have plant

# garden has plants
# plants have a name
# plants have times
# when started
# when planted
#
# needs...
class Bed:

    """Represents a spot to plant plants"""

    tags = []

    def getTags(self):
        return self.tags

    def addTag(self, tag):
        if not tag in self.tags:
            self.tags.append(tag)


aBed = Bed()
print("tags {}".format( aBed.getTags() ))

aBed.addTag("Backyard")
print("After tags aBed.addTag('Backyard'): {}".format( aBed.getTags() ))


#print("tags {}".format(aBed.getTags())
