class Component:
    def __init__(self, id, name, contained_in=None, radioactive_potential=0, linked_to=None):
        self.id = id
        self.name = name
        self.contained_in = contained_in
        self.radioactive_potential = radioactive_potential
        self.linked_to = linked_to
        self.left = None
        self.right = None
        
