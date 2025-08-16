# Import all tkinter widgets and functions for GUI creation
from tkinter import *
# Import themed tkinter widgets for modern look
from tkinter import ttk
# Import messagebox for showing dialog boxes to user
from tkinter import messagebox
# Import MySQL connector for database operations
import mysql.connector

# Define the main Patients class that contains all functionality
class Patients:
    # Constructor method that runs when Patients object is created
    def __init__(self, root, main_app=None):
        # Store the root window reference in self.root
        self.root = root
        self.main_app = main_app
        # Set the window title that appears in title bar
        if main_app is None:
            self.root.title("Patient Management System")
            # Set window size (width=1540, height=800) and position (x=0, y=0)
            self.root.geometry("1540x800+0+0")
        
        # Create StringVar objects to store form data - these link GUI to variables
        self.PatientId=StringVar()        # Stores patient ID number
        self.PatientName=StringVar()      # Stores patient full name
        self.Age=StringVar()              # Stores patient age
        self.Gender=StringVar()           # Stores patient gender selection
        self.Phone=StringVar()            # Stores patient phone number
        self.Email=StringVar()            # Stores patient email address
        self.Address=StringVar()          # Stores patient address
        self.BloodType=StringVar()        # Stores patient blood type
        self.Height=StringVar()           # Stores patient height
        self.Weight=StringVar()           # Stores patient weight
        self.EmergencyContact=StringVar() # Stores emergency contact
        self.Insurance=StringVar()        # Stores insurance information
        self.Allergies=StringVar()        # Stores patient allergies
        self.Diagnosis=StringVar()        # Stores medical diagnosis
        self.DoctorName=StringVar()       # Stores assigned doctor name
        self.Department=StringVar()       # Stores hospital department
        self.AppointmentDate=StringVar()  # Stores appointment date
        self.Medicine=StringVar()         # Stores prescribed medicine name
        self.Dose=StringVar()             # Stores medicine dosage
        self.Frequency=StringVar()        # Stores how often to take medicine
        self.Duration=StringVar()         # Stores treatment duration

        # Add back button if integrated
        if self.main_app:
            Button(self.root, text="← Back to Main Menu", font=("Arial", 12, "bold"), bg="blue", fg="white", command=self.main_app.show_main_menu).pack(anchor="nw", padx=10, pady=5)
        
        # Create main title label with styling and pack it at top
        Label(self.root,                           # Parent container is root window
              bd=20,                               # Border width of 20 pixels
              relief=RIDGE,                        # 3D ridge border style
              text="PATIENT MANAGEMENT SYSTEM",    # Text to display
              font=("times new roman", 50, "bold"), # Font family, size, style
              fg="red",                            # Foreground (text) color
              bg="white"                           # Background color
              ).pack(side=TOP, fill=X)             # Pack at top, fill horizontally

        # Create main data container frame with border
        dataframe=Frame(self.root,        # Parent is root window
                       bd=20,             # Border width
                       relief=RIDGE)      # Border style
        # Position frame using absolute positioning
        dataframe.place(x=0,              # X coordinate from left
                       y=130,             # Y coordinate from top
                       width=1530,        # Frame width
                       height=430)        # Frame height

        # Create left frame for patient information input
        leftframe = LabelFrame(dataframe,                    # Parent is dataframe
                              text="Patient Information",    # Frame title text
                              font=("times new roman", 12, "bold"), # Title font
                              bd=10,                         # Border width
                              relief=RIDGE,                  # Border style
                              padx=10)                       # Internal padding X
        # Position left frame inside dataframe
        leftframe.place(x=0,              # X position
                       y=5,               # Y position
                       width=980,         # Frame width
                       height=380)        # Frame height

        # Create right frame for prescription notes
        rightframe = LabelFrame(dataframe,                   # Parent is dataframe
                               text="Patient Records",       # Frame title
                               font=("times new roman", 12, "bold"), # Title font
                               bd=10,                        # Border width
                               relief=RIDGE,                 # Border style
                               padx=10)                      # Internal padding
        # Position right frame next to left frame
        rightframe.place(x=990,           # X position (after left frame)
                        y=5,              # Y position
                        width=460,        # Frame width
                        height=350)       # Frame height

        # Create button container frame
        buttonframe=Frame(self.root,      # Parent is root window
                         bd=20,           # Border width
                         relief=RIDGE)    # Border style
        # Position button frame below data frames
        buttonframe.place(x=0,            # X position
                         y=560,           # Y position (below dataframe)
                         width=1530,      # Full width
                         height=70)       # Button area height

        # Create detail/table container frame
        detailframe=Frame(self.root,      # Parent is root window
                         bd=20,           # Border width
                         relief=RIDGE)    # Border style
        # Position detail frame at bottom
        detailframe.place(x=0,            # X position
                         y=630,           # Y position (below buttons)
                         width=1530,      # Full width
                         height=160)      # Table area height

        # Create Patient ID label and entry field
        Label(leftframe,                  # Parent container
              text="Patient ID:",         # Label text
              font=("arial", 12, "bold"), # Font styling
              padx=2,                     # Horizontal padding
              pady=6                      # Vertical padding
              ).grid(row=0,               # Grid row position
                    column=0,             # Grid column position
                    sticky="w")           # Align to west (left)
        # Create Patient ID input field
        Entry(leftframe,                  # Parent container
              textvariable=self.PatientId, # Link to PatientId variable
              font=("arial", 11, "bold"), # Font styling
              width=28                    # Field width in characters
              ).grid(row=0,               # Same row as label
                    column=1)             # Next column
        
        # Create Patient Name label and entry (same pattern as above)
        Label(leftframe,text="Patient Name:",font=("arial", 12, "bold"),padx=2,pady=6).grid(row=1,column=0, sticky="w")
        Entry(leftframe,textvariable=self.PatientName,font=("arial", 11, "bold"),width=28).grid(row=1,column=1)
        
        # Create Age label and entry
        Label(leftframe,text="Age:",font=("arial", 12, "bold"),padx=2,pady=6).grid(row=2,column=0, sticky="w")
        Entry(leftframe,textvariable=self.Age,font=("arial", 11, "bold"),width=28).grid(row=2,column=1)

        # Create Gender label
        Label(leftframe,text="Gender:",font=("arial", 12, "bold"),padx=2,pady=6).grid(row=3,column=0, sticky="w")
        # Create Gender dropdown (Combobox) instead of text entry
        cmbGender=ttk.Combobox(leftframe,        # Parent container
                              textvariable=self.Gender, # Link to Gender variable
                              font=("arial", 11, "bold"), # Font styling
                              width=25,                  # Width in characters
                              state="readonly")          # User can't type, only select
        # Set dropdown options
        cmbGender["values"]=("Male","Female","Other")  # Available choices
        # Position the dropdown
        cmbGender.grid(row=3,column=1)
        
        # Create Phone label and entry
        Label(leftframe,text="Phone:",font=("arial", 12, "bold"),padx=2,pady=6).grid(row=4,column=0, sticky="w")
        Entry(leftframe,textvariable=self.Phone,font=("arial", 11, "bold"),width=28).grid(row=4,column=1)
        
        # Create Email label and entry
        Label(leftframe,text="Email:",font=("arial", 12, "bold"),padx=2,pady=6).grid(row=5,column=0, sticky="w")
        Entry(leftframe,textvariable=self.Email,font=("arial", 11, "bold"),width=28).grid(row=5,column=1)
        
        # Create Address label and entry
        Label(leftframe,text="Address:",font=("arial", 12, "bold"),padx=2,pady=6).grid(row=6,column=0, sticky="w")
        Entry(leftframe,textvariable=self.Address,font=("arial", 11, "bold"),width=28).grid(row=6,column=1)
        
        # Create Blood Type label and dropdown
        Label(leftframe,text="Blood Type:",font=("arial", 12, "bold"),padx=2,pady=6).grid(row=7,column=0, sticky="w")
        cmbBloodType=ttk.Combobox(leftframe,textvariable=self.BloodType,font=("arial", 11, "bold"),width=25,state="readonly")
        cmbBloodType["values"]=("A+","A-","B+","B-","AB+","AB-","O+","O-")
        cmbBloodType.grid(row=7,column=1)
        
        # Create Height label and entry
        Label(leftframe,text="Height (cm):",font=("arial", 12, "bold"),padx=2,pady=6).grid(row=8,column=0, sticky="w")
        Entry(leftframe,textvariable=self.Height,font=("arial", 11, "bold"),width=28).grid(row=8,column=1)
        
        # Create Weight label and entry
        Label(leftframe,text="Weight (kg):",font=("arial", 12, "bold"),padx=2,pady=6).grid(row=9,column=0, sticky="w")
        Entry(leftframe,textvariable=self.Weight,font=("arial", 11, "bold"),width=28).grid(row=9,column=1)

        # Create Doctor Name label and entry in column 2-3 (right side of left frame)
        Label(leftframe,text="Doctor Name:",font=("arial", 12, "bold"),padx=2,pady=6).grid(row=0,column=2, sticky="w")
        Entry(leftframe,textvariable=self.DoctorName,font=("arial", 11, "bold"),width=28).grid(row=0,column=3)
        
        # Create Department label
        Label(leftframe,text="Department:",font=("arial", 12, "bold"),padx=2,pady=6).grid(row=1,column=2, sticky="w")
        # Create Department dropdown with medical departments
        cmbDepartment=ttk.Combobox(leftframe,textvariable=self.Department,font=("arial", 11, "bold"),width=25,state="readonly")
        # Set department options
        cmbDepartment["values"]=("Cardiology","Neurology","Orthopedics","Pediatrics","General Medicine","Surgery")
        cmbDepartment.grid(row=1,column=3)

        # Create remaining fields in right column of left frame
        Label(leftframe,text="Appointment Date:",font=("arial", 12, "bold"),padx=2,pady=6).grid(row=2,column=2, sticky="w")
        Entry(leftframe,textvariable=self.AppointmentDate,font=("arial", 11, "bold"),width=28).grid(row=2,column=3)
        
        Label(leftframe,text="Medicine:",font=("arial", 12, "bold"),padx=2,pady=6).grid(row=3,column=2, sticky="w")
        Entry(leftframe,textvariable=self.Medicine,font=("arial", 11, "bold"),width=28).grid(row=3,column=3)
        
        Label(leftframe,text="Dose:",font=("arial", 12, "bold"),padx=2,pady=6).grid(row=4,column=2, sticky="w")
        Entry(leftframe,textvariable=self.Dose,font=("arial", 11, "bold"),width=28).grid(row=4,column=3)
        
        # Create Emergency Contact label and entry
        Label(leftframe,text="Emergency Contact:",font=("arial", 12, "bold"),padx=2,pady=6).grid(row=5,column=2, sticky="w")
        Entry(leftframe,textvariable=self.EmergencyContact,font=("arial", 11, "bold"),width=28).grid(row=5,column=3)
        
        # Create Insurance label and entry
        Label(leftframe,text="Insurance:",font=("arial", 12, "bold"),padx=2,pady=6).grid(row=6,column=2, sticky="w")
        Entry(leftframe,textvariable=self.Insurance,font=("arial", 11, "bold"),width=28).grid(row=6,column=3)
        
        # Create Allergies label and entry
        Label(leftframe,text="Allergies:",font=("arial", 12, "bold"),padx=2,pady=6).grid(row=7,column=2, sticky="w")
        Entry(leftframe,textvariable=self.Allergies,font=("arial", 11, "bold"),width=28).grid(row=7,column=3)
        
        # Create Diagnosis label and entry
        Label(leftframe,text="Diagnosis:",font=("arial", 12, "bold"),padx=2,pady=6).grid(row=8,column=2, sticky="w")
        Entry(leftframe,textvariable=self.Diagnosis,font=("arial", 11, "bold"),width=28).grid(row=8,column=3)
        
        Label(leftframe,text="Duration:",font=("arial", 12, "bold"),padx=2,pady=6).grid(row=9,column=2, sticky="w")
        Entry(leftframe,textvariable=self.Duration,font=("arial", 11, "bold"),width=28).grid(row=9,column=3)

        # Create prescription text area for notes
        self.txtprescription = Text(rightframe,          # Parent container
                                   font=("arial", 12, "bold"), # Font styling
                                   width=46,                    # Width in characters
                                   height=16,                   # Height in lines
                                   padx=2,                      # Horizontal padding
                                   pady=6)                      # Vertical padding
        # Position text area in right frame
        self.txtprescription.grid(row=0, column=0)

        # Configure button frame columns to expand equally
        for i in range(6):                    # Loop through 6 columns (0-5)
            buttonframe.columnconfigure(i,    # Column number
                                       weight=1) # Equal weight for expansion
        
        # Create Patient Record button
        Button(buttonframe,                   # Parent container
               text="Patient Record",         # Button text
               font=("arial", 12, "bold"),    # Font styling
               height=1,                      # Button height
               bg="Green",                    # Background color
               fg="white"                     # Text color
               ).grid(row=0,                  # Grid row
                     column=0,                # Grid column
                     sticky='ew')             # Expand east-west (horizontally)
        
        # Create Save Data button with command function
        Button(buttonframe, text="Save Patient Data", font=("arial", 12, "bold"), height=1, bg="Green", fg="white", 
               command=self.save_data        # Function to call when clicked
               ).grid(row=0, column=1, sticky='ew')
        
        # Create remaining buttons
        Button(buttonframe, text="Update", font=("arial", 12, "bold"), height=1, bg="Green", fg="white").grid(row=0, column=2, sticky='ew')
        Button(buttonframe, text="Delete", font=("arial", 12, "bold"), height=1, bg="Green", fg="white").grid(row=0, column=3, sticky='ew')
        
        # Create Clear button with clear function
        Button(buttonframe, text="Clear", font=("arial", 12, "bold"), height=1, bg="Green", fg="white", 
               command=self.clear_fields     # Function to clear all fields
               ).grid(row=0, column=4, sticky='ew')
        
        # Create Exit button that closes application
        exit_command = self.main_app.show_main_menu if self.main_app else root.quit
        Button(buttonframe, text="Exit", font=("arial", 12, "bold"), height=1, bg="Green", fg="white", 
               command=exit_command          # Function to quit or return to main menu
               ).grid(row=0, column=5, sticky='ew')

        # Create horizontal scrollbar for table
        scroll_x=ttk.Scrollbar(detailframe,   # Parent container
                              orient=HORIZONTAL) # Horizontal orientation
        # Create vertical scrollbar for table
        scroll_y=ttk.Scrollbar(detailframe,   # Parent container
                              orient=VERTICAL)   # Vertical orientation
        
        # Create data table (Treeview) with columns
        self.patient_table = ttk.Treeview(
            detailframe,                      # Parent container
            columns=("Patient ID", "Patient Name", "Age", "Gender", "Phone", "Email", 
                    "Address", "Blood Type", "Height", "Weight", "Emergency Contact", "Insurance", "Allergies",
                    "Diagnosis", "Doctor Name", "Department", "Appointment Date", 
                    "Medicine", "Dose", "Frequency", "Duration"), # Column names
            show="headings",                  # Show only column headers, not tree structure
            xscrollcommand=scroll_x.set,      # Link horizontal scrollbar
            yscrollcommand=scroll_y.set)      # Link vertical scrollbar
        
        # Position scrollbars
        scroll_x.pack(side=BOTTOM, fill=X)    # Horizontal scrollbar at bottom
        scroll_y.pack(side=RIGHT, fill=Y)     # Vertical scrollbar at right
        
        # Configure scrollbar commands to control table view
        scroll_x.config(command=self.patient_table.xview) # Horizontal scroll control
        scroll_y.config(command=self.patient_table.yview) # Vertical scroll control
        
        # Configure table columns - set headers and widths
        for col in ("Patient ID", "Patient Name", "Age", "Gender", "Phone", "Email", 
                   "Address", "Blood Type", "Height", "Weight", "Emergency Contact", "Insurance", "Allergies",
                   "Diagnosis", "Doctor Name", "Department", "Appointment Date", 
                   "Medicine", "Dose", "Frequency", "Duration"):
            self.patient_table.heading(col, text=col) # Set column header text
            self.patient_table.column(col, width=100) # Set column width to 100 pixels
        
        # Pack table to fill available space
        self.patient_table.pack(fill=BOTH, expand=1) # Fill both directions, expand with window
        
        # Smooth scrolling variables
        self.scroll_momentum = 0
        self.scroll_timer = None
        
        # Enhanced smooth vertical scrolling
        def smooth_scroll_vertical(event):
            delta = int(-1 * (event.delta / 120))
            # Smooth scroll with smaller increments
            for i in range(abs(delta)):
                if delta > 0:
                    self.patient_table.yview_scroll(1, "units")
                else:
                    self.patient_table.yview_scroll(-1, "units")
                self.root.update_idletasks()
        
        # Enhanced smooth horizontal scrolling
        def smooth_scroll_horizontal(event):
            delta = int(-1 * (event.delta / 120))
            # Smooth scroll with smaller increments
            for i in range(abs(delta)):
                if delta > 0:
                    self.patient_table.xview_scroll(1, "units")
                else:
                    self.patient_table.xview_scroll(-1, "units")
                self.root.update_idletasks()
        
        # Momentum scrolling function
        def momentum_scroll():
            if abs(self.scroll_momentum) > 0.1:
                self.patient_table.yview_scroll(int(self.scroll_momentum), "units")
                self.scroll_momentum *= 0.9  # Decay momentum
                self.scroll_timer = self.root.after(20, momentum_scroll)
            else:
                self.scroll_momentum = 0
        
        # Mouse wheel with momentum
        def on_mousewheel_momentum(event):
            self.scroll_momentum += int(-1 * (event.delta / 120))
            if self.scroll_timer is None:
                momentum_scroll()
        
        # Bind enhanced scroll events
        self.patient_table.bind("<MouseWheel>", smooth_scroll_vertical)
        self.patient_table.bind("<Shift-MouseWheel>", smooth_scroll_horizontal)
        self.patient_table.bind("<Control-MouseWheel>", on_mousewheel_momentum)
        
        # Keyboard smooth scrolling
        def smooth_key_scroll(event):
            key = event.keysym
            if key == "Up":
                self.patient_table.yview_scroll(-1, "units")
            elif key == "Down":
                self.patient_table.yview_scroll(1, "units")
            elif key == "Left":
                self.patient_table.xview_scroll(-1, "units")
            elif key == "Right":
                self.patient_table.xview_scroll(1, "units")
        
        # Bind keyboard events
        self.patient_table.bind("<Key>", smooth_key_scroll)
        self.patient_table.focus_set()  # Enable keyboard focus

    # Method to save patient data to database
    def save_data(self):
        # Check if required fields are filled using all() function
        if not all([self.PatientId.get(),     # Patient ID must be filled
                   self.PatientName.get(),    # Patient Name must be filled
                   self.Medicine.get(),       # Medicine must be filled
                   self.Dose.get()]):         # Dose must be filled
            # Show error message if any required field is empty
            messagebox.showerror("Error", "All required fields must be filled")
            return # Exit function early

        # Initialize connection variable
        conn = None
        try:
            # Establish database connection
            conn = mysql.connector.connect(
                host="localhost",     # Database server address
                user="root",          # Database username
                password="",          # Database password (empty for local)
                database="patientData") # Database name
            
            # Create cursor object to execute SQL commands
            cursor = conn.cursor()
            
            # Execute INSERT SQL command with parameter placeholders
            cursor.execute("INSERT INTO patients VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (
                self.PatientId.get(),        # Get value from PatientId variable
                self.PatientName.get(),      # Get value from PatientName variable
                self.Age.get(),              # Get value from Age variable
                self.Gender.get(),           # Get value from Gender variable
                self.Phone.get(),            # Get value from Phone variable
                self.Email.get(),            # Get value from Email variable
                self.Address.get(),          # Get value from Address variable
                self.BloodType.get(),        # Get value from BloodType variable
                self.Height.get(),           # Get value from Height variable
                self.Weight.get(),           # Get value from Weight variable
                self.EmergencyContact.get(), # Get value from EmergencyContact variable
                self.Insurance.get(),        # Get value from Insurance variable
                self.Allergies.get(),        # Get value from Allergies variable
                self.Diagnosis.get(),        # Get value from Diagnosis variable
                self.DoctorName.get(),       # Get value from DoctorName variable
                self.Department.get(),       # Get value from Department variable
                self.AppointmentDate.get(),  # Get value from AppointmentDate variable
                self.Medicine.get(),         # Get value from Medicine variable
                self.Dose.get(),             # Get value from Dose variable
                self.Frequency.get(),        # Get value from Frequency variable
                self.Duration.get()          # Get value from Duration variable
            ))
            # Commit changes to database (make them permanent)
            conn.commit()
            # Show success message to user
            messagebox.showinfo("Success", "Patient record saved successfully")
        
        # Handle database errors
        except mysql.connector.Error:
            # Show error message if database operation fails
            messagebox.showerror("Error", "Database operation failed")
        
        # Finally block always executes (cleanup)
        finally:
            # Close database connection if it exists and is connected
            if conn and conn.is_connected():
                conn.close()

    # Method to clear all input fields
    def clear_fields(self):
        # Loop through all StringVar variables and clear them
        for var in [self.PatientId, self.PatientName, self.Age, self.Gender, 
                   self.Phone, self.Email, self.Address, self.BloodType, self.Height, self.Weight,
                   self.EmergencyContact, self.Insurance, self.Allergies, self.Diagnosis, self.DoctorName, 
                   self.Department, self.AppointmentDate, self.Medicine, 
                   self.Dose, self.Frequency, self.Duration]:
            var.set("")  # Set each variable to empty string
        
        # Clear prescription text area from first character to end
        self.txtprescription.delete(1.0, END)

# Only run as standalone if this file is executed directly
if __name__ == "__main__":
    # Create main tkinter window
    root=Tk()
    # Create Patients object with root window as parameter
    Patients(root)
    # Start the GUI event loop (keeps window open and responsive)
    root.mainloop()