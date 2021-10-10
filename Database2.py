#Function Name    :  Insert One Record Into employee table
#Function Date    :  10 Oct 2021
#Function Author  :  Om Deshmukh
#Input            :  Int
#Output           :  Record Get Inserted Into The Row


# insert single entity query

import MySQLdb

def Connection():

    Connection = MySQLdb.connect(host = "localhost", database = "pythondb", user = "root", password = "-----")

    try:

        cobj = Connection.cursor()

        str = "insert into emptab(eno, ename, sal) values(1006, 'varad', 6000)"

        cobj.execute(str)
        Connection.commit()

        print("1 Row Inserted...")

    except:

        Connection.rollback()
        print("Not Inserted")

    cobj.close()
    Connection.close()

def main():

    Connection()

if __name__ == "__main__":
    main()
