#-*- coding: utf8 -*-

import MySQLdb as mdb
import psycopg2 as pdb
import sqlite3 as sdb
import warnings

# CREATE THE DATABASE

def createdb_mysql():

    # SET UP THE CONNECTION
    try:
        db = mdb.connect(host="localhost", user="USERNAME", passwd="PASSWORD")
        db1 = db.cursor()
        with warnings.catch_warnings():
            warnings.simplefilter('ignore')
            db1.execute('CREATE DATABASE IF NOT EXISTS testdb')
            print('Create Database MYSQL testdb')
        con = mdb.connect('localhost', 'USERNAME', 'PASSWORD', 'testdb')
        cur = con.cursor()
        cur.execute("SELECT VERSION()")
        ver = cur.fetchone()
        print "Database version : %s " % ver
        return con

    except mdb.Error, e:

        print "Error %d: %s" % (e.args[0], e.args[1])
        sys.exit(1)


def creatdb_postgres():

    # SET UP THE CONNECTION
    try:
        con = pdb.connect(database="testdb", user="USERNAME",
                          password="PASSWORD", host="127.0.0.1", port="5432")
        print "Create database testdb"
        cur = con.cursor()
        cur.execute('SELECT version()')
        ver = cur.fetchone()
        print ver
        return con

    except pdb.DatabaseError, e:

        print "Error %d: %s" % (e.args[0], e.args[1])
        sys.exit(1)


def creatdb_sqlite():

    # SET UP THE CONNECTION
    try:
        con = sdb.connect('testdb.db')
        print "Creat database testdb"
        cur = con.cursor()
        cur.execute('SELECT SQLITE_VERSION()')
        data = cur.fetchone()
        print "SQLite version: %s" % data
        return con

    except sdb.Error, e:

        print "Error %s:" % e.args[0]
        sys.exit(1)
