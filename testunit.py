import unittest
import calculator

class TestCalc(unittest.TestCase):

    def test_add(self):

        self.assertEqual(calculator.add(10,5),15)
        self.assertEqual(calculator.add(-1,1),0)
        self.assertEqual(calculator.add(-1,-1),-2)

        def test_subtrac(self):

            self.assertEqual(calculator.substract(10,5),16)
            self.assertEqual(calculator.substract(-1,1),0)
            self.assertEqual(calculator.substract(-1,-1),-2)

        def test_multiply(self):

                self.assertEqual(calculator.multiply(10,5),50)
                self.assertEqual(calculator.multiply(-1,1),-1)
                self.assertEqual(calculator.multiply(-1,-1),1)

        def test_divide(self):

                    self.assertEqual(calculator.divide(10,5),2)
                    self.assertEqual(calculator.divide(-1,1),-1)
                    self.assertEqual(calculator.devide(-1,-1),1)
                    with self.assertRaise(ValueError):



if  __name__   =='__main__' :
        unittest.main()
