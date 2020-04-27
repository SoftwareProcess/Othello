'''
    Created on Apr 26, 2020
    
    @author:    Tae Myles
'''
from unittest import TestCase
from othello.place import _place as place


class Test(TestCase):
    def setUp(self):
        self.parms = {'op': 'place', 'light': '1', 'dark': '2', 'blank': '0', 'location': '1:1',
                      'board': [0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,2,0,0,0,0,2,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                      'integrity': '6c3ec0129f5e128f48e2541bd6663a52a825c35f99b9a69d9593f2fc44b0bb4b'
                      }


    def tearDown(self):
        self.parms = {'op': 'place', 'light': '1', 'dark': '2', 'blank': '0', 'location': '1:1',
                      'board': [0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,2,0,0,0,0,2,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                      'integrity': '6c3ec0129f5e128f48e2541bd6663a52a825c35f99b9a69d9593f2fc44b0bb4b'
                      }


    def test900_AboveBoundLight(self):
        self.setUp()
        self.parms['light'] = '10'
        expected = 'error: above bound light value'
        self.actual = place(self.parms)
        self.assertEqual(expected, self.actual['status'])
        self.tearDown()

    def test901_AboveBoundLight(self):
        self.setUp()
        self.parms['light'] = '-1'
        expected = 'error: below bound light value'
        self.actual = place(self.parms)
        self.assertEqual(expected, self.actual['status'])
        self.tearDown()

    def test902_NonIntegerLight(self):
        self.setUp()
        self.parms['light'] = 'X'
        expected = 'error: non-integer light value'
        self.actual = place(self.parms)
        self.assertEqual(expected, self.actual['status'])
        self.tearDown()
        
    def test903_NullLight(self):
        self.setUp()
        self.parms['light'] = None
        expected = 'error: Null light value'
        self.actual = place(self.parms)
        self.assertEqual(expected, self.actual['status'])
        self.tearDown()
        
    def test910_AboveBoundDark(self):
        self.setUp()
        self.parms['dark'] = '10'
        expected = 'error: above bound dark value'
        self.actual = place(self.parms)
        self.assertEqual(expected, self.actual['status'])
        self.tearDown()
        
    def test911_BelowBoundDark(self):
        self.setUp()
        self.parms['dark'] = '-1'
        expected = 'error: below bound dark value'
        self.actual = place(self.parms)
        self.assertEqual(expected, self.actual['status'])
        self.tearDown()

    def test912_NonIntegerDark(self):
        self.setUp()
        self.parms['dark'] = '1.2'
        expected = 'error: non-integer dark value'
        self.actual = place(self.parms)
        self.assertEqual(expected, self.actual['status'])
        self.tearDown()
        
    def test913_NullDark(self):
        self.setUp()
        self.parms['dark'] = None
        expected = 'error: Null dark value'
        self.actual = place(self.parms)
        self.assertEqual(expected, self.actual['status'])
        self.tearDown()
        
    def test920_AboveBoundBlank(self):
        self.setUp()
        self.parms['blank'] = '10'
        expected = 'error: above bound blank value'
        self.actual = place(self.parms)
        self.assertEqual(expected, self.actual['status'])
        self.tearDown()
        
    def test921_BelowBoundBlank(self):
        self.setUp()
        self.parms['blank'] = '-1'
        expected = 'error: below bound blank value'
        self.actual = place(self.parms)
        self.assertEqual(expected, self.actual['status'])
        self.tearDown()
        
    def test922_NonIntegerBlank(self):
        self.setUp()
        self.parms['blank'] = '1E5'
        expected = 'error: non-integer blank value'
        self.actual = place(self.parms)
        self.assertEqual(expected, self.actual['status'])
        self.tearDown()
        
    def test923_NullBlank(self):
        self.setUp()
        self.parms['blank'] = None
        expected = 'error: Null blank value'
        self.actual = place(self.parms)
        self.assertEqual(expected, self.actual['status'])
        self.tearDown()
        
    def test930_invalidLocationSeparator(self):
        self.setUp()
        self.parms['location'] = '3&4'
        expected = 'error: invalid location separator'
        self.actual = place(self.parms)
        self.assertEqual(expected, self.actual['status'])
        self.tearDown()
    
    def test931_NonIntegerLocation(self):
        self.setUp()
        self.parms['location'] = 'A:B'
        expected = 'error: non-integer location value'
        self.actual = place(self.parms)
        self.assertEqual(expected, self.actual['status'])
        self.tearDown()
        
    def test932_MissingValueOnOneSideOfSeparator(self):
        self.setUp()
        self.parms['location'] = '2:'
        expected = 'error: missing a value on one side of separator'
        self.actual = place(self.parms)
        self.assertEqual(expected, self.actual['status'])
        self.tearDown()
        
    def test933_MissingLocation(self):
        self.setUp()
        del self.parms['location']
        expected = 'error: missing location'
        self.actual = place(self.parms)
        self.assertEqual(expected, self.actual['status'])
        self.tearDown()
        
    def test934_NullLocation(self):
        self.setUp()
        self.parms['location'] = None
        expected = 'error: Null location'
        self.actual = place(self.parms)
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
        self.actual = place(self.parms)
        self.assertEqual(expected, self.actual['status'])
        self.tearDown()