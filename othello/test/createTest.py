from unittest import TestCase
from othello.create import _create as create

class CreateTest(TestCase):
    #    Desired level of confidence: boundary value analysis
    #    Input-output analysis
    #        inputs:    light -> integer .GE. 0, .LE. 9, Optional (Integer 1), unvalidated
    #                   dark -> integer .GE. 0, .LE. 9, Optional (Integer 2), unvalidated
    #                   blank -> integer .GE. 0, .LE. 9, Optional (Integer 0), unvalidated
    #                   size -> integer .GE. 6, .LE. 16, Optional (Integer 8), unvalidated
    #        ouputs:    board -> dictionary .GE.0 .LE.9,
    #                   tokens -> dictionary value specified by light, dark, and blank
    #                   integrity -> dictionary value is sha256 hash hexdigest of the strin
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
    
    #900 Sad Path
    def test900_AboveBoundLight(self):
        light = 10
        dark = 2
        blank = 0
        size = 8
        errorDict = {'status':'error: Above bound light integer'}
        actual = create(light, dark, blank, size)
        expected = errorDict
        self.assertEqual(actual, expected)
        
    
    def test901_BelowBoundLight(self):
        light = -1
        dark = 2
        blank = 0
        size = 8
        errorDict = {'status':'error: Below bound light integer'}
        actual = create(light, dark, blank, size)
        expected = errorDict
        self.assertEqual(actual, expected)
        
    def test902_NonIntegerLight(self):
        light = 'w'
        dark = 2
        blank = 0
        size = 8
        errorDict = {'status':'error: Non integer light'}
        actual = create(light, dark, blank, size)
        expected = errorDict
        self.assertEqual(actual, expected)
        
    def test903_NullLight(self):
        light = None
        dark = 2
        blank = 0
        size = 8
        errorDict = {'status':'error: Null light'}
        actual = create(light, dark, blank, size)
        expected = errorDict
        self.assertEqual(actual, expected)
    
    def test910_AboveBoundDark(self):
        light = 1
        dark = 10
        blank = 0
        size = 8
        errorDict = {'status':'error: Above bound dark integer'}
        actual = create(light, dark, blank, size)
        expected = errorDict
        self.assertEqual(actual, expected)
    
    def test911_BelowBoundDark(self):
        light = 1
        dark = -1
        blank = 0
        size = 8
        errorDict = {'status':'error: Below bound dark integer'}
        actual = create(light, dark, blank, size)
        expected = errorDict
        self.assertEqual(actual, expected)
        
    def test912_NonIntegerDark(self):
        light = 1
        dark = 'd'
        blank = 0
        size = 8
        errorDict = {'status':'error: Non integer dark'}
        actual = create(light, dark, blank, size)
        expected = errorDict
        self.assertEqual(actual, expected)
    
    def test913_NullDark(self):
        light = 1
        dark = None
        blank = 0
        size = 8
        errorDict = {'status':'error: Null dark'}
        actual = create(light, dark, blank, size)
        expected = errorDict
        self.assertEqual(actual, expected)
        
    def test920_AboveBoundBlank(self):
        light = 1
        dark = 2
        blank = 10
        size = 8
        errorDict = {'status':'error: Above bound blank integer'}
        actual = create(light, dark, blank, size)
        expected = errorDict
        self.assertEqual(actual, expected)
    
    def test921_BelowBoundBlank(self):
        light = 1
        dark = 2
        blank = -1
        size = 8
        errorDict = {'status':'error: Below bound blank integer'}
        actual = create(light, dark, blank, size)
        expected = errorDict
        self.assertEqual(actual, expected)
        
    def test922_BelowBoundBlank(self):
        light = 1
        dark = 2
        blank = 'b'
        size = 8
        errorDict = {'status':'error: Non integer blank'}
        actual = create(light, dark, blank, size)
        expected = errorDict
        self.assertEqual(actual, expected)
    
    def test923_NullBlank(self):
        light = 1
        dark = 2
        blank = None
        size = 8
        errorDict = {'status':'error: Null blank'}
        actual = create(light, dark, blank, size)
        expected = errorDict
        self.assertEqual(actual, expected)
        
    def test930_AboveBoundSize(self):
        light = 1
        dark = 2
        blank = 0
        size = 17
        errorDict = {'status':'error: Above bound size integer'}
        actual = create(light, dark, blank, size)
        expected = errorDict
        self.assertEqual(actual, expected)

    def test931_AboveBoundSize(self):
        light = 1
        dark = 2
        blank = 0
        size = 5
        errorDict = {'status':'error: Below bound size integer'}
        actual = create(light, dark, blank, size)
        expected = errorDict
        self.assertEqual(actual, expected)
        
    
        
        