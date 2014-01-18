import unittest


class TestLine(unittest.TestCase):
    def test___init__(self):
        # line = Line(timestamp)
        assert False  # TODO: implement your test here

class TestEqualAssertionLine(unittest.TestCase):
    def test___init__(self):
        # equal_assertion_line = EqualAssertionLine(expected, actual, timestamp)
        assert False  # TODO: implement your test here

    def test___repr__(self):
        # equal_assertion_line = EqualAssertionLine(expected, actual, timestamp)
        # self.assertEqual(expected, equal_assertion_line.__repr__())
        assert False  # TODO: implement your test here

class TestEqualAssertionStubLine(unittest.TestCase):
    def test___init__(self):
        # equal_assertion_stub_line = EqualAssertionStubLine(actual, timestamp)
        assert False  # TODO: implement your test here

class TestGeneratorAssertionLine(unittest.TestCase):
    def test___init__(self):
        # generator_assertion_line = GeneratorAssertionLine(generator_call, timestamp)
        assert False  # TODO: implement your test here

class TestRaisesAssertionLine(unittest.TestCase):
    def test___init__(self):
        # raises_assertion_line = RaisesAssertionLine(expected_exception, call, timestamp)
        assert False  # TODO: implement your test here

class TestCommentLine(unittest.TestCase):
    def test___init__(self):
        # comment_line = CommentLine(comment, timestamp)
        assert False  # TODO: implement your test here

class TestSkipTestLine(unittest.TestCase):
    def test___init__(self):
        # skip_test_line = SkipTestLine(timestamp)
        assert False  # TODO: implement your test here

class TestModuleVariableReference(unittest.TestCase):
    def test___init__(self):
        # module_variable_reference = ModuleVariableReference(module, name, timestamp)
        assert False  # TODO: implement your test here

class TestObjectAttributeReference(unittest.TestCase):
    def test___init__(self):
        # object_attribute_reference = ObjectAttributeReference(obj, name, timestamp)
        assert False  # TODO: implement your test here

    def test___repr__(self):
        # object_attribute_reference = ObjectAttributeReference(obj, name, timestamp)
        # self.assertEqual(expected, object_attribute_reference.__repr__())
        assert False  # TODO: implement your test here

class TestBindingChange(unittest.TestCase):
    def test___init__(self):
        # binding_change = BindingChange(name, obj, timestamp)
        assert False  # TODO: implement your test here

    def test___repr__(self):
        # binding_change = BindingChange(name, obj, timestamp)
        # self.assertEqual(expected, binding_change.__repr__())
        assert False  # TODO: implement your test here

if __name__ == '__main__':
    unittest.main()
