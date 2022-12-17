from pynput.keyboard import Key, Listener, KeyCode
import pyautogui

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
        # making sure the string is spaced out properly
        notes = notes.replace("|", "");
        notes = notes.replace("[", " [");
        notes = notes.replace("]", "] ");

        # split the notes by spaces
        chords = notes.split();

        # cleaning the chords, since some notes are strung together like this "abcd" but should not be a chord
        result = [];
        for chord in chords:
            if ("[" in chord or "]" in chord):
                result.append(chord.replace("[", "").replace("]", ""));
            else:
                for c in chord:
                    result.append(c);

        return result;


    """
    Method to parse the file into list of chords/notes.
    Uses self.parse_notes method once file is read.

    Args:
        filename: Name of the file (or the relative path to it);
        
    Returns:
        List of strings that represent individual chords/notes.
    """
    def parse_file(self, filename):
        with open(filename) as f:
            return self.parse_notes(f.read());
    

    """
    Called when a key is pressed and plays the following note.

    Args:
        key: The key that was pressed
    
    Returns:
        False if self.current_note is pointing out of bounds or if Esc was pressed.
        None otherwise.
    """
    def on_press(self, key):
        if (self.current_note == -1 or self.current_note >= len(self.notes)): # if the pointer is out of bounds we end
            return False;
        
        if (key == KeyCode.from_char(".")): # if is the keybind then play the note/chord
            pyautogui.write(self.notes[self.current_note]);
            self.current_note = self.current_note + 1;
        elif (key == KeyCode.from_char("/")): # if is slash then we want to restart the song
            self.current_note = 0;
        elif (key == Key.esc): # we don't want to play anymore
            return False;


    """
    Method to start listening to keyboard inputs, using self.on_press as the on_press function.
    """
    def listen(self):
        # start listening using pynput
        with Listener(on_press=self.on_press) as listener:
            listener.join();
    

    """
    Constructor for Player object.

    Args:
        notes: The string containing the virtual piano notes.
    """
    def __init__(self, notes = None, filename = None):
        if (notes):
            self.notes = self.parse_notes(notes);
        elif (filename):
            self.notes = self.parse_file(filename);
        
        self.current_note = 0 if (len(self.notes) > 0) else -1;