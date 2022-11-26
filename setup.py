from distutils.core import setup
from distutils.extension import Extension
from Cython.Build import cythonize

ext_modules = [ Extension("NR_random_lib", sources=["NR_random_lib.pyx"] ) ]
setup( name = "NR_random_lib", ext_modules = cythonize(ext_modules) )
