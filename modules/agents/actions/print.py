# -*- coding: utf-8 -*-

required_states = []
required_matrices = []

def run(world, matrices, states, *args, **kwargs):
    print 'matrices =', ', '.join(['"'+name+'"=('+str(type(m))+')' for name,m in matrices.iteritems()])
    print 'states =', states
    print 'args =', args
    print 'kwargs =', kwargs
