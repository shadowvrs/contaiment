class GameObject:

    def __init__(self, name, location, movable, visible, carried, examined, description):
        self.name  = name
        self.location = location
        self.movable = movable
        self.visible = visible
        self.carried = carried
        self.examined = examined
        self.description  = description
