import collections


class TrieNode(object):
    def __init__(self):
        self.children=collections.defaultdict(TrieNode)
        self.is_word=False


def build_tree(strings):
    trie=TrieNode()
    trie.is_word=True
    for word in strings:
        curr=trie
        for ch in word:
            curr=curr.children[ch]
        curr.is_word=True
    return trie


def find_longest(trie):
    curr=trie
    if not curr.is_word: return 0, ''

    ret=0; ret_path=''
    for ch in curr.children:
        max_chd, path = find_longest(curr.children[ch])
        if max_chd>ret:
            ret=max_chd
            ret_path=ch+path
    return ret+1, ret_path


def longest_con_string(strings):
    trie=build_tree(strings)
    return find_longest(trie)



strings=[
    'a',
    'b',
    'ab',
    'abc',
    'abdf'
    'bdfe',
]

print longest_con_string(strings)[1]  # abc
