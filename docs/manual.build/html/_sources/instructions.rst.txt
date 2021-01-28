""""""""""""
Installation
""""""""""""

Source Code
===========


SGX is available as a `PyPi package <https://en.wikipedia.org/wiki/Python_Package_Index>`_ from https://pypi.org/project/sgx/ and installing it is as simple as

::

    pip install sgx

and then

.. code-block:: python

    >>> import sgx

Caveat: on some systems the package manager is ``pip3``.


Importance of FOSS
==================

**Personal control, customizability and freedom:**

Users of FOSS benefit from the Four Essential Freedoms to make unrestricted use of,
and to study, copy, modify, and redistribute such software with or without modification.
If they would like to change the functionality of software they can bring about changes to the code and, if they wish,
distribute such modified versions of the software or often − depending on the software's decision making model and
its other users − even push or request such changes to be made via updates to the original software.

**Privacy and security:**

Manufacturers of proprietary, closed-source software are sometimes pressured to building in backdoors or other covert,
undesired features into their software. Instead of having to trust software vendors,
users of FOSS can inspect and verify the source code themselves and can put trust on a community of volunteers and users.
As proprietary code is typically hidden from public view, only the vendors themselves and hackers may be aware
of any vulnerabilities in them while FOSS involves as many people as possible for exposing bugs quickly.

**Low costs or no costs:**

FOSS is often free of charge although donations are often encouraged.
This also allows users to better test and compare software.

**Quality, collaboration and efficiency:**

FOSS allows for better collaboration among various parties and individuals with the goal
of developing the most efficient software for its users or use-cases
while proprietary software is typically meant to generate profits.
Furthermore, in many cases more organizations and individuals contribute to such projects than to proprietary software.
It has been shown that technical superiority is typically the primary reason why companies choose open source software.

-----------------------------------------------------------------------------------------------------------------------------

The default branch is always the more stable and the only one tested through Travis CI.
The experimental branches ``exp/*`` contain code and comments that some programmers may find disturbing — Viewers discretion advised.
Before trying to contribute read this paper and this style guide.
It may be wise to send Giovanni an email [@] before digging into the project.