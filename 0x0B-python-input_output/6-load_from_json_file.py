#!/usr/bin/python3
"""This module ing function"""
import json


def load_from_json_file(filename):
    """Creates JSON file"""
    with open(filename) as f:
        return json.load(f)
