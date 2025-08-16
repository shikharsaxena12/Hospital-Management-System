# Import all tkinter widgets and functions for GUI creation
from tkinter import *
# Import themed tkinter widgets for modern look
from tkinter import ttk
# Import messagebox for showing dialog boxes to user
from tkinter import messagebox
# Import MySQL connector for database operations
import mysql.connector

# ==================== HOSPITAL STAFF MANAGEMENT SYSTEM ====================
class HospitalStaff:
    def __init__(self, root, main_app=None):
        self.root = root
        self.main_app = main_app
        if main_app is None:
            self.setup_window()
        self.initialize_variables()
        self.create_main_interface()
    
    # ==================== WINDOW SETUP ====================
    def setup_window(self):
        """Configure main window properties"""
        self.root.title("Hospital Staff Management System")
        self.root.geometry("1540x800+0+0")
    
    # ==================== VARIABLE INITIALIZATION ====================
    def initialize_variables(self):
        """Initialize all StringVar objects for form data"""
        # Staff Basic Information
        self.StaffId = StringVar()
        self.StaffName = StringVar()
        self.Department = StringVar()
        self.Position = StringVar()
        self.EmployeeId = StringVar()
        self.ContactNumber = StringVar()
        self.Email = StringVar()
        
        # Work Information
        self.JoiningDate = StringVar()
        self.ShiftTiming = StringVar()
        self.Salary = StringVar()
        self.EmploymentStatus = StringVar()
        self.EmergencyContact = StringVar()
        self.Qualification = StringVar()
        self.Notes = StringVar()
    
    # ==================== MAIN INTERFACE CREATION ====================
    def create_main_interface(self):
        """Create the main user interface"""
        self.create_title_section()
        self.create_frame_layout()
        self.create_input_fields()
        self.create_buttons()
        self.create_data_table()
        self.setup_scrolling()
    
    # ==================== TITLE SECTION ====================
    def create_title_section(self):
        """Create main title header"""
        if self.main_app:
            Button(self.root, text="← Back to Main Menu", font=("Arial", 12, "bold"), bg="blue", fg="white", command=self.main_app.show_main_menu).pack(anchor="nw", padx=10, pady=5)
        
        Label(self.root,
              bd=20, relief=RIDGE,
              text="HOSPITAL STAFF MANAGEMENT SYSTEM",
              font=("times new roman", 50, "bold"),
              fg="red", bg="white"
              ).pack(side=TOP, fill=X)
    
    # ==================== FRAME LAYOUT ====================
    def create_frame_layout(self):
        """Create main frame structure"""
        # Main data container
        self.dataframe = Frame(self.root, bd=20, relief=RIDGE)
        self.dataframe.place(x=0, y=130, width=1530, height=430)
        
        # Left frame for staff information
        self.leftframe = LabelFrame(self.dataframe,
                                   text="Staff Information",
                                   font=("times new roman", 12, "bold"),
                                   bd=10, relief=RIDGE, padx=10)
        self.leftframe.place(x=0, y=5, width=980, height=380)
        
        # Right frame for records
        self.rightframe = LabelFrame(self.dataframe,
                                    text="Staff Records",
                                    font=("times new roman", 12, "bold"),
                                    bd=10, relief=RIDGE, padx=10)
        self.rightframe.place(x=990, y=5, width=460, height=350)
        
        # Button frame
        self.buttonframe = Frame(self.root, bd=20, relief=RIDGE)
        self.buttonframe.place(x=0, y=560, width=1530, height=70)
        
        # Detail/table frame
        self.detailframe = Frame(self.root, bd=20, relief=RIDGE)
        self.detailframe.place(x=0, y=630, width=1530, height=160)
    
    # ==================== INPUT FIELDS CREATION ====================
    def create_input_fields(self):
        """Create all input fields and labels"""
        self.create_left_column_fields()
        self.create_right_column_fields()
        self.create_text_area()
    
    def create_left_column_fields(self):
        """Create input fields for left column"""
        # Essential Staff Information
        Label(self.leftframe, text="Staff ID:", font=("arial", 12, "bold"), padx=2, pady=6).grid(row=0, column=0, sticky="w")
        Entry(self.leftframe, textvariable=self.StaffId, font=("arial", 11, "bold"), width=28).grid(row=0, column=1)
        
        Label(self.leftframe, text="Staff Name:", font=("arial", 12, "bold"), padx=2, pady=6).grid(row=1, column=0, sticky="w")
        Entry(self.leftframe, textvariable=self.StaffName, font=("arial", 11, "bold"), width=28).grid(row=1, column=1)
        
        Label(self.leftframe, text="Department:", font=("arial", 12, "bold"), padx=2, pady=6).grid(row=2, column=0, sticky="w")
        cmbDepartment = ttk.Combobox(self.leftframe, textvariable=self.Department, font=("arial", 11, "bold"), width=25, state="readonly")
        cmbDepartment["values"] = ("Emergency", "Cardiology", "Neurology", "Orthopedics", "Pediatrics", "Radiology", "Laboratory", "Pharmacy", "Administration", "Nursing", "Surgery", "ICU")
        cmbDepartment.grid(row=2, column=1)
        
        Label(self.leftframe, text="Position:", font=("arial", 12, "bold"), padx=2, pady=6).grid(row=3, column=0, sticky="w")
        cmbPosition = ttk.Combobox(self.leftframe, textvariable=self.Position, font=("arial", 11, "bold"), width=25, state="readonly")
        cmbPosition["values"] = ("Doctor", "Nurse", "Technician", "Administrator", "Pharmacist", "Receptionist", "Security", "Cleaner", "Manager", "Supervisor")
        cmbPosition.grid(row=3, column=1)
        
        Label(self.leftframe, text="Employee ID:", font=("arial", 12, "bold"), padx=2, pady=6).grid(row=4, column=0, sticky="w")
        Entry(self.leftframe, textvariable=self.EmployeeId, font=("arial", 11, "bold"), width=28).grid(row=4, column=1)
        
        Label(self.leftframe, text="Contact Number:", font=("arial", 12, "bold"), padx=2, pady=6).grid(row=5, column=0, sticky="w")
        Entry(self.leftframe, textvariable=self.ContactNumber, font=("arial", 11, "bold"), width=28).grid(row=5, column=1)
        
        Label(self.leftframe, text="Email:", font=("arial", 12, "bold"), padx=2, pady=6).grid(row=6, column=0, sticky="w")
        Entry(self.leftframe, textvariable=self.Email, font=("arial", 11, "bold"), width=28).grid(row=6, column=1)
    
    def create_right_column_fields(self):
        """Create input fields for right column"""
        Label(self.leftframe, text="Joining Date:", font=("arial", 12, "bold"), padx=2, pady=6).grid(row=0, column=2, sticky="w")
        Entry(self.leftframe, textvariable=self.JoiningDate, font=("arial", 11, "bold"), width=28).grid(row=0, column=3)
        
        Label(self.leftframe, text="Shift Timing:", font=("arial", 12, "bold"), padx=2, pady=6).grid(row=1, column=2, sticky="w")
        cmbShift = ttk.Combobox(self.leftframe, textvariable=self.ShiftTiming, font=("arial", 11, "bold"), width=25, state="readonly")
        cmbShift["values"] = ("Morning (6AM-2PM)", "Evening (2PM-10PM)", "Night (10PM-6AM)", "Rotating")
        cmbShift.grid(row=1, column=3)
        
        Label(self.leftframe, text="Salary:", font=("arial", 12, "bold"), padx=2, pady=6).grid(row=2, column=2, sticky="w")
        Entry(self.leftframe, textvariable=self.Salary, font=("arial", 11, "bold"), width=28).grid(row=2, column=3)
        
        Label(self.leftframe, text="Employment Status:", font=("arial", 12, "bold"), padx=2, pady=6).grid(row=3, column=2, sticky="w")
        cmbEmploymentStatus = ttk.Combobox(self.leftframe, textvariable=self.EmploymentStatus, font=("arial", 11, "bold"), width=25, state="readonly")
        cmbEmploymentStatus["values"] = ("Active", "On Leave", "Suspended", "Terminated")
        cmbEmploymentStatus.grid(row=3, column=3)
        
        Label(self.leftframe, text="Emergency Contact:", font=("arial", 12, "bold"), padx=2, pady=6).grid(row=4, column=2, sticky="w")
        Entry(self.leftframe, textvariable=self.EmergencyContact, font=("arial", 11, "bold"), width=28).grid(row=4, column=3)
        
        Label(self.leftframe, text="Qualification:", font=("arial", 12, "bold"), padx=2, pady=6).grid(row=5, column=2, sticky="w")
        Entry(self.leftframe, textvariable=self.Qualification, font=("arial", 11, "bold"), width=28).grid(row=5, column=3)
    
    def create_text_area(self):
        """Create staff notes text area"""
        self.txtstaff = Text(self.rightframe,
                               font=("arial", 12, "bold"),
                               width=46, height=16,
                               padx=2, pady=6)
        self.txtstaff.grid(row=0, column=0)
    
    # ==================== BUTTON CREATION ====================
    def create_buttons(self):
        """Create all action buttons"""
        # Configure button frame columns
        for i in range(6):
            self.buttonframe.columnconfigure(i, weight=1)
        
        Button(self.buttonframe, text="Staff Record", font=("arial", 12, "bold"), height=1, bg="Green", fg="white").grid(row=0, column=0, sticky='ew')
        Button(self.buttonframe, text="Save Staff Data", font=("arial", 12, "bold"), height=1, bg="Green", fg="white", command=self.save_data).grid(row=0, column=1, sticky='ew')
        Button(self.buttonframe, text="Update", font=("arial", 12, "bold"), height=1, bg="Green", fg="white").grid(row=0, column=2, sticky='ew')
        Button(self.buttonframe, text="Delete", font=("arial", 12, "bold"), height=1, bg="Green", fg="white").grid(row=0, column=3, sticky='ew')
        Button(self.buttonframe, text="Clear", font=("arial", 12, "bold"), height=1, bg="Green", fg="white", command=self.clear_fields).grid(row=0, column=4, sticky='ew')
        exit_command = self.main_app.show_main_menu if self.main_app else self.root.quit
        Button(self.buttonframe, text="Exit", font=("arial", 12, "bold"), height=1, bg="Green", fg="white", command=exit_command).grid(row=0, column=5, sticky='ew')
    
    # ==================== DATA TABLE CREATION ====================
    def create_data_table(self):
        """Create data display table with scrollbars"""
        # Create scrollbars
        scroll_x = ttk.Scrollbar(self.detailframe, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(self.detailframe, orient=VERTICAL)
        
        # Create table
        self.staff_table = ttk.Treeview(
            self.detailframe,
            columns=("Staff ID", "Staff Name", "Department", "Position", "Employee ID", "Contact Number",
                    "Email", "Joining Date", "Shift Timing", "Salary", "Employment Status", "Emergency Contact", "Qualification"),
            show="headings",
            xscrollcommand=scroll_x.set,
            yscrollcommand=scroll_y.set)
        
        # Position scrollbars
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        
        # Configure scrollbar commands
        scroll_x.config(command=self.staff_table.xview)
        scroll_y.config(command=self.staff_table.yview)
        
        # Configure table columns
        for col in ("Staff ID", "Staff Name", "Department", "Position", "Employee ID", "Contact Number",
                   "Email", "Joining Date", "Shift Timing", "Salary", "Employment Status", "Emergency Contact", "Qualification"):
            self.staff_table.heading(col, text=col)
            self.staff_table.column(col, width=100)
        
        self.staff_table.pack(fill=BOTH, expand=1)
    
    # ==================== SMOOTH SCROLLING SETUP ====================
    def setup_scrolling(self):
        """Setup smooth scrolling functionality"""
        self.scroll_momentum = 0
        self.scroll_timer = None
        
        def smooth_scroll_vertical(event):
            delta = int(-1 * (event.delta / 120))
            for i in range(abs(delta)):
                if delta > 0:
                    self.staff_table.yview_scroll(1, "units")
                else:
                    self.staff_table.yview_scroll(-1, "units")
                self.root.update_idletasks()
        
        def smooth_scroll_horizontal(event):
            delta = int(-1 * (event.delta / 120))
            for i in range(abs(delta)):
                if delta > 0:
                    self.staff_table.xview_scroll(1, "units")
                else:
                    self.staff_table.xview_scroll(-1, "units")
                self.root.update_idletasks()
        
        def momentum_scroll():
            if abs(self.scroll_momentum) > 0.1:
                self.staff_table.yview_scroll(int(self.scroll_momentum), "units")
                self.scroll_momentum *= 0.9
                self.scroll_timer = self.root.after(20, momentum_scroll)
            else:
                self.scroll_momentum = 0
        
        def on_mousewheel_momentum(event):
            self.scroll_momentum += int(-1 * (event.delta / 120))
            if self.scroll_timer is None:
                momentum_scroll()
        
        def smooth_key_scroll(event):
            key = event.keysym
            if key == "Up":
                self.staff_table.yview_scroll(-1, "units")
            elif key == "Down":
                self.staff_table.yview_scroll(1, "units")
            elif key == "Left":
                self.staff_table.xview_scroll(-1, "units")
            elif key == "Right":
                self.staff_table.xview_scroll(1, "units")
        
        # Bind scroll events
        self.staff_table.bind("<MouseWheel>", smooth_scroll_vertical)
        self.staff_table.bind("<Shift-MouseWheel>", smooth_scroll_horizontal)
        self.staff_table.bind("<Control-MouseWheel>", on_mousewheel_momentum)
        self.staff_table.bind("<Key>", smooth_key_scroll)
        self.staff_table.focus_set()
    
    # ==================== DATABASE OPERATIONS ====================
    def save_data(self):
        """Save staff data to database"""
        if not self.validate_required_fields():
            return
        
        conn = None
        try:
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="staffData")
            
            cursor = conn.cursor()
            cursor.execute("INSERT INTO staff VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (
                self.StaffId.get(), self.StaffName.get(), self.Department.get(), self.Position.get(),
                self.EmployeeId.get(), self.ContactNumber.get(), self.Email.get(), self.JoiningDate.get(),
                self.ShiftTiming.get(), self.Salary.get(), self.EmploymentStatus.get(), self.EmergencyContact.get(),
                self.Qualification.get()))
            
            conn.commit()
            messagebox.showinfo("Success", "Staff record saved successfully")
        
        except mysql.connector.Error:
            messagebox.showerror("Error", "Database operation failed")
        
        finally:
            if conn and conn.is_connected():
                conn.close()
    
    def validate_required_fields(self):
        """Validate that required fields are filled"""
        if not all([self.StaffId.get(), self.StaffName.get(), self.Department.get(), self.Position.get()]):
            messagebox.showerror("Error", "All required fields must be filled")
            return False
        return True
    
    # ==================== UTILITY METHODS ====================
    def clear_fields(self):
        """Clear all input fields"""
        variables = [self.StaffId, self.StaffName, self.Department, self.Position, self.EmployeeId,
                    self.ContactNumber, self.Email, self.JoiningDate, self.ShiftTiming, self.Salary,
                    self.EmploymentStatus, self.EmergencyContact, self.Qualification]
        
        for var in variables:
            var.set("")
        
        self.txtstaff.delete(1.0, END)


# ==================== MAIN EXECUTION ====================
if __name__ == "__main__":
    root = Tk()
    app = HospitalStaff(root)
    root.mainloop()