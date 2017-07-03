#-*- coding: utf8 -*-


import db_config
import MySQLdb as mdb
import psycopg2 as pdb
import psycopg2.extras
import sqlite3 as sdb
import sys
import warnings


''' MYSQL CRUD '''

# CREATE A NEW TABLE of MYSQL


def createTable(con):

    cur = con.cursor()
    cur.execute("DROP TABLE IF EXISTS Citizen")
    with warnings.catch_warnings():
        warnings.simplefilter('ignore')
        cur.execute("CREATE TABLE Citizen(Id INT PRIMARY KEY AUTO_INCREMENT, Firstname VARCHAR(25),Lastname VARCHAR(25), City VARCHAR(25), State VARCHAR(25), Country VARCHAR(25));")
    print 'Citizen Table created'

# INSERT VALUES


def insertTable(con):
    with con:

        try:
            cur = con.cursor()

            with warnings.catch_warnings():
                warnings.simplefilter('ignore')
                cur.execute("CREATE TABLE IF NOT EXISTS Citizen(Id INT PRIMARY KEY AUTO_INCREMENT, Firstname VARCHAR(25),Lastname VARCHAR(25), City VARCHAR(25), State VARCHAR(25), Country VARCHAR(25));")
                warnings.filterwarnings('ignore', 'unknown table')

            Id = 0
            Firstname = raw_input("Enter Your First Name ")
            Lastname = raw_input("Enter Your Last Name")
            City = raw_input("Enter Your City")
            State = raw_input("Enter Your State")
            Country = raw_input("Enter Your Country")
            cur.execute("INSERT INTO Citizen VALUES (%s, %s, %s, %s, %s, %s)",
                        (Id, Firstname, Lastname, City, State, Country))
            print "Record Inserted"
        except Exception as e:
            print e


# RETRIEVE TABLE ROWS
def retrieveTable(con):
    with con:

        cur = con.cursor(mdb.cursors.DictCursor)
        cur.execute("SELECT * FROM Citizen")

        rows = cur.fetchall()

        for row in rows:
            print row["Id"], row["Firstname"], row["Lastname"], row["City"], row["State"], row["Country"]


# UPDATE ROW
def updateRow(con):
    with con:

        try:
            cur = con.cursor()
            cur = con.cursor(mdb.cursors.DictCursor)
            cur.execute("SELECT * FROM Citizen")
            rows = cur.fetchall()
            for row in rows:
                print 'Table Data:', row["Id"], row["Firstname"], row["Lastname"], row["City"], row["State"], row["Country"]
            id = input("Enter ID for Update Record")
            fname = raw_input('Enter First Name For Update record')
            lname = raw_input('Enter Last Name For Update record')
            city = raw_input('Enter City Name For Update record')
            state = raw_input('Enter State Name For Update record')
            con = raw_input('Enter Country Name For Update record')
            cur.execute("UPDATE Citizen SET Firstname = %s, Lastname = %s, City = %s, State = %s, Country = %s  WHERE Id = %s",
                        (fname, lname, city, state, con, id))

            print "Number of rows updated:",  cur.rowcount
            if cur.rowcount == 0:
                print 'Record Not Updated'
        except TypeError as e:
            print 'ID Not Exist '

 # DELETE ROW


def deleteRow(con):
    with con:

        try:
            cur = con.cursor()
            cur = con.cursor(mdb.cursors.DictCursor)
            cur.execute("SELECT * FROM Citizen")
            rows = cur.fetchall()
            for row in rows:
                print 'Table Data:', row["Id"], row["Firstname"], row["Lastname"], row["City"], row["State"], row["Country"]

            id = raw_input("Enter ID for Delete Record")
            cur.execute("DELETE FROM Citizen WHERE Id = %s", id)
            print "Number of rows deleted:", cur.rowcount

        except TypeError as e:
            print 'ID Not Exist '


''' POSTGRESQL CRUD '''

# CREATE A NEW TABLE OF Postgresql


def createTable_psql(con):
    with con:

        cur = con.cursor()
        cur.execute("DROP TABLE IF EXISTS Emp")
        cur.execute(
            "CREATE TABLE Emp(Id SERIAL PRIMARY KEY, Name VARCHAR(25), Company_Name VARCHAR(25), Designation VARCHAR(25), Age VARCHAR(25), City VARCHAR(25));")
        print 'Employee Table created'

# INSERT VALUES


def insertTable_psql(con):
    with con:

        try:
            cur = con.cursor()

            with warnings.catch_warnings():
                warnings.simplefilter('ignore')
                cur.execute(
                    "CREATE TABLE IF NOT EXISTS Emp(Id SERIAL PRIMARY KEY, Name VARCHAR(25), Company_Name VARCHAR(25), Designation VARCHAR(25), Age VARCHAR(25), City VARCHAR(25));")
                print 'Employee Table created'
                warnings.filterwarnings('ignore', 'unknown table')

            Name = raw_input("Enter Your Name ")
            Company_Name = raw_input("Enter Your Company Name")
            Designation = raw_input("Enter Your Designation")
            Age = raw_input("Enter Your Age")
            City = raw_input("Enter Your City")
            cur.execute("INSERT INTO Emp  (Name, Company_Name, Designation, Age, City) VALUES(%s, %s, %s, %s, %s)",
                        (Name, Company_Name, Designation, Age, City))
            print "Record Inserted"
            con.commit()
        except Exception as e:
            print e


# RETRIEVE TABLE ROWS
def retrieveTable_psql(con):
    with con:

        cur = con.cursor(cursor_factory=pdb.extras.DictCursor)
        cur.execute("SELECT * FROM Emp")

        rows = cur.fetchall()
        for row in rows:
            if rows == None:
                print 'Table is Empty'
                break
            else:
                print('ID: {0} Name: {1} Company Name: {2} Designation: {3} Age: {4} City: {5}'.format(
                    row[0], row[1], row[2], row[3], row[4], row[5]))


# UPDATE ROW
def updateRow_psql(con):
    with con:

        try:
            cur = con.cursor()
            cur = con.cursor(cursor_factory=pdb.extras.DictCursor)
            cur.execute("SELECT * FROM Emp")
            rows = cur.fetchall()
            for row in rows:
                print('ID: {0} Name: {1} Company Name: {2} Designation: {3} Age: {4} City: {5}'.format(
                    row[0], row[1], row[2], row[3], row[4], row[5]))

            e_id = input("Enter id You want to update")
            name = raw_input("Enter Name for Update Record")
            cname = raw_input("Enter Company Name for Update Record")
            deg = raw_input("Enter Designation for Update Record")
            age = raw_input("Enter Age for Update Record")
            city = raw_input('Enter City Name For Update record')

            cur.execute("UPDATE Emp SET name =%s, Company_Name = %s, Designation = %s, Age = %s, City = %s WHERE Id = %s",
                        (name, cname, deg, age, city, e_id))

            print "Number of rows updated:",  cur.rowcount
            if cur.rowcount == 0:
                print 'Record Not Updated'
        except TypeError as e:
            print 'ID Not Exist '

#  # DELETE ROW


def deleteRow_psql(con):
    with con:

        try:
            cur = con.cursor()
            cur = con.cursor(cursor_factory=pdb.extras.DictCursor)
            cur.execute("SELECT * FROM Emp")
            rows = cur.fetchall()
            for row in rows:
                print('ID: {0} Name: {1} Company Name: {2} Designation: {3} Age: {4} City: {5}'.format(
                    row[0], row[1], row[2], row[3], row[4], row[5]))

            id = raw_input("Enter ID for Delete Record")
            cur.execute("DELETE FROM Emp WHERE Id = %s", id)
            print "Number of rows deleted:", cur.rowcount

        except TypeError as e:
            print 'ID Not Exist '


''' SQLITE CRUD '''

# CREATE A NEW TABLE


def createTable_sqlite(con):
    with con:

        cur = con.cursor()
        cur.execute("DROP TABLE IF EXISTS Student")
        cur.execute("CREATE TABLE Student(Id INTEGER PRIMARY KEY AUTOINCREMENT, Name VARCHAR(25),College VARCHAR(25), Course VARCHAR(25), Age INT, City VARCHAR(25));")
        print 'Student Table created'

# # INSERT VALUES


def insertTable_sqlite(con):
    with con:

        try:
            cur = con.cursor()

            with warnings.catch_warnings():
                warnings.simplefilter('ignore')
                cur.execute(
                    "CREATE TABLE IF NOT EXISTS Student(Id INTEGER PRIMARY KEY AUTOINCREMENT, Name VARCHAR(25),College VARCHAR(25), Course VARCHAR(25), Age INT, City VARCHAR(25));")
                warnings.filterwarnings('ignore', 'unknown table')

            Name = raw_input("Enter Your Name ")
            College = raw_input("Enter Your College Name")
            Course = raw_input("Enter Your Course")
            Age = raw_input("Enter Your Age")
            City = raw_input("Enter Your City")
            cur.execute("INSERT INTO Student(Name, College, Course, Age, City) VALUES (?, ?, ?, ?, ?)",
                        (Name, College, Course, Age, City))
            print "Record Inserted"
        except Exception as e:
            print e


# RETRIEVE TABLE ROWS
def retrieveTable_sqlite(con):
    with con:

        cur = con.cursor()
        con.row_factory = sdb.Row
        cur.execute("SELECT * FROM Student")

        rows = cur.fetchall()
        for row in rows:
            if row == None:
                print 'Please Insert Record'
                break
            else:
                print('ID: {0} Name: {1} College: {2} Course: {3} Age: {4} City: {5}'.format(
                    row[0], row[1], row[2], row[3], row[4], row[5]))


# # UPDATE ROW
def updateRow_sqlite(con):
    with con:

        try:
            cur = con.cursor()
            con.row_factory = sdb.Row
            cur.execute("SELECT * FROM Student")
            rows = cur.fetchall()
            for row in rows:
                print('ID: {0} Name: {1} College: {2} Course: {3} Age: {4} City: {5}'.format(
                    row[0], row[1], row[2], row[3], row[4], row[5]))

            id = input("Enter ID for Update Record")
            name = raw_input("Enter Name for Update Record")
            clgname = raw_input("Enter College Name for Update Record")
            csr = raw_input("Enter Course for Update Record")
            age = raw_input("Enter Age for Update Record")
            city = raw_input('Enter City Name For Update record')
            cur.execute("UPDATE Student SET Name = ?, College = ?, Course = ?, Age = ?, City = ?  WHERE Id = ?",
                        (name, clgname, csr, age, city, id))
            print "Number of rows updated:",  cur.rowcount
            if cur.rowcount == 0:
                print 'Record Not Updated'
        except TypeError as e:
            print 'ID Not Exist '

#  DELETE ROW


def deleteRow_sqlite(con):
    with con:

        try:
            cur = con.cursor()
            con.row_factory = sdb.Row
            cur.execute("SELECT * FROM Student")
            rows = cur.fetchall()
            for row in rows:
                print 'Table Data:', row["Id"], row["Name"], row["College"], row["Course"], row["Age"], row["City"]

            id = input("Enter ID for Delete Record")
            cur.execute("DELETE FROM Student WHERE Id =  ?", (id,))
            print "Number of rows deleted:", cur.rowcount

        except TypeError as e:
            print 'ID Not Exist '
