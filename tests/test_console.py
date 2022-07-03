#!/usr/bin/python3
"""
Unittests for the Console.py file
"""

import cmd
import pycodestyle
import unittest

import console


class TestConsole(unittest.TestCase):
    """
    Class to test Console class
    """
    def test_style_test(self):
        """
        Test if test_console.py passes the pycodestyle style
        """
        console_style = pycodestyle.StyleGuide().check_\
            files(['test_console.py'])
        self.assertEqual(console_style.total_errors, 0, "Does not com\
        ply with pycodestyle")

    def test_style(self):
        """
        Test if console.py passes the pycodestyle style
        """
        console_style = pycodestyle.StyleGuide().check_files(['console.py'])
        self.assertEqual(console_style.total_errors, 0, "Does not com\
        ply with pycodestyle")

    def test_methods_doc_exists(self):
        """
        Test if the methods in console.py have document\
        ation (test only if they exist)
        """
        self.assertIsNotNone(console.__doc__, "Console doc documentat\
        ion does not exists")
        self.assertIsNotNone(console.do_quit.__doc__, "Console do_quit\
        Documentation does not exists")
        self.assertIsNotNone(console.do_EOF.__doc__, "Console do_EOF\
        Documentation does not exists")
        self.assertIsNotNone(console.emptyline.__doc__, "Console\
        do_emptyline Documentation does not exists")
        self.assertIsNotNone(console.do_create.__doc__, "Console\
        do_create Documentation does not exists")
        self.assertIsNotNone(console.do_show.__doc__, "Console do_show\
        Documentation does not exists")
        self.assertIsNotNone(console.do_destroy.__doc__, "Console\
        do_destroy Documentation does not exists")
        self.assertIsNotNone(console.do_all.__doc__, "Console do_all\
        Documentation does not exists")
        self.assertIsNotNone(console.do_update.__doc__, "Console\
        do_update Documentation does not exists")
        self.assertIsNotNone(console.default.__doc__, "Console default\
        Documentation does not exists")

    def test_methods_doc_length(self):
        """
        Test if the methods documentation in console.py have more than 5 words
        """
        n_con = len(console.__doc__)
        self.assertGreaterEqual(n_con, 10, "Console doc document\
        ation has less than 5 words")
        n_con_quit = len(console.do_quit.__doc__)
        self.assertGreaterEqual(n_con_quit, 10, "Console do_quit Document\
        ation has less than 5 words")
        n_con_eof = len(console.do_EOF.__doc__)
        self.assertGreaterEqual(n_con_eof, 10, "Console do_EOF Documentat\
        ion has less than 5 words")
        n_con_emptyline = len(console.emptyline.__doc__)
        self.assertGreaterEqual(n_con_emptyline, 10, "Console do_emptyline D\
        ocumentation has less than 5 words")
        n_con_create = len(console.do_create.__doc__)
        self.assertGreaterEqual(n_con_create, 10, "Console do_create Document\
        ation has less than 5 words")
        n_con_show = len(console.do_show.__doc__)
        self.assertGreaterEqual(n_con_show, 10, "Console do_show Document\
        ation has less than 5 words")
        n_con_destroy = len(console.do_destroy.__doc__)
        self.assertGreaterEqual(n_con_destroy, 10, "Console do_destroy Doc\
        umentation has less than 5 words")
        n_con_all = len(console.do_all.__doc__)
        self.assertGreaterEqual(n_con_all, 10, "Console do_all Document\
        ation has less than 5 words")
        n_con_update = len(console.do_update.__doc__)
        self.assertGreaterEqual(n_con_update, 10, "Console do_update Document\
        ation has less than 5 words")
        n_con_default = len(console.default.__doc__)
        self.assertGreaterEqual(n_con_default, 10, "Console default Document\
        ation has less than 5 words")
