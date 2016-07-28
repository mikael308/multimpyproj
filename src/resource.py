# 
# handling string resource data from xml file
# resourcefile is defined in var resourcefile
# to get string from resourcefile, use getString(resId) function
#
# author Mikael Holmbom
# ver 1.0

import xml.etree.ElementTree as ET

# path to resource data
resdir = "res/"
# resourcefiles containing data
resfile_string 	= "strings.xml"
resfile_dimen 	= "dimens.xml"
resfile_img		= "images.xml"

"""
get string from resource
param resId: resource id as of attribute name in resource file
returns textvalue from resource element, if resource not found, empty string is returned
"""
def get_string(resId):

	attrKey = "name"
	resNotFoundValue = ""

	tree = ET.parse(resdir + resfile_string)
	root = tree.getroot()

	for child in root:
		# if resource is found
		if child.attrib[attrKey] == resId:
			return child.text

	return resNotFoundValue

def get_dimen(resId):
	attrKey = "name"
	resNotFoundValue = None

	tree = ET.parse(resdir + resfile_dimen)
	root = tree.getroot()

	for child in root:
		# if resource is found
		if child.attrib[attrKey] == resId:
			return int(child.text)

	return resNotFoundValue

def getImageSrc(resId):
	attrKey = "name"
	resNotFoundValue = None

	tree = ET.parse(resdir + resfile_img)
	root = tree.getroot()

	for child in root:
		# if resource is found
		if child.attrib[attrKey] == resId:

			return resdir + root.attrib["rootdir"] + child.text

	return resNotFoundValue
