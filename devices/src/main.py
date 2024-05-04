from dataLoader import DataLoader
import os

def main():
    current_dir = os.path.dirname(__file__)
    json_file = os.path.join(current_dir, 'db', 'data.json')

    data_loader = DataLoader(json_file)
    data = data_loader.load_data()
    print(data)

if __name__ == "__main__":
    main()
