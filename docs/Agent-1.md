# L'agent qui n'aimait pas s'ennuyer

Implémenter un agent qui : 
1. apprend à prédire le résultat (outcome) de ses action en fonction de son environnement. 
1. choisit une action différente quand ses prédictions sont correctes depuis trop longtemps (fixer un temps arbitraire, par exemple 4 cycles d'interaction).

L'agent peut choisir entre deux actions possibles : "0" ou "1".
Il peut recevoir deux outcome possibles : "0" ou "1".

L'anticipation se fait sur la base de l'hypothèse que la même action produira le même outcome. Il faut donc implémenter une mémoire des outcome obtenus pour chaque action. 

Tester l'agent dans l'environnement 1 et dans l'environnement 2.

La Figure 1 montre un exemple de trace obtenue dans l'environnement 1. Selon les particularités de votre implémentation, vous pouvez obtenir une trace un peu différente.

![Trace_agent1](https://user-images.githubusercontent.com/11695651/98649838-5a983f80-2338-11eb-821e-6d0e7d8d8490.png)

_Figure 1. La Satisfaction est un triplet (anticipation correcte, valeur de l'interaction, ennui). Pendant les 4 premiers pas, l'agent anticipe correctement l'outcome (dans cette implémentation, l'anticipation par défaut est 0 et par chance elle est juste). Au 4ème pas, il s'ennuie. Au 5ème pas, il choisit donc une action différente mais son anticipation est fausse. A partir du 6ème pas, il anticipe toujours correctement l'outcome._