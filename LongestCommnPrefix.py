# Will check all the words given in array, and for these words, whatever is common string in the starting of the words - that is common string as prefix for all the words - is
def longest_common_prefix(words):
    if not words:
        return ""

    prefix = words[0]
    for word in words[1:]:
        while not word.startswith(prefix):
            prefix = prefix[:-1]
            if not prefix:
                return ""
    return prefix

# Example usage
wordsList = [["flower", "flow", "flight"], ["", "empty", "emptiness"], ["train", "track", "trick"], ["hello", "world", "python"],["computer", "computation", "compact"], ["apple", "apricot", "apology"], ["banana", "band", "banner"],["dog", "deer", "dove"] ]
for k in wordsList:
    print(longest_common_prefix(k))
