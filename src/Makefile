all:

install:
	. /etc/environ.sh; use -e -r anaconda-7; cd ..; export PYTHONPATH=$$PWD; jupyter-book build --all jupyter_book_contents

clean:

distclean: clean
	cd ..; jupyter-book clean jupyter_book_contents

.PHONY: all install clean distclean

