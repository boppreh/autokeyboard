from keyboard import *

if __name__ == '__main__':
    actions = []

    def recording_handler(event):
        if event.name not in ['f7', 'f8', 'f9']:
            actions.append(event)

    def start_recording():
        actions[:] = []
        print 'Recording...'
        add_handler(recording_handler)

    def stop_recording():
        print 'Recorded {} actions.'.format(len(actions))
        remove_handler(recording_handler)

    def playback():
        print 'Playing {} actions.'.format(len(actions))
        play(list(actions))
        print 'Finished playing.'

    register_hotkey('F7', start_recording)
    register_hotkey('F8', stop_recording)
    register_hotkey('F9', playback)
    raw_input()
