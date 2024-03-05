import shutil
import os
import time
import subprocess


def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            print("File content:")
            print(content)
    except FileNotFoundError:
        print("File not found.")


def write_file(file_path, content):
    with open(file_path, 'w') as file:
        file.write(content)
    print("Content written to the file.")


def append_to_file(file_path, content):
    with open(file_path, 'a') as file:
        file.write(content)
    print("Content appended to the file.")


def delete_file(file_path):
    try:
        os.remove(file_path)
        print("File deleted successfully.")
    except FileNotFoundError:
        print("File not found.")


def list_files(directory):
    files = os.listdir(directory)
    print("Files in the directory:")
    for file in files:
        print(file)


def check_file_existence(file_path):
    if os.path.exists(file_path):
        print("File exists.")
    else:
        print("File does not exist.")


def move_file(source, destination):
    shutil.move(source, destination)
    print("File moved successfully.")


def copy_file(source, destination):
    shutil.copy(source, destination)
    print("File copied successfully.")


def create_directory(directory):
    os.makedirs(directory, exist_ok=True)
    print("Directory created.")


def delete_directory(directory):
    try:
        shutil.rmtree(directory)
        print("Directory deleted successfully.")
    except FileNotFoundError:
        print("Directory not found.")


def open_program(program_path):
    subprocess.Popen(program_path)
    print("Program opened.")


def exit_program():
    print("Exiting the program.")
    exit()


if __name__ == "__main__":
    while True:
        print("\nFile Manager Menu:")
        print("1. Read File")
        print("2. Write to File")
        print("3. Append to File")
        print("4. Delete File")
        print("5. List Files in Directory")
        print("6. Check File Existence")
        print("7. Move File")
        print("8. Copy File")
        print("9. Create Directory")
        print("10. Delete Directory")
        print("11. Open Program")
        print("12. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            file_path = input("Enter the file path: ")
            read_file(file_path)
        elif choice == "2":
            file_path = input("Enter the file path: ")
            content = input("Enter content to write: ")
            write_file(file_path, content)
        elif choice == "3":
            file_path = input("Enter the file path: ")
            content = input("Enter content to append: ")
            append_to_file(file_path, content)
        elif choice == "4":
            file_path = input("Enter the file path: ")
            delete_file(file_path)
        elif choice == "5":
            directory = input("Enter the directory path: ")
            list_files(directory)
        elif choice == "6":
            file_path = input("Enter the file path: ")
            check_file_existence(file_path)
        elif choice == "7":
            source = input("Enter the source file path: ")
            destination = input("Enter the destination file path: ")
            move_file(source, destination)
        elif choice == "8":
            source = input("Enter the source file path: ")
            destination = input("Enter the destination file path: ")
            copy_file(source, destination)
        elif choice == "9":
            directory = input("Enter the directory path: ")
            create_directory(directory)
        elif choice == "10":
            directory = input("Enter the directory path: ")
            delete_directory(directory)
        elif choice == "11":
            program_path = input("Enter the program path: ")
            open_program(program_path)
        elif choice == "12":
            exit_program()
        else:
            print("Invalid choice. Please enter a valid option.")
