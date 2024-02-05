#!/usr/bin/env python3
"""
Unit tests for functions
"""
import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize
from parameterized import parameterized  # type: ignore


class TestAccessNestedMap(unittest.TestCase):
    """Test for access_nested_map function"""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """Test access_nested_map with different inputs"""
        result = access_nested_map(nested_map, path)
        self.assertEqual(result, expected)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b")),
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """Test access_nested_map"""
        with self.assertRaises(KeyError) as context:
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """Test case for get_json function"""

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    @patch('utils.requests.get')
    def test_get_json(self, url, json_data, mock_get):
        """Test get_json function with mocked requests.get"""
        mock_response = Mock()
        mock_response.json.return_value = json_data
        mock_get.return_value = mock_response

        result = get_json(url)
        self.assertEqual(result, json_data)
        mock_get.assert_called_once_with(url)


class TestMemoize(unittest.TestCase):
    """Class Testmemoize decorator"""

    def test_memoize(self):
        """Test memoize decorator"""
        class TestClass:
            """Test class"""
            def __init__(self):
                self.call_count = 0

            @memoize
            def a_property(self):
                """Memoized property"""
                self.call_count += 1
                return 42

        test_instance = TestClass()
        result1 = test_instance.a_property
        result2 = test_instance.a_property

        self.assertEqual(result1, 42)
        self.assertEqual(result2, 42)
        self.assertEqual(test_instance.call_count, 1)


if __name__ == "__main__":
    unittest.main()
