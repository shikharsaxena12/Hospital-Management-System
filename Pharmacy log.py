# Import all tkinter widgets and functions for GUI creation
from tkinter import *
# Import themed tkinter widgets for modern look
from tkinter import ttk
# Import messagebox for showing dialog boxes to user
from tkinter import messagebox
# Import MySQL connector for database operations
import mysql.connector

# ==================== MEDICINAL STOCK MANAGEMENT SYSTEM ====================
class MedicinalStock:
    def __init__(self, root):
        self.root = root
        self.setup_window()
        self.initialize_variables()
        self.create_main_interface()
    
    # ==================== WINDOW SETUP ====================
    def setup_window(self):
        """Configure main window properties"""
        self.root.title("Medicinal Stock Management System")
        self.root.geometry("1540x800+0+0")
    
    # ==================== VARIABLE INITIALIZATION ====================
    def initialize_variables(self):
        """Initialize all StringVar objects for form data"""
        # Medicine Basic Information
        self.MedicineId = StringVar()
        self.MedicineName = StringVar()
        self.Category = StringVar()
        self.Manufacturer = StringVar()
        self.BatchNo = StringVar()
        self.ExpiryDate = StringVar()
        self.ManufactureDate = StringVar()
        
        # Stock Information
        self.Quantity = StringVar()
        self.Unit = StringVar()
        self.MinStockLevel = StringVar()
        self.MaxStockLevel = StringVar()
        self.ReorderLevel = StringVar()
        
        # Pricing Information
        self.CostPrice = StringVar()
        self.SellingPrice = StringVar()
        self.Discount = StringVar()
        
        # Supplier Information
        self.Supplier = StringVar()
        self.SupplierContact = StringVar()
        
        # Storage Information
        self.Location = StringVar()
        self.StorageCondition = StringVar()
        self.PurchaseDate = StringVar()
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
        Label(self.root,
              bd=20, relief=RIDGE,
              text="MEDICINAL STOCK MANAGEMENT SYSTEM",
              font=("times new roman", 50, "bold"),
              fg="red", bg="white"
              ).pack(side=TOP, fill=X)
    
    # ==================== FRAME LAYOUT ====================
    def create_frame_layout(self):
        """Create main frame structure"""
        # Main data container
        self.dataframe = Frame(self.root, bd=20, relief=RIDGE)
        self.dataframe.place(x=0, y=130, width=1530, height=430)
        
        # Left frame for medicine information
        self.leftframe = LabelFrame(self.dataframe,
                                   text="Medicine Information",
                                   font=("times new roman", 12, "bold"),
                                   bd=10, relief=RIDGE, padx=10)
        self.leftframe.place(x=0, y=5, width=980, height=380)
        
        # Right frame for records
        self.rightframe = LabelFrame(self.dataframe,
                                    text="Medicine Records",
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
        # Medicine Basic Information Fields
        Label(self.leftframe, text="Medicine ID:", font=("arial", 12, "bold"), padx=2, pady=6).grid(row=0, column=0, sticky="w")
        Entry(self.leftframe, textvariable=self.MedicineId, font=("arial", 11, "bold"), width=28).grid(row=0, column=1)
        
        Label(self.leftframe, text="Medicine Name:", font=("arial", 12, "bold"), padx=2, pady=6).grid(row=1, column=0, sticky="w")
        Entry(self.leftframe, textvariable=self.MedicineName, font=("arial", 11, "bold"), width=28).grid(row=1, column=1)
        
        Label(self.leftframe, text="Category:", font=("arial", 12, "bold"), padx=2, pady=6).grid(row=2, column=0, sticky="w")
        cmbCategory = ttk.Combobox(self.leftframe, textvariable=self.Category, font=("arial", 11, "bold"), width=25, state="readonly")
        cmbCategory["values"] = ("Tablet", "Capsule", "Syrup", "Injection", "Ointment", "Drops", "Inhaler", "Other")
        cmbCategory.grid(row=2, column=1)
        
        Label(self.leftframe, text="Manufacturer:", font=("arial", 12, "bold"), padx=2, pady=6).grid(row=3, column=0, sticky="w")
        Entry(self.leftframe, textvariable=self.Manufacturer, font=("arial", 11, "bold"), width=28).grid(row=3, column=1)
        
        Label(self.leftframe, text="Batch No:", font=("arial", 12, "bold"), padx=2, pady=6).grid(row=4, column=0, sticky="w")
        Entry(self.leftframe, textvariable=self.BatchNo, font=("arial", 11, "bold"), width=28).grid(row=4, column=1)
        
        Label(self.leftframe, text="Expiry Date:", font=("arial", 12, "bold"), padx=2, pady=6).grid(row=5, column=0, sticky="w")
        Entry(self.leftframe, textvariable=self.ExpiryDate, font=("arial", 11, "bold"), width=28).grid(row=5, column=1)
        
        Label(self.leftframe, text="Manufacture Date:", font=("arial", 12, "bold"), padx=2, pady=6).grid(row=6, column=0, sticky="w")
        Entry(self.leftframe, textvariable=self.ManufactureDate, font=("arial", 11, "bold"), width=28).grid(row=6, column=1)
        
        # Stock Information Fields
        Label(self.leftframe, text="Quantity:", font=("arial", 12, "bold"), padx=2, pady=6).grid(row=7, column=0, sticky="w")
        Entry(self.leftframe, textvariable=self.Quantity, font=("arial", 11, "bold"), width=28).grid(row=7, column=1)
        
        Label(self.leftframe, text="Unit:", font=("arial", 12, "bold"), padx=2, pady=6).grid(row=8, column=0, sticky="w")
        cmbUnit = ttk.Combobox(self.leftframe, textvariable=self.Unit, font=("arial", 11, "bold"), width=25, state="readonly")
        cmbUnit["values"] = ("Pieces", "Bottles", "Boxes", "Strips", "Vials", "Tubes", "Packets")
        cmbUnit.grid(row=8, column=1)
        
        Label(self.leftframe, text="Min Stock Level:", font=("arial", 12, "bold"), padx=2, pady=6).grid(row=9, column=0, sticky="w")
        Entry(self.leftframe, textvariable=self.MinStockLevel, font=("arial", 11, "bold"), width=28).grid(row=9, column=1)
    
    def create_right_column_fields(self):
        """Create input fields for right column"""
        # Stock Management Information
        Label(self.leftframe, text="Max Stock Level:", font=("arial", 12, "bold"), padx=2, pady=6).grid(row=0, column=2, sticky="w")
        Entry(self.leftframe, textvariable=self.MaxStockLevel, font=("arial", 11, "bold"), width=28).grid(row=0, column=3)
        
        Label(self.leftframe, text="Reorder Level:", font=("arial", 12, "bold"), padx=2, pady=6).grid(row=1, column=2, sticky="w")
        Entry(self.leftframe, textvariable=self.ReorderLevel, font=("arial", 11, "bold"), width=28).grid(row=1, column=3)
        
        Label(self.leftframe, text="Cost Price:", font=("arial", 12, "bold"), padx=2, pady=6).grid(row=2, column=2, sticky="w")
        Entry(self.leftframe, textvariable=self.CostPrice, font=("arial", 11, "bold"), width=28).grid(row=2, column=3)
        
        # Pricing Information
        Label(self.leftframe, text="Selling Price:", font=("arial", 12, "bold"), padx=2, pady=6).grid(row=3, column=2, sticky="w")
        Entry(self.leftframe, textvariable=self.SellingPrice, font=("arial", 11, "bold"), width=28).grid(row=3, column=3)
        
        Label(self.leftframe, text="Discount (%):", font=("arial", 12, "bold"), padx=2, pady=6).grid(row=4, column=2, sticky="w")
        Entry(self.leftframe, textvariable=self.Discount, font=("arial", 11, "bold"), width=28).grid(row=4, column=3)
        
        # Supplier Information
        Label(self.leftframe, text="Supplier:", font=("arial", 12, "bold"), padx=2, pady=6).grid(row=5, column=2, sticky="w")
        Entry(self.leftframe, textvariable=self.Supplier, font=("arial", 11, "bold"), width=28).grid(row=5, column=3)
        
        Label(self.leftframe, text="Supplier Contact:", font=("arial", 12, "bold"), padx=2, pady=6).grid(row=6, column=2, sticky="w")
        Entry(self.leftframe, textvariable=self.SupplierContact, font=("arial", 11, "bold"), width=28).grid(row=6, column=3)
        
        Label(self.leftframe, text="Location:", font=("arial", 12, "bold"), padx=2, pady=6).grid(row=7, column=2, sticky="w")
        Entry(self.leftframe, textvariable=self.Location, font=("arial", 11, "bold"), width=28).grid(row=7, column=3)
        
        Label(self.leftframe, text="Storage Condition:", font=("arial", 12, "bold"), padx=2, pady=6).grid(row=8, column=2, sticky="w")
        cmbStorage = ttk.Combobox(self.leftframe, textvariable=self.StorageCondition, font=("arial", 11, "bold"), width=25, state="readonly")
        cmbStorage["values"] = ("Room Temperature", "Refrigerated", "Frozen", "Cool & Dry", "Special Storage")
        cmbStorage.grid(row=8, column=3)
        
        Label(self.leftframe, text="Purchase Date:", font=("arial", 12, "bold"), padx=2, pady=6).grid(row=9, column=2, sticky="w")
        Entry(self.leftframe, textvariable=self.PurchaseDate, font=("arial", 11, "bold"), width=28).grid(row=9, column=3)
    
    def create_text_area(self):
        """Create medicine notes text area"""
        self.txtmedicine = Text(self.rightframe,
                               font=("arial", 12, "bold"),
                               width=46, height=16,
                               padx=2, pady=6)
        self.txtmedicine.grid(row=0, column=0)
    
    # ==================== BUTTON CREATION ====================
    def create_buttons(self):
        """Create all action buttons"""
        # Configure button frame columns
        for i in range(6):
            self.buttonframe.columnconfigure(i, weight=1)
        
        Button(self.buttonframe, text="Medicine Record", font=("arial", 12, "bold"), height=1, bg="Green", fg="white").grid(row=0, column=0, sticky='ew')
        Button(self.buttonframe, text="Save Medicine Data", font=("arial", 12, "bold"), height=1, bg="Green", fg="white", command=self.save_data).grid(row=0, column=1, sticky='ew')
        Button(self.buttonframe, text="Update", font=("arial", 12, "bold"), height=1, bg="Green", fg="white").grid(row=0, column=2, sticky='ew')
        Button(self.buttonframe, text="Delete", font=("arial", 12, "bold"), height=1, bg="Green", fg="white").grid(row=0, column=3, sticky='ew')
        Button(self.buttonframe, text="Clear", font=("arial", 12, "bold"), height=1, bg="Green", fg="white", command=self.clear_fields).grid(row=0, column=4, sticky='ew')
        Button(self.buttonframe, text="Exit", font=("arial", 12, "bold"), height=1, bg="Green", fg="white", command=self.root.quit).grid(row=0, column=5, sticky='ew')
    
    # ==================== DATA TABLE CREATION ====================
    def create_data_table(self):
        """Create data display table with scrollbars"""
        # Create scrollbars
        scroll_x = ttk.Scrollbar(self.detailframe, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(self.detailframe, orient=VERTICAL)
        
        # Create table
        self.medicine_table = ttk.Treeview(
            self.detailframe,
            columns=("Medicine ID", "Medicine Name", "Category", "Manufacturer", "Batch No", "Expiry Date", "Manufacture Date",
                    "Quantity", "Unit", "Min Stock Level", "Max Stock Level", "Reorder Level",
                    "Cost Price", "Selling Price", "Discount", "Supplier", "Supplier Contact",
                    "Location", "Storage Condition", "Purchase Date"),
            show="headings",
            xscrollcommand=scroll_x.set,
            yscrollcommand=scroll_y.set)
        
        # Position scrollbars
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        
        # Configure scrollbar commands
        scroll_x.config(command=self.medicine_table.xview)
        scroll_y.config(command=self.medicine_table.yview)
        
        # Configure table columns
        for col in ("Medicine ID", "Medicine Name", "Category", "Manufacturer", "Batch No", "Expiry Date", "Manufacture Date",
                   "Quantity", "Unit", "Min Stock Level", "Max Stock Level", "Reorder Level",
                   "Cost Price", "Selling Price", "Discount", "Supplier", "Supplier Contact",
                   "Location", "Storage Condition", "Purchase Date"):
            self.medicine_table.heading(col, text=col)
            self.medicine_table.column(col, width=100)
        
        self.medicine_table.pack(fill=BOTH, expand=1)
    
    # ==================== SMOOTH SCROLLING SETUP ====================
    def setup_scrolling(self):
        """Setup smooth scrolling functionality"""
        self.scroll_momentum = 0
        self.scroll_timer = None
        
        def smooth_scroll_vertical(event):
            delta = int(-1 * (event.delta / 120))
            for i in range(abs(delta)):
                if delta > 0:
                    self.medicine_table.yview_scroll(1, "units")
                else:
                    self.medicine_table.yview_scroll(-1, "units")
                self.root.update_idletasks()
        
        def smooth_scroll_horizontal(event):
            delta = int(-1 * (event.delta / 120))
            for i in range(abs(delta)):
                if delta > 0:
                    self.medicine_table.xview_scroll(1, "units")
                else:
                    self.medicine_table.xview_scroll(-1, "units")
                self.root.update_idletasks()
        
        def momentum_scroll():
            if abs(self.scroll_momentum) > 0.1:
                self.medicine_table.yview_scroll(int(self.scroll_momentum), "units")
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
                self.medicine_table.yview_scroll(-1, "units")
            elif key == "Down":
                self.medicine_table.yview_scroll(1, "units")
            elif key == "Left":
                self.medicine_table.xview_scroll(-1, "units")
            elif key == "Right":
                self.medicine_table.xview_scroll(1, "units")
        
        # Bind scroll events
        self.medicine_table.bind("<MouseWheel>", smooth_scroll_vertical)
        self.medicine_table.bind("<Shift-MouseWheel>", smooth_scroll_horizontal)
        self.medicine_table.bind("<Control-MouseWheel>", on_mousewheel_momentum)
        self.medicine_table.bind("<Key>", smooth_key_scroll)
        self.medicine_table.focus_set()
    
    # ==================== DATABASE OPERATIONS ====================
    def save_data(self):
        """Save medicine data to database"""
        if not self.validate_required_fields():
            return
        
        conn = None
        try:
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="medicineData")
            
            cursor = conn.cursor()
            cursor.execute("INSERT INTO medicines VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (
                self.MedicineId.get(), self.MedicineName.get(), self.Category.get(), self.Manufacturer.get(),
                self.BatchNo.get(), self.ExpiryDate.get(), self.ManufactureDate.get(), self.Quantity.get(),
                self.Unit.get(), self.MinStockLevel.get(), self.MaxStockLevel.get(), self.ReorderLevel.get(),
                self.CostPrice.get(), self.SellingPrice.get(), self.Discount.get(), self.Supplier.get(),
                self.SupplierContact.get(), self.Location.get(), self.StorageCondition.get(), self.PurchaseDate.get()))
            
            conn.commit()
            messagebox.showinfo("Success", "Medicine record saved successfully")
        
        except mysql.connector.Error:
            messagebox.showerror("Error", "Database operation failed")
        
        finally:
            if conn and conn.is_connected():
                conn.close()
    
    def validate_required_fields(self):
        """Validate that required fields are filled"""
        if not all([self.MedicineId.get(), self.MedicineName.get(), self.Quantity.get(), self.ExpiryDate.get()]):
            messagebox.showerror("Error", "All required fields must be filled")
            return False
        return True
    
    # ==================== UTILITY METHODS ====================
    def clear_fields(self):
        """Clear all input fields"""
        variables = [self.MedicineId, self.MedicineName, self.Category, self.Manufacturer, self.BatchNo,
                    self.ExpiryDate, self.ManufactureDate, self.Quantity, self.Unit, self.MinStockLevel,
                    self.MaxStockLevel, self.ReorderLevel, self.CostPrice, self.SellingPrice, self.Discount,
                    self.Supplier, self.SupplierContact, self.Location, self.StorageCondition, self.PurchaseDate]
        
        for var in variables:
            var.set("")
        
        self.txtmedicine.delete(1.0, END)


# ==================== MAIN EXECUTION ====================
if __name__ == "__main__":
    root = Tk()
    app = MedicinalStock(root)
    root.mainloop()