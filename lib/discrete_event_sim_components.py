from simpy import Environment as SimpyEnvironment

from lib.config import Config
from lib.discrete_event import BroadcastPipe

# This is where we put components of DiscreteEventSim that need to be referenced
# by other classes, to avoid circular imports

class SimulationState:
    """Class to hold all global mutated state of a simulation, not including
    node-specific state such as the position of a moving node.
    """
    def __init__(self, conf: Config, env: SimpyEnvironment):
        """Constructor

        Arguments:
        conf -- Config object of global sim constants. Only used for NR_NODES.
        env -- SimPy Environment for simulation. Required for internal BroadcastPipe.
        """
        self.env = env
        self.bc_pipe = BroadcastPipe(self.env)
        self.packets = [] # used mostly for data tracking, but also for state
        self.packetsAtN = [[] for _ in range(conf.NR_NODES)]
        self.messageSeq = {"val": 0} # TODO: turn this into a locked counter

class SimulationDataTracking:
    """Class to hold data used to monitor a simulation which has no
    impact on the state or progress of the simulation
    """
    def __init__(self):
        self.messages = []
        self.delays = []
        self.totalPairs = 0
        self.symmetricLinks = 0
        self.asymmetricLinks = 0
        self.noLinks = 0
