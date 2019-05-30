import math

class Environment(object):

    def __init__(self):
        # robot end-effect position x = state[0]
        # robot end-effect velocity x_ = state[1]
        # human-robot force fh = state[2]
        self.state = [0, 0, 0]
        self.count = 0
        self.reward_list = []

    def apply_action(self, action):
        u = action
        self.get_current_state(u)
        reward = self.get_reward()
        return reward, self.state

    def get_state_variable(self,variable_name):

        if variable_name == 'x':
            return self.state[0]
        elif variable_name == "x_":
            return self.state[1]
        elif variable_name == "fh":
            return self.state[2]

    def set_state_variable(self,variable_name,value):

        if variable_name == 'x':
            self.state[0] = value
        elif variable_name == "x_":
            self.state[1] = value
        elif variable_name == "fh":
            self.state[2] = value

    def get_current_state(self,u):
        xd = 10
        kd = 1
        kp = 2
        ke = 1
        md = 3
        h = 0.02
        # The dynamics of the human-robot physical interaction system
        fh_ = (ke * (xd - self.get_state_variable('x')) - kp * self.get_state_variable('fh')) / kd
        x__ = (self.get_state_variable('fh') - u * self.get_state_variable('x_')) / md
        self.x___ = (fh_ - u * x__) / md
        self.set_state_variable('x', self.get_state_variable('x') + self.get_state_variable('x_') * h)
        self.set_state_variable('x_', self.get_state_variable('x_') + x__ * h)
        self.set_state_variable('fh', self.get_state_variable('fh') + fh_ * h)

    def get_reward(self):
        reward = -(self.x___ * self.x___)
        return reward

        # reward = -(self.get_state_variable('fh') * self.get_state_variable('fh') + self.get_state_variable('x_') * self.get_state_variable('x_'))

        # reward_agent_rate = 0
        # if self.count < 10:
        #     reward_controller_rate = -(self.get_state_variable('x_') * self.get_state_variable('x_') + self.get_state_variable('fh') * self.get_state_variable('fh'))
        #     self.reward_list.append(reward_controller_rate)
        #     self.count += 1
        # else:
        #     reward_agent_rate = sum(self.reward_list)
        #     self.count = 0
        #     self.reward_list = []
        # return reward_agent_rate


