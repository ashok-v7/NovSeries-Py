import sqlite3


class DatabaseManager:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.create_table()

    def create_table(self):
        try:
            cursor = self.conn.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS courses (
                    id INTEGER PRIMARY KEY,
                    name TEXT NOT NULL,
                    description TEXT
                )
            ''')
            self.conn.commit()
        except sqlite3.Error as e:
            print(f"An error occurred while creating the table: {str(e)}")

    def insert_data(self, name, description):
        try:
            cursor = self.conn.cursor()
            cursor.execute(
                'INSERT INTO courses (name, description) VALUES (?, ?)', (name, description))
            self.conn.commit()
            print("Data inserted successfully.")
        except sqlite3.Error as e:
            print(f"An error occurred while inserting data: {str(e)}")

    def fetch_all_data(self):
        try:
            cursor = self.conn.cursor()
            cursor.execute('SELECT * FROM courses')
            data = cursor.fetchall()
            if data:
                for row in data:
                    print(
                        f"ID: {row[0]}, Name: {row[1]}, Description: {row[2]}")
            else:
                print("No data found.")
        except sqlite3.Error as e:
            print(f"An error occurred while fetching data: {str(e)}")

    def delete_data(self, id):
        try:
            cursor = self.conn.cursor()
            cursor.execute('DELETE FROM courses WHERE id = ?', (id,))
            self.conn.commit()
            print("Data deleted successfully.")
        except sqlite3.Error as e:
            print(f"An error occurred while deleting data: {str(e)}")


if __name__ == "__main__":
    db_name = "courses.db"
    db_manager = DatabaseManager(db_name)

    while True:
        print("\nOptions:")
        print("1. Insert data")
        print("2. Fetch all data")
        print("3. Delete data by ID")
        print("4. Exit")

        choice = input("Enter your choice (1/2/3/4): ")

        if choice == "1":
            name = input("Enter course name: ")
            description = input("Enter course description: ")
            db_manager.insert_data(name, description)

        elif choice == "2":
            db_manager.fetch_all_data()

        elif choice == "3":
            id_to_delete = input("Enter the ID of the course to delete: ")
            db_manager.delete_data(id_to_delete)

        elif choice == "4":
            break

        else:
            print("Invalid choice. Please enter a valid option.")
