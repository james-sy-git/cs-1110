"""
Models module for Alien Invaders

This module contains the model classes for the Alien Invaders game. Anything
that you interact with on the screen is model: the ship, the laser bolts, and
the aliens.

Just because something is a model does not mean there has to be a special
class for it. Unless you need something special for your extra gameplay
features, Ship and Aliens could just be an instance of GImage that you move
across the screen. You only need a new class when you add extra features to
an object. So technically Bolt, which has a velocity, is really the only model
that needs to have its own class.

With that said, we have included the subclasses for Ship and Aliens. That is
because there are a lot of constants in consts.py for initializing the
objects, and you might want to add a custom initializer.  With that said,
feel free to keep the pass underneath the class definitions if you do not want
to do that.

You are free to add even more models to this module.  You may wish to do this
when you add new features to your game, such as power-ups.  If you are unsure
about whether to make a new class or not, please ask on Piazza.

# James Sy (jcs547) and Willy Swenson (wzs6)
# December 6, 2021
"""
from consts import *
from game2d import *

# PRIMARY RULE: Models are not allowed to access anything in any module other
# than consts.py.  If you need extra information from Gameplay, then it should
# be a parameter in your method, and Wave should pass it as a argument when it
# calls the method.


class Ship(GSprite):
    """
    A class to represent the game ship.

    At the very least, you want a __init__ method to initialize the ships
    dimensions. These dimensions are all specified in consts.py.

    You should probably add a method for moving the ship.  While moving a
    ship just means changing the x attribute (which you can do directly),
    you want to prevent the player from moving the ship offscreen.  This
    is an ideal thing to do in a method.

    You also MIGHT want to add code to detect a collision with a bolt. We
    do not require this.  You could put this method in Wave if you wanted to.
    But the advantage of putting it here is that Ships and Aliens collide
    with different bolts.  Ships collide with Alien bolts, not Ship bolts.
    And Aliens collide with Ship bolts, not Alien bolts. An easy way to
    keep this straight is for this class to have its own collision method.

    However, there is no need for any more attributes other than those
    inherited by GImage. You would only add attributes if you needed them
    for extra gameplay features (like animation).
    """

    def getframe(self):
        """
        Returns the value of the current frame of the Ship
        """
        return self.frame

    def setframe(self, value):
        """
        Assigns value input to the attribute 'frame'
        """
        self.frame = value

    def __init__(self, x, y, width, height, source, format):
        """
        Initializes a new ship with the given parameters

        Parameter x: the x coordinate of the ship
        Precondition: Value must be an int or float

        Parameter y: the y coordinate of the ship
        Precondition: Value must be an int or float

        Parameter width: the width of the ship
        Precondition: Value must be an a int or float that is positive

        Parameter height: the height of the ship
        Precondition: Value must be an a int or float that is positive

        Parameter source: the source of the ship
        Precondition: value be a string referring to a .png file in Images

        Parameter format: the format of the ship
        Precondition: a tuple of the rows followed by length of row
        """
        super().__init__(x=x, y=y, width=width, height=height, source=source,
        format=format)

    def moveship(self, input):
        """
        Adjusts the x coordinates of the ship to move it given the input of
        the left and right arrow keys

        Parameter input: allows access to the methods within GInput
        Precondition: input is a attribute of Invaders
        """
        if self.getframe() is 0:
            if input.is_key_down('right'):
                self.x += SHIP_MOVEMENT
            if input.is_key_down('left'):
                self.x -= SHIP_MOVEMENT
            if self.x <= SHIP_WIDTH/2:
                self.x = SHIP_WIDTH/2
            if self.x >= (GAME_WIDTH - SHIP_WIDTH/2):
                self.x = (GAME_WIDTH - SHIP_WIDTH/2)

    def collides(self, bolt):
        """
        Returns True if the alien bolt collides with this ship

        This method returns False if bolt was not fired by the alien.

        Parameter bolt: The laser bolt to check
        Precondition: bolt is an object of class Bolt
        """
        x_inc = BOLT_WIDTH/2
        y_inc = BOLT_HEIGHT/2
        c1 = (bolt.x - x_inc, bolt.y + y_inc)
        c2 = (bolt.x + x_inc, bolt.y + y_inc)
        c3 = (bolt.x - x_inc, bolt.y - y_inc)
        c4 = (bolt.x + x_inc, bolt.y - y_inc)

        if (self.contains(c1) or self.contains(c2) or self.contains(c3)
        or self.contains(c4)) and bolt.getvelocity() < 0:
            return True
        else:
            return False


class Alien(GSprite):
    """
    A class to represent a single alien.

    At the very least, you want a __init__ method to initialize the alien
    dimensions. These dimensions are all specified in consts.py.

    You also MIGHT want to add code to detect a collision with a bolt. We
    do not require this.  You could put this method in Wave if you wanted to.
    But the advantage of putting it here is that Ships and Aliens collide
    with different bolts.  Ships collide with Alien bolts, not Ship bolts.
    And Aliens collide with Ship bolts, not Alien bolts. An easy way to
    keep this straight is for this class to have its own collision method.

    However, there is no need for any more attributes other than those
    inherited by GImage. You would only add attributes if you needed them
    for extra gameplay features (like giving each alien a score value).
    """

    def getframe(self):
        """
        Returns the value of the current frame of the Alien
        """
        return self.frame

    def setframe(self, value):
        """
        Assigns value input to the attribute 'frame'
        """
        self.frame = value

    def __init__(self, x, y, width, height, source, format):
        """
        Initializes a new alien with the given parameters

        Parameter x: the x coordinate of the alien
        Precondition: Value must be an int or float

        Parameter y: the y coordinate of the alien
        Precondition: Value must be an int or float

        Parameter width: the width of the alien
        Precondition: Value must be an a int or float that is positive

        Parameter height: the height of the alien
        Precondition: Value must be an a int or float that is positive

        Parameter source: the source of the alien
        Precondition: value be a string referring to a .png file in Images
        """
        super().__init__(x=x, y=y, width=width, height=height, source=source,
        format=format)

    def collides(self, bolt):
        """
        Returns True if the player bolt collides with this alien

        This method returns False if bolt was not fired by the player.

        Parameter bolt: The laser bolt to check
        Precondition: bolt is an object of class Bolt
        """
        x_inc = BOLT_WIDTH/2
        y_inc = BOLT_HEIGHT/2
        c1 = (bolt.x - x_inc, bolt.y + y_inc)
        c2 = (bolt.x + x_inc, bolt.y + y_inc)
        c3 = (bolt.x - x_inc, bolt.y - y_inc)
        c4 = (bolt.x + x_inc, bolt.y - y_inc)

        if (self.contains(c1) or self.contains(c2) or self.contains(c3)
        or self.contains(c4)) and bolt.getvelocity() > 0:
            return True
        else:
            return False


class Bolt(GRectangle):
    """
    A class representing a laser bolt.

    Laser bolts are often just thin, white rectangles. The size of the bolt
    is determined by constants in consts.py. We MUST subclass GRectangle,
    because we need to add an extra (hidden) attribute for the velocity of
    the bolt.

    The class Wave will need to look at these attributes, so you will need
    getters for them.  However, it is possible to write this assignment with
    no setters for the velocities.  That is because the velocity is fixed and
    cannot change once the bolt is fired.

    In addition to the getters, you need to write the __init__ method to set
    the starting velocity. This __init__ method will need to call the __init__
    from GRectangle as a  helper.

    You also MIGHT want to create a method to move the bolt.  You move the
    bolt by adding the velocity to the y-position.  However, the getter
    allows Wave to do this on its own, so this method is not required.
    """
    # INSTANCE ATTRIBUTES:
    # Attribute _velocity: the velocity in y direction
    # Invariant: _velocity is an int or float

    def getvelocity(self):
        """
        Returns the value of the velocity of the bolt
        """
        return self._velocity

    def __init__(self, x, y, width, height, fillcolor, linecolor, velocity):
        """
        Initializes a new bolt with the given parameters

        Parameter x: the x coordinate of the bolt
        Precondition: Value must be an int or float

        Parameter y: the y coordinate of the bolt
        Precondition: Value must be an int or float

        Parameter width: the width of the bolt
        Precondition: Value must be an a int or float that is positive

        Parameter height: the height of the bolt
        Precondition: Value must be an a int or float that is positive

        Parameter fillcolor: the source of the bolt
        Precondition: Value must be None or a 4-element list of floats
        between 0 and 1

        Parameter linecolor: the linecolor of the bolt
        Precondition: Value must be None or a 4-element list of floats
        between 0 and 1

        Parameter velocity: the velocity of the bolt
        Precondition: must be an int or float
        """
        super().__init__(x=x, y=y, width=width, height=height,
        fillcolor=fillcolor, linecolor=linecolor)
        self._velocity = velocity

    def updatey(self):
        """
        Updates the y coordinate of the bolt by the addtion of the velocity
        """
        self.y += self._velocity

    def isplayerbolt(self):
        """
        Returns True if the velocity is postive, False otherwise
        """
        if self._velocity > 0:
            return True
        else:
            return False
