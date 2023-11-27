from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import random
import time
import datetime
import sqlite3


class Hospital:
    def __init__(self, root):
        self.root = root
        self.root.title("Hospital Management System")
        self.root.geometry("1540x800+150+150")
        
        self.tablets = StringVar()
        self.ref = StringVar()
        self.Dose = StringVar()
        self.NumberofTablets = StringVar()
        self.Lot = StringVar()
        self.Issuedate = StringVar()
        self.ExpDate = StringVar()
        self.DailyDose = StringVar()
        self.sideEffect = StringVar()
        self.FurtherInformation = StringVar()
        self.StorageAdvice = StringVar()
        self.BloodPressure = StringVar() 
        self.HowToUseMedication = StringVar() 
        self.PatientId = StringVar() 
        self.insNumber = StringVar() 
        self.PatientName = StringVar() 
        self.DateofBirth = StringVar()
        self.PatientAddress = StringVar()
        
        
        lbltitle = Label(self.root, bd = 20, relief = RIDGE, text="+ Hospital Management System", fg="blue", bg="white", font=("time new roman", 50, "bold"))
        lbltitle.pack(side=TOP, fill=X)
        
        # ===========================================================Data Frame==========================================================================================
        Dataframe = Frame(self.root, bd = 20, relief = RIDGE)
        Dataframe.place(x = 0, y = 120, width = 1530, height = 400)
        
        DataframeLeft = LabelFrame(Dataframe, bd = 10, relief = RAISED, padx=20, font=("arial", 12, "bold"), text = "Patient Information")
        DataframeLeft.place(x = 15, y = 8, width = 980, height = 340)
        
        DataframeRight = LabelFrame(Dataframe, bd = 10, relief = RAISED, padx=20, font=("arial", 12, "bold"), text = "Prescription")
        DataframeRight.place(x =1005, y = 8, width = 470, height = 340)
        
        # ===========================================================Buttons Frame=======================================================================================
        Buttonframe = Frame(self.root, bd = 20, relief = FLAT)
        Buttonframe.place(x = 0, y = 530, width = 1530, height = 70)
        
        # ===========================================================Details Frame=======================================================================================
        Detailsframe = Frame(self.root, bd = 20, relief = RIDGE)
        Detailsframe.place(x = 0, y = 600, width = 1530, height = 190)
        
        # ===========================================================Data Frame Left=====================================================================================
        
        lblname = Label(DataframeLeft, text = "Tablets:", font = ("arial", 12, "bold"), padx = 2, pady = 6)
        lblname.grid(row = 0, column = 0, sticky = W, pady = (20, 0))
        txtname = Entry(DataframeLeft, textvariable = self.tablets, font = ("arial", 13, "bold"), width = 35)
        txtname.grid(row = 0, column = 1, pady = (20, 0))
        
        lblref = Label(DataframeLeft, font = ("arial", 12, "bold"), text = "Reference No:" , padx = 2)
        lblref.grid(row = 1, column = 0, sticky = W) 
        txtref = Entry(DataframeLeft, textvariable = self.ref, font = ("arial", 13, "bold"), width = 35)
        txtref.grid(row = 1, column = 1)
        
        lblDose = Label(DataframeLeft, font = ("arial", 12, "bold"), text="Dose:", padx = 2, pady = 4)
        lblDose.grid(row=2, column=0, sticky=W) 
        txtDose = Entry (DataframeLeft, textvariable = self.Dose, font = ("arial", 13, "bold"), width=35)
        txtDose.grid (row=2, column=1)
        
        lblNoOftablets = Label(DataframeLeft,font = ("arial",12,"bold"),text = "No Of Tablets:", padx = 2, pady = 6)
        lblNoOftablets.grid(row = 3,column = 0, sticky = W) 
        txtNoOftablets = Entry(DataframeLeft, textvariable = self.NumberofTablets, font = ("arial", 13, "bold"), width = 35)
        txtNoOftablets.grid(row = 3, column = 1)
        
        lblLot = Label (DataframeLeft, font = ("arial", 12, "bold"), text="Lot:", padx = 2, pady = 6)
        lblLot.grid(row = 4, column = 0, sticky = W) 
        txtLot = Entry(DataframeLeft, textvariable = self.Lot, font = ("arial", 13, "bold"), width = 35)
        txtLot.grid (row = 4, column = 1)

        lblissueDate = Label (DataframeLeft, font = ("arial", 12, "bold"), text = "Issue Date:", padx = 2, pady = 6) 
        lblissueDate.grid (row = 5, column = 0, sticky = W) 
        txtissueDate = Entry(DataframeLeft, textvariable = self.Issuedate, font = ("arial", 13, "bold"), width = 35)
        txtissueDate.grid (row = 5, column = 1)

        lblExpDate = Label (DataframeLeft, font = ("arial", 12, "bold"), text = "Exp Date:", padx = 2, pady = 6)
        lblExpDate.grid(row = 6, column = 0, sticky = W) 
        txtExpDate = Entry (DataframeLeft, textvariable = self.ExpDate, font = ("arial", 13, "bold"), width = 35)
        txtExpDate.grid(row = 6, column = 1)
        
        lblDailyDose = Label (DataframeLeft, font = ("arial", 12, "bold"), text = "Daily Dose:", padx = 2, pady = 4)
        lblDailyDose.grid(row = 7, column = 0, sticky = W) 
        txtDailyDose = Entry (DataframeLeft, textvariable = self.DailyDose, font = ("arial", 13, "bold"), width = 35)
        txtDailyDose.grid(row = 7, column = 1)
        
        lblSideEffect = Label(DataframeLeft, font = ("arial", 12, "bold"), text = "Side Effect:", padx=2, pady=6)
        lblSideEffect.grid(row = 8, column = 0, sticky  = W) 
        txtSideEffect = Entry(DataframeLeft, textvariable = self.sideEffect, font = ("arial", 13, "bold"), width = 35)
        txtSideEffect.grid(row = 8, column = 1)
        
        lblFurtherinfo = Label(DataframeLeft, font = ("arial", 12, "bold"), text = "Further Information:", padx=2)
        lblFurtherinfo.grid(row = 0, column = 2, sticky = W, padx = (50, 0), pady = (20, 0)) 
        txtFurtherinfo = Entry(DataframeLeft, textvariable = self.FurtherInformation, font = ("arial", 12, "bold"), width = 35)
        txtFurtherinfo.grid(row = 0, column = 3, pady = (20, 0))
        
        lblBloodPressure = Label(DataframeLeft, font = ("arial", 12, "bold"), text = "Blood Pressure", padx = 2, pady = 6)
        lblBloodPressure.grid(row = 1, column = 2, sticky = W, padx = (50, 0)) 
        txtBloodPressure = Entry(DataframeLeft, textvariable = self.BloodPressure, font = ("arial", 12, "bold"), width = 35)
        txtBloodPressure. grid(row = 1, column = 3)
    
        lblStorage = Label(DataframeLeft, font = ("arial",12,"bold"), text = "Storage Advice:",padx = 2, pady = 6)
        lblStorage.grid(row = 2, column = 2,sticky = W, padx = (50, 0)) 
        txtStorage = Entry (DataframeLeft, textvariable = self.StorageAdvice, font = ("arial", 12, "bold"), width = 35)
        txtStorage.grid(row = 2, column = 3)
        
        lblMedicine = Label(DataframeLeft, font = ("arial", 12, "bold"), text = "Medication:", padx = 2, pady = 6)
        lblMedicine.grid(row = 3, column = 2,sticky = W, padx = (50, 0)) 
        txtMedicine = Entry(DataframeLeft, textvariable = self.HowToUseMedication, font = ("arial", 12, "bold"), width = 35)
        txtMedicine.grid(row = 3, column = 3, sticky=W) 
        
        lblPatientId = Label(DataframeLeft,font = ("arial",12,"bold"),text = "Patient Id:", padx = 2, pady = 6)
        lblPatientId.grid(row = 4, column = 2,sticky = W, padx = (50, 0)) 
        txtPatientId = Entry(DataframeLeft, textvariable = self.PatientId, font = ("arial", 12, "bold"), width = 35)
        txtPatientId.grid(row = 4, column = 3)
        
        lblInsNumber = Label(DataframeLeft, font = ("arial", 12, "bold") , text = "Insurance Number:", padx = 2, pady = 6) 
        lblInsNumber.grid (row = 5, column = 2, sticky = W, padx = (50, 0)) 
        txtInsNumber = Entry(DataframeLeft, textvariable = self.insNumber, font = ("arial", 12, "bold"), width = 35)
        txtInsNumber.grid (row = 5, column = 3)
        
        lblPatientname = Label(DataframeLeft, font = ("arial", 12, "bold"), text = "Patient Name:", padx = 2, pady = 6)
        lblPatientname.grid(row = 6, column = 2,sticky = W, padx = (50, 0)) 
        txtPatientname = Entry(DataframeLeft, textvariable = self.PatientName, font = ("arial", 12, "bold") ,width = 35)
        txtPatientname.grid(row = 6, column = 3) 
        
        lblDateofBirth = Label(DataframeLeft,font = ("arial",12,"bold"), text = "Date Of Birth:", padx = 2, pady = 6)
        lblDateofBirth.grid(row = 7,column = 2,sticky = W, padx = (50, 0)) 
        txtDateofBirth = Entry (DataframeLeft, textvariable = self.DateofBirth, font = ("arial", 12, "bold") ,width = 35)
        txtDateofBirth.grid(row = 7, column = 3)
        
        lblPatientAddress = Label(DataframeLeft, font = ("arial", 12, "bold"), text = "Patient Address", padx = 2, pady = 6)
        lblPatientAddress.grid(row = 8,column = 2,sticky = W, padx = (50, 0)) 
        txtPatientAddress = Entry(DataframeLeft, textvariable = self.PatientAddress, font = ("arial", 12, "bold") , width = 35)
        txtPatientAddress.grid(row = 8, column = 3)
        
        # ===========================================================Data Frame Right====================================================================================
        
        self.txtPrescription = Text(DataframeRight, font = ("arial", 12, "bold"), width = 58, height = 20, padx = 1, pady = 6)
        self.txtPrescription.grid(row = 0, column = 0, pady = (6, 0))
        
        # ===========================================================Buttons=============================================================================================
        
        btnPrescription = Button(Buttonframe, command = self.iPrescription, text = "Prescription", font = ("arial", 12, "bold"), width = 23, padx = 2, pady = 6)
        btnPrescription.grid(row = 0, column = 0, padx = (20, 0))
        
        btnPrescriptionData = Button(Buttonframe, command = self.iPrescriptionData, text = "Prescription Data", font = ("arial", 12, "bold"), width = 23, padx = 2, pady = 6)
        btnPrescriptionData.grid(row = 0, column = 1, padx = (50, 50))
        
        btnUpdate = Button(Buttonframe, command = self.update, text = "Update", font = ("arial", 12, "bold"), width = 23, padx = 2, pady = 6)
        btnUpdate.grid(row = 0, column = 2, padx = (0, 50))
        
        btnDelete = Button(Buttonframe, command = self.idelete, text = "Delete", font = ("arial", 12, "bold"), width = 23, padx = 2, pady = 6)
        btnDelete.grid(row = 0, column = 3, padx = (0, 50))
        
        btnClear = Button(Buttonframe, command = self.clear, text = "Clear", font = ("arial", 12, "bold"), width = 23, padx = 2, pady = 6)
        btnClear.grid(row = 0, column = 4, padx = (0, 50))
        
        btnExit = Button(Buttonframe, command = self.iExit, text = "Exit", font = ("arial", 12, "bold"), width = 23, padx = 2, pady = 6)
        btnExit.grid(row = 0, column = 5)
        
        # ===========================================================Table===============================================================================================
        
        # ==============Scroll Bar==============
        scroll_x = ttk.Scrollbar(Detailsframe, orient = HORIZONTAL)
        scroll_y = ttk.Scrollbar(Detailsframe, orient = VERTICAL)
        
        self.hospital_table = ttk.Treeview(Detailsframe, columns = ("Tablets", "ref", "dose", "nooftablets", "lot", "issuedate", 
                                                                 "expdate", "dailydose","storage", "insnumber", 
                                                                 "pname", "dob", "address"), xscrollcommand = scroll_x.set, yscrollcommand = scroll_y.set)
        
        scroll_x.pack(side = BOTTOM, fill = X)
        scroll_y.pack(side = RIGHT, fill = Y)
        
        scroll_x = ttk.Scrollbar(command = self.hospital_table.xview)
        scroll_y = ttk.Scrollbar(command = self.hospital_table.yview)
        
        self.hospital_table.heading("Tablets", text = "List of Tablets")
        self.hospital_table.heading("ref", text="Reference No.") 
        self.hospital_table.heading("dose", text="Dose") 
        self.hospital_table.heading("nooftablets",text="No Of Tablets") 
        self.hospital_table.heading("lot", text="Lot") 
        self.hospital_table.heading("issuedate", text="Issue Date") 
        self.hospital_table.heading("expdate", text="Exp Date") 
        self.hospital_table.heading("dailydose",text="Daily Dose") 
        self.hospital_table.heading("storage", text="Storage") 
        self.hospital_table.heading("insnumber", text="Insurance Number") 
        self.hospital_table.heading("pname", text="Patient Name") 
        self.hospital_table.heading("dob", text="Date Of Birth")
        self.hospital_table.heading("address", text="Patient Address")
        
        self.hospital_table["show"]="headings"
        
        self.hospital_table.pack(fill = BOTH, expand = 1)
        
        self.hospital_table.column("Tablets", width = 100)
        self.hospital_table.column("ref", width=100)
        self.hospital_table.column("dose", width=100)
        self.hospital_table.column("nooftablets", width=100)
        self.hospital_table.column("lot", width=100) 
        self.hospital_table.column("issuedate", width=100)
        self.hospital_table.column("expdate", width=100) 
        self.hospital_table.column("dailydose", width=100) 
        self.hospital_table.column("storage", width=100) 
        self.hospital_table.column("insnumber", width=100)
        self.hospital_table.column("pname", width=100) 
        self.hospital_table.column("dob", width=100)
        self.hospital_table.column("address", width=100)
        
        self.hospital_table.pack(fill=BOTH, expand=1)
        self.hospital_table.bind("<ButtonRelease-1>", self.get_cursor)
        self.fetch_data()
        
        
    # ==============Functionality Declaration==============
        
    def iPrescriptionData(self):
            
            if self.tablets.get() == "" or self.ref.get() == "":
                messagebox.showerror("Missing Field(s)", "All fields are required")
            else:
                conn = sqlite3.connect("hospital.db")
                cursor = conn.cursor()
                cursor.execute("insert into hospitalData values (?,?,?,?,?,?,?,?,?,?,?,?,?)", (
                                                                                                self.tablets.get(),
                                                                                                self.ref.get(),
                                                                                                self.Dose.get(),
                                                                                                self.NumberofTablets.get(),
                                                                                                self.Lot.get(),
                                                                                                self.Issuedate.get(),
                                                                                                self.ExpDate.get(),
                                                                                                self.DailyDose.get(),
                                                                                                self.StorageAdvice.get(),
                                                                                                self.insNumber.get(),
                                                                                                self.PatientName.get(),
                                                                                                self.DateofBirth.get(),
                                                                                                self.PatientAddress.get()
                                                                                                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "Record has been inserted")
    
    
    def update(self):
        conn = sqlite3.connect("hospital.db")
        cursor = conn.cursor()
        cursor.execute("update hospitalData set Tablets=?, dose=?, nooftablets=?, lot=?, issuedate=?, expdate=?, dailydose=?, storage=?, insnumber=?, pname=?, dob=?, paddress=? where ref=?", (
                                                                                                self.tablets.get(),
                                                                                                self.Dose.get(),
                                                                                                self.NumberofTablets.get(),
                                                                                                self.Lot.get(),
                                                                                                self.Issuedate.get(),
                                                                                                self.ExpDate.get(),
                                                                                                self.DailyDose.get(),
                                                                                                self.StorageAdvice.get(),
                                                                                                self.insNumber.get(),
                                                                                                self.PatientName.get(),
                                                                                                self.DateofBirth.get(),
                                                                                                self.PatientAddress.get(), 
                                                                                                self.ref.get()
                                                                                                ))
        conn.commit()
        self.fetch_data()
        conn.close()
        messagebox.showinfo("Success", "Record has been updated")
                
                                                                                                            
    def fetch_data(self):
        
        conn = sqlite3.connect("hospital.db")
        cursor = conn.cursor()
        cursor.execute("select * from hospitalData")
        rows = cursor.fetchall()
        
        if len(rows) > 0:
            self.hospital_table.delete(*self.hospital_table.get_children())
            
            for i in rows:
                self.hospital_table.insert("", END, values = i)
            
            conn.commit()
            
        conn.close() 
    
    
    def get_cursor(self, event = ""):
        
        cursor_row = self.hospital_table.focus()
        content = self.hospital_table.item(cursor_row)
        
        row = content["values"]
        self.tablets.set(row[0])
        self.ref.set(row[1]),
        self.Dose.set(row[2]),
        self.NumberofTablets.set(row[3]),
        self.Lot.set(row[4]),
        self.Issuedate.set(row[5]),
        self.ExpDate.set(row[6]),
        self.DailyDose.set(row[7]),
        self.StorageAdvice.set(row[8]),
        self.insNumber.set(row[9]),
        self.PatientName.set(row[10]),
        self.DateofBirth.set(row[11]),
        self.PatientAddress.set(row[12])
        
    
    def iPrescription(self):
        self.txtPrescription.insert(END, "Tablets:\t\t\t" + self.tablets.get() + "\n")
        self.txtPrescription.insert(END, "Rerefence No:\t\t\t" + self.ref.get() + "\n")
        self.txtPrescription.insert(END, "Dose:\t\t\t" + self.Dose.get() + "\n")
        self.txtPrescription.insert(END, "No. of Tablets:\t\t\t" + self.NumberofTablets.get() + "\n")
        self.txtPrescription.insert(END, "Lot:\t\t\t" + self.Lot.get() + "\n")
        self.txtPrescription.insert(END, "Issue Date:\t\t\t" + self.Issuedate.get() + "\n")
        self.txtPrescription.insert(END, "Expiry Date:\t\t\t" + self.ExpDate.get() + "\n")
        self.txtPrescription.insert(END, "Daily Dose:\t\t\t" + self.DailyDose.get() + "\n")
        self.txtPrescription.insert(END, "Side Effect:\t\t\t" + self.sideEffect.get() + "\n")
        self.txtPrescription.insert(END, "Further Information:\t\t\t" + self.FurtherInformation.get() + "\n")
        self.txtPrescription.insert(END, "Storage Advice:\t\t\t" + self.StorageAdvice.get() + "\n")
        self.txtPrescription.insert(END, "Blood Pressure:\t\t\t" + self.BloodPressure.get() + "\n")
        self.txtPrescription.insert(END, "Patient ID:\t\t\t" + self.PatientId.get() + "\n")
        self.txtPrescription.insert(END, "Insurance Number:\t\t\t" + self.insNumber.get() + "\n")
        self.txtPrescription.insert(END, "Patient Name:\t\t\t" + self.PatientName.get() + "\n")
        self.txtPrescription.insert(END, "Date of Birth:\t\t\t" + self.DateofBirth.get() + "\n")
        self.txtPrescription.insert(END, "Patient Address:\t\t\t" + self.PatientAddress.get() + "\n")
        
    
    def idelete(self):
        conn = sqlite3.connect("hospital.db")
        cursor = conn.cursor()
        query = "delete from hospitalData where ref=?"
        value = (self.ref.get(),)
        cursor.execute(query, value)
        
        conn.commit()
        self.fetch_data()
        conn.close()
        messagebox.showinfo("Success", "Record has been deleted")
        
    
    def clear(self):
        
        self.tablets.set("")
        self.ref.set("")
        self.Dose.set("")
        self.NumberofTablets.set("")
        self.Lot.set("")
        self.Issuedate.set("")
        self.ExpDate.set("")
        self.DailyDose.set("")
        self.sideEffect.set("")
        self.FurtherInformation.set("")
        self.StorageAdvice.set("")
        self.BloodPressure.set("") 
        self.HowToUseMedication.set("") 
        self.PatientId.set("") 
        self.insNumber.set("") 
        self.PatientName.set("") 
        self.DateofBirth.set("")
        self.PatientAddress.set("")  
        self.txtPrescription.delete("1.0", END)       
        
    
    def iExit(self):
        iExit = messagebox.askyesno("Hospital Management System", "Are you sure you want to exit?") 
        
        if iExit > 0:
            root.destroy()
            return
        
             

root = Tk()
ob = Hospital(root)
root.mainloop()