from tkinter import Tk, Frame, Label, Entry, Button, Text, StringVar, LabelFrame, RIDGE, TOP, X, BOTTOM, Y, BOTH, END
from tkinter import ttk, messagebox
from mysql.connector import connect, Error, InterfaceError, ProgrammingError
from config import DB_CONFIG

class HospitalStaff:
    # Constants for styling and configuration
    LABEL_FONT = ("arial", 12, "bold")
    ENTRY_FONT = ("arial", 11, "bold")
    BUTTON_FONT = ("arial", 12, "bold")
    TITLE_FONT = ("times new roman", 50, "bold")
    LABEL_PADDING = {'padx': 2, 'pady': 6}
    BUTTON_STYLE = {'font': BUTTON_FONT, 'height': 1, 'bg': "Green", 'fg': "white"}
    
    DEPARTMENTS = ("Emergency", "Cardiology", "Neurology", "Orthopedics", "Pediatrics", 
                   "Radiology", "Laboratory", "Pharmacy", "Administration", "Nursing", "Surgery", "ICU")
    POSITIONS = ("Doctor", "Nurse", "Technician", "Administrator", "Pharmacist", 
                 "Receptionist", "Security", "Cleaner", "Manager", "Supervisor")
    SHIFTS = ("Morning (6AM-2PM)", "Evening (2PM-10PM)", "Night (10PM-6AM)", "Rotating")
    EMPLOYMENT_STATUS = ("Active", "On Leave", "Suspended", "Terminated")
    
    TABLE_COLUMNS = ("Staff ID", "Staff Name", "Department", "Position", "Employee ID", "Contact Number",
                     "Email", "Joining Date", "Shift Timing", "Salary", "Employment Status", "Emergency Contact", "Qualification")
    
    def __init__(self, root):
        self.root = root
        self.db_pool = None
        self.setup_window()
        self.initialize_variables()
        self.create_main_interface()
    
    def setup_window(self):
        """Configure main window properties"""
        self.root.title("Hospital Staff Management System")
        self.root.state('zoomed')  # Responsive fullscreen
        self.root.configure(bg='white')
    
    def initialize_variables(self):
        """Initialize all StringVar objects for form data"""
        self.staff_id = StringVar()
        self.staff_name = StringVar()
        self.department = StringVar()
        self.position = StringVar()
        self.employee_id = StringVar()
        self.contact_number = StringVar()
        self.email = StringVar()
        self.joining_date = StringVar()
        self.shift_timing = StringVar()
        self.salary = StringVar()
        self.employment_status = StringVar()
        self.emergency_contact = StringVar()
        self.qualification = StringVar()
    
    def create_main_interface(self):
        """Create the main user interface"""
        self.create_title_section()
        self.create_frame_layout()
        self.create_input_fields()
        self.create_buttons()
        self.create_data_table()
        self.setup_scrolling()
    
    def create_title_section(self):
        """Create main title header"""
        title_label = Label(self.root, bd=20, relief=RIDGE, text="HOSPITAL STAFF MANAGEMENT SYSTEM",
                           font=self.TITLE_FONT, fg="red", bg="white")
        title_label.pack(side=TOP, fill=X)
    
    def create_frame_layout(self):
        """Create responsive frame structure"""
        # Main container using pack for responsiveness
        self.main_container = Frame(self.root, bg='white')
        self.main_container.pack(fill=BOTH, expand=True, padx=10, pady=10)
        
        # Top section for forms
        self.form_container = Frame(self.main_container, bd=10, relief=RIDGE)
        self.form_container.pack(fill=X, pady=(0, 10))
        
        # Left frame for staff information
        self.leftframe = LabelFrame(self.form_container, text="Staff Information",
                                   font=self.LABEL_FONT, bd=5, relief=RIDGE, padx=10, pady=10)
        self.leftframe.pack(side='left', fill=BOTH, expand=True, padx=(0, 5))
        
        # Right frame for notes
        self.rightframe = LabelFrame(self.form_container, text="Staff Notes",
                                    font=self.LABEL_FONT, bd=5, relief=RIDGE, padx=10, pady=10)
        self.rightframe.pack(side='right', fill=Y, padx=(5, 0))
        
        # Button frame
        self.buttonframe = Frame(self.main_container, bd=10, relief=RIDGE)
        self.buttonframe.pack(fill=X, pady=(0, 10))
        
        # Table frame
        self.detailframe = Frame(self.main_container, bd=10, relief=RIDGE)
        self.detailframe.pack(fill=BOTH, expand=True)
    
    def create_input_fields(self):
        """Create all input fields and labels"""
        self.create_form_fields()
        self.create_text_area()
    
    def create_label_entry(self, parent, text, variable, row, column):
        """Helper method to create label-entry pairs"""
        Label(parent, text=text, font=self.LABEL_FONT, **self.LABEL_PADDING).grid(row=row, column=column, sticky="w")
        Entry(parent, textvariable=variable, font=self.ENTRY_FONT, width=28).grid(row=row, column=column+1, padx=(0, 10))
    
    def create_label_combobox(self, parent, text, variable, values, row, column):
        """Helper method to create label-combobox pairs"""
        Label(parent, text=text, font=self.LABEL_FONT, **self.LABEL_PADDING).grid(row=row, column=column, sticky="w")
        combo = ttk.Combobox(parent, textvariable=variable, font=self.ENTRY_FONT, width=25, state="readonly")
        combo["values"] = values
        combo.grid(row=row, column=column+1, padx=(0, 10))
        return combo
    
    def create_form_fields(self):
        """Create all form input fields"""
        # Left column
        self.create_label_entry(self.leftframe, "Staff ID:", self.staff_id, 0, 0)
        self.create_label_entry(self.leftframe, "Staff Name:", self.staff_name, 1, 0)
        self.create_label_combobox(self.leftframe, "Department:", self.department, self.DEPARTMENTS, 2, 0)
        self.create_label_combobox(self.leftframe, "Position:", self.position, self.POSITIONS, 3, 0)
        self.create_label_entry(self.leftframe, "Employee ID:", self.employee_id, 4, 0)
        self.create_label_entry(self.leftframe, "Contact Number:", self.contact_number, 5, 0)
        self.create_label_entry(self.leftframe, "Email:", self.email, 6, 0)
        
        # Right column
        self.create_label_entry(self.leftframe, "Joining Date:", self.joining_date, 0, 2)
        self.create_label_combobox(self.leftframe, "Shift Timing:", self.shift_timing, self.SHIFTS, 1, 2)
        self.create_label_entry(self.leftframe, "Salary:", self.salary, 2, 2)
        self.create_label_combobox(self.leftframe, "Employment Status:", self.employment_status, self.EMPLOYMENT_STATUS, 3, 2)
        self.create_label_entry(self.leftframe, "Emergency Contact:", self.emergency_contact, 4, 2)
        self.create_label_entry(self.leftframe, "Qualification:", self.qualification, 5, 2)
    
    def create_text_area(self):
        """Create staff notes text area"""
        self.txt_staff = Text(self.rightframe, font=self.ENTRY_FONT, width=40, height=20, wrap='word')
        self.txt_staff.pack(fill=BOTH, expand=True)
    
    def create_buttons(self):
        """Create all action buttons"""
        for i in range(6):
            self.buttonframe.columnconfigure(i, weight=1)
        
        buttons = [
            ("Staff Record", None),
            ("Save Staff Data", self.save_data),
            ("Update", None),
            ("Delete", None),
            ("Clear", self.clear_fields),
            ("Exit", self.root.quit)
        ]
        
        for i, (text, command) in enumerate(buttons):
            btn = Button(self.buttonframe, text=text, command=command, **self.BUTTON_STYLE)
            btn.grid(row=0, column=i, sticky='ew', padx=2)
    
    def create_data_table(self):
        """Create data display table with scrollbars"""
        scroll_x = ttk.Scrollbar(self.detailframe, orient='horizontal')
        scroll_y = ttk.Scrollbar(self.detailframe, orient='vertical')
        
        self.staff_table = ttk.Treeview(
            self.detailframe,
            columns=self.TABLE_COLUMNS,
            show="headings",
            xscrollcommand=scroll_x.set,
            yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side='right', fill=Y)
        scroll_x.config(command=self.staff_table.xview)
        scroll_y.config(command=self.staff_table.yview)
        
        for col in self.TABLE_COLUMNS:
            self.staff_table.heading(col, text=col)
            self.staff_table.column(col, width=100)
        
        self.staff_table.pack(fill=BOTH, expand=True)
    
    def setup_scrolling(self):
        """Setup optimized scrolling functionality"""
        self.scroll_momentum = 0
        self.scroll_timer = None
        
        def smooth_scroll_vertical(event):
            delta = -1 if event.delta > 0 else 1
            self.staff_table.yview_scroll(delta, "units")
        
        def smooth_scroll_horizontal(event):
            delta = -1 if event.delta > 0 else 1
            self.staff_table.xview_scroll(delta, "units")
        
        def momentum_scroll():
            if abs(self.scroll_momentum) > 0.1:
                self.staff_table.yview_scroll(int(self.scroll_momentum), "units")
                self.scroll_momentum *= 0.9
                self.scroll_timer = self.root.after(20, momentum_scroll)
            else:
                self.scroll_momentum = 0
                self.scroll_timer = None
        
        def on_mousewheel_momentum(event):
            self.scroll_momentum += int(-1 * (event.delta / 120))
            if self.scroll_timer is None:
                self.scroll_timer = self.root.after(20, momentum_scroll)
        
        def smooth_key_scroll(event):
            key_actions = {
                "Up": lambda: self.staff_table.yview_scroll(-1, "units"),
                "Down": lambda: self.staff_table.yview_scroll(1, "units"),
                "Left": lambda: self.staff_table.xview_scroll(-1, "units"),
                "Right": lambda: self.staff_table.xview_scroll(1, "units")
            }
            action = key_actions.get(event.keysym)
            if action:
                action()
        
        self.staff_table.bind("<MouseWheel>", smooth_scroll_vertical)
        self.staff_table.bind("<Shift-MouseWheel>", smooth_scroll_horizontal)
        self.staff_table.bind("<Control-MouseWheel>", on_mousewheel_momentum)
        self.staff_table.bind("<Key>", smooth_key_scroll)
        self.staff_table.focus_set()
    
    def get_db_connection(self):
        """Get database connection with proper error handling"""
        try:
            return connect(**DB_CONFIG)
        except InterfaceError as e:
            messagebox.showerror("Connection Error", f"Cannot connect to database: {e}")
            return None
        except ProgrammingError as e:
            messagebox.showerror("Database Error", f"Database configuration error: {e}")
            return None
        except Error as e:
            messagebox.showerror("Database Error", f"Database error: {e}")
            return None
    
    def save_data(self):
        """Save staff data to database with proper resource management"""
        if not self.validate_required_fields():
            return
        
        conn = self.get_db_connection()
        if not conn:
            return
        
        try:
            with conn.cursor() as cursor:
                cursor.execute(
                    "INSERT INTO staff VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                    (self.staff_id.get(), self.staff_name.get(), self.department.get(), self.position.get(),
                     self.employee_id.get(), self.contact_number.get(), self.email.get(), self.joining_date.get(),
                     self.shift_timing.get(), self.salary.get(), self.employment_status.get(), 
                     self.emergency_contact.get(), self.qualification.get()))
                conn.commit()
                messagebox.showinfo("Success", "Staff record saved successfully")
        except InterfaceError:
            messagebox.showerror("Error", "Database connection lost")
        except ProgrammingError as e:
            messagebox.showerror("Error", f"SQL execution error: {e}")
        except Error as e:
            messagebox.showerror("Error", f"Database operation failed: {e}")
        finally:
            if conn.is_connected():
                conn.close()
    
    def validate_required_fields(self):
        """Validate that required fields are filled"""
        required_fields = [self.staff_id.get(), self.staff_name.get(), 
                          self.department.get(), self.position.get()]
        if not all(required_fields):
            messagebox.showerror("Error", "All required fields must be filled")
            return False
        return True
    
    def clear_fields(self):
        """Clear all input fields"""
        variables = [self.staff_id, self.staff_name, self.department, self.position, self.employee_id,
                    self.contact_number, self.email, self.joining_date, self.shift_timing, self.salary,
                    self.employment_status, self.emergency_contact, self.qualification]
        
        for var in variables:
            var.set("")
        
        self.txt_staff.delete(1.0, END)


if __name__ == "__main__":
    root = Tk()
    app = HospitalStaff(root)
    root.mainloop()