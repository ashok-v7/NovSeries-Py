import os
import sqlite3 as lite

# functionilty


class DatabaseManage(object):
    def __init__(self):
        global con
        try:
            con = lite.connect("courses.db")
            with con:
                cur = con.cursor()
                cur.execute(
                    "CREATE TABLE IF NOT EXISTS course(id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, description TEXT)")
                print("table created")
            print("connected to DB")
        except Exception:
            print("unable to create conn DB")

    def insert_data(self, data):
        try:
            with con:
                cur = con.cursor()
                cur.execute('INSERT INTO course(name,description) VALUES(?,?)', data

                            )
            return True
        except Exception:
            return False

    def fetch_data(self):
        try:
            with con:
                cur = con.cursor()
                cur.execute("SELECT * FROM course")
            return cur.fetchall()
        except Exception:
            return False

    def delete_data(self, id):
        try:
            with con:
                cur = con.cursor()
            d1 = "DELETE FROM course WHERE id = ?"
            cur.execute(d1, [id])
            return True

        except Exception:
            return False

# provide interface to user to interact


def main():
    print("*"*20)
    print("\n::COURSE MANAGMENT :: \n")
    print("\n")

    dbobj = DatabaseManage()
    rtv = dbobj.fetch_data()
    print("#"*20)
    print("\n:: USer manual::\n")
    print('\n Press 1. Insert a new course\n')
    print('\n Press 2. View all courses\n')
    print('\n Press 3. Delete a course\n')
    print("#"*20)
    print("\n")
    choice = input("\n Enter a choice : \n")
    if choice == "1":
        name = input("\n Enter course name : \n")
        description = input("\n Enter course description : \n")
        # data = ()
        # if dbobj.insert_data([name, description]):
        if dbobj.insert_data([name, description]):
            print("course was inserted succesfully")
        else:
            print("Something went wrong")
    elif choice == '2':
        print("\n::course list :: ")
        if rtv:
            for index, value in enumerate(rtv):
                # print("\n Sl no : " + str(index + 1))
                print("\n Course ID : " + str(value[0]))
            print("\n Course Name : " + str(value[1]))
            print("\n Course Description : " + str(value[2]))
            print("\n")
        else:
            print("No data found")

    elif choice == '3':
        rec_id = input("\n Enter course id : \n")
        if dbobj.delete_data(rec_id):
            print("course was deleted succesfully")
        else:
            print("\n BAD CHOICE Something went wrong \n")


if __name__ == "__main__":
    main()
