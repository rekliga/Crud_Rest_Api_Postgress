# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.test import BaseTestCase


class TestDefaultController(BaseTestCase):
    """DefaultController integration test stubs"""

    def test_consultar_get(self):
        """Test case for consultar_get

        Obtiene una lista
        """
        response = self.client.open(
            '/ILKERFRANCISCO/Api_db/1.0.0/consultar',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
