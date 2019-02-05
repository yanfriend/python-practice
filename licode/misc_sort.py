def misc_sort(words):
    def sort_func(w):
        for i, ch in enumerate(w):
            if ch.isdigit():
                break
        return (w[:i], int(w[i:]))

    return sorted(words, key=sort_func)


print misc_sort(['aaa100', 'aaa2', 'b10'])  # should be aaa2, aaa100, b10

# this is q from Uber
