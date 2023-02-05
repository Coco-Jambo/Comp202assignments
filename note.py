#Réda Alidrissi-Omari
#261068776

import musicalbeeps, doctest

class Note:
    """ Represents a Note
    
    Attributes: duration, pitch, octave, accidental
    """
    
    OCTAVE_MIN = 1
    OCTAVE_MAX = 7
    
    def __init__(self, duration, pitch, octave, accidental):
        """(float, str, int, str)->Note
        Creates a new Note with the given duration, pitch, octave and accidental.
        Raises an AssertionError if the duration is not a positive float,
        if pitch is not a letter from A to G or R, if octave is not a positive int between 1 and 7,
        or if accidental is not a string that is either naturtal, sharp, or flat.

        >>> note1 = Note(0.35, "E",  4,  "NATURAL")
        >>> note1.pitch
        'E'
        >>> note2 = Note(0.35, "F",  4,  "sharp")
        >>> note2.duration
        0.35
        >>> note3 = Note(1.0, "B",  3,  "flat")
        >>> note3.accidental
        'flat'
        """
        
        if type(duration) == float and duration > 0:
            self.duration = duration
        else:
            raise AssertionError("The duration must be a positive float")
        
        if type(pitch) == str and pitch in ['A','B','C','D','E','F','G','R']:
            self.pitch = pitch
        else:
            raise AssertionError("The pitch must be a single letter from A to G or R")
        
        if type(octave) == int and Note.OCTAVE_MIN <= octave <= Note.OCTAVE_MAX:
            self.octave = octave
        else:
            raise AssertionError("The octave should be an integer between 1 and 7")
        
        if type(accidental) == str and accidental.lower() in ['natural','sharp','flat']:
            self.accidental = accidental.lower()
        else:
            raise AssertionError("The accidental value should be either natural, sharp, or flat.")
            
    def __str__(self):
        """()->str
        Returns a string that represents the Note object created.
        
        >>> note1 = Note(0.35, "E",  4,  "NATURAL")
        >>> print(note1)
        0.35 E 4 natural
        
        >>> note2 = Note(0.35, "F",  4,  "sharp")
        >>> print(note2)
        0.35 F 4 sharp
        
        >>> note3 = Note(1.0, "B",  3,  "flat")
        >>> print(note3)
        1.0 B 3 flat
        """
        return str(self.duration) + " " + self.pitch + " " + str(self.octave) + " " + self.accidental
    
    
    def play(self, player):
        """(Player)->None
        Plays a note using the play_note method from the musicalbeeps module
        """
        if self.pitch == "R":
            pitch_and_octave = "pause"
        else:
            pitch_and_octave = self.pitch + str(self.octave)
        
            if self.accidental == "sharp":
                pitch_and_octave+= "#"
            elif self.accidental == "sharp":
                pitch_and_octave+= "b"
        
        player.play_note(pitch_and_octave, self.duration)
            
if __name__ == '__main__':
    doctest.testmod()    
            
            
    