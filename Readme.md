# TallNotes

## Description

Tall Notes is a group of scripts that can generate a json document containing all chords, scales and tonalities based on
the 12 notes of the occidental system.12

## Use

Just execute the script TallNotes.py to obtain the TallNotes.json file.

~~~
python TallNotes
~~~

## TallNotes.json

The structure of the generated file is the following:

~~~~
{
    chords:{chord_a:[note_a, ..., note_b], ...}
    scales:{scale_a:[note_c, ..., note_d], ...}
    tonalities:{tonality_a:[chord_b, ..., chord_c], ...}
}
~~~~
