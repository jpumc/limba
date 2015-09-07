#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Limba documentation build configuration file

import sys
import os
import guzzle_sphinx_theme

# -- General configuration ------------------------------------------------

needs_sphinx = '1.0'

extensions = [
    'sphinx.ext.todo',
    'guzzle_sphinx_theme',
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix of source filenames.
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = 'Limba'
copyright = '2014-2015, Matthias Klumpp'

version = '0.5'
release = '0.5'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = []

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# -- Options for HTML output ----------------------------------------------

html_translator_class = 'guzzle_sphinx_theme.HTMLTranslator'
html_theme_path = guzzle_sphinx_theme.html_theme_path()
html_theme = 'guzzle_sphinx_theme'

html_title = None
html_short_title = "Limba Docs"

#html_logo = None

#html_favicon = None

html_static_path = ['_static']

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
html_use_smartypants = True

# If false, no module index is generated.
html_domain_indices = False

# If false, no index is generated.
html_use_index = True

# If true, links to the reST sources are added to the pages.
html_show_sourcelink = False
html_show_sphinx = False

# Output file base name for HTML help builder.
htmlhelp_basename = 'LimbaDoc'


# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
    'papersize': 'a4paper',
}

latex_documents = [
  ('index', 'Limba.tex', 'Limba Documentation',
   'Matthias Klumpp', 'manual'),
]

# The name of an image file (relative to this directory) to place at the top of
# the title page.
#latex_logo = None

# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    ('index', 'limba', 'Limba Documentation',
     ['Matthias Klumpp'], 1)
]

# If true, show URL addresses after external links.
#man_show_urls = False