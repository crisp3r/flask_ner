class NamedEntityClient:
    def __init__(self, model):
        self.model = model

    def get_ents(self, sentence):
        doc = self.model(sentence)
        entities = [{'ent': ent.text, 'label': self.map_spacy_labels(ent.label_)} for ent in doc.ents]
        result = {
                'ents': entities,
                'html': ""
        }
        return result

    def map_spacy_labels(self, text):
        self.my_labels = {
                'PERSON': "Person",
                'GPE': "Location",
                'LOC': "Location",
                'ORG': "Organisation",
                'NORP': "Group",
                "CARDINAL": "Cardinal",
                "TIME": "Time",
                "PRODUCT": "Product",
                "MONEY": "Money"
        }
        return self.my_labels[text]
