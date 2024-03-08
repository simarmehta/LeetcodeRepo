class Solution(object):
    def palindromePairs(self, words):
        def is_palindrome(check):
            return check == check[::-1]

        word_dict = {word: i for i, word in enumerate(words)}
        result = set()

        for i, word in enumerate(words):
            for j in range(len(word) + 1):
                prefix, suffix = word[:j], word[j:]
                reverse_prefix, reverse_suffix = prefix[::-1], suffix[::-1]

                if is_palindrome(prefix) and reverse_suffix in word_dict and word_dict[reverse_suffix] != i:
                    result.add((word_dict[reverse_suffix], i))

                
                if j > 0 and is_palindrome(suffix) and reverse_prefix in word_dict and word_dict[reverse_prefix] != i:
                    result.add((i, word_dict[reverse_prefix]))

        if "" in word_dict:
            empty_index = word_dict[""]
            for i, word in enumerate(words):
                if word != "" and is_palindrome(word):
                    result.add((empty_index, i))
                    result.add((i, empty_index))

        return list(result)
