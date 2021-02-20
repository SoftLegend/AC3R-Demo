import json
import unittest
import numpy
from ac3r_plus import CrashScenario
from evolution import RandomEvolution, OpoEvolution, Selector, Mutator, Generator, Fitness, LogBook


def expectations(gens):
    # TODO: calculate maximum value for each scenario
    return [7 for _ in range(gens)]


class RandomEvolutionTest(unittest.TestCase):
    def test_run_scenario_in_population(self):
        self.assertEqual(0, 0)
        with open("./data/Case6.json") as file:
            scenario_data = json.load(file)
        orig_ind = CrashScenario.from_json(scenario_data)
        timeout = 60 * 20

        numpy.random.seed(64)

        rev = RandomEvolution(
            orig_ind=orig_ind,
            fitness=Fitness.evaluate,
            generate=Generator.generate_random_from,
            generate_params={"min": 10, "max": 50},
            select=Selector.select_best_ind,
            timeout=timeout
        )

        oev = OpoEvolution(
            orig_ind=orig_ind,
            fitness=Fitness.evaluate,
            generate=Generator.generate_random_from,
            generate_params={"min": 10, "max": 50},
            mutate=Mutator.mutate,
            mutate_params={"std": 0.5, "min": 10, "max": 50},
            select=Selector.select_best_ind,
            timeout=timeout
        )

        rev.run()
        oev.run()

        v = LogBook(expectations)
        v.print_logbook(rev.logbook)
        v.visualize_ind(rev.logbook, "Random")

        v.print_logbook(oev.logbook)
        v.visualize_ind(oev.logbook, "OPO")

        v.visualize(rev.logbook, oev.logbook, "Random", "OPO")


