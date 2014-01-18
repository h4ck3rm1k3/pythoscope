import unittest


class TestGetHumanReadableId(unittest.TestCase):
    def test_get_human_readable_id(self):
        # self.assertEqual(expected, get_human_readable_id(obj))
        assert False  # TODO: implement your test here

class TestGetTypeName(unittest.TestCase):
    def test_get_type_name(self):
        # self.assertEqual(expected, get_type_name(obj))
        assert False  # TODO: implement your test here

class TestSerializedObject(unittest.TestCase):
    def test___init__(self):
        # serialized_object = SerializedObject(obj)
        assert False  # TODO: implement your test here

class TestImmutableObject(unittest.TestCase):
    def test___eq__(self):
        # immutable_object = ImmutableObject(obj)
        # self.assertEqual(expected, immutable_object.__eq__(other))
        assert False  # TODO: implement your test here

    def test___hash__(self):
        # immutable_object = ImmutableObject(obj)
        # self.assertEqual(expected, immutable_object.__hash__())
        assert False  # TODO: implement your test here

    def test___init__(self):
        # immutable_object = ImmutableObject(obj)
        assert False  # TODO: implement your test here

    def test___repr__(self):
        # immutable_object = ImmutableObject(obj)
        # self.assertEqual(expected, immutable_object.__repr__())
        assert False  # TODO: implement your test here

    def test_get_reconstructor_with_imports(self):
        # immutable_object = ImmutableObject(obj)
        # self.assertEqual(expected, immutable_object.get_reconstructor_with_imports())
        assert False  # TODO: implement your test here

class TestUnknownObject(unittest.TestCase):
    def test___init__(self):
        # unknown_object = UnknownObject(obj)
        assert False  # TODO: implement your test here

    def test___repr__(self):
        # unknown_object = UnknownObject(obj)
        # self.assertEqual(expected, unknown_object.__repr__())
        assert False  # TODO: implement your test here

class TestLibraryObject(unittest.TestCase):
    def test___init__(self):
        # library_object = LibraryObject(obj, serialize)
        assert False  # TODO: implement your test here

class TestSequenceObject(unittest.TestCase):
    def test___init__(self):
        # sequence_object = SequenceObject(obj, serialize)
        assert False  # TODO: implement your test here

class TestMapObject(unittest.TestCase):
    def test___init__(self):
        # map_object = MapObject(obj, serialize)
        assert False  # TODO: implement your test here

class TestBuiltinException(unittest.TestCase):
    def test___init__(self):
        # builtin_exception = BuiltinException(obj, serialize)
        assert False  # TODO: implement your test here

class TestIsImmutable(unittest.TestCase):
    def test_is_immutable(self):
        # self.assertEqual(expected, is_immutable(obj))
        assert False  # TODO: implement your test here

class TestIdOfClassOf(unittest.TestCase):
    def test_id_of_class_of(self):
        # self.assertEqual(expected, id_of_class_of(obj))
        assert False  # TODO: implement your test here

class TestIsLibraryObject(unittest.TestCase):
    def test_is_library_object(self):
        # self.assertEqual(expected, is_library_object(obj))
        assert False  # TODO: implement your test here

class TestIsMapping(unittest.TestCase):
    def test_is_mapping(self):
        # self.assertEqual(expected, is_mapping(obj))
        assert False  # TODO: implement your test here

class TestIsSequence(unittest.TestCase):
    def test_is_sequence(self):
        # self.assertEqual(expected, is_sequence(obj))
        assert False  # TODO: implement your test here

class TestIsBuiltinException(unittest.TestCase):
    def test_is_builtin_exception(self):
        # self.assertEqual(expected, is_builtin_exception(obj))
        assert False  # TODO: implement your test here

class TestIsSerializedString(unittest.TestCase):
    def test_is_serialized_string(self):
        # self.assertEqual(expected, is_serialized_string(obj))
        assert False  # TODO: implement your test here

if __name__ == '__main__':
    unittest.main()
