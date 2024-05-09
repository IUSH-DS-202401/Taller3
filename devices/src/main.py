from dataLoader import DataLoader
from binaryTree import BinaryTree
import os

def main():
    current_dir = os.path.dirname(__file__)
    json_file = os.path.join(current_dir, 'db', 'data.json')

    data_loader = DataLoader(json_file)
    data = data_loader.load_data()
    tree = BinaryTree()
    tree.build(data)
    tree.calculate_potential(tree.root)
    isBalanced = tree.is_balanced(tree.root)
    if isBalanced:
        print("The device is radioactively balanced.")
    else:
        print("The device is not radioactively balanced.")
    

if __name__ == "__main__":
    main()
