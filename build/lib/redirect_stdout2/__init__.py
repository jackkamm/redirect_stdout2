from contextlib import contextmanager
import sys
import traceback

@contextmanager
def redirect_stdout(stream, stdout=True, stderr=False):
    if stdout:
        sys.stdout = stream
    if stderr:
        sys.stderr = stream
    try:
        yield
    except Exception,e:
        if stderr:
            # swap stdout and stderr
            #sys.stdout, sys.stderr = sys.stderr, sys.stdout
            # writes error to stdout
            traceback.print_exc()
            # swap back
            #sys.stdout, sys.stderr = sys.stderr, sys.stdout            
        raise
    finally:
        if stdout:
            sys.stdout = sys.__stdout__
        if stderr:
            sys.stderr = sys.__stderr__

def redirect_stderr(stream):
    return redirect_stdout(stream, stdout=False, stderr=True)
