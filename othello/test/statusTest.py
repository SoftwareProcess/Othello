'''
Created on Mar 27, 2020

@author:    Tae Myles
'''
from unittest import TestCase
from othello.status import _status as status


class StatusTest(TestCase):
    def setUp(self):
        self.parms = {'op': 'status', 'light': '1', 'dark': '2', 'blank': '0',
            'board': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 0, 0, 0, 0, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            'integrity': '6c3ec0129f5e128f48e2541bd6663a52a825c35f99b9a69d9593f2fc44b0bb4b'}
            
    def tearDown(self):
        self.parms = {'op': 'status', 'light': '1', 'dark': '2', 'blank:': '0',
            'board': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 0, 0, 0, 0, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            'integrity': '6c3ec0129f5e128f48e2541bd6663a52a825c35f99b9a69d9593f2fc44b0bb4b'}

    def test900_AboveBoundLight(self):
        self.setUp()
        self.parms['light'] = '10'
        expected = 'error: above bound light value'
        self.actual = status(self.parms)
        self.assertEqual(expected, self.actual['status'])
        self.tearDown()

    def test901_BelowBoundLight(self):
        self.setUp()
        self.parms['light'] = '-1'
        expected = 'error: below bound light value'
        self.actual = status(self.parms)
        self.assertEqual(expected, self.actual['status'])
        self.tearDown()
        
    def test902_NonIntegerLight(self):
        self.setUp()
        self.parms['light'] = 'X'
        expected = 'error: non-integer light value'
        self.actual = status(self.parms)
        self.assertEqual(expected, self.actual['status'])
        self.tearDown()
        
    def test903_NullLight(self):
        self.setUp()
        self.parms['light'] = None
        expected = 'error: Null light value'
        self.actual = status(self.parms)
        self.assertEqual(expected, self.actual['status'])
        self.tearDown()
        
    def test910_AboveBoundDark(self):
        self.setUp()
        self.parms['dark'] = '10'
        expected = 'error: above bound dark value'
        self.actual = status(self.parms)
        self.assertEqual(expected, self.actual['status'])
        self.tearDown()
        
    def test911_BelowBoundDark(self):
        self.setUp()
        self.parms['dark'] = '-1'
        expected = 'error: below bound dark value'
        self.actual = status(self.parms)
        self.assertEqual(expected, self.actual['status'])
        self.tearDown()
        
    def test912_NonIntegerDark(self):
        self.setUp()
        self.parms['dark'] = '1.2'
        expected = 'error: non-integer dark value'
        self.actual = status(self.parms)
        self.assertEqual(expected, self.actual['status'])
        self.tearDown()
        
    def test913_NullDark(self):
        self.setUp()
        self.parms['dark'] = None
        expected = 'error: Null dark value'
        self.actual = status(self.parms)
        self.assertEqual(expected, self.actual['status'])
        self.tearDown()
        
    def test920_AboveBoundBlank(self):
        self.setUp()
        self.parms['blank'] = '10'
        expected = 'error: above bound blank value'
        self.actual = status(self.parms)
        self.assertEqual(expected, self.actual['status'])
        self.tearDown()

    def test921_BelowBoundBlank(self):
        self.setUp()
        self.parms['blank'] = '-1'
        expected = 'error: below bound blank value'
        self.actual = status(self.parms)
        self.assertEqual(expected, self.actual['status'])
        self.tearDown()
        
    def test922_NonIntegerBlank(self):
        self.setUp()
        self.parms['blank'] = '1E5'
        expected = 'error: non-integer blank value'
        self.actual = status(self.parms)
        self.assertEqual(expected, self.actual['status'])
        self.tearDown()
        
    def test923_NullBlank(self):
        self.setUp()
        self.parms['blank'] = None
        expected = 'error: Null blank value'
        self.actual = status(self.parms)
        self.assertEqual(expected, self.actual['status'])
        self.tearDown()
        
    def test930_NonSquaredBoard(self):
        self.setUp()
        self.parms['light'] = 1
        self.parms['dark'] = 2
        self.parms['blank'] = 3
        self.parms['board'] = [3,3,3,3,3,3,3,3,
                               3,3,3,3,3,3,1,2,
                               3,3,3,3,2,1,3,3,
                               3,3,3,3,3,3,3,3,
                               3,3,3]
        expected = 'error: uneven board'
        self.actual = status(self.parms)
        self.assertEqual(expected, self.actual['status'])
        self.tearDown() 
        
    def test931_OddxOddBoard(self):
        self.setUp()
        self.parms['light'] = 1
        self.parms['dark'] = 2
        self.parms['blank'] = 3
        self.parms['board'] = [3,3,3,3,3,3,
                               3,3,3,3,3,3,
                               3,3,1,2,3,3,
                               3,3,2,1,3,3,
                               3,3,3,3,3,3,
                               3,3,3,3,3,3,
                               3,3,3,3,3,3,
                               3,3,3,3,3,3,3]
        expected = 'error: uneven board'
        self.actual = status(self.parms)
        self.assertEqual(expected, self.actual['status'])
        self.tearDown() 
           
    def test932_MissingBoard(self):
        self.setUp()
        self.parms['light'] = 1
        self.parms['dark'] = 2
        self.parms['blank'] = 3
        del self.parms['board']
        expected = 'error: board does not exist'
        self.actual = status(self.parms)
        self.assertEqual(expected, self.actual['status'])
        self.tearDown()

    def test933_NullBoard(self):
        self.setUp()
        self.parms['light'] = 1
        self.parms['dark'] = 2
        self.parms['blank'] = 3
        self.parms['board'] = None
        expected = 'error: null board'
        self.actual = status(self.parms)
        self.assertEqual(expected, self.actual['status'])
        self.tearDown()  
        
    def test940_shortIntegrity(self):
        self.setUp()
        self.parms['integrity'] = 'f01977c17f801c43eeb13fb9f74a49bd0c761db3cdffe01510f47ddd23ab465'
        expected = 'error: short integrity'
        self.actual = status(self.parms)
        self.assertEqual(expected, self.actual['status'])
        self.tearDown()  
