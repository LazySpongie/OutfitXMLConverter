# Project Zomboid Outfit XML Converter
A python script for clothing modders that makes editing zombie outfits easier.

## Features
- Convert_To_Readable.bat saves a copy of clothing.xml with item guids replaced by item names as clothing_readable.xml
  
- Convert_To_ClothingXML.bat updates clothing.xml with any changes made to clothing_readable.xml
  
- The script reads from the fileGuidTable.xml in your mod folder to match the names and guids of each item

- The script will also let you know if any items in the outfits file are missing from your mods fileGuidTable.xml

## Usage
- [Install Python](https://www.python.org/downloads/).
Make sure python is added to PATH in the installer.

- [Install lxml for Python](https://lxml.de/installation.html)

- Run one of the bat files and paste the file path of your mods media folder. This can also be used on the vanilla media folder.
