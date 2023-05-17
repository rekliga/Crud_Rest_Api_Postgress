import connexion
import six

from swagger_server.models.inventory_item import InventoryItem  # noqa: E501
from swagger_server import util


def add_inventory(body=None):  # noqa: E501
    """adds an inventory item

    Adds an item to the system # noqa: E501

    :param body: Inventory item to add
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = InventoryItem.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def create_user(body=None):  # noqa: E501
    """create an user

    create an user # noqa: E501

    :param body: Inventory item to add
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = InventoryItem.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def delete_user(body=None):  # noqa: E501
    """adds an inventory item

    delete an user # noqa: E501

    :param body: Inventory item to add
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = InventoryItem.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def loginuser(body=None):  # noqa: E501
    """adds an inventory item

    logs a user # noqa: E501

    :param body: Inventory item to add
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = InventoryItem.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def logoutuser(body=None):  # noqa: E501
    """adds an inventory item

    logs out a user # noqa: E501

    :param body: Inventory item to add
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = InventoryItem.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def protect_user(body=None):  # noqa: E501
    """adds an inventory item

    protect a user # noqa: E501

    :param body: Inventory item to add
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = InventoryItem.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def query_user(body=None):  # noqa: E501
    """adds an inventory item

    consult an user # noqa: E501

    :param body: Inventory item to add
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = InventoryItem.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def register_user(body=None):  # noqa: E501
    """adds an inventory item

    register a user # noqa: E501

    :param body: Inventory item to add
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = InventoryItem.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def update_user(body=None):  # noqa: E501
    """adds an inventory item

    update an user # noqa: E501

    :param body: Inventory item to add
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = InventoryItem.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
