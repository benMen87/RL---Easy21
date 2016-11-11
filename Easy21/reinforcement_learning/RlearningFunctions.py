from collections import namedtuple

class RlearningFunctions(object):
    """Logic for updating Q V """

    def __init__(self, step, eps_greedy, valid_actions, qkeyfunc, vkeyfunc=None,
                 nsakeyfunc=None, nskeyfunc=None):
        self.step       = step
        self.eps_greedy = eps_greedy
        self.V          = dict()
        self.Q          = dict()
        self.Ns         = dict()
        self.Nsa        = dict()
        self.state = None
        self.valid_actions = valid_actions

        #
        # KeyFunc
        #
        if qkeyfunc is None:
            self.qkeyfunc      = namedtuple('qkey', ['state' 'action'])
        else:
            self.qkeyfunc = qkeyfunc

        if vkeyfunc is None:
            self.vkeyfunc = lambda state : state
        else:
            self.vkeyfunc = vkeyfunc

        if nsakeyfunc is None:
            self.nsakeyfunc    =  namedtuple('qkey', ['state' 'action'])
        else:
            self.nsakeyfunc = nsakeyfunc

        if nskeyfunc is None:
            self.nskeyfunc     = lambda state : state
        else:
            self.nskeyfunc = nskeyfunc
     
    def get_eps(self):
        return self.eps_gready

    def get_step(self):
        return self.step

    def update_q(self, state, action, reward):
        q_key = self.qkeyfunc(state, action, reward)
        self.Q[q_key] = self.Q.get(q_key, 0) + reward
        
    def update_v(self, state, action):
        v_key = self.vkeyfunc(state)
        self.V[v_key] = self.Nsa.get(v_key, 0) + reward

    def update_ns(self, state):
        n_key  = self.nsakeyfunc(state)
        self.Ns[n_key] = self.Ns.get(n_key, 0) + 1

    def update_nsa(self, state, action):
        nsa_key = self.nsakeyfunc(state)
        self.Nsa[nsa_key] = self.Ns.get(nsa_key, 0) + 1

    def update_learnig_vars(self, state, action, reward):
        self.update_ns(state)
        self.update_nsa(state, action)
        self.update_q(state, action, reward)
        self.update_v(state, action)
