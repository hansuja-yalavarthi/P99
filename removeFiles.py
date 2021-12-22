import os
import shutil
import time

def removeFolder(path):
	if not shutil.rmtree(path):
		print(f"{path} is removed successfully")
	else:
		print(f"Unable to delete the "+path)

def removeFile(path):
	if not os.remove(path):
		print(f"{path} is removed successfully")
	else:
		print("Unable to delete the "+path)

def getObjectAge(path):
	ctime = os.stat(path).st_ctime
	return ctime

def main():
	deleted_folders_count = 0
	deleted_files_count = 0
	path = input("Enter the folder path:-")
	days = 30
	seconds = time.time() - (days * 24 * 60 * 60)
	if os.path.exists(path):
		for root_folder, folders, files in os.walk(path):
			if seconds >= getObjectAge(root_folder):
				removeFolder(root_folder)
				deleted_folders_count += 1 
				break
			else:
				for folder in folders:
					folder_path = os.path.join(root_folder, folder)
					if seconds >= getObjectAge(folder_path):
						removeFolder(folder_path)
						deleted_folders_count += 1 
				for file in files:
					file_path = os.path.join(root_folder, file)
					if seconds >= getObjectAge(file_path):
						removeFile(file_path)
						deleted_files_count += 1  
		else:
			if seconds >= getObjectAge(path):
				removeFile(path)
				deleted_files_count += 1 
	else:
		print(f'"{path}" is not found')
		deleted_files_count += 1 
	print(f"Total folders deleted: {deleted_folders_count}")
	print(f"Total files deleted: {deleted_files_count}")

if __name__ == '__main__':
	main()