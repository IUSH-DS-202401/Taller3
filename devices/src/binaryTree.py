from node import Node

class BinaryTree:
    def __init__(self) -> None:
        self.root = None
        self.vertices = {}

    def build(self, edge_list):
        if len(edge_list) == 0:
            raise Exception("Empty list")
        
        for edge in edge_list:
            if edge["content_in"] == None:
                node = Node(edge)
                self.vertices[edge["name"]] = node
                self.root = node
            elif edge["content_in"] in self.vertices.keys():
                node = Node(edge)
                parent = self.vertices[edge["content_in"]]
                if parent.left is None:
                    parent.left = node
                else:
                    parent.right = node
                
                self.vertices[edge["name"]] = node

    def calculate_potential(self, node):
        if node.left is None and node.right is None:
            return node.data["p_radioactive"]
        
        node.data["p_radioactive"] = self.calculate_potential(node.left) + self.calculate_potential(node.right)
        return node.data["p_radioactive"]
    
    def is_balanced(self, node):
        if node.left is None and node.right is None:
            return True
        
        left_balance = self.is_balanced(node.left)
        right_balance = self.is_balanced(node.right)

        children_balance = (node.left.data["p_radioactive"] * node.left.data["r_link"]) == (node.right.data["p_radioactive"] * node.right.data["r_link"])
        
        if children_balance is not True and (left_balance is True and right_balance is True):
            
            self.post_order(node)


        return right_balance is True and left_balance is True and children_balance is True
    
    def post_order(self, node):
        if node is None:
            return
        self.post_order(node.left)
        self.post_order(node.right)
        print(node.data["name"])