from Player import Player
import sys

"""
Main entry into program.
Run by using: python main.py [filename].
Or by directing modifying the code:
    Player("abcde") will take in "abcde" as the notes.
    Player(filename = "./song_name.txt") will take in "./song_name.txt" as the file.
"""
def main():
    if (len(sys.argv) >= 2):
        player = Player(filename = sys.argv[1]);
        player.listen();
    else:
        print("Usage: python main.py <filename>");

if __name__ == "__main__":
    main();