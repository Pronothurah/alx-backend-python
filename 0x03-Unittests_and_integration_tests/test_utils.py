#!/usr/bin/env python3
"""Unittests and Integration Tests"""
import unittest
from unittest.mock import (
    patch,
    Mock
)
from parameterized import parameterized
from utils import (
    access_nested_map,
    get_json,
    memoize
)
from typing import (
    Dict,
    Tuple,
    Union,
    Any
)


class TestAccessNestedMap(unittest.TestCase):
    """ Class definition """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(
        self,
        map: Dict,
        path: Tuple[str],
        expected: Union[Dict, int]
    ) -> None:
        """ Test `access_nested_map` method """
        self.assertEqual(access_nested_map(map, path), expected)
