import subprocess
import sys
from os.path import dirname
from unittest import TestCase

import mo_future
from mo_future import function_type


class TestBasic(TestCase):
    def test_import(self):
        self.assertEqual(function_type, (lambda x: x).__class__)

    def test_lazy_modules_not_loaded(self):
        result = subprocess.run(
            [sys.executable, "-c", "import sys, mo_future; print(sorted(m for m in ('configparser', 'html.parser', 'json', 'urllib.parse') if m in sys.modules))"],
            capture_output=True,
            text=True,
            cwd=dirname(dirname(mo_future.__file__)),
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(result.stdout.strip(), "[]")

    def test_lazy_modules_resolve(self):
        from configparser import ConfigParser
        from html.parser import HTMLParser
        from urllib.parse import urlparse

        self.assertIs(mo_future.ConfigParser, ConfigParser)
        self.assertIs(mo_future.HTMLParser, HTMLParser)
        self.assertIs(mo_future.urlparse, urlparse)

    def test_utf8_json_encoder(self):
        from mo_future import utf8_json_encoder

        self.assertEqual(utf8_json_encoder({"b": 1, "a": "é"}), '{"a":"é","b":1}')

    def test_unknown_attribute(self):
        with self.assertRaises(AttributeError):
            mo_future.does_not_exist


class TestIsBinary(TestCase):
    def test_bytes_and_bytearray_are_binary(self):
        self.assertTrue(mo_future.is_binary(b"a"))
        self.assertTrue(mo_future.is_binary(bytearray(b"a")))

    def test_text_is_not_binary(self):
        self.assertFalse(mo_future.is_binary("a"))
