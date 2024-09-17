# TESTER world.py

Le fichier [world.py](https://github.com/OlivierGeorgeon/TestROS/blob/master/world.py) contient le cadre général pour implémenter un agent interagissant avec un environnement. Le nom "world" vient du fait qu'il contient à la fois l'agent et son environnement (minimaliste).

Executer [world.py](https://github.com/OlivierGeorgeon/TestROS/blob/master/world.py)  dans votre IDE python favori, par exemple [pycharm](https://www.jetbrains.com/pycharm/). Vous obtenez la trace d'interaction de l'agent pendant 10 cycles d'interaction (Figure 1).

![Trace_agent_0](https://user-images.githubusercontent.com/11695651/138603283-edd42015-57cf-4834-881e-d61682069398.PNG)

_Figure 1: Trace d'interaction_

Cet agent choisit toujours l'action 0 et anticipe toujours le résultat 0. Il est donc toujours satisfait de son anticipation mais "malheureux" car cette interaction a pour valence -1.

# MODIFIER world.py

Faite 

* [Agent 1](Agent-1)
* [Agent 2](Agent-2)
* [Agent 3](Agent-3)
* [Agent 4](Agent-4)

A chaque fois, compléter les TODOs: 

1. Implémenter le mécanisme d'anticipation de votre agent.
1. Implémenter le mécanisme de décision de votre agent.
1. Définir les valeurs des interactions dans la table `hedonist_table`
1. Choisir l'environnement

Executer votre version de world.py pour voir la trace d'interaction de l'agent que vous avez implémenté avec l'environnement que vous avez choisi.



