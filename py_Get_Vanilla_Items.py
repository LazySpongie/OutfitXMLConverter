from lxml import etree
import sys

def trimItemName(str):
    newstr = str
    newstr = newstr.replace("media/clothing/clothingItems/", "")
    newstr = newstr.replace(".xml", "")
    return newstr


def getGUIDS(xmlFile):
    items = { }
    
    with open(xmlFile, encoding="utf8") as f:
        tree = etree.parse(f)
        root = tree.getroot()

    for file in root:
        name = ""
        guid = ""
        for elem in file:
            if elem.tag == "path":
                name = elem.text
            if elem.tag == "guid":
                guid = elem.text
        if name != "":
            items[name] = guid
        # print(name + " " + guid)

    return items


def GetVanillaItems(filepath, vanillaPath):
    items = getGUIDS(vanillaPath + "/fileGuidTable.xml")

    readXML = filepath + "/clothing/clothing_readable.xml"

    with open(readXML, encoding="utf8") as f:
        tree = etree.parse(f)
        root = tree.getroot()

    foundItems = []
    for elem in root.getiterator():
        try:
            if elem.tag == "itemGUID":
                
                path = "media/clothing/clothingItems/" + elem.text + ".xml"
                exists = items.get(path, "") != ""

                if exists:
                    foundItems.append(path)

        except AttributeError:
            pass


    newRoot = etree.Element("fileGuidTable")

    newTree = etree.ElementTree(newRoot)

    for item in foundItems:
        file = etree.Element("files")
        path = etree.Element("path")
        guid = etree.Element("guid")

        newRoot.append(file)
        file.append(path)
        file.append(guid)

        path.text = item
        guid.text = items.get(item, "")

    writeXML = filepath + "/fileGuidTable_VANILLAITEMS.xml"

    newTree.write(writeXML, xml_declaration=True, method='xml', encoding="utf8", pretty_print=True)

    print("")
    print("Created " + writeXML)
    print("")
    print("Paste the items into your fileGuidTable")


path = input("Enter the file path to your mod's media folder: \n")
vanillaPath = input("Enter the file path to the vanilla media folder: \n")
GetVanillaItems(path, vanillaPath)
