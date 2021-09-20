#import docx2txt
from transpose_functions import *


def determine_key(raw_text):
    text = raw_text.splitlines()

    total_chords = []

    for line in text:
        #determine whether the line is lyric or chord
        if chord_line(line):

            #find the chords in a line
            chords = line.split()
            total_chords = total_chords + chords


    return infer_key(total_chords)



def transpose(raw_text, num_steps, sharp):
    """if reading chord sheet from a Word Doc
    filename = "test_songsheet.docx"
    raw_text = docx2txt.process(filename)
    """

    text = raw_text.splitlines()
    new_text = u""

    for line in text:
        #determine whether the line is lyric or chord
        if chord_line(line):

            #find the chords in a line
            chords = line.split()

            #replace chords with the right chords
            for chord in chords:

                new_chord = transpose_chord(chord, num_steps, sharp)
                line = line.replace(chord, new_chord, 1)
                print("line: ", line)

            #once done replacing in line, change all back to uppercase
            line = line.upper()

            #manually correct any musical notations that were changed, minors or flats
            line = line.replace("M","m")
            line = line.replace("AB","Ab")
            line = line.replace("BB","Bb")
            line = line.replace("DB","Db")
            line = line.replace("EB","Eb")
            line = line.replace("GB","Gb")




        new_text = new_text + line + "\n"

    return new_text
