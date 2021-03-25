import sys
from typing import Optional

from syllabifier import cmuparser3
from syllabifier.syllable3 import generate_syllables

cmu_dict = cmuparser3.CMUDictionary()


def generate(candidate: str) -> Optional[map]:
    phoneme_str = cmu_dict.get_first(candidate)
    if phoneme_str:
        return generate_syllables(phoneme_str)
    else:
        print("***" + candidate + " not in CMU dictionary, sorry, please try again...")
        return None


def num_syllables(candidate: str) -> Optional[int]:
    # print(f"{candidate}")
    syl_map = generate(candidate)
    if syl_map is not None:
        return len(syl_map)
    return None


if __name__ == "__main__":
    if len(sys.argv) > 1:
        words = sys.argv[1:]
        for word in words:
            syllable = generate(word.rstrip())
            n_syls = num_syllables(word.rstrip())
            if syllable:
                print(f"{word}: {n_syls} syllables: ", end='')
                for syll in syllable:
                    print(syll, end=' ')
                print()
    else:
        print(
            "Please input a word, or list of words (space-separated) as argument variables"
        )
        print("e.g. python3 syllable3.py linguist linguistics")
