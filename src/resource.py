"""
handling string resource data from xml file
resourcefile is defined in var resourcefile
to get string from resourcefile, use getString(resId) function

:author: Mikael Holmbom
:version: 1.0
"""
import xml.etree.ElementTree as ET


# path to resource data
resdir = "../res/"
# resourcefiles containing data
resfile_string 	= "strings.xml"
resfile_dimen 	= "dimens.xml"
resfile_img		= "images.xml"
resfile_val		= "values.xml"
resfile_sound	= "sounds.xml"


def get_string(res_id):
	"""
	get string from resource
	:param res_id: resource id as of attribute name in resource file
	:return: textvalue from resources, if resource not found: empty string is returned
	"""
	attr_key = "name"
	res_notfound_val = ""

	tree = ET.parse(resdir + resfile_string)
	root = tree.getroot()

	for child in root:
		# if resource is found
		if child.attrib[attr_key] == res_id:
			return child.text

	return res_notfound_val


def get_dimen(res_id):
	"""
	get resource dimension of name param
	:param res_id: resource id as of attribute name in resource file
	:return: dimension from resources, if resource not found: None is returned
	"""
	attr_key = "name"
	res_notfound_val = None

	tree = ET.parse(resdir + resfile_dimen)
	root = tree.getroot()

	for child in root:
		# if resource is found
		if child.attrib[attr_key] == res_id:
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
			try:
				return int(child.text)
			except ValueError:
				return float(child.text)

	return res_notfound_val


def get_imagesrc(res_id):
	"""
	get filepath of image of name param
	:param res_id: resource id as of attribute name in resource file
	:return: image source from resources, if resource not found: None is returned
	"""
	attr_key = "name"
	res_notfound_val = None

	tree = ET.parse(resdir + resfile_img)
	root = tree.getroot()

	for child in root:
		# if resource is found
		if child.attrib[attr_key] == res_id:

			return resdir + root.attrib["rootdir"] + child.text

	return res_notfound_val


def get_soundsrc(res_id):
	"""
	get the filepath to sound of name param
	:param res_id: resource id as of attribute name in resource file
	:return: sound source from resources, if resource not found: None is returned
	"""
	attr_key = "name"
	res_notfound_val = None

	tree = ET.parse(resdir + resfile_sound)
	root = tree.getroot()

	for child in root:
		# if resource is found
		if child.attrib[attr_key] == res_id:
			return resdir + root.attrib["rootdir"] + child.text

	return res_notfound_val


