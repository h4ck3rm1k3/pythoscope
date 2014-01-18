import unittest


class TestGatheringResults(unittest.TestCase):
    def test___init__(self):
        # gathering_results = GatheringResults(loc, functions, classes, methods, passed, skipped, errors, failures, coverage)
        assert False  # TODO: implement your test here

class TestNotify(unittest.TestCase):
    def test_notify(self):
        # self.assertEqual(expected, notify(message))
        assert False  # TODO: implement your test here

class TestCheckEnvironment(unittest.TestCase):
    def test_check_environment(self):
        # self.assertEqual(expected, check_environment())
        assert False  # TODO: implement your test here

class TestPrepareProject(unittest.TestCase):
    def test_prepare_project(self):
        # self.assertEqual(expected, prepare_project(project))
        assert False  # TODO: implement your test here

class TestGetCodeMetricsFromFile(unittest.TestCase):
    def test_get_code_metrics_from_file(self):
        # self.assertEqual(expected, get_code_metrics_from_file(code))
        assert False  # TODO: implement your test here

class TestRlistdir(unittest.TestCase):
    def test_rlistdir(self):
        # self.assertEqual(expected, rlistdir(path))
        assert False  # TODO: implement your test here

class TestPythonModulesBelow(unittest.TestCase):
    def test_python_modules_below(self):
        # self.assertEqual(expected, python_modules_below(path))
        assert False  # TODO: implement your test here

class TestGetCodeMetrics(unittest.TestCase):
    def test_get_code_metrics(self):
        # self.assertEqual(expected, get_code_metrics(project_path))
        assert False  # TODO: implement your test here

class TestDoPythoscopeInit(unittest.TestCase):
    def test_do_pythoscope_init(self):
        # self.assertEqual(expected, do_pythoscope_init(project_path))
        assert False  # TODO: implement your test here

class TestPutPointOfEntry(unittest.TestCase):
    def test_put_point_of_entry(self):
        # self.assertEqual(expected, put_point_of_entry(poe, project_dir))
        assert False  # TODO: implement your test here

class TestRunSnippet(unittest.TestCase):
    def test_run_snippet(self):
        # self.assertEqual(expected, run_snippet(snippet, project_dir))
        assert False  # TODO: implement your test here

class TestGenerateTestsForFile(unittest.TestCase):
    def test_generate_tests_for_file(self):
        # self.assertEqual(expected, generate_tests_for_file(project_dir, appfile))
        assert False  # TODO: implement your test here

class TestContainsDynamicInspectionError(unittest.TestCase):
    def test_contains_dynamic_inspection_error(self):
        # self.assertEqual(expected, contains_dynamic_inspection_error(output))
        assert False  # TODO: implement your test here

class TestRunNosetests(unittest.TestCase):
    def test_run_nosetests(self):
        # self.assertEqual(expected, run_nosetests(project_dir, test_path))
        assert False  # TODO: implement your test here

class TestGetTestCounts(unittest.TestCase):
    def test_get_test_counts(self):
        # self.assertEqual(expected, get_test_counts(output))
        assert False  # TODO: implement your test here

class TestRunNosetestsWithCoverage(unittest.TestCase):
    def test_run_nosetests_with_coverage(self):
        # self.assertEqual(expected, run_nosetests_with_coverage(project_dir, test_path, cover_package))
        assert False  # TODO: implement your test here

class TestExtractCoveragePercent(unittest.TestCase):
    def test_extract_coverage_percent(self):
        # self.assertEqual(expected, extract_coverage_percent(output))
        assert False  # TODO: implement your test here

class TestCleanupProject(unittest.TestCase):
    def test_cleanup_project(self):
        # self.assertEqual(expected, cleanup_project(project_dir))
        assert False  # TODO: implement your test here

class TestPathExists(unittest.TestCase):
    def test_path_exists(self):
        # self.assertEqual(expected, path_exists(path))
        assert False  # TODO: implement your test here

class TestGatherMetricsFromProject(unittest.TestCase):
    def test_gather_metrics_from_project(self):
        # self.assertEqual(expected, gather_metrics_from_project(project, poes, snippets, appfile, testfile, cover_package, python_path))
        assert False  # TODO: implement your test here

if __name__ == '__main__':
    unittest.main()
