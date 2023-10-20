from pytest import approx
from math import sqrt
from r2point import R2Point
from convex import Figure, Void, Point, Segment, Polygon


class TestVoid:

    
    def setup_method(self):
        self.f = Void()

    
    def test_figure(self):
        assert isinstance(self.f, Figure)

    
    def test_void(self):
        assert isinstance(self.f, Void)

    
    def test_perimeter(self):
        assert self.f.perimeter() == 0.0

    
    def test_аrea(self):
        assert self.f.area() == 0.0

    
    def test_add(self):
        assert isinstance(self.f.add(R2Point(0.0, 0.0)), Point)


class TestPoint:

    
    def setup_method(self):
        self.f = Point(R2Point(0.0, 0.0))

    
    def test_figure(self):
        assert isinstance(self.f, Figure)

    
    def test_point(self):
        assert isinstance(self.f, Point)

    
    def test_perimeter(self):
        assert self.f.perimeter() == 0.0

    
    def test_аrea(self):
        assert self.f.area() == 0.0

    
    def test_add1(self):
        assert self.f.add(R2Point(0.0, 0.0)) is self.f

    
    def test_add2(self):
        assert isinstance(self.f.add(R2Point(1.0, 0.0)), Segment)


class TestSegment:

    
    def setup_method(self):
        self.f = Segment(R2Point(0.0, 0.0), R2Point(1.0, 0.0))

    
    def test_figure(self):
        assert isinstance(self.f, Figure)

    
    def test_segment(self):
        assert isinstance(self.f, Segment)

    
    def test_perimeter(self):
        assert self.f.perimeter() == approx(2.0)

    
    def test_аrea(self):
        assert self.f.area() == 0.0

    
    def test_add1(self):
        assert self.f.add(R2Point(0.5, 0.0)) is self.f

    
    def test_add2(self):
        assert isinstance(self.f.add(R2Point(2.0, 0.0)), Segment)

    
    def test_add2(self):
        assert isinstance(self.f.add(R2Point(0.0, 1.0)), Polygon)


class TestPolygon:

    
    def setup_method(self):
        self.f = Polygon(
            R2Point(
                0.0, 0.0), R2Point(
                1.0, 0.0), R2Point(
                0.0, 1.0))

    
    def test_figure(self):
        assert isinstance(self.f, Figure)

    
    def test_polygon(self):
        assert isinstance(self.f, Polygon)

    
    
    def test_vertexes1(self):
        assert self.f.points.size() == 3
    

    def test_vertexes2(self):
        assert self.f.add(R2Point(0.1, 0.1)).points.size() == 3
    

    def test_vertexes3(self):
        assert self.f.add(R2Point(1.0, 1.0)).points.size() == 4
    

    def test_vertexes4(self):
        assert self.f.add(
            R2Point(
                0.4,
                1.0)).add(
            R2Point(
                1.0,
                0.4)).add(
                    R2Point(
                        0.8,
                        0.9)).add(
                            R2Point(
                                0.9,
                                0.8)).points.size() == 7
        assert self.f.add(R2Point(2.0, 2.0)).points.size() == 4

    
    
    def test_perimeter1(self):
        assert self.f.perimeter() == approx(2.0 + sqrt(2.0))
    

    def test_perimeter2(self):
        assert self.f.add(R2Point(1.0, 1.0)).perimeter() == approx(4.0)

    
    
    def test_аrea1(self):
        assert self.f.area() == approx(0.5)
    

    def test_area2(self):
        assert self.f.add(R2Point(1.0, 1.0)).area() == approx(1.0)
