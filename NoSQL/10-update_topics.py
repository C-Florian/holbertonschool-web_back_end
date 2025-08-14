#!/usr/bin/env python3
"""Function to update topics of a school document."""

def update_topics(mongo_collection, name, topics):
    """Updates all topics of the school with the given name.
    
    Args:
        mongo_collection: pymongo collection object.
        name (str): Name of the school.
        topics (list): List of topics to set.
    """
    mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )
