#!/usr/bin/python3
"""defines JSON-to-object functions"""
import json


def from_json_string(my_str):
    """Return Python object representation of JSON string"""
    return json.loads(my_str)
