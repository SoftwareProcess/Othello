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

    # Happy path
    def test010_AllNominalInput(self):
        self.setUp()
        self.parms['light'] = '1'
        self.parms['dark'] = '2'
        self.parms['blank'] = '0'
        self.parms['board'] = [0, 0, 0, 0, 0, 0,
                               0, 0, 0, 0, 0, 0, 
                               0, 0, 1, 2, 0, 0, 
                               0, 0, 2, 1, 0, 0, 
                               0, 0, 0, 0, 0, 0, 
                               0, 0, 0, 0, 0, 0]
        self.parms['integrity'] = '6c3ec0129f5e128f48e2541bd6663a52a825c35f99b9a69d9593f2fc44b0bb4b'
        expected = 'ok'
        self.actual = status(self.parms)
        self.assertEqual(expected, self.actual['status'])
        self.tearDown()

    def test020_HighBoundLightNominalLightDarkBlankBoardIntegrity(self):
        self.setUp()
        self.parms['light'] = '9'
        self.parms['dark'] = '2'
        self.parms['blank'] = '0'
        self.parms['board'] = [0, 0, 0, 0, 0, 0,
                               0, 0, 0, 0, 0, 0, 
                               0, 0, 9, 2, 0, 0, 
                               0, 0, 2, 9, 0, 0, 
                               0, 0, 0, 0, 0, 0, 
                               0, 0, 0, 0, 0, 0]
        self.parms['integrity'] = '5ab81cb67067273363db989119448a0b878896f7db5c268a50c4ae3062cb3647'
        expected = 'ok'
        self.actual = status(self.parms)
        self.assertEqual(expected, self.actual['status'])
        self.tearDown()
        
    def test021_LowBoundLightNominalLightDarkBlankBoardIntegrity(self):
        self.setUp()
        self.parms['light'] = '0'
        self.parms['dark'] = '2'
        self.parms['blank'] = '1'
        self.parms['board'] = [1, 1, 1, 1, 1, 1,
                               1, 1, 1, 1, 1, 1, 
                               1, 1, 0, 2, 1, 1, 
                               1, 1, 2, 0, 1, 1, 
                               1, 1, 1, 1, 1, 1, 
                               1, 1, 1, 1, 1, 1]
        self.parms['integrity'] = '1b7e612b959852acbaf6b55d3f6b8dab2cdc32248a58a89dcf022ae80e5b36de'
        expected = 'ok'
        self.actual = status(self.parms)
        self.assertEqual(expected, self.actual['status'])
        self.tearDown()
    
    def test022_MissingLightNominalLightDarkBlankBoardIntegrity(self):
        self.setUp()
        del self.parms['light']
        self.parms['dark'] = '2'
        self.parms['blank'] = '3'
        self.parms['board'] = [3, 3, 3, 3, 3, 3,
                               3, 3, 3, 3, 3, 3, 
                               3, 3, 1, 2, 3, 3, 
                               3, 3, 2, 1, 3, 3, 
                               3, 3, 3, 3, 3, 3, 
                               3, 3, 3, 3, 3, 3]
        self.parms['integrity'] = 'f01977c17f801c43eeb13fb9f74a49bd0c761db3cdffe01510f47ddd23ab465a'
        expected = 'ok'
        self.actual = status(self.parms)
        self.assertEqual(expected, self.actual['status'])
        self.tearDown()
        
    def test030_LowBoundDarkNominalLightBlankBoardIntegrity(self):
        self.setUp()
        self.parms['light'] = '5'
        self.parms['dark'] = '0'
        self.parms['blank'] = '9'
        self.parms['board'] = [9, 9, 9, 9, 9, 9,
                               9, 9, 9, 9, 9, 9,
                               9, 9, 5, 0, 9, 9, 
                               9, 9, 0, 5, 9, 9, 
                               9, 9, 9, 9, 9, 9, 
                               9, 9, 9, 9, 9, 9]
        self.parms['integrity'] = '85c972c79b667135f99ad9380f4af4a7495c5b5de3768c9cb36c4bc73f0da08a'
        expected = 'ok'
        self.actual = status(self.parms)
        self.assertEqual(expected, self.actual['status'])
        self.tearDown()
        
    def test031_HighBoundDarkNominalLightBlankBoardIntegrity(self):
        self.setUp()
        self.parms['light'] = '5'
        self.parms['dark'] = '9'
        self.parms['blank'] = '3'
        self.parms['board'] = [3, 3, 3, 3, 3, 3,
                               3, 3, 3, 3, 3, 3, 
                               3, 3, 5, 9, 3, 3, 
                               3, 3, 9, 5, 3, 3, 
                               3, 3, 3, 3, 3, 3, 
                               3, 3, 3, 3, 3, 3]
        self.parms['integrity'] = '34932b7f4bbafed18cf99e367e29407e6aae8b49b2ced711f31e429e7efc2a12'
        expected = 'ok'
        self.actual = status(self.parms)
        self.assertEqual(expected, self.actual['status'])
        self.tearDown()
        
    def test032_MissingDarkNominalLightBlankBoardIntegrity(self):
        self.setUp()
        self.parms['light'] = '5'
        del self.parms['dark']
        self.parms['blank'] = '3'
        self.parms['board'] = [3, 3, 3, 3, 3, 3,
                               3, 3, 3, 3, 3, 3, 
                               3, 3, 5, 2, 3, 3, 
                               3, 3, 2, 5, 3, 3, 
                               3, 3, 3, 3, 3, 3, 
                               3, 3, 3, 3, 3, 3]
        self.parms['integrity'] = 'a348c2dae89e65378fc64d889b1d394819c021b2e4cccb37310bbef9335bb900'
        expected = 'ok'
        self.actual = status(self.parms)
        self.assertEqual(expected, self.actual['status'])
        self.tearDown()
        
    def test040_LowBoundBlankNominalLightDarkBoardIntegrity(self):
        self.setUp()
        self.parms['light'] = '5'
        self.parms['dark'] = '6'
        self.parms['blank'] = '0'
        self.parms['board'] = [0, 0, 0, 0, 0, 0,
                               0, 0, 0, 0, 0, 0,
                               0, 0, 5, 6, 0, 0, 
                               0, 0, 6, 5, 0, 0, 
                               0, 0, 0, 0, 0, 0, 
                               0, 0, 0, 0, 0, 0]
        self.parms['integrity'] = '062f219e852404144cd7967bcbac5d5d82c151697d8eacfd8c29779acbc58b19'
        expected = 'ok'
        self.actual = status(self.parms)
        self.assertEqual(expected, self.actual['status'])
        self.tearDown()
        
    def test041_HighBoundBlankNominalLightDarkBoardIntegrity(self):
        self.setUp()
        self.parms['light'] = '5'
        self.parms['dark'] = '6'
        self.parms['blank'] = '9'
        self.parms['board'] = [9, 9, 9, 9, 9, 9,
                               9, 9, 9, 9, 9, 9,
                               9, 9, 5, 6, 9, 9, 
                               9, 9, 6, 5, 9, 9, 
                               9, 9, 9, 9, 9, 9, 
                               9, 9, 9, 9, 9, 9]
        self.parms['integrity'] = '5b698f38d9d1c1754df196ee688f3900ceba9d074cb74b5e17c19a197b69bf02'
        expected = 'ok'
        self.actual = status(self.parms)
        self.assertEqual(expected, self.actual['status'])
        self.tearDown()

    def test042_MissingBlankNominalLightDarkBoardIntegrity(self):
        self.setUp()
        self.parms['light'] = '5'
        self.parms['dark'] = '6'
        del self.parms['blank']
        self.parms['board'] = [0, 0, 0, 0, 0, 0,
                               0, 0, 0, 0, 0, 0, 
                               0, 0, 5, 6, 0, 0, 
                               0, 0, 6, 5, 0, 0, 
                               0, 0, 0, 0, 0, 0, 
                               0, 0, 0, 0, 0, 0]
        self.parms['integrity'] = '5b698f38d9d1c1754df196ee688f3900ceba9d074cb74b5e17c19a197b69bf02'
        expected = 'ok'
        self.actual = status(self.parms)
        self.assertEqual(expected, self.actual['status'])
        self.tearDown()

    def test050_LowBoundSizeBoardNominalLightDarkBlankIntegrity(self):
        self.setUp()
        self.parms['light'] = '1'
        self.parms['dark'] = '2'
        self.parms['blank'] = '0'
        self.parms['board'] = [0, 0, 0, 0, 0, 0,
                               0, 0, 0, 0, 0, 0, 
                               0, 0, 1, 2, 0, 0, 
                               0, 0, 2, 1, 0, 0, 
                               0, 0, 0, 0, 0, 0, 
                               0, 0, 0, 0, 0, 0]
        self.parms['integrity'] = '6c3ec0129f5e128f48e2541bd6663a52a825c35f99b9a69d9593f2fc44b0bb4b'
        expected = 'ok'
        self.actual = status(self.parms)
        self.assertEqual(expected, self.actual['status'])
        self.tearDown()
        
    # Sad path
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
        
    def test940_ShortIntegrity(self):
        self.setUp()
        self.parms['integrity'] = 'f01977c17f801c43eeb13fb9f74a49bd0c761db3cdffe01510f47ddd23ab465'
        expected = 'error: short integrity'
        self.actual = status(self.parms)
        self.assertEqual(expected, self.actual['status'])
        self.tearDown() 
        
    def test941_LongIntegrity(self):
        self.setUp()
        self.parms['integrity'] = 'f01977c17f801c43eeb13fb9f74a49bd0c761db3cdffe01510f47ddd23ab465a00'
        expected = 'error: long integrity'
        self.actual = status(self.parms)
        self.assertEqual(expected, self.actual['status'])
        self.tearDown()
    
    def test942_NonHexIntegrity(self):
        self.setUp()
        self.parms['integrity'] = 'f01977c17f801c43eeb13fb9f74a49bd0c761db3cdffe01510f47ddd23ab465$'
        expected = 'error: non hex characters'
        self.actual = status(self.parms)
        self.assertEqual(expected, self.actual['status'])
        self.tearDown()

    def test943_MissingIntegrity(self):
        self.setUp()
        del self.parms['integrity']
        expected = 'error: integrity does not exist'
        self.actual = status(self.parms)
        self.assertEqual(expected, self.actual['status'])
        self.tearDown()
        
    def test944_NullIntegrity(self):
        self.setUp()
        self.parms['integrity'] = None
        expected = 'error: null integrity'
        self.actual = status(self.parms)
        self.assertEqual(expected, self.actual['status'])
        self.tearDown()
        
    def test950_LightEqualsDark(self):
        self.setUp()
        self.parms['light'] = 2
        self.parms['dark'] = 2
        self.parms['blank'] = 0
        self.parms['board'] = [0,0,0,0,0,0,
                               0,0,0,0,0,0,
                               0,0,2,2,0,0,
                               0,0,2,2,0,0,
                               0,0,0,0,0,0,
                               0,0,0,0,0,0]
        expected = 'error: light is equal to dark value'
        self.actual = status(self.parms)
        self.assertEqual(expected, self.actual['status'])
        self.tearDown()
        
    def test951_BlankEqualsLight(self):
        self.setUp()
        self.parms['light'] = 1
        self.parms['dark'] = 2
        self.parms['blank'] = 1
        self.parms['board'] = [1,1,1,1,1,1,
                               1,1,1,1,1,1,
                               1,1,1,2,1,1,
                               1,1,2,1,1,1,
                               1,1,1,1,1,1,
                               1,1,1,1,1,1]
        expected = 'error: blank is equal to light value'
        self.actual = status(self.parms)
        self.assertEqual(expected, self.actual['status'])
        self.tearDown()
        
    def test952_DarkEqualsBlank(self):
        self.setUp()
        self.parms['light'] = 1
        self.parms['dark'] = 2
        self.parms['blank'] = 2
        self.parms['board'] = [2,2,2,2,2,2,
                               2,2,2,2,2,2,
                               2,2,1,2,2,2,
                               2,2,2,1,2,2,
                               2,2,2,2,2,2,
                               2,2,2,2,2,2,]
        expected = 'error: dark is equal to blank value'
        self.actual = status(self.parms)
        self.assertEqual(expected, self.actual['status'])
        self.tearDown()
        
    def test953_BoardWithNonTokenValues(self):
        self.setUp()
        self.parms['light'] = 1
        self.parms['dark'] = 2
        self.parms['blank'] = 3
        self.parms['board'] = [0,0,0,0,0,0,
                               0,0,0,0,0,0,
                               0,0,1,2,0,0,
                               0,0,2,1,0,0,
                               0,0,0,0,0,0,
                               0,0,0,0,0,0,]
        expected = 'error: incorrect board value'
        self.actual = status(self.parms)
        self.assertEqual(expected, self.actual['status'])
        self.tearDown()
        
    def test954_InvalidIntegrity(self):
        self.setUp()
        self.parms['light'] = 1
        self.parms['dark'] = 2
        self.parms['blank'] = 3
        self.parms['board'] = [3,3,3,3,3,3,
                               3,3,3,3,3,3,
                               3,3,1,2,3,3,
                               3,3,2,1,3,3,
                               3,3,3,3,3,3,
                               3,3,3,3,3,3]
        self.parms['integrity'] = '4d5aeb4a45b57eecf69dcc304664fcf7a6f7c74c86ef9ede14da46ab2d9df242'
        expected = 'error: invalid integrity'
        self.actual = status(self.parms)
        self.assertEqual(expected, self.actual['status'])
        self.tearDown()