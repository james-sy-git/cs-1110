"""
Unit Test for Assignment A3

This module shows off what a good unit test for a3 should look like.

James Sy (jcs547)
6 October 2021
"""
import introcs
import a3


def test_complement():
    """
    Test function complement
    """
    print('Testing complement')

    # One test is really good enough here
    comp = a3.complement_rgb(introcs.RGB(250, 0, 71))
    introcs.assert_equals(255-250, comp.red)
    introcs.assert_equals(255-0,   comp.green)
    introcs.assert_equals(255-71,  comp.blue)

    # One more for good measure
    comp = a3.complement_rgb(introcs.RGB(128, 64, 255))
    introcs.assert_equals(255-128, comp.red)
    introcs.assert_equals(255-64,  comp.green)
    introcs.assert_equals(255-255, comp.blue)


def test_str5():
    """
    Test function str5
    """
    print('Testing str5')
    introcs.assert_equals('130.6',  a3.str5(130.59))
    introcs.assert_equals('130.5',  a3.str5(130.54))
    introcs.assert_equals('100.0',  a3.str5(100))
    introcs.assert_equals('100.6',  a3.str5(100.56))
    introcs.assert_equals('99.57',  a3.str5(99.566))
    introcs.assert_equals('99.99',  a3.str5(99.99))
    introcs.assert_equals('100.0',  a3.str5(99.995))
    introcs.assert_equals('22.00',  a3.str5(21.99575))
    introcs.assert_equals('21.99',  a3.str5(21.994))
    introcs.assert_equals('10.01',  a3.str5(10.013567))
    introcs.assert_equals('10.00',  a3.str5(10.000000005))
    introcs.assert_equals('10.00',  a3.str5(9.9999))
    introcs.assert_equals('9.999',  a3.str5(9.9993))
    introcs.assert_equals('1.355',  a3.str5(1.3546))
    introcs.assert_equals('1.354',  a3.str5(1.3544))
    introcs.assert_equals('0.046',  a3.str5(.0456))
    introcs.assert_equals('0.045',  a3.str5(.0453))
    introcs.assert_equals('0.006',  a3.str5(.0056))
    introcs.assert_equals('0.001',  a3.str5(.0013))
    introcs.assert_equals('0.000',  a3.str5(.0004))
    introcs.assert_equals('0.001',  a3.str5(.0009999))
    introcs.assert_equals('1.000',  a3.str5(1))
    introcs.assert_equals('0.000',  a3.str5(0.0000000001))


def test_str5_color():
    """
    Test the str5 functions for cmyk and hsv.
    """
    print('Testing str5_cmyk and str5_hsl')

    # Tests for str5_cmyk
    text = a3.str5_cmyk(introcs.CMYK(98.448, 25.362, 72.8, 1.0))
    introcs.assert_equals('(98.45, 25.36, 72.80, 1.000)',text)

    text = a3.str5_cmyk(introcs.CMYK(0.0, 1.5273, 100.0, 57.846))
    introcs.assert_equals('(0.000, 1.527, 100.0, 57.85)',text)

    text = a3.str5_cmyk(introcs.CMYK(0.0004, 29.9999, 9.999999, .00000005))
    introcs.assert_equals('(0.000, 30.00, 10.00, 0.000)',text)

    # max case
    text = a3.str5_hsl(introcs.HSL(359.9999999, 0.99999, 0.99999))
    introcs.assert_equals('(359.9, 1.000, 1.000)', text)

    # in-betweeen
    text = a3.str5_hsl(introcs.HSL(23.559, 0.1236, 0.1234))
    introcs.assert_equals('(23.56, 0.124, 0.123)', text)

    # min case
    text = a3.str5_hsl(introcs.HSL(0.00000000, 0.000, 0.0))
    introcs.assert_equals('(0.000, 0.000, 0.000)', text)


def test_rgb_to_cmyk():
    """
    Test translation function rgb_to_cmyk
    """
    print('Testing rgb_to_cmyk')

    # max case
    rgb = introcs.RGB(255, 255, 255);
    cmyk = a3.rgb_to_cmyk(rgb);
    introcs.assert_equals(0.0, round(cmyk.cyan,3))
    introcs.assert_equals(0.0, round(cmyk.magenta,3))
    introcs.assert_equals(0.0, round(cmyk.yellow,3))
    introcs.assert_equals(0.0, round(cmyk.black,3))

    # min case
    rgb = introcs.RGB(0, 0, 0);
    cmyk = a3.rgb_to_cmyk(rgb);
    introcs.assert_equals(0.0, round(cmyk.cyan,3))
    introcs.assert_equals(0.0, round(cmyk.magenta,3))
    introcs.assert_equals(0.0, round(cmyk.yellow,3))
    introcs.assert_equals(100.0, round(cmyk.black,3))

    # in between
    rgb = introcs.RGB(217, 43, 164);
    cmyk = a3.rgb_to_cmyk(rgb);
    introcs.assert_equals(0.0, round(cmyk.cyan,3))
    introcs.assert_equals(80.184, round(cmyk.magenta,3))
    introcs.assert_equals(24.424, round(cmyk.yellow,3))
    introcs.assert_equals(14.902, round(cmyk.black,3))


def test_cmyk_to_rgb():
    """
    Test translation function cmyk_to_rgb
    """
    print('Testing cmyk_to_rgb')

    # Tests for cmyk_to_rgb
    cmyk = introcs.CMYK(34.783, 0.00000005, 100.0, 9.8040000004);
    rgb = a3.cmyk_to_rgb(cmyk);
    introcs.assert_equals(150, rgb.red)
    introcs.assert_equals(230, rgb.green)
    introcs.assert_equals(0, rgb.blue)

    # maximum case
    cmyk = introcs.CMYK(100.0, 100.0, 100.0, 100.0);
    rgb = a3.cmyk_to_rgb(cmyk);
    introcs.assert_equals(0, rgb.red)
    introcs.assert_equals(0, rgb.green)
    introcs.assert_equals(0, rgb.blue)

    # rounding up and rounding down
    cmyk = introcs.CMYK(29.996, 29.994, 12.33513, 0.9);
    rgb = a3.cmyk_to_rgb(cmyk);
    introcs.assert_equals(177, rgb.red)
    introcs.assert_equals(177, rgb.green)
    introcs.assert_equals(222, rgb.blue)

    # additional case
    cmyk = introcs.CMYK(42.0, 14.67, 1.1, 9.9999);
    rgb = a3.cmyk_to_rgb(cmyk);
    introcs.assert_equals(133, rgb.red)
    introcs.assert_equals(196, rgb.green)
    introcs.assert_equals(227, rgb.blue)

    # minimum case
    cmyk = introcs.CMYK(0.0, 0.00, 0.000, 0.0000000);
    rgb = a3.cmyk_to_rgb(cmyk);
    introcs.assert_equals(255, rgb.red)
    introcs.assert_equals(255, rgb.green)
    introcs.assert_equals(255, rgb.blue)


def test_rgb_to_hsl():
    """
    Test translation function rgb_to_hsv
    """
    print('Testing rgb_to_hsl')

    # Tests for rgb_to_hsl
    # max == min and (max + min)/2 == 0
    rgb = introcs.RGB(0, 0, 0);
    hsl = a3.rgb_to_hsl(rgb);
    introcs.assert_equals(0.0, hsl.hue)
    introcs.assert_equals(0.0, hsl.saturation)
    introcs.assert_equals(0.0, hsl.lightness)

    # max == r and g >= b
    rgb = introcs.RGB(241, 123, 10);
    hsl = a3.rgb_to_hsl(rgb);
    introcs.assert_equals(29.351, round(hsl.hue, 3))
    introcs.assert_equals(0.92, round(hsl.saturation,3))
    introcs.assert_equals(0.492, round(hsl.lightness,3))

    # max == r and g < b
    rgb = introcs.RGB(241, 37, 44);
    hsl = a3.rgb_to_hsl(rgb);
    introcs.assert_equals(357.941, round(hsl.hue, 3))
    introcs.assert_equals(0.879, round(hsl.saturation,3))
    introcs.assert_equals(0.545, round(hsl.lightness,3))

    # max == g
    rgb = introcs.RGB(12, 144, 0);
    hsl = a3.rgb_to_hsl(rgb);
    introcs.assert_equals(115.0, round(hsl.hue, 3))
    introcs.assert_equals(1.0, round(hsl.saturation,3))
    introcs.assert_equals(0.282, round(hsl.lightness,3))

    # max == b
    rgb = introcs.RGB(89, 90, 91);
    hsl = a3.rgb_to_hsl(rgb);
    introcs.assert_equals(210.0, round(hsl.hue, 3))
    introcs.assert_equals(0.011, round(hsl.saturation,3))
    introcs.assert_equals(0.353, round(hsl.lightness,3))

    # (max + min)/2 == 1
    rgb = introcs.RGB(1, 1, 1);
    hsl = a3.rgb_to_hsl(rgb);
    introcs.assert_equals(0.0, round(hsl.hue, 3))
    introcs.assert_equals(0.0, round(hsl.saturation,3))
    introcs.assert_equals(0.004, round(hsl.lightness,3))


def test_hsl_to_rgb():
    """
    Test translation function hsv_to_rgb
    """
    print('Testing hsl_to_rgb')

    # let H = math.floor(hsl.hue/60)

    # max case
    hsl = introcs.HSL(359.999, 1.000, 1.000);
    rgb = a3.hsl_to_rgb(hsl);
    introcs.assert_equals(255, rgb.red)
    introcs.assert_equals(255, rgb.green)
    introcs.assert_equals(255, rgb.blue)

    # min case
    hsl = introcs.HSL(0.0, 0.0, 0.0);
    rgb = a3.hsl_to_rgb(hsl);
    introcs.assert_equals(0, rgb.red)
    introcs.assert_equals(0, rgb.green)
    introcs.assert_equals(0, rgb.blue)

    # H == 0
    hsl = introcs.HSL(59.032, 0.9923, 0.1224);
    rgb = a3.hsl_to_rgb(hsl);
    introcs.assert_equals(62, rgb.red)
    introcs.assert_equals(61, rgb.green)
    introcs.assert_equals(0, rgb.blue)

    # H == 1
    hsl = introcs.HSL(64.992, 0.8743, 0.2642);
    rgb = a3.hsl_to_rgb(hsl);
    introcs.assert_equals(116, rgb.red)
    introcs.assert_equals(126, rgb.green)
    introcs.assert_equals(8, rgb.blue)

    # H == 2
    hsl = introcs.HSL(167.983, 0.129, 0.198);
    rgb = a3.hsl_to_rgb(hsl);
    introcs.assert_equals(44, rgb.red)
    introcs.assert_equals(57, rgb.green)
    introcs.assert_equals(54, rgb.blue)

    # H == 3
    hsl = introcs.HSL(220.3, 0.711, 0.800);
    rgb = a3.hsl_to_rgb(hsl);
    introcs.assert_equals(168, rgb.red)
    introcs.assert_equals(192, rgb.green)
    introcs.assert_equals(240, rgb.blue)

    # H == 4
    hsl = introcs.HSL(277.332, 0.66321, 0.66321);
    rgb = a3.hsl_to_rgb(hsl);
    introcs.assert_equals(183, rgb.red)
    introcs.assert_equals(112, rgb.green)
    introcs.assert_equals(226, rgb.blue)

    # H == 5 : "else"
    hsl = introcs.HSL(324.234975293874, 0.8569237498, 0.882348732);
    rgb = a3.hsl_to_rgb(hsl);
    introcs.assert_equals(251, rgb.red)
    introcs.assert_equals(199, rgb.green)
    introcs.assert_equals(230, rgb.blue)


def test_contrast_value():
    """
    Test translation function contrast_value
    """
    print('Testing contrast_value')

    # contrast == -1.0 (extreme)
    result = a3.contrast_value(0.0,-1.0)
    introcs.assert_floats_equal(0.5,result)

    result = a3.contrast_value(1.0,-1.0)
    introcs.assert_floats_equal(0.5,result)

    # contrast < 0, bottom part of sawtooth
    result = a3.contrast_value(0.1,-0.5)
    introcs.assert_floats_equal(0.3,result)

    # contrast < 0, middle of sawtooth
    result = a3.contrast_value(0.4,-0.4)
    introcs.assert_floats_equal(0.4571429,result)

    # contrast < 0, upper part of sawtooth
    result = a3.contrast_value(0.9,-0.3)
    introcs.assert_floats_equal(0.8142857,result)

    # contrast == 0.0, bottom part of sawtooth
    result = a3.contrast_value(0.1,0.0)
    introcs.assert_floats_equal(0.1,result)

    # contrast == 0, middle of sawtooth
    result = a3.contrast_value(0.6,0.0)
    introcs.assert_floats_equal(0.6,result)

    # contrast == 0.0, upper part of sawtooth
    result = a3.contrast_value(0.9,0.0)
    introcs.assert_floats_equal(0.9,result)

    # contrast > 0, bottom part of sawtooth
    result = a3.contrast_value(0.1,0.3)
    introcs.assert_floats_equal(0.05384615,result)

    # contrast > 0, middle of sawtooth
    result = a3.contrast_value(0.4,0.5)
    introcs.assert_floats_equal(0.2,result)

    # contrast > 0, upper part of sawtooth
    result = a3.contrast_value(0.9,0.4)
    introcs.assert_floats_equal(0.95714286,result)

    # contrast == 1.0 (extreme)
    result = a3.contrast_value(0.2,1.0)
    introcs.assert_floats_equal(0.0,result)

    result = a3.contrast_value(0.6,1.0)
    introcs.assert_floats_equal(1.0,result)


def test_contrast_rgb():
    """
    Test translation function contrast_value
    """
    print('Testing contrast_rgb')

    # negative contrast
    rgb = introcs.RGB(240, 15, 118)
    hsv = a3.contrast_rgb(rgb,-0.4)
    introcs.assert_equals(220, rgb.red)
    introcs.assert_equals(35,  rgb.green)
    introcs.assert_equals(123, rgb.blue)

    # positive contrast
    rgb = introcs.RGB(240, 15, 118)
    hsv = a3.contrast_rgb(rgb, 0.61)
    introcs.assert_equals(251, rgb.red)
    introcs.assert_equals(4,  rgb.green)
    introcs.assert_equals(88, rgb.blue)

    # zero contrast
    rgb = introcs.RGB(240, 15, 118)
    hsv = a3.contrast_rgb(rgb, 0.0)
    introcs.assert_equals(240, rgb.red)
    introcs.assert_equals(15,  rgb.green)
    introcs.assert_equals(118, rgb.blue)


# Script Code (Prevents tests running on import)
if __name__ == "__main__":
    test_complement()
    test_str5()
    test_str5_color()
    test_rgb_to_cmyk()
    test_cmyk_to_rgb()
    test_rgb_to_hsl()
    test_hsl_to_rgb()
    test_contrast_value()
    test_contrast_rgb()
    print('Module a3 passed all tests.')
