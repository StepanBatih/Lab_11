from LawyerManager.models.Lawyer import Lawyer
from LawyerManager.models.Advocate import Advocate
from LawyerManager.models.Specialization import Specialization
from LawyerManager.models.Lawsuit import Lawsuit
from LawyerManager.models.Notary import Notary 
from LawyerManager.managers.Lawyer_manager import Lawyer_manager
def main():
    
    manager = Lawyer_manager()

    

    advocate = Advocate("Homa",3,2.3,Lawsuit.MAKINGCLAIM,Specialization.MILITARY,50,"Lazar Entertaiment")
    lawyer = Lawyer("Mateush",5, 5.1,Lawsuit.COURTREPRESENTATION)
    notary = Notary("Adam",6,6.7,Lawsuit.EVIDECECOLLECTION,"Lviv",500)
    

    lawyer_list = [advocate,lawyer,notary]

    print("\nSort by name:",*manager.sort_by_name(lawyer_list,False))
    
    print("\nFind by experience bigger than:",*manager.find_by_experience_big_than(lawyer_list,5))

    

if __name__ == "__main__":
    main()