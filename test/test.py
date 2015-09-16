from redirect_stdout2 import redirect_stdout, redirect_stderr

with file('test.out','w') as f:
    with redirect_stdout(f):
        print "foo"
    with redirect_stdout(f, stderr=True, stdout=False):
        raise Exception("bar")


