import unittest
class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)

        return finishers

def func_frozen(func):
    def wrapper(self):
        if self.is_frozen == True:
           return self.skipTest('Тесты в этом кейсе заморожены')
        else:
            func
    return wrapper

class RunnerTest(unittest.TestCase):
    is_frozen = False

    @func_frozen
    def test_walk(self):
        func_runner = Runner('Walk')
        for i in range(10):
            func_runner.walk()
        self.assertEqual(func_runner.distance, 50)

    @func_frozen
    def test_run(self):
        func_runner = Runner('Run')
        for i in range(10):
            func_runner.run()
        self.assertEqual(func_runner.distance, 100)

    @func_frozen
    def test_chellenger(self):
        func_runner = Runner('Walk_1')
        func_runner_1 = Runner('Run_1')
        for i in range(10):
            func_runner.walk()
            func_runner_1.run()
        self.assertNotEqual(func_runner.distance, func_runner_1.distance)



class TournamentTest(unittest.TestCase):
    is_frozen = True

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.runner = Runner('Усэйн', 10)
        self.runner1 = Runner('Андрей', 9)
        self.runner2 = Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        for key in sorted(cls.all_results.keys()):
            print(cls.all_results[key])

    @func_frozen
    def test_1(self):
        tour = Tournament(90,self.runner, self.runner2)
        res = tour.start()
        self.all_results[1] = {1: res[1].name, 2: res[2].name}
        self.assertTrue(res[max(res)] == 'Ник')

    @func_frozen
    def test_2(self):
        tour = Tournament(90,self.runner1, self.runner2)
        res = tour.start()
        self.all_results[2] = {1: res[1].name, 2: res[2].name}
        self.assertTrue(res[max(res)] == 'Ник')

    @func_frozen
    def test_3(self):
        tour = Tournament(90, self.runner, self.runner1, self.runner2)
        res = tour.start()
        self.all_results[3] = {1: res[1].name, 2: res[2].name, 3: res[3].name}
        self.assertTrue(res[max(res)] == 'Ник')


if __name__ == '__main__':
    unittest.main()
