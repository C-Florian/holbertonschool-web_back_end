#!/usr/bin/env python3
"""Function to list all documents in a MongoDB collection."""

def list_all(mongo_collection):
    """Lists all documents in the given collection.
    
    Args:
        mongo_collection: pymongo collection object.

    Returns:
        list: All documents in the collection, or an empty list if none.
    """
    return list(mongo_collection.find())
