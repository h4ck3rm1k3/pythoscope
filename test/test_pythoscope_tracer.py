import unittest


class TestFindVariable(unittest.TestCase):
    def test_find_variable(self):
        # self.assertEqual(expected, find_variable(frame, varname))
        assert False  # TODO: implement your test here

class TestCallableType(unittest.TestCase):
    def test_callable_type(self):
        # self.assertEqual(expected, callable_type(frame))
        assert False  # TODO: implement your test here

class TestIsClassDefinition(unittest.TestCase):
    def test_is_class_definition(self):
        # self.assertEqual(expected, is_class_definition(frame))
        assert False  # TODO: implement your test here

class TestGetMethodInformation(unittest.TestCase):
    def test_get_method_information(self):
        # self.assertEqual(expected, get_method_information(frame))
        assert False  # TODO: implement your test here

class TestResolveArgs(unittest.TestCase):
    def test_resolve_args(self):
        # self.assertEqual(expected, resolve_args(names, locals))
        assert False  # TODO: implement your test here

class TestInputFromArgvalues(unittest.TestCase):
    def test_input_from_argvalues(self):
        # self.assertEqual(expected, input_from_argvalues(args, varargs, varkw, locals))
        assert False  # TODO: implement your test here

class TestMakeCallable(unittest.TestCase):
    def test_make_callable(self):
        # self.assertEqual(expected, make_callable(code))
        assert False  # TODO: implement your test here

class TestIsGeneratorExit(unittest.TestCase):
    def test_is_generator_exit(self):
        # self.assertEqual(expected, is_generator_exit(obj))
        assert False  # TODO: implement your test here

class TestWithoutExtension(unittest.TestCase):
    def test_without_extension(self):
        # self.assertEqual(expected, without_extension(path))
        assert False  # TODO: implement your test here

class TestWholeStack(unittest.TestCase):
    def test_whole_stack(self):
        # self.assertEqual(expected, whole_stack(frame))
        assert False  # TODO: implement your test here

class TestIsFrameFromCodeRewritingImporter(unittest.TestCase):
    def test_is_frame_from_code_rewriting_importer(self):
        # self.assertEqual(expected, is_frame_from_code_rewriting_importer(frame))
        assert False  # TODO: implement your test here

class TestIsCalledFromCodeRewritingImporter(unittest.TestCase):
    def test_is_called_from_code_rewriting_importer(self):
        # self.assertEqual(expected, is_called_from_code_rewriting_importer(frame))
        assert False  # TODO: implement your test here

class TestStandardTracer(unittest.TestCase):
    def test___init__(self):
        # standard_tracer = StandardTracer(callback)
        assert False  # TODO: implement your test here

    def test_handle_bytecode_tracer_event(self):
        # standard_tracer = StandardTracer(callback)
        # self.assertEqual(expected, standard_tracer.handle_bytecode_tracer_event(event, args))
        assert False  # TODO: implement your test here

    def test_handle_standard_tracer_event(self):
        # standard_tracer = StandardTracer(callback)
        # self.assertEqual(expected, standard_tracer.handle_standard_tracer_event(frame, event, arg))
        assert False  # TODO: implement your test here

    def test_is_ignored_code(self):
        # standard_tracer = StandardTracer(callback)
        # self.assertEqual(expected, standard_tracer.is_ignored_code(code))
        assert False  # TODO: implement your test here

    def test_record_c_call(self):
        # standard_tracer = StandardTracer(callback)
        # self.assertEqual(expected, standard_tracer.record_c_call(func, pargs, kargs))
        assert False  # TODO: implement your test here

    def test_record_call(self):
        # standard_tracer = StandardTracer(callback)
        # self.assertEqual(expected, standard_tracer.record_call(frame))
        assert False  # TODO: implement your test here

    def test_setup(self):
        # standard_tracer = StandardTracer(callback)
        # self.assertEqual(expected, standard_tracer.setup(code))
        assert False  # TODO: implement your test here

    def test_should_ignore_frame(self):
        # standard_tracer = StandardTracer(callback)
        # self.assertEqual(expected, standard_tracer.should_ignore_frame(frame))
        assert False  # TODO: implement your test here

    def test_teardown(self):
        # standard_tracer = StandardTracer(callback)
        # self.assertEqual(expected, standard_tracer.teardown())
        assert False  # TODO: implement your test here

    def test_trace(self):
        # standard_tracer = StandardTracer(callback)
        # self.assertEqual(expected, standard_tracer.trace(code))
        assert False  # TODO: implement your test here

    def test_tracer(self):
        # standard_tracer = StandardTracer(callback)
        # self.assertEqual(expected, standard_tracer.tracer(frame, event, arg))
        assert False  # TODO: implement your test here

class TestPython23Tracer(unittest.TestCase):
    def test___init__(self):
        # python23_tracer = Python23Tracer(*args)
        assert False  # TODO: implement your test here

    def test_handle_standard_tracer_event(self):
        # python23_tracer = Python23Tracer(*args)
        # self.assertEqual(expected, python23_tracer.handle_standard_tracer_event(frame, event, arg))
        assert False  # TODO: implement your test here

class TestICallback(unittest.TestCase):
    def test_attribute_rebound(self):
        # i_callback = ICallback()
        # self.assertEqual(expected, i_callback.attribute_rebound(obj, name, value))
        assert False  # TODO: implement your test here

    def test_c_function_called(self):
        # i_callback = ICallback()
        # self.assertEqual(expected, i_callback.c_function_called(name, pargs))
        assert False  # TODO: implement your test here

    def test_c_method_called(self):
        # i_callback = ICallback()
        # self.assertEqual(expected, i_callback.c_method_called(obj, klass, name, pargs))
        assert False  # TODO: implement your test here

    def test_c_returned(self):
        # i_callback = ICallback()
        # self.assertEqual(expected, i_callback.c_returned(output))
        assert False  # TODO: implement your test here

    def test_function_called(self):
        # i_callback = ICallback()
        # self.assertEqual(expected, i_callback.function_called(name, args, code, frame))
        assert False  # TODO: implement your test here

    def test_global_read(self):
        # i_callback = ICallback()
        # self.assertEqual(expected, i_callback.global_read(module, name, value))
        assert False  # TODO: implement your test here

    def test_global_rebound(self):
        # i_callback = ICallback()
        # self.assertEqual(expected, i_callback.global_rebound(module, name, value))
        assert False  # TODO: implement your test here

    def test_method_called(self):
        # i_callback = ICallback()
        # self.assertEqual(expected, i_callback.method_called(name, obj, args, code, frame))
        assert False  # TODO: implement your test here

    def test_raised(self):
        # i_callback = ICallback()
        # self.assertEqual(expected, i_callback.raised(exception, traceback))
        assert False  # TODO: implement your test here

    def test_returned(self):
        # i_callback = ICallback()
        # self.assertEqual(expected, i_callback.returned(output))
        assert False  # TODO: implement your test here

if __name__ == '__main__':
    unittest.main()
