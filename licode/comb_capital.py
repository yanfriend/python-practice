def perm_comb_letters(word):
    word_letters = list(word)
    ans = []

    def helper(index, path):
        if index == len(word_letters): ans.append(path); return

        word_letters[index] = word_letters[index].upper()
        helper(index + 1, ''.join(word_letters))
        word_letters[index] = word_letters[index].lower()
        helper(index + 1, ''.join(word_letters))

    helper(0, '')
    return ans


print perm_comb_letters('ac')

print perm_comb_letters('abc')
