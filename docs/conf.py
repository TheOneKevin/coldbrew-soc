# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))

# -- Project information -----------------------------------------------------

project = 'HS32 and HSC SoC Documentation'
author = 'Kevin Dai'
copyright = '2021, ' + author
root_doc = 'index'

# The full version, including alpha/beta/rc tags
release = 'draft'
version = 'rev2'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinxcontrib.bitfield'
]

# Add any paths that contain templates here, relative to this directory.
templates_path = [ ]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']
html_css_files = [
    'css/style.css',
]

latex_documents = [(
    root_doc, 'hs32.tex',
    "HS32 ISA and HSC-SoC Programmer's Manual",
    author, 'manual'
)]
latex_elements = {
    'extraclassoptions': 'openany,oneside',
    'releasename': 'Version',
    'preamble': R'''
        \protected\def\sphinxcrossref#1{#1}
        \renewcommand{\baselinestretch}{1.1}
        \AtBeginDocument{\raggedright}
    ''',
    'fontpkg': R'''
        \usepackage{tgtermes}
        \usepackage{tgheros}
        \renewcommand\ttdefault{txtt}
        \renewcommand*\familydefault{\sfdefault}
    ''',
    'pointsize': '10pt'
}

latex_additional_files = [
    '_static/sphinxmanual.cls'
]
