import unittest


class TestRegisterSideEffectType(unittest.TestCase):
    def test_register_side_effect_type(self):
        # self.assertEqual(expected, register_side_effect_type(trigger, klass))
        assert False  # TODO: implement your test here

class TestRecognizeSideEffect(unittest.TestCase):
    def test_recognize_side_effect(self):
        # self.assertEqual(expected, recognize_side_effect(klass, func_name))
        assert False  # TODO: implement your test here

class TestMetaSideEffect(unittest.TestCase):
    def test___init__(self):
        # meta_side_effect = MetaSideEffect(*args, **kwds)
        assert False  # TODO: implement your test here

class TestSideEffect(unittest.TestCase):
    def test___init__(self):
        # side_effect = SideEffect(affected_objects, only_referenced_objects)
        assert False  # TODO: implement your test here

class TestGlobalVariableSideEffect(unittest.TestCase):
    def test___repr__(self):
        # global_variable_side_effect = GlobalVariableSideEffect()
        # self.assertEqual(expected, global_variable_side_effect.__repr__())
        assert False  # TODO: implement your test here

    def test_get_full_name(self):
        # global_variable_side_effect = GlobalVariableSideEffect()
        # self.assertEqual(expected, global_variable_side_effect.get_full_name())
        assert False  # TODO: implement your test here

class TestGlobalRead(unittest.TestCase):
    def test___init__(self):
        # global_read = GlobalRead(module, name, value)
        assert False  # TODO: implement your test here

class TestGlobalRebind(unittest.TestCase):
    def test___init__(self):
        # global_rebind = GlobalRebind(module, name, value)
        assert False  # TODO: implement your test here

class TestAttributeRebind(unittest.TestCase):
    def test___init__(self):
        # attribute_rebind = AttributeRebind(obj, name, value)
        assert False  # TODO: implement your test here

    def test___repr__(self):
        # attribute_rebind = AttributeRebind(obj, name, value)
        # self.assertEqual(expected, attribute_rebind.__repr__())
        assert False  # TODO: implement your test here

class TestBuiltinMethodWithPositionArgsSideEffect(unittest.TestCase):
    def test___init__(self):
        # builtin_method_with_position_args_side_effect = BuiltinMethodWithPositionArgsSideEffect(obj, *args)
        assert False  # TODO: implement your test here

    def test_args_mapping(self):
        # builtin_method_with_position_args_side_effect = BuiltinMethodWithPositionArgsSideEffect(obj, *args)
        # self.assertEqual(expected, builtin_method_with_position_args_side_effect.args_mapping())
        assert False  # TODO: implement your test here

if __name__ == '__main__':
    unittest.main()
