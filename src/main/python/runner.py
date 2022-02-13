import winsound

from word_finder import WordFinder


def play_sound():
    duration = 2000
    freq = 440
    winsound.Beep(freq, duration)


def print_results(words):
    print("Found {} words!".format(len(words)))
    sorted_list = sorted(words, key=len, reverse=True)
    format_string = "{}|{}"
    list_with_lens = [format_string.format(word, str(len(word))) for word in sorted_list]
    print("Sorted words:\n{}".format(", ".join(list_with_lens)))
    play_sound()
    

filename = input("Filename for grid ([name].txt): ")
word_finder = WordFinder(filename)
found_words = word_finder.generate_word_list()
print_results(found_words)
