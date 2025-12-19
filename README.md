# Project Zomboid Outfit XML Converter
A python script for clothing modders that can convert clothing.xml into a readable format so that changes can be made more easily and then converted back.

The script reads the guids and item names from fileGuidTable.xml and will also tell you if any items in the outfit xml are missing from fileGuidTable.

## Features
- Convert the guids in clothing.xml to item names and save it as clothing_readable.xml.

- Convert the item names in clothing_readable.xml to guids and save the changes to clothing.xml.

## Usage
- [Install Python](https://www.python.org/downloads/).
Make sure python is added to PATH in the installer.

- [Install lxml for Python](https://lxml.de/installation.html)

- Run one of the bat files and paste the file path of your mods media folder. This can also be used on the vanilla media folder.