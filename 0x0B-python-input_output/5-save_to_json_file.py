#!/usr/bin/python3
"""This modulng function"""
import json


def save_to_json_file(my_obj, filename):
    """Writes an  JSON format"""
    with open(filename, "w") as f:
        json.dump(my_obj, f)
