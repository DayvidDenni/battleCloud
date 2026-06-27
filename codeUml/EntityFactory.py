#!/usr/bin/python
# -*- coding: utf-8 -*-
from codeUml.Background import Background


class EntityFactory:


    @staticmethod
    def get_entity(entity_name: str, position=(0,0)) :
        match entity_name :
            case 'LevelBG':
              list_bg = []
              for i in range(4) :
                  list_bg.append(Background(f'LevelBG{i}',position))
              return list_bg
