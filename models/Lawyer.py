

class Lawyer:

    def __init__(self, name, experience, rating, lawsuit):
        self.name = name
        self.experience = experience
        self.rating = rating
        self.lawsuit = lawsuit
    
    
    
    def __str__(self):
        return "\n\n Name: " + str(self.name) + \
            ",\n Experience: " + str(self.experience) + " years" \
            ",\n Rating: " + str(self.rating) + " Stars"\
            ",\n Law Services: " + str(self.lawsuit) 