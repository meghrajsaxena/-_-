import os
import shutil

def organize_files(directory):
   
    file_extensions = {
        'Images': ['.jpg', '.jpeg', '.png', '.gif'],
        'Documents': ['.pdf', '.doc', '.docx', '.txt'],
        'Videos': ['.mp4', '.avi', '.mov', '.mkv'],
        'Others': []  # Default directory for other file types
    }

  
    for folder in file_extensions.keys():
        folder_path = os.path.join(directory, folder)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

  
    files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]

    
    for file in files:
        file_extension = os.path.splitext(file)[1]
        moved = False
        for folder, extensions in file_extensions.items():
            if file_extension in extensions:
                src = os.path.join(directory, file)
                dst = os.path.join(directory, folder, file)
                shutil.move(src, dst)
                moved = True
                break
        
        if not moved:
            src = os.path.join(directory, file)
            dst = os.path.join(directory, 'Others', file)
            shutil.move(src, dst)

    print("Files organized successfully!")


if __name__ == "__main__":
        directory_path = 'files'
        organize_files(directory_path)
        
