# -*- coding: utf-8 -*-
"""
Deletes metadata from Jupyter Notebooks

@author: matze
"""
fname='cryo_project.ipynb'

with open(fname, 'r') as file :
  texta = file.read()

#texta=r'''"cell_type": "markdown",
#   "metadata": {ddfff},
#   "source": [
#    "<font color='red'>TO DO:</font> \n",
#    "\n",
#    "- GENERAL INTRO (what is this document, which data did we use, who did what) -> **Alex**\n",
#    "- connect paragra'''
pos = 0
foundpos = 0
openBr = 0 # count open braces

while foundpos >-1:
    openBr = 0
    foundpos = texta.find( '"metadata": ',pos)
    pos = foundpos + 12
    if pos<12:
        break
   # print(texta[pos])
    start=pos
    result = ""
    while foundpos > -1 and openBr >= 0:
        pos = pos + 1
        if texta[pos] == "{":
            openBr = openBr + 1
        if texta[pos] == "}":
            openBr = openBr - 1
        result = result + texta[pos]
    if "mimetype" in result:
        break
    textl=list(texta)
    textl[start:pos+1]=['{','}']
    texta="".join(textl)
file = open(fname, "w")
file.write(texta)
file.close()

