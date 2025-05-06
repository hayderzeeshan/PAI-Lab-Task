def solve_n_queens(N):
    def backtrack(row, cols, diag1, diag2, current_solution):
        if row == N:
            solutions.append(current_solution[:])
            return
        
        for col in range(N):
            if col in cols or (row - col) in diag1 or (row + col) in diag2:
                continue

            cols.add(col)
            diag1.add(row - col)
            diag2.add(row + col)
            current_solution.append(col)
            backtrack(row + 1, cols, diag1, diag2, current_solution)

            current_solution.pop()
            cols.remove(col)
            diag1.remove(row - col)
            diag2.remove(row + col)

    solutions = []
    backtrack(0, set(), set(), set(), [])
    return solutions

def print_solutions(solutions):
    for solution in solutions:
        for row in solution:
            print(' '.join('Q' if col == row else '.' for col in range(len(solution))))
        print()
N = 4 
solutions = solve_n_queens(N)
print(f"Found {len(solutions)} solutions for N={N}:")
print_solutions(solutions)

