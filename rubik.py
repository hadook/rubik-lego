
"""This class represents a Rubik's cube"""
class Cube():
    pass

"""This class represents a single face of a Rubik's cube"""
class Face():
    
    # initializes the face with a give color
    def __init__(self, color: str) -> None:
        self.color = []
        for i in range(9):
            self.color.append(color)
