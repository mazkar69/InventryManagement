
import sqlite3



#==============================================================================
def create_db_1():
    con=sqlite3.connect(database=r"ims.db")
    cur=con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS employee (eid INTEGER PRIMARY KEY AUTOINCREMENT,name text,email text,gender text,contact text,dob text,doj text,pass text,utype text,address text,salary text)")
    con.commit()


#====================================================================
def create_db_2():
    con=sqlite3.connect(database=r"ims.db")
    cur=con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS category (cid INTEGER PRIMARY KEY AUTOINCREMENT,name text)")
    con.commit()



#=========================================================================

def create_db_3():
    con=sqlite3.connect(database=r"ims.db")
    cur=con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS product (pid INTEGER PRIMARY KEY AUTOINCREMENT,category text,supplier text,name text,price text,qty text,status text)")
    con.commit()

#==========================================================

def createdatabase():
    con=sqlite3.connect(database=r"ims.db")
    cur=con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS supplier (sup_id INTEGER PRIMARY KEY AUTOINCREMENT,invoice_no text,name text,contact text,description text)")
    con.commit()




#===============================================================================================
#===============================================================================================
#===============================================================================================
#===============================================================================================

# calling all the function

def createAllTables():

    create_db_1()
    create_db_2()
    create_db_3()
    createdatabase()

createAllTables()           #Creating all the tables
