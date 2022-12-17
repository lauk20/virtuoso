from pynput.keyboard import Key, Listener, Controller, KeyCode
keyboard = Controller();

"""
Player class to represent a piano Player!
"""
class Player:

    """
    Method to parse the notes into a list of chords/notes.

    Args:
        notes: The string containing the virtual piano notes.
    
    Returns:
        List of strings that represent individual chords/notes.
    """
    def parse_notes(self, notes):
        notes = notes.replace("|", "");
        chords = notes.split();
        print(chords);

        return chords;
    

    def on_press(key):
        #if (keyboard.KeyCode.from_char(key) )
        if (key == KeyCode.from_char(".")):
            print("Triggered");
            keyboard.type("wty");

    
    def listen(self):
        with Listener(on_press=on_press, on_release=on_release) as listener:
            listener.join();
    

    """
    Constructor for Player object.

    Args:
        notes: The string containing the virtual piano notes.
    """
    def __init__(self, notes):
        self.notes = self.parse_notes(notes);