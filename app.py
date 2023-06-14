from rubik import Cube


cube = Cube()

scramble = cube.scramble(4)
print('\n' + 'scramble:', scramble)

print('\n' + 'starting position:')
print(cube)

print('\n' + 'solutions:')
solutions = cube.solutions(5)
for solution in solutions:
    print(solution)
