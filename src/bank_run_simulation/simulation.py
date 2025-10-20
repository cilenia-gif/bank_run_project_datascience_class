class Simulation:
    def __init__(self, n_banks=5, steps=3):
        self.n_banks = n_banks
        self.steps = steps

    def run(self):
        print(f"Running simulation with {self.n_banks} banks for {self.steps} steps")
        return list(range(self.steps))
