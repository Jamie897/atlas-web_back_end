#!/usr/bin/env python3
import unittest
from unittest.mock import patch, PropertyMock
from parameterized import parameterized, parameterized_class
from requests import HTTPError
from client import GithubOrgClient
from fixtures import TEST_PAYLOAD

class TestGithubOrgClient(unittest.TestCase):
    @parameterized.expand([
        ("google"),
        ("abc"),
    ])