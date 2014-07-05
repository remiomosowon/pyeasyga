.. :changelog:

History
-------

2014-07-05 (v0.2.2)
~~~~~~~~~~~~~~~~~~~

* Removed duplicate ‘Example’ documentation; now maintaining only one copy in 
  examples/README.rst
* Added link to jeffknupp’s sandman repo in HISTORY
* Modified make release to also upload project documentation
* Added Installation, and Example info to README.rst
* Removed easy_install installation step from docs/installation.rst (pip is 
  sufficient)
* Added a simple example of usage to docs/usage.rst
* Reduced the default GA population and generation size (to allow applications 
  that use the different parameters to run quickly)
* Modified tests to account for the new default population, generation size
* Added docstrings to all methods

2014-07-04 (v0.2.0)
~~~~~~~~~~~~~~~~~~~

* Upload to pypi.
* Reflect changes in HISTORY (pypi upload, new version)

2014-07-03 (v0.1.0)
~~~~~~~~~~~~~~~~~~~

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

2014-06-23 (v0.1.0)
~~~~~~~~~~~~~~~~~~~

* Start of ``pyeasyga`` development.
