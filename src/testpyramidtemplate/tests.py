# -*- coding: utf-8 -*-
"""Tests."""

from pyramid import testing

import unittest


class TestHome(unittest.TestCase):

    def setUp(self):
        self.config = testing.setUp()

    def tearDown(self):
        testing.tearDown()

    def test_home(self):
        from testpyramidtemplate.views import home
        request = testing.DummyRequest()
        result = home(request)
        self.assertEqual(result['name'], 'testpyramidtemplate')


class TestHomeFunctional(unittest.TestCase):

    def setUp(self):
        from testpyramidtemplate import main
        settings = {'sqlalchemy.url': 'sqlite://'}
        app = main({}, **settings)
        from webtest import TestApp
        self.testapp = TestApp(app)

    def test_home(self):
        res = self.testapp.get('/', status=200)
        self.assertIn(b'testpyramidtemplate!', res.body)
