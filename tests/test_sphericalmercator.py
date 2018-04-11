import pytest

from sphericalmercator import SphericalMercator


@pytest.mark.parametrize("x,y,z,expected", [
    (10475, 25327, 16, (-122.4591064453125, 37.78808138412046, -122.45361328125, 37.792422407988575)),
    (9903, 5123, 14, (37.59521484375, 55.727110085045986, 37.6171875, 55.73948169869349)),
    (5521, 9867, 14, (-58.68896484375, -34.52466147177172, -58.6669921875, -34.50655662164559)),
    (60299, 39341, 16, (151.2322998046875, -33.934245311173115, 151.23779296875, -33.92968762757659)),
])
def test_xyz_to_envelope__returns_expected(x, y, z, expected):
    merc = SphericalMercator()

    assert merc.xyz_to_envelope(x, y, z) == expected


@pytest.mark.parametrize("minx,miny,maxx,maxy,zoom,expected", [
    (-122.4591, 37.7880, -122.4536, 37.7924, 16, [(10475, 25327), (10475, 25328), (10476, 25327), (10476, 25328)]),
    (179.99, 35, -179.99, 35, 16, [(0, 25958), (1, 25958), (65534, 25958), (65535, 25958)]),
])
def test_bbox_to_tiles__returns_expected(minx, miny, maxx, maxy, zoom, expected):
    merc = SphericalMercator()

    assert list(merc.bbox_to_tiles(minx, miny, maxx, maxy, zoom)) == expected
