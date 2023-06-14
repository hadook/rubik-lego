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
    
    # returns a new cube object that is a copy of the current object
    def copy(self):
        cube = Cube()
        cube.up = copy.deepcopy(self.up)
        cube.down = copy.deepcopy(self.down)
        cube.front = copy.deepcopy(self.front)
        cube.back = copy.deepcopy(self.back)
        cube.left = copy.deepcopy(self.left)
        cube.right = copy.deepcopy(self.right)
        return cube

    # constructs a cube instance from another cube object
    @classmethod
    def from_cube(cls, other: 'Cube'):
        cube = Cube()
        cube.up = copy.deepcopy(other.up)
        cube.down = copy.deepcopy(other.down)
        cube.front = copy.deepcopy(other.front)
        cube.back = copy.deepcopy(other.back)
        cube.left = copy.deepcopy(other.left)
        cube.right = copy.deepcopy(other.right)
        return cube
    
    # constructs a cube instance from string
    @classmethod
    def from_string(cls, colors: str):
        if len(colors) != 54:
            raise ValueError(f'Cube class constructor from_string expected string argument of length 54, got {len(colors)} instead.')
        
        cube = Cube()
        for num_face, face in enumerate(cube.faces):
            subset = colors[num_face*9:(num_face+1)*9]
            for i in range(3):
                for j in range(3):
                    face[i][j] = subset[i*3+j:i*3+j+1]
        return cube

    # constructs a cube instance from list
    @classmethod
    def from_list(cls, colors: list):
        if len(colors) != 54:
            raise ValueError(f'Cube class constructor from_list expected list argument of length 54, got {len(colors)} instead.')
        
        cube = Cube()
        for num_face, face in enumerate(cube.faces):
            subset = colors[num_face*9:(num_face+1)*9]
            for i in range(3):
                for j in range(3):
                    face[i][j] = subset[i*3+j]
        return cube

    # constructs a cube instance from dictionary
    @classmethod
    def from_dict(cls, faces: dict):
        cube = Cube()
        cube.up = copy.deepcopy(faces['up'])
        cube.down = copy.deepcopy(faces['down'])
        cube.front = copy.deepcopy(faces['front'])
        cube.back = copy.deepcopy(faces['back'])
        cube.left = copy.deepcopy(faces['left'])
        cube.right = copy.deepcopy(faces['right'])
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

    # return a list of possible solutions
    def solutions(self, max_moves: int = 30) -> list:
        solutions = []
        history = []
        self.__try_solve(self.copy(), solutions, history, max_moves, stop_on_first=False)
        return solutions

    # return first solution found
    def solve(self, max_moves: int = 30) -> list:
        solutions = []
        history = []
        self.__try_solve(self.copy(), solutions, history, max_moves, stop_on_first=True)
        
        if len(solutions) > 0:
            return solutions[0]
        else:
            return None

    # attempts to recursively solve the given cube (uses DFS recurrence)
    def __try_solve(self, cube: 'Cube', solutions: list, history: list, max_moves: int, stop_on_first: bool = True) -> None:

        # base scenarios, cube is solved or max recurrence depth reached
        if stop_on_first and len(solutions)>0:
            return
        if cube.is_solved:
            solutions.append(history.copy())
            return
        if max_moves == 0:
            return

        # try rotations
        last = ''
        if len(history) > 0:
            last = history[-1][:1]
        
        if last != 'U':
            self.__try_solve(cube.rotate("U"), solutions, [*history, "U"], max_moves-1, stop_on_first)
            self.__try_solve(cube.rotate("U2"), solutions, [*history, "U2"], max_moves-1, stop_on_first)
            self.__try_solve(cube.rotate("U'"), solutions, [*history, "U'"], max_moves-1, stop_on_first)
        if last != 'D':
            self.__try_solve(cube.rotate("D"), solutions, [*history, "D"], max_moves-1, stop_on_first)
            self.__try_solve(cube.rotate("D2"), solutions, [*history, "D2"], max_moves-1, stop_on_first)
            self.__try_solve(cube.rotate("D'"), solutions, [*history, "D'"], max_moves-1, stop_on_first)
        if last != 'F':
            self.__try_solve(cube.rotate("F"), solutions, [*history, "F"], max_moves-1, stop_on_first)
            self.__try_solve(cube.rotate("F2"), solutions, [*history, "F2"], max_moves-1, stop_on_first)
            self.__try_solve(cube.rotate("F'"), solutions, [*history, "F'"], max_moves-1, stop_on_first)
        if last != 'B':
            self.__try_solve(cube.rotate("B"), solutions, [*history, "B"], max_moves-1, stop_on_first)
            self.__try_solve(cube.rotate("B2"), solutions, [*history, "B2"], max_moves-1, stop_on_first)
            self.__try_solve(cube.rotate("B'"), solutions, [*history, "B'"], max_moves-1, stop_on_first)
        if last != 'L':
            self.__try_solve(cube.rotate("L"), solutions, [*history, "L"], max_moves-1, stop_on_first)
            self.__try_solve(cube.rotate("L2"), solutions, [*history, "L2"], max_moves-1, stop_on_first)
            self.__try_solve(cube.rotate("L'"), solutions, [*history, "L'"], max_moves-1, stop_on_first)
        if last != 'R':
            self.__try_solve(cube.rotate("R"), solutions, [*history, "R"], max_moves-1, stop_on_first)
            self.__try_solve(cube.rotate("R2"), solutions, [*history, "R2"], max_moves-1, stop_on_first)
            self.__try_solve(cube.rotate("R'"), solutions, [*history, "R'"], max_moves-1, stop_on_first)
    
    # scrambles the cube by applying a number of random moves
    def scramble(self, num_moves: int) -> list:
        history = []
        for _ in range(num_moves):
            move = random.choice(self.moves)
            if len(history) != 0:
                while move[:1] == history[-1][:1]:
                    move = random.choice(self.moves)
            self.rotate_ip(move)
            history.append(move)
        return history
    
    # rotate cube and return a new cube object (single face rotation)
    def rotate(self, move: str):
        cube = self.copy()
        cube.rotate_ip(move)
        return cube

    # rotate cube in place (single face rotation)
    def rotate_ip(self, move: str) -> None:
        match move:
            
            case "U":
                # rotate face itself
                self.up = self.__get_rotated_face(self.up)
                
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
                self.down = self.__get_rotated_face(self.down)
                
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
                self.front = self.__get_rotated_face(self.front)
                
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
                self.back = self.__get_rotated_face(self.back)
                
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
                self.left = self.__get_rotated_face(self.left)
                
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
                self.right = self.__get_rotated_face(self.right)
                
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
                    self.rotate_ip("U")

            case "D2":
                for _ in range(2):
                    self.rotate_ip("D")

            case "F2":
                for _ in range(2):
                    self.rotate_ip("F")

            case "B2":
                for _ in range(2):
                    self.rotate_ip("B")

            case "L2":
                for _ in range(2):
                    self.rotate_ip("L")

            case "R2":
                for _ in range(2):
                    self.rotate_ip("R")

            case "U'":
                for _ in range(3):
                    self.rotate_ip("U")

            case "D'":
                for _ in range(3):
                    self.rotate_ip("D")

            case "F'":
                for _ in range(3):
                    self.rotate_ip("F")

            case "B'":
                for _ in range(3):
                    self.rotate_ip("B")

            case "L'":
                for _ in range(3):
                    self.rotate_ip("L")

            case "R'":
                for _ in range(3):
                    self.rotate_ip("R")

    # apply a set of rotations, return a new cube object
    def rotations(self, moves: list):
        cube = self.copy()
        cube.rotations_ip(moves)
        return cube

    # apply a set of rotations in place
    def rotations_ip(self, moves: str) -> None:
        for move in moves:
            self.rotate_ip(move)

    # returns a single face after clockwise rotation was applied to it
    @staticmethod
    def __get_rotated_face(face: list) -> list:
        rotated_face = [['' for _ in range(3)] for _ in range(3)]
        for i in range(3):
            for j in range(3):
                rotated_face[j][2 - i] = face[i][j]
        return rotated_face

    # returns a user-friendly string representation of a cube object
    def __str__(self):
        blank = ' ' * 15
        lines = [
            ' '.join([blank, str(self.up[0]), blank, blank]),
            ' '.join([blank, str(self.up[1]), blank, blank]),
            ' '.join([blank, str(self.up[2]), blank, blank]),
            ' '.join([str(self.left[0]), str(self.front[0]), str(self.right[0]), str(self.back[0])]),
            ' '.join([str(self.left[1]), str(self.front[1]), str(self.right[1]), str(self.back[1])]),
            ' '.join([str(self.left[2]), str(self.front[2]), str(self.right[2]), str(self.back[2])]),
            ' '.join([blank, str(self.down[0]), blank, blank]),
            ' '.join([blank, str(self.down[1]), blank, blank]),
            ' '.join([blank, str(self.down[2]), blank, blank])
        ]
        return '\n'.join(lines)
