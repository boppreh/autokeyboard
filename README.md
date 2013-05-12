autokeyboard
============

*autokeyboard* is both a library and a standalone application to automate
keyboard actions. It listens to global hotkeys and generates keyboard events
that mimic user keyboard interactions to the current application.


Text Shortcuts
--------------

Types a given text excerpt when a hotkey is pressed. Useful for canned replies
and filling out form data. Supported charset is very limited at the moment.


Generic Shortcuts
-----------------

Simulates a whole chain of arbitrary keypresses when the hotkey is invoked.
Useful for automating tasks.


Turbo
-----

Used to speed up keys. When a "turboed" key is held, it emits hold and release
events pretending it is being constantly pressed. To turbo a key, just press
the key while holding the turbo hotkey. Doing so again clears the modification.

The name comes from the button available in a few video game controllers that
does the same thing, so you can guess this is perfect for games.


Macro
-----

One hotkey starts recording, another stops recording and the third will
playback everything you recorded. Simple, efficient, tremendously useful. The
playback is done at the same speed recorded or you can configure a speed
factor (try 0 for instant replay).

Because it handles the internal events and there is no description/letter to
keycode conversion required, this feature should be the most reliable, working
on any keyboard layout, application and key combination.
