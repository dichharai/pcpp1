import xml.etree.ElementTree


hkeys = ["COMPANY", "LAST", "CHANGE", "MIN", "MAX"]
hwidth = [40, 10, 10, 7, 7]


def output_header():
    for (k, w) in zip(hkeys, hwidth):
        print(k.ljust(w), end=" ")
    print()
    print("-"*81)


def output_data(quote: xml.etree.ElementTree.Element):
    # print(quote.text, quote.attrib["last"], type(quote.attrib))
    att_dict = quote.attrib
    vals = [quote.text, att_dict["last"], att_dict["change"], att_dict["min"], att_dict["max"]]
    for (v, w) in zip(vals, hwidth):
        print(v.ljust(w), end=" ")
    print()

tree = xml.etree.ElementTree.parse("nyse.xml")
quotes = tree.getroot()
print(quotes, type(quotes))

output_header()
for quote in quotes.findall('quote'):
    output_data(quote)