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
	attr_key = "name"
	res_notfound_val = ""

	tree = ET.parse(resdir + resfile_string)
	root = tree.getroot()

	for child in root:
		# if resource is found
		if child.attrib[attr_key] == resId:
			return child.text

	return res_notfound_val


"""
get resource dimension of name param
"""
def get_dimen(resId):
	attr_key = "name"
	res_notfound_val = None

	tree = ET.parse(resdir + resfile_dimen)
	root = tree.getroot()

	for child in root:
		# if resource is found
		if child.attrib[attr_key] == resId:
			return int(child.text)

	return res_notfound_val


"""
get filepath of image of name param
"""
def get_imagesrc(resId):
	attr_key = "name"
	res_notfound_val = None

	tree = ET.parse(resdir + resfile_img)
	root = tree.getroot()

	for child in root:
		# if resource is found
		if child.attrib[attr_key] == resId:

			return resdir + root.attrib["rootdir"] + child.text

	return res_notfound_val
