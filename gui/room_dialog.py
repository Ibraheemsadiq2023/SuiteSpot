from tkinter import *
from PIL import Image, ImageTk  # pip install pillow
from tkinter import ttk, messagebox
from tkcalendar import Calendar
from database.db import connect_db

class Roombooking:
    def __init__(self, root):
        self.root = root
        self.root.title("HOTEL MANAGEMENT SYSTEM")
        self.root.geometry("1295x570+235+220")
        self.root.resizable(False, False)

        # Variables
        self.var_contact = StringVar()
        self.var_checkin = StringVar()
        self.var_checkout = StringVar()
        self.var_roomtype = StringVar()
        self.var_roomno = StringVar()
        self.var_meal = StringVar()
        self.var_noOfDays = StringVar()
        self.var_paidtax = StringVar()
        self.var_subTotal = StringVar()
        self.var_Total = StringVar()

        # Title
        lbl_title = Label(
            self.root,
            text="ROOM BOOKING DETAILS",
            font=("times new roman", 18, "bold"),
            bg="black",
            fg="gold",
            bd=4,
            relief=RIDGE,
        )
        lbl_title.place(x=0, y=0, width=1295, height=50)

        # Logo
        img2 = Image.open("Image/logo2.jpg")
        self.photoimg2 = ImageTk.PhotoImage(img2)
        labimg2 = Label(self.root, image=self.photoimg2, bd=0, relief=RIDGE)
        labimg2.place(x=5, y=2, width=100, height=40)

        # Left Frame
        left_frame = LabelFrame(
            self.root,
            bd=2,
            relief=RIDGE,
            text="ROOM BOOKING",
            padx=2,
            font=("times new roman", 12, "bold"),
        )
        left_frame.place(x=5, y=50, width=425, height=490)

        # Customer Contact
        Label(left_frame, text="Customer Contact", font=("arial", 12, "bold")).grid(row=0, column=0, sticky=W)
        entry_contact = ttk.Entry(
            left_frame,
            textvariable=self.var_contact,
            width=20,
            font=("arial", 13, "bold"),
            justify=CENTER,
        )
        entry_contact.grid(row=0, column=1)
        Button(
            left_frame,
            text="Fetch Data",
            command=self.fetch_contact,
            font=("arial", 10, "bold"),
            bg="black",
            fg="gold",
            cursor="hand2",
            width=8,
        ).place(x=340, y=4)

        # Check-in Date
        Label(left_frame, text="Check-In Date", font=("arial", 12, "bold")).grid(row=1, column=0, sticky=W)
        txt_checkin = ttk.Entry(left_frame, textvariable=self.var_checkin, width=29, font=("arial", 13, "bold"), justify=CENTER)
        txt_checkin.grid(row=1, column=1)
        txt_checkin.bind(
            "<Button-1>", lambda e: self.show_calendar(e, txt_checkin)
        )

        # Check-Out Date
        Label(left_frame, text="Check-Out Date", font=("arial", 12, "bold")).grid(row=2, column=0, sticky=W)
        txt_checkout = ttk.Entry(left_frame, textvariable=self.var_checkout, width=29, font=("arial", 13, "bold"), justify=CENTER)
        txt_checkout.grid(row=2, column=1)
        txt_checkout.bind(
            "<Button-1>", lambda e: self.show_calendar(e, txt_checkout)
        )

        # Room Type
        Label(left_frame, text="Room Type", font=("arial", 12, "bold")).grid(row=3, column=0, sticky=W)
        combo_room = ttk.Combobox(
            left_frame,
            textvariable=self.var_roomtype,
            values=("Single", "Double", "Luxury"),
            state="readonly",
            width=27,
            font=("arial", 12, "bold"),
        )
        combo_room.current(0)
        combo_room.grid(row=3, column=1)

        # Room No
        Label(left_frame, text="Room No", font=("arial", 12, "bold")).grid(row=4, column=0, sticky=W)
        ttk.Entry(left_frame, textvariable=self.var_roomno, width=29, font=("arial", 13, "bold"), justify=CENTER).grid(row=4, column=1)

        # Meal
        Label(left_frame, text="Meal", font=("arial", 12, "bold")).grid(row=5, column=0, sticky=W)
        combo_meal = ttk.Combobox(
            left_frame,
            textvariable=self.var_meal,
            values=("None", "Breakfast", "Lunch", "Dinner", "Water", "Juice", "Fast Food"),
            state="readonly",
            width=27,
            font=("arial", 13, "bold"),
        )
        combo_meal.current(0)
        combo_meal.grid(row=5, column=1)

        # No Of Days
        Label(left_frame, text="No Of Days", font=("arial", 12, "bold")).grid(row=6, column=0, sticky=W)
        ttk.Entry(left_frame, textvariable=self.var_noOfDays, width=29, font=("arial", 13, "bold"), justify=CENTER).grid(row=6, column=1)

        # Paid Tax, Subtotal, Total
        Label(left_frame, text="Paid Tax", font=("arial", 12, "bold")).grid(row=7, column=0, sticky=W)
        ttk.Entry(left_frame, textvariable=self.var_paidtax, width=29, font=("arial", 13, "bold"), justify=CENTER).grid(row=7, column=1)

        Label(left_frame, text="Sub Total", font=("arial", 12, "bold")).grid(row=8, column=0, sticky=W)
        ttk.Entry(left_frame, textvariable=self.var_subTotal, width=29, font=("arial", 13, "bold"), justify=CENTER).grid(row=8, column=1)

        Label(left_frame, text="Total", font=("arial", 12, "bold")).grid(row=9, column=0, sticky=W)
        ttk.Entry(left_frame, textvariable=self.var_Total, width=29, font=("arial", 13, "bold"), justify=CENTER).grid(row=9, column=1)

        # Buttons
        btn_frame = Frame(left_frame, bd=2, relief=RIDGE)
        btn_frame.place(x=0, y=400, width=412, height=40)
        Button(btn_frame, text="BILL", command=self.calculate_bill, width=9, font=("arial", 12, "bold"), bg="black", fg="gold").grid(row=0, column=0, padx=1)
        Button(btn_frame, text="ADD", command=self.add_customer_data, width=9, font=("arial", 12, "bold"), bg="black", fg="gold").grid(row=0, column=1, padx=1)
        Button(btn_frame, text="UPDATE", command=self.update, width=9, font=("arial", 12, "bold"), bg="black", fg="gold").grid(row=0, column=2, padx=1)
        Button(btn_frame, text="DELETE", command=self.mDelete, width=9, font=("arial", 12, "bold"), bg="black", fg="gold").grid(row=0, column=3, padx=1)

        # Right Image
        img3 = Image.open("Image/bed3.jpg")
        self.photoimg3 = ImageTk.PhotoImage(img3.resize((550, 300), Image.Resampling.LANCZOS))
        Label(self.root, image=self.photoimg3, bd=0, relief=RIDGE).place(x=760, y=55, width=550, height=300)

        # Table Frame
        table_frame = LabelFrame(self.root, bd=2, relief=RIDGE, text="VIEW DETAILS AND SEARCH SYSTEM", padx=2, font=("times new roman", 12, "bold"))
        table_frame.place(x=435, y=280, width=860, height=260)
        Scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        Scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)
        self.room_table = ttk.Treeview(
            table_frame,
            columns=("contact","checkin","checkout","room_type","roomno","meal","no_of_days","paid_tax","sub_total","total"),
            xscrollcommand=Scroll_x.set,
            yscrollcommand=Scroll_y.set,
        )
        Scroll_x.pack(side=BOTTOM, fill=X)
        Scroll_y.pack(side=RIGHT, fill=Y)
        Scroll_x.config(command=self.room_table.xview)
        Scroll_y.config(command=self.room_table.yview)
        for col, heading in zip(self.room_table["columns"], ["Contact","Check-in","Check-out","Room Type","Room No","Meal","No Of Days","Paid Tax","Sub Total","Total"]):
            self.room_table.heading(col, text=heading)
            self.room_table.column(col, width=100)
        self.room_table["show"] = "headings"
        self.room_table.pack(fill=BOTH, expand=1)
        self.room_table.bind("<ButtonRelease-1>", self.get_cursor)

        self.fetch_data()

    def show_calendar(self, event, entry):
        top = Toplevel(self.root)
        cal = Calendar(top, selectmode='day')
        cal.pack(fill='both', expand=True)
        cal.bind('<<CalendarSelected>>', lambda e: (entry.delete(0, END), entry.insert(END, cal.get_date()), top.destroy()))

    def fetch_contact(self):
        if not self.var_contact.get():
            messagebox.showerror("Error", "Enter Contact Number", parent=self.root)
            return
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Customer WHERE mobile=?", (self.var_contact.get(),))
        row = cursor.fetchone()
        conn.close()
        if not row:
            messagebox.showerror("Error", "Customer not found", parent=self.root)
            return
        # Display fetched customer details as before
        # ... (same UI code for labels)

    def add_customer_data(self):
        fields = [self.var_contact.get(), self.var_checkin.get(), self.var_checkout.get(),
                  self.var_roomtype.get(), self.var_roomno.get(), self.var_meal.get(),
                  self.var_noOfDays.get(), self.var_paidtax.get(), self.var_subTotal.get(), self.var_Total.get()]
        if not all(fields):
            messagebox.showerror("Error", "All fields are required", parent=self.root)
            return
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO room (contact, checkin, checkout, room_type, roomno, Meal, NoOfdays, paid_tax, sub_total, total) VALUES (?,?,?,?,?,?,?,?,?,?)",
            fields
        )
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", "Customer data added successfully", parent=self.root)
        self.fetch_data()
        self.reset()

    def calculate_bill(self):
        try:
            days = int(self.var_noOfDays.get())
        except ValueError:
            messagebox.showerror("Error", "Enter valid number of days", parent=self.root)
            return
        rates = {"Single":1500, "Double":3000, "Luxury":5000}
        subtotal = rates.get(self.var_roomtype.get(),0)*days
        meal_rates = {"Breakfast":1000, "Lunch":1500, "Dinner":2000, "Water":50, "Juice":200, "Fast Food":1500}
        meal_charge = meal_rates.get(self.var_meal.get(),0)
        tax = int((subtotal+meal_charge)*0.18)
        total = subtotal+meal_charge+tax
        self.var_paidtax.set(str(tax))
        self.var_subTotal.set(str(subtotal+meal_charge))
        self.var_Total.set(str(total))

    def fetch_data(self):
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM room")
        rows = cursor.fetchall()
        conn.close()
        self.room_table.delete(*self.room_table.get_children())
        for row in rows:
            self.room_table.insert("","end",values=row)

    def get_cursor(self, event):
        sel = self.room_table.focus()
        values = self.room_table.item(sel, 'values')
        if values:
            (self.var_contact.set(values[0]), self.var_checkin.set(values[1]), self.var_checkout.set(values[2]),
             self.var_roomtype.set(values[3]), self.var_roomno.set(values[4]), self.var_meal.set(values[5]),
             self.var_noOfDays.set(values[6]), self.var_paidtax.set(values[7]), self.var_subTotal.set(values[8]),
             self.var_Total.set(values[9]))

    def update(self):
        if not self.var_roomno.get():
            messagebox.showerror("Error", "Enter Room Number", parent=self.root)
            return
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE room SET contact=?, checkin=?, checkout=?, room_type=?, Meal=?, NoOfdays=?, paid_tax=?, sub_total=?, total=? WHERE roomno=?",
            (self.var_contact.get(), self.var_checkin.get(), self.var_checkout.get(), self.var_roomtype.get(),
             self.var_meal.get(), self.var_noOfDays.get(), self.var_paidtax.get(), self.var_subTotal.get(),
             self.var_Total.get(), self.var_roomno.get())
        )
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", "Data updated successfully", parent=self.root)
        self.fetch_data()
        self.reset()

    def mDelete(self):
        if not self.var_roomno.get():
            return
        if messagebox.askyesno("Confirm","Delete this record?", parent=self.root):
            conn = connect_db()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM room WHERE roomno=?", (self.var_roomno.get(),))
            conn.commit()
            conn.close()
            messagebox.showinfo("Deleted","Record deleted", parent=self.root)
            self.fetch_data()
            self.reset()

    def reset(self):
        for var in (self.var_contact, self.var_checkin, self.var_checkout, self.var_roomtype,
                    self.var_roomno, self.var_meal, self.var_noOfDays, self.var_paidtax,
                    self.var_subTotal, self.var_Total):
            var.set("")

if __name__ == "__main__":
    root=Tk()
    app=Roombooking(root)
    root.mainloop()

