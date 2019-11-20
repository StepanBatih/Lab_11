from LawyerManager.models.Lawyer import Lawyer

class Advocate(Lawyer):
    def __init__(self,name,experience,rating,lawsuit,specialization,price_per_hour,company_name):
        super().__init__(name, experience, rating,lawsuit)
        self.specialization = specialization
        self.price_per_hour = price_per_hour
        self.company_name = company_name
    
    def __str__(self):
        return super().__str__() + \
            "\n Specialization: " + str(self.specialization) + \
            ",\n Price per Hour: " + str(self.price_per_hour) + " $" \
            ",\n Company name: " + str(self.company_name)