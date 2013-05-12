from time import sleep
from keyboard import *

def setup_text_shortcuts(text_by_shortcut):
    """
    Defines a series of key combinations that, when pressed, type the
    corresponding text excerpt.
    """
    for shortcut, text in text_by_shortcut.items():
        register_hotkey(shortcut, write, [text])

def setup_shortcuts(combinations_by_shortcut):
    """
    Defines a series of key combinations that, when pressed, simulate the
    pressing of a list of key combinations.
    """
    for shortcut, combinations in combinations_by_shortcut.items():
        register_hotkey(shortcut, lambda: map(send, combinations))

def setup_turbo(hotkey):
    """
    Defines a hotkey that, when pressed in combination to another key,
    "turboes" that other key, making it send press and release events when held
    down.

    When the hotkey+key combination is pressed again, it clears the turbo
    status for that key.
    """
    turboed = set()
    hotkey_keycode = name_to_keycode(hotkey)

    def handler(event):
        if (is_pressed(hotkey)
            and event.keycode != hotkey_keycode
            and event.event_type == KEY_DOWN):

            if event.keycode in turboed:
                turboed.remove(event.keycode)
            else:
                turboed.add(event.keycode)

        elif event.keycode in turboed and event.event_type == KEY_DOWN:
            release_keycode(event.keycode)
            sleep(0.01)

    add_handler(handler)

def setup_macro(start_recording_hotkey='F7',
                stop_recording_hotkey='F8',
                playback_hotkey='F9',
                playback_speed=1.0):
    """
    Records all keyboard events a user generates and plays back when requested,
    at a given speed factor. If the speed factor is 0.0, it'll be played back
    instantly.

    Recording actions overwrites the previous actions and a recorded set of
    actions can be played back any number of times.
    """

    hotkey_keycodes = map(name_to_keycode, [start_recording_hotkey,
                                            stop_recording_hotkey,
                                            playback_hotkey
                                           ])

    actions = []
    def recording_handler(event):
        if event.keycode not in hotkey_keycodes:
            actions.append(event)

    def start_recording():
        actions[:] = []
        add_handler(recording_handler)

    def stop_recording():
        remove_handler(recording_handler)

    def playback():
        if playback_speed > 0:
            play(list(actions), playback_speed)
        else:
            send_keys(action.keycode for action in actions
                      if action.event_type == KEY_DOWN)

    register_hotkey(start_recording_hotkey, start_recording)
    register_hotkey(stop_recording_hotkey, stop_recording)
    register_hotkey(playback_hotkey, playback)

if __name__ == '__main__':
    from ConfigParser import ConfigParser
    config = ConfigParser()
    config.read('config.ini')

    turbo_hotkey = config.get('Hotkeys', 'turbo')
    start_recording = config.get('Hotkeys', 'start_recording')
    stop_recording = config.get('Hotkeys', 'stop_recording')
    playback = config.get('Hotkeys', 'playback')

    speed = float(config.get('General', 'playback_speed'))

    text_shortcuts = dict(config.items('TextShortcuts'))
    shortcuts = {key: combinations.split(',') for key, combinations in
                 config.items('CombinationShortcuts')}

    setup_text_shortcuts(text_shortcuts)
    setup_shortcuts(shortcuts)
    setup_turbo(turbo_hotkey)
    setup_macro(start_recording, stop_recording, playback, playback_speed=speed)
    raw_input()
