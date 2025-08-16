from tkinter import *
import subprocess

class HospitalManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Hospital Management System")
        self.root.geometry("600x400")
        
        Label(self.root, text="HOSPITAL MANAGEMENT SYSTEM", 
              font=("Arial", 20, "bold")).pack(pady=30)
        
        Button(self.root, text="Patient Management", 
               font=("Arial", 14), width=20, height=2,
               command=self.open_patients).pack(pady=10)
        
        Button(self.root, text="Medicinal Stock", 
               font=("Arial", 14), width=20, height=2,
               command=self.open_medicine_stock).pack(pady=10)
        
        Button(self.root, text="Hospital Staff", 
               font=("Arial", 14), width=20, height=2,
               command=self.open_hospital_staff).pack(pady=10)
        
        Button(self.root, text="Exit", 
               font=("Arial", 14), width=20, height=2,
               command=self.root.quit).pack(pady=10)
    
    def open_patients(self):
        subprocess.Popen(["python", "patients.log.py"])
    
    def open_medicine_stock(self):
        subprocess.Popen(["python", "Pharmacy log.py"])
    
    def open_hospital_staff(self):
        subprocess.Popen(["python", "Staff log.py"])


root = Tk()
app = HospitalManagementSystem(root)
root.mainloop()