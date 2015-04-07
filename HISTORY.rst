.. :changelog:

History
-------

v0.3.0
~~~~~~

**2015-04-07**

* Added Python 3.4 support without breaking Python 2 compatibility (thanks to `yasserglez <https://github.com/yasserglez>`_)

v0.2.5
~~~~~~

**2014-07-09**

* Added an example that solves the `8 Queens Puzzle
  <http://en.wikipedia.org/wiki/Eight_queens_puzzle>`_

**2014-07-09**

* Modified the GeneticAlgorithm class initialisation parameters
* Made changes to USAGE documentation
* Added EXAMPLE documentation as a separate section

v0.2.4
~~~~~~

**2014-07-07**

* Refactored most of the code; Made GeneticAlgorithm class more OOP
* Made changes to INSTALLATION documentation

v0.2.3
~~~~~~

**2014-07-05**

* Fixed breaking python 2.6 build

v0.2.2
~~~~~~

**2014-07-05**

* Removed duplicate ‘Example’ documentation; now maintaining only one copy in 
  examples/README.rst
* Added link to jeffknupp’s sandman repo in HISTORY
* Modified release option in Makefile to also upload project documentation
* Added INSTALLATION and EXAMPLE sections to README.rst
* Removed easy_install installation step from documentation (pip is 
  sufficient)
* Added a simple example of usage to docs/usage.rst
* Reduced the default GA population and generation size (to allow applications 
  that use the different parameters to run quickly)
* Modified tests to account for the new default population, generation size
* Added docstrings to all methods

v0.2.0
~~~~~~

**2014-07-04**

* First upload to pypi.
* Added changes made to HISTORY (pypi upload, new version)

v0.1.0
~~~~~~

**2014-06-23**

* Start of ``pyeasyga`` development.

**2014-07-03**

* Implemented all of basic GA functionality
* Fix issue with odd-numbered population that causes an off-by-one error in the 
  population size
* Set default ga selection function to tournament_selection
* Created examples to show how to use the library
* Start versioning (better late than never); copied jeffknupp’s 
  update_version.sh from `sandman <https://github.com/jeffknupp/sandman/>`_
 
  **selected versioning standard:**  major.minor.micro (e.g. 2.1.5)
  
  - major => big changes that can break compatibility
  - minor => new features
  - micro => bug fixes

