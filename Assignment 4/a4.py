"""
A module to draw cool shapes with the introcs Turtle.

You call all of these functions in the interactive shell, but you will have
to create a Window first.  Alternatively, you can use the a4test.py test script
to try out the functions.

James Sy (jcs547)
10/28/21
"""
from introcs.turtle import Window, Turtle, Pen
import introcs  # For the RGB and HSV objects
import math     # For the math computations


################# Helpers for Precondition Verification #################

def is_number(x):
    """
    Returns: True if value x is a number; False otherwise.

    Parameter x: the value to check
    Precondition: NONE (x can be any value)
    """
    return type(x) in [float, int]


def is_window(w):
    """
    Returns: True if w is a introcs Window; False otherwise.

    Parameter w: the value to check
    Precondition: NONE (w can be any value)
    """
    return type(w) == Window


def is_valid_color(c):
    """
    Returns: True c is a valid turtle color; False otherwise

    Parameter c: the value to check
    Precondition: NONE (c can be any value)
    """
    return (type(c) == introcs.RGB or type(c) == introcs.HSV or
            (type(c) == str and (introcs.is_tkcolor(c) or introcs.is_webcolor(c))))


def is_valid_speed(sp):
    """
    Returns: True if sp is an int in range 0..10; False otherwise.

    Parameter sp: the value to check
    Precondition: NONE (sp can be any value)
    """
    return (type(sp) == int and 0 <= sp and sp <= 10)


def is_valid_length(side):
    """
    Returns: True if side is a number >= 0; False otherwise.

    Parameter side: the value to check
    Precondition: NONE (side can be any value)
    """
    return (is_number(side) and 0 <= side)


def is_valid_iteration(n):
    """
    Returns: True if n is an int >= 1; False otherwise.

    Parameter n: the value to check
    Precondition: NONE (n can be any value)
    """
    return (type(n) == int and 1 <= n)


def is_valid_depth(d):
    """
    Returns: True if d is an int >= 0; False otherwise.

    Parameter d: the value to check
    Precondition: NONE (d can be any value)
    """
    return (type(d) == int and d >= 0)


def is_valid_turtlemode(t):
    """
    Returns: True t is a Turtle with drawmode True; False otherwise.

    Parameter t: the value to check
    Precondition: NONE (t can be any value)
    """
    return (type(t) == Turtle and t.drawmode)


def is_valid_penmode(p):
    """
    Returns: True t is a Pen with solid False; False otherwise.

    Parameter p: the value to check
    Precondition: NONE (p can be any value)
    """
    return (type(p) == Pen and not p.solid)


def report_error(message, value):
    """
    Returns: An error message about the given value.

    This is a function for constructing error messages to be used in assert
    statements. We find that students often introduce bugs into their assert
    statement messages, and do not find them because they are in the habit of
    not writing tests that violate preconditions.

    The purpose of this function is to give you an easy way of making error
    messages without having to worry about introducing such bugs. Look at
    the function draw_two_lines for the proper way to use it.

    Parameter message: The error message to display
    Precondition: message is a string

    Parameter value: The value that caused the error
    Precondition: NONE (value can be anything)
    """
    return message+': '+repr(value)


#################### DEMO: Two lines ####################

def draw_two_lines(w,sp):
    """
    Draws two lines on to window w.

    This function clears w of any previous drawings. Then, in the middle of
    the window w, this function draws a green line 100 pixels to the east,
    and then a blue line 200 pixels to the north. It uses a new turtle that
    moves at speed sp, 0 <= sp <= 10, with 1 being slowest and 10 fastest
    (and 0 being "instant").

    REMEMBER: You need to flush the turtle if the speed is 0.

    This procedure asserts all preconditions.

    Parameter w: The window to draw upon.
    Precondition: w is a introcs Window object.

    Parameter sp: The turtle speed.
    Precondition: sp is a valid turtle speed.
    """
    # Assert the preconditions
    assert is_window(w), report_error('w is not a valid window',w)
    assert is_valid_speed(sp), report_error('sp is not a valid speed',sp)

    # Clear the window first!
    w.clear()

    # Create a turtle and draw
    t = Turtle(w)
    t.speed = sp
    t.color = 'green'
    t.forward(100) # draw a line 100 pixels in the current direction
    t.left(90)     # add 90 degrees to the angle
    t.color = 'blue'
    t.forward(200)

    # This is necessary if speed is 0!
    t.flush()


#################### TASK 1: Triangle ####################

def draw_triangle(t, s, c):
    """
    Draws an equilateral triangle of side s and color c at current position.

    The direction of the triangle depends on the current facing of the turtle.
    If the turtle is facing west, the triangle points up and the turtle starts
    and ends at the east end of the base line.

    WHEN DONE, THE FOLLOWING TURTLE ATTRIBUTES ARE THE SAME AS IT STARTED:
    position (x and y, within round-off errors), heading, color, and drawmode.
    If you changed any of these in the function, you must change them back.

    REMEMBER: You need to flush the turtle if the speed is 0.

    This procedure asserts all preconditions.

    Parameter t: The drawing Turtle
    Precondition: t is a Turtle with drawmode True.

    Parameter s: The length of each triangle side
    Precondition: s is a valid side length (number >= 0)

    Parameter c: The triangle color
    Precondition: c is a valid turtle color (see the helper function above)
    """
    # Assert the preconditions
    assert is_valid_turtlemode(t), report_error('Invalid turtle mode', t)
    assert is_valid_length(s), report_error('Invalid side length', s)
    assert is_valid_color(c), report_error('Invalid color', c)

    head_0 = t.heading
    c_0 = t.color
    draw_0 = t.drawmode

    t.color = c

    for x in range(3):
        t.forward(s)
        t.left(120)

    t.heading = head_0
    t.color = c_0
    t.drawmode = draw_0

    t.flush()


#################### TASK 2: Hexagon ####################

def draw_hex(t, s):
    """
    Draws six triangles using the color 'cyan' to make a hexagon.

    The triangles are equilateral triangles, using draw_triangle as a helper.
    The drawing starts at the turtle's current position and heading. The
    middle of the hexagon is the turtle's starting position.

    WHEN DONE, THE FOLLOWING TURTLE ATTRIBUTES ARE THE SAME AS IT STARTED:
    position (x and y, within round-off errors), heading, color, and drawmode.
    If you changed any of these in the function, you must change them back.

    REMEMBER: You need to flush the turtle if the speed is 0.

    This procedure asserts all preconditions.

    Parameter t: The drawing Turtle
    Precondition: t is a Turtle with drawmode True.

    Parameter s: The length of each triangle side
    Precondition: s is a valid side length (number >= 0)
    """
    # Assert the preconditions
    assert is_valid_turtlemode(t), report_error('Invalid turtle mode', t)
    assert is_valid_length(s), report_error('Invalid side length', s)

    for x in range(6):
        draw_triangle(t, s, 'cyan')
        t.right(60)

    t.flush()


#################### Task 3A: Spirals ####################

def draw_spiral(w, side, ang, n, sp):
    """
    Draws a spiral using draw_spiral_helper(t, side, ang, n, sp)

    This function clears the window and makes a new turtle t.  This turtle
    starts in the middle of the canvas facing south (NOT the default east).
    It then calls draw_spiral_helper(t, side, ang, n, sp). When it is done,
    the turtle is left hidden (visible is False).

    REMEMBER: You need to flush the turtle if the speed is 0.

    This procedure asserts all preconditions.

    Parameter w: The window to draw upon.
    Precondition: w is a introcs Window object.

    Parameter side: The length of each spiral side
    Precondition: side is a valid side length (number >= 0)

    Parameter ang: The angle of each corner of the spiral
    Precondition: ang is a number

    Parameter n: The number of edges of the spiral
    Precondition: n is a valid number of iterations (int >= 1)

    Parameter sp: The turtle speed.
    Precondition: sp is a valid turtle speed.
    """

    assert is_window(w), report_error('w is invalid window',w)
    assert is_valid_length(side), report_error('side is invalid length',side)
    assert is_number(ang), report_error('ang is invalid angle',ang)
    assert is_valid_iteration(n), report_error('n is invalid number of iterations',n)
    assert is_valid_speed(sp), report_error('sp is invalid speed',sp)

    w.clear()
    t = Turtle(w)
    t.speed = sp
    t.heading = -90
    draw_spiral_helper(t, side, ang, n, sp)
    t.visible = False

    t.flush()


def draw_spiral_helper(t, side, ang, n, sp):
    """
    Draws a spiral of n lines at the current position and heading.

    The spiral begins at the current turtle position and heading, turning ang
    degrees to the left after each line. Line 0 is side pixels long. Line 1
    is 2*side pixels long, and so on.  Hence each Line i is (i+1)*side pixels
    long. The lines alternate between blue, magenta, and red, in that order,
    with the first one blue.

    WHEN DONE, THE FOLLOWING TURTLE ATTRIBUTES ARE THE SAME AS IT STARTED:
    color, speed, visible, and drawmode. However, the final position and
    heading may be different. If you changed any of these four in the
    function, you must change them back.

    This procedure asserts all preconditions.

    Parameter t: The drawing Turtle
    Precondition: t is a Turtle with drawmode True.

    Parameter side: The length of each spiral side
    Precondition: side is a valid side length (number >= 0)

    Parameter ang: The angle of each corner of the spiral
    Precondition: ang is a number

    Parameter n: The number of edges of the spiral
    Precondition: n is a valid number of iterations (int >= 1)

    Parameter sp: The turtle speed.
    Precondition: sp is a valid turtle speed.
    """
    # ARE THESE ALL OF THE PRECONDITIONS?
    assert is_valid_turtlemode(t), report_error('Invalid turtle mode', t)
    assert is_valid_length(side), report_error('side is invalid length',side)
    assert is_number(ang), report_error('ang is invalid angle', ang)
    assert is_valid_iteration(n), report_error('n is invalid number of iterations',n)
    assert is_valid_speed(sp), report_error('sp is invalid speed',sp)

    c_0 = t.color
    sp_0 = t.speed
    v_0 = t.visible
    draw_0 = t.drawmode

    colors = ['blue', 'magenta', 'red']

    for x in range(n):
        t.speed = sp
        if x > 3:
            t.color = colors[x % 3]
        elif 0 <= x <= 2:
            t.color = colors[x]
        elif x == 3:
            t.color = 'blue'
        t.forward((x+1)*side)
        t.left(ang)

    t.color = c_0
    t.speed = sp_0
    t.visible = v_0
    t.drawmode = draw_0


#################### TASK 3B: Polygons ####################

def multi_polygons(w, side, k, n, sp):
    """
    Draws polygons using multi_polygons_helper(t, side, k, n, sp)

    This function clears the window and makes a new turtle t. This turtle
    starts in the middle of the canvas facing north (NOT the default east).
    It then calls multi_polygons_helper(t, side, k, n, sp). When it is done,
    the turtle is left hidden (visible is False).

    REMEMBER: You need to flush the turtle if the speed is 0.

    This procedure asserts all preconditions.

    Parameter w: The window to draw upon.
    Precondition: w is a introcs Window object.

    Parameter side: The length of each polygon side
    Precondition: side is a valid side length (number >= 0)

    Parameter k: The number of polygons to draw
    Precondition: k is an int >= 1

    Parameter n: The number of sides of each polygon
    Precondition: n is an int >= 3

    Parameter sp: The turtle speed.
    Precondition: sp is a valid turtle speed.
    """
    # ARE THESE ALL OF THE PRECONDITIONS?
    assert is_window(w), report_error('w is invalid window',w)
    assert is_valid_length(side), report_error('side is invalid length',side)
    assert is_valid_iteration(k), report_error('k is invalid number of polygons',k)
    assert n >= 3 and type(n) == int, report_error('n is invalid number of sides',n)
    assert is_valid_speed(sp), report_error('sp is invalid speed',sp)

    w.clear()
    t = Turtle(w)
    t.speed = sp
    t.heading = 90
    multi_polygons_helper(t, side, k, n, sp)
    t.visible = False

    t.flush()


def multi_polygons_helper(t, side, k, n, sp):
    """
    Draws k n-sided polygons of side length s.

    The polygons are drawn by turtle t, starting at the current position. The
    turtles alternate colors between blue and orange (starting with blue).
    Each polygon is drawn starting at the same place (within roundoff errors),
    but t turns left 360.0/k degrees after each polygon.

    At the end, ALL ATTRIBUTES of the turtle are the same as they were in the
    beginning (within roundoff errors). If you change any attributes of the
    turtle. then you must restore them. Look at the helper draw_polygon for
    more information.

    This procedure asserts all preconditions.

    Parameter t: The drawing Turtle
    Precondition: t is a Turtle with drawmode True.

    Parameter side: The length of each polygon side
    Precondition: side is a valid side length (number >= 0)

    Parameter k: The number of polygons to draw
    Precondition: k is an int >= 1

    Parameter n: The number of sides of each polygon
    Precondition: n is an int >= 3

    Parameter sp: The turtle speed.
    Precondition: sp is a valid turtle speed.
    """
    # ARE THESE ALL OF THE PRECONDITIONS?
    assert is_valid_turtlemode(t), report_error('Invalid turtle mode', t)
    assert is_valid_length(side), report_error('side is invalid length',side)
    assert is_valid_iteration(k), report_error('k is invalid number of polygons',k)
    assert n >= 3 and type(n) == int, report_error('n is invalid number of sides',n)
    assert is_valid_speed(sp), report_error('sp is invalid speed',sp)

    c_0 = t.color
    sp_0 = t.speed

    colors = ['blue', 'orange']

    for x in range(k):
        if x == 0 or x == 1:
            t.color = colors[x]
        elif x > 1:
            t.color = colors[x % 2]
        draw_polygon(t, side, n)
        t.left(360.0/k)

    t.color = c_0
    t.speed = sp_0


# DO NOT MODIFY
def draw_polygon(t, side, n):
    """
    Draws an n-sided polygon using of side length side.

    WHEN DONE, THE FOLLOWING TURTLE ATTRIBUTES ARE THE SAME AS IT STARTED:
    position (x and y, within round-off errors), heading, color, speed,
    visible, and drawmode. There is no need to restore these.

    This procedure asserts all preconditions.

    Parameter t: The drawing Turtle
    Precondition: t is a Turtle with drawmode True.

    Parameter side: The length of each polygon side
    Precondition: side is a valid side length (number >= 0)

    Parameter n: The number of sides of each polygon
    Precondition: n is an int >= 1
    """
    # Assert the preconditions
    assert is_valid_turtlemode(t), report_error('Invalid turtle mode', t)
    assert is_valid_length(side), report_error('side is not a valid length',side)
    assert type(n) == int and n >= 1, report_error('n is not valid # of sides',n)

    # Remember old speed
    ang = 360.0/n # exterior angle between adjacent sides

    # t is in position and facing the direction to draw the next line.
    for _ in range(n):
        t.forward(side)
        t.left(ang)


#################### TASK 3C: Radiating Petals ####################

def radiate(w, side, n, sp):
    """
    Drawd n straight radiating lines using radiate_helper(t, side, n, sp)

    This function clears the window and makes a new turtle t.  This turtle
    starts in the middle of the canvas facing west (NOT the default east).
    It then calls radiate_helper(t, side, n, sp). When it is done, the turtle
    is left hidden (visible is False).

    REMEMBER: You need to flush the turtle if the speed is 0.

    Parameter w: The window to draw upon.
    Precondition: w is a tkturtle Window object.

    Parameter side: The length of each radial line
    Precondition: side is a valid side length (number >= 0)

    Parameter n: The number of lines to draw
    Precondition: n is an int >= 2

    Parameter sp: The turtle speed.
    Precondition: sp is a valid turtle speed.
    """
    # ARE THESE ALL OF THE PRECONDITIONS?
    assert is_window(w), report_error('w is invalid window',w)
    assert is_valid_length(side), report_error('side is invalid length',side)
    assert n >= 2 and type(n) == int, report_error('n is not valid number of lines')
    assert is_valid_speed(sp), report_error('sp is invalid speed',sp)

    w.clear()
    t = Turtle(w)
    t.speed = sp
    t.drawmode = True
    t.heading = 180
    radiate_helper(t, side, n, sp)
    t.visible = False

    t.flush()


def radiate_helper(t, side, n, sp):
    """
    Draws n straight radiating lines of length s at equal angles.

    This lines are drawn using turtle t with the turtle moving at speed sp.
    A line drawn at angle ang, 0 <= ang < 360 has HSL color (ang % 360.0, 1, 0.4).

    WHEN DONE, THE FOLLOWING TURTLE ATTRIBUTES ARE THE SAME AS IT STARTED:
    color, speed, visible, and drawmode. However, the final position and
    heading may be different. If you changed any of these four in the
    function, you must change them back.

    Parameter t: The drawing Turtle
    Precondition: t is a Turtle with drawmode True.

    Parameter side: The length of each radial line
    Precondition: side is a valid side length (number >= 0)

    Parameter n: The number of lines to draw
    Precondition: n is an int >= 2

    Parameter sp: The turtle speed.
    Precondition: sp is a valid turtle speed.
    """
    # Assert the preconditions
    assert is_valid_turtlemode(t), report_error('Invalid turtle mode', t)
    assert is_valid_length(side), report_error('side is not a valid length',side)
    assert (type(n) == int and n >= 2), report_error('n is invalid # of petals',n)
    assert is_valid_speed(sp), report_error('sp is not a valid speed',sp)

    c_0 = t.color
    sp_0 = t.speed
    v_0 = t.visible
    draw_0 = t.drawmode

    for x in range(n):
        t.right(360.0/n)
        hsl = introcs.HSL(t.heading % 360.0, 1, 0.4)
        t.color = hsl.webColor()
        t.forward(side)
        t.backward(side)

    t.color = c_0
    t.speed = sp_0
    t.visible = v_0
    t.drawmode = draw_0


#################### TASK 4A: Sierpinski Triangle ####################

def triangle(w, side, d, sp):
    """
    Draws a Sierpinski triangle with the given side length and depth d.

    This function clears the window and makes a new pen p.  This pen starts at the
    triangle center (0,0). This method draws the triangle by calling the helper
    function triangle_helper with color blue: RGB(0,0,255). The pen is hidden during
    drawing and left hidden at the end.

    REMEMBER: You need to flush the pen if the speed is 0.

    Parameter w: The window to draw upon.
    Precondition: w is a cornell Window object.

    Parameter side: The side length of the triangle
    Precondition: side is a valid side length (number >= 0)

    Parameter d: The recursive depth of the triangle
    Precondition: n is a valid depth (int >= 0)
    """
    # ARE THESE ALL OF THE PRECONDITIONS?
    assert is_window(w), report_error('w is invalid window',w)
    assert is_valid_length(side), report_error('side is invalid length', side)
    assert is_valid_depth(d), report_error('d is invalid depth', d)
    assert is_valid_speed(sp), report_error('sp is invalid speed', sp)

    w.clear()
    p = Pen(w)
    p.visible = False
    p.speed = sp
    p.solid = False
    p.move(0, 0)
    blue = introcs.RGB(0, 0, 255)
    triangle_helper(p, 0, 0, blue, side, d)

    p.flush()


def triangle_helper(p, x, y, color, side, d):
    """
    Draws a Sierpinski triangle with side length s and depth d, anchored at (x, y).

    The triangle is draw with current pen visibility attribute, but it uses the provided
    color. Follow the instructions on the course website to recursively draw the
    Sierpinski triangle. Remember to draw an upside down triangle in the center with the
    complement of color.

    Parameter p: The graphics pen
    Precondition: p is a Pen with fill attribute False.

    Parameter x: The x-coordinate of the triangle center
    Precondition: x is a number

    Parameter y: The y-coordinate of the triangle center
    Precondition: y is a number

    Parameter color: The triangle color
    Precondition: color is an RGB object (NOT a string)

    Parameter side: The side-length of the triangle
    Precondition: side is a valid side length (number >= 0)

    Parameter d: The recursive depth of the triangle
    Precondition: n is a valid depth (int >= 0)
    """
    # ARE THESE ALL OF THE PRECONDITIONS?
    assert is_valid_penmode(p), report_error('Invalid pen mode', p)
    assert is_number(x), report_error('x is not a number', x)
    assert is_number(y), report_error('x is not a number', y)
    assert is_valid_color(color), report_error('color is not a color', color)
    assert is_valid_length(side), report_error('side is invalid length', side)
    assert is_valid_depth(d), report_error('d is invalid depth', d)


    colorcomp = introcs.RGB(255-(color.red), 255-(color.green), 255-(color.blue))

    if d == 0:
        p.fillcolor = color
        p.edgecolor = color
        fill_triangle(p, x, y, side, True)
    else:
        x_orient = side/4.0
        y_orient = (side*(math.sqrt(3/4)))/4
        p.fillcolor = colorcomp
        p.edgecolor = colorcomp
        fill_triangle(p, x, y - y_orient, (side/2.0), False)
        triangle_helper(p, x - x_orient, y - y_orient, color, (side/2.0), (d-1))
        triangle_helper(p, x + x_orient, y - y_orient, color, (side/2.0), (d-1))
        triangle_helper(p, x, y + y_orient, color, (side/2.0), (d-1))


# DO NOT MODIFY
def fill_triangle(p, x, y, side, up):
    """
    Fills an equilateral triangle of side length centered at (0,0)

    The triangle may either be pointing up or down, depending upon the value
    of parameter up.

    Parameter p: The graphics pen
    Precondition: p is a Pen with fill attribute False.

    Parameter x: The x-coordinate of the triangle center
    Precondition: x is a number

    Parameter y: The y-coordinate of the triangle center
    Precondition: y is a number

    Parameter side: The side length of the triangle
    Precondition: side is a valid side length (number >= 0)
    """
    # Precondition Assertions
    assert is_valid_penmode(p), report_error('Invalid pen mode', p)
    assert is_number(x), report_error('x is invalid position',x)
    assert is_number(y), report_error('x is invalid position',y)
    assert is_valid_length(side), report_error('side is invalid length',side)

    h = side * math.sqrt(.75)
    if not up:
        h = -h

    p.move(x-side/2, y-h/2)
    p.solid = True
    p.drawLine(side, 0)
    p.drawLine(-side/2.0, h)
    p.drawLine(-side/2.0, -h)
    p.solid = False


#################### TASK 4B: Sierpinski Snowflake ####################

def snowflake(w, side, d, sp):
    """
    Draws a Sierpinski snowflake with the given side length and depth d.

    This function clears the window and makes a new graphics pen p.  This pen starts
    in the middle of the canvas at (0,0). It draws by calling the function
    sierpinski_helper(p, 0, 0, side, d). The pen is hidden during drawing and left
    hidden at the end.

    The pen should have fill color 'deep sky blue' and a 'black' line color.

    REMEMBER: You need to flush the pen if the speed is 0.

    Parameter w: The window to draw upon.
    Precondition: w is a cornell Window object.

    Parameter side: The side-length of the snowflake
    Precondition: side is a valid side length (number >= 0)

    Parameter d: The recursive depth of the snowflake
    Precondition: n is a valid depth (int >= 0)
    """
    # ARE THESE ALL OF THE PRECONDITIONS?
    assert is_window(w), report_error('w is not a valid window',w)

    # HINT: w.clear() clears window.
    # HINT: Set the visible attribute to False at the end, and remember to flush
    pass


def snowflake_helper(p, x, y, side, d):
    """
    Draws a snowflake with the given side length and depth d centered at (x, y).

    The snowflake is draw with the current pen color and visibility attribute. Follow the
    instructions on the course website to recursively draw the Sierpinski snowflake.

    Parameter p: The graphics pen
    Precondition: p is a Pen with fill attribute False.

    Parameter x: The x-coordinate of the snowflake center
    Precondition: x is a number

    Parameter y: The y-coordinate of the snowflake center
    Precondition: y is a number

    Parameter side: The side-length of the snowflake
    Precondition: side is a valid side length (number >= 0)

    Parameter d: The recursive depth of the snowflake
    Precondition: n is a valid depth (int >= 0)
    """
    # ARE THESE ALL OF THE PRECONDITIONS?
    assert is_valid_penmode(p), report_error('Invalid pen mode', p)

    # HINT: Use fill_hex instead of setting p's position directly
    pass


# DO NOT MODIFY
def fill_hex(p, x, y, side):
    """
    Fills a hexagon of side length s with center at (x, y) using pen p.

    Parameter p: The graphics pen
    Precondition: p is a Pen with fill attribute False.

    Parameter x: The x-coordinate of the hexagon center
    Precondition: x is a number

    Parameter y: The y-coordinate of the hexagon center
    Precondition: y is a number

    Parameter side: The side length of the hexagon
    Precondition: side is a valid side length (number >= 0)
    """
    # Precondition assertions omitted
    assert is_valid_penmode(p), report_error('Invalid pen mode', p)
    assert is_number(x), report_error('x is not a valid position',x)
    assert is_number(y), report_error('x is not a valid position',y)
    assert is_valid_length(side), report_error('side is not a valid length',side)

    # Move to the center and draw
    p.move(x + side, y)
    dx = side*math.cos(math.pi/3.0)
    dy = side*math.sin(math.pi/3.0)
    p.solid = True
    p.drawLine(  -dx,  dy)
    p.drawLine(-side,   0)
    p.drawLine(  -dx, -dy)
    p.drawLine(   dx, -dy)
    p.drawLine( side,   0)
    p.drawLine(   dx,  dy)
    p.solid = False


#################### TASK 5: Sierpinski Arrowhead ####################

def arrowhead(w, side, d, sp):
    """
    Draws a Sierpinski arrowhead with the given side length and depth d.

    This function clears the window and makes a new turtle T. While the arrowhead
    triangle is centered at (0,0), the turtle will need to move to the bottom left
    corner of the triangle (see the instructions for how to compute the position).
    The turtle should start facing east and draw a left-turning arrowhead by calling
    arrowhead_helper.

    The turtle should be visible while drawing, but hidden at the end. The turtle
    color is 'sea green'.

    REMEMBER: You need to flush the turtle if the speed is 0.

    Parameter w: The window to draw upon.
    Precondition: w is a Window object.

    Parameter side: The side-length of the arrowhead triangle
    Precondition: side is a valid side length (number >= 0)

    Parameter d: The recursive depth of the arrowhead triangle
    Precondition: n is a valid depth (int >= 0)

    Parameter sp: The drawing speed.
    Precondition: sp is a valid turtle/pen speed.
    """
    # ARE THESE ALL OF THE PRECONDITIONS?
    assert is_window(w), report_error('w is invalid window',w)
    assert is_valid_length(side), report_error('side is invalid length', side)
    assert is_valid_depth(d), report_error('d is invalid depth', d)
    assert is_valid_speed(sp), report_error('sp is invalid speed', sp)

    w.clear()
    T = Turtle(w)
    T.heading = 0
    T.speed = sp
    T.visible = True
    T.color = 'sea green'
    height = side*(math.sqrt(3/4))
    T.move(0 - (side/2.0), 0 - (height/2.0))
    arrowhead_helper(T, side, True, d)
    T.visible = False

    T.flush()


def arrowhead_helper(t, length, left, d):
    """
    Draws an arrowhead with the given length and depth d at the current position.

    The edge is draw with the current turtle color. You should make no assumptions of
    the current angle of the turtle (e.g. use left and right to turn; do not set the
    heading). See the instructions for the difference between a left-turning edge
    and a right-turning edge.

    WHEN DONE, THE FOLLOWING TURTLE ATTRIBUTES ARE THE SAME AS IT STARTED:
    color, speed, visible, and drawmode. However, the final position and
    heading may be different. If you changed any of these four in the function,
    you must change them back.

    Parameter t: The drawing Turtle
    Precondition: t is a Turtle with drawmode True.

    Parameter length: The length of each side in the arrowhead triangle
    Precondition: length is a valid side length (number >= 0)

    Parameter left: The arrowhead orientation (true if left-turning edge)
    Precondition: left is a boolean

    Parameter d: The recursive depth of the edge
    Precondition: n is a valid depth (int >= 0)
    """
    # ARE THESE ALL OF THE PRECONDITIONS?
    assert is_valid_turtlemode(t), report_error('Invalid turtle mode', t)
    assert is_number(length), report_error('length is invalid length', length)
    assert left == True or left == False, ('left is not a boolean', left)
    assert is_valid_depth(d), report_error('d is invalid depth', d)

    c_0 = t.color
    sp_0 = t.speed
    v_0 = t.visible
    draw_0 = t.drawmode

    if d == 0:
        t.forward(length)
    elif d > 0 and left == True:
        t.left(60)
        arrowhead_helper(t, length/2.0, False, (d-1))
        t.right(60)
        arrowhead_helper(t, length/2.0, True, (d-1))
        t.right(60)
        arrowhead_helper(t, length/2.0, False, (d-1))
        t.left(60)
    elif d > 0 and left == False:
        t.right(60)
        arrowhead_helper(t, length/2.0, True, (d-1))
        t.left(60)
        arrowhead_helper(t, length/2.0, False, (d-1))
        t.left(60)
        arrowhead_helper(t, length/2.0, True, (d-1))
        t.right(60)

    t.color = c_0
    t.speed = sp_0
    t.visible = v_0
    t.drawmode = draw_0
