from enum import Enum

class CollectionsDisabledReason(Enum):
    deceased = 'deceased'
    fraud = 'fraud'
    scra = 'scra'
    bankruptcy = 'bankruptcy'
    failed_reassignment = 'failed_reassignment'
    other = 'other'
print [ t.value for t in CollectionsDisabledReason]

