#!/usr/bin/env python3
"""Function to find schools by topic."""

def schools_by_topic(mongo_collection, topic):
    """Finds and returns schools having a specific topic.
    
    Args:
        mongo_collection: pymongo collection object.
        topic (str): The topic to search for.

    Returns:
        list: Matching school documents.
    """
    return list(mongo_collection.find({"topics": topic}))
