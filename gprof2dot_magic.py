"""
magic function that profile any statement as a dot graph using cProfile, gprof2dot and graphviz
%gprof2dot print('hello world')

should give you a nice dot profile rendered as svg
"""

__version__ = '0.2'


import cProfile
import gprof2dot as gprof2dot_source
import sys
from graphviz import Source
import tempfile
import os
from IPython.core.magic import register_line_magic

@register_line_magic
def gprof2dot(line):
    # run cProfile and prepare dot file
    with tempfile.NamedTemporaryFile(suffix='.pstats') as tf:
        tf_directory = os.path.dirname(tf.name)
        tf_basename = os.path.basename(tf.name)
        dot_fp = os.path.join(tf_directory, '{}.dot'.format(tf_name_no_ext))

        cProfile.run(statement=line, filename=tf.name)
        sys.argv = ['gprof2dot.py', '-f', 'pstats', '-o', dot_fp, tf.name]
        gprof2dot_source.main()

    # read dot file and parse as graph object
    with open(dot_fp) as file:
        dot_data = file.read()
        dot_graph = Source(dot_data)

    # cleanup
    os.remove(dot_fp)

    return dot_graph
