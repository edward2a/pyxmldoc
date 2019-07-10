from xml.etree import ElementTree as et


class XmlDocument(object):

    def __init__(self):
        pass

    def load_file(self, f):
        self.source_data = et.parse(f)

    def xml_to_dict(self):
        self.xmldoc = {}

        # Get root and process it
        root = self.source_data.getroot()
        self.xmldoc = self.load_tree(root)

    @staticmethod
    def load_element(e):
        return {'attrs': e.attrib, 'children': [
            {c.tag: {'attrs': c.attrib}} for c in e.getchildren() ]}

    def load_tree(self, e):
        return {e.tag: {'attrs': e.attrib, 'children': [
            self.load_tree(c) for c in e.getchildren() ]}}
