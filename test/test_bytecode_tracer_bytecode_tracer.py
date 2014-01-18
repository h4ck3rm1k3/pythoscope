import unittest


class TestValueStack(unittest.TestCase):
    def test___init__(self):
        # value_stack = ValueStack(frame, bcode)
        assert False  # TODO: implement your test here

    def test_bottom(self):
        # value_stack = ValueStack(frame, bcode)
        # self.assertEqual(expected, value_stack.bottom())
        assert False  # TODO: implement your test here

    def test_keyword_args(self):
        # value_stack = ValueStack(frame, bcode)
        # self.assertEqual(expected, value_stack.keyword_args())
        assert False  # TODO: implement your test here

    def test_keyword_args_from_double_star(self):
        # value_stack = ValueStack(frame, bcode)
        # self.assertEqual(expected, value_stack.keyword_args_from_double_star())
        assert False  # TODO: implement your test here

    def test_keyword_args_from_stack(self):
        # value_stack = ValueStack(frame, bcode)
        # self.assertEqual(expected, value_stack.keyword_args_from_stack())
        assert False  # TODO: implement your test here

    def test_positional_args(self):
        # value_stack = ValueStack(frame, bcode)
        # self.assertEqual(expected, value_stack.positional_args())
        assert False  # TODO: implement your test here

    def test_positional_args_from_stack(self):
        # value_stack = ValueStack(frame, bcode)
        # self.assertEqual(expected, value_stack.positional_args_from_stack())
        assert False  # TODO: implement your test here

    def test_positional_args_from_varargs(self):
        # value_stack = ValueStack(frame, bcode)
        # self.assertEqual(expected, value_stack.positional_args_from_varargs())
        assert False  # TODO: implement your test here

    def test_values(self):
        # value_stack = ValueStack(frame, bcode)
        # self.assertEqual(expected, value_stack.values(offset, count))
        assert False  # TODO: implement your test here

class TestFlatlistToDict(unittest.TestCase):
    def test_flatlist_to_dict(self):
        # self.assertEqual(expected, flatlist_to_dict(alist))
        assert False  # TODO: implement your test here

class TestBytecode(unittest.TestCase):
    def test___init__(self):
        # bytecode = Bytecode(name, arg1, arg2)
        assert False  # TODO: implement your test here

class TestCurrentBytecode(unittest.TestCase):
    def test_current_bytecode(self):
        # self.assertEqual(expected, current_bytecode(frame))
        assert False  # TODO: implement your test here

class TestIsCFunc(unittest.TestCase):
    def test_is_c_func(self):
        # self.assertEqual(expected, is_c_func(func))
        assert False  # TODO: implement your test here

class TestNameFromArg(unittest.TestCase):
    def test_name_from_arg(self):
        # self.assertEqual(expected, name_from_arg(frame, bcode))
        assert False  # TODO: implement your test here

class TestFrameModule(unittest.TestCase):
    def test_frame_module(self):
        # self.assertEqual(expected, frame_module(frame))
        assert False  # TODO: implement your test here

class TestStandardBytecodeTracer(unittest.TestCase):
    def test___init__(self):
        # standard_bytecode_tracer = StandardBytecodeTracer()
        assert False  # TODO: implement your test here

    def test_setup(self):
        # standard_bytecode_tracer = StandardBytecodeTracer()
        # self.assertEqual(expected, standard_bytecode_tracer.setup())
        assert False  # TODO: implement your test here

    def test_teardown(self):
        # standard_bytecode_tracer = StandardBytecodeTracer()
        # self.assertEqual(expected, standard_bytecode_tracer.teardown())
        assert False  # TODO: implement your test here

    def test_trace(self):
        # standard_bytecode_tracer = StandardBytecodeTracer()
        # self.assertEqual(expected, standard_bytecode_tracer.trace(frame, event))
        assert False  # TODO: implement your test here

class TestPython23BytecodeTracer(unittest.TestCase):
    def test___init__(self):
        # python23_bytecode_tracer = Python23BytecodeTracer(*args)
        assert False  # TODO: implement your test here

    def test_trace(self):
        # python23_bytecode_tracer = Python23BytecodeTracer(*args)
        # self.assertEqual(expected, python23_bytecode_tracer.trace(frame, event))
        assert False  # TODO: implement your test here

class TestRewriteLnotab(unittest.TestCase):
    def test_rewrite_lnotab(self):
        # self.assertEqual(expected, rewrite_lnotab(code))
        assert False  # TODO: implement your test here

class TestRewriteAll(unittest.TestCase):
    def test_rewrite_all(self):
        # self.assertEqual(expected, rewrite_all(objects))
        assert False  # TODO: implement your test here

class TestHasBeenRewritten(unittest.TestCase):
    def test_has_been_rewritten(self):
        # self.assertEqual(expected, has_been_rewritten(code))
        assert False  # TODO: implement your test here

if __name__ == '__main__':
    unittest.main()
