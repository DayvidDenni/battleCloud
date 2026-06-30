#!/usr/bin/python
# -*- coding: utf-8 -*-
import random

from codeUml.Const import WIN_WIDTH, WIN_HEIGHT
from codeUml.Background import Background
from codeUml.Enemy import Enemy
from codeUml.Player import Player


class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str, position=(0,0)):
        match entity_name:
            case 'Level1BG':
                list_bg = []
                for i in range(4):
                    list_bg.append(Background(f'Level1BG{i}', (0, 0)))
                    list_bg.append(Background(f'Level1BG{i}', (WIN_WIDTH, 0)))
                return list_bg
            case 'Level2BG':
                list_bg = []
                for i in range(6):
                    list_bg.append(Background(f'Level2BG{i}', (0, 0)))
                    list_bg.append(Background(f'Level2BG{i}', (WIN_WIDTH, 0)))
                return list_bg
            case 'Player1':
                return Player('Player1', (12, WIN_HEIGHT / 2.5 - 40))
            case 'Player2':
                return Player('Player2', (12, WIN_HEIGHT / 2.5 + 40))
            case 'Enemy1':
                return Enemy('Enemy1', (WIN_WIDTH + 10, random.randint(40, WIN_HEIGHT - 35)))
            case 'Enemy2':
                return Enemy('Enemy2', (WIN_WIDTH + 10, random.randint(40, WIN_HEIGHT - 35)))
        return None
