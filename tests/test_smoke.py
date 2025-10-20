from bank_run_simulation.simulation import Simulation


def test_simulation_runs():
    sim = Simulation(n_banks=3, steps=2)
    result = sim.run()
    assert len(result) == 2
