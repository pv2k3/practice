import tkinter as tk
import ttkbootstrap as ttk
import os, shutil, pathlib
def sort():
    try :
        # Source  directory to sort
        source_directory = entry.get()
        # List of all the available files in folder
        list_of_files = os.listdir(source_directory)
        # For mapping extensions to the folder
        common_extensions = {
            '.doc': "Text Document", '.docx': "Text Document", '.odt': "Text Document", '.txt': "Text Document",
            '.mpg': "Videos", '.mpeg': "Videos", '.mp4': "Videos", '.mov': "Videos",
            '.mkv': "Videos", '.ods': "Spreadsheet", '.xls': "Spreadsheet", '.xlsx': "Spreadsheet",
            '.xlsm': "Spreadsheet", '.ppt': "Powerpoint", '.pptx': "Powerpoint", '.odp': "Powerpoint",
            '.pps': "Powerpoint", '.gif': "Images", '.ico': "Images", '.jpeg': "Images",
            '.jpg': "Images", '.png': "Images", '.svg': "Images", '.zip': "Compressed",
            '.z': "Compressed", '.7z': "Compressed", '.deb': "Compressed", '.pkg': "Compressed",
            '.rar': "Compressed", '.rpm': "Compressed", '.tar.gz': "Compressed", '.mp3': "Audio",
            '.pdf': "PDF", '.jar': "Executable", '.vsix': "Compressed"
        }
        # To check whether the specified filetype is in the dictionary or not
        check = 0
        # Iterating through elements of the source folder
        for i in list_of_files:
            # Making a path to the file
            source_file = os.path.join(source_directory, i)
            # Getting the file extension
            extension = pathlib.Path(source_file).suffix
            # To avoid key error if extension is not a key in dictionary
            if extension in common_extensions:
                check = 1
            # Making destination accessible in the for loop
            destination = ""
            if extension and (check == 1):
                # Place to move file
                destination = os.path.join(source_directory, common_extensions[extension])
                # Make the folder if it does not exist
                if not os.path.exists(destination):
                    os.makedirs(destination)
            # Move the file if it is mapped
            if extension and (check == 1):
                shutil.move(source_file, destination)
            else:
                continue
            print(f"Moved {i} to {destination}")
        if check==0:
            result_label.config(text="The present entities are a folder or not have been mapped")
        else:
            result_label.config(text="Successful All files which can be mapped are moved")
    except:
        result_label.config(text="Invalid Input")

# Create window
window = ttk.Window(themename="superhero")
# Set window Title
window.title("Arrange files in Folder")
# Set Window size
window.geometry("500x250")

# Creating an entry field
entry = ttk.Entry(window, width=50, background="#aaccaa", font=("Arial", 12))
entry.pack(pady=20)

# Creating a button to perform the task
calculate_button = ttk.Button(window, text="Arrange", command=sort)
calculate_button.pack()

# Show text in the window
result_label = ttk.Label(window, text="Result: ")
result_label.pack()

# Start the window
window.mainloop()