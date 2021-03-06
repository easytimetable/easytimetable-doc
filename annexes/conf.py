import sys, os
project = u'Documentation'
copyright = u'2010, Guillaume Espanel, Julien Grande, Nicolas Morel, Alexis Metaireau'
version = "1.0"
extensions = []
templates_path = ['_templates']
source_suffix = '.rst'
master_doc = 'index'
release = version

#language = None
exclude_trees = ['_build']
pygments_style = 'sphinx'

# HTML
html_theme = 'default'
html_static_path = ['_static']
htmlhelp_basename = 'annexes'

# Latex
latex_documents = [
  ('index', 'annexes.tex', u'TimeTableEasy - Documentation',
   u'GREATTEAMDEVELOPMENT', 'manual'),
]
