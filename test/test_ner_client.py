import unittest
from ner_client import NamedEntityClient
from test_doubles import NerModelTestDouble

class TestNerClient(unittest.TestCase):

    # { ents: [{...}],
    #   html: "<span>..."}

    def test_get_ents_returns_dictionary_given_empty_string_causes_empty_spacy_doc_ents(self):
        model = NerModelTestDouble('eng')
        model.returns_doc_ents([]) # Empty doc_ents because of emptye string
        ner =  NamedEntityClient(model)
        ents = ner.get_ents("") # Empty string
        self.assertIsInstance(ents, dict)

    def test_get_ents_returns_dictionary_given_non_empty_string_causes_empty_space_doc_ents(self):
        model = NerModelTestDouble('eng')
        model.returns_doc_ents([])
        ner = NamedEntityClient(model)
        ents = ner.get_ents("Madison is a city in Wisconsin ")
        self.assertIsInstance(ents, dict)

    # CARDINAL, DATE, EVENT, FAC, GPE, LANGUAGE, LAW, LOC, MONEY, NORP, ORDINAL, ORG, PERCENT, PERSON, PRODUCT, QUANTITY, TIME, WORK_OF_ART
    # >>> spacy.explain("GPE") : To get an explanation of the various labels used your model, https://spacy.io/api/top-level#spacy.explain
    def test_get_ents_given_SPACY_PERSON_is_returned_serializes_to_Person(self):
        model = NerModelTestDouble('eng')
        model.returns_doc_ents([
            {"text": "Madison", "label_": "PERSON"},
            ])
        ner = NamedEntityClient(model)
        ents = ner.get_ents("Madison is a city in Wisconsin")
        expected_result = {
                'ents': [
                    {'ent': "Madison", 'label':"Person"},
                ],
                'html': ""
        }
        self.assertDictEqual(ents, expected_result, msg="Didn't get expected result")

    def test_get_ents_given_SPACY_GPE_is_returned_serializes_to_Location(self):
        # GPE: GeoPolictical Entity --> (Country, City, State)
        model = NerModelTestDouble('eng')
        model.returns_doc_ents([{"text": "Cameroon", "label_": "GPE"}])
        ner = NamedEntityClient(model)
        ents = ner.get_ents("Cameroon is a beautiful Country")
        expected_result = {'ents':[{'ent': "Cameroon", 'label': "Location"}], 'html': ""}
        self.assertDictEqual(ents, expected_result)

    def test_get_ents_given_SPACY_LOC_is_returned_serializes_to_Location(self):
        # LOC: Non GPE Locations --> (Mountains, water bodies)
        model = NerModelTestDouble('eng')
        model.returns_doc_ents([{"text": "Mountain", "label_": "LOC"}])
        ner = NamedEntityClient(model)
        ents = ner.get_ents("I live on a Mountain range")
        expected_result = {'ents':[{'ent': "Mountain", 'label': "Location"}], 'html': ""}
        self.assertDictEqual(ents, expected_result)

    def test_get_ents_given_SPACY_NORP_is_returned_serializes_to_Group(self):
        # NORP: Nationalities or Political Group
        model = NerModelTestDouble('eng')
        model.returns_doc_ents([{"text": "Muslim", "label_": "NORP"}])
        ner = NamedEntityClient(model)
        ents = ner.get_ents("I have a Muslim friend")
        expected_result = {'ents':[{'ent': "Muslim", 'label': "Group"}], 'html': ""}
        self.assertDictEqual(ents, expected_result)

    def test_get_ents_given_SPACY_ORG_is_returned_serializes_to_Organisation(self):
        # ORG: 'Companies, Agencies, Institutions'
        model = NerModelTestDouble('eng')
        model.returns_doc_ents([{"text": "OrangeCM", "label_": "ORG"}])
        ner = NamedEntityClient(model)
        ents = ner.get_ents("OrangeCM is an ISP")
        expected_result = {'ents':[{'ent': "OrangeCM", 'label': "Organisation"}], 'html': ""}
        self.assertDictEqual(ents, expected_result)

    def test_get_ents_given_SPACY_MONEY_is_returned_serializes_to_Money(self):
        # ORG: 'Companies, Agencies, Institutions'
        model = NerModelTestDouble('eng')
        # "Dollars"/"dollars"/"cents"/"USD" all works with the real model
        model.returns_doc_ents([{"text": "Dollars", "label_": "MONEY"}])
        ner = NamedEntityClient(model)
        ents = ner.get_ents("I have 5 Dollars")
        expected_result = {'ents':[{'ent': "Dollars", 'label': "Money"}], 'html': ""}
        self.assertDictEqual(ents, expected_result)

    def test_get_ents_given_SPACY_PRODUCT_is_returned_serializes_to_Product(self):
        # ORG: 'Companies, Agencies, Institutions'
        model = NerModelTestDouble('eng')
        model.returns_doc_ents([{"text": "cake", "label_": "PRODUCT"}])
        ner = NamedEntityClient(model)
        ents = ner.get_ents("Please buy me some cake")
        expected_result = {'ents':[{'ent': "cake", 'label': "Product"}], 'html': ""}
        self.assertDictEqual(ents, expected_result)

    def test_get_ents_given_SPACY_CARDINAL_is_returned_serializes_to_Cardinal(self):
        # ORG: 'Companies, Agencies, Institutions'
        model = NerModelTestDouble('eng')
        model.returns_doc_ents([{"text": "5", "label_": "CARDINAL"}])
        ner = NamedEntityClient(model)
        ents = ner.get_ents("5 cakes")
        expected_result = {'ents':[{'ent': "5", 'label': "Cardinal"}], 'html': ""}
        self.assertDictEqual(ents, expected_result)

    def test_get_ents_given_SPACY_TIME_is_returned_serializes_to_Time(self):
        # ORG: 'Companies, Agencies, Institutions'
        model = NerModelTestDouble('eng')
        model.returns_doc_ents([{"text": "5 pm", "label_": "TIME"}])
        ner = NamedEntityClient(model)
        ents = ner.get_ents("it is 5 pm")
        expected_result = {'ents':[{'ent': "5 pm", 'label': "Time"}], 'html': ""}
        self.assertDictEqual(ents, expected_result)
    
    def test_get_ents_given_multiple_spacy_ents_is_fed_to_model_serializes_to_multiple_ents(self):
        model = NerModelTestDouble('eng')
        model.returns_doc_ents([
            {"text": "France", "label_": "GPE"},
            {"text": "Pacific Ocean", "label_": "LOC"},
            {"text": "Burger", "label_": "PRODUCT"},
            {"text": "10 am", "label_": "TIME"}
        ])
        ner = NamedEntityClient(model)
        ents = ner.get_ents("")
        expected_result = {
            'ents':[
                {'ent': "France", 'label': "Location"},
                {'ent': "Pacific Ocean", 'label': "Location"},
                {'ent': "Burger", 'label': "Product"},
                {'ent': "10 am", 'label': "Time"}
            ],
            'html': ""
        }
        self.assertDictEqual(ents, expected_result)