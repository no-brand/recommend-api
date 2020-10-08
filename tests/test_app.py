# -*- coding: utf-8 -*-

import unittest
import app as web_app


class FlaskAppTestCase(unittest.TestCase):

    def test_access(self):
        with web_app.app.test_client() as client:
            rv = client.get('/')
            self.assertEqual(rv._status_code, 200)


if __name__ == '__main__':
    unittest.main()
