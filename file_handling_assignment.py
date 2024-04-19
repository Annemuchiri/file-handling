def create_file_with_content(file_name):
        with open(file_name, 'w') as file:
            file.write("john,45")
            file.write("jane,30")
            file.write("joan,23")
        print('file','file_name')
        
def append_to_file(file_name):
    try:
        with open(file_name, 'a') as file:
            file.write("john,45")
            file.write("jane,30")
            file.write("joan,23")
        print("Three lines appended to 'my_file.txt' successfully.")
    except FileNotFoundError:
            print("Error: File not found.")
    except PermissionError:
        print("Error: Permission denied to append to the file.")
    except Exception as e:
        print("Unexpected error:", e)


    