Used files

	NR_random.c
	NR_random_Compare.c
	NR_random_Compare.py
	NR_random_lib.pyx
	README.txt
	setup.py

** Install cython (if not installed). Run at command prompt:
conda install cython

** To build run at command prompt:

python setup.py build_ext --inplace

** To install run at command prompt:

python setup.py install

** To COMPARE results of the "C" at python codes run at command prompt:

gcc NR_random_Compare.c -o NR_random_Compare.exe
NR_random_Compare.exe
python NR_random_Compare.py

