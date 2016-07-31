"""
handling string resource data from xml file
resourcefile is defined in var resourcefile
to get string from resourcefile, use getString(resId) function

author Mikael Holmbom
ver 1.0
"""
import xml.etree.ElementTree as ET


# path to resource data
resdir = "res/"
# resourcefiles containing data
resfile_string 	= "strings.xml"
resfile_dimen 	= "dimens.xml"
resfile_img		= "images.xml"
resfile_val		= "values.xml"


def get_string(resId):
	"""
	get string from resource
	:param resId: resource id as of attribute name in resource file
	:return: textvalue from resources, if resource not found: empty string is returned
	"""
	attr_key = "name"
	res_notfound_val = ""

	tree = ET.parse(resdir + resfile_string)
	root = tree.getroot()

	for child in root:
		# if resource is found
		if child.attrib[attr_key] == resId:
			return child.text

	return res_notfound_val


def get_dimen(resId):
	"""
	get resource dimension of name param
	:param resId: resource id as of attribute name in resource file
	:return: dimension from resources, if resource not found: None is returned
	"""
	attr_key = "name"
	res_notfound_val = None

	tree = ET.parse(resdir + resfile_dimen)
	root = tree.getroot()

	for child in root:
		# if resource is found
		if child.attrib[attr_key] == resId:
			return int(child.text)

	return res_notfound_val

def get_value(res_id):
	attr_key = "name"
	res_notfound_val = None

	tree = ET.parse(resdir + resfile_val)
	root = tree.getroot()

	for child in root:
		# if resource is found
		if child.attrib[attr_key] == res_id:
			return int(child.text)

	return res_notfound_val


def get_imagesrc(resId):
	"""
	get filepath of image of name param
	:param resId: resource id as of attribute name in resource file
	:return: image source from resources, if resource not found: None is returned
	"""
	attr_key = "name"
	res_notfound_val = None

	tree = ET.parse(resdir + resfile_img)
	root = tree.getroot()

	for child in root:
		# if resource is found
		if child.attrib[attr_key] == resId:

			return resdir + root.attrib["rootdir"] + child.text

	return res_notfound_val
