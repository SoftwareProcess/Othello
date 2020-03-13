'''
    Created on Mar 8, 2020
    
    @author:    Tae Myles
'''

from unittest import TestCase
from othello.create import _create as create

class CreateTest(TestCase):

    #    Desired level of confidence: boundary value analysis
    #    Input-output analysis
    #        inputs:    light -> dictionary string key, value .GE. 0, .LE. 9, Optional (Integer 1), unvalidated
    #                   dark -> dictionary string key, value .GE. 0, .LE. 9, Optional (Integer 2), unvalidated
    #                   blank -> dictionary string key, value .GE. 0, .LE. 9, Optional (Integer 0), unvalidated
    #                   size -> dictionary string key, value .GE. 6, .LE. 16, Optional (Integer 8), unvalidated
    #        ouputs:    board -> dictionary string key, list of integer value .GE.0 .LE.9,
    #                   tokens -> dictionary string key, value specified by light, dark, and blank
    #                   integrity -> dictionary string key, value is sha256 hash hexdigest of the strin
    #                   status -> dictionary string associating that the board is created
    #    Happy path analysis
    #        light:    low value    light = 0
    #                  high value    light = 9
    #                  missing light    light = 1
    #        dark:     low value    dark = 0
    #                  high value    dark = 9
    #                  missing dark    dark= 2
    #        blank:    low value    blank = 0
    #                  high value    blank = 9
    #                  missing blank    blank = 0
    #        size:    low value    size = 6
    #                  high value    size = 16
    #                  missing size    size = 8
    #    
    #    Sad path analysis
    #        light:    above boundary    light = 10
    #                  below boundary    light = -1
    #                  non integer        light = w
    #                  null                light =
    #        dark:    above boundary    dark = 10
    #                  below boundary    dark = -1
    #                  non integer        dark = d
    #                  null                dark =
    #        blank:    above boundary    blank = 10
    #                  below boundary    blank = -1
    #                  non integer        blank = b
    #                  null                blank =
    #        size:    above boundary    size = 17
    #                  below boundary    size = 5
    #                  odd number         size = 9
    #                  non integer        size = 1.2
    #                  null                size = 
    #    light=dark:    same value as light and dark    light = 5 & dark = 5
    #    light=blank:    same value as ligth and blank    light = 5 & blank = 5
    #    blank=dark:    same value as blank and dark    blank = 2 & dark = 2
    
    def setUp(self):
        self.parms = {'op': 'create', 'light': '1', 'dark': '2', 'blank': '0', 'size': '8'}
    
    def tearDown(self):
        self.parms = {'op': 'create', 'light': '1', 'dark': '2', 'blank': '0', 'size': '8'}
        
    #900 Sad Path
    def test900_AboveBoundLight(self):
        self.setUp()
        self.parms['light'] = '10'
        expected = 'error: above bound light value'
        self.actual = create(self.parms)
        self.assertEqual(expected, self.actual['status'])
        self.tearDown()
        
    def test901_BelowBoundLight(self):
        self.setUp()
        self.parms['light'] = '-1'
        expected = 'error: below bound light value'
        self.actual = create(self.parms)
        self.assertEqual(expected, self.actual['status'])
        self.tearDown()
        
    def test902_NonIntegerLight(self):
        self.setUp()
        self.parms['light'] = 'w'
        expected = 'error: non-integer light value'
        self.actual = create(self.parms)
        self.assertEqual(expected, self.actual['status'])
        self.tearDown()
        
    def test903_NullLight(self):
        self.setUp()
        self.parms['light'] = None
        expected = 'error: Null light value'
        self.actual = create(self.parms)
        self.assertEqual(expected, self.actual['status'])
        self.tearDown()
        
    def test910_AboveBoundDark(self):
        self.setUp()
        self.parms['dark'] = '10'
        expected = 'error: above bound dark value'
        self.actual = create(self.parms)
        self.assertEqual(expected, self.actual['status'])
        self.tearDown()
        
    def test911_BelowBoundDark(self):
        self.setUp()
        self.parms['dark'] = '-1'
        expected = 'error: below bound dark value'
        self.actual = create(self.parms)
        self.assertEqual(expected, self.actual['status'])
        self.tearDown()
        
    def test912_NonIntegerDark(self):
        self.setUp()
        self.parms['dark'] = 'd'
        expected = 'error: non-integer dark value'
        self.actual = create(self.parms)
        self.assertEqual(expected, self.actual['status'])
        self.tearDown()
