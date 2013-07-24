def buildjaki_py():
    f=open('jaki.py','w')
    c="from jakijudge import jaki,base"
    print >>f,c
    c="def special_setting():"
    print >>f,c
    c="    # You can write some scripts to set the jaki"
    print >>f,c
    c="    pass"
    print >>f,c
    c="jaki.Main(special_setting)"
    print >>f,c

