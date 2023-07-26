import xml.etree.ElementTree as ET


root = ET.Element("shop")
tree = ET.ElementTree(root)

c1 = ET.SubElement(root, "category", {"name": "Vegan Products"})
p1 = ET.SubElement(c1, "product", {"name": "Good Morning Sunshine"})
t1 = ET.SubElement(p1, "type")
t1.text = "cereals"
pr1 = ET.SubElement(p1, "producer")
pr1.text = "OpenEDG Testing Service"
pri1 = ET.SubElement(p1, "price")
pri1.text = "9.90"
cu1 = ET.SubElement(p1, "currency")
cu1.text = "USD"

p2 = ET.SubElement(c1, "product", {"name": "Spaghetti Veganietto"})
t2 = ET.SubElement(p2, "type")
t2.text = "pasta"
pr2 = ET.SubElement(p2, "producer")
pr2.text = "Programmers Eat Pasta"
pri2 = ET.SubElement(p2, "price")
pri2.text = "15.49"
cu2 = ET.SubElement(p2, "currency")
cu2.text = "EUR"

p3 = ET.SubElement(c1, "product", {"name": "Fantastic Almond Mild"})
t3 = ET.SubElement(p3, "type")
t3.text = "beverages"
pr3 = ET.SubElement(p3, "producer")
pr3.text = "Drinks4Coders Inc."
pri3 = ET.SubElement(p3, "price")
pri3.text = "19.75"
cu3 = ET.SubElement(p3, "currency")
cu3.text = "USD" 

tree.write("vegan.xml", "UTF-8", True)

