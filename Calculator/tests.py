import unittest

from pyramid import testing


class ViewTests(unittest.TestCase):
    def setUp(self):
        self.config = testing.setUp()

    def tearDown(self):
        testing.tearDown()

    def test_my_view(self):
        from Calculator.views.default import my_view
        request = testing.DummyRequest()
        info = my_view(request)
        self.assertEqual(info['project'], 'Calculator')

    def test_calculate(self):
        from Calculator.views.calculate import main_calculator
        request = testing.DummyRequest()
        request.matchdict['operator'] = 'sum'
        request.matchdict['firstOper'] = 1
        request.matchdict['secondOper'] = 2
        info = main_calculator(request)
        self.assertEqual(info['result'], 3)

        request.matchdict['firstOper'] = '1'
        request.matchdict['secondOper'] = '2'
        info = main_calculator(request)
        self.assertEqual(info['result'], 3)
