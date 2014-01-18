import unittest


class TestSortedByTimestamp(unittest.TestCase):
    def test_sorted_by_timestamp(self):
        # self.assertEqual(expected, sorted_by_timestamp(objects))
        assert False  # TODO: implement your test here

class TestOlderThan(unittest.TestCase):
    def test_older_than(self):
        # self.assertEqual(expected, older_than(events, reference_timestamp))
        assert False  # TODO: implement your test here

class TestNewerThan(unittest.TestCase):
    def test_newer_than(self):
        # self.assertEqual(expected, newer_than(events, reference_timestamp))
        assert False  # TODO: implement your test here

class TestTopCaller(unittest.TestCase):
    def test_top_caller(self):
        # self.assertEqual(expected, top_caller(call))
        assert False  # TODO: implement your test here

class TestSubcallsBeforeTimestamp(unittest.TestCase):
    def test_subcalls_before_timestamp(self):
        # self.assertEqual(expected, subcalls_before_timestamp(call, reference_timestamp))
        assert False  # TODO: implement your test here

class TestCallsBefore(unittest.TestCase):
    def test_calls_before(self):
        # self.assertEqual(expected, calls_before(call))
        assert False  # TODO: implement your test here

class TestSideEffectsOf(unittest.TestCase):
    def test_side_effects_of(self):
        # self.assertEqual(expected, side_effects_of(calls))
        assert False  # TODO: implement your test here

class TestSideEffectsBefore(unittest.TestCase):
    def test_side_effects_before(self):
        # self.assertEqual(expected, side_effects_before(call))
        assert False  # TODO: implement your test here

class TestObjectsAffectedBySideEffects(unittest.TestCase):
    def test_objects_affected_by_side_effects(self):
        # self.assertEqual(expected, objects_affected_by_side_effects(side_effects))
        assert False  # TODO: implement your test here

class TestResolveDependencies(unittest.TestCase):
    def test_resolve_dependencies(self):
        # self.assertEqual(expected, resolve_dependencies(events))
        assert False  # TODO: implement your test here

if __name__ == '__main__':
    unittest.main()
