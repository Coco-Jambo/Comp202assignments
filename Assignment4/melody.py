#Réda Alidrissi-Omari
#261068776

import musicalbeeps, doctest
from note import Note

class Melody:
    """Represents a Melody
    
    Attributes: title, author, notes
    """
    
    def __init__(self, filename):
        """(str)->Melody
        Creates a new Note by opening the file with the name filename, with attributes title which is the first line of the file,
        author which is the second, and the rest are notes which are added to the notes attribute.
        
        >>> happy_birthday = Melody("birthday.txt")
        >>> len(happy_birthday.notes)
        25
        >>> print(happy_birthday.notes[5])
        1.0 F 4 sharp
        
        >>> fur_elise = Melody("fur_elise.txt")
        >>> len(fur_elise.notes)
        165
        >>> print(fur_elise.notes[0])
        0.15 E 5 natural
        
        >>> tetris = Melody("tetris.txt")
        >>> len(tetris.notes)
        40
        >>> print(tetris.notes[0])
        0.5 E 5 natural
        """
        song = open(filename, "r")
        song_content = song.read()
        song.close()
        
        song_content_separated = song_content.split("\n")
        
        self.title = song_content_separated[0]
        self.author = song_content_separated[1]
        
        song_notes = song_content_separated[2:]
        notes_list = []
        repeated_notes_list = []
        true_count = 0
        for note in song_notes:
            attributes_list = note.split()
            if attributes_list[1] == "R":
                if attributes_list[2] == "true" and true_count ==0:
                    note_object = Note(float(attributes_list[0]), attributes_list[1], 1, "natural")
                    notes_list.append(note_object)
                    repeated_note = Note(float(attributes_list[0]), attributes_list[1], 1, "natural")
                    repeated_notes_list.append(repeated_note)
                    true_count=1
                elif attributes_list[2] == "true" and true_count ==1:
                    note_object = Note(float(attributes_list[0]), attributes_list[1], 1, "natural")
                    notes_list.append(note_object)
                    repeated_note = Note(float(attributes_list[0]), attributes_list[1], 1, "natural")
                    repeated_notes_list.append(repeated_note)
                    for repeated_note in repeated_notes_list:
                        notes_list.append(repeated_note)
                    true_count=0
                    repeated_notes_list = []
                else:
                    note_object = Note(float(attributes_list[0]), attributes_list[1], 1, "natural")
                    notes_list.append(note_object)
                    if true_count == 1:
                        repeated_note = Note(float(attributes_list[0]), attributes_list[1], 1, "natural")
                        repeated_notes_list.append(repeated_note)
            else:
                if attributes_list[4] == "true" and true_count ==0:
                    note_object = Note(float(attributes_list[0]), attributes_list[1], int(attributes_list[2]), attributes_list[3])
                    notes_list.append(note_object)
                    repeated_note = Note(float(attributes_list[0]), attributes_list[1], int(attributes_list[2]), attributes_list[3])
                    repeated_notes_list.append(repeated_note)
                    true_count=1
                elif attributes_list[4] == "true" and true_count ==1:
                    note_object = Note(float(attributes_list[0]), attributes_list[1], int(attributes_list[2]), attributes_list[3])
                    notes_list.append(note_object)
                    repeated_note = Note(float(attributes_list[0]), attributes_list[1], int(attributes_list[2]), attributes_list[3])
                    repeated_notes_list.append(repeated_note)
                    for repeated_note in repeated_notes_list:
                        notes_list.append(repeated_note)
                    true_count=0
                    repeated_notes_list = []
                else:
                    note_object = Note(float(attributes_list[0]), attributes_list[1], int(attributes_list[2]), attributes_list[3])
                    notes_list.append(note_object)
                    if true_count == 1:
                        repeated_note = Note(float(attributes_list[0]), attributes_list[1], int(attributes_list[2]), attributes_list[3])
                        repeated_notes_list.append(repeated_note)
        
        self.notes = notes_list
    
    def __str__(self):
        """()->str
        Returns a string that represents the Melody object created.
        
        >>> melody = Melody("birthday.txt")
        >>> print(melody)
        Title: Happy Birthday
        Author: Patty and Mildred J. Hill
        Note list: 
        0.25 D 4 natural
        0.25 D 4 natural
        0.5 E 4 natural
        0.5 D 4 natural
        0.5 G 4 natural
        1.0 F 4 sharp
        0.25 D 4 natural
        0.25 D 4 natural
        0.5 E 4 natural
        0.5 D 4 natural
        0.5 A 4 natural
        1.0 G 4 natural
        0.25 D 4 natural
        0.25 D 4 natural
        0.5 D 5 natural
        0.5 B 4 natural
        0.5 G 4 natural
        0.5 F 4 sharp
        1.0 E 4 natural
        0.25 C 5 natural
        0.25 C 5 natural
        0.5 B 4 natural
        0.5 G 4 natural
        0.5 A 4 natural
        1.5 G 4 natural

        >>> melody = Melody("hotcrossbuns.txt")
        >>> print(melody)
        Title: Hot Cross Buns
        Author: Traditional
        Note list: 
        0.5 B 4 natural
        0.5 A 4 natural
        1.0 G 4 natural
        0.5 B 4 natural
        0.5 A 4 natural
        1.0 G 4 natural
        0.25 G 4 natural
        0.25 G 4 natural
        0.25 G 4 natural
        0.25 G 4 natural
        0.25 A 4 natural
        0.25 A 4 natural
        0.25 A 4 natural
        0.25 A 4 natural
        0.5 B 4 natural
        0.5 A 4 natural
        1.0 G 4 natural

        >>> tetris = Melody("tetris.txt")
        >>> print(tetris)
        Title: Tetris
        Author: Nikolay Nekrasov, Hirokazu Tanaka
        Note list: 
        0.5 E 5 natural
        0.25 B 4 natural
        0.25 C 5 natural
        0.5 D 5 natural
        0.25 C 5 natural
        0.25 B 4 natural
        0.5 A 4 natural
        0.25 A 4 natural
        0.25 C 5 natural
        0.5 E 5 natural
        0.25 D 5 natural
        0.25 C 5 natural
        0.75 B 4 natural
        0.25 C 5 natural
        0.5 D 5 natural
        0.5 E 5 natural
        0.5 C 5 natural
        0.5 A 4 natural
        0.25 A 4 natural
        0.25 A 4 natural
        0.25 B 4 natural
        0.25 C 5 natural
        0.75 D 5 natural
        0.25 F 5 natural
        0.5 A 5 natural
        0.25 G 5 natural
        0.25 F 5 natural
        0.75 E 5 natural
        0.25 C 5 natural
        0.5 E 5 natural
        0.25 D 5 natural
        0.25 C 5 natural
        0.5 B 4 natural
        0.25 B 4 natural
        0.25 C 5 natural
        0.5 D 5 natural
        0.5 E 5 natural
        0.5 C 5 natural
        0.5 A 4 natural
        0.5 A 4 natural
        """
        notes = ""
        for note in self.notes:
            notes += "\n" + str(note)
        return "Title: " + self.title + "\nAuthor: " + self.author + "\nNote list: " + notes
        
        
    def play(self, player):
        """(Player)->None
        Plays all the notes in the notes attribute using the play method from the Note class
        """
        
        for note in self.notes:
            note.play(player)
    
    def get_total_duration(self):
        """()->float
        Returns the total duration of the melody by adding up the durations of all the notes in the notes attribute.
        
        >>> happy_birthday = Melody("birthday.txt")
        >>> happy_birthday.get_total_duration()
        13.0
        
        >>> fur_elise = Melody("fur_elise.txt")
        >>> fur_elise.get_total_duration()
        25.8
        
        >>> tetris = Melody("tetris.txt")
        >>> tetris.get_total_duration()
        15.5
        """
        total = 0.0
        for note in self.notes:
            total += note.duration
        return round(total, 2)
        
    def lower_octave(self):
        """()->bool
        Returns True if all octave attributes of the notes in the notes attribute of the melody object are above 1
        and decreases all of them by 1. Returns False and does not modify the notes if otherwise.

        >>> happy_birthday = Melody("birthday.txt")
        >>> happy_birthday.lower_octave()
        True
        >>> happy_birthday.notes[5].octave
        3
       
        >>> fur_elise = Melody("fur_elise.txt")
        >>> fur_elise.lower_octave()
        True
        
        >>> tetris = Melody("tetris.txt")
        >>> tetris.lower_octave()
        True
        >>> tetris.lower_octave()
        True
        >>> tetris.lower_octave()
        True
        >>> tetris.lower_octave()
        False
        >>> print(tetris.notes[5])
        0.25 B 1 natural
        """
        is_lowerable = False
        for note in self.notes:
            if note.octave > Note.OCTAVE_MIN:
                note.octave -= 1
                is_lowerable = True
            else:
                is_lowerable = False
                break
            
        return is_lowerable
        
    def upper_octave(self):
        """()->bool
        Returns True if all octave attributes of the notes in the notes attribute of the melody object are below 7
        and increases all of them by 1. Returns False and does not modify the notes if otherwise.

        >>> happy_birthday = Melody("birthday.txt")
        >>> happy_birthday.upper_octave()
        True
        >>> happy_birthday.notes[5].octave
        5
       
        >>> fur_elise = Melody("fur_elise.txt")
        >>> fur_elise.upper_octave()
        True
        
        >>> tetris = Melody("tetris.txt")
        >>> tetris.upper_octave()
        True
        >>> tetris.upper_octave()
        True
        >>> tetris.upper_octave()
        False
        >>> print(tetris.notes[4])
        0.25 C 7 natural
        """
        is_increasable = False
        for note in self.notes:
            if note.octave < Note.OCTAVE_MAX:
                note.octave += 1
                is_increasable = True
            else:
                is_increasable = False
                break
            
        return is_increasable     
        
    def change_tempo(self, multiplier):
        """(float)->None
        Multiplies the duration of each note in the notes attribute by multiplier.
        
        >>> happy_birthday = Melody("birthday.txt")
        >>> happy_birthday.get_total_duration()
        13.0
        >>> happy_birthday.change_tempo(0.5)
        >>> happy_birthday.get_total_duration()
        6.5
        
        >>> tetris = Melody("tetris.txt")
        >>> tetris.get_total_duration()
        15.5
        >>> tetris.change_tempo(2)
        >>> tetris.get_total_duration()
        31.0
        
        >>> fur_elise = Melody("fur_elise.txt")
        >>> fur_elise.get_total_duration()
        25.8
        >>> fur_elise.change_tempo(0.5)
        >>> fur_elise.get_total_duration()
        12.9
        """
        for note in self.notes:
            note.duration *= multiplier
        
        
if __name__ == '__main__':
    doctest.testmod()        
        
        
