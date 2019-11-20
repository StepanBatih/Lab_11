from LawyerManager.models.Lawyer import Lawyer

class Notary(Lawyer):
    def __init__(self,name,experience,rating,lawsuit,notary_district,price_per_case):
        super().__init__(name, experience, rating,lawsuit)
        self.notary_district = notary_district
        self.price_per_case = price_per_case

    def __str__(self):
        return super().__str__() + \
            "\n Notary district: " + str(self.notary_district) + \
            ",\n Price per Case: " + str(self.price_per_case) + " $" 
            