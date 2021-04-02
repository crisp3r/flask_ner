class NerModelTestDouble():
    """
    Test Double class for spacy NER model
    """
    def __init__(self, model):
        self.model = model

    def returns_doc_ents(self, ents):
        # This is the ents we inject into the
        self.ents = ents

    def __call__(self, sentence):
        # when called it should return a Doc Test Double
        # just like the real spacy that returns a Doc object
        return DocTestDouble(sentence, self.ents)



class DocTestDouble():
    def __init__(self, sentence, ents):
        self.sent = sentence
        self.ents = [SpanTestDouble(ent.get('text'), ent.get('label_')) for ent in ents]


class SpanTestDouble():
    def __init__(self, text, label_):
        self.text = text
        self.label_ = label_
