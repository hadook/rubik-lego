import random
import copy


"""This class represents a Rubik's cube"""
class Cube():
    moves = ["U", "U2", "U'",
            "D", "D2", "D'",
            "F", "F2", "F'",
            "B", "B2", "B'",
            "L", "L2", "L'",
            "R", "R2", "R'"]
    
    # initializes cube with starting colors
    def __init__(self) -> None:
        self.up     = [['W' for _ in range(3)] for _ in range(3)]
        self.down   = [['Y' for _ in range(3)] for _ in range(3)]
        self.front  = [['G' for _ in range(3)] for _ in range(3)]
        self.back   = [['B' for _ in range(3)] for _ in range(3)]
        self.left   = [['O' for _ in range(3)] for _ in range(3)]
        self.right  = [['R' for _ in range(3)] for _ in range(3)]
        
    # constructs a cube instance from a dictionary of face arrays
    @classmethod
    def from_dict(cls, faces: dict):
        cube = Cube()
        cube.up = faces['up']
        cube.down = faces['down']
        cube.front = faces['front']
        cube.back = faces['back']
        cube.left = faces['left']
        cube.right = faces['right']
        return cube

    # returns a list of face arrays
    @property
    def faces(self) -> list:
        return [self.up, self.left, self.front, self.right, self.back, self.down]

    # cube is solved if each face has all tiles of the same color
    @property
    def is_solved(self) -> bool:
        for face in self.faces:
            center = face[1][1]
            for i in range(3):
                for j in range(3):
                    if face[i][j] != center:
                        return False
        return True

    # DFS recurrence to solve the cube
    def solve(self, history: list, max_moves: int = 60) -> list:
        pass
    
    # scrambles the cube by applying a number of random moves
    def scramble(self, num_moves: int) -> list:
        moves = []
        last = None

        for _ in range(num_moves):
            # select from available moves (different than last)
            moveset = random.choice(self.moves)
            while moveset == last:
                moveset = random.choice(self.moves)
            last = moveset
            move = random.choice(moveset)

            # apply move to cube
            self.rotate(move)
            moves.append(move)
        return moves
            
    # rotate one of the faces according to the parameter
    def rotate(self, move: str) -> None:
        match move:
            
            case "U":
                # rotate face itself
                self.up = self.get_rotated_face(self.up)
                
                # adjust adjacent faces
                (
                    self.left[0][0], self.left[0][1], self.left[0][2],
                    self.front[0][0], self.front[0][1], self.front[0][2],
                    self.right[0][0], self.right[0][1], self.right[0][2],
                    self.back[0][0], self.back[0][1], self.back[0][2]
                ) = (
                    self.front[0][0], self.front[0][1], self.front[0][2],
                    self.right[0][0], self.right[0][1], self.right[0][2],
                    self.back[0][0], self.back[0][1], self.back[0][2],
                    self.left[0][0], self.left[0][1], self.left[0][2]
                )

            case "D":
                # rotate face itself
                self.down = self.get_rotated_face(self.down)
                
                # adjust adjacent faces
                (
                    self.left[2][2], self.left[2][1], self.left[2][0],
                    self.back[2][2], self.back[2][1], self.back[2][0],
                    self.right[2][2], self.right[2][1], self.right[2][0],
                    self.front[2][2], self.front[2][1], self.front[2][0]
                ) = (
                    self.back[2][2], self.back[2][1], self.back[2][0],
                    self.right[2][2], self.right[2][1], self.right[2][0],
                    self.front[2][2], self.front[2][1], self.front[2][0],
                    self.left[2][2], self.left[2][1], self.left[2][0],
                )
            
            case "F":
                # rotate face itself
                self.front = self.get_rotated_face(self.front)
                
                # adjust adjacent faces
                (
                    self.left[0][2], self.left[1][2], self.left[2][2],
                    self.down[0][0], self.down[0][1], self.down[0][2],
                    self.right[2][0], self.right[1][0], self.right[0][0],
                    self.up[2][2], self.up[2][1], self.up[2][0]
                ) = (
                    self.down[0][0], self.down[0][1], self.down[0][2],
                    self.right[2][0], self.right[1][0], self.right[0][0],
                    self.up[2][2], self.up[2][1], self.up[2][0],
                    self.left[0][2], self.left[1][2], self.left[2][2]
                )
            
            case "B":
                # rotate face itself
                self.back = self.get_rotated_face(self.back)
                
                # adjust adjacent faces
                (
                    self.right[0][2], self.right[1][2], self.right[2][2],
                    self.down[2][2], self.down[2][1], self.down[2][0],
                    self.left[2][0], self.left[1][0], self.left[0][0],
                    self.up[0][0], self.up[0][1], self.up[0][2]
                ) = (
                    self.down[2][2], self.down[2][1], self.down[2][0],
                    self.left[2][0], self.left[1][0], self.left[0][0],
                    self.up[0][0], self.up[0][1], self.up[0][2],
                    self.right[0][2], self.right[1][2], self.right[2][2]
                )
            
            case "L":
                # rotate face itself
                self.left = self.get_rotated_face(self.left)
                
                # adjust adjacent faces
                (
                    self.back[0][2], self.back[1][2], self.back[2][2],
                    self.down[2][0], self.down[1][0], self.down[0][0],
                    self.front[2][0], self.front[1][0], self.front[0][0],
                    self.up[2][0], self.up[1][0], self.up[0][0]
                ) = (
                    self.down[2][0], self.down[1][0], self.down[0][0],
                    self.front[2][0], self.front[1][0], self.front[0][0],
                    self.up[2][0], self.up[1][0], self.up[0][0],
                    self.back[0][2], self.back[1][2], self.back[2][2]
                )
            
            case "R":
                # rotate face itself
                self.right = self.get_rotated_face(self.right)
                
                # adjust adjacent faces
                (
                    self.front[0][2], self.front[1][2], self.front[2][2],
                    self.down[0][2], self.down[1][2], self.down[2][2],
                    self.back[2][0], self.back[1][0], self.back[0][0],
                    self.up[0][2], self.up[1][2], self.up[2][2]
                ) = (
                    self.down[0][2], self.down[1][2], self.down[2][2],
                    self.back[2][0], self.back[1][0], self.back[0][0],
                    self.up[0][2], self.up[1][2], self.up[2][2],
                    self.front[0][2], self.front[1][2], self.front[2][2]
                )

            case "U2":
                for _ in range(2):
                    self.rotate("U")

            case "D2":
                for _ in range(2):
                    self.rotate("D")

            case "F2":
                for _ in range(2):
                    self.rotate("F")

            case "B2":
                for _ in range(2):
                    self.rotate("B")

            case "L2":
                for _ in range(2):
                    self.rotate("L")

            case "R2":
                for _ in range(2):
                    self.rotate("R")

            case "U'":
                for _ in range(3):
                    self.rotate("U")

            case "D'":
                for _ in range(3):
                    self.rotate("D")

            case "F'":
                for _ in range(3):
                    self.rotate("F")

            case "B'":
                for _ in range(3):
                    self.rotate("B")

            case "L'":
                for _ in range(3):
                    self.rotate("L")

            case "R'":
                for _ in range(3):
                    self.rotate("R")

    # returns a single face after clockwise rotation was applied to it
    @staticmethod
    def get_rotated_face(face: list) -> list:
        rotated_face = [['' for _ in range(3)] for _ in range(3)]
        for i in range(3):
            for j in range(3):
                rotated_face[j][2 - i] = face[i][j]
        return rotated_face

    # prints rubik cube face colors in a grid
    def print(self, face: str=None) -> None:
        if face is not None:
            face = getattr(self, face)
            for i in range(3):
                print(face[i])
        else:
            blank = ' ' * 15
            print(blank, self.up[0], blank, blank)
            print(blank, self.up[1], blank, blank)
            print(blank, self.up[2], blank, blank)
            # print(blank, blank, blank, blank)
            print(self.left[0], self.front[0], self.right[0], self.back[0])
            print(self.left[1], self.front[1], self.right[1], self.back[1])
            print(self.left[2], self.front[2], self.right[2], self.back[2])
            # print(blank, blank, blank, blank)
            print(blank, self.down[0], blank, blank)
            print(blank, self.down[1], blank, blank)
            print(blank, self.down[2], blank, blank)
            print()
