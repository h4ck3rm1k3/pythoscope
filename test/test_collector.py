import sys

from nose.tools import assert_equal
from nose.exc import SkipTest
from helper import assert_length, assert_single_class, assert_single_function

from pythoscope.collector import collect_information_from_code

new_style_class = """
class AClass(object):
    def amethod(self):
        pass
"""

old_style_class = """
class OldStyleClass:
    def amethod(self):
        pass
"""

class_without_methods = """
class ClassWithoutMethods(object):
    pass
"""

stand_alone_function = """
def a_function():
    pass
"""

inner_classes_and_function = """
def outer_function():
    def inner_function():
        pass
    class InnerClass(object):
        pass

class OuterClass(object):
    class AnotherInnerClass(object):
        pass
"""

class_with_methods = """
class ClassWithThreeMethods(object):
    def first_method(self):
        pass
    def second_method(self, x):
        pass
    def third_method(self, x, y):
        pass
"""

syntax_error = """
a b c d e f g
"""

indentation_error = """
  def answer():
    42
"""

definitions_inside_try_except = """
try:
    def inside_function(): pass
    class InsideClass(object): pass
except:
    pass
"""

definitions_inside_if = """
if True:
    def inside_function(): pass
    class InsideClass(object): pass
"""

definitions_inside_while = """
while True:
    def inside_function(): pass
    class InsideClass(object): pass
"""

definitions_inside_for = """
for x in range(1):
    def inside_function(): pass
    class InsideClass(object): pass
"""

definitions_inside_with = """
from __future__ import with_statement
with x:
    def inside_function(): pass
    class InsideClass(object): pass
"""

lambda_definition = """
lambda_function = lambda x: not x
"""

class TestCollector:
    def test_collects_information_about_top_level_classes(self):
        info = collect_information_from_code(new_style_class)

        assert_single_class(info, "AClass")

    def test_collects_information_about_top_level_functions(self):
        info = collect_information_from_code(stand_alone_function)

        assert_single_function(info, "a_function")

    def test_doesnt_count_methods_as_functions(self):
        info = collect_information_from_code(new_style_class)

        assert_length(info.functions, 0)

    def test_collects_information_about_old_style_classes(self):
        info = collect_information_from_code(old_style_class)

        assert_single_class(info, "OldStyleClass")

    def test_collects_information_about_classes_without_methods(self):
        info = collect_information_from_code(class_without_methods)

        assert_single_class(info, "ClassWithoutMethods")

    def test_ignores_inner_classes_and_functions(self):
        info = collect_information_from_code(inner_classes_and_function)

        assert_single_class(info, "OuterClass")
        assert_single_function(info, "outer_function")

    def test_collects_information_about_methods_of_a_class(self):
        info = collect_information_from_code(class_with_methods)

        assert_equal(["first_method", "second_method", "third_method"],
                     info.classes[0].methods)

    def test_collector_handles_syntax_errors(self):
        info = collect_information_from_code(syntax_error)

        assert_length(info.errors, 1)

    def test_collector_handles_indentation_errors(self):
        info = collect_information_from_code(indentation_error)

        assert_length(info.errors, 1)

    def test_collects_information_about_functions_and_classes_inside_other_blocks(self):
        suite = [definitions_inside_try_except, definitions_inside_if,
                 definitions_inside_while, definitions_inside_for]

        for case in suite:
            info = collect_information_from_code(case)
            assert_single_class(info, "InsideClass")
            assert_single_function(info, "inside_function")

    def test_collects_information_about_functions_and_classes_inside_with(self):
        # With statement was introduced in Python 2.5, so skip this test for
        # earlier versions.
        if float(sys.version[:3]) < 2.5:
            raise SkipTest

        info = collect_information_from_code(definitions_inside_with)
        assert_single_class(info, "InsideClass")
        assert_single_function(info, "inside_function")

    def test_collects_information_about_functions_defined_using_lambda(self):
        info = collect_information_from_code(lambda_definition)

        assert_single_function(info, "lambda_function")