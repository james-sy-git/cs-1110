"""
Functions for Assignment A3

This file contains the functions for Assignment 3

James Sy (jcs547)
5 October 2021
"""
import introcs
import math


def complement_rgb(rgb):
    """
    Returns the complement of color rgb.

    Parameter rgb: the color to complement
    Precondition: rgb is an RGB object
    """
    return introcs.RGB(255-(rgb.red), 255-(rgb.green), 255-(rgb.blue))


def str5(value):
    """
    Returns value as a string, but expanded or rounded to be exactly 5 characters.

    The decimal point counts as one of the five characters.

    Examples:
        str5(1.3546)  is  '1.355'.
        str5(21.9954) is  '22.00'.
        str5(21.994)  is  '21.99'.
        str5(130.59)  is  '130.6'.
        str5(130.54)  is  '130.5'.
        str5(1)       is  '1.000'.

    Parameter value: the number to conver to a 5 character string.
    Precondition: value is a number (int or float), 0 <= value <= 360.
    """
    value_as_string = str(value)

    count = len(value_as_string)

    num_to_add = 5-count

    if count < 5:
        if type(value) == int:
            if num_to_add == 4:
                ret_val = value_as_string + '.000'
            elif num_to_add == 3:
                ret_val = value_as_string + '.00'
            elif num_to_add == 2:
                ret_val = value_as_string + '.0'

        if type(value) == float:
            if num_to_add == 2:
                ret_val = value_as_string + '00'
            elif num_to_add == 1:
                ret_val = value_as_string + '0'

    if count > 5 or count == 5:
        find_decimal = value_as_string.find('.')
        before_decimal = value_as_string[0:find_decimal]
        length_before_decimal = len(before_decimal)

        if find_decimal == -1:
            ret_val = '0.000'

        if length_before_decimal == 2:
            round_to_2 = round(value, 2)
            ret_val = str(round_to_2)

            test_if_zero = str(round_to_2)

            find_last_digit = test_if_zero[len(test_if_zero)-1:len(test_if_zero)]

            if find_last_digit == '0':
                if len(str(round_to_2)) == 5:
                    ret_val = str(round_to_2)
                else:
                    ret_val = str(round_to_2) + '0'

        elif length_before_decimal == 1:
            round_to_3 = round(value, 3)
            ret_val = str(round_to_3)

            test_if_zero = str(round_to_3)

            find_last_digit = test_if_zero[len(test_if_zero)-1:len(test_if_zero)]

            if find_last_digit == '0':
                if len(str(round_to_3)) == 3:
                    ret_val = str(round_to_3) + '00'
                else:
                    ret_val = str(round_to_3) + '0'

        elif length_before_decimal == 3:
            round_to_1 = round(value, 1)
            ret_val = str(round_to_1)

    return ret_val


def str5_cmyk(cmyk):
    """
    Returns the string representation of cmyk in the form "(C, M, Y, K)".

    In the output, each of C, M, Y, and K should be exactly 5 characters long.
    Hence the output of this function is not the same as str(cmyk)

    Example: if str(cmyk) is

          '(0.0,31.3725490196,31.3725490196,0.0)'

    then str5_cmyk(cmyk) is '(0.000, 31.37, 31.37, 0.000)'. Note the spaces after
    the commas. These must be there.

    Parameter cmyk: the color to convert to a string
    Precondition: cmyk is an CMYK object.
    """
    c_0 = cmyk.cyan

    m_0 = cmyk.magenta

    y_0 = cmyk.yellow

    k_0 = cmyk.black

    c = str5(c_0)

    m = str5(m_0)

    y = str5(y_0)

    k = str5(k_0)

    return '(' + c + ', ' + m + ', ' + y + ', ' + k + ')'


def str5_hsl(hsl):
    """
    Returns the string representation of hsl in the form "(H, S, L)".

    In the output, each of H, S, and L should be exactly 5 characters long.
    Hence the output of this function is not the same as str(hsv)

    Example: if str(hsl) is

          '(0.0,0.313725490196,0.5)'

    then str5_hsv(hsl) is '(0.000, 0.314, 0.500)'. Note the spaces after the
    commas. These must be there.

    Parameter hsl: the color to convert to a string
    Precondition: hsl is an HSL object.
    """
    h_0 = hsl.hue

    s_0 = hsl.saturation

    l_0 = hsl.lightness

    if str5(h_0) == '360.0':
        h = '359.9'
    else:
        h = str5(h_0)

    s = str5(s_0)

    l = str5(l_0)

    return '(' + h + ', ' + s + ', ' + l + ')'


def rgb_to_cmyk(rgb):
    """
    Returns a CMYK object equivalent to rgb, with the most black possible.

    Formulae from https://www.rapidtables.com/convert/color/rgb-to-cmyk.html

    Parameter rgb: the color to convert to a CMYK object
    Precondition: rgb is an RGB object
    """
    r_1 = rgb.red/255.0

    g_1 = rgb.green/255.0

    b_1 = rgb.blue/255.0

    k_1 = 1 - max(r_1, g_1, b_1)

    if k_1 == 1:
        c = 0
        m = 0
        y = 0
        k = 100.0

    else:

        c_1 = (1 - r_1 - k_1)/(1-k_1)

        m_1 = (1 - g_1 - k_1)/(1-k_1)

        y_1 = (1 - b_1 - k_1)/(1-k_1)

        c = (c_1)*100

        m = (m_1)*100

        y = (y_1)*100

        k = (k_1)*100

    return introcs.CMYK(c,m,y,k)


def cmyk_to_rgb(cmyk):
    """
    Returns an RGB object equivalent to cmyk

    Formulae from https://www.rapidtables.com/convert/color/cmyk-to-rgb.html

    Parameter cmyk: the color to convert to a RGB object
    Precondition: cmyk is an CMYK object.
    """
    c_1 = cmyk.cyan/100.0

    m_1 = cmyk.magenta/100.0

    y_1 = cmyk.yellow/100.0

    k_1 = cmyk.black/100.0

    r = (1-c_1) * (1-k_1)

    g = (1-m_1) * (1-k_1)

    b = (1-y_1) * (1-k_1)

    return introcs.RGB(round(255.0 * r),round(255.0 * g),round(255.0 * b))


def rgb_to_hsl(rgb):
    """
    Return an HSL object equivalent to rgb

    Formulae from https://en.wikipedia.org/wiki/HSL_and_HSV

    Parameter rgb: the color to convert to a HSL object
    Precondition: rgb is an RGB object
    """
    r = rgb.red/255.0

    g = rgb.green/255.0

    b = rgb.blue/255.0

    max_rgb = max(r,g,b)

    min_rgb = min(r,g,b)

    if max_rgb == min_rgb:
        hval = 0
    elif max_rgb == r and g >= b:
        hval = 60.0 * ((g-b)/(max_rgb-min_rgb))
    elif max_rgb == r and g < b:
        hval = 60.0 * ((g-b)/(max_rgb-min_rgb)) + 360.0
    elif max_rgb == g:
        hval = 60.0 * ((b-r)/(max_rgb-min_rgb)) + 120.0
    elif max_rgb == b:
        hval = 60.0 * ((r-g)/(max_rgb-min_rgb)) + 240.0

    lval = (max_rgb+min_rgb)/2

    if lval == 0 or lval == 1:
        sval = 0
    else:
        sval = (max_rgb-lval)/min(lval,1-lval)

    return introcs.HSL(hval,sval,lval)


def hsl_to_rgb(hsl):
    """
    Returns an RGB object equivalent to hsl

    Formulae from https://en.wikipedia.org/wiki/HSL_and_HSV

    Parameter hsl: the color to convert to a RGB object
    Precondition: hsl is an HSL object.
    """
    hue = hsl.hue

    sat = hsl.saturation

    light = hsl.lightness

    h_1 = math.floor(hue/60.0)

    f = (hue/60.0)-h_1

    c = min(light,(1-light)) * sat

    p = light + c

    q = light - c

    u = light - (1-(2*f))*c

    v = light + (1-(2*f))*c

    if h_1 == 0:
        rval = p
        gval = u
        bval = q
    elif h_1 == 1:
        rval = v
        gval = p
        bval = q
    elif h_1 == 2:
        rval = q
        gval = p
        bval = u
    elif h_1 == 3:
        rval = q
        gval = v
        bval = p
    elif h_1 == 4:
        rval = u
        gval = q
        bval = p
    else: # h_1 == 5
        rval = p
        gval = q
        bval = v

    r_0 = rval * 255.0

    g_0 = gval * 255.0

    b_0 = bval * 255.0

    r = abs(r_0)
    g = abs(g_0)
    b = abs(b_0)

    return introcs.RGB(round(r),round(g),round(b))


def contrast_value(value,contrast):
    """
    Returns value adjusted to the "sawtooth curve" for the given contrast

    At contrast = 0, the curve is the normal line y = x, so value is unaffected.
    If contrast < 0, values are pulled closer together, with all values collapsing
    to 0.5 when contrast = -1.  If contrast > 0, values are pulled farther apart,
    with all values becoming 0 or 1 when contrast = 1.

    Parameter value: the value to adjust
    Precondition: value is a float in 0..1

    Parameter contrast: the contrast amount (0 is no contrast)
    Precondition: contrast is a float in -1..1
    """
    c = contrast

    if value < 0.25 + (0.25 * c):
        adj_val = ((1-c)/(1+c)) * value
    elif value > 0.75 - (0.25 * c):
        adj_val = ((1-c)/(1+c)) * (value - (3-c)/4) + (3+c)/4
    else:
        adj_val = ((1+c)/(1-c)) * (value - (1+c)/4) + (1-c)/4

    return adj_val


def contrast_rgb(rgb,contrast):
    """
    Applies the given contrast to the RGB object rgb

    This function is a PROCEDURE.  It modifies rgb and has no return value.  It
    should apply contrast_value to the red, blue, and green values.

    Parameter rgb: the color to adjust
    Precondition: rgb is an RGB object

    Parameter contrast: the contrast amount (0 is no contrast)
    Precondition: contrast is a float in -1..1
    """
    r_0 = (rgb.red)/255.0

    g_0 = (rgb.green)/255.0

    b_0 = (rgb.blue)/255.0

    r_1 = contrast_value(r_0, contrast)

    g_1 = contrast_value(g_0, contrast)

    b_1 = contrast_value(b_0, contrast)

    rgb.red = round((r_1) * 255.0)

    rgb.green = round((g_1) * 255.0)

    rgb.blue = round((b_1) * 255.0)
