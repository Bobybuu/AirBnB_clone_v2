#!/usr/bin/python3
"""
    tests for FileStorage
"""
import unittest
from models.base_model import BaseModel
from models.engine.db_storage import DBStorage
from sqlalchemy.engine.base import Engine
from sqlalchemy.orm.session import Session


class TestDBStorage(unittest.TestCase):
    """
        Test class for DBStorage
    """
    @classmethod
    def setUpClass(cls):
        """
            setup
        """
        cls.dummy = DBStorage()

    @classmethod
    def tearDownClass(cls):
        """
            tear down
        """
        del cls.dummy

    def test_attributes(self):
        """
            Test attributes
        """
        self.assertTrue(hasattr(self.dummy, '_DBStorage__engine'))
        self.assertTrue(hasattr(self.dummy, '_DBStorage__session'))
        self.assertTrue(isinstance(self.dummy._DBStorage__engine, Engine))
        self.assertTrue(self.dummy._DBStorage__session is None)

    def test_new_save_all(self):
        """
            Test new, save, all methods
        """
        new_model = BaseModel()
        self.dummy.new(new_model)
        self.assertTrue(new_model in self.dummy.all(BaseModel))
        self.dummy.save()
        self.assertTrue(new_model in self.dummy.all(BaseModel))

    def test_delete(self):
        """
            Test delete method
        """
        new_model = BaseModel()
        self.dummy.new(new_model)
        self.assertTrue(new_model in self.dummy.all(BaseModel))
        self.dummy.delete(new_model)
        self.assertTrue(new_model not in self.dummy.all(BaseModel))

    def test_reload(self):
        """
            Test reload method
        """
        new_model = BaseModel()
        new_model.save()
        self.assertTrue(new_model in self.dummy.all(BaseModel))
        self.dummy.reload()
        self.assertTrue(new_model in self.dummy.all(BaseModel))

if __name__ == "__main__":
    unittest.main()

