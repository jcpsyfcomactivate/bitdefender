# Configuration file for the Sphinx documentation builder.

import os
import sys

# -- Path setup --------------------------------------------------------------

# If extensions or modules to document with autodoc are in another directory,
# add these directories to sys.path here.
# Example:
# sys.path.insert(0, os.path.abspath('../src'))

# -- Project information -----------------------------------------------------

project = 'Bitdefender Central Login Guide'
copyright = '2025, Bitdefender'
author = 'Bitdefender Support Team'

# The full version, including alpha/beta/rc tags
release = '1.0.0'

# -- HTML output settings ----------------------------------------------------

# SEO Title shown in the browser tab and HTML pages
html_title = "Bitdefender Central Login: Access Your Cybersecurity Dashboard Easily"

# Optional short title for navigation bar or breadcrumbs
html_short_title = "Bitdefender Login"

# Favicon (place favicon.ico in the root or _static folder)
html_favicon = 'favicon.ico'

# Choose a theme (uncomment if needed)
# html_theme = 'sphinx_rtd_theme'

# Hide "View page source"
html_show_sourcelink = False

# Allow raw HTML in reStructuredText files
html_allow_unsafe = True

# Theme customization options
html_theme_options = {
    'show_powered_by': False,
}

# Templates and static files
templates_path = ['_templates']
# html_static_path = ['_static']  # Uncomment if needed

# Files to ignore
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']
