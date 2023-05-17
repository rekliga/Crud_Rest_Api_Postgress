# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.inventory_item import InventoryItem  # noqa: E501
from swagger_server.test import BaseTestCase


class TestUsuariosController(BaseTestCase):
    """UsuariosController integration test stubs"""

    def test_add_inventory(self):
        """Test case for add_inventory

        adds an inventory item
        """
        body = InventoryItem()
        response = self.client.open(
            '/ILKERFRANCISCO/Api_db/1.0.0/inventory',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_create_user(self):
        """Test case for create_user

        create an user
        """
        body = InventoryItem()
        response = self.client.open(
            '/ILKERFRANCISCO/Api_db/1.0.0/crear',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_user(self):
        """Test case for delete_user

        adds an inventory item
        """
        body = InventoryItem()
        response = self.client.open(
            '/ILKERFRANCISCO/Api_db/1.0.0/eliminar',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_loginuser(self):
        """Test case for loginuser

        adds an inventory item
        """
        body = InventoryItem()
        response = self.client.open(
            '/ILKERFRANCISCO/Api_db/1.0.0/login',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_logoutuser(self):
        """Test case for logoutuser

        adds an inventory item
        """
        body = InventoryItem()
        response = self.client.open(
            '/ILKERFRANCISCO/Api_db/1.0.0/logout',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_protect_user(self):
        """Test case for protect_user

        adds an inventory item
        """
        body = InventoryItem()
        response = self.client.open(
            '/ILKERFRANCISCO/Api_db/1.0.0/protected',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_query_user(self):
        """Test case for query_user

        adds an inventory item
        """
        body = InventoryItem()
        response = self.client.open(
            '/ILKERFRANCISCO/Api_db/1.0.0/consultar',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_register_user(self):
        """Test case for register_user

        adds an inventory item
        """
        body = InventoryItem()
        response = self.client.open(
            '/ILKERFRANCISCO/Api_db/1.0.0/register',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_user(self):
        """Test case for update_user

        adds an inventory item
        """
        body = InventoryItem()
        response = self.client.open(
            '/ILKERFRANCISCO/Api_db/1.0.0/update',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
