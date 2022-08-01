import xmltodict


def convert_xml_to_dict(data_as_xml):
    data_as_dict = xmltodict.parse(data_as_xml)

    return data_as_dict
