from tkinter import *
from PIL import Image, ImageTk  # pip install pillow
from tkinter import ttk, messagebox
import random
from customer_dialog import cust__Win

class cust__Win:
    def __init__(self, root):
        self.root = root
        self.root.title("HOTEL MANAGEMENT SYSTEM")
        self.root.geometry("1295x570+235+220")
        self.root.resizable(False, False)

        # Variables
        self.var_ref = StringVar()
        self.var_cust_name = StringVar()
        self.var_mother = StringVar()
        self.var_gender = StringVar()
        self.var_post = StringVar()
        self.var_mobile = StringVar()
        self.var_email = StringVar()
        self.var_nationality = StringVar()
        self.var_idproof = StringVar()
        self.var_idnumber = StringVar()
        self.var_address = StringVar()

        # Title
        lbl_title = Label(
            self.root,
            text="ADD CUSTOMER DETAILS",
            font=("times new roman", 18, "bold"),
            bg="black",
            fg="gold",
            bd=4,
            relief=RIDGE,
        )
        lbl_title.place(x=0, y=0, width=1295, height=50)

        # Logo
        img2 = Image.open("resources/images/logo2.jpg")
        self.photoimg2 = ImageTk.PhotoImage(img2)
        Label(self.root, image=self.photoimg2, bd=0, relief=RIDGE).place(x=5, y=2, width=100, height=40)

        # Left Frame
        left_frame = LabelFrame(
            self.root,
            bd=2,
            relief=RIDGE,
            text="CUSTOMER DETAILS",
            padx=2,
            font=("times new roman", 12, "bold"),
        )
        left_frame.place(x=5, y=50, width=425, height=490)

        # Customer Ref
        Label(left_frame, text="CUSTOMER REF", font=("arial", 12, "bold")).grid(row=0, column=0, sticky=W)
        entry_ref = ttk.Entry(left_frame, textvariable=self.var_ref, width=29, font=("arial", 13, "bold"), justify=CENTER, state='readonly')
        entry_ref.grid(row=0, column=1)

        # Generate ref
        self.reset()

        # Name
        Label(left_frame, text="CUSTOMER NAME", font=("arial", 12, "bold")).grid(row=1, column=0, sticky=W)
        ttk.Entry(left_frame, textvariable=self.var_cust_name, width=29, font=("arial", 13, "bold"), justify=CENTER).grid(row=1, column=1)

        # Mother Name
        Label(left_frame, text="MOTHER NAME", font=("arial", 12, "bold")).grid(row=2, column=0, sticky=W)
        ttk.Entry(left_frame, textvariable=self.var_mother, width=29, font=("arial", 13, "bold"), justify=CENTER).grid(row=2, column=1)

        # Gender
        Label(left_frame, text="GENDER", font=("arial", 12, "bold")).grid(row=3, column=0, sticky=W)
        combo_gender = ttk.Combobox(left_frame, textvariable=self.var_gender, values=("Male", "Female", "Other"), state="readonly", width=27, font=("arial", 12, "bold"))
        combo_gender.current(0)
        combo_gender.grid(row=3, column=1)

        # Postcode
        Label(left_frame, text="POSTCODE", font=("arial", 12, "bold")).grid(row=4, column=0, sticky=W)
        ttk.Entry(left_frame, textvariable=self.var_post, width=29, font=("arial", 13, "bold"), justify=CENTER).grid(row=4, column=1)

        # Mobile
        Label(left_frame, text="MOBILE", font=("arial", 12, "bold")).grid(row=5, column=0, sticky=W)
        ttk.Entry(left_frame, textvariable=self.var_mobile, width=29, font=("arial", 13, "bold"), justify=CENTER).grid(row=5, column=1)

        # Email
        Label(left_frame, text="EMAIL", font=("arial", 12, "bold")).grid(row=6, column=0, sticky=W)
        ttk.Entry(left_frame, textvariable=self.var_email, width=29, font=("arial", 13, "bold"), justify=CENTER).grid(row=6, column=1)

        # Nationality
        Label(left_frame, text="NATIONALITY", font=("arial", 12, "bold")).grid(row=7, column=0, sticky=W)
        combo_nationality = ttk.Combobox(left_frame, textvariable=self.var_nationality, values=("Indian", "American", "British", "Other"), state="readonly", width=27, font=("arial", 12, "bold"))
        combo_nationality.current(0)
        combo_nationality.grid(row=7, column=1)

        # ID Proof
        Label(left_frame, text="ID PROOF TYPE", font=("arial", 12, "bold")).grid(row=8, column=0, sticky=W)
        combo_id = ttk.Combobox(left_frame, textvariable=self.var_idproof, values=("Aadhar Card", "Driving Licence", "Passport", "PAN Card"), state="readonly", width=27, font=("arial", 12, "bold"))
        combo_id.current(0)
        combo_id.grid(row=8, column=1)

        # ID Number
        Label(left_frame, text="ID NUMBER", font=("arial", 12, "bold")).grid(row=9, column=0, sticky=W)
        ttk.Entry(left_frame, textvariable=self.var_idnumber, width=29, font=("arial", 13, "bold"), justify=CENTER).grid(row=9, column=1)

        # Address
        Label(left_frame, text="ADDRESS", font=("arial", 12, "bold")).grid(row=10, column=0, sticky=W)
        ttk.Entry(left_frame, textvariable=self.var_address, width=29, font=("arial", 13, "bold"), justify=CENTER).grid(row=10, column=1)

        # Buttons
        btn_frame = Frame(left_frame, bd=2, relief=RIDGE)
        btn_frame.place(x=0, y=400, width=412, height=40)
        Button(btn_frame, text="ADD", command=self.add_data, width=9, font=("arial", 12, "bold"), bg="black", fg="gold").grid(row=0, column=0, padx=1)
        Button(btn_frame, text="UPDATE", command=self.update, width=9, font=("arial", 12, "bold"), bg="black", fg="gold").grid(row=0, column=1, padx=1)
        Button(btn_frame, text="DELETE", command=self.mDelete, width=9, font=("arial", 12, "bold"), bg="black", fg="gold").grid(row=0, column=2, padx=1)
        Button(btn_frame, text="RESET", command=self.reset, width=9, font=("arial", 12, "bold"), bg="black", fg="gold").grid(row=0, column=3, padx=1)

        # Table Frame
        table_frame = LabelFrame(self.root, bd=2, relief=RIDGE, text="VIEW DETAILS AND SEARCH SYSTEM", padx=2, font=("times new roman", 12, "bold"))
        table_frame.place(x=435, y=50, width=860, height=490)
        Scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        Scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)
        self.cust_table = ttk.Treeview(table_frame, columns=("ref","name","mother","gender","post","mobile","email","nationality","idproof","idnumber","address"), xscrollcommand=Scroll_x.set, yscrollcommand=Scroll_y.set)
        Scroll_x.pack(side=BOTTOM, fill=X)
        Scroll_y.pack(side=RIGHT, fill=Y)
        Scroll_x.config(command=self.cust_table.xview)
        Scroll_y.config(command=self.cust_table.yview)
        headings = ["Ref","Name","Mother","Gender","Post","Mobile","Email","Nationality","ID Proof","ID Number","Address"]
        for col, head in zip(self.cust_table["columns"], headings):
            self.cust_table.heading(col, text=head)
            self.cust_table.column(col, width=100)
        self.cust_table.pack(fill=BOTH, expand=1)
        self.cust_table.bind("<ButtonRelease-1>", self.get_cursor)

        self.fetch_data()

    def add_data(self):
        fields = (self.var_ref.get(), self.var_cust_name.get(), self.var_mother.get(), self.var_gender.get(),
                  self.var_post.get(), self.var_mobile.get(), self.var_email.get(), self.var_nationality.get(),
                  self.var_idproof.get(), self.var_idnumber.get(), self.var_address.get())
        if not all(fields[1:]):
            messagebox.showerror("Error", "All fields are required", parent=self.root)
            return
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO Customer (ref,name,mother,gender,post,mobile,email,nationality,idproof,idnumber,address) VALUES (?,?,?,?,?,?,?,?,?,?,?)",
            fields
        )
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", "Customer added successfully", parent=self.root)
        self.fetch_data()
        self.reset()

    def fetch_data(self):
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Customer")
        rows = cursor.fetchall()
        conn.close()
        self.cust_table.delete(*self.cust_table.get_children())
        for row in rows:
            self.cust_table.insert("", END, values=row)

    def get_cursor(self, event):
        item = self.cust_table.focus()
        values = self.cust_table.item(item, 'values')
        if values:
            (self.var_ref.set(values[0]), self.var_cust_name.set(values[1]), self.var_mother.set(values[2]),
             self.var_gender.set(values[3]), self.var_post.set(values[4]), self.var_mobile.set(values[5]),
             self.var_email.set(values[6]), self.var_nationality.set(values[7]), self.var_idproof.set(values[8]),
             self.var_idnumber.set(values[9]), self.var_address.set(values[10]))

    def update(self):
        if not self.var_ref.get():
            return
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE Customer SET name=?,mother=?,gender=?,post=?,mobile=?,email=?,nationality=?,idproof=?,idnumber=?,address=? WHERE ref=?",
            (self.var_cust_name.get(), self.var_mother.get(), self.var_gender.get(), self.var_post.get(),
             self.var_mobile.get(), self.var_email.get(), self.var_nationality.get(), self.var_idproof.get(),
             self.var_idnumber.get(), self.var_address.get(), self.var_ref.get())
        )
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", "Customer updated successfully", parent=self.root)
        self.fetch_data()
        self.reset()

    def mDelete(self):
        if not self.var_ref.get():
            return
        if messagebox.askyesno("Confirm", "Delete this customer?", parent=self.root):
            conn = connect_db()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM Customer WHERE ref=?", (self.var_ref.get(),))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success", "Customer deleted", parent=self.root)
            self.fetch_data()
            self.reset()

    def reset(self):
        self.var_cust_name.set("")
        self.var_mother.set("")
        self.var_gender.set("Male")
        self.var_post.set("")
        self.var_mobile.set("")
        self.var_email.set("")
        self.var_nationality.set("Indian")
        self.var_idproof.set("Aadhar Card")
        self.var_idnumber.set("")
        self.var_address.set("")
        self.var_ref.set(str(random.randint(1000,9999)))

if __name__ == "__main__":
    root = Tk()
    app = cust__Win(root)
    root.mainloop()
