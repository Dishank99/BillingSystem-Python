import mysql.connector

def createDB(username,password):
    mydb1 = mysql.connector.connect(
     host="localhost",
     user=username,
     passwd=password,
    )

    obj1=mydb1.cursor()

    obj1.execute('Create Database billingsys')
    mydb1.commit()

def createTBLS(username,password):
    mydb2 = mysql.connector.connect(
     host="localhost",
     user=username,
     passwd=password,
     database="billingsys"
    )

    obj2=mydb2.cursor()

    obj2.execute("Create Table itemsinvent (ItemName Varchar(50), Rate Varchar(15))")
    obj2.execute("Create Table billdata (id INT AUTO_INCREMENT PRIMARY KEY,billref Varchar(50),date Varchar(50),customername Varchar(50),itemname Varchar(50),Rate Varchar(50),Quantity Varchar(50),Amount Varchar(50),TotalAmount Varchar(50))")
    mydb2.commit()

username=input("Enter the username:")
password=input("Enter the password:")
createDB(username,password)
createTBLS(username,password)