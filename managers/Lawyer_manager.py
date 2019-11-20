class Lawyer_manager:

    def __init__(self,lawyer_list=()):
        self.lawyer_list = lawyer_list
    
    def sort_by_name (self,lawyer_list, revers ):
        return sorted(lawyer_list,key=lambda lawyer: lawyer.name , reverse = revers)
    
    def find_by_experience_big_than (self,lawyer_list,experience):
        return list(filter(lambda lawyer: lawyer.experience >= experience, lawyer_list))
    