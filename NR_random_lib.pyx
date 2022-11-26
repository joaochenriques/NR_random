cdef extern from "NR_random.c":
    cpdef void nr_seed( unsigned long long )
    cpdef double nr_random()

#~ def NRC_seed( j ):
    #~ nr_seed( j )
    
#~ def NRC_random():
    #~ return nr_random( )