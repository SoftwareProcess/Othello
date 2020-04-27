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


    def test010_AllNominal(self):
        self.setUp()
        self.parms['light'] = 1
        self.parms['dark'] = 2
        self.parms['blank'] = 0
        self.parms['location'] = '1:2'
        self.parms['board'] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,2,0,0,0,0,2,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        self.parms['integrity'] = '6c3ec0129f5e128f48e2541bd6663a52a825c35f99b9a69d9593f2fc44b0bb4b'
        expected = {'board': [0,0,0,0,0,0,0,0,2,0,0,0,0,0,1,2,0,0,0,0,2,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                    'integrity': '5931bd7690588ed916c03b76aa07cad99800290577c40481d6eece941fcaf7cc',
                    'status': 'ok'}
        self.actual = place(self.parms)
        self.assertEqual(expected, self.actual)
        self.tearDown()

    def test020_HighLightBound(self):
        self.setUp()
        self.parms['light'] = 9
        self.parms['dark'] = 2
        self.parms['blank'] = 0
        self.parms['location'] = '1:2'
        self.parms['board'] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,9,2,0,0,0,0,2,9,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        self.parms['integrity'] = '5ab81cb67067273363db989119448a0b878896f7db5c268a50c4ae3062cb3647'
        expected = {'board': [0,0,0,0,0,0,0,0,2,0,0,0,0,0,9,2,0,0,0,0,2,9,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                    'integrity': 'b3a9c918ec9e6beb9a9f0430f4e8373c247d0fa49a246936d721641749808aca',
                    'status': 'ok'}
        self.actual = place(self.parms)
        self.assertEqual(expected, self.actual)
        self.tearDown()
        
    def test021_LowLightBound(self):
        self.setUp()
        self.parms['light'] = 0
        self.parms['dark'] = 2
        self.parms['blank'] = 1
        self.parms['location'] = '1:2'
        self.parms['board'] = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,2,1,1,1,1,2,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
        self.parms['integrity'] = '1b7e612b959852acbaf6b55d3f6b8dab2cdc32248a58a89dcf022ae80e5b36de'
        expected = {'board': [1,1,1,1,1,1,1,1,2,1,1,1,1,1,0,2,1,1,1,1,2,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                    'integrity': '8359a74bfa2e3052471b78230d8a5c3e0260ced88818dd956a9b1a3d8e53ae47',
                    'status': 'ok'}
        self.actual = place(self.parms)
        self.assertEqual(expected, self.actual)
        self.tearDown()
        
    def test022_MissingLight(self):
        self.setUp()
        del self.parms['light']
        self.parms['dark'] = 2
        self.parms['blank'] = 0
        self.parms['location'] = '1:2'
        self.parms['board'] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,2,0,0,0,0,2,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        self.parms['integrity'] = '6c3ec0129f5e128f48e2541bd6663a52a825c35f99b9a69d9593f2fc44b0bb4b'
        expected = {'board': [0,0,0,0,0,0,0,0,2,0,0,0,0,0,1,2,0,0,0,0,2,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                    'integrity': '5931bd7690588ed916c03b76aa07cad99800290577c40481d6eece941fcaf7cc',
                    'status': 'ok'}
        self.actual = place(self.parms)
        self.assertEqual(expected, self.actual)
        self.tearDown()
        
    def test030_LowDarkBound(self):
        self.setUp()
        self.parms['light'] = 1
        self.parms['dark'] = 0
        self.parms['blank'] = 5
        self.parms['location'] = '1:2'
        self.parms['board'] = [5,5,5,5,5,5,5,5,5,5,5,5,5,5,1,0,5,5,5,5,0,1,5,5,5,5,5,5,5,5,5,5,5,5,5,5]
        self.parms['integrity'] = '608f93025021dc6463199841f5c698dfba4daf01642ab8f3d3ad511d52851960'
        expected = {'board': [5,5,5,5,5,5,5,5,0,5,5,5,5,5,1,0,5,5,5,5,0,1,5,5,5,5,5,5,5,5,5,5,5,5,5,5],
                    'integrity': '046ef8205d3c7b8da0a1e0e85f722b373fac6a4f4a02543848ee70c69b2ff492',
                    'status': 'ok'}
        self.actual = place(self.parms)
        self.assertEqual(expected, self.actual)
        self.tearDown()
        
    def test031_HighDarkBound(self):
        self.setUp()
        self.parms['light'] = 1
        self.parms['dark'] = 9
        self.parms['blank'] = 5
        self.parms['location'] = '1:2'
        self.parms['board'] = [5,5,5,5,5,5,5,5,5,5,5,5,5,5,1,9,5,5,5,5,9,1,5,5,5,5,5,5,5,5,5,5,5,5,5,5]
        self.parms['integrity'] = '14df96aec47b28b46a66ba58ba46e28835b0c97ee552d4d4a59b1fa6ba26f4ac'
        expected = {'board': [5,5,5,5,5,5,5,5,9,5,5,5,5,5,1,9,5,5,5,5,9,1,5,5,5,5,5,5,5,5,5,5,5,5,5,5],
                    'integrity': '8b77aab822ed575b873b47ee3d6bf407c5ac1bab6a5109d12986e36c0d5b017e',
                    'status': 'ok'}
        self.actual = place(self.parms)
        self.assertEqual(expected, self.actual)
        self.tearDown()
        
    def test032_MissingDark(self):
        self.setUp()
        self.parms['light'] = 1
        del self.parms['dark']
        self.parms['blank'] = 5
        self.parms['location'] = '1:2'
        self.parms['board'] = [5,5,5,5,5,5,5,5,5,5,5,5,5,5,1,2,5,5,5,5,2,1,5,5,5,5,5,5,5,5,5,5,5,5,5,5]
        self.parms['integrity'] = '4f10d7db033df3ce6347853ef60ea402c9b639732317ebe753131fe783dfa0e2'
        expected = {'board': [5,5,5,5,5,5,5,5,2,5,5,5,5,5,1,2,5,5,5,5,2,1,5,5,5,5,5,5,5,5,5,5,5,5,5,5],
                    'integrity': '23484fa5bf3e8494dca99b859a24c5e8a285acee2b14eb98532ddd95b207ea23',
                    'status': 'ok'}
        self.actual = place(self.parms)
        self.assertEqual(expected, self.actual)
        self.tearDown()
        
    def test040_LowBlankBound(self):
        self.setUp()
        self.parms['light'] = 1
        self.parms['dark'] = 2
        self.parms['blank'] = 0
        self.parms['location'] = '1:2'
        self.parms['board'] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,2,0,0,0,0,2,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        self.parms['integrity'] = '6c3ec0129f5e128f48e2541bd6663a52a825c35f99b9a69d9593f2fc44b0bb4b'
        expected = {'board': [0,0,0,0,0,0,0,0,2,0,0,0,0,0,1,2,0,0,0,0,2,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                    'integrity': '5931bd7690588ed916c03b76aa07cad99800290577c40481d6eece941fcaf7cc',
                    'status': 'ok'}
        self.actual = place(self.parms)
        self.assertEqual(expected, self.actual)
        self.tearDown()
        
    def test041_HighBlankBound(self):
        self.setUp()
        self.parms['light'] = 1
        self.parms['dark'] = 2
        self.parms['blank'] = 9
        self.parms['location'] = '1:2'
        self.parms['board'] = [9,9,9,9,9,9,9,9,9,9,9,9,9,9,1,2,9,9,9,9,2,1,9,9,9,9,9,9,9,9,9,9,9,9,9,9]
        self.parms['integrity'] = 'f5f16ee0264578f836977c3d79ed8fa2bdeadb90371ef16095dc36064a23f656'
        expected = {'board': [9,9,9,9,9,9,9,9,2,9,9,9,9,9,1,2,9,9,9,9,2,1,9,9,9,9,9,9,9,9,9,9,9,9,9,9],
                    'integrity': '63080df8002556d44a7fdef4927c918a63864a6a034c6d4110d2dba29168fe3f',
                    'status': 'ok'}
        self.actual = place(self.parms)
        self.assertEqual(expected, self.actual)
        self.tearDown()
        
    def test042_MissingBlank(self):
        self.setUp()
        self.parms['light'] = 1
        self.parms['dark'] = 2
        del self.parms['blank']
        self.parms['location'] = '1:2'
        self.parms['board'] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,2,0,0,0,0,2,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        self.parms['integrity'] = '6c3ec0129f5e128f48e2541bd6663a52a825c35f99b9a69d9593f2fc44b0bb4b'
        expected = {'board': [0,0,0,0,0,0,0,0,2,0,0,0,0,0,1,2,0,0,0,0,2,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                    'integrity': '5931bd7690588ed916c03b76aa07cad99800290577c40481d6eece941fcaf7cc',
                    'status': 'ok'}
        self.actual = place(self.parms)
        self.assertEqual(expected, self.actual)
        self.tearDown()
        
    def test050_LowBoundBoard(self):
        self.setUp()
        self.parms['light'] = 1
        self.parms['dark'] = 2
        self.parms['blank'] = 0
        self.parms['location'] = '1:2'
        self.parms['board'] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,2,0,0,0,0,2,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        self.parms['integrity'] = '6c3ec0129f5e128f48e2541bd6663a52a825c35f99b9a69d9593f2fc44b0bb4b'
        expected = {'board': [0,0,0,0,0,0,0,0,2,0,0,0,0,0,1,2,0,0,0,0,2,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                    'integrity': '5931bd7690588ed916c03b76aa07cad99800290577c40481d6eece941fcaf7cc',
                    'status': 'ok'}
        self.actual = place(self.parms)
        self.assertEqual(expected, self.actual)
        self.tearDown()
        
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
        
    def test940_NonSquareBoard(self):
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
        
    def test941_OddxOddBoard(self):
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
        self.actual = place(self.parms)
        self.assertEqual(expected, self.actual['status'])
        self.tearDown() 

    def test942_MissingBoard(self):
        self.setUp()
        self.parms['light'] = 1
        self.parms['dark'] = 2
        self.parms['blank'] = 3
        del self.parms['board']
        expected = 'error: board does not exist'
        self.actual = place(self.parms)
        self.assertEqual(expected, self.actual['status'])
        self.tearDown()
        
    def test943_NullBoard(self):
        self.setUp()
        self.parms['light'] = 1
        self.parms['dark'] = 2
        self.parms['blank'] = 3
        self.parms['board'] = None
        expected = 'error: null board'
        self.actual = place(self.parms)
        self.assertEqual(expected, self.actual['status'])
        self.tearDown() 
        
    def test950_ShortIntegrity(self):
        self.setUp()
        self.parms['integrity'] = 'f01977c17f801c43eeb13fb9f74a49bd0c761db3cdffe01510f47ddd23ab465'
        expected = 'error: short integrity'
        self.actual = place(self.parms)
        self.assertEqual(expected, self.actual['status'])
        self.tearDown() 
        
    def test951_LongIntegrity(self):
        self.setUp()
        self.parms['integrity'] = 'f01977c17f801c43eeb13fb9f74a49bd0c761db3cdffe01510f47ddd23ab465a00'
        expected = 'error: long integrity'
        self.actual = place(self.parms)
        self.assertEqual(expected, self.actual['status'])
        self.tearDown()
        
    def test952_NonHexIntegrity(self):
        self.setUp()
        self.parms['integrity'] = 'f01977c17f801c43eeb13fb9f74a49bd0c761db3cdffe01510f47ddd23ab465$'
        expected = 'error: non hex characters'
        self.actual = place(self.parms)
        self.assertEqual(expected, self.actual['status'])
        self.tearDown()
        
    def test953_MissingIntegrity(self):
        self.setUp()
        del self.parms['integrity']
        expected = 'error: integrity does not exist'
        self.actual = place(self.parms)
        self.assertEqual(expected, self.actual['status'])
        self.tearDown()
        
    def test954_NullIntegrity(self):
        self.setUp()
        self.parms['integrity'] = None
        expected = 'error: null integrity'
        self.actual = place(self.parms)
        self.assertEqual(expected, self.actual['status'])
        self.tearDown()
        
    def test960_BlankEqualsLight(self):
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
        self.actual = place(self.parms)
        self.assertEqual(expected, self.actual['status'])
        self.tearDown()
        
    def test961_DarkEqualsBlank(self):
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
        self.actual = place(self.parms)
        self.assertEqual(expected, self.actual['status'])
        self.tearDown()
        
    def test962_LightEqualsDark(self):
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
        self.actual = place(self.parms)
        self.assertEqual(expected, self.actual['status'])
        self.tearDown()
        
    def test970_BoardWithNonTokenValues(self):
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
        self.actual = place(self.parms)
        self.assertEqual(expected, self.actual['status'])
        self.tearDown()
