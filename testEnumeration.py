import unittest
import ast

from Enumerator import Enumerator


class EnumerationTestCases(unittest.TestCase):
    # Notice: the full, unpruned enumeration appears in the file, and
    # commented out lines are programs from the full enumeration that
    # need to be skipped with observational equivalence.
    def testEnumerate1(self):
        contexts = [{"x": 1,"y": 2, "z": 3}]
        enumerator = Enumerator([0,1],["x","y","z"],contexts)
        p1 = next(enumerator)
        self.assertEqual("x",ast.unparse(p1))
        self.assertEqual([1],p1.values)
        self.assertEqual("y",ast.unparse(next(enumerator))) # values: [2]
        self.assertEqual("z", ast.unparse(next(enumerator)))  # values: [3]
        self.assertEqual("0", ast.unparse(next(enumerator)))  # values: [0]
        #self.assertEqual("1", ast.unparse(next(enumerator)))  # values: [1]

        self.assertEqual("-x", ast.unparse(next(enumerator)))  # values: [-1]
        self.assertEqual("-y", ast.unparse(next(enumerator)))  # values: [-2]
        self.assertEqual("-z", ast.unparse(next(enumerator)))  # values: [-3]
        #self.assertEqual("-0", ast.unparse(next(enumerator)))  # values: [0]
        #self.assertEqual("-1", ast.unparse(next(enumerator)))  # values: [-1]

        #self.assertEqual("x + x", ast.unparse(next(enumerator)))  # values: [2]
        #self.assertEqual("x + y", ast.unparse(next(enumerator)))  # values: [3]
        self.assertEqual("x + z", ast.unparse(next(enumerator)))  # values: [4]
        #self.assertEqual("x + 0", ast.unparse(next(enumerator)))  # values: [1]
        #self.assertEqual("x + 1", ast.unparse(next(enumerator)))  # values: [2]

        #self.assertEqual("y + x", ast.unparse(next(enumerator)))  # values: [3]
        #self.assertEqual("y + y", ast.unparse(next(enumerator)))  # values: [4]
        self.assertEqual("y + z", ast.unparse(next(enumerator)))  # values: [5]
        #self.assertEqual("y + 0", ast.unparse(next(enumerator)))  # values: [2]
        #self.assertEqual("y + 1", ast.unparse(next(enumerator)))  # values: [3]

        #self.assertEqual("z + x", ast.unparse(next(enumerator)))  # values: [4]
        #self.assertEqual("z + y", ast.unparse(next(enumerator)))  # values: [5]
        self.assertEqual("z + z", ast.unparse(next(enumerator)))  # values: [6]
        #self.assertEqual("z + 0", ast.unparse(next(enumerator)))  # values: [3]
        #self.assertEqual("z + 1", ast.unparse(next(enumerator)))  # values: [4]

        #self.assertEqual("0 + x", ast.unparse(next(enumerator)))  # values: [1]
        #self.assertEqual("0 + y", ast.unparse(next(enumerator)))  # values: [2]
        #self.assertEqual("0 + z", ast.unparse(next(enumerator)))  # values: [3]
        #self.assertEqual("0 + 0", ast.unparse(next(enumerator)))  # values: [0]
        #self.assertEqual("0 + 1", ast.unparse(next(enumerator)))  # values: [1]

        #self.assertEqual("1 + x", ast.unparse(next(enumerator)))  # values: [2]
        #self.assertEqual("1 + y", ast.unparse(next(enumerator)))  # values: [3]
        #self.assertEqual("1 + z", ast.unparse(next(enumerator)))  # values: [4]
        #self.assertEqual("1 + 0", ast.unparse(next(enumerator)))  # values: [1]
        #self.assertEqual("1 + 1", ast.unparse(next(enumerator)))  # values: [2]

        #self.assertEqual("x - x", ast.unparse(next(enumerator)))  # values: [0]
        #self.assertEqual("x - y", ast.unparse(next(enumerator)))  # values: [-1]
        #self.assertEqual("x - z", ast.unparse(next(enumerator)))  # values: [-2]
        #self.assertEqual("x - 0", ast.unparse(next(enumerator)))  # values: [1]
        #self.assertEqual("x - 1", ast.unparse(next(enumerator)))  # values: [0]

        #self.assertEqual("y - x", ast.unparse(next(enumerator)))  # values: [1]
        #self.assertEqual("y - y", ast.unparse(next(enumerator)))  # values: [0]
        #self.assertEqual("y - z", ast.unparse(next(enumerator)))  # values: [-1]
        #self.assertEqual("y - 0", ast.unparse(next(enumerator)))  # values: [2]
        #self.assertEqual("y - 1", ast.unparse(next(enumerator)))  # values: [1]

        #self.assertEqual("z - x", ast.unparse(next(enumerator)))  # values: [2]
        #self.assertEqual("z - y", ast.unparse(next(enumerator)))  # values: [1]
        #self.assertEqual("z - z", ast.unparse(next(enumerator)))  # values: [0]
        #self.assertEqual("z - 0", ast.unparse(next(enumerator)))  # values: [3]
        #self.assertEqual("z - 1", ast.unparse(next(enumerator)))  # values: [2]

        #self.assertEqual("0 - x", ast.unparse(next(enumerator)))  # values: [-1]
        #self.assertEqual("0 - y", ast.unparse(next(enumerator)))  # values: [-2]
        #self.assertEqual("0 - z", ast.unparse(next(enumerator)))  # values: [-3]
        #self.assertEqual("0 - 0", ast.unparse(next(enumerator)))  # values: [0]
        #self.assertEqual("0 - 1", ast.unparse(next(enumerator)))  # values: [-1]

        #self.assertEqual("1 - x", ast.unparse(next(enumerator)))  # values: [0]
        #self.assertEqual("1 - y", ast.unparse(next(enumerator)))  # values: [-1]
        #self.assertEqual("1 - z", ast.unparse(next(enumerator)))  # values: [-2]
        #self.assertEqual("1 - 0", ast.unparse(next(enumerator)))  # values: [1]
        #self.assertEqual("1 - 1", ast.unparse(next(enumerator)))  # values: [0]

        #self.assertEqual("x * x", ast.unparse(next(enumerator)))  # values: [1]
        #self.assertEqual("x * y", ast.unparse(next(enumerator)))  # values: [2]
        #self.assertEqual("x * z", ast.unparse(next(enumerator)))  # values: [3]
        #self.assertEqual("x * 0", ast.unparse(next(enumerator)))  # values: [0]
        #self.assertEqual("x * 1", ast.unparse(next(enumerator)))  # values: [1]

        #self.assertEqual("y * x", ast.unparse(next(enumerator)))  # values: [2]
        #self.assertEqual("y * y", ast.unparse(next(enumerator)))  # values: [4]
        #self.assertEqual("y * z", ast.unparse(next(enumerator)))  # values: [6]
        #self.assertEqual("y * 0", ast.unparse(next(enumerator)))  # values: [0]
        #self.assertEqual("y * 1", ast.unparse(next(enumerator)))  # values: [2]

        #self.assertEqual("z * x", ast.unparse(next(enumerator)))  # values: [3]
        #self.assertEqual("z * y", ast.unparse(next(enumerator)))  # values: [6]
        self.assertEqual("z * z", ast.unparse(next(enumerator)))  # values: [9]
        #self.assertEqual("z * 0", ast.unparse(next(enumerator)))  # values: [0]
        #self.assertEqual("z * 1", ast.unparse(next(enumerator)))  # values: [3]

        #self.assertEqual("0 * x", ast.unparse(next(enumerator)))  # values: [0]
        #self.assertEqual("0 * y", ast.unparse(next(enumerator)))  # values: [0]
        #self.assertEqual("0 * z", ast.unparse(next(enumerator)))  # values: [0]
        #self.assertEqual("0 * 0", ast.unparse(next(enumerator)))  # values: [0]
        #self.assertEqual("0 * 1", ast.unparse(next(enumerator)))  # values: [0]

        #self.assertEqual("1 * x", ast.unparse(next(enumerator)))  # values: [1]
        #self.assertEqual("1 * y", ast.unparse(next(enumerator)))  # values: [2]
        #self.assertEqual("1 * z", ast.unparse(next(enumerator)))  # values: [3]
        #self.assertEqual("1 * 0", ast.unparse(next(enumerator)))  # values: [0]
        #self.assertEqual("1 * 1", ast.unparse(next(enumerator)))  # values: [1]

        #self.assertEqual("x // x", ast.unparse(next(enumerator)))  # values: [1]
        #self.assertEqual("x // y", ast.unparse(next(enumerator)))  # values: [0]
        #self.assertEqual("x // z", ast.unparse(next(enumerator)))  # values: [0]
        #self.assertEqual("x // 0", ast.unparse(next(enumerator)))  # values: ZeroDivisionError
        #self.assertEqual("x // 1", ast.unparse(next(enumerator)))  # values: [1]

        #self.assertEqual("y // x", ast.unparse(next(enumerator)))  # values: [2]
        #self.assertEqual("y // y", ast.unparse(next(enumerator)))  # values: [1]
        #self.assertEqual("y // z", ast.unparse(next(enumerator)))  # values: [0]
        #self.assertEqual("y // 0", ast.unparse(next(enumerator)))  # values: ZeroDivisionError
        #self.assertEqual("y // 1", ast.unparse(next(enumerator)))  # values: [2]

        #self.assertEqual("z // x", ast.unparse(next(enumerator)))  # values: [3]
        #self.assertEqual("z // y", ast.unparse(next(enumerator)))  # values: [1]
        #self.assertEqual("z // z", ast.unparse(next(enumerator)))  # values: [1]
        #self.assertEqual("z // 0", ast.unparse(next(enumerator)))  # values: ZeroDivisionError
        #self.assertEqual("z // 1", ast.unparse(next(enumerator)))  # values: [3]

        #self.assertEqual("0 // x", ast.unparse(next(enumerator)))  # values: [0]
        #self.assertEqual("0 // y", ast.unparse(next(enumerator)))  # values: [0]
        #self.assertEqual("0 // z", ast.unparse(next(enumerator)))  # values: [0]
        #self.assertEqual("0 // 0", ast.unparse(next(enumerator)))  # values: ZeroDivisionError
        #self.assertEqual("0 // 1", ast.unparse(next(enumerator)))  # values: [0]

        #self.assertEqual("1 // x", ast.unparse(next(enumerator)))  # values: [1]
        #self.assertEqual("1 // y", ast.unparse(next(enumerator)))  # values: [0]
        #self.assertEqual("1 // z", ast.unparse(next(enumerator)))  # values: [0]
        #self.assertEqual("1 // 0", ast.unparse(next(enumerator)))  # values: ZeroDivisionError
        #self.assertEqual("1 // 1", ast.unparse(next(enumerator)))  # values: [1]

        #self.assertEqual("x % x", ast.unparse(next(enumerator)))  # values: [0]
        #self.assertEqual("x % y", ast.unparse(next(enumerator)))  # values: [1]
        #self.assertEqual("x % z", ast.unparse(next(enumerator)))  # values: [1]
        #self.assertEqual("x % 0", ast.unparse(next(enumerator)))  # values: ZeroDivisionError
        #self.assertEqual("x % 1", ast.unparse(next(enumerator)))  # values: [0]

        #self.assertEqual("y % x", ast.unparse(next(enumerator)))  # values: [0]
        #self.assertEqual("y % y", ast.unparse(next(enumerator)))  # values: [0]
        #self.assertEqual("y % z", ast.unparse(next(enumerator)))  # values: [2]
        #self.assertEqual("y % 0", ast.unparse(next(enumerator)))  # values: ZeroDivisionError
        #self.assertEqual("y % 1", ast.unparse(next(enumerator)))  # values: [0]

        #self.assertEqual("z % x", ast.unparse(next(enumerator)))  # values: [0]
        #self.assertEqual("z % y", ast.unparse(next(enumerator)))  # values: [0]
        #self.assertEqual("z % z", ast.unparse(next(enumerator)))  # values: [0]
        #self.assertEqual("z % 0", ast.unparse(next(enumerator)))  # values: ZeroDivisionError
        #self.assertEqual("z % 1", ast.unparse(next(enumerator)))  # values: [0]

        #self.assertEqual("0 % x", ast.unparse(next(enumerator)))  # values: [0]
        #self.assertEqual("0 % y", ast.unparse(next(enumerator)))  # values: [0]
        #self.assertEqual("0 % z", ast.unparse(next(enumerator)))  # values: [0]
        #self.assertEqual("0 % 0", ast.unparse(next(enumerator)))  # values: ZeroDivisionError
        #self.assertEqual("0 % 1", ast.unparse(next(enumerator)))  # values: [0]

        #self.assertEqual("1 % x", ast.unparse(next(enumerator)))  # values: [0]
        #self.assertEqual("1 % y", ast.unparse(next(enumerator)))  # values: [1]
        #self.assertEqual("1 % z", ast.unparse(next(enumerator)))  # values: [1]
        #self.assertEqual("1 % 0", ast.unparse(next(enumerator)))  # values: ZeroDivisionError
        #self.assertEqual("1 % 1", ast.unparse(next(enumerator)))  # values: [0]

        #self.assertEqual("--x", ast.unparse(next(enumerator)))  # values: [1]
        #self.assertEqual("--y", ast.unparse(next(enumerator)))  # values: [2]
        #self.assertEqual("--z", ast.unparse(next(enumerator)))  # values: [3]
        #self.assertEqual("--0", ast.unparse(next(enumerator)))  # values: [0]
        #self.assertEqual("--1", ast.unparse(next(enumerator)))  # values: [1]

        #self.assertEqual("-(x + x)", ast.unparse(next(enumerator)))  # values: [3]
        #self.assertEqual("-(x + y)", ast.unparse(next(enumerator)))  # values: [3]
        #self.assertEqual("-(x + z)", ast.unparse(next(enumerator)))  # values: [4]
        #self.assertEqual("-(x + 0)", ast.unparse(next(enumerator)))  # values: [1]
        #self.assertEqual("-(x + 1)", ast.unparse(next(enumerator)))  # values: [2]

    def testEnumerate2(self):
        contexts = [{"x": 1,"y": 2},{"x": 8,"y": 2}]
        enumerator = Enumerator([0,1],["x","y"],contexts)
        self.assertEqual("x", ast.unparse(next(enumerator)))  # values: [1,8]
        self.assertEqual("y", ast.unparse(next(enumerator)))  # values: [2,2]
        self.assertEqual("0", ast.unparse(next(enumerator)))  # values: [0,0]
        self.assertEqual("1", ast.unparse(next(enumerator)))  # values: [1,1]

        self.assertEqual("-x", ast.unparse(next(enumerator)))  # values: [-1,-8]
        self.assertEqual("-y", ast.unparse(next(enumerator)))  # values: [-2,-2]
        #self.assertEqual("-0", ast.unparse(next(enumerator)))  # values: [0,0]
        self.assertEqual("-1", ast.unparse(next(enumerator)))  # values: [-1,-1]

        self.assertEqual("x + x", ast.unparse(next(enumerator)))  # values: [2,16]
        self.assertEqual("x + y", ast.unparse(next(enumerator)))  # values: [3,10]
        #self.assertEqual("x + 0", ast.unparse(next(enumerator)))  # values: [1,8]
        self.assertEqual("x + 1", ast.unparse(next(enumerator)))  # values: [2,9]

        #self.assertEqual("y + x", ast.unparse(next(enumerator)))  # values: [3,10]
        self.assertEqual("y + y", ast.unparse(next(enumerator)))  # values: [4,4]
        #self.assertEqual("y + 0", ast.unparse(next(enumerator)))  # values: [2,2]
        self.assertEqual("y + 1", ast.unparse(next(enumerator)))  # values: [3,3]

        #self.assertEqual("0 + x", ast.unparse(next(enumerator)))  # values: [1,8]
        #self.assertEqual("0 + y", ast.unparse(next(enumerator)))  # values: [2,2]
        #self.assertEqual("0 + 0", ast.unparse(next(enumerator)))  # values: [0,0]
        #self.assertEqual("0 + 1", ast.unparse(next(enumerator)))  # values: [1,1]

        #self.assertEqual("1 + x", ast.unparse(next(enumerator)))  # values: [2,9]
        #self.assertEqual("1 + y", ast.unparse(next(enumerator)))  # values: [3,3]
        #self.assertEqual("1 + 0", ast.unparse(next(enumerator)))  # values: [1,1]
        #self.assertEqual("1 + 1", ast.unparse(next(enumerator)))  # values: [2,2]

        #self.assertEqual("x - x", ast.unparse(next(enumerator)))  # values: [0,0]
        self.assertEqual("x - y", ast.unparse(next(enumerator)))  # values: [-1,6]
        #self.assertEqual("x - 0", ast.unparse(next(enumerator)))  # values: [1,8]
        self.assertEqual("x - 1", ast.unparse(next(enumerator)))  # values: [0,7]

        self.assertEqual("y - x", ast.unparse(next(enumerator)))  # values: [1,-6]
        #self.assertEqual("y - y", ast.unparse(next(enumerator)))  # values: [0,0]
        #self.assertEqual("y - 0", ast.unparse(next(enumerator)))  # values: [2,2]
        #self.assertEqual("y - 1", ast.unparse(next(enumerator)))  # values: [1,1]

        #self.assertEqual("0 - x", ast.unparse(next(enumerator)))  # values: [-1,-8]
        #self.assertEqual("0 - y", ast.unparse(next(enumerator)))  # values: [-2,-2]
        #self.assertEqual("0 - 0", ast.unparse(next(enumerator)))  # values: [0,0]
        #self.assertEqual("0 - 1", ast.unparse(next(enumerator)))  # values: [-1,-1]

        self.assertEqual("1 - x", ast.unparse(next(enumerator)))  # values: [0,-7]
        #self.assertEqual("1 - y", ast.unparse(next(enumerator)))  # values: [-1,-1]
        #self.assertEqual("1 - 0", ast.unparse(next(enumerator)))  # values: [1,1]
        #self.assertEqual("1 - 1", ast.unparse(next(enumerator)))  # values: [0,0]

        self.assertEqual("x * x", ast.unparse(next(enumerator)))  # values: [1,64]
        #self.assertEqual("x * y", ast.unparse(next(enumerator)))  # values: [2,16]
        #self.assertEqual("x * 0", ast.unparse(next(enumerator)))  # values: [0,0]
        #self.assertEqual("x * 1", ast.unparse(next(enumerator)))  # values: [1,8]

        #self.assertEqual("y * x", ast.unparse(next(enumerator)))  # values: [2,16]
        #self.assertEqual("y * y", ast.unparse(next(enumerator)))  # values: [4,4]
        #self.assertEqual("y * 0", ast.unparse(next(enumerator)))  # values: [0,0]
        #self.assertEqual("y * 1", ast.unparse(next(enumerator)))  # values: [2,2]

        #self.assertEqual("0 * x", ast.unparse(next(enumerator)))  # values: [0,0]
        #self.assertEqual("0 * y", ast.unparse(next(enumerator)))  # values: [0,0]
        #self.assertEqual("0 * 0", ast.unparse(next(enumerator)))  # values: [0,0]
        #self.assertEqual("0 * 1", ast.unparse(next(enumerator)))  # values: [0,0]

        #self.assertEqual("1 * x", ast.unparse(next(enumerator)))  # values: [1,8]
        #self.assertEqual("1 * y", ast.unparse(next(enumerator)))  # values: [2,2]
        #self.assertEqual("1 * 0", ast.unparse(next(enumerator)))  # values: [0,0]
        #self.assertEqual("1 * 1", ast.unparse(next(enumerator)))  # values: [1,1]

        #self.assertEqual("x // x", ast.unparse(next(enumerator)))  # values: [1,1]
        self.assertEqual("x // y", ast.unparse(next(enumerator)))  # values: [0,4]
        #self.assertEqual("x // 0", ast.unparse(next(enumerator)))  # values: ZeroDivisionError
        #self.assertEqual("x // 1", ast.unparse(next(enumerator)))  # values: [1,8]

        self.assertEqual("y // x", ast.unparse(next(enumerator)))  # values: [2,0]
        #self.assertEqual("y // y", ast.unparse(next(enumerator)))  # values: [1,1]
        #self.assertEqual("y // 0", ast.unparse(next(enumerator)))  # values: ZeroDivisionError
        #self.assertEqual("y // 1", ast.unparse(next(enumerator)))  # values: [2,2]

        #self.assertEqual("0 // x", ast.unparse(next(enumerator)))  # values: [0,0]
        #self.assertEqual("0 // y", ast.unparse(next(enumerator)))  # values: [0,0]
        #self.assertEqual("0 // 0", ast.unparse(next(enumerator)))  # values: ZeroDivisionError
        #self.assertEqual("0 // 1", ast.unparse(next(enumerator)))  # values: [0,0]

        self.assertEqual("1 // x", ast.unparse(next(enumerator)))  # values: [1,0]
        #self.assertEqual("1 // y", ast.unparse(next(enumerator)))  # values: [0,0]
        #self.assertEqual("1 // 0", ast.unparse(next(enumerator)))  # values: ZeroDivisionError
        #self.assertEqual("1 // 1", ast.unparse(next(enumerator)))  # values: [1,1]

        #self.assertEqual("x % x", ast.unparse(next(enumerator)))  # values: [0,0]
        #self.assertEqual("x % y", ast.unparse(next(enumerator)))  # values: [1,0]
        #self.assertEqual("x % 0", ast.unparse(next(enumerator)))  # values: ZeroDivisionError
        #self.assertEqual("x % 1", ast.unparse(next(enumerator)))  # values: [0,0]

        self.assertEqual("y % x", ast.unparse(next(enumerator)))  # values: [0,2]
        #self.assertEqual("y % y", ast.unparse(next(enumerator)))  # values: [0,0]
        #self.assertEqual("y % 0", ast.unparse(next(enumerator)))  # values: ZeroDivisionError
        #self.assertEqual("y % 1", ast.unparse(next(enumerator)))  # values: [0,0]

        #self.assertEqual("0 % x", ast.unparse(next(enumerator)))  # values: [0,0]
        #self.assertEqual("0 % y", ast.unparse(next(enumerator)))  # values: [0,0]
        #self.assertEqual("0 % 0", ast.unparse(next(enumerator)))  # values: ZeroDivisionError
        #self.assertEqual("0 % 1", ast.unparse(next(enumerator)))  # values: [0,0]

        self.assertEqual("1 % x", ast.unparse(next(enumerator)))  # values: [0,1]
        #self.assertEqual("1 % y", ast.unparse(next(enumerator)))  # values: [1,1]
        #self.assertEqual("1 % 0", ast.unparse(next(enumerator)))  # values: ZeroDivisionError
        #self.assertEqual("1 % 1", ast.unparse(next(enumerator)))  # values: [0,0]

        #self.assertEqual("--x", ast.unparse(next(enumerator)))  # values: [1,8]
        #self.assertEqual("--y", ast.unparse(next(enumerator)))  # values: [2,2]
        #self.assertEqual("--0", ast.unparse(next(enumerator)))  # values: [0,0]
        #self.assertEqual("--1", ast.unparse(next(enumerator)))  # values: [1,1]

        self.assertEqual("-(x + x)", ast.unparse(next(enumerator)))  # values: [-2,-16]
        self.assertEqual("-(x + y)", ast.unparse(next(enumerator)))  # values: [-3,-10]
        #self.assertEqual("-(x + 0)", ast.unparse(next(enumerator)))  # values: [-1,-8]
        self.assertEqual("-(x + 1)", ast.unparse(next(enumerator)))  # values: [-2,-9]

    def testEnumerate3(self):
        contexts = [{"x": 1}, {"x": 8}, {"x": 2}]
        enumerator = Enumerator([0,1],["x"],contexts)
        self.assertEqual("x", ast.unparse(next(enumerator)))  # values: [1,8,2]
        self.assertEqual("0", ast.unparse(next(enumerator)))  # values: [0,0,0]
        self.assertEqual("1", ast.unparse(next(enumerator)))  # values: [1,1,1]

        self.assertEqual("-x", ast.unparse(next(enumerator)))  # values: [-1,-8,-2]
        #self.assertEqual("-0", ast.unparse(next(enumerator)))  # values: [0,0,0]
        self.assertEqual("-1", ast.unparse(next(enumerator)))  # values: [-1,-1,-1]

        self.assertEqual("x + x", ast.unparse(next(enumerator)))  # values: [2,16,4]
        #self.assertEqual("x + 0", ast.unparse(next(enumerator)))  # values: [1,8,2]
        self.assertEqual("x + 1", ast.unparse(next(enumerator)))  # values: [2,9,3]

        #self.assertEqual("0 + x", ast.unparse(next(enumerator)))  # values: [1,8,2]
        #self.assertEqual("0 + 0", ast.unparse(next(enumerator)))  # values: [0,0,0]
        #self.assertEqual("0 + 1", ast.unparse(next(enumerator)))  # values: [1,1,1]

        #self.assertEqual("1 + x", ast.unparse(next(enumerator)))  # values: [2,9,3]
        #self.assertEqual("1 + 0", ast.unparse(next(enumerator)))  # values: [1,1,1]
        self.assertEqual("1 + 1", ast.unparse(next(enumerator)))  # values: [2,2,2]

        #self.assertEqual("x - x", ast.unparse(next(enumerator)))  # values: [0,0,0]
        #self.assertEqual("x - 0", ast.unparse(next(enumerator)))  # values: [1,8,2]
        self.assertEqual("x - 1", ast.unparse(next(enumerator)))  # values: [0,7,1]

        #self.assertEqual("0 - x", ast.unparse(next(enumerator)))  # values: [-1,-8,-2]
        #self.assertEqual("0 - 0", ast.unparse(next(enumerator)))  # values: [0,0,0]
        #self.assertEqual("0 - 1", ast.unparse(next(enumerator)))  # values: [-1,-1,-1]

        self.assertEqual("1 - x", ast.unparse(next(enumerator)))  # values: [0,-7,-1]
        #self.assertEqual("1 - 0", ast.unparse(next(enumerator)))  # values: [1,1,1]
        #self.assertEqual("1 - 1", ast.unparse(next(enumerator)))  # values: [0,0,0]

        self.assertEqual("x * x", ast.unparse(next(enumerator)))  # values: [1,64,4]
        #self.assertEqual("x * 0", ast.unparse(next(enumerator)))  # values: [0,0,0]
        #self.assertEqual("x * 1", ast.unparse(next(enumerator)))  # values: [1,8,2]

        #self.assertEqual("0 * x", ast.unparse(next(enumerator)))  # values: [0,0,0]
        #self.assertEqual("0 * 0", ast.unparse(next(enumerator)))  # values: [0,0,0]
        #self.assertEqual("0 * 1", ast.unparse(next(enumerator)))  # values: [0,0,0]

        #self.assertEqual("1 * x", ast.unparse(next(enumerator)))  # values: [1,8,2]
        #self.assertEqual("1 * 0", ast.unparse(next(enumerator)))  # values: [0,0,0]
        #self.assertEqual("1 * 1", ast.unparse(next(enumerator)))  # values: [1,1,1]

        #self.assertEqual("x // x", ast.unparse(next(enumerator)))  # values: [1,1,1]
        #self.assertEqual("x // 0", ast.unparse(next(enumerator)))  # values: ZeroDivisionError
        #self.assertEqual("x // 1", ast.unparse(next(enumerator)))  # values: [1,8,2]

        #self.assertEqual("0 // x", ast.unparse(next(enumerator)))  # values: [0,0,0]
        #self.assertEqual("0 // 0", ast.unparse(next(enumerator)))  # values: ZeroDivisionError
        #self.assertEqual("0 // 1", ast.unparse(next(enumerator)))  # values: [0,0,0]

        self.assertEqual("1 // x", ast.unparse(next(enumerator)))  # values: [1,0,0]
        #self.assertEqual("1 // 0", ast.unparse(next(enumerator)))  # values: ZeroDivisionError
        #self.assertEqual("1 // 1", ast.unparse(next(enumerator)))  # values: [1,1,1]

        #self.assertEqual("x % x", ast.unparse(next(enumerator)))  # values: [0,0,0]
        #self.assertEqual("x % 0", ast.unparse(next(enumerator)))  # values: ZeroDivisionError
        #self.assertEqual("x % 1", ast.unparse(next(enumerator)))  # values: [0,0,0]

        #self.assertEqual("0 % x", ast.unparse(next(enumerator)))  # values: [0,0,0]
        #self.assertEqual("0 % 0", ast.unparse(next(enumerator)))  # values: ZeroDivisionError
        #self.assertEqual("0 % 1", ast.unparse(next(enumerator)))  # values: [0,0,0]

        self.assertEqual("1 % x", ast.unparse(next(enumerator)))  # values: [0,1,1]
        #self.assertEqual("1 % 0", ast.unparse(next(enumerator)))  # values: ZeroDivisionError
        #self.assertEqual("1 % 1", ast.unparse(next(enumerator)))  # values: [0,0,0]

        #self.assertEqual("--x", ast.unparse(next(enumerator)))  # values: [1,8,2]
        #self.assertEqual("--0", ast.unparse(next(enumerator)))  # values: [0,0,0]
        #self.assertEqual("--1", ast.unparse(next(enumerator)))  # values: [1,1,1]

        self.assertEqual("-(x + x)", ast.unparse(next(enumerator)))  # values: [-2,-16,-4]
        #self.assertEqual("-(x + 0)", ast.unparse(next(enumerator)))  # values: [-1,-8,-2]
        self.assertEqual("-(x + 1)", ast.unparse(next(enumerator)))  # values: [-2,-9,-3]

        #self.assertEqual("-(0 + x)", ast.unparse(next(enumerator)))  # values: [-1,-8,-2]
        #self.assertEqual("-(0 + 0)", ast.unparse(next(enumerator)))  # values: [0,0,0]
        #self.assertEqual("-(0 + 1)", ast.unparse(next(enumerator)))  # values: [-1,-1,-1]

if __name__ == '__main__':
    unittest.main()
