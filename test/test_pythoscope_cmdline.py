import unittest


class TestFail(unittest.TestCase):
    def test_fail(self):
        # self.assertEqual(expected, fail(message))
        assert False  # TODO: implement your test here

class TestFindProjectDirectory(unittest.TestCase):
    def test_find_project_directory(self):
        # self.assertEqual(expected, find_project_directory(path))
        assert False  # TODO: implement your test here

class TestInitProject(unittest.TestCase):
    def test_init_project(self):
        # self.assertEqual(expected, init_project(path, skip_inspection))
        assert False  # TODO: implement your test here

class TestGenerateTests(unittest.TestCase):
    def test_generate_tests(self):
        # self.assertEqual(expected, generate_tests(modules, force, template))
        assert False  # TODO: implement your test here

if __name__ == '__main__':
    unittest.main()
