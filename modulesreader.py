#!/usr/bin/python
# -*- coding: utf-8 -*-

import matrix
import cellularautomaton
import agent

import pkgutil



class ModulesReader(object):

    def __init__(self):
        self.matrices         = [mdl for mdl in pkgutil.iter_modules(['modules/matrices'])]
        self.matricesborders  = [mdl for mdl in pkgutil.iter_modules(['modules/matrices/borders'])]
        self.cellularautomata = [mdl for mdl in pkgutil.iter_modules(['modules/cellularautomata'])]
        self.lsystems         = [mdl for mdl in pkgutil.iter_modules(['modules/lsystems'])]
        self.agentsstates     = [mdl for mdl in pkgutil.iter_modules(['modules/agents/states'])]
        self.agentspercepts   = [mdl for mdl in pkgutil.iter_modules(['modules/agents/percepts'])]
        self.agentsactions    = [mdl for mdl in pkgutil.iter_modules(['modules/agents/actions'])]
        self.agentsbrains     = [mdl for mdl in pkgutil.iter_modules(['modules/agents/brains'])]
        self.agents           = [mdl for mdl in pkgutil.iter_modules(['modules/agents'])]
        self.objects          = [mdl for mdl in pkgutil.iter_modules(['modules/objects'])]
        #TODO: Better object model
        self.agentsstates_obj = {}
        for mdl in self.agentsstates:
            self.agentsstates_obj[mdl[1]] = self.create_state(mdl[1])
        self.agentspercepts_obj = {}
        for mdl in self.agentspercepts:
            self.agentspercepts_obj[mdl[1]] = self.create_percept(mdl[1])
        self.agentsactions_obj = {}
        for mdl in self.agentsactions:
            self.agentsactions_obj[mdl[1]] = self.create_action(mdl[1])
        self.agentsbrains_obj = {}
        for mdl in self.agentsbrains:
            self.agentsbrains_obj[mdl[1]] = self.create_brain(mdl[1])
        self.agents_obj = {}
        for mdl in self.agents:
            if mdl[2]: continue
            def factory():
                return self.create_agent(mdl[1])
            self.agents_obj[mdl[1]] = factory
        self.cellularautomata_obj = {}
        for mdl in self.cellularautomata:
            self.cellularautomata_obj[mdl[1]] = self.create_cellularautomaton(mdl[1])

    def get_requirements(self):
        #TODO
        raise NotImplemented()

    def get_module(self, name, from_list):
        candidates = filter(lambda tupl: tupl[1] == name, from_list)
        if len(candidates) != 1:
            return None
        importer = candidates[0][0]
        loader = importer.find_module(name)
        module = loader.load_module(name)
        return module

    def create_matrix_border(self, name):
        module = self.get_module(name, self.matricesborders)
        if module == None:
            raise Exception("Matrix border module not found: %s" % name)
        return module.border_check

    def create_matrix(self, world, index, name, shape):
        module = self.get_module(name, self.matrices)
        if module == None:
            raise Exception("Matrix module not found: %s" % name)
        border = self.create_matrix_border(module.border)
        rtn = matrix.Matrix(world, index, name, shape, module.dtype, module.track_updates, border)
        module.init(world, rtn)
        rtn.visible = module.visible
        rtn.colormap = module.colormap
        rtn.alpha = module.alpha
        return rtn

    def create_state(self, name):
        module = self.get_module(name, self.agentsstates)
        if module == None:
            raise Exception("Agent State module not found: %s" % name)
        return agent.State(module.init)

    def get_all_states(self):
        return self.agentsstates_obj

    def create_percept(self, name):
        module = self.get_module(name, self.agentspercepts)
        if module == None:
            raise Exception("Agent Percept module not found: %s" % name)
        return agent.Percept(module.run)

    def get_all_percepts(self):
        return self.agentspercepts_obj

    def create_action(self, name):
        module = self.get_module(name, self.agentsactions)
        if module == None:
            raise Exception("Agent Action module not found: %s" % name)
        return agent.Action(module.run)

    def get_all_actions(self):
        return self.agentsactions_obj

    def create_brain(self, name):
        module = self.get_module(name, self.agentsbrains)
        if module == None:
            raise Exception("Agent Brain module not found: %s" % name)
        return agent.Brain(module.run)

    def get_all_brains(self):
        return self.agentsbrains_obj

    def create_agent(self, world, name):
        module = self.get_module(name, self.agents)
        if module == None:
            raise Exception("Agent module not found: %s" % name)
        states = dict([(state,self.agentsstates_obj[state]) for state in module.states])
        brains = [self.agentsbrains_obj[brain] for brain in module.brains]
        return agent.Agent(name, world, states, brains)

    def get_all_agents(self):
        return self.agents_obj

    def create_objects(self, world, name):
        module = self.get_module(name, self.objects)
        if module == None:
            raise Exception("Object module not found: %s" % name)
        return module

    def create_cellularautomaton(self, name):
        module = self.get_module(name, self.cellularautomata)
        if module == None:
            raise Exception("Cellular automaton module not found: %s" % name)
        """return cellularautomaton.CellularAutomaton(module.run, module.output_matrices)"""
        return cellularautomaton.CellularAutomaton(module.run)

    def get_all_cellularautomata(self):
        return self.cellularautomata_obj

ModulesReaderInstance = ModulesReader()



if __name__ == "__main__":
    mr = ModulesReaderInstance
    print "Known matrices:"
    print "\n".join([" - "+str(n) for n in mr.matrices])
    print "Known matrices borders:"
    print "\n".join([" - "+str(n) for n in mr.matricesborders])
    print "Known cellular automata:"
    print "\n".join([" - "+str(n) for n in mr.cellularautomata])
    print "Known L-systems:"
    print "\n".join([" - "+str(n) for n in mr.lsystems])
    print "Known agents states:"
    print "\n".join([" - "+str(n) for n in mr.agentsstates])
    print "Known agents percepts:"
    print "\n".join([" - "+str(n) for n in mr.agentspercepts])
    print "Known agents actions:"
    print "\n".join([" - "+str(n) for n in mr.agentsactions])
    print "Known agent brains:"
    print "\n".join([" - "+str(n) for n in mr.agentsbrains])
    print "Known objects:"
    print "\n".join([" - "+str(n) for n in mr.objects])
