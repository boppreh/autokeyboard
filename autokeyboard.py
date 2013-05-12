from keyboard import *

def setup_macro(start_recording_hotkey='F7',
                stop_recording_hotkey='F8',
                playback_hotkey='F9',
                playback_speed=1.0):

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
    setup_macro(playback_speed=0)
    raw_input()
