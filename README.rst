Author
======

Franck Barbenoire <contact@franck-barbenoire.fr>

Software version
================

Version 0.0.2, June 18th, 2014.

License
=======

This software is released under GPL v3 license :

http://www.gnu.org/licenses/gpl-3.0.html 

Introduction
============

This module is intended for recovering an image from the tiles generated from
this image.

This program is based on this article from Daniel Gasienica :

http://www.gasi.ch/blog/inside-deep-zoom-2/

API description
===============

Properties :

- maximum_level : get the maximum level of the image tree

Methods :

- Roofer(xml_url, dir_suffix='_files', mode='RGB') : constructor

- image_size(level) : get the size of the final image for a given level

- get_level_size(level) : returns a tuple (width, height, columns, rows) for a level

- get_tile_image(level, column, row) : returns a tile image from a level at given coordinates (row, column)

- get_level_image(level) : builds and returns the whole image corresponding to a level

- get_level_image_t(level, tasks=2) : same as get_level_image but using threads (experimental)

Required packages
=================

* Pillow is required
