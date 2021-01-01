# Table of Contents <!-- omit in toc -->
- [1. Overview](#1-overview)
  - [1.1. Goal of the project](#11-goal-of-the-project)
  - [1.2. Code structure](#12-code-structure)
# 1. Overview
In this project, I simulated a Monopoly game, focusing only on the movements that the players make across the board. This implies that the financial part of the game is not considered, as it does not affect the way in which players move.

Movement is strictly deterministic and regulated solely by the chain of actions triggered by the dices throw.

## 1.1. Goal of the project
Which are the spaces in which players end up stopping most frequently during a Monopoly game? This script wants to provide an analytical answer to this question.

One might be tempted to think that the probability of stopping is uniformly distributed across the board. However, this is not entirely true because of two game components:
- The jail
- The Chances/Community Chest

## 1.2. Code structure
There are four scripts:
- **monopoly.py**: the main file of the project. It puts together the other scripts, running the complete game process. The function game_analytics returns a dictionary where the data on the spaces' stops are stored.
- **player.py**: contains class to create player objects which move across the board.
- **cell.py**: contains class to create spaces objects which store the info on stops and trigger specific effects.
- **chance.py**: contains class to crete chances and community chests objects, which apply special effects to the player.