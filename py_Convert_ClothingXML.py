from lxml import etree
import sys

def trimItemName(str):
    newstr = str
    newstr = newstr.replace("media/clothing/clothingItems/", "")
    newstr = newstr.replace(".xml", "")
    return newstr

def createItemDictionaries(xmlFile):
    dictionaries = { 
        "names": {}, 
        "guids": {}, 
        }
    
    with open(xmlFile, encoding="utf8") as f:
        tree = etree.parse(f)
        root = tree.getroot()

    for item in root:
        name = ""
        guid = ""
        for elem in item:
            if elem.tag == "path":
                name = trimItemName(elem.text)
            if elem.tag == "guid":
                guid = elem.text
        if name != "":
            dictionaries["names"][name] = guid
            dictionaries["guids"][guid] = name

    return dictionaries


def ConvertClothingXML(path, toReadable):
    itemDicts = createItemDictionaries(path + "\\fileGuidTable.xml")

    filepath = path + "\\clothing\\"
    readXML = filepath + "clothing_readable.xml"
    if toReadable:
        readXML = filepath + "clothing.xml"

    with open(readXML, encoding="utf8") as f:
        tree = etree.parse(f)
        root = tree.getroot()

    missingelements = {}
    for elem in root.getiterator():
        try:
            if elem.tag == "itemGUID":
                newtext = ""

                dictKey = "names"
                if toReadable:
                    dictKey = "guids"

                newtext = itemDicts[dictKey].get(elem.text, "")
                if newtext != "":
                    elem.text = newtext
                else:
                    missingelements[elem.text] = True

        except AttributeError:
            pass

    writeXML = filepath + "clothing.xml"
    if toReadable:
        writeXML = filepath + "clothing_readable.xml"
    tree.write(writeXML, xml_declaration=True, method='xml', encoding="utf8")

    print("")
    for item in missingelements:
        print("Element missing from fileGuidTable.xml: " + item)

    print("")
    print("Created " + writeXML)

def CreateReadableFile():
    print("Create clothing_readable.xml from clothing.xml")
    path = input("Enter the file path to your mod's media folder:   ")
    ConvertClothingXML(path, True)

def CreateClothingXML():
    print("Create clothing.xml from clothing_readable.xml")
    path = input("Enter the file path to your mod's media folder:   ")
    ConvertClothingXML(path, False)


if len(sys.argv) > 1:
    readable = sys.argv[1] == "True"
    if readable:
        CreateReadableFile()
    else:
        CreateClothingXML()
else:
    print("No arguments received.")
    
# CreateReadableFile()