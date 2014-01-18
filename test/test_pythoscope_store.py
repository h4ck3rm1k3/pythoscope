import unittest


class TestGetPythoscopePath(unittest.TestCase):
    def test_get_pythoscope_path(self):
        # self.assertEqual(expected, get_pythoscope_path(project_path))
        assert False  # TODO: implement your test here

class TestGetPicklePath(unittest.TestCase):
    def test_get_pickle_path(self):
        # self.assertEqual(expected, get_pickle_path(project_path))
        assert False  # TODO: implement your test here

class TestGetPointsOfEntryPath(unittest.TestCase):
    def test_get_points_of_entry_path(self):
        # self.assertEqual(expected, get_points_of_entry_path(project_path))
        assert False  # TODO: implement your test here

class TestGetCodeTreesPath(unittest.TestCase):
    def test_get_code_trees_path(self):
        # self.assertEqual(expected, get_code_trees_path(project_path))
        assert False  # TODO: implement your test here

class TestModuleLevelId(unittest.TestCase):
    def test_module_level_id(self):
        # self.assertEqual(expected, module_level_id(obj))
        assert False  # TODO: implement your test here

class TestObjectInModule(unittest.TestCase):
    def test___init__(self):
        # object_in_module = ObjectInModule(name, code)
        assert False  # TODO: implement your test here

class TestDefinition(unittest.TestCase):
    def test___init__(self):
        # definition = Definition(name, args, code, is_generator)
        assert False  # TODO: implement your test here

class TestCall(unittest.TestCase):
    def test___eq__(self):
        # call = Call(definition, args, output, exception)
        # self.assertEqual(expected, call.__eq__(other))
        assert False  # TODO: implement your test here

    def test___hash__(self):
        # call = Call(definition, args, output, exception)
        # self.assertEqual(expected, call.__hash__())
        assert False  # TODO: implement your test here

    def test___init__(self):
        # call = Call(definition, args, output, exception)
        assert False  # TODO: implement your test here

    def test___repr__(self):
        # call = Call(definition, args, output, exception)
        # self.assertEqual(expected, call.__repr__())
        assert False  # TODO: implement your test here

    def test_add_side_effect(self):
        # call = Call(definition, args, output, exception)
        # self.assertEqual(expected, call.add_side_effect(side_effect))
        assert False  # TODO: implement your test here

    def test_add_subcall(self):
        # call = Call(definition, args, output, exception)
        # self.assertEqual(expected, call.add_subcall(call))
        assert False  # TODO: implement your test here

    def test_clear_exception(self):
        # call = Call(definition, args, output, exception)
        # self.assertEqual(expected, call.clear_exception())
        assert False  # TODO: implement your test here

    def test_raised_exception(self):
        # call = Call(definition, args, output, exception)
        # self.assertEqual(expected, call.raised_exception())
        assert False  # TODO: implement your test here

    def test_set_exception(self):
        # call = Call(definition, args, output, exception)
        # self.assertEqual(expected, call.set_exception(exception))
        assert False  # TODO: implement your test here

    def test_set_output(self):
        # call = Call(definition, args, output, exception)
        # self.assertEqual(expected, call.set_output(output))
        assert False  # TODO: implement your test here

class TestCallToC(unittest.TestCase):
    def test___init__(self):
        # call_to_c = CallToC(name, side_effect)
        assert False  # TODO: implement your test here

    def test_clear_side_effect(self):
        # call_to_c = CallToC(name, side_effect)
        # self.assertEqual(expected, call_to_c.clear_side_effect())
        assert False  # TODO: implement your test here

class TestUnknownCall(unittest.TestCase):
    def test___init__(self):
        # unknown_call = UnknownCall()
        assert False  # TODO: implement your test here

class TestCallable(unittest.TestCase):
    def test___init__(self):
        # callable = Callable(calls)
        assert False  # TODO: implement your test here

    def test_add_call(self):
        # callable = Callable(calls)
        # self.assertEqual(expected, callable.add_call(call))
        assert False  # TODO: implement your test here

class TestFunction(unittest.TestCase):
    def test___init__(self):
        # function = Function(name, args, code, calls, is_generator, module)
        assert False  # TODO: implement your test here

    def test___repr__(self):
        # function = Function(name, args, code, calls, is_generator, module)
        # self.assertEqual(expected, function.__repr__())
        assert False  # TODO: implement your test here

    def test_get_unique_calls(self):
        # function = Function(name, args, code, calls, is_generator, module)
        # self.assertEqual(expected, function.get_unique_calls())
        assert False  # TODO: implement your test here

class TestGeneratorObject(unittest.TestCase):
    def test___init__(self):
        # generator_object = GeneratorObject(obj, generator, args, callable)
        assert False  # TODO: implement your test here

    def test___repr__(self):
        # generator_object = GeneratorObject(obj, generator, args, callable)
        # self.assertEqual(expected, generator_object.__repr__())
        assert False  # TODO: implement your test here

    def test_activate(self):
        # generator_object = GeneratorObject(obj, generator, args, callable)
        # self.assertEqual(expected, generator_object.activate(generator, args, callable))
        assert False  # TODO: implement your test here

    def test_is_activated(self):
        # generator_object = GeneratorObject(obj, generator, args, callable)
        # self.assertEqual(expected, generator_object.is_activated())
        assert False  # TODO: implement your test here

    def test_raised_exception(self):
        # generator_object = GeneratorObject(obj, generator, args, callable)
        # self.assertEqual(expected, generator_object.raised_exception())
        assert False  # TODO: implement your test here

class TestUserObject(unittest.TestCase):
    def test___init__(self):
        # user_object = UserObject(obj, klass)
        assert False  # TODO: implement your test here

    def test___repr__(self):
        # user_object = UserObject(obj, klass)
        # self.assertEqual(expected, user_object.__repr__())
        assert False  # TODO: implement your test here

    def test_get_external_calls(self):
        # user_object = UserObject(obj, klass)
        # self.assertEqual(expected, user_object.get_external_calls())
        assert False  # TODO: implement your test here

    def test_get_init_and_external_calls(self):
        # user_object = UserObject(obj, klass)
        # self.assertEqual(expected, user_object.get_init_and_external_calls())
        assert False  # TODO: implement your test here

    def test_get_init_call(self):
        # user_object = UserObject(obj, klass)
        # self.assertEqual(expected, user_object.get_init_call())
        assert False  # TODO: implement your test here

    def test_is_external_call(self):
        # user_object = UserObject(obj, klass)
        # self.assertEqual(expected, user_object.is_external_call(call))
        assert False  # TODO: implement your test here

if __name__ == '__main__':
    unittest.main()
