class FileSystem:
    def __init__(self):
        self.files = []

    def upload_file(self, file_name):
        if file_name in self.files:
            print("File already exists!")
        else:
            self.files.append(file_name)
            print(f"File '{file_name}' uploaded successfully.")

    def delete_file(self, file_name):
        if file_name in self.files:
            self.files.remove(file_name)
            print(f"File '{file_name}' deleted successfully.")
        else:
            print("File does not exist!")

    def list_files(self):
        return self.files
