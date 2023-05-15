all:

install:
	cd ..; export PYTHON_ATH=$$PWD; jupyter-book build --all jupyter-book

clean:

distclean: clean
	cd ..; jupyter-book clean jupyter-book

.PHONY: all install clean distclean

