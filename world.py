#!/usr/bin/env python
from turtlesim_enacter import TurtleSimEnacter

# Olivier Georgeon, 2020.
# This code is used to teach Develpmental AI.


class Agent:
    def __init__(self, _hedonist_table):
        """ Creating our agent """
        self.hedonist_table = _hedonist_table
        self._action = 0
        self.new_action = 0
        self.anticipated_outcome = 0
        self.anticipation_0 = 0
        self.anticipation_1 = 0
        self.ennui = 0
        self.Valeur_hedoniste_anticipee_pour_action_0 = 0
        self.Valeur_hedoniste_anticipee_pour_action_1 = 0

    def action(self, outcome):
        """ Computing the next action to enact """
        if self._action == 0:
            self.anticipation_0 = outcome
            self.Valeur_hedoniste_anticipee_pour_action_0 = self.hedonist_table[0][self.anticipation_0]
            if outcome == self.anticipated_outcome and self.Valeur_hedoniste_anticipee_pour_action_0 >= self.Valeur_hedoniste_anticipee_pour_action_1:
                self.new_action = self._action
            if self.ennui >= 3 or self.Valeur_hedoniste_anticipee_pour_action_0 <= self.Valeur_hedoniste_anticipee_pour_action_1:
                if self._action == 0:
                    self.new_action = 1
                else:
                    self.new_action = 0

        else:
            self.anticipation_1 = outcome
            self.Valeur_hedoniste_anticipee_pour_action_1 = self.hedonist_table[1][self.anticipation_1]
            if outcome == self.anticipated_outcome and self.Valeur_hedoniste_anticipee_pour_action_1 >= self.Valeur_hedoniste_anticipee_pour_action_0:
                self.new_action = self._action
            if self.ennui >= 3 or self.Valeur_hedoniste_anticipee_pour_action_1 <= self.Valeur_hedoniste_anticipee_pour_action_0:
                if self._action == 0:
                    self.new_action = 1
                else:
                    self.new_action = 0

        if self._action == self.new_action:
            self.ennui = self.ennui + 1
        else:
            self.ennui = 0
        if self.ennui >= 4:
            self.ennui = 0

        self._action = self.new_action

        return self._action

    def anticipation(self):
        """ computing the anticipated outcome from the latest action """
        if self._action == 0:
            self.anticipated_outcome = self.anticipation_0
        else:
            self.anticipated_outcome = self.anticipation_1
        return self.anticipated_outcome

    def satisfaction(self, new_outcome):
        """ Computing a tuple representing the agent's satisfaction after the last interaction """
        # True if the anticipation was correct
        anticipation_satisfaction = (self.anticipated_outcome == new_outcome)
        # The value of the enacted interaction
        hedonist_satisfaction = self.hedonist_table[self._action][new_outcome]
        ennui = False
        if self.ennui == 3:
            ennui = True
        else :
            ennui = False
        return anticipation_satisfaction, hedonist_satisfaction, ennui


class Environment1:
    """ In Environment 1, action 0 yields outcome 0, action 1 yields outcome 1 """
    def outcome(self, action):
        if action == 0:
            return 0
        else:
            return 1


class Environment2:
    """ In Environment 2, action 0 yields outcome 1, action 1 yields outcome 0 """
    def outcome(self, action):
        if action == 0:
            return 1
        else:
            return 0


def world(agent, environment):
    """ The main loop controlling the interaction of the agent with the environment """
    outcome = 0
    for i in range(15):
        action = agent.action(outcome)
        outcome = environment.outcome(action)
        print(" Action: " + str(action) + ", Anticipation: " + str(agent.anticipation()) + ", Outcome: " + str(outcome)
              + ", Satisfaction: " + str(agent.satisfaction(outcome)))


# hedonist_table = [[0, 1], [0, 1]]
hedonist_table = [[-1, 1], [-1, 1]]
a = Agent(hedonist_table)
# e = Environment1()
# e = Environment2()
e = TurtleSimEnacter()

world(a, e)
