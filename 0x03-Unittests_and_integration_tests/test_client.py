#!/usr/bin/env python3
"""
Unit tests for client module
"""
import unittest
from unittest.mock import patch, PropertyMock
from parameterized import parameterized, parameterized_class
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Test cases for GithubOrgClient"""

    @parameterized.expand([
        ("google", {'login': "google"}),
        ("abc", {'login': "abc"}),
    ])
    @patch("client.get_json")
    def test_org(self, org_name, expected_response, mock_get_json: Mock):
        """Test org method"""
        mock_get_json.return_value = expected_response
        client = GithubOrgClient(org_name)
        self.assertEqual(client.org(), expected_response)
        url = f"https://api.github.com/orgs/{org_name}"
        mock_get_json.assert_called_once_with(url)

    def test_public_repos_url(self):
        """
        Test that the result of _public_repos_url is the
        """
        with patch('client.GithubOrgClient.org',
                   new_callable=PropertyMock) as mock_org:
            payload = {"repos_url": "World"}
            mock_org.return_value = payload
            test_class = GithubOrgClient('test')
            result = test_class._public_repos_url
            self.assertEqual(result, payload["repos_url"])

    @patch('client.get_json')
    def test_public_repos(self, mock_get):
        """Test that the list of repos is what
        you expect from the chosen payload.
        """
        json_payload = [{"name": "Google"}, {"name": "Twitter"}]
        mock_get.return_value = json_payload

        with patch('client.GithubOrgClient._public_repos_url',
                   new_callable=PropertyMock) as mock_public_repos_url:

            mock_public_repos_url.return_value = "hello/world"
            test_class = GithubOrgClient('test')
            result = test_class.public_repos()

            check = [i["name"] for i in json_payload]
            self.assertEqual(result, check)

            mock_public_repos_url.assert_called_once()
            mock_get.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, repo, license_key, expected):
        """Unit-test for GithubOrgClient.has_license"""
        result = GithubOrgClient.has_license(repo, license_key)
        self.assertEqual(result, expected)
