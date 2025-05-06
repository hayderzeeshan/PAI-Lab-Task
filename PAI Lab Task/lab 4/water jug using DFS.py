class WaterJugSolver:
    def __init__(self, capacity1, capacity2, target):
        self.capacity1 = capacity1
        self.capacity2 = capacity2
        self.target = target
        self.visited_states = set()
        self.solution_path = []

    def is_target_achieved(self, state):
        return state[0] == self.target or state[1] == self.target

    def get_next_possible_states(self, current_state):
        jug1, jug2 = current_state
        next_states = []
        next_states.append((self.capacity1, jug2))
        next_states.append((jug1, self.capacity2))
        next_states.append((0, jug2))
        next_states.append((jug1, 0))
        transfer_to_jug2 = min(jug1, self.capacity2 - jug2)
        next_states.append((jug1 - transfer_to_jug2, jug2 + transfer_to_jug2))
        transfer_to_jug1 = min(jug2, self.capacity1 - jug1)
        next_states.append((jug1 + transfer_to_jug1, jug2 - transfer_to_jug1))
        
        return next_states

    def dfs(self):
        stack = [(0, 0)]
        self.visited_states.add((0, 0))

        while stack:
            current_state = stack.pop()
            self.solution_path.append(current_state)
            if self.is_target_achieved(current_state):
                return self.solution_path
            for next_state in self.get_next_possible_states(current_state):
                if next_state not in self.visited_states:
                    stack.append(next_state)
                    self.visited_states.add(next_state)
        return None
    def display_solution(self):
        if self.solution_path:
            for step, state in enumerate(self.solution_path):
                print(f"Step {step}: Jug1 = {state[0]} liters, Jug2 = {state[1]} liters")
        else:
            print("No solution found.")
            
solver = WaterJugSolver(4, 3, 2)
solver.dfs()
solver.display_solution()
