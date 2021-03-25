# Syllabifier

Count the number of syllables in arbitrary English words

Adapted from [this repository](https://github.com/anthonysgevans/syllabify) with some major changes:

* Ported to Python 3 and rewrote much of the code in a more Pythonic style
* Made a few relatively minor corrections to the syllabification rules, following "English Words: A 
  Linguistic Introduction" by Heidi Harley (Blackwell Publishing).
* Removed ambisyllabicity rules for onset and coda

Please see Anthony Evans' README file for a detailed background to the project.


## Set up

* Requires [Python 3](https://www.python.org/downloads)
* Clone this repo. No further installation required.


## Usage

One word at a time:
```
python3 syllable3.py linguistics
```

Or several (space-separated):
```
python3 syllable3.py colourless green ideas
```

If using as a library, and you just need the syllable count of a word, use the `num_syllables(word: str)` function instead.

## Output

If the input word is found in the dictionary, a phonemic, syllabified transcript is returned. For example, for the word _linguistics_:
```
linguistics: 3 syllables: <o:L|n:IH|c:NG> <o:GW|n:IH|c:None> <o:ST|n:IH|c:KS>
```
Each syllable is made up of an 'o' onset, 'n' nucleus, and 'c' coda. Phonemes capitalized in [ARPAbet](http://en.wikipedia.org/wiki/ARPABET) 
format. In line with phonological theory, the nucleus must have content, whereas the onset and coda may be empty. 


## CMU Pronouncing Dictionary

`Syllabify` depends on the [CMU Pronouncing Dictionary](http://www.speech.cs.cmu.edu/cgi-bin/cmudict) of North 
American English word pronunciations. Version 0.7b was the current one at time of writing, but it throws a 
UnicodeDecodeError, so we're still using version 0.7a (amended to remove erroneous 'G' from SUGGEST and related words). 
Please see the dictionary download website to obtain the current version, add the `cmudict-N.nx(.phones|.symbols)*` 
files to the `CMU_dictionary` directory, remove the '.txt' suffixes, and update the line `VERSION = 'cmudict-n.nx'` 
in `cmuparser3.py`
