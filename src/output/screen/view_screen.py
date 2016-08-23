from src.output.screen.screen import Screen


class ViewScreen(Screen):
    """
    Screen used only for viewing information from\n

    :author: Mikael Holmbom
    :version: 1.0
    """

    _font               = None
    _font_res           = None
    _font_res_header    = None
    _font_header        = None

    _article_padd       = None

    def _blit_text(self, surface, text_content, text_color, pos):
        """

        :param surface: the surface to blit
        :param text_content: the text to blit
        :param text_color: color of the text
        :param pos: position of blit
        :return:
        """
        text_surface = self._font.render(text_content, 0, text_color)
        surface.blit(text_surface, pos)

    def _blit_rows(self, surf, header, text_color, rows):
        """
        blit head togheter with rows\n
        :param surf: surf to blit headers and rows onto
        :param header:
        :param text_color:
        :param rows: the rows to blit
        :return:
        """
        padd = self._article_padd
        x = padd.left
        y = padd.top

        row_height      = self._font.size(rows[0])[1] + padd.linespacing
        header_surf     = self._font_header.render(header, 0, text_color)
        surf.blit(header_surf, (x, y))
        y += self._font_header.size(header)[1] # add header height
        for row in rows:
            self._blit_text(surf, row, text_color, (x, y))
            y += row_height

    def _get_article_size(self, header, rows):
        """
        get the dimension width and height\n
        :param rows: strings of text
        :return: width and height of rows content including padding
        """
        padd = self._article_padd
        header_size = self._font_header.size(header)
        x = header_size[0]
        for row in rows:
            if row is not None:
                row_width = self._font.size(row)[0]
                if row_width > x:
                    x = row_width

        row_height      = self._font.size(rows[0])[1] + padd.linespacing
        header_height   = (header_size[1] + padd.linespacing)
        y           = (row_height * len(rows)) + header_height
        width       = x + padd.left + padd.right
        height      = y + padd.top + padd.bottom
        return width, height
