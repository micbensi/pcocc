# -*- coding: utf-8 -*-
#
# pcocc documentation build configuration file, created by
# sphinx-quickstart on Mon Jun 26 15:52:57 2017.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ['sphinx.ext.autodoc',
    'sphinx.ext.doctest',
    'sphinx.ext.todo',
    'sphinx.ext.coverage',
    'sphinx.ext.mathjax',
    'sphinx.ext.ifconfig',
    'sphinx.ext.viewcode',
    'sphinx.ext.githubpages']

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = '.rst'


titles = {
'pcocc': 'Private Cloud on a Compute Cluster',
'alloc': 'Instantiate or restore a virtual cluster (interactive mode)',
'batch': 'Instantiate or restore a virtual cluster (batch mode)',
'template': 'List and manage VM templates',
'console': 'Connect to a VM console',
'nc': 'Connect to a VM via  nc',
'scp': 'Transfer files to a VM via scp',
'ssh': 'Connect to a VM via ssh',
'image': 'List and manage VM and Container images',
'ps': 'List current pcocc jobs',
'run': 'Execute commands in VMs and containers',
'docker': 'Access a docker daemon',
'display': 'Display the graphical output of a VM',
'reset': 'Reset a VM',
'ckpt': 'Checkpoint a virtual cluster',
'dump': 'Dump the memory of a VM to a file',
'monitor-cmd': 'Send a command to the monitor',
'save': 'Save the disk of a VM',
'batch.yaml': 'Batch environment configuration file',
'networks.yaml': 'Networks configuration file',
'resources.yaml': 'Resource sets configuration file',
'templates.yaml': 'VM templates definition file',
'repos.yaml': 'Image repositories configuration file',
'newvm-tutorial': 'How to import VM images and define VM templates',
'cloudconfig-tutorial': 'How to configure cloud-init enabled VMs',
'9pmount-tutorial': 'How to mount host directories in VMs',
'containers.yaml': 'Container Configuration File',
}

rst_prolog = ''

for page, title in titles.items():
  rst_prolog += '.. |{0}_title| replace:: {1}\n'.format(page, title)

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = 'pcocc'
copyright = '2017'
author = 'François Diakhaté'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = '0.7.0'
# The full version, including alpha/beta/rc tags.
release = '0.7.0'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = []

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = True

# Important for MAN not to convert to UTF8 chars
# Prevent alteration of command-line arguments
# Sphinx <1.6 use `html_use_smartypants` and >=1.6 use `smartquotes`
from sphinx import __version__ as sphinx_version
sphinx_version_parts = [int(i) for i in sphinx_version.split('.')]
if sphinx_version_parts[0] <= 1 and sphinx_version_parts[1] < 6:
    html_use_smartypants = False
else:
    smartquotes = False


# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.

# [[ ==
#
# USING THE DEFAULT AGOGO THEME
#
#html_theme = 'agogo'
# OPTIONS FOR THE agogo theme
#
#html_theme_options = {
#		 "headercolor1":"#900",
#		 "headercolor2":"#000",
#		 "linkcolor":"#A00",
#		 "headerlinkcolor":"#FFF",
#		 "headerbg":"#900",
#		 "footerbg":"#acacac",
#		}
#
# === ]]

#
# USING THE DEPENDENCY RTD
# ==> pip install sphinx_rtd_theme
#
html_theme = 'sphinx_rtd_theme'


# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
# html_static_path = ['_static']


# -- Options for HTMLHelp output ------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'pcoccdoc'


# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    # 'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    #
    # 'preamble': '',

    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, 'pcocc.tex', 'pcocc Documentation',
     'François Diakhaté', 'manual'),
]


# -- Options for manual page output ---------------------------------------



# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).

#Here we extract the man-pages from the ./manpages/ directory

import glob
import re

man_pages = []


for f in glob.glob('manpages/*/*.rst'):
    print(f)
    m = re.match(r'(manpages/man(\d)/([\w\-\.]+)).rst', f)
    fpath = m.group(1)
    fname = m.group(3)

    section = int(m.group(2))

    if fname in titles:
        title = titles[fname]
    else:
        title = "Help for {0}".format(fname)

    if fname != 'pcocc':
        fname = 'pcocc-' + fname

    man_pages.append((
        fpath,
        fname,
        title,
        [author],
        section,
    ))

# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'pcocc', 'pcocc Documentation',
     author, 'pcocc', 'One line description of project.',
     'Miscellaneous'),
]



# -- Options for Epub output ----------------------------------------------

# Bibliographic Dublin Core info.
epub_title = project
epub_author = author
epub_publisher = author
epub_copyright = copyright

# The unique identifier of the text. This can be a ISBN number
# or the project homepage.
#
# epub_identifier = ''

# A unique identification for the text.
#
# epub_uid = ''

# A list of files that should not be packed into the epub file.
epub_exclude_files = ['search.html']



# Example configuration for intersphinx: refer to the Python standard library.
intersphinx_mapping = {'https://docs.python.org/': None}
