import reg
@reg.dispatch('obj')
def title(obj):
   return "we don't know the title"

class TitledReport(object):
   def __init__(self, title):
      self.title = title

class LabeledReport(object):
   def __init__(self, label):
      self.label = label

def titled_report_title(obj):
    return obj.title

def labeled_report_title(obj):
    return obj.label

registry = reg.Registry()
registry.register_function(
    title, titled_report_title, obj=TitledReport)
registry.register_function(
    title, labeled_report_title, obj=LabeledReport)

from reg import implicit
implicit.initialize(registry.lookup())


titled = TitledReport('This is a report')
labeled = LabeledReport('This is also a report')
print title(titled)
print title(labeled)

