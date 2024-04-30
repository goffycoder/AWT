import numpy as np

def read_matrix(prompt):
    print(prompt)
    return np.array([list(map(int, input("Enter row {} (separated by spaces): ".format(i+1)).split())) for i in range(3)])

start_matrix = read_matrix("Enter the start matrix (3x3) row by row:")
end_matrix = read_matrix("Enter the end matrix (3x3) row by row:")

visited = []
open = []
closed = []

closed.append(start_matrix)

def heuristic(matrix, end_matrix):
    res = matrix == end_matrix
    return 9 - np.count_nonzero(res)

def possibleChildren(matrix, e_matrix):
    visited.append(matrix)
    [i],[j] = np.where(matrix == 0)
    direction = [[-1, 0], [0, -1], [1, 0],[0, 1]]
    children = []
    for dir in direction:
        ni = i + dir[0]
        nj = j + dir[1]
        newMatrix = matrix.copy()
        if 0 <= ni <= 2 and 0 <= nj <= 2:
            newMatrix[i, j], newMatrix[ni, nj] = matrix[ni, nj], matrix[i, j]
            if not any(np.array_equal(newMatrix, visited_mat) for visited_mat in visited):
                visited.append(newMatrix)
                newMatrix_heu = heuristic(newMatrix, end_matrix)
                children.append([newMatrix_heu, newMatrix])

    children = sorted(children, key=lambda x: x[0])
    return [child[1] for child in children]

def main(start_matrix, end_matrix):
    start_heuristic = heuristic(start_matrix, end_matrix)
    if start_heuristic == 0:
        for node in closed:
            print(node)
        return True
    else:
        children = possibleChildren(start_matrix, end_matrix)
        for child in children:
            open.append(child)

        while open:
            newMatrix = open.pop(0)
            newHeu = heuristic(newMatrix, end_matrix)
            closed.append(newMatrix)

            if newHeu == 0:
                for node in closed:
                    print(node)
                return True
            else:
                children = possibleChildren(newMatrix, end_matrix)
                for child in children:
                    open.append(child)

        return False

if __name__ == "__main__":
    main(start_matrix, end_matrix)
