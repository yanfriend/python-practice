import luigi
class EnumParameter(luigi.Parameter):
    def __init__(self, enum_cls, *args, **kwargs):
        super(EnumParameter, self).__init__(*args, **kwargs)
        self.enum_cls = enum_cls

    def parse(self, x):
        return self.enum_cls(x)

    def serialize(self, x):
        return x.value
