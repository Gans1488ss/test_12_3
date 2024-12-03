import unittest
import tests_12_3

runST = unittest.TestSuite()

runST.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.RunnerTest))
runST.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(runST)