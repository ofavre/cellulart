# -*- coding: utf-8 -*-

import matrix
import modulesreader

import numpy
import threading



class World:
    """ The world is responsible for the life and states.
        The world is composed of multiple superposed named matrices of different data types,
        as well as some objects such as agents."""

    def __init__(self, shape):
        """Creates a new, empty world, with a fixed given shape (2D-size)."""
        self.__step_lock = threading.Lock()
        self.__mustdraw_isdone_event = threading.Event()
        self.__mustdraw_isdone_event.set()
        self.__teardown_event = threading.Event()
        self.__shape = shape
        self.__matrices = {} # name to matrix
        self.__matrices_list = [] # front to back matrix drawing order
        self.__matrices_are_updating_index = False # flag indicating whether a grouped index update is being performed
        self.__agents = {}
        self.__agents_new = {} # to be added for next step
        self.__cellularautomata = {}
        self.__lsystems = {}
        self.__objects_modules = {}
        self.__objects = {}

    def get_shape(self):
        """Returns the shape (2D-size) of the world."""
        return self.__shape.__class__(self.__shape) # return a copy

    def create_matrix(self, name):
        if self.__matrices.has_key(name):
            raise KeyError("matrix already existing")
        matrix = modulesreader.ModulesReaderInstance.create_matrix(self, len(self.__matrices_list), name, self.__shape)
        return self.add_matrix(name, matrix)
    def add_matrix(self, name, matrix):
        self.__matrices_list.append(matrix)
        if matrix.index != len(self.__matrices_list)-1:
            matrix.index = len(self.__matrices_list)-1
        self.__matrices[name] = matrix
        return matrix

    def get_matrix(self, name):
        """Returns the matrix of a given name."""
        return self.__matrices[name]

    def get_matrices_list(self):
        """Returns the known matrices."""
        return list(self.__matrices_list) # return a copy of the matrices list (but a reference to the true matrices)

    def get_matrices_dict(self):
        """Returns the known matrices."""
        return dict(self.__matrices) # return a copy of the matrices dict (but a reference to the true matrices)

    def set_matrix_index(self, name, index):
        """ Modifies the index of a matrix, reodering the necessary ones.
            Equivalent to directly setting the index property on the corresponding matrix."""
        self.__matrices[name].index = index
    def _matrix_index_changed(self, matrix, old_index, new_index):
        """ Notified (or rather called as it is not a signal), when a matrix has been changed its index value.
            Changes the drawing list order accordindly and shifts the necessary other matrices.
            Returns the new index the matrix should set internally (for potential range ensurance)."""
        # Ensure the new index is correct
        new_index = max(0,min(len(self.__matrices_list)-1,int(new_index)))
        # Skip if no real change, or if a batch update is already going on
        if old_index == new_index or self.__matrices_are_updating_index:
            return new_index
        else:
            # Flag a batch update
            self.__matrices_are_updating_index = True
        # Shift the other matrices between the old and the new position accordingly to the direction of the initial change (bring to front, send to back)
        if old_index < new_index:
            for i in xrange(old_index+1,new_index+1):
                self.__matrices_list[i].index -= 1
        else:
            for i in xrange(new_index,old_index):
                self.__matrices_list[i].index += 1
        # Also impact the changes on the drawing list
        self.__matrices_list.insert(new_index, self.__matrices_list.pop(old_index))
        # End of batch update
        self.__matrices_are_updating_index = False
        return new_index

    def create_agents(self,name,count):
        if self.__agents.has_key(name):
            raise KeyError("agents already existing")
        agents = [modulesreader.ModulesReaderInstance.create_agent(self, name) for i in xrange(count)]
        return self.add_agents(name, agents)
    def get_agents(self,name):
        return self.__agents.get(name,[])
    def add_agents(self, name, agents):
        self.__agents[name] = agents
        return agents
    def add_new_agents(self,name,count=1):
        """ Adds new agents to the world for the next iteration.
            Return newly constructed and initialized agents, that can be further modified.
            Callable inside step() by an agent module."""
        new_agents = [modulesreader.ModulesReaderInstance.create_agent(self, name) for i in xrange(count)]
        self.__agents_new.setdefault(name, []).extend(new_agents)
        return new_agents

    def create_objects(self,name,*args,**kwargs):
        if self.__objects.has_key(name):
            raise KeyError("objects already existing")
        module = modulesreader.ModulesReaderInstance.create_objects(self, name)
        self.__objects_modules[name] = module
        # The following call should add any objects to the world by calling add_new_objects, through the object's init method
        module.init(self,*args,**kwargs)
    def get_objects(self,name):
        return self.__objects.get(name,[])
    def add_new_objects(self,name,objects):
        module = self.__objects_modules[name]
        # Warn the objects of their creation, before adding them
        for obj in objects:
            module.created(self, obj)
        # Add them in the list
        self.__objects.setdefault(name,[]).extend(objects)
    def remove_objects(self,name,objects):
        module = self.__objects_modules[name]
        # Warn the objects of their deletion, before removing them
        for obj in objects:
            module.deleted(self, obj)
        for obj in objects:
            self.__objects.setdefault(name,[]).remove(obj)

    def create_cellularautomaton(self,name):
        if self.__cellularautomata.has_key(name):
            raise KeyError("cellular automata already existing")
        cellularautomaton = modulesreader.ModulesReaderInstance.create_cellularautomaton(name)
        return self.add_cellularautomaton(name, cellularautomaton)
    def get_cellularautomaton(self,name):
        return self.__cellularautomata[name]
    def add_cellularautomaton(self, name, cellularautomaton):
        self.__cellularautomata[name] = cellularautomaton
        return cellularautomaton

    def step(self):
        """ Calculate the next iteration of the world.
            This function is thread-safe."""
        if self.__teardown_event.isSet(): return False
        # Make sure no other thread is accessing the matrices, so that we can update them
        self.__mustdraw_isdone_event.wait()
        # Make sure no other thread will compute a step concurrently
        self.__step_lock.acquire()
        try:
            # Make cellular automata step
            for name,cellularautomaton in self.__cellularautomata.iteritems():
                cellularautomaton.run(self, self.__matrices)
            # Make agents step
            percepts = modulesreader.ModulesReaderInstance.get_all_percepts()
            actions = modulesreader.ModulesReaderInstance.get_all_actions()
            for name,agents in self.__agents.iteritems():
                if type(agents) != list:
                    agents = [agents]
                # Construct the list of agents for the next iteration
                agents_next = []
                for a in agents:
                    if a.run(self, percepts, actions):
                        # Only add surviving agents
                        agents_next.append(a)
                # Add newly created agents, for next iteration
                agents_next.extend(self.__agents_new.get(name,[]))
                self.__agents_new.clear()
                self.__agents[name] = agents_next
            # Tell objects they are existing
            for name,objects in self.__objects.iteritems():
                module = self.__objects_modules[name]
                for obj in objects:
                    module.exists(self, obj)
        finally:
            self.__step_lock.release()

    def wait_for_drawing_to_be_done(self):
        if self.__teardown_event.isSet(): return False
        self.__mustdraw_isdone_event.clear()

    def lock_for_drawing(self):
        """Require that the matrices won't be modified for a drawing phase."""
        if self.__teardown_event.isSet(): return False
        self.__mustdraw_isdone_event.clear()
        self.__step_lock.acquire()
    def unlock_for_drawing(self):
        """Cease requiring that the matrices won't be modified, at the end of a drawing phase."""
        self.__step_lock.release()
        self.__mustdraw_isdone_event.set()

    def teardown(self, wait=False):
        """Makes sure we can quit the world, ie if no other thread is working on it."""
        self.__teardown_event.set()
        if wait:
            # Wait for locks to be free
            self.__mustdraw_isdone_event.set()
            self.__step_lock.acquire()
            self.__step_lock.release()
