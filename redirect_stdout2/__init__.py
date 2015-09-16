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
            traceback.print_exc()
        raise
    finally:
        if stdout:
            sys.stdout = sys.__stdout__
        if stderr:
            sys.stderr = sys.__stderr__

def redirect_stderr(stream):
    return redirect_stdout(stream, stdout=False, stderr=True)
