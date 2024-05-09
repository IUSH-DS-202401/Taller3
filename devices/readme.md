# Binary Tree Radiation Analysis

This Python project implements a binary tree structure to analyze radiation potential within nodes. It includes classes for creating a binary tree and nodes, as well as methods to build the tree, calculate radiation potential, and check if the tree is balanced based on radiation and link properties.

## Classes

### `DataLoader`

#### Methods

- `__init__(file_path)`: Initializes a data loader object with the given file path.
- `load_data()`: Loads data from the file 


### `BinaryTree`

#### Methods

- `__init__()`: Initializes a binary tree object with a root node and a dictionary to store vertices.
- `build(edge_list)`: Builds the binary tree structure based on the given list of edges.
- `calculate_potential(node)`: Calculates the radiation potential of a given node and its subtree.
- `is_balanced(node)`: Checks if the binary tree rooted at the given node is balanced in terms of radiation potential and link properties.
- `post_order(node)`: Traverses the binary tree in post-order fashion, printing node names.

### `Node`

#### Attributes

- `data`: Holds the data associated with the node.
- `left`: Points to the left child node.
- `right`: Points to the right child node.

### Usage

Create a folder, put the devices project into that folder, then run the following command in the created folder.

```bash
  py -B devices/src/main.py
```

