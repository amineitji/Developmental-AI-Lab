# INSTALLER L'ENVIRONNEMENT

Cette page est une première étape pour interfacer ce tutoriel avec un robot utilisant ROS, tel que le TurtleBot. 

Si vous faites seulement le TP de Master IA, ou êtes intéressé par interfacer ce tutoriel avec le robot Osoyoo, inutile de lire cette page. 

## Installer ROS dans une machine virtuelle 

Pour installer l'environnement ROS dans une machine virtuelle VirtualBox, suivez les étapes 1 et 2 de la procédure [Configuration de l'environnement de travail](https://github.com/UCLy/INIT/wiki/Configuration-de-l'environnement-de-travail).

## Télécharger les fichiers TestROS

Dans le terminal, entrer :

```
cd ~/catkin_ws/src/
git clone https://github.com/OlivierGeorgeon/TestROS.git
```

## Configurer world.py

Dans le terminal, entrer :

```
cd ~/catkin_ws/src/TestROS
```

Ouvrir world.py

```
gedit world.py
```

Au début du fichier world.py, décommenter la ligne suivante pour importer le programme turtlesim_enacter : 

```
from turtlesim_enacter import TurtleSimEnacter
```

A la fin du fichier world.py, sélectionner l'environnement TurtleSimEnacter() en commentant et décommentant les lignes suivantes : 

```
# e = Environment1()
# e = Environment2()
e = TurtleSimEnacter()
```

# EXECUTER 

## Lancer le simulateur turtlesim

Pour lancer ROS, dans un terminal, faire :

```
roscore
```

![Figure_lancer_roscore](https://user-images.githubusercontent.com/11695651/83604210-18432900-a576-11ea-9980-9165268d2eae.PNG)

Laisser ce terminal ouvert.

Pour lancer le simulateur turtlesim, ouvrir un nouveau terminal et faire :

```
rosrun turtlesim turtlesim_node
```

Le simulateur turtlesim se lance (Figure 1).

![Figure2_1a](https://user-images.githubusercontent.com/11695651/80861149-ed12a480-8c6c-11ea-9485-a5b6eb1924b1.PNG)

_Figure 1: Turtlesim_

## Tester turtlesim_enacter.py

Dans un nouveau terminal, executer turtlesim_enacter.py:

```
cd ~/catkin_ws/src/TestROS
./turtlesim_enacter.py
```

Suivez les instructions pour contrôler le mouvement de la tortue (Figure 2).

![Figure2_3](https://user-images.githubusercontent.com/11695651/80861255-a1acc600-8c6d-11ea-98a3-4f93d8131466.PNG)

_Figure 2: controler la tortue_

## Lancer l'agent

Dans un nouveau terminal, faire :

```
cd ~/catkin_ws/src/TestROS
```

Si vous utilisez votre propre fichier world.py, vous devrez peut être lui attribuer les droits d'exécution : 

```
chmod +x world.py
```

Executer world.py : 

```
./world.py
```

Le simulateur exécute les interactions commandées par l'agent, et le terminal affiche la trace d'interaction au fur et à mesure (Figure 3).

![Figure2_4](https://user-images.githubusercontent.com/11695651/80861318-39aaaf80-8c6e-11ea-8086-c529eff70051.PNG)

_Figure 3: L'agent interagit avec l'environnement dans le simulateur_