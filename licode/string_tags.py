def string_tags(line, tags):
    for k, v in tags.items():
        lower_line = line.lower()
        end = len(lower_line)
        while lower_line.rfind(k.lower(), 0, end) != -1:
            ind = lower_line.rfind(k.lower(), 0, end)
            line = line[:ind + len(k)] + '[' + v + ']' + line[ind + len(k):]
            # print line
            end = ind
    return line


print string_tags("I love airbnb, Airbnb is awesome. Bay area is a great place! I love to live at the bay area.",
                  {"airbnb": "company", "bay Area": "place"}
                  )
# I love airbnb[company], Airbnb[company] is awesome.
# Bay area[place] is a great place! I love to live at the bay area[place]."
