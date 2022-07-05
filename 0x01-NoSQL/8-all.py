#!/usr/bin/env python3
"""Defines a function that lists all the documents in a collection
"""


def list_all(mongo_collection):
    """Lists all the documents in a collection

    Args:
        mongo_collection: The pymongo collection object

    Returns:
        A list of all the documents in a collection
        An empty list if the collection has no documents
    """
    cursor = list(mongo_collection.find())
    return cursor


if __name__ == '__main__':
    list_all(mongo_collection)
