#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# neurokit2 documentation build configuration file, created by
# sphinx-quickstart on Fri Jun  9 13:47:02 2017.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

# If extensions (or modules to document with autodoc) are in another
# directory, add these directories to sys.path here. If the directory is
# relative to the documentation root, use os.path.abspath to make it
# absolute, like shown here.
#
import os
import mock
import re
import sys

sys.path.insert(0, os.path.abspath('../'))


MOCK_MODULES = ['numpy', 'pandas',
                'matplotlib', 'matplotlib.pyplot', 'matplotlib.patches', 'matplotlib.cm', 'matplotlib.collections', 'matplotlib.gridspec', 'matplotlib.animation', 'mpl_toolkits', 'mpl_toolkits.mplot3d',
                'scipy', 'scipy.signal', 'scipy.ndimage', 'scipy.stats', 'scipy.misc', 'scipy.interpolate', 'scipy.sparse', 'scipy.linalg', 'scipy.spatial', 'scipy.special', 'scipy.integrate',
                'sklearn', 'sklearn.neighbors', 'sklearn.mixture', 'sklearn.datasets', 'sklearn.metrics',
                'mne', 'bioread', 'cvxopt', 'pywt']

for mod_name in MOCK_MODULES:
    sys.modules[mod_name] = mock.Mock()



# -- General configuration ---------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.doctest',
    'sphinx.ext.intersphinx',
    'sphinx.ext.todo',
    'sphinx.ext.coverage',
    'sphinx.ext.mathjax',
    'sphinx.ext.ifconfig',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
    'sphinx_rtd_theme',
    'nbsphinx',
    'sphinx_nbexamples',
]


# on_rtd is whether we are on readthedocs.org
on_rtd = os.environ.get('READTHEDOCS', None) == 'True'

# sphinx-nbexamples
process_examples = not os.path.exists(os.path.join(os.path.dirname(__file__), 'examples'))
not_document_data = 'sphinx_nbexamples.gallery_config'

# Style autodoc
napoleon_google_docstring = False
napoleon_numpy_docstring = True
napoleon_use_param = False
napoleon_use_ivar = False
napoleon_use_rtype = False

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# General information about the project.
def find_author():
    result = re.search(r'{}\s*=\s*[\'"]([^\'"]*)[\'"]'.format("__author__"), open('../neurokit2/__init__.py').read())
    return str(result.group(1))


project = u'NeuroKit'
copyright = u"2020, Dominique Makowski"
author = find_author()


# The version info for the project you're documenting, acts as replacement
# for |version| and |release|, also used in various other places throughout
# the built documents.
#
# The short X.Y version.
def find_version():
    result = re.search(r'{}\s*=\s*[\'"]([^\'"]*)[\'"]'.format("__version__"), open('../neurokit2/__init__.py').read())
    return result.group(1)


version = find_version()
# The full version, including alpha/beta/rc tags.
release = version

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', '**.ipynb_checkpoints']

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'monokai'  # 'default'
nbsphinx_codecell_lexer = 'ipython3'

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = False

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
html_show_sphinx = False

# -- Options for HTML output -------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'
html_favicon = "img/icon.ico"
html_logo = "img/neurokit.png"

# Theme options are theme-specific and customize the look and feel of a
# theme further.  For a list of options available for each theme, see the
# documentation.
#
# html_theme_options = {}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']


# -- Options for HTMLHelp output ---------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'neurokit2doc'


# Bootstrap theme
# html_theme = 'bootstrap'
# html_theme_path = sphinx_bootstrap_theme.get_html_theme_path()
# html_theme_options = {
#     'source_link_position': "footer",
#     'bootswatch_theme': "readable",
#     'navbar_sidebarrel': False,
#     'nosidebar': True,
#     'navbar_pagenav': False,
#     'bootstrap_version': "3",
#     'navbar_links': [
#                      ("Installation", "installation"),
#                      ("What's new", "news"),
#                      ("Functions", "functions"),
#                      ("Contributing", "contributing"),
#                      ("Authors", "credits")
#                      ],
#
#     }


# -- Options for LaTeX output ------------------------------------------
pdf_title = u'NeuroKit2'
author_field = u'Official Documentation'


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
# (source start file, target name, title, author, documentclass
# [howto, manual, or own class]).
latex_documents = [
        (master_doc,
         'neurokit2.tex',
         pdf_title,
         author_field,
         'manual'),
]


# -- Options for manual page output ------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
        (master_doc,
         'neurokit2',
         pdf_title,
         [author_field],
         1)
]


# -- Options for Texinfo output ----------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc,
     'neurokit2',
     pdf_title,
     author_field,
     'neurokit2',
     'The Python Toolbox for Neurophysiological Signal Processing.',
     'Miscellaneous'),
]


# Other
add_module_names = False  # so functions aren’t prepended with the name of the package/module
add_function_parentheses = True  # to ensure that parentheses are added to the end of all function names

