import json

class DataLoader:
    def __init__(self,file_path):
        self.file_path = file_path
    
    
    def load_data(self):
        with open(self.file_path) as file:
            data = json.load(file)
        return data
    
 