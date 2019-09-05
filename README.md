# gprof2dot_magic
Magic function for `gprof2dot` to profile any Python statement as a DOT graph in JupyterLab or Jupyter Notebook.

<img src="./img/30441189-B028-4C44-BA31-47D813EA2EFE.gif">

# installation
Make sure you've the Python package `gprof2dot_magic`.

```
pip install gprof2dot_magic
```
This will also install its dependencies `gprof2dot` and `graphviz`.

It is also important to have the Graphviz software installed.

Apperently you can use conda as such (I don't have conda):

```
conda install python-graphviz
```

Without conda 

For macOS:

```brew
brew install graphviz
```

For Windows ([source](https://stackoverflow.com/a/44005139/2459096)):

- Install windows package from: https://graphviz.gitlab.io/_pages/Download/Download_windows.html
- Add `C:\Program Files (x86)\Graphviz2.38\bin` to User path
- Add `C:\Program Files (x86)\Graphviz2.38\bin\dot.exe` to System Path

Note: close your "cmd" in which jupyter lab/notebook is running. Existing running CMD dont catch the new changes in Environment variables


# usage
To enable the magic function, first load the `gprof2dot_magic` module

```python
%load_ext gprof2dot_magic
```

and then profile any line statement as a DOT graph as such:

```python
%gprof2dot print('hello world')
```


<img src="./img/dot_graph_hello_world.svg">
