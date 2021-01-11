---
title: 'SGX: A Python package about the Extended Selfish Gene'
tags:
  - Python
  - evolutionary algorithm
  - selfish gene

authors:
  - name: Giovanni Squillero
    orcid: 0000-0000-0000-0000
    affiliation: "1, 2" # (Multiple affiliations must be quoted)
  - name: Author Without ORCID
    affiliation: 2
  - name: Author with no affiliation
    affiliation: 3
affiliations:
 - name: Politecnico di Torino
   index: 1
date: 1 February 2021
bibliography: paper.bib

# Optional fields if submitting to a AAS journal too, see this blog post:
# https://blog.joss.theoj.org/2018/12/a-new-collaboration-with-aas-publishing
aas-doi: 10.3847/xxxxx <- update this with the DOI from AAS once you know it.
aas-journal: Computer Science Journal <- The name of the AAS journal.
---

# Summary

The Selfish Gene optimization algorithm (SG) is a population-less evolutionary algorithm
loosely inspired by the interpretation of the Darwinian theory given by the English
biologist Richard Dawkins and popularized as the Selfish Gene theory. 
It enables a user to efficiently find the list parameters, either discrete symbols or 
real numbers, that maximizes a given target function.

# Statement of need

`SGX` is a package about an evolutionary algorithm implemented in Python. Python
enables wrapping low-level languages (e.g., C) for speed without losing
flexibility or ease-of-use in the user-interface. The API for `SGX` was
designed to provide a class-based and user-friendly interface to fast (C or
Cython-optimized) implementations of .... `SGX` also relies heavily on and
interfaces well with the implementations of ....

`SGX` was designed to be used by both astronomical researchers and by
students in courses on ...

# Citations

Citations to entries in paper.bib should be in
[rMarkdown](http://rmarkdown.rstudio.com/authoring_bibliographies_and_citations.html)
format.

If you want to cite a software repository URL (e.g. something on GitHub without a preferred
citation) then you can do it with the example BibTeX entry below for @fidgit.

For a quick reference, the following citation commands can be used:
- `@author:2001`  ->  "Author et al. (2001)"
- `[@author:2001]` -> "(Author et al., 2001)"
- `[@author1:2001; @author2:2001]` -> "(Author1 et al., 2001; Author2 et al., 2002)"

# Figures

Figures can be included like this:
![Caption for example figure.\label{fig:example}](figure.png)
and referenced from text using \autoref{fig:example}.

Figure sizes can be customized by adding an optional second parameter:
![Caption for example figure.](figure.png){ width=20% }

# Acknowledgements

We acknowledge contributions from .... and support from ... during the genesis of this project.
