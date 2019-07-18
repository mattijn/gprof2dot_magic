# gprof2dot_magic
Magic function for gprof2dot to profile any statement as a dot graph


# installation
Make sure you've the Python package `gprof2dot_magic`.

```
pip install gprof2dot_magic
```

Its dependencies `gprof2dot` and `graphviz` will be automatically installed as well

# usage
Enable the magic function by using the gprof2dot_magic module on a line statement

```python
%load_ext gprof2dot_magic
```

and then use the magic on a line statement to profile the statement as a dot graph:

```python
%gprof2dot print('hello world')
```


<img src="./img/dot_graph_hello_world.svg">