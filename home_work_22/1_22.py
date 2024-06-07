class Hospital: 
    
    def __init__(self,patient_fname,patient_lname) -> None:
        self.patient_fname = patient_fname
        self.patient_lname = patient_lname

    def visit_planing(self,visit_date,dr_name):
        self.visit_date = visit_date
        self.dr_name = dr_name
        x = [self.dr_name,self.visit_date,self.patient_fname,self.patient_lname]
        return x
    
a = Hospital("david","manasyan")


print(a.visit_planing("30/11/2024","house"))



