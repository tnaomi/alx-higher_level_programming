#!/usr/bin/python3
""" Test `Rectangle` """
import pytest
from models.rectangle import Rectangle

class TestRectangle():
    """ Test Rectangle class """
    def test_rectangle_has_doc(self):
        """ Verify if Rectangle has documentation """
        assert hasattr(Rectangle, "__doc__")

    def test_rectangle_create_all_args(self):
        """ Test `Rectangle` instance with all args """
        new = Rectangle(4, 3, 2, 1, 12)
        assert new.id == 12
        assert new.width == 4
        assert new.height == 3
        assert new.x == 2
        assert new.y == 1

    def test_rectangle_create_defaults(self):
        """ Create a `Rectangle` instance w defaults """
        new = Rectangle(1, 2)
        assert hasattr(new, "id")
        assert new.width == 1
        assert new.height == 2
        assert new.x == 0
        assert new.y == 0

    def test_rectangle_create_w_default(self):
        """ Create `Rectangle` with one default """
        new = Rectangle(width=1, height=2, x=3, id=18)
        assert new.width == 1
        assert new.height == 2 
        assert new.id == 18
        assert new.x == 3
        assert new.y == 0
        new2 = Rectangle(width=1, height=2, y=3, id=18)
        assert new2.width == 1
        assert new2.height == 2 
        assert new2.id == 18
        assert new2.y == 3
        assert new2.x == 0
        new3 = Rectangle(1,2,3,3)
        assert new3.width == 1
        assert new3.height == 2
        assert new3.x == 3
        assert new3.y == 3
        assert hasattr(new3, "id")

class TestRectangleValidation():
    """ Test Rectangle validation"""
    def test_zero_width(self):
        """ Assert zero `width` """
        with pytest.raises(ValueError) as VE:
            new = Rectangle(0, 1, 2, 3, 10)
        assert "width must be > 0" in str(VE.value)

    def test_zero_height(self):
        """ Assert zero `height` """
        with pytest.raises(ValueError) as VE:
            new = Rectangle(1, 0, 2, 3, 10)
        assert "height must be > 0" in str(VE.value)

    def test_negative_width(self):
        """ Test negative `width` """
        with pytest.raises(ValueError) as VE:
            new = Rectangle(-1, 2, 3, 4, 10)
        assert "width must be > 0" in str(VE.value)

    def test_negative_height(self):
        """ Test negative `height` """
        with pytest.raises(ValueError) as VE:
            new = Rectangle(1, -2, 3, 4, 10)
        assert "height must be > 0" in str(VE.value)

    def test_negative_x(self):
        """ Test negative `x` """
        with pytest.raises(ValueError) as VE:
            new = Rectangle(1, 2, -3, 4, 10)
        assert "x must be >= 0" in str(VE.value)

    def test_negative_y(self):
        """ Test negative `y` """
        with pytest.raises(ValueError) as VE:
            new = Rectangle(1, 2, 3, -4, 10)
        assert "y must be >= 0" in str(VE.value)

    def test_non_int_width(self):
        """ Test non-int `width` """
        with pytest.raises(TypeError) as TE:
            new = Rectangle("1", 2, 3, 4, 10)
        assert "width must be an integer" in str(TE.value)

    def test_non_int_height(self):
        """ Test non-int `height` """
        with pytest.raises(TypeError) as TE:
            new = Rectangle(1, "2", 3, 4, 10)
        assert "height must be an integer" in str(TE.value)

    def test_non_int_x(self):
        """ Test non-int `x` """
        with pytest.raises(TypeError) as TE:
            new = Rectangle(1, 2, "3", 4, 10)  # type: ignore
        assert "x must be an integer" in str(TE.value)

    def test_non_int_y(self):
        """ Test non-int `y` """
        with pytest.raises(TypeError) as TE:
            new = Rectangle(1, 2, 3, "4", 10)  # type: ignore
        assert "y must be an integer" in str(TE.value)

class TestRectangleMethods():
    """ Test `Rectangle` methods """
    def test_if_area(self):
        """ Assert `Rectangle` has `Area` """
        assert hasattr(Rectangle, "area")
    def test_area_doc(self):
        """ Assert documentation """
        assert hasattr(Rectangle.area, "__doc__")
    def test_area(self):
        """ Test `Area` """
        assert Rectangle(10, 2, id=10).area() == 20
    def test_if_str_(self):
        """ Assert `Rectangle` has __str__ """
        assert hasattr(Rectangle, "__str__")
    def test_str_doc(self):
        """ Assert __str__ has documentation """
        assert hasattr(Rectangle.__str__, "__doc__")
    def test_str(self):
        """ Test `__str__` """
        new = Rectangle(4, 6, 2, 1, 12)
        assert new.__str__() == "[Rectangle] (12) 2/1 - 4/6"
        new1 = Rectangle(5, 5, 1, id=1)
        assert new1.__str__() == "[Rectangle] (1) 1/0 - 5/5"
    def test_if_update(self):
        """ Assert `Update` """
        assert hasattr(Rectangle, "update")
    def test_update_doc(self):
        """ Assert `update` documentation """
        assert hasattr(Rectangle.update, "__doc__")
    def test_update(self):
        """ Test `update` #0 """
        new = Rectangle(10, 10, 10, 10, 10)
        assert new.__str__() == "[Rectangle] (10) 10/10 - 10/10"
        new.update(89)
        assert new.__str__() == "[Rectangle] (89) 10/10 - 10/10"
        new.update(89, 2)
        assert  new.__str__() == "[Rectangle] (89) 10/10 - 2/10"
        new.update(89, 2, 3)
        assert new.__str__() == "[Rectangle] (89) 10/10 - 2/3"
        new.update(89, 2, 3, 4)
        assert new.__str__() == "[Rectangle] (89) 4/10 - 2/3"
        new.update(89, 2, 3, 4, 5)
        assert new.__str__() == "[Rectangle] (89) 4/5 - 2/3"