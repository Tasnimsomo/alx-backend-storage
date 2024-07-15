#!/usr/bin/env python3
"""
Where can I learn Python?
"""


def schools_by_topic(mongo_collection, topic):
    """
        Python function that returns the list of school specific topic
        """
    cursor = mongo_collection.find({"topic": topic})
    list = []

    for a in cursor:
        list.append(a)
    return list
