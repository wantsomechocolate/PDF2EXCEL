try:
    hey=1+1
    print 1
    try:
        hey=1+one
        print 2
    except:
        hey=1+one
        print 3
        
except:
    print 'do I get here'
