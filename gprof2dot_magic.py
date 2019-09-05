"""
magic function that profile any statement as a dot graph using cProfile, gprof2dot and graphviz
%gprof2dot print('hello world')

should give you a nice dot profile rendered as svg
"""

__version__ = '0.4'


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
    tf = tempfile.NamedTemporaryFile(suffix='.pstats', mode='w', delete=False)
    tf_directory = os.path.dirname(tf.name)
    tf_basename = os.path.basename(tf.name)
    tf_name_no_ext = os.path.splitext(tf_basename)[0]
    dot_fp = os.path.join(tf_directory, '{}.dot'.format(tf_name_no_ext))
    tf.close()

    cProfile.run(statement=line, filename=tf.name)
    sys.argv = ['gprof2dot.py', '-f', 'pstats', '-o', dot_fp, tf.name]
    gprof2dot_source.main()

    # read dot file and parse as graph object
    with open(dot_fp) as file:
        dot_data = file.read()
        dot_graph = Source(dot_data)

    # cleanup
    os.remove(dot_fp)
    os.remove(tf.name)

    return dot_graph
