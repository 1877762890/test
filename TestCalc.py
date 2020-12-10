import unittest
from  day15.testdemo.calc import Calc
from ddt import ddt
from ddt import data
from ddt import unpack

#加

data1=[
    [1,2,3],
    [9,-1,8],
    [-9,8,-1],
    [0,4,4],
    [100,100,200]
]
@ddt
class TestCalcAdd(unittest.TestCase):
    @data(*data1)
    @unpack
    def testAdd(self,s,t,y):
        a=s
        b=t
        p=y
        calc=Calc()


        sum=calc.add(a,b)

        self.assertEqual(p,sum)


#减

data2=[
    [3,2,1],
    [9,-1,10],
    [-9,8,-17],
    [0,4,-4],
    [-9,-8,-1]
]
@ddt
class TestCalcReduce(unittest.TestCase):
    @data(*data2)
    @unpack
    def testAdd(self, s1, t1, y1):
        c=s1
        d=t1
        p1=y1
        calc=Calc()


        send=calc.reduce(c,d)

        self.assertEqual(p1,send)


#乘

data3=[
    [3,2,6],
    [9,-1,-9],
    [-9,-1,9],
    [0,4,0]
]
@ddt
class TestCalcRide(unittest.TestCase):
    @data(*data3)
    @unpack
    def testAdd(self, s2, t2, y2):
        e = s2
        f = t2
        p2 =y2
        calc = Calc()

        mass = calc.ride(e, f)

        self.assertEqual(p2, mass)


#除
data4=[
    [6,2,3],
    [9,-1,-9],
    [-8,-4,2],
    [0,4,0]
]
@ddt
class TestCalcRemove(unittest.TestCase):
    @data(*data4)
    @unpack
    def testAdd(self, s3, t3, y3):
        j = s3
        k = t3
        p3 =y3
        calc = Calc()

        trade = calc.remove(j, k)

        self.assertEqual(p3, trade)




