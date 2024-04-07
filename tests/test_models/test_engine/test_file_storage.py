#!/usr/bin/python3
"""
    tests for FileStorage
"""
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import os


class TestFileStorage(unittest.TestCase):
    """
        Test class for FileStorage
    """
    @classmethod
    def setUpClass(cls):
        """
            Setup class
        """
        cls.dummy = FileStorage()

    @classmethod
    def tearDownClass(cls):
        """
            Teardown class
        """
        del cls.dummy
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_attributes(self):
        """
            Test attributes
        """
        self.assertTrue(hasattr(self.dummy, "_FileStorage__objects"))
        self.assertTrue(isinstance(self.dummy._FileStorage__objects, dict))
        self.assertTrue(hasattr(self.dummy, "_FileStorage__file_path"))
        self.assertTrue(isinstance(self.dummy._FileStorage__file_path, str))

    def test_all(self):
        """
            Test all method
        """
        new_model = BaseModel()
        self.dummy.new(new_model)
        objects = self.dummy.all()
        self.assertTrue(isinstance(objects, dict))
        self.assertIn("BaseModel." + new_model.id, objects)

    def test_new_save_reload(self):
        """
            Test new, save, reload methods
        """
        new_model = BaseModel()
        self.dummy.new(new_model)
        self.assertTrue("BaseModel." + new_model.id in self.dummy._FileStorage__objects)
        self.dummy.save()
        self.dummy._FileStorage__objects = {}
        self.dummy.reload()
        self.assertTrue("BaseModel." + new_model.id in self.dummy.all())

    def test_delete(self):
        """
            Test delete method
        """
        new_model = BaseModel()
        self.dummy.new(new_model)
        self.assertTrue("BaseModel." + new_model.id in self.dummy._FileStorage__objects)
        self.dummy.delete(new_model)
        self.assertTrue("BaseModel." + new_model.id not in self.dummy._FileStorage__objects)

if __name__ == "__main__":
    unittest.main()

