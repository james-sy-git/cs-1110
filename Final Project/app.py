"""
Primary module for Alien Invaders

This module contains the main controller class for the Alien Invaders app.
There is no need for any additional classes in this module.  If you need
more classes, 99% of the time they belong in either the wave module or the
models module. If you are unsure about where a new class should go, post a
question on Piazza.

# James Sy (jcs547) and Willy Swenson (wzs6)
# December 6, 2021
"""
from consts import *
from game2d import *
from wave import *


# PRIMARY RULE: Invaders can only access attributes in wave.py via getters/setters
# Invaders is NOT allowed to access anything in models.py

class Invaders(GameApp):
    """
    The primary controller class for the Alien Invaders application

    This class extends GameApp and implements the various methods necessary
    for processing the player inputs and starting/running a game.

        Method start begins the application.

        Method update either changes the state or updates the Play object

        Method draw displays the Play object and any other elements on screen

    Because of some of the weird ways that Kivy works, you SHOULD NOT create
    an initializer __init__ for this class.  Any initialization should be done
    in the start method instead.  This is only for this class.  All other
    classes behave normally.

    Most of the work handling the game is actually provided in the class Wave.
    Wave should be modeled after subcontrollers.py from lecture, and will
    have its own update and draw method.

    The primary purpose of this class is to manage the game state: which is
    when the game started, paused, completed, etc. It keeps track of that in
    an internal (hidden) attribute.

    For a complete description of how the states work, see the specification
    for the method update.

    Attribute view: the game view, used in drawing
    Invariant: view is an instance of GView (inherited from GameApp)

    Attribute input: user input, used to control the ship or resume the game
    Invariant: input is an instance of GInput (inherited from GameApp)
    """
    # HIDDEN ATTRIBUTES:
    # Attribute _state: the current state of the game represented as an int
    # Invariant: _state is one of STATE_INACTIVE, STATE_NEWWAVE, STATE_ACTIVE,
    # STATE_PAUSED, STATE_CONTINUE, or STATE_COMPLETE
    #
    # Attribute _wave: the subcontroller for a single wave, managing aliens
    # Invariant: _wave is a Wave object, or None if there is no wave currently
    # active. It is only None if _state is STATE_INACTIVE.
    #
    # Attribute _text: the currently active message
    # Invariant: _text is a GLabel object, or None if there is no message to
    # display. It is onl None if _state is STATE_ACTIVE.
    #
    # You may have new attributes if you wish (you might want an attribute to
    # store any score across multiple waves). But you must document them.

    # LIST MORE ATTRIBUTES (AND THEIR INVARIANTS) HERE IF NECESSARY

    # Attribute _last: the number of keys pressed in the previous frame
    # Invariant: _last is an int >= 0
    #
    # Attribute _laststate: the previous state that the game was in
    # Invariant: _laststate is one of STATE_INACTIVE, STATE_NEWWAVE,
    # STATE_ACTIVE, STATE_PAUSED, STATE_CONTINUE
    #
    # Attribute _break: controls if the game is paused
    # Invariant: _break must be a boolean
    #
    # Attribute _textlives: text representing the current lives of the player
    # Invariant: _textlives is a GLabel object, or None if there is no
    # message to display.
    #
    # Attribute _storelives: the remaining lives of the player (does not reset
    # between waves)
    # Invariant: _storelives is an int between 0 and SHIP_LIVES (inclusive)
    #
    # Attribute _title: the title of the game
    # Invariant: _title is a GLabel object. This is only displayed in
    # STATE_INACTIVE
    #
    # Attribute _wavecount: the number of waves remaining in the game
    # Invariant: _wavecount is an int in range 0 to GAME_WAVES, or None
    #
    # Attribute _wavelabel: the counter that displays the waves remaining in
    # the game
    # Invariant: _wavelabel is a GLabel object or None
    #
    # Attribute _storescore: the overall score of the game that carries over
    # between waves
    # Invariant: _storescore is an int >= 0
    #
    # Attribute _background: the background image of the game
    # Invariant: _background is a GImage object that fills a rectangular space
    # of GAME_WIDTH by GAME_HEIGHT
    #
    # Attribute _difficulty: the player-selected difficulty of the game that
    # is determined in the pregame screen
    # Invariant: _difficulty is either EASY, MEDIUM, or HARD, EASY by default
    #
    # Attribute _difftext: the difficulty indicator shown in the pregame screen
    # Invariant: _easytext is a GLabel object (shows 'EASY' by default)

    def start(self):
        """
        Initializes the application.

        This method is distinct from the built-in initializer __init__ (which
        you should not override or change). This method is called once the
        game is running. You should use it to initialize any game specific
        attributes.

        This method should make sure that all of the attributes satisfy the
        given invariants. When done, it sets the _state to STATE_INACTIVE and
        create a message (in attribute _text) saying that the user should press
        to play a game.
        """
        self._state = STATE_INACTIVE
        self._wave = None
        self._text = None
        self._last = 0
        self._laststate = STATE_INACTIVE
        self._break = False
        self._textlives = None
        self._storelives = 0
        self._title = GLabel(text = 'Space\nInvaders', font_size = 120,
        x = GAME_WIDTH/2, y = 510, font_name = 'Arcade.ttf', linecolor = 'white')
        self._wavecount = GAME_WAVES
        self._wavelabel = None
        self._storescore = 0
        self._background = GImage(x = GAME_WIDTH/2, y = GAME_HEIGHT/2,
        width = GAME_WIDTH, height = GAME_HEIGHT, source = 'stars.png')
        self._difficulty = EASY
        self._difftext = GLabel(text = 'EASY', font_size = 70,
        x = GAME_WIDTH/2, y = DEFENSE_LINE, font_name = 'Arcade.ttf',
        linecolor = 'green')

    def update(self,dt):
        """
        Animates a single frame in the game.

        It is the method that does most of the work. It is NOT in charge of
        playing the game.  That is the purpose of the class Wave. The primary
        purpose of this game is to determine the current state, and -- if the
        game is active -- pass the input to the Wave object _wave to play the
        game.

        As part of the assignment, you are allowed to add your own states.
        However, at a minimum you must support the following states:
        STATE_INACTIVE, STATE_NEWWAVE, STATE_ACTIVE, STATE_PAUSED,
        STATE_CONTINUE, and STATE_COMPLETE.  Each one of these does its own
        thing and might even needs its own helper.  We describe these below.

        STATE_INACTIVE: This is the state when the application first opens.
        It is a paused state, waiting for the player to start the game.  It
        displays a simple message on the screen. The application remains in
        this state so long as the player never presses a key.  In addition,
        this is the state the application returns to when the game is over
        (all lives are lost or all aliens are dead).

        STATE_NEWWAVE: This is the state creates a new wave and shows it on
        the screen. The application switches to this state if the state was
        STATE_INACTIVE in the previous frame, and the player pressed a key.
        This state only lasts one animation frame before switching to
        STATE_ACTIVE.

        STATE_ACTIVE: This is a session of normal gameplay.  The player can
        move the ship and fire laser bolts.  All of this should be handled
        inside of class Wave (NOT in this class).  Hence the Wave class
        should have an update() method, just like the subcontroller example
        in lecture.

        STATE_PAUSED: Like STATE_INACTIVE, this is a paused state. However,
        the game is still visible on the screen.

        STATE_CONTINUE: This state restores the ship after it was destroyed.
        The application switches to this state if the state was STATE_PAUSED
        in the previous frame, and the player pressed a key. This state only
        lasts one animation frame before switching to STATE_ACTIVE.

        STATE_COMPLETE: The wave is over, and is either won or lost.

        You are allowed to add more states if you wish. Should you do so, you should
        describe them here.

        Parameter dt: The time in seconds since last update
        Precondition: dt is a number (int or float)
        """
        self.determinestate()

        if self._state == STATE_INACTIVE:
            self.stateinactive()
        elif self._state == STATE_NEWWAVE:
            self.statenewwave()
        elif self._state == STATE_ACTIVE:
            self.stateactive(dt)
        elif self._state == STATE_PAUSED:
            self.statepaused()
        elif self._state == STATE_CONTINUE:
            self.statecontinue()
        elif self._state == STATE_COMPLETE:
            self.statecomplete()

    def draw(self):
        """
        Draws the game objects to the view.

        Every single thing you want to draw in this game is a GObject.  To
        draw a GObject g, simply use the method g.draw(self.view).  It is
        that easy!

        Many of the GObjects (such as the ships, aliens, and bolts) are
        attributes in Wave. In order to draw them, you either need to add
        getters for these attributes or you need to add a draw method to
        class Wave.  We suggest the latter.  See the example subcontroller.py
        from class.
        """
        self._background.draw(self.view)
        if self._state == STATE_INACTIVE:
            self._difftext.draw(self.view)
            self._title.draw(self.view)
            if self._text != None:
                self._text.draw(self.view)
        elif self._state == STATE_ACTIVE or self._state == STATE_PAUSED:
            self._wave.wavedraw(self.view)
            self._textlives.draw(self.view)
            self._textscore.draw(self.view)
            self._wavelabel.draw(self.view)
            if self._state == STATE_PAUSED:
                self._text.draw(self.view)
        elif self._state == STATE_COMPLETE:
            self._text.draw(self.view)
            if self._textscore != None:
                self._textscore.draw(self.view)

    def key(self):
        """
        Returns True if a key was pressed in this animation frame and not
        the previous one.
        """
        current = self.input.key_count

        change = current > 0 and self._last == 0

        self._last = current

        return change

    def determinestate(self):
        """
        Determines the state of the game
        """
        if self.key() and self.input.is_key_down('s') and \
        self._state == STATE_INACTIVE:
            self._state = STATE_NEWWAVE
            self._laststate = STATE_NEWWAVE

        elif self._laststate == self._state and self._state == STATE_NEWWAVE:
            self._state = STATE_ACTIVE
            self._laststate = STATE_ACTIVE

        elif (self._state == STATE_ACTIVE and self.alienwin()) or \
        (self._state == STATE_ACTIVE and self.playerwin()):
            self._state = STATE_COMPLETE

        elif self._state == STATE_ACTIVE and not self._wave.survivors() and \
        self._wavecount > 0:
            self._state = STATE_NEWWAVE
            self._laststate = STATE_NEWWAVE
            self._wavecount -= 1
            if self._wavecount > 0:
                self._storescore += self._wave.getscore()
                self._storelives = self._wave.getlives()

        elif self._break:
            self.breakhelper()

        elif self._state == STATE_PAUSED:
            if self.input.is_key_down('s'):
                self._state = STATE_CONTINUE
                self._laststate = STATE_PAUSED

        elif self._state == STATE_CONTINUE and self._laststate == STATE_PAUSED:
            self._state = STATE_ACTIVE

    def stateinactive(self):
        """
        Creates the starting screen instruction message and allows the player
        to select their desired difficulty while also updating the difficulty
        indicator.
        """
        if self.input.is_key_down('q'):
            self._difficulty = EASY
            self._difftext = GLabel(text = 'EASY', font_size = 70,
            x = GAME_WIDTH/2, y = 100, font_name = 'Arcade.ttf',
            linecolor = 'green')
        if self.input.is_key_down('w'):
            self._difficulty = MEDIUM
            self._difftext = GLabel(text = 'MEDIUM', font_size = 70,
            x = GAME_WIDTH/2, y = 100, font_name = 'Arcade.ttf',
            linecolor = 'orange')
        if self.input.is_key_down('e'):
            self._difficulty = HARD
            self._difftext = GLabel(text = 'DIFFICULT', font_size = 70,
            x = GAME_WIDTH/2, y = 100, font_name = 'Arcade.ttf',
            linecolor = 'red')
        self._text = GLabel(text = startmessage, font_size = 20,
        x = GAME_WIDTH/2, y = GAME_HEIGHT/2.5, font_name = 'RetroGame.ttf',
        linecolor = 'white')

    def statenewwave(self):
        """
        Creates a new Wave object with the difficulty determined by
        _difficulty.
        """
        if 0 < self._wavecount <= 3:
            self._wave = Wave(self._difficulty)
        if 0 < self._wavecount < 3:
            self._wave.setlives(self._storelives)

    def stateactive(self, dt):
        """
        Creates the lives counter and updates the wave. Updates self._break
        if the conditions to stop updating are met.

        Parameter dt: The time in seconds since last update
        Precondition: dt is a number (int or float)
        """
        self._textlives = GLabel(text = 'LIVES: ' + str(self._wave.getlives()),
        font_size = 20, x = GAME_WIDTH-100, y = GAME_HEIGHT-30,
        font_name = 'RetroGame.ttf', linecolor = 'white')
        self._textscore = GLabel(text = 'SCORE ' + str(self._wave.getscore() + \
        self._storescore),
        font_size = 20, x = GAME_WIDTH-700, y = GAME_HEIGHT-30,
        font_name = 'RetroGame.ttf', linecolor = 'white')
        self._wavelabel = GLabel(text = 'WAVES REMAINING: ' + str(self._wavecount),
        font_size = 20, x = GAME_WIDTH/2, y = GAME_HEIGHT - 30,
        font_name = 'RetroGame.ttf', linecolor = 'white')
        if (self._wave.getship() != None) and (self._wave.survivors() \
        or not self._wave.crossdline()):
            self._wave.update(self.input, dt)
        else:
            self._break = True

    def statepaused(self):
        """
        Creates the message to be displayed when the ship has been hit and
        the player must choose whether to continue.
        """
        self._text = GLabel(text = pausemessage, font_size = 45,
        x = GAME_WIDTH/2, y = GAME_HEIGHT/2, font_name = 'Arcade.ttf',
        linecolor = 'red')

    def statecontinue(self):
        """
        Restores the ship in preparation for the continuation of the wave.
        """
        self._wave.restoreship()

    def statecomplete(self):
        """
        Runs two attribute-setters if the state is STATE_COMPLETE.
        """
        self.playerwin()
        self.alienwin()

    def breakhelper(self):
        """
        If self._break is True, checks if player or alien wins, or if the game
        should conitnue, and changes state accordingly.
        """
        if self.playerwin() or self.alienwin():
            self._state = STATE_COMPLETE
        else:
            self._state = STATE_PAUSED
            self._laststate = STATE_ACTIVE
            self._break = False

    def playerwin(self):
        """
        Returns True if there are no aliens left AND the player has more than
        0 lives remaining: Player wins. Also updates self._text.

        Returns False otherwise
        """
        if self._wavecount == 1 and self._wave.getlives() > 0 and \
        self._wave.survivors() is False:
            self._text = GLabel(text = winmessage, font_size = 70,
            x = GAME_WIDTH/2, y = GAME_HEIGHT/2, font_name = 'Arcade.ttf',
            linecolor = CYAN)
            self._textscore = None
            return True
        else:
            return False

    def alienwin(self):
        """
        Returns True if the player has 0 lives or the bottom most alien crosses
        the Defense Line: Aliens win. Also updates self._text.

        Returns False otherwise
        """
        if self._wave.getlives() == 0 or self._wave.crossdline():
            self._text = GLabel(text = losemessage, font_size = 80,
            x = GAME_WIDTH/2, y = GAME_HEIGHT/2, font_name = 'Arcade.ttf',
            linecolor = 'red')
            self._textscore = GLabel(text = 'FINAL SCORE: ' + \
            str(self._wave.getscore() + self._storescore),
            font_size = 40, x = GAME_WIDTH/2, y = GAME_HEIGHT-100,
            font_name = 'Arcade.ttf', linecolor = 'white')
            return True
        else:
            return False
