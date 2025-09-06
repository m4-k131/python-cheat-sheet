import xmltodict

xml_path = ""
with open(xml_path, "r", encoding="utf-8") as f:
    xml_data = f.read()
xml_dict = xmltodict.parse(xml_data)