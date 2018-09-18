#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for the mytestmodule module.
"""
import pytest

from mytestmodule import mytestmodule

def test_mytestfunction():
    expected_value = 42
    actual_value = mytestmodule.mytestfunction()
    assert expected_value == actual_value, "the actual value is not 42"

#def test_without_test_object():
#    assert False


#class TestMytestmodule(object):
#    @pytest.fixture
#    def return_a_test_object(self):
#        pass
#
#    def test_mytestmodule(self, mytestmodule):
#        assert False
#
#    def test_with_error(self, mytestmodule):
#        with pytest.raises(ValueError):
#            pass
