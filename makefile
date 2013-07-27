SUBDIRS=oidiff watcher
all:
	@for dir in $(SUBDIRS); do (cd $$dir && make all) done;
install:
	@for dir in $(SUBDIRS); do (cd $$dir && make install) done;
	mkdir /usr/lib/jaki/
	cp jakijudge/ /usr/lib/jaki/ -r 
	cp docs/ /usr/lib/jaki/ -r
	cp jaki_build /usr/bin/
clean:
	@for dir in $(SUBDIRS); do (cd $$dir && make clean) done;
uninstall:
	@for dir in $(SUBDIRS); do (cd $$dir && make uninstall) done;
	rm /usr/lib/jaki/ -r
	rm /usr/bin/jaki_build

