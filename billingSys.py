from tkinter import *
from tkinter import ttk
from tkinter import messagebox

def showMessage(msg):
    messagebox.showerror('Error',msg)

def ViewBillActionCommand(getBillRef,chkTxtCond,prevWin):
#def ViewBillActionCommand(getBillRef,prevWin):
    prevWin.destroy()
    f2=Tk()
    f2.title('View Bill')
    """menu=Menu(f2)
    f2.config(menu=menu)
    filemenu=Menu(f2,tearoff=0)
    menu.add_cascade(label='File',menu=filemenu)
    filemenu.add_command(label='Create Bill',command=BillActionCommand)"""
    fr=Frame(f2,width=500,height=50,bg='Grey')
    fr.propagate(0)
    billrefcode=StringVar()

    lblSrNoDate=Label
    lblCustNameData=Label
    lblBillDateData=Label
    lblBillRefData=Label
    lblItemNameData=Label
    lblRateData=Label
    lblQuantityData=Label
    lblAmountData=Label
    lblTotalAmountData=Label

    def previewBill():
        try:
            obj.execute('SELECT * from billdata where billref = '+txtBillref.get())
            data=obj.fetchall()
            sr=''
            bd=''
            cn=''
            br=''
            In=''
            r=''
            q=''
            a=''
            ta=''
            for i in range(len(data)):
                sr=sr+str(i+1)+'\n'
                br=data[i][1]
                bd=data[i][2]
                cn=data[i][3]
                In=In+data[i][4]+'\n'
                r=r+data[i][5]+'\n'
                q=q+data[i][6]+'\n'
                a=a+data[i][7]+'\n'
                ta=data[i][8]
        
            lblSrNoDate.config(text=sr)
            lblCustNameData.config(text=cn)
            lblBillDateData.config(text=bd)
            lblBillRefData.config(text=br)
            lblItemNameData.config(text=In)
            lblRateData.config(text=r)
            lblQuantityData.config(text=q)
            lblAmountData.config(text=a)
            lblTotalAmountData.config(text=ta)
        except Exception as e:
            showMessage(str(e))

    def func(event):
        previewBill()

    lblBillref=Label(text='Bill reference :',bg='white',font=('Arial',10))
    txtBillref=Entry(fr,width=25,bg='white',font=('Arial',10), textvariable=billrefcode)
    billrefcode.set(getBillRef)
    btnViewBill=Button(fr,command=previewBill,text='View Bill',width=10)
    if(chkTxtCond is 0):
        txtBillref.config(state='normal')
    elif(chkTxtCond is 1):
        txtBillref.config(state='disable')
        btnViewBill.config(state='disable')
        f2.bind('<Enter>',func)
        #f2.bind(lambda: previewBill())
        #btnViewBill.config(command=previewBill)
        #btnViewBill.connect('clicked',previewBill)
    lblBillref.place(x=20,y=20)
    txtBillref.place(x=150,y=20)
    btnViewBill.place(x=375,y=20)
    fr.pack()
    
    c=Canvas(f2,bg='White',width=500,height=450)
    id=c.create_rectangle(40,60,450,20,outline='black')
    lblBillTitle=Label(text='INVOICE',font=('Arial',15),bg='white')
    lblBillTitle.place(x=195,y=75)
    id=c.create_rectangle(40,110,450,60,outline='black')
    lblCustNamePrompt=Label(text='Customer Name :',font=('Arial',9),bg='white')
    lblCustNamePrompt.place(x=45,y=115)
    lblCustNameData=Label(font=('Arial',9),bg='white')
    lblCustNameData.place(x=150,y=115)
    lblBillDatePrompt=Label(bg='white',text='Bill Date :',font=('Arial',9))
    lblBillDatePrompt.place(x=45,y=135)
    lblBillDateData=Label(bg='white',font=('Arial',9))
    lblBillDateData.place(x=150,y=135)
    lblBillRefPrompt=Label(bg='white',text='Bill Ref. :',font=('Arial',9))
    lblBillRefPrompt.place(x=260,y=115)
    lblBillRefData=Label(bg='white',font=('Arial',9))
    lblBillRefData.place(x=310,y=115)
    id=c.create_rectangle(40,110,65,380,outline='black')
    id=c.create_rectangle(65,110,320,380,outline='black')
    id=c.create_rectangle(320,110,370,380,outline='black')
    id=c.create_rectangle(370,110,400,380,outline='black')
    id=c.create_rectangle(400,110,450,380,outline='black')
    id=c.create_rectangle(40,110,450,135,outline='black')
    lblSrNoPrompt=Label(bg='white',text='Sr.',font=('Arial',9))
    lblSrNoPrompt.place(x=42.5,y=162.5)
    lblItemNamePrompt=Label(bg='white',text='Item Name',font=('Arial',9))
    lblItemNamePrompt.place(x=160.5,y=162.5)
    lblRatePrompt=Label(bg='white',text='Rate',font=('Arial',9))
    lblRatePrompt.place(x=328.5,y=162.5)
    lblQuantityPrompt=Label(bg='white',text='Qty.',font=('Arial',9))
    lblQuantityPrompt.place(x=372.5,y=162.5)
    lblAmountPrompt=Label(bg='white',text='Amount',font=('Arial',9))
    lblAmountPrompt.place(x=400.5,y=162.5)
    lblSrNoDate=Label(bg='white',font=('Arial',9))
    lblSrNoDate.place(x=42.5,y=185.5)
    lblItemNameData=Label(bg='white',font=('Arial',9))
    lblItemNameData.place(x=68.5,y=185.5)
    lblRateData=Label(bg='white',font=('Arial',9))
    lblRateData.place(x=328.5,y=185.5)
    lblQuantityData=Label(bg='white',font=('Arial',9))
    lblQuantityData.place(x=372.5,y=185.5)
    lblAmountData=Label(bg='white',font=('Arial',9))
    lblAmountData.place(x=400.5,y=185.5)
    id=c.create_rectangle(40,380,400,405,outline='black')
    lblTotalAmountPrompt=Label(bg='white',text='Total Amount',font=('Arial',9))
    lblTotalAmountPrompt.place(x=317.5,y=432.5)
    id=c.create_rectangle(400,380,450,405)
    lblTotalAmountData=Label(bg='white',font=('Arial',9))
    lblTotalAmountData.place(x=402.5,y=432.5)
    c.pack()

    

    f2.geometry('500x500')
    f2.mainloop()

def BillActionCommand():
    root.destroy()
    f1=Tk()
    f1.title('Create Bill')
    f1.geometry('500x500')
    menu=Menu(f1)
    f1.config(menu=menu)
    filemenu=Menu(f1,tearoff=0)
    menu.add_cascade(label='File',menu=filemenu)
    filemenu.add_command(label='View Bill',command=lambda: ViewBillActionCommand('',0,f1))
    fr=Frame(f1,width=500,height=500,bg='white')
    fr.propagate(0)
    fr.pack()

    obj.execute('SELECT ItemName from itemsinvent')
    menList=obj.fetchall()
    menList=[''.join(x) for x in menList]
    var=StringVar()
    quant=StringVar()
    rateinp=[]
    listItemDet=[]
    

    tree=ttk.Treeview(height=5,columns=4)
    tree.place(x=60,y=285)
    tree['show'] = 'headings'
    tree['columns']=('Item Name','Rate','Quantity','Amount')
    tree.heading('Item Name',text='Item Name')
    tree.heading('Rate',text='Rate')
    tree.heading('Quantity',text='Quantity')
    tree.heading('Amount',text='Amount')
    tree.column('Item Name', width=100)
    tree.column('Rate', width=80)
    tree.column('Quantity', width=80)
    tree.column('Amount', width=80)
    ysb = ttk.Scrollbar( orient='vertical', command=tree.yview)
    #.grid(row=0, column=0, sticky='nsew')
    ysb.place(x=400,y=305,height=108)
    tree.configure(yscroll=ysb.set) 

    def callbackFunc(event):
        obj.execute("SELECT Rate from itemsinvent where ItemName = '"+menItems.get()+"'")
        rateinp=obj.fetchall()
        var.set(rateinp)
        #print(rateinp)
        

    def populateDetBox():
        try:
            srno=len(listItemDet)
            name=menItems.get()
            rate=float(txtItemRate.get())
            #print(rate)
            quantity=int(txtItemQuant.get())
            amount=float(rate*quantity)
            #totalamount=totalamount+amount
            listItemDet.append([name,rate,quantity,amount])
            """for i in listItemDet:
                lstItemDet.insert("end", i)"""
            """for i in range(1,srno):            
                for j in range(4):         
                    e = Entry(lstItemDet, width=10, fg='black', font=('Arial', 10))    
                    e.grid(row=i, column=j)              
                    e.insert(END, listItemDet[i][j])"""
            viewRecords(name,rate,quantity,amount)
            #SaveAndBill()
        except Exception as e:
            showMessage(str(e))
        
    
    def viewRecords(name,rate,quantity,amount):

        """records=tree.get_children()
        for element in records:
            tree.delete(records)"""
        #obj.execute('SELECT itemname, Rate, Quantity, Amount from billdata')
        #recrows=obj.fetchall()
        #for x in listItemDet:
        try:
            tree.insert('','end',values=(name,rate,quantity,amount))
        except Exception as e:
            showMessage(str(e))

    def SaveAndBill():
        """obj.execute('SELECT billref from billdata where billref = '+txtBillRef.get())
        chkbillref=obj.fetchall()
        if(chkbillref is txtBillRef.get()):
            print("Bill ref is repeated")"""
        try:
            billref=txtBillRef.get()
            custname=txtCustName.get()
            billdate=txtDate.get()
            totalamount=0.0
            for i in range(len(listItemDet)):
                totalamount=totalamount+listItemDet[i][3]

            #toInsertData=[]

            """for i in range(len(listItemDet)):
                listItemDet[i].insert(0,custname)
                listItemDet[i].insert(0,billdate)
                listItemDet[i].insert(0,billref)
                print(listItemDet[i])

            obj.executemany(INSERT into billdata values(%s,%s,%s,%s,%s,%s,%s,%s)",listItemDet)
            obj.commit()"""

            for i in range(len(listItemDet)):
                #print(listItemDet[i])
                n=listItemDet[i][0]
                r=str(listItemDet[i][1])
                q=str(listItemDet[i][2])
                a=str(listItemDet[i][3])
                #query="INSERT into billdata values('"+billref+"','"+custname+"','"+billdate+"','"+n+"',",r,",",q,",",a,",",totalamount,")"
                #obj.execute("INSERT into billdata values('"+billref+"','"+custname+"','"+billdate+"','"+n+"',",r,",",q,",",a,",",totalamount,")")
                obj.execute("""INSERT into billdata (billref,date,customername,itemname,Rate,Quantity,Amount,TotalAmount) values(%s,%s,%s,%s,%s,%s,%s,%s)""",(billref,billdate,custname,n,r,q,a,totalamount))
                #obj.execute("INSERT into billdata (Rate,Quantity) values ('",r,"','",q,"')")
                conn.commit()

            ViewBillActionCommand(str(txtBillRef.get()),1,f1)
        except Exception as e:
            showMessage(str(e))

    obj.execute('SELECT * FROM billdata ORDER BY id DESC LIMIT 1')
    """if(obj.fetchone() is ):
        lastestbillref=1"""
    gotdata=obj.fetchone()[1]
    lastestbillref=str(int(gotdata)+1)
    #print(lastestbillref)
    refvar=StringVar()
    lblBillRef=Label(text='Bill Reference No. :',bg='white',font=('Arial',10))
    txtBillRef=Entry(f1,width=25,bg='white',font=('Arial',10),textvariable=refvar,state='disable')
    refvar.set(lastestbillref)
    lblCustName=Label(text='Customer Name :',bg='white',font=('Arial',10))
    txtCustName=Entry(f1,width=25,bg='white',font=('Arial',10))
    lblDate=Label(text='Date :',bg='white',font=('Arial',10))
    txtDate=Entry(f1,width=20,bg='white',font=('Arial',10))
    lblAddItems=Label(text='Add Items',bg='white',font=('Times New Roman',14))
    lblItems=Label(text='Items :',bg='white',font=('Arial',10))
    menItems = ttk.Combobox(f1, values=menList)
    #menItems.current(1)
    menItems.bind("<<ComboboxSelected>>", callbackFunc)
    lblItemRate=Label(text='Rate :',bg='white',font=('Arial',10))
    txtItemRate=Entry(f1,width=10,font=('Arial',10), state='disabled', textvariable=var)
    lblItemQuant=Label(text='Quantity :',bg='white',font=('Arial',10))
    txtItemQuant=Entry(f1,width=10,bg='white',font=('Arial',10), textvariable=quant)
    btnItemSave=Button(f1,text='Save',width=15,command=populateDetBox)
    lblPvItemDet=Label(text='Preview of Items Details :',bg='white',font=('Arial',12))
    """lstItemDet=Listbox(f1,selectmode='MULTIPLE',width=75)
    lstItemDet.insert('end',('Sr.No.','Name','Rate','Quantity','Amount'))
    lstItemDet.insert('end',('--------','----','----','--------','------'))"""
    
    lstItemDet=Frame(f1,width=80)
    """listItemDetTabTitle=['Item Name','Rate','Quantity','Amount']
    for j in range(4):         
        e = Entry(lstItemDet, width=10, fg='red', font=('Arial', 12, 'bold')) 
        e.grid(row=0, column=j)              
        e.insert(END, listItemDetTabTitle[j])"""

    btnGoToBill=Button(f1,text='Go to Bill',width=20, command=SaveAndBill)

    lblBillRef.place(x=20,y=20)
    txtBillRef.place(x=180,y=20)
    lblCustName.place(x=20,y=50)
    txtCustName.place(x=180,y=50)
    lblDate.place(x=20,y=80)
    txtDate.place(x=180,y=80)
    lblAddItems.place(x=20,y=140)
    lblItems.place(x=20,y=170)
    menItems.place(x=20,y=190)
    lblItemRate.place(x=170,y=170)
    txtItemRate.place(x=170,y=190)
    lblItemQuant.place(x=250,y=170)
    txtItemQuant.place(x=250,y=190)
    btnItemSave.place(x=350,y=185)
    lblPvItemDet.place(x=20,y=230)
    lstItemDet.place(x=60,y=285)
    btnGoToBill.place(x=160,y=465)

    f1.mainloop()

import mysql.connector

conn = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="dishank143!$#",
  database="billingsys"
)

obj=conn.cursor()

root=Tk()
root.title('Billing System')
root.geometry('500x500')
menu=Menu(root)
root.config(menu=menu)
filemenu=Menu(root,tearoff=0)
menu.add_cascade(label='File',menu=filemenu)
filemenu.add_command(label='Create Bill', command=BillActionCommand)
filemenu.add_command(label='View Bill',command=lambda: ViewBillActionCommand('',0,root))
homeCanvas=Canvas(root,bg='white',width=500,height=500)
homeImg=PhotoImage(file='original_billing.png')
image=homeCanvas.create_image(0.5,12,anchor=NW, image=homeImg)
homeCanvas.pack()
root.mainloop()