# Pattern-Lattice-Builder
A Python implementation of generalized Pattern Lattice Builder (gPLB).

# Synopsis

gPLB implements a _generalized_ Pattern Lattice. A normal, _non-generalized_ Pattern Lattice of [a, b, c] is the is-a network over the set
{[\_, \_, \_],
[a, \_, \_], [\_, b, \_], [\_, \_, c],
[a, b, \_], [a, \_, c], [\_, b, c],
[a, b, c] } of six elements.
But in the generelized form, the resulting Pattern Lattice of the same input is the is-a network over the set 
{ [\_, \_, \_],
[a, \_, \_], [\_, b, \_], [\_, \_, c],
[a, b, \_], [a, \_, c], [\_, b, c],
[a, b, c],
[\_, \_, \_, \_],
[a, \_, \_, \_], [\_, b, \_, \_], [\_, \_, c, \_],
[a, b, \_, \_], [a, \_, c, \_], [\_, b, c, \_],
[a, b, c, \_],
[\_, a, \_, \_], [\_, \_, b, \_], [\_, \_, \_, c],
[\_, a, b, \_], [\_, a, \_, c], [\_, \_, b, c],
[\_, a, b, c],
[\_, \_, \_, \_, \_],
[\_, a, \_, \_, \_], [\_, \_, b, \_, \_], [\_, \_, c, \_, \_],
[\_, a, b, \_, \_], [\_, a, \_, b, \_], [\_, \_, b, c, \_],
[\_, a, b, c, \_]} of 31 (= 8+8+7+8) elements.
This makes gPLB different from its predecessor [RubyPLB](https://github.com/yohasebe/rubyplb), a Ruby implementation of Pattern Lattice Builder.

Additonally, gPLB, unlike RubyPLB, gives you a lot of analytical information in text format. For example, it gives you:

- all the instantiation (is-a) links generated
- all the nodes created for a pattern lattice with z-scores

gPLB also allows you specify parameters to draw graphs interactively.

gPLB will implement _content tracking_ in near future, which I believe is quite useful to make more detailed analysis of data.


## gPLB (a package including a runnable script)
[gPLB](gPLB) is a package that can be run as a script. To run it, issue the following command in the terminal:

```python gPLB <file>```

where `<file>` is an input file in .csv format. Crucial options are:

- -n [int] sets the number of instances to handle using random sampling.
- -m [int] sets the maximum number of segments in an instance.
- -s [str] sets the field separator (defaults to ",") to the one you choose.
- -g [str] sets the gap_mark (defaults to "\_") to the one you choose.
- -z [float] sets the lower limit of z-score to prune the unwanted nodes. This is truly useful when a Pattern Lattice grows a big and complex.
- -L [str] selects graph layout. Default is 'Multi_partite', a (clumsy) NetworkX-based simulation of RubyPLB output, but other layouts like Graphviz, Spring, Kamada-Kawai, which are available layout options in NetworkX, are available.
- -D [flag] flag to draw diagrams without specifying layout.
- -J [flag] set multibyte font to display. Setting up for a font path may be also needed.
- -A [flag] sets on automatic figure sizing to produce a better diagram. Useful at running on terminal rather than in Jupyter Notebook.
- -G [flag] runs the ungeneralized version instead of the generalized version (default)

## gPLB-runner (Jupyter Notebook)

[gPLB-runner.ipynb](gPLB-runner.ipynb) is a Jupyter Notebook that runs gPLB interactively. This is a better way to experiment, I suppose, especially when you need to customize graph drawing.

The following graph is a sample of Pattern Lattice generated from [XiY-wiper3-dual](sources/plb-XiY-wiper3-dual.csv) with pruning of nodes with z-scores less than 0.0 using gPLB-runner.ipynb. I would be quite difficult to produce graphs like this by running gPLB as a script. A lot of frustrating adjustments should be needed. 

![XiY-wiper3-dual](graphs/pl-XiY-wiper3-dual.png){width=100}


## Information

- [Pattern Lattice as a mode for liniguistic knowledge and performance](https://aclanthology.org/Y09-1030.pdf) 