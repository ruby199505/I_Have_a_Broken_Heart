# -*- coding: utf-8 -*-
from game import Game
from agent import AgentRandom, AgentMedium, MyAgent

import logging
import random


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    agents = [AgentMedium('Iron Man'), AgentMedium('Superman'),
              MyAgent('Batman'), AgentMedium('Spiderman')]
    scores = {agent.id: 0 for agent in agents}

    for _ in range(1000):
        random.shuffle(agents)
        game = Game(agents)

        game.set_game()

        for i, score in enumerate(game.play()):
            scores[agents[i].id] += score

    print(scores)
