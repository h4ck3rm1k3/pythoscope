import unittest


class TestDescend(unittest.TestCase):
    def test_descend(self):
        # self.assertEqual(expected, descend(tree, visitor_type))
        assert False  # TODO: implement your test here

class TestFindLastLeaf(unittest.TestCase):
    def test_find_last_leaf(self):
        # self.assertEqual(expected, find_last_leaf(node))
        assert False  # TODO: implement your test here

class TestGetStartingWhitespace(unittest.TestCase):
    def test_get_starting_whitespace(self):
        # self.assertEqual(expected, get_starting_whitespace(code))
        assert False  # TODO: implement your test here

class TestRemoveTrailingWhitespace(unittest.TestCase):
    def test_remove_trailing_whitespace(self):
        # self.assertEqual(expected, remove_trailing_whitespace(code))
        assert False  # TODO: implement your test here

class TestIsLeafOfType(unittest.TestCase):
    def test_is_leaf_of_type(self):
        # self.assertEqual(expected, is_leaf_of_type(leaf, *types))
        assert False  # TODO: implement your test here

class TestIsNodeOfType(unittest.TestCase):
    def test_is_node_of_type(self):
        # self.assertEqual(expected, is_node_of_type(node, *types))
        assert False  # TODO: implement your test here

class TestLeafValue(unittest.TestCase):
    def test_leaf_value(self):
        # self.assertEqual(expected, leaf_value(leaf))
        assert False  # TODO: implement your test here

class TestRemoveCommas(unittest.TestCase):
    def test_remove_commas(self):
        # self.assertEqual(expected, remove_commas(nodes))
        assert False  # TODO: implement your test here

class TestRemoveDefaults(unittest.TestCase):
    def test_remove_defaults(self):
        # self.assertEqual(expected, remove_defaults(nodes))
        assert False  # TODO: implement your test here

class TestDeriveClassName(unittest.TestCase):
    def test_derive_class_name(self):
        # self.assertEqual(expected, derive_class_name(node))
        assert False  # TODO: implement your test here

class TestDeriveClassNames(unittest.TestCase):
    def test_derive_class_names(self):
        # self.assertEqual(expected, derive_class_names(node))
        assert False  # TODO: implement your test here

class TestDeriveArgument(unittest.TestCase):
    def test_derive_argument(self):
        # self.assertEqual(expected, derive_argument(node))
        assert False  # TODO: implement your test here

class TestDeriveArgumentsFromTypedargslist(unittest.TestCase):
    def test_derive_arguments_from_typedargslist(self):
        # self.assertEqual(expected, derive_arguments_from_typedargslist(typedargslist))
        assert False  # TODO: implement your test here

class TestDeriveArguments(unittest.TestCase):
    def test_derive_arguments(self):
        # self.assertEqual(expected, derive_arguments(node))
        assert False  # TODO: implement your test here

class TestDeriveImportName(unittest.TestCase):
    def test_derive_import_name(self):
        # self.assertEqual(expected, derive_import_name(node))
        assert False  # TODO: implement your test here

class TestDeriveImportNames(unittest.TestCase):
    def test_derive_import_names(self):
        # self.assertEqual(expected, derive_import_names(node))
        assert False  # TODO: implement your test here

class TestASTVisitor(unittest.TestCase):
    def test___init__(self):
        # a_st_visitor = ASTVisitor()
        assert False  # TODO: implement your test here

    def test_register_pattern(self):
        # a_st_visitor = ASTVisitor()
        # self.assertEqual(expected, a_st_visitor.register_pattern(method, pattern))
        assert False  # TODO: implement your test here

    def test_visit(self):
        # a_st_visitor = ASTVisitor()
        # self.assertEqual(expected, a_st_visitor.visit(tree))
        assert False  # TODO: implement your test here

    def test_visit_class(self):
        # a_st_visitor = ASTVisitor()
        # self.assertEqual(expected, a_st_visitor.visit_class(name, bases, body))
        assert False  # TODO: implement your test here

    def test_visit_function(self):
        # a_st_visitor = ASTVisitor()
        # self.assertEqual(expected, a_st_visitor.visit_function(name, args, body))
        assert False  # TODO: implement your test here

    def test_visit_import(self):
        # a_st_visitor = ASTVisitor()
        # self.assertEqual(expected, a_st_visitor.visit_import(names, import_from, body))
        assert False  # TODO: implement your test here

    def test_visit_lambda_assign(self):
        # a_st_visitor = ASTVisitor()
        # self.assertEqual(expected, a_st_visitor.visit_lambda_assign(name, args))
        assert False  # TODO: implement your test here

    def test_visit_leaf(self):
        # a_st_visitor = ASTVisitor()
        # self.assertEqual(expected, a_st_visitor.visit_leaf(leaf))
        assert False  # TODO: implement your test here

    def test_visit_main_snippet(self):
        # a_st_visitor = ASTVisitor()
        # self.assertEqual(expected, a_st_visitor.visit_main_snippet(body))
        assert False  # TODO: implement your test here

    def test_visit_node(self):
        # a_st_visitor = ASTVisitor()
        # self.assertEqual(expected, a_st_visitor.visit_node(node))
        assert False  # TODO: implement your test here

if __name__ == '__main__':
    unittest.main()
