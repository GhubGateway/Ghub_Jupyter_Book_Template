all:

install:
	cd ..; export PYTHONPATH=$$PWD; jupyter-book build --all jupyter-book-build-dir

clean:

distclean: clean
	cd ..; jupyter-book clean jupyter-book-build-dir

.PHONY: all install clean distclean

