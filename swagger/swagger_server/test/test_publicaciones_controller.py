# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.inventory_item import InventoryItem  # noqa: E501
from swagger_server.test import BaseTestCase


class TestPublicacionesController(BaseTestCase):
    """PublicacionesController integration test stubs"""

    def test_search_inventory(self):
        """Test case for search_inventory

        searches inventory
        """
        query_string = [('search_string', 'search_string_example'),
                        ('skip', 1),
                        ('limit', 50)]
        response = self.client.open(
            '/ILKERFRANCISCO/Api_db/1.0.0/inventory',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
