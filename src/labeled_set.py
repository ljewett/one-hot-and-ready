class LabeledSet(set):
    def __init__(self, label, *args, **kwargs):
        self.label = label
        super().__init__(*args, **kwargs)