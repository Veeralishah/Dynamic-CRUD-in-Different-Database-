#-*- coding: utf8 -*-

import sys
import db_query
'''Menu for User Input '''


def choice_mysql(con):
    print "1. Create Table"
    print "2. Insert Data"
    print "3. Read Data"
    print "4. Update Data"
    print "5. Delete Data"
    print "6. Quit"

    ch = input("Enter Your Choice")
    if ch == 1:
        db_query.createTable(con)
        choice_mysql(con)
    elif ch == 2:
        db_query.insertTable(con)
        choice_mysql(con)
    elif ch == 3:
        db_query.retrieveTable(con)
        choice_mysql(con)
    elif ch == 4:
        db_query.updateRow(con)
        choice_mysql(con)
    elif ch == 5:
        db_query.deleteRow(con)
        choice_mysql(con)
    elif ch == 6:
        exit()
        pass
    else:
        print "Please Enter Valid Input"


def choice_postgresql(con):
    print "1. Create Table"
    print "2. Insert Data"
    print "3. Read Data"
    print "4. Update Data"
    print "5. Delete Data"
    print "6. Quit"

    ch = input("Enter Your Choice")
    if ch == 1:
        db_query.createTable_psql(con)
        choice_postgresql(con)
    elif ch == 2:
        db_query.insertTable_psql(con)
        choice_postgresql(con)
    elif ch == 3:
        db_query.retrieveTable_psql(con)
        choice_postgresql(con)
    elif ch == 4:
        db_query.updateRow_psql(con)
        choice_postgresql(con)
    elif ch == 5:
        db_query.deleteRow_psql(con)
        choice_postgresql(con)
    elif ch == 6:
        exit()
        pass
    else:
        print "Please Enter Valid Input"


def choice_sqlite(con):
    print "1. Create Table"
    print "2. Insert Data"
    print "3. Read Data"
    print "4. Update Data"
    print "5. Delete Data"
    print "6. Quit"

    ch = input("Enter Your Choice")
    if ch == 1:
        db_query.createTable_sqlite(con)
        choice_sqlite(con)
    elif ch == 2:
        db_query.insertTable_sqlite(con)
        choice_sqlite(con)
    elif ch == 3:
        db_query.retrieveTable_sqlite(con)
        choice_sqlite(con)
    elif ch == 4:
        db_query.updateRow_sqlite(con)
        choice_sqlite(con)
    elif ch == 5:
        db_query.deleteRow_sqlite(con)
        choice_sqlite(con)
    elif ch == 6:
        exit()
        pass
    else:
        print "Please Enter Valid Input"


def choice():
    print "1. MYSQL Database"
    print "2. PostgreSQL Database"
    print "3. Sqlite Databse"
    print "4. Exit"

    ch = input("Enter Your Choice")
    if ch == 1:
        con = db_query.db_config.createdb_mysql()
        choice_mysql(con)
    elif ch == 2:
        con = db_query.db_config.creatdb_postgres()
        choice_postgresql(con)
    elif ch == 3:
        con = db_query.db_config.creatdb_sqlite()
        choice_sqlite(con)
    elif ch == 4:
        exit()
        pass
    else:
        print "Please Enter Valid Input"

choice()
