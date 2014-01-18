import unittest


class TestAddTestCaseToProject(unittest.TestCase):
    def test_add_test_case_to_project(self):
        # self.assertEqual(expected, add_test_case_to_project(project, test_class, main_snippet, force))
        assert False  # TODO: implement your test here

class TestAddTestCaseWithoutAppend(unittest.TestCase):
    def test_add_test_case_without_append(self):
        # self.assertEqual(expected, add_test_case_without_append(test_suite, test_case))
        assert False  # TODO: implement your test here

class TestAddTestCase(unittest.TestCase):
    def test_add_test_case(self):
        # self.assertEqual(expected, add_test_case(test_suite, test_case))
        assert False  # TODO: implement your test here

class TestEnsureMainSnippet(unittest.TestCase):
    def test_ensure_main_snippet(self):
        # self.assertEqual(expected, ensure_main_snippet(module, main_snippet, force))
        assert False  # TODO: implement your test here

class TestEnsureImports(unittest.TestCase):
    def test_ensure_imports(self):
        # self.assertEqual(expected, ensure_imports(test_suite, imports))
        assert False  # TODO: implement your test here

class TestInsertAfterOtherImports(unittest.TestCase):
    def test_insert_after_other_imports(self):
        # self.assertEqual(expected, insert_after_other_imports(module, code))
        assert False  # TODO: implement your test here

class TestFindTestClassByName(unittest.TestCase):
    def test_find_test_class_by_name(self):
        # self.assertEqual(expected, find_test_class_by_name(project, name))
        assert False  # TODO: implement your test here

class TestMergeTestClasses(unittest.TestCase):
    def test_merge_test_classes(self):
        # self.assertEqual(expected, merge_test_classes(test_class, other_test_class, force))
        assert False  # TODO: implement your test here

class TestReplaceTestCase(unittest.TestCase):
    def test_replace_test_case(self):
        # self.assertEqual(expected, replace_test_case(test_suite, old_test_case, new_test_case))
        assert False  # TODO: implement your test here

class TestFindModuleForTestClass(unittest.TestCase):
    def test_find_module_for_test_class(self):
        # self.assertEqual(expected, find_module_for_test_class(project, test_class))
        assert False  # TODO: implement your test here

class TestFindTestModule(unittest.TestCase):
    def test_find_test_module(self):
        # self.assertEqual(expected, find_test_module(project, test_class))
        assert False  # TODO: implement your test here

class TestFindAssociateTestModuleByName(unittest.TestCase):
    def test_find_associate_test_module_by_name(self):
        # self.assertEqual(expected, find_associate_test_module_by_name(project, module))
        assert False  # TODO: implement your test here

class TestFindAssociateTestModuleByTestClass(unittest.TestCase):
    def test_find_associate_test_module_by_test_class(self):
        # self.assertEqual(expected, find_associate_test_module_by_test_class(project, module))
        assert False  # TODO: implement your test here

class TestTestModuleNameForTestCase(unittest.TestCase):
    def test_test_module_name_for_test_case(self):
        # self.assertEqual(expected, test_module_name_for_test_case(test_case))
        assert False  # TODO: implement your test here

class TestCreateTestModule(unittest.TestCase):
    def test_create_test_module(self):
        # self.assertEqual(expected, create_test_module(project, test_case))
        assert False  # TODO: implement your test here

class TestModulePathToTestPath(unittest.TestCase):
    def test_module_path_to_test_path(self):
        # self.assertEqual(expected, module_path_to_test_path(module))
        assert False  # TODO: implement your test here

class TestPossibleTestModuleNames(unittest.TestCase):
    def test_possible_test_module_names(self):
        # self.assertEqual(expected, possible_test_module_names(module))
        assert False  # TODO: implement your test here

class TestPossibleTestModulePaths(unittest.TestCase):
    def test_possible_test_module_paths(self):
        # self.assertEqual(expected, possible_test_module_paths(module, new_tests_directory))
        assert False  # TODO: implement your test here

if __name__ == '__main__':
    unittest.main()
