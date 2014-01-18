import unittest


class TestIsTestClass(unittest.TestCase):
    def test_is_test_class(self):
        # self.assertEqual(expected, is_test_class(name, bases))
        assert False  # TODO: implement your test here

class TestUnindent(unittest.TestCase):
    def test_unindent(self):
        # self.assertEqual(expected, unindent(string))
        assert False  # TODO: implement your test here

class TestFunctionCodeFromDefinition(unittest.TestCase):
    def test_function_code_from_definition(self):
        # self.assertEqual(expected, function_code_from_definition(definition))
        assert False  # TODO: implement your test here

class TestIsGeneratorDefinition(unittest.TestCase):
    def test_is_generator_definition(self):
        # self.assertEqual(expected, is_generator_definition(definition))
        assert False  # TODO: implement your test here

class TestCreateDefinition(unittest.TestCase):
    def test_create_definition(self):
        # self.assertEqual(expected, create_definition(name, args, code, definition_type))
        assert False  # TODO: implement your test here

class TestModuleVisitor(unittest.TestCase):
    def test___init__(self):
        # module_visitor = ModuleVisitor()
        assert False  # TODO: implement your test here

    def test_visit_class(self):
        # module_visitor = ModuleVisitor()
        # self.assertEqual(expected, module_visitor.visit_class(name, bases, body))
        assert False  # TODO: implement your test here

    def test_visit_function(self):
        # module_visitor = ModuleVisitor()
        # self.assertEqual(expected, module_visitor.visit_function(name, args, body))
        assert False  # TODO: implement your test here

    def test_visit_import(self):
        # module_visitor = ModuleVisitor()
        # self.assertEqual(expected, module_visitor.visit_import(names, import_from, body))
        assert False  # TODO: implement your test here

    def test_visit_lambda_assign(self):
        # module_visitor = ModuleVisitor()
        # self.assertEqual(expected, module_visitor.visit_lambda_assign(name, args))
        assert False  # TODO: implement your test here

    def test_visit_main_snippet(self):
        # module_visitor = ModuleVisitor()
        # self.assertEqual(expected, module_visitor.visit_main_snippet(body))
        assert False  # TODO: implement your test here

class TestClassVisitor(unittest.TestCase):
    def test___init__(self):
        # class_visitor = ClassVisitor()
        assert False  # TODO: implement your test here

    def test_visit_class(self):
        # class_visitor = ClassVisitor()
        # self.assertEqual(expected, class_visitor.visit_class(name, bases, body))
        assert False  # TODO: implement your test here

    def test_visit_function(self):
        # class_visitor = ClassVisitor()
        # self.assertEqual(expected, class_visitor.visit_function(name, args, body))
        assert False  # TODO: implement your test here

class TestInspectModule(unittest.TestCase):
    def test_inspect_module(self):
        # self.assertEqual(expected, inspect_module(project, path))
        assert False  # TODO: implement your test here

class TestInspectCode(unittest.TestCase):
    def test_inspect_code(self):
        # self.assertEqual(expected, inspect_code(project, path, code))
        assert False  # TODO: implement your test here

if __name__ == '__main__':
    unittest.main()
