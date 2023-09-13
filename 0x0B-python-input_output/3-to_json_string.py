#!/usr/bin/python3
"""defines string-to-JSON operation functions"""
import json


def to_json_string(my_obj):
    """Return JSON representation of string object"""
    return json.dumps(my_obj)
