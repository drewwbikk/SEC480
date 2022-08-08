from ingest_files import ingest_files
from search import search
from new_iso import new_iso
import new_db
import time

def menu():
    menu_options = {
        1: 'Ingest list of file paths',
        2: 'Enumerate disk image and ingest file paths',
        3: 'Search the database',
        4: 'Create the database',
        5: 'Exit'
    }
    print('---------------------------------------')
    for key in menu_options.keys():
        print (key, '--', menu_options[key] )
    print('---------------------------------------')

def main():
    while True:
        menu()
        option = None
        try:
            option = int(input("What would you like to do?: "))
            if option not in range(1, 6):
                raise ValueError
        except ValueError:
            print("Invalid option. Please enter a number (1-5) corresponding to your choice.")
        if option == 1:
            # Ingest file paths
            os_name = input('What is the name/version of the OS? (Ex: windows10): ')
            file_name = input('What is the path of the CSV file? (Ex: file_paths.csv): ')
            file_exists = False
            while(file_exists == False):
                if not os.path.exists(file_name):
                    print("File not found!")
                    file_name = input('What is the path of the CSV file? (Ex: file_paths.csv): ')
                else:
                    file_exists = True
            os_type = input('What is the type of the OS? (windows, linux, unix): ')
            ingest_files(os_name, file_name, os_type)
        elif option == 2: 
            # Enumerate disk img
            os_name = input('What is the name/version of the OS? (Ex: windows10): ')
            file_name = input('What is the path of the disk image file? (Ex: windows10.iso): ')
            file_exists = False
            while(file_exists == False):
                if not os.path.exists(file_name):
                    print("File not found!")
                    file_name = input('What is the path of the ISO file? (Ex: windows10.iso): ')
                else:
                    file_exists = True
            os_type = input('What is the type of the OS? (windows, linux, unix): ')
            new_iso(file_name, os_name, os_type)
        elif option == 3:
            # Search database
            file_name = input('What is the name of the file? (Ex: cmd.exe): ')
            os_name = input('What is the name/version of the OS? (Ex: windows10): ')
            print('---------------------------------------')
            search(file_name, os_name)
            time.sleep(2)
        elif option == 4:
            # Create the db
            new_db.main()
        elif option == 5:
            # Exit the program
            print("Exiting...")
            exit()

if __name__ == '__main__':
    main()