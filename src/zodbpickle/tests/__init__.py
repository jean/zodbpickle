import os
import platform

py_impl = getattr(platform, 'python_implementation', lambda: None)
_is_pypy = py_impl() == 'PyPy'
_is_pure = 'PURE_PYTHON' in os.environ
