from enum import Enum

def get_value(line, enum_field):
        return None if line.get(enum_field.value, '') is None else line.get(enum_field.value, '').strip() or None


line = {'aa':'avalue', 'bb':'bvalue', 'cc':None, 'ee':'' }

class color(Enum):
    aa='aa'
    bb='bb'
    cc='cc'
    dd='dd'
    ee='ee'

print get_value(line, color.aa)
print get_value(line, color.bb)
print get_value(line, color.cc)
print get_value(line, color.dd)
print get_value(line, color.ee)


