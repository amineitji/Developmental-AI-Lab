# README of this Developmental AI tutorial project

This repository provides the code for the exercises in my course on Develipmental AI.
Follow the [wiki](https://github.com/OlivierGeorgeon/TestROS/wiki) to do the exercises (French).

[world.py](https://github.com/OlivierGeorgeon/TestROS/blob/master/world.py) provides the general framework to implement a developmental agent and test it in rudimentary environments. 
It is a standalone file that can run in any python environment.

[turtlepy_enacter](https://github.com/OlivierGeorgeon/TestROS/blob/master/turtlepy_enacter.py) provides the code for testing the develipmental agent in the TurtlePy environment.

[PetitCatTester.py](https://github.com/OlivierGeorgeon/TestROS/blob/master/PetitCatTester.py) provides the code for remote controlling the [PetitCat implementation of the Osoyoo car robot](https://github.com/OlivierGeorgeon/TestROS/wiki/Utiliser-le-robot-osyoo). 

[PetitCatEnacter.py](https://github.com/OlivierGeorgeon/TestROS/blob/master/PetitCatEnacter.py) provides the interface for the developmental agent to control the PetitCat robot. 

[turtlesim_enacter.py](https://github.com/OlivierGeorgeon/TestROS/blob/master/turtlesim_enacter.py) provides the interface for the developmental agent to control the [turtlesim simulator](http://wiki.ros.org/turtlesim). 
It requires a [ROS](https://www.ros.org/) installation. It is provided here as an intial step to let the developmental agent control a TurtleBot robot.
