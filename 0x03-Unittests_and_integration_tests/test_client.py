#!/usr/bin/env python3
"""
testing client
"""
import unittest
from unittest.mock import patch, PropertyMock, Mock
from parameterized import parameterized
from client import GithubOrgClient
from typing import Dict, Tuple, Any


class TestGithubOrgClient(unittest.TestCase):
    """ Class testing githubOrgClient
    returns the correct value."""
    @parameterized.expand([
        ("google"),
        ("abc"),
    ])
    @patch('client.get_json')
    def test_org(self, org: str, mock_get: Mock) -> None:
        """
        Test GithubOrgClient.org
        """
        test_class = GithubOrgClient(org).org
        url = f"https://api.github.com/orgs/{org}"
        mock_get.assert_called_once_with(url)
