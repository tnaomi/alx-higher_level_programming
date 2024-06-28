import pytest
from models.base import Base

class Test_base():
    def test_base_create_no_id(self):
        """ Create a `Base` instance with no `id`"""
        none, none2, none3= Base(), Base(), Base()
        assert none.id==1 and none2.id == 2 and none3.id == 3
        assert none.id != none2.id != none3.id

    def test_base_create_none(self):
        assert Base(None).id == 4

    def test_base_create_id(self):
        """ Create a `Base` instance with `id` """
        new = Base(10)
        assert new.id==10

    def test_base_create_id_not_int(self):
        """ Create a `Base` instance with a non int `id`"""
        msg = "Yes"
        assert Base(msg).id == 5