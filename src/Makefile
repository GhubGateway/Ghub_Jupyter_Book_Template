all:

install:
	. /etc/environ.sh; use -e -r anaconda-7; cd ..; export PYTHONPATH=$$PWD; jupyter-book build --all template_jupyter_book

clean:

distclean: clean
	cd ..; jupyter-book clean template_jupyter_book

.PHONY: all install clean distclean

