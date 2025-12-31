
# Project Zomboid Outfit XML Converter
A python script for clothing modders that makes editing zombie outfits easier.

## Features
- Convert_To_Readable.bat saves a copy of clothing.xml with item guids replaced by item names as clothing_readable.xml
  
- Convert_To_ClothingXML.bat updates clothing.xml with any changes made to clothing_readable.xml

- Get_Vanilla_Items.bat gets every vanilla item found in clothing_readable.xml and saves them to a new file so they can be pasted into your mod's fileGuidTable.
  

- The scripts read from the fileGuidTable.xml in your mod folder to match the names and guids of each item

- The script will also let you know if any items are missing from your fileGuidTable.xml


## Usage
- [Install Python](https://www.python.org/downloads/).
Make sure python is added to PATH in the installer.

- [Install lxml for Python](https://lxml.de/installation.html)

- Run Convert_To_Readable.bat and paste the file path of your mods media folder.

- Edit the outfits in clothing_readable.xml

- Run Get_Vanilla_Items.bat so you can add any vanilla items you've used into fileGuidTable.xml. 
Items used in your outfits that aren't in your mod's fileGuidTable.xml will not appear in-game.
  
- Run Convert_To_ClothingXML.bat and paste the file path of your mods media folder to save your changes back into clothing.xml to test your outfits in-game
