import unittest


class TestImportManager(unittest.TestCase):
    def test___init__(self):
        # import_manager = ImportManager()
        assert False  # TODO: implement your test here

    def test___init___case_2(self):
        # import_manager = ImportManager()
        assert False  # TODO: implement your test here

    def test_add_suffix(self):
        # import_manager = ImportManager()
        # self.assertEqual(expected, import_manager.add_suffix(suffix, importFunc))
        assert False  # TODO: implement your test here

    def test_install(self):
        # import_manager = ImportManager()
        # self.assertEqual(expected, import_manager.install(namespace))
        assert False  # TODO: implement your test here

    def test_uninstall(self):
        # import_manager = ImportManager()
        # self.assertEqual(expected, import_manager.uninstall())
        assert False  # TODO: implement your test here

class TestImporter(unittest.TestCase):
    def test_get_code(self):
        # importer = Importer()
        # self.assertEqual(expected, importer.get_code(parent, modname, fqname))
        assert False  # TODO: implement your test here

    def test_import_top(self):
        # importer = Importer()
        # self.assertEqual(expected, importer.import_top(name))
        assert False  # TODO: implement your test here

class TestBuiltinImporter(unittest.TestCase):
    def test_get_code(self):
        # builtin_importer = BuiltinImporter()
        # self.assertEqual(expected, builtin_importer.get_code(parent, modname, fqname))
        assert False  # TODO: implement your test here

class test__FilesystemImporter(unittest.TestCase):
    def test___init__(self):
        # __filesystem_importer = _FilesystemImporter()
        assert False  # TODO: implement your test here

    def test_add_suffix(self):
        # __filesystem_importer = _FilesystemImporter()
        # self.assertEqual(expected, __filesystem_importer.add_suffix(suffix, importFunc))
        assert False  # TODO: implement your test here

    def test_get_code(self):
        # __filesystem_importer = _FilesystemImporter()
        # self.assertEqual(expected, __filesystem_importer.get_code(parent, modname, fqname))
        assert False  # TODO: implement your test here

    def test_import_from_dir(self):
        # __filesystem_importer = _FilesystemImporter()
        # self.assertEqual(expected, __filesystem_importer.import_from_dir(dir, fqname))
        assert False  # TODO: implement your test here

class TestPySuffixImporter(unittest.TestCase):
    def test_py_suffix_importer(self):
        # self.assertEqual(expected, py_suffix_importer(filename, finfo, fqname))
        assert False  # TODO: implement your test here

class TestDynLoadSuffixImporter(unittest.TestCase):
    def test___init__(self):
        # dyn_load_suffix_importer = DynLoadSuffixImporter(desc)
        assert False  # TODO: implement your test here

    def test_import_file(self):
        # dyn_load_suffix_importer = DynLoadSuffixImporter(desc)
        # self.assertEqual(expected, dyn_load_suffix_importer.import_file(filename, finfo, fqname))
        assert False  # TODO: implement your test here

if __name__ == '__main__':
    unittest.main()
