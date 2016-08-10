"""
handling string resource data from xml file
resourcefile is defined in var resourcefile
to get string from resourcefile, use getString(resId) function

:author: Mikael Holmbom
:version: 1.0
"""
import xml.etree.ElementTree as ET
from font_resource import FontResource


# path to resource data
resdir = "../res/"
# resourcefiles containing data
resfile_string 	= "strings.xml"
resfile_dimen 	= "dimens.xml"
resfile_img		= "images.xml"
resfile_val		= "values.xml"
resfile_sound	= "sounds.xml"
resfile_font	= "fonts.xml"


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


def get_soundsrc():
	"""
	reads all data from sounds resourcefile into a ResourceAccessObject
	:return: image source from resources, if resource not found:
	:returns ResourceAccessObject: containing all values from sound resourcefile
	"""
	attr_key = "name"

	tree = ET.parse(resdir + resfile_sound)
	root = tree.getroot()

	rootdir = resdir + root.attrib["rootdir"]

	paths = {}

	for child in root:
		key = child.attrib[attr_key]
		val = child.text
		paths[key] = str(rootdir) + str(val)

	return paths


def get_font(res_id):
	"""
	get font from resource file
	:param res_id: name of the font to access
	:return: font, if resource not found -> None
	:returns: src.resource.FontResource
	"""
	attr_key = "name"
	res_notfound_val = None

	tree = ET.parse(resdir + resfile_font)
	root = tree.getroot()

	for child in root:
		# if resource is found
		if child.attrib[attr_key] == res_id:
			name = child.text
			size = int(child.attrib["size"])
			return FontResource(name, size)

	return res_notfound_val
