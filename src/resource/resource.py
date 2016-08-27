"""
handling string resource data from xml file
resourcefile is defined in var resourcefile
to get string from resourcefile, use getString(resId) function\n

:author: Mikael Holmbom
:version: 1.0
"""
import xml.etree.ElementTree as ET
from font_resource import FontResource
from color_resource import ColorResource
from dimen_resource import DimenResource


# path to resource data
resdir = "../res/"
# resourcefiles containing data
resfile_string 	= "strings.xml"
resfile_dimen 	= "dimens.xml"
resfile_img		= "images.xml"
resfile_val		= "values.xml"
resfile_sound	= "sounds.xml"
resfile_font	= "fonts.xml"
resfile_color	= "colors.xml"


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
	:return: dimension from resources as DimenResource, if resource not found: None is returned
	"""
	attr_key = "name"
	res_notfound_val = None

	tree = ET.parse(resdir + resfile_dimen)
	root = tree.getroot()

	def get_attr(child, key):
		try:
			return int(child.attrib[key])
		except:
			return None

	for child in root:
		# if resource is found
		if child.attrib[attr_key] == res_id:
			dimen = DimenResource()

			dimen.top 			= get_attr(child, "top")
			dimen.right 		= get_attr(child, "right")
			dimen.bottom 		= get_attr(child, "bottom")
			dimen.left 			= get_attr(child, "left")
			dimen.linespacing	= get_attr(child, "linespacing")
			dimen.dist 			= get_attr(child, "dist")
			dimen.width 		= get_attr(child, "width")
			dimen.height 		= get_attr(child, "height")
			dimen.x 			= get_attr(child, "x")
			dimen.y 			= get_attr(child, "y")
			dimen.size 			= get_attr(child, "size")
			dimen.radius 		= get_attr(child, "radius")
			dimen.border		= get_attr(child, "border")

			return dimen

	return res_notfound_val


def get_value(res_id):
	"""
	get value of name param
	:param res_id: resource id as of attribute name in resource file
	:return: value from resources, if resource not found: None is returned
	"""
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
			font_res = FontResource(name, size)
			try:
				style = child.attrib["style"]
				if "italic" in style:
					font_res.style_italic = True
				if "bold" in style:
					font_res.style_bold = True
			except KeyError as e:
				pass

			return font_res

	return res_notfound_val


def get_color(res_id):
	attr_key = "name"
	res_notfound_val = None

	def valid_rgb(val):
		"""
		determine if val is valid rgb value
		:param val:
		:return:
		"""
		if isinstance(val, int) and \
			 0 <= int(val) <=255:
			return True

		return False

	tree = ET.parse(resdir + resfile_color)
	root = tree.getroot()
	key_red 	= "r"
	key_green 	= "g"
	key_blue 	= "b"
	key_ref 	= "ref"

	for child in root:
		# if resource is found
		if child.attrib[attr_key] == res_id:
			attr = child.attrib
			# color is a reference to other color
			if key_ref in attr:
				return get_color(attr[key_ref])
			# color has a RGB value
			elif key_red in attr \
					and key_green in attr \
					and key_blue in attr:
				rgb = [int(attr[key_red]), int(attr[key_green]), int(attr[key_blue])]

				if valid_rgb(rgb[0]) \
					and valid_rgb(rgb[1]) \
					and valid_rgb(rgb[2]):

					return ColorResource(rgb[0], rgb[1], rgb[2])

	return res_notfound_val