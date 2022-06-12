"""
Subcontroller module for Alien Invaders

This module contains the subcontroller to manage a single level or wave in
the Alien Invaders game.  Instances of Wave represent a single wave. Whenever
you move to a new level, you are expected to make a new instance of the class.

The subcontroller Wave manages the ship, the aliens and any laser bolts on
screen. These are model objects.  Their classes are defined in models.py.

Most of your work on this assignment will be in either this module or
models.py. Whether a helper method belongs in this module or models.py is
often a complicated issue.  If you do not know, ask on Piazza and we will
answer.

# James Sy (jcs547) and Willy Swenson (wzs6)
# December 6, 2021
"""
from game2d import *
from consts import *
from models import *
import random

# PRIMARY RULE: Wave can only access attributes in models.py via getters/setters
# Wave is NOT allowed to access anything in app.py (Subcontrollers are not
# permitted to access anything in their parent. To see why, take CS 3152)


class Wave(object):
    """
    This class controls a single level or wave of Alien Invaders.

    This subcontroller has a reference to the ship, aliens, and any laser bolts
    on screen. It animates the laser bolts, removing any aliens as necessary.
    It also marches the aliens back and forth across the screen until they are
    all destroyed or they reach the defense line (at which point the player
    loses). When the wave is complete, you  should create a NEW instance of
    Wave (in Invaders) if you want to make a new wave of aliens.

    If you want to pause the game, tell this controller to draw, but do not
    update.  See subcontrollers.py from Lecture 24 for an example.  This
    class will be similar to than one in how it interacts with the main class
    Invaders.

    All of the attributes of this class ar to be hidden. You may find that
    you want to access an attribute in class Invaders. It is okay if you do,
    but you MAY NOT ACCESS THE ATTRIBUTES DIRECTLY. You must use a getter
    and/or setter for any attribute that you need to access in Invaders.
    Only add the getters and setters that you need for Invaders. You can keep
    everything else hidden.

    """
    # HIDDEN ATTRIBUTES:
    # Attribute _ship: the player ship to control
    # Invariant: _ship is a Ship object or None
    #
    # Attribute _aliens: the 2d list of aliens in the wave
    # Invariant: _aliens is a rectangular 2d list containing Alien objects or None
    #
    # Attribute _bolts: the laser bolts currently on screen
    # Invariant: _bolts is a list of Bolt objects, possibly empty
    #
    # Attribute _dline: the defensive line being protected
    # Invariant : _dline is a GPath object
    #
    # Attribute _lives: the number of lives left
    # Invariant: _lives is an int >= 0
    #
    # Attribute _time: the amount of time since the last Alien "step"
    # Invariant: _time is a float >= 0s
    #
    # You may change any attribute above, as long as you update the invariant
    # You may also add any new attributes as long as you document them.
    # LIST MORE ATTRIBUTES (AND THEIR INVARIANTS) HERE IF NECESSARY
    #
    # Attribute _left: the direction of alien movement (True if moving left,
    # False if moving right)
    # Invariant: _left is a bool
    #
    # Attribute _fire: status of whether or not a player has fired a bolt
    # Invariant: _fire is a bool
    #
    # Attribute _steps: the number of steps until the aliens fire
    # Invariant: _steps is an int >= 0
    #
    # Attribute _track: whether or not a player-fired bolt has hit an alien
    # Invariant: _track is a bool
    #
    # Attribute _animator: a coroutine for creating a ship explosion animation
    # Invariant: _animator is a generator-based coroutine or None
    #
    # Attribute _shiptracker: whether or not the ship has been destroyed
    # Invariant: _shiptracker is a bool
    #
    # Attribute _score: player score for a wave
    # Invariant: _score is an int >= 0
    #
    # Attribute _pointmultiplier: value to multiply score by
    # (row of alien destroyed)
    # Invariant: _pointmultiplier is an int in range ALIEN_ROWS - 1
    #
    # Attribute _alien_animator: a coroutine for creating an alien explosion
    # animation
    # Invariant: _alien_animator is a generator-based coroutine or None
    #
    # Attribute _aliendestroyed: stores the most recent alien that was hit by
    # a bolt
    # Invariant: _aliendestroyed is an alien in self._aliens or None
    #
    # Attribute _alienspeed: the number of seconds between alien steps
    # Invariant: _alienspeed is a float between 0.0 and ALIEN_SPEED (inclusive)

    def getlives(self):
        """
        Returns the number of lives remaining for this wave's ship.
        """
        return self._lives

    def setlives(self, value):
        """
        Sets the number of lives remaining for this wave.

        Parameter value: the number of lives remaining
        Precondition: value is an int between 0 and SHIP_LIVES (inclusive)
        """
        self._lives = value

    def getship(self):
        """
        Returns the ship for this wave.
        """
        return self._ship

    def getscore(self):
        """
        Returns the score for this wave.
        """
        return self._score

    def __init__(self, speed):
        """
        Initializes the attributes for a new Wave object.

        Parameter speed: the difficulty that corresponds to a float between
        0 and 1 in consts.py
        Precondition: speed is either EASY, MEDIUM, or DIFFICULT
        """
        self._ship = Ship(GAME_WIDTH/2, SHIP_BOTTOM + SHIP_HEIGHT/2, SHIP_WIDTH,
        SHIP_HEIGHT, SHIP_IMAGE, (2,4))
        self._ship.setframe(0)
        self._aliens = self.createaliens()
        self._bolts = []
        self._dline = GPath(points=[0,DEFENSE_LINE, GAME_WIDTH, DEFENSE_LINE],
        linewidth=1, linecolor=DLINE_COLOR)
        self._lives = SHIP_LIVES
        self._time = 0.0
        self._left = False
        self._fire = False
        self._steps = random.randint(1, BOLT_RATE)
        self._track = False
        self._animator = None
        self._shiptracker = False
        self._score = 0
        self._pointmultiplier = 0
        self._alien_animator = None
        self._aliendestroyed = None
        self._alienspeed = speed

    def update(self, input, dt):
        """
        Moves and updates the ship, aliens, and laser bolts.

        Parameter input: the user input
        Precondition: input is an instance of GInput (inherited from GameApp)

        Parameter dt: The number of seconds that have passed since the
        last animation frame
        Precondition: dt is a float >= 0.0
        """
        if self._ship.getframe() is 0 and self.survivors():
            self._ship.moveship(input)
            self.boltcollide_ship()
            self.bolt(input)
            self.has_player_fired()
            self.stepaliens(dt)
            self.boltcollide_alien()
            self.count_score()
            self.updatespeed()
        if not self._animator is None: # SHIP
            try:
                self._animator.send(dt)
            except:
                self._animator = None
                self._ship = None
                self.clearbolts()
                self._lives = self._lives - 1
        elif self._shiptracker:
            self._animator = self.animateship(dt)
            next(self._animator)
        if not self._alien_animator is None: # ALIEN
            try:
                self._alien_animator.send(dt)
            except:
                self._alien_animator = None
        elif self._track:
            self._alien_animator = self.animatealien(dt)
            next(self._alien_animator)

    def wavedraw(self, view):
        """
        Draws the ship, aliens, defensive line, and bolts.

        Parameter view: The window on which to draw
        Precondition: view is an instance of GView (inherited from GameApp)
        """
        for x in self._aliens:
            for y in x:
                if y != None:
                    y.draw(view)
        if self._ship != None:
            self._ship.draw(view)
        self._dline.draw(view)
        for x in self._bolts:
            x.draw(view)

    def createaliens(self):
        """
        Creates an array of aliens with ALIEN_ROW row and ALIENS_IN_ROW aliens
        in each row.
        """
        cols = []
        top_dist_one = GAME_HEIGHT - ALIEN_CEILING
        real_sep = ALIEN_V_SEP + ALIEN_HEIGHT
        sources = ['alien-strip1.png','alien-strip1.png','alien-strip2.png',
        'alien-strip2.png', 'alien-strip3.png','alien-strip3.png']
        h_sep_unit = ALIEN_H_SEP + ALIEN_WIDTH
        x = ALIEN_ROWS - 1
        while x >= 0:
            rows = []
            top_dist = top_dist_one - (ALIEN_HEIGHT/2) - (real_sep*x)
            x -= 1
            y = ALIENS_IN_ROW - 1
            while y >= 0:
                alien = Alien((h_sep_unit + h_sep_unit*y), top_dist, ALIEN_WIDTH,
                ALIEN_HEIGHT, sources[x%6], (4,2))
                alien.setframe(0)
                rows.append(alien)
                y -= 1
            cols.append(rows)

        return cols

    def stepaliens(self, dt):
        """
        Moves the aliens. Starts the aliens back in the other direction
        if the aliens have reached a distance of ALIEN_H_SEP from either edge.

        Parameter dt: The number of seconds that have passed since the
        last animation frame
        Precondition: dt is a float >= 0.0
        """
        right_limit = GAME_WIDTH - (ALIEN_H_SEP + ALIEN_WIDTH/2)
        left_limit = ALIEN_H_SEP + ALIEN_WIDTH/2
        
        if self._left == False: # MOVING RIGHT
            if self._time > self._alienspeed:
                self.stepright()
                self.alienbolt()
                self._time = 0.0
            elif self._time <= self._alienspeed:
                self._time += dt
            if (self.rightmost().x) > right_limit:
                self.stepdown()
                self._left = True

        if self._left == True: # MOVING LEFT
            if self._time > self._alienspeed:
                self.stepleft()
                self.alienbolt()
                self._time = 0.0
            elif self._time <= self._alienspeed:
                self._time += dt
            if (self.leftmost()).x < left_limit:
                self.stepdown()
                self._left = False

    def stepdown(self):
        """
        Helper method for stepaliens that moves the aliens down by increments
        of ALIEN_V_WALK
        """
        for x in range(len(self._aliens)):
            for y in self._aliens[x]:
                if y != None:
                    y.y -= ALIEN_V_WALK

    def stepright(self):
        """
        Helper method for stepaliens that moves the aliens right by increments
        of ALIEN_H_WALK
        """
        for x in range(len(self._aliens)):
            for y in self._aliens[x]:
                if y != None:
                    y.x += ALIEN_H_WALK

    def stepleft(self):
        """
        Helper method for stepaliens that moves the aliens left by increments
        of ALIEN_H_WALK.
        """
        for x in range(len(self._aliens)):
            for y in self._aliens[x]:
                if y != None:
                    y.x -= ALIEN_H_WALK

    def leftmost(self):
        """
        Helper method for stepaliens that eturns the leftmost alien in the
        array.
        """
        temp_one = []
        for alien in range(ALIENS_IN_ROW):
            temp = []
            for rows in range(ALIEN_ROWS):
                temp.append(self._aliens[rows][alien])
            temp_one.append(temp)
        temp_one.reverse()
        for x in range(ALIENS_IN_ROW):
            if temp_one[x].count(None) is not len(temp_one[x]):
                for y in temp_one[x]:
                    if y is not None:
                        return y

    def rightmost(self):
        """
        Helper method for stepaliens that eturns the rightmost alien in the
        array.
        """
        temp_one = []
        for alien in range(ALIENS_IN_ROW):
            temp = []
            for rows in range(ALIEN_ROWS):
                temp.append(self._aliens[rows][alien])
            temp_one.append(temp)
        for x in range(ALIENS_IN_ROW):
            if temp_one[x].count(None) is not len(temp_one[x]):
                for y in temp_one[x]:
                    if y is not None:
                        return y

    def bolt(self, input):
        """
        Creates the player bolts and adds them to self._bolts.

        Attribute input: the user input
        Precondition: input is an instance of GInput (inherited from GameApp)
        """
        current = input.key_count
        change = current > 0 and self._fire == False

        if change == True and input.is_key_down('spacebar') and self._ship != None:
            newbolt = Bolt(x=self._ship.x, y=(SHIP_BOTTOM + SHIP_HEIGHT),
            width=BOLT_WIDTH, height=BOLT_HEIGHT, fillcolor='red',
            linecolor='red', velocity=BOLT_SPEED)

            self._bolts.append(newbolt)

        self.updatebolt()

    def has_player_fired(self):
        """
        Updates self._fire if the player has fired a bolt.
        """
        for x in self._bolts:
            if x.getvelocity() > 0:
                self._fire = True

    def alienbolt(self):
        """
        Creates the alien bots and adds them to self._bolts.
        """
        alien = self.pickalien()

        if alien != None:
            if self._steps == 0:
                newbolt = Bolt(x=(alien.x), y=(alien.y)-ALIEN_HEIGHT/2,
                width=BOLT_WIDTH, height=BOLT_HEIGHT, fillcolor='green',
                linecolor='green', velocity=(-1)*BOLT_SPEED)

                self._bolts.append(newbolt)
                self._steps = random.randint(1, BOLT_RATE)

            else:
                self._steps -= 1
        else:
            self.alienbolt()

    def pickalien(self):
        """
        Returns a random, bottommost, non-None alien to fire a bolt;
        a helper for alienbolt.
        """
        choosecol = random.randint(0, ALIENS_IN_ROW-1)
        alien_temp = []
        for x in self._aliens:
            alien_temp.append(x[choosecol])
        for x in alien_temp:
            if x != None:
                return x

    def updatebolt(self):
        """
        Updates both the player bolts and removes bolts when necessary.
        """
        for x in self._bolts:
            x.updatey()
            if self._ship == None:
                self._bolts.clear()
            elif x.getvelocity() > 0:
                if (x.y - BOLT_HEIGHT/2) >= GAME_HEIGHT \
                or self._track == True:
                    self._bolts.remove(x)
                    self._fire = False
                    self._track = False
            else:
                if (x.y + BOLT_HEIGHT/2) <= 0:
                    self._bolts.remove(x)

    def boltcollide_alien(self):
        """
        Checks if a player bolt has collided with any aliens. Updates
        self._track and self._aliendestroyed if this condition is met.
        """
        for row in range(ALIEN_ROWS):
            for alien in range(ALIENS_IN_ROW):
                for bolt in self._bolts:
                    if self._aliens[row][alien] != None:
                        if self._aliens[row][alien].collides(bolt):
                            self._pointmultiplier = row
                            self._aliendestroyed = self._aliens[row][alien]
                            self._track = True

    def count_score(self):
        """
        Updates the score when an alien is destroyed. Every row up from the
        bottom values the alien at 10 fewer points (max. points per alien is 100).
        """
        max = 100
        if self._track:
            self._score += max - (self._pointmultiplier*10)

    def boltcollide_ship(self):
        """
        Checks if any bolts fired by aliens have collided with the ship.
        Updates self._shiptracker and removes the collided bolt if this
        condition is met.
        """
        for bolt in self._bolts:
            if self._ship != None:
                if self._ship.collides(bolt):
                    self._shiptracker = True
                    self._bolts.remove(bolt)

    def clearbolts(self):
        """
        Clears all bolts from self._bolts and prepares the attributes to
        allow the player to fire again.
        """
        self._bolts = []
        self._fire = False
        self._track = False

    def restoreship(self):
        """
        Restores the ship after it is destroyed.
        """
        self._ship = Ship(GAME_WIDTH/2, SHIP_BOTTOM + SHIP_HEIGHT/2, SHIP_WIDTH,
        SHIP_HEIGHT, 'ship-strip.png', (2,4))
        self._ship.setframe(0)
        self._shiptracker = False

    def survivors(self):
        """
        Returns True if there are aliens left in the wave (e.g., the aliens
        are not all None), and False otherwise.
        """
        survivor = False
        for row in self._aliens:
            for alien in row:
                if alien != None:
                    survivor = True
        return survivor

    def crossdline(self):
        """
        Returns True if any alien has crossed the defense line, and False
        otherwise.
        """

        ret_val = False
        for row in self._aliens:
            for alien in row:
                if alien != None:
                    if (alien.y - (ALIEN_HEIGHT/2)) < DEFENSE_LINE:
                        ret_val = True
        return ret_val

    def updatespeed(self):
        """
        Decreases self._alienspeed (thus increasing the speed at which the
        wave moves) if the player destroys an alien
        """
        if self._track:
            self._alienspeed = self._alienspeed * SPEED_MULT

    def animateship(self, dt):
        """
        Animator to display the explosion of the ship.

        Parameter dt: The number of seconds that have passed since the
        last animation frame.
        Precondition: dt is a float >= 0.0
        """
        timepassed = 0
        frametime = (DEATH_SPEED/7)
        if timepassed < DEATH_SPEED:
            animating = True
        while animating:
            dt = (yield)
            timepassed += dt

            if timepassed < frametime:
                self._ship.setframe(1)
            elif frametime <= timepassed < frametime*2:
                self._ship.setframe(2)
            elif frametime*2 <= timepassed < frametime*3:
                self._ship.setframe(3)
            elif frametime*3 <= timepassed < frametime*4:
                self._ship.setframe(4)
            elif frametime*4 <= timepassed < frametime*5:
                self._ship.setframe(5)
            elif frametime*5 <= timepassed < frametime*6:
                self._ship.setframe(6)
            elif timepassed >= frametime*6:
                self._ship.setframe(7)
            if timepassed > DEATH_SPEED:
                animating = False

    def animatealien(self, dt):
        """
        Animator to display the explosion of the alien.

        Parameter dt: The number of seconds that have passed since the
        last animation frame.
        Precondition: dt is a float >= 0.0
        """
        timepassed = 0
        frametime = (DEATH_SPEED/7)
        if timepassed < DEATH_SPEED:
            animating = True
        while animating:
            dt = (yield)
            timepassed += dt

            if timepassed < frametime:
                self._aliendestroyed.setframe(1)
            elif frametime <= timepassed < frametime*2:
                self._aliendestroyed.setframe(2)
            elif frametime*2 <= timepassed < frametime*3:
                self._aliendestroyed.setframe(3)
            elif frametime*3 <= timepassed < frametime*4:
                self._aliendestroyed.setframe(4)
            elif frametime*4 <= timepassed < frametime*5:
                self._aliendestroyed.setframe(5)
            elif frametime*5 <= timepassed < frametime*6:
                self._aliendestroyed.setframe(6)
            elif timepassed >= frametime*6:
                self._aliendestroyed.setframe(7)
            if timepassed > DEATH_SPEED:
                self.deletealien()
                animating = False

    def deletealien(self):
        """
        Sets alien to none once the animation completes.
        """
        for row in range(ALIEN_ROWS):
            for alien in range(ALIENS_IN_ROW):
                if self._aliens[row][alien] != None:
                    if self._aliens[row][alien].getframe() == 7:
                        self._aliens[row][alien] = None
