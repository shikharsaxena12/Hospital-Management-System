from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import mysql.connector
from importlib import import_module

# Import the actual module classes
try:
    from Patients import Patients as PatientsModule
except:
    PatientsModule = None

try:
    pharmacy_module = import_module('Pharmacy log')
    MedicinalStockModule = pharmacy_module.MedicinalStock
except:
    MedicinalStockModule = None

try:
    staff_module = import_module('Staff log')
    HospitalStaffModule = staff_module.HospitalStaff
except:
    HospitalStaffModule = None

class HospitalManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Hospital Management System")
        self.root.geometry("1540x800+0+0")
        self.root.state('zoomed')
        
        # Create main container
        self.main_frame = Frame(self.root)
        self.main_frame.pack(fill=BOTH, expand=True)
        
        # Show main menu initially
        self.show_main_menu()
    
    def clear_frame(self):
        for widget in self.main_frame.winfo_children():
            widget.destroy()
    
    def show_main_menu(self):
        self.clear_frame()
        
        Label(self.main_frame, text="HOSPITAL MANAGEMENT SYSTEM", 
              font=("Arial", 20, "bold")).pack(pady=30)
        
        Button(self.main_frame, text="Patient Management", 
               font=("Arial", 14), width=20, height=2,
               command=self.open_patients).pack(pady=10)
        
        Button(self.main_frame, text="Medicinal Stock", 
               font=("Arial", 14), width=20, height=2,
               command=self.open_medicine_stock).pack(pady=10)
        
        Button(self.main_frame, text="Hospital Staff", 
               font=("Arial", 14), width=20, height=2,
               command=self.open_hospital_staff).pack(pady=10)
        
        Button(self.main_frame, text="Exit", 
               font=("Arial", 14), width=20, height=2,
               command=self.root.quit).pack(pady=10)
    
    def open_patients(self):
        self.clear_frame()
        if PatientsModule:
            PatientsModule(self.main_frame, self)
        else:
            Patients(self.main_frame, self)
    
    def open_medicine_stock(self):
        self.clear_frame()
        if MedicinalStockModule:
            MedicinalStockModule(self.main_frame, self)
        else:
            MedicinalStock(self.main_frame, self)
    
    def open_hospital_staff(self):
        self.clear_frame()
        if HospitalStaffModule:
            HospitalStaffModule(self.main_frame, self)
        else:
            HospitalStaff(self.main_frame, self)

class Patients:
    def __init__(self, parent, main_app):
        self.parent = parent
        self.main_app = main_app
        
        # Create StringVar objects
        self.PatientId=StringVar()
        self.PatientName=StringVar()
        self.Age=StringVar()
        self.Gender=StringVar()
        self.Phone=StringVar()
        self.Email=StringVar()
        self.Address=StringVar()
        self.BloodType=StringVar()
        self.Height=StringVar()
        self.Weight=StringVar()
        self.EmergencyContact=StringVar()
        self.Insurance=StringVar()
        self.Allergies=StringVar()
        self.Diagnosis=StringVar()
        self.DoctorName=StringVar()
        self.Department=StringVar()
        self.AppointmentDate=StringVar()
        self.Medicine=StringVar()
        self.Dose=StringVar()
        self.Frequency=StringVar()
        self.Duration=StringVar()

        # Create back button
        Button(self.parent, text="← Back to Main Menu", 
               font=("Arial", 12, "bold"), bg="blue", fg="white",
               command=self.main_app.show_main_menu).pack(anchor="nw", padx=10, pady=5)

        # Create main title
        Label(self.parent, bd=20, relief=RIDGE, text="PATIENT MANAGEMENT SYSTEM", 
              font=("times new roman", 50, "bold"), fg="red", bg="white").pack(side=TOP, fill=X)

        # Create frames
        dataframe=Frame(self.parent, bd=20, relief=RIDGE)
        dataframe.place(x=0, y=130, width=1530, height=430)

        leftframe = LabelFrame(dataframe, text="Patient Information", 
                              font=("times new roman", 12, "bold"), bd=10, relief=RIDGE, padx=10)
        leftframe.place(x=0, y=5, width=980, height=380)

        rightframe = LabelFrame(dataframe, text="Patient Records", 
                               font=("times new roman", 12, "bold"), bd=10, relief=RIDGE, padx=10)
        rightframe.place(x=990, y=5, width=460, height=350)

        buttonframe=Frame(self.parent, bd=20, relief=RIDGE)
        buttonframe.place(x=0, y=560, width=1530, height=70)

        detailframe=Frame(self.parent, bd=20, relief=RIDGE)
        detailframe.place(x=0, y=630, width=1530, height=160)

        # Create form fields
        Label(leftframe, text="Patient ID:", font=("arial", 12, "bold"), padx=2, pady=6).grid(row=0, column=0, sticky="w")
        Entry(leftframe, textvariable=self.PatientId, font=("arial", 11, "bold"), width=28).grid(row=0, column=1)
        
        Label(leftframe,text="Patient Name:",font=("arial", 12, "bold"),padx=2,pady=6).grid(row=1,column=0, sticky="w")
        Entry(leftframe,textvariable=self.PatientName,font=("arial", 11, "bold"),width=28).grid(row=1,column=1)
        
        Label(leftframe,text="Age:",font=("arial", 12, "bold"),padx=2,pady=6).grid(row=2,column=0, sticky="w")
        Entry(leftframe,textvariable=self.Age,font=("arial", 11, "bold"),width=28).grid(row=2,column=1)

        Label(leftframe,text="Gender:",font=("arial", 12, "bold"),padx=2,pady=6).grid(row=3,column=0, sticky="w")
        cmbGender=ttk.Combobox(leftframe, textvariable=self.Gender, font=("arial", 11, "bold"), width=25, state="readonly")
        cmbGender["values"]=("Male","Female","Other")
        cmbGender.grid(row=3,column=1)
        
        Label(leftframe,text="Phone:",font=("arial", 12, "bold"),padx=2,pady=6).grid(row=4,column=0, sticky="w")
        Entry(leftframe,textvariable=self.Phone,font=("arial", 11, "bold"),width=28).grid(row=4,column=1)
        
        Label(leftframe,text="Email:",font=("arial", 12, "bold"),padx=2,pady=6).grid(row=5,column=0, sticky="w")
        Entry(leftframe,textvariable=self.Email,font=("arial", 11, "bold"),width=28).grid(row=5,column=1)
        
        Label(leftframe,text="Address:",font=("arial", 12, "bold"),padx=2,pady=6).grid(row=6,column=0, sticky="w")
        Entry(leftframe,textvariable=self.Address,font=("arial", 11, "bold"),width=28).grid(row=6,column=1)
        
        Label(leftframe,text="Blood Type:",font=("arial", 12, "bold"),padx=2,pady=6).grid(row=7,column=0, sticky="w")
        cmbBloodType=ttk.Combobox(leftframe,textvariable=self.BloodType,font=("arial", 11, "bold"),width=25,state="readonly")
        cmbBloodType["values"]=("A+","A-","B+","B-","AB+","AB-","O+","O-")
        cmbBloodType.grid(row=7,column=1)
        
        Label(leftframe,text="Height (cm):",font=("arial", 12, "bold"),padx=2,pady=6).grid(row=8,column=0, sticky="w")
        Entry(leftframe,textvariable=self.Height,font=("arial", 11, "bold"),width=28).grid(row=8,column=1)
        
        Label(leftframe,text="Weight (kg):",font=("arial", 12, "bold"),padx=2,pady=6).grid(row=9,column=0, sticky="w")
        Entry(leftframe,textvariable=self.Weight,font=("arial", 11, "bold"),width=28).grid(row=9,column=1)

        Label(leftframe,text="Doctor Name:",font=("arial", 12, "bold"),padx=2,pady=6).grid(row=0,column=2, sticky="w")
        Entry(leftframe,textvariable=self.DoctorName,font=("arial", 11, "bold"),width=28).grid(row=0,column=3)
        
        Label(leftframe,text="Department:",font=("arial", 12, "bold"),padx=2,pady=6).grid(row=1,column=2, sticky="w")
        cmbDepartment=ttk.Combobox(leftframe,textvariable=self.Department,font=("arial", 11, "bold"),width=25,state="readonly")
        cmbDepartment["values"]=("Cardiology","Neurology","Orthopedics","Pediatrics","General Medicine","Surgery")
        cmbDepartment.grid(row=1,column=3)

        Label(leftframe,text="Appointment Date:",font=("arial", 12, "bold"),padx=2,pady=6).grid(row=2,column=2, sticky="w")
        Entry(leftframe,textvariable=self.AppointmentDate,font=("arial", 11, "bold"),width=28).grid(row=2,column=3)
        
        Label(leftframe,text="Medicine:",font=("arial", 12, "bold"),padx=2,pady=6).grid(row=3,column=2, sticky="w")
        Entry(leftframe,textvariable=self.Medicine,font=("arial", 11, "bold"),width=28).grid(row=3,column=3)
        
        Label(leftframe,text="Dose:",font=("arial", 12, "bold"),padx=2,pady=6).grid(row=4,column=2, sticky="w")
        Entry(leftframe,textvariable=self.Dose,font=("arial", 11, "bold"),width=28).grid(row=4,column=3)
        
        Label(leftframe,text="Emergency Contact:",font=("arial", 12, "bold"),padx=2,pady=6).grid(row=5,column=2, sticky="w")
        Entry(leftframe,textvariable=self.EmergencyContact,font=("arial", 11, "bold"),width=28).grid(row=5,column=3)
        
        Label(leftframe,text="Insurance:",font=("arial", 12, "bold"),padx=2,pady=6).grid(row=6,column=2, sticky="w")
        Entry(leftframe,textvariable=self.Insurance,font=("arial", 11, "bold"),width=28).grid(row=6,column=3)
        
        Label(leftframe,text="Allergies:",font=("arial", 12, "bold"),padx=2,pady=6).grid(row=7,column=2, sticky="w")
        Entry(leftframe,textvariable=self.Allergies,font=("arial", 11, "bold"),width=28).grid(row=7,column=3)
        
        Label(leftframe,text="Diagnosis:",font=("arial", 12, "bold"),padx=2,pady=6).grid(row=8,column=2, sticky="w")
        Entry(leftframe,textvariable=self.Diagnosis,font=("arial", 11, "bold"),width=28).grid(row=8,column=3)
        
        Label(leftframe,text="Duration:",font=("arial", 12, "bold"),padx=2,pady=6).grid(row=9,column=2, sticky="w")
        Entry(leftframe,textvariable=self.Duration,font=("arial", 11, "bold"),width=28).grid(row=9,column=3)

        self.txtprescription = Text(rightframe, font=("arial", 12, "bold"), width=46, height=16, padx=2, pady=6)
        self.txtprescription.grid(row=0, column=0)

        for i in range(6):
            buttonframe.columnconfigure(i, weight=1)
        
        Button(buttonframe, text="Patient Record", font=("arial", 12, "bold"), height=1, bg="Green", fg="white").grid(row=0, column=0, sticky='ew')
        Button(buttonframe, text="Save Patient Data", font=("arial", 12, "bold"), height=1, bg="Green", fg="white", command=self.save_data).grid(row=0, column=1, sticky='ew')
        Button(buttonframe, text="Update", font=("arial", 12, "bold"), height=1, bg="Green", fg="white").grid(row=0, column=2, sticky='ew')
        Button(buttonframe, text="Delete", font=("arial", 12, "bold"), height=1, bg="Green", fg="white").grid(row=0, column=3, sticky='ew')
        Button(buttonframe, text="Clear", font=("arial", 12, "bold"), height=1, bg="Green", fg="white", command=self.clear_fields).grid(row=0, column=4, sticky='ew')
        Button(buttonframe, text="Exit", font=("arial", 12, "bold"), height=1, bg="Green", fg="white", command=self.main_app.show_main_menu).grid(row=0, column=5, sticky='ew')

        scroll_x=ttk.Scrollbar(detailframe, orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(detailframe, orient=VERTICAL)
        
        self.patient_table = ttk.Treeview(
            detailframe,
            columns=("Patient ID", "Patient Name", "Age", "Gender", "Phone", "Email", 
                    "Address", "Blood Type", "Height", "Weight", "Emergency Contact", "Insurance", "Allergies",
                    "Diagnosis", "Doctor Name", "Department", "Appointment Date", 
                    "Medicine", "Dose", "Frequency", "Duration"),
            show="headings",
            xscrollcommand=scroll_x.set,
            yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        
        scroll_x.config(command=self.patient_table.xview)
        scroll_y.config(command=self.patient_table.yview)
        
        for col in ("Patient ID", "Patient Name", "Age", "Gender", "Phone", "Email", 
                   "Address", "Blood Type", "Height", "Weight", "Emergency Contact", "Insurance", "Allergies",
                   "Diagnosis", "Doctor Name", "Department", "Appointment Date", 
                   "Medicine", "Dose", "Frequency", "Duration"):
            self.patient_table.heading(col, text=col)
            self.patient_table.column(col, width=100)
        
        self.patient_table.pack(fill=BOTH, expand=1)

    def save_data(self):
        if not all([self.PatientId.get(), self.PatientName.get(), self.Medicine.get(), self.Dose.get()]):
            messagebox.showerror("Error", "All required fields must be filled")
            return

        conn = None
        try:
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="patientData")
            
            cursor = conn.cursor()
            
            cursor.execute("INSERT INTO patients VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (
                self.PatientId.get(), self.PatientName.get(), self.Age.get(), self.Gender.get(),
                self.Phone.get(), self.Email.get(), self.Address.get(), self.BloodType.get(),
                self.Height.get(), self.Weight.get(), self.EmergencyContact.get(), self.Insurance.get(),
                self.Allergies.get(), self.Diagnosis.get(), self.DoctorName.get(), self.Department.get(),
                self.AppointmentDate.get(), self.Medicine.get(), self.Dose.get(), self.Frequency.get(),
                self.Duration.get()))
            
            conn.commit()
            messagebox.showinfo("Success", "Patient record saved successfully")
        
        except mysql.connector.Error:
            messagebox.showerror("Error", "Database operation failed")
        
        finally:
            if conn and conn.is_connected():
                conn.close()

    def clear_fields(self):
        for var in [self.PatientId, self.PatientName, self.Age, self.Gender, 
                   self.Phone, self.Email, self.Address, self.BloodType, self.Height, self.Weight,
                   self.EmergencyContact, self.Insurance, self.Allergies, self.Diagnosis, self.DoctorName, 
                   self.Department, self.AppointmentDate, self.Medicine, 
                   self.Dose, self.Frequency, self.Duration]:
            var.set("")
        
        self.txtprescription.delete(1.0, END)

class MedicinalStock:
    def __init__(self, parent, main_app):
        self.parent = parent
        self.main_app = main_app
        self.initialize_variables()
        self.create_main_interface()
    
    def initialize_variables(self):
        self.MedicineId = StringVar()
        self.MedicineName = StringVar()
        self.Category = StringVar()
        self.Manufacturer = StringVar()
        self.BatchNo = StringVar()
        self.ExpiryDate = StringVar()
        self.Quantity = StringVar()
        self.Unit = StringVar()
        self.CostPrice = StringVar()
        self.SellingPrice = StringVar()
        self.Supplier = StringVar()
        self.Location = StringVar()
        self.StorageCondition = StringVar()
    
    def create_main_interface(self):
        Button(self.parent, text="← Back to Main Menu", font=("Arial", 12, "bold"), bg="blue", fg="white", command=self.main_app.show_main_menu).pack(anchor="nw", padx=10, pady=5)
        
        Label(self.parent, bd=20, relief=RIDGE, text="MEDICINAL STOCK MANAGEMENT SYSTEM", font=("times new roman", 50, "bold"), fg="red", bg="white").pack(side=TOP, fill=X)
        
        dataframe = Frame(self.parent, bd=20, relief=RIDGE)
        dataframe.place(x=0, y=130, width=1530, height=430)
        
        leftframe = LabelFrame(dataframe, text="Medicine Information", font=("times new roman", 12, "bold"), bd=10, relief=RIDGE, padx=10)
        leftframe.place(x=0, y=5, width=980, height=380)
        
        rightframe = LabelFrame(dataframe, text="Medicine Records", font=("times new roman", 12, "bold"), bd=10, relief=RIDGE, padx=10)
        rightframe.place(x=990, y=5, width=460, height=350)
        
        buttonframe = Frame(self.parent, bd=20, relief=RIDGE)
        buttonframe.place(x=0, y=560, width=1530, height=70)
        
        detailframe = Frame(self.parent, bd=20, relief=RIDGE)
        detailframe.place(x=0, y=630, width=1530, height=160)
        
        Label(leftframe, text="Medicine ID:", font=("arial", 12, "bold"), padx=2, pady=6).grid(row=0, column=0, sticky="w")
        Entry(leftframe, textvariable=self.MedicineId, font=("arial", 11, "bold"), width=28).grid(row=0, column=1)
        
        Label(leftframe, text="Medicine Name:", font=("arial", 12, "bold"), padx=2, pady=6).grid(row=1, column=0, sticky="w")
        Entry(leftframe, textvariable=self.MedicineName, font=("arial", 11, "bold"), width=28).grid(row=1, column=1)
        
        Label(leftframe, text="Category:", font=("arial", 12, "bold"), padx=2, pady=6).grid(row=2, column=0, sticky="w")
        cmbCategory = ttk.Combobox(leftframe, textvariable=self.Category, font=("arial", 11, "bold"), width=25, state="readonly")
        cmbCategory["values"] = ("Tablet", "Capsule", "Syrup", "Injection", "Ointment", "Drops", "Inhaler", "Other")
        cmbCategory.grid(row=2, column=1)
        
        Label(leftframe, text="Manufacturer:", font=("arial", 12, "bold"), padx=2, pady=6).grid(row=3, column=0, sticky="w")
        Entry(leftframe, textvariable=self.Manufacturer, font=("arial", 11, "bold"), width=28).grid(row=3, column=1)
        
        Label(leftframe, text="Batch No:", font=("arial", 12, "bold"), padx=2, pady=6).grid(row=4, column=0, sticky="w")
        Entry(leftframe, textvariable=self.BatchNo, font=("arial", 11, "bold"), width=28).grid(row=4, column=1)
        
        Label(leftframe, text="Expiry Date:", font=("arial", 12, "bold"), padx=2, pady=6).grid(row=5, column=0, sticky="w")
        Entry(leftframe, textvariable=self.ExpiryDate, font=("arial", 11, "bold"), width=28).grid(row=5, column=1)
        
        Label(leftframe, text="Quantity:", font=("arial", 12, "bold"), padx=2, pady=6).grid(row=6, column=0, sticky="w")
        Entry(leftframe, textvariable=self.Quantity, font=("arial", 11, "bold"), width=28).grid(row=6, column=1)
        
        Label(leftframe, text="Unit:", font=("arial", 12, "bold"), padx=2, pady=6).grid(row=7, column=0, sticky="w")
        cmbUnit = ttk.Combobox(leftframe, textvariable=self.Unit, font=("arial", 11, "bold"), width=25, state="readonly")
        cmbUnit["values"] = ("Pieces", "Bottles", "Boxes", "Strips", "Vials", "Tubes", "Packets")
        cmbUnit.grid(row=7, column=1)
        
        Label(leftframe, text="Cost Price:", font=("arial", 12, "bold"), padx=2, pady=6).grid(row=0, column=2, sticky="w")
        Entry(leftframe, textvariable=self.CostPrice, font=("arial", 11, "bold"), width=28).grid(row=0, column=3)
        
        Label(leftframe, text="Selling Price:", font=("arial", 12, "bold"), padx=2, pady=6).grid(row=1, column=2, sticky="w")
        Entry(leftframe, textvariable=self.SellingPrice, font=("arial", 11, "bold"), width=28).grid(row=1, column=3)
        
        Label(leftframe, text="Supplier:", font=("arial", 12, "bold"), padx=2, pady=6).grid(row=2, column=2, sticky="w")
        Entry(leftframe, textvariable=self.Supplier, font=("arial", 11, "bold"), width=28).grid(row=2, column=3)
        
        Label(leftframe, text="Location:", font=("arial", 12, "bold"), padx=2, pady=6).grid(row=3, column=2, sticky="w")
        Entry(leftframe, textvariable=self.Location, font=("arial", 11, "bold"), width=28).grid(row=3, column=3)
        
        Label(leftframe, text="Storage Condition:", font=("arial", 12, "bold"), padx=2, pady=6).grid(row=4, column=2, sticky="w")
        cmbStorage = ttk.Combobox(leftframe, textvariable=self.StorageCondition, font=("arial", 11, "bold"), width=25, state="readonly")
        cmbStorage["values"] = ("Room Temperature", "Refrigerated", "Frozen", "Cool & Dry", "Special Storage")
        cmbStorage.grid(row=4, column=3)
        
        self.txtmedicine = Text(rightframe, font=("arial", 12, "bold"), width=46, height=16, padx=2, pady=6)
        self.txtmedicine.grid(row=0, column=0)
        
        for i in range(6):
            buttonframe.columnconfigure(i, weight=1)
        
        Button(buttonframe, text="Medicine Record", font=("arial", 12, "bold"), height=1, bg="Green", fg="white").grid(row=0, column=0, sticky='ew')
        Button(buttonframe, text="Save Medicine Data", font=("arial", 12, "bold"), height=1, bg="Green", fg="white", command=self.save_data).grid(row=0, column=1, sticky='ew')
        Button(buttonframe, text="Update", font=("arial", 12, "bold"), height=1, bg="Green", fg="white").grid(row=0, column=2, sticky='ew')
        Button(buttonframe, text="Delete", font=("arial", 12, "bold"), height=1, bg="Green", fg="white").grid(row=0, column=3, sticky='ew')
        Button(buttonframe, text="Clear", font=("arial", 12, "bold"), height=1, bg="Green", fg="white", command=self.clear_fields).grid(row=0, column=4, sticky='ew')
        Button(buttonframe, text="Exit", font=("arial", 12, "bold"), height=1, bg="Green", fg="white", command=self.main_app.show_main_menu).grid(row=0, column=5, sticky='ew')
        
        scroll_x = ttk.Scrollbar(detailframe, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(detailframe, orient=VERTICAL)
        
        self.medicine_table = ttk.Treeview(detailframe, columns=("Medicine ID", "Medicine Name", "Category", "Manufacturer", "Batch No", "Expiry Date", "Quantity", "Unit", "Cost Price", "Selling Price", "Supplier", "Location", "Storage Condition"), show="headings", xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.medicine_table.xview)
        scroll_y.config(command=self.medicine_table.yview)
        
        for col in ("Medicine ID", "Medicine Name", "Category", "Manufacturer", "Batch No", "Expiry Date", "Quantity", "Unit", "Cost Price", "Selling Price", "Supplier", "Location", "Storage Condition"):
            self.medicine_table.heading(col, text=col)
            self.medicine_table.column(col, width=100)
        
        self.medicine_table.pack(fill=BOTH, expand=1)
    
    def save_data(self):
        if not all([self.MedicineId.get(), self.MedicineName.get(), self.Quantity.get(), self.ExpiryDate.get()]):
            messagebox.showerror("Error", "All required fields must be filled")
            return
        messagebox.showinfo("Success", "Medicine record saved successfully")
    
    def clear_fields(self):
        for var in [self.MedicineId, self.MedicineName, self.Category, self.Manufacturer, self.BatchNo, self.ExpiryDate, self.Quantity, self.Unit, self.CostPrice, self.SellingPrice, self.Supplier, self.Location, self.StorageCondition]:
            var.set("")
        self.txtmedicine.delete(1.0, END)

class HospitalStaff:
    def __init__(self, parent, main_app):
        self.parent = parent
        self.main_app = main_app
        self.initialize_variables()
        self.create_main_interface()
    
    def initialize_variables(self):
        self.StaffId = StringVar()
        self.StaffName = StringVar()
        self.Department = StringVar()
        self.Position = StringVar()
        self.EmployeeId = StringVar()
        self.ContactNumber = StringVar()
        self.Email = StringVar()
        self.JoiningDate = StringVar()
        self.ShiftTiming = StringVar()
        self.Salary = StringVar()
        self.EmploymentStatus = StringVar()
        self.EmergencyContact = StringVar()
        self.Qualification = StringVar()
    
    def create_main_interface(self):
        Button(self.parent, text="← Back to Main Menu", font=("Arial", 12, "bold"), bg="blue", fg="white", command=self.main_app.show_main_menu).pack(anchor="nw", padx=10, pady=5)
        
        Label(self.parent, bd=20, relief=RIDGE, text="HOSPITAL STAFF MANAGEMENT SYSTEM", font=("times new roman", 50, "bold"), fg="red", bg="white").pack(side=TOP, fill=X)
        
        dataframe = Frame(self.parent, bd=20, relief=RIDGE)
        dataframe.place(x=0, y=130, width=1530, height=430)
        
        leftframe = LabelFrame(dataframe, text="Staff Information", font=("times new roman", 12, "bold"), bd=10, relief=RIDGE, padx=10)
        leftframe.place(x=0, y=5, width=980, height=380)
        
        rightframe = LabelFrame(dataframe, text="Staff Records", font=("times new roman", 12, "bold"), bd=10, relief=RIDGE, padx=10)
        rightframe.place(x=990, y=5, width=460, height=350)
        
        buttonframe = Frame(self.parent, bd=20, relief=RIDGE)
        buttonframe.place(x=0, y=560, width=1530, height=70)
        
        detailframe = Frame(self.parent, bd=20, relief=RIDGE)
        detailframe.place(x=0, y=630, width=1530, height=160)
        
        Label(leftframe, text="Staff ID:", font=("arial", 12, "bold"), padx=2, pady=6).grid(row=0, column=0, sticky="w")
        Entry(leftframe, textvariable=self.StaffId, font=("arial", 11, "bold"), width=28).grid(row=0, column=1)
        
        Label(leftframe, text="Staff Name:", font=("arial", 12, "bold"), padx=2, pady=6).grid(row=1, column=0, sticky="w")
        Entry(leftframe, textvariable=self.StaffName, font=("arial", 11, "bold"), width=28).grid(row=1, column=1)
        
        Label(leftframe, text="Department:", font=("arial", 12, "bold"), padx=2, pady=6).grid(row=2, column=0, sticky="w")
        cmbDepartment = ttk.Combobox(leftframe, textvariable=self.Department, font=("arial", 11, "bold"), width=25, state="readonly")
        cmbDepartment["values"] = ("Emergency", "Cardiology", "Neurology", "Orthopedics", "Pediatrics", "Radiology", "Laboratory", "Pharmacy", "Administration", "Nursing", "Surgery", "ICU")
        cmbDepartment.grid(row=2, column=1)
        
        Label(leftframe, text="Position:", font=("arial", 12, "bold"), padx=2, pady=6).grid(row=3, column=0, sticky="w")
        cmbPosition = ttk.Combobox(leftframe, textvariable=self.Position, font=("arial", 11, "bold"), width=25, state="readonly")
        cmbPosition["values"] = ("Doctor", "Nurse", "Technician", "Administrator", "Pharmacist", "Receptionist", "Security", "Cleaner", "Manager", "Supervisor")
        cmbPosition.grid(row=3, column=1)
        
        Label(leftframe, text="Employee ID:", font=("arial", 12, "bold"), padx=2, pady=6).grid(row=4, column=0, sticky="w")
        Entry(leftframe, textvariable=self.EmployeeId, font=("arial", 11, "bold"), width=28).grid(row=4, column=1)
        
        Label(leftframe, text="Contact Number:", font=("arial", 12, "bold"), padx=2, pady=6).grid(row=5, column=0, sticky="w")
        Entry(leftframe, textvariable=self.ContactNumber, font=("arial", 11, "bold"), width=28).grid(row=5, column=1)
        
        Label(leftframe, text="Email:", font=("arial", 12, "bold"), padx=2, pady=6).grid(row=6, column=0, sticky="w")
        Entry(leftframe, textvariable=self.Email, font=("arial", 11, "bold"), width=28).grid(row=6, column=1)
        
        Label(leftframe, text="Joining Date:", font=("arial", 12, "bold"), padx=2, pady=6).grid(row=0, column=2, sticky="w")
        Entry(leftframe, textvariable=self.JoiningDate, font=("arial", 11, "bold"), width=28).grid(row=0, column=3)
        
        Label(leftframe, text="Shift Timing:", font=("arial", 12, "bold"), padx=2, pady=6).grid(row=1, column=2, sticky="w")
        cmbShift = ttk.Combobox(leftframe, textvariable=self.ShiftTiming, font=("arial", 11, "bold"), width=25, state="readonly")
        cmbShift["values"] = ("Morning (6AM-2PM)", "Evening (2PM-10PM)", "Night (10PM-6AM)", "Rotating")
        cmbShift.grid(row=1, column=3)
        
        Label(leftframe, text="Salary:", font=("arial", 12, "bold"), padx=2, pady=6).grid(row=2, column=2, sticky="w")
        Entry(leftframe, textvariable=self.Salary, font=("arial", 11, "bold"), width=28).grid(row=2, column=3)
        
        Label(leftframe, text="Employment Status:", font=("arial", 12, "bold"), padx=2, pady=6).grid(row=3, column=2, sticky="w")
        cmbEmploymentStatus = ttk.Combobox(leftframe, textvariable=self.EmploymentStatus, font=("arial", 11, "bold"), width=25, state="readonly")
        cmbEmploymentStatus["values"] = ("Active", "On Leave", "Suspended", "Terminated")
        cmbEmploymentStatus.grid(row=3, column=3)
        
        Label(leftframe, text="Emergency Contact:", font=("arial", 12, "bold"), padx=2, pady=6).grid(row=4, column=2, sticky="w")
        Entry(leftframe, textvariable=self.EmergencyContact, font=("arial", 11, "bold"), width=28).grid(row=4, column=3)
        
        Label(leftframe, text="Qualification:", font=("arial", 12, "bold"), padx=2, pady=6).grid(row=5, column=2, sticky="w")
        Entry(leftframe, textvariable=self.Qualification, font=("arial", 11, "bold"), width=28).grid(row=5, column=3)
        
        self.txtstaff = Text(rightframe, font=("arial", 12, "bold"), width=46, height=16, padx=2, pady=6)
        self.txtstaff.grid(row=0, column=0)
        
        for i in range(6):
            buttonframe.columnconfigure(i, weight=1)
        
        Button(buttonframe, text="Staff Record", font=("arial", 12, "bold"), height=1, bg="Green", fg="white").grid(row=0, column=0, sticky='ew')
        Button(buttonframe, text="Save Staff Data", font=("arial", 12, "bold"), height=1, bg="Green", fg="white", command=self.save_data).grid(row=0, column=1, sticky='ew')
        Button(buttonframe, text="Update", font=("arial", 12, "bold"), height=1, bg="Green", fg="white").grid(row=0, column=2, sticky='ew')
        Button(buttonframe, text="Delete", font=("arial", 12, "bold"), height=1, bg="Green", fg="white").grid(row=0, column=3, sticky='ew')
        Button(buttonframe, text="Clear", font=("arial", 12, "bold"), height=1, bg="Green", fg="white", command=self.clear_fields).grid(row=0, column=4, sticky='ew')
        Button(buttonframe, text="Exit", font=("arial", 12, "bold"), height=1, bg="Green", fg="white", command=self.main_app.show_main_menu).grid(row=0, column=5, sticky='ew')
        
        scroll_x = ttk.Scrollbar(detailframe, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(detailframe, orient=VERTICAL)
        
        self.staff_table = ttk.Treeview(detailframe, columns=("Staff ID", "Staff Name", "Department", "Position", "Employee ID", "Contact Number", "Email", "Joining Date", "Shift Timing", "Salary", "Employment Status", "Emergency Contact", "Qualification"), show="headings", xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.staff_table.xview)
        scroll_y.config(command=self.staff_table.yview)
        
        for col in ("Staff ID", "Staff Name", "Department", "Position", "Employee ID", "Contact Number", "Email", "Joining Date", "Shift Timing", "Salary", "Employment Status", "Emergency Contact", "Qualification"):
            self.staff_table.heading(col, text=col)
            self.staff_table.column(col, width=100)
        
        self.staff_table.pack(fill=BOTH, expand=1)
    
    def save_data(self):
        if not all([self.StaffId.get(), self.StaffName.get(), self.Department.get(), self.Position.get()]):
            messagebox.showerror("Error", "All required fields must be filled")
            return
        messagebox.showinfo("Success", "Staff record saved successfully")
    
    def clear_fields(self):
        for var in [self.StaffId, self.StaffName, self.Department, self.Position, self.EmployeeId, self.ContactNumber, self.Email, self.JoiningDate, self.ShiftTiming, self.Salary, self.EmploymentStatus, self.EmergencyContact, self.Qualification]:
            var.set("")
        self.txtstaff.delete(1.0, END)

root = Tk()
app = HospitalManagementSystem(root)
root.mainloop()