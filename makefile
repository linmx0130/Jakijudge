SUBDIRS=oidiff watcher
INSTALLDIR=/usr
all:
	@for dir in $(SUBDIRS); do (cd $$dir && make all) done;
install:
	@for dir in $(SUBDIRS); do (cd $$dir && make install) done;
	mkdir $(INSTALLDIR)/lib/jaki/
	cp jakijudge/ $(INSTALLDIR)/lib/jaki/ -r 
	cp docs/ $(INSTALLDIR)/lib/jaki/ -r
	cp jaki_build $(INSTALLDIR)/bin/
	chmod 0755 $(INSTALLDIR)/bin/jaki_build
clean:
	@for dir in $(SUBDIRS); do (cd $$dir && make clean) done;
uninstall:
	@for dir in $(SUBDIRS); do (cd $$dir && make uninstall) done;
	rm $(INSTALLDIR)/lib/jaki/ -r
	rm $(INSTALLDIR)/bin/jaki_build

