import os

def create_file(filename):
    try:
        with open(filename, "x") as file:
            print(f"file Name {filename} created successfully!")

    except FileExistsError:
        print(f"file name {filename} already existes!")

    except Exception as E:
        print(f"An error occurred !")  

def view_all_files():
    files = os.listdir()
    if not files:
        print("No files found in the current directory!")
    else:
        print(f"files in the current directory!")
        for file in files:
            print(file)

def delete_file(filename):
    try:
        os.remove(filename)
        print(f"file {filename} deleted successfully!")
    except FileNotFoundError:
        print(f"file {filename} not found!")

    except Exception as e:
        print(f"An error occurred while deleting the file")

def read_file(filename):
    try:
        with open("sample.txt", "r") as f:
            Content = f.read()
            print(f"Content of '{filename}' : {Content}")
    except FileNotFoundError:
        print(f"file {filename} not found!")

    except Exception as e:
        print(f"An error occurred while reading the file :")

def edit_file(filename):
    try:
        with open("sample.txt", "a") as f:
            content = input("Enter the content to append to the file =")
            f.write(content + "\n")
            print(f"content appened to {filename} successfully!")

    except FileNotFoundError:
        print(f"file {filename} not found!")

    except Exception as e:
        print(f"An error occurred while reading the file :")

def main():
    while True:
        print("1. Create a file")
        print("2. view all files")
        print("3. Delete a file")
        print("4. Read a file")
        print("5. Edit a file")
        print("6. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            filename = input("Enter the file name to create: ")
            create_file(filename)
        elif choice == "2":
            view_all_files()
        elif choice == "3":
            filename = input("enter the file name to delete: ")
            delete_file(filename)
        elif choice =="4":
            filename = input("Enter the files name to read: ")
            read_file(filename)
        elif choice == "5":
            filename = input("Enter the file name to edit: ")
            edit_file(filename)
        elif choice == "6":
            print("Exiting the program! ")
            break
        else:
            print("Invalid choice please try again!")

if __name__ == " __main__ ":
    main()         
