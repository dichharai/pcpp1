import xml.etree.ElementTree as ET


class TemperatureConverter:
    def convert_celsius_to_fahreinheit(c: float):
        return (9/5 * c) + 32

class ForecastXmlParser:
    def parse(self):
        tree = ET.parse("forecast.xml")
        root = tree.getroot()

        for item in root.findall('item'):
            # cel_t = item[1].text
            day = item.find("day").text
            cel_t = item.find('temperature_in_celsius').text
            fah_t = TemperatureConverter.convert_celsius_to_fahreinheit(float(cel_t))
            print(f'{day}: {cel_t} Celsius, {round(fah_t, 1)} Fahrenheit')

fxp = ForecastXmlParser()
fxp.parse()