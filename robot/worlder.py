import pygame, sys, os
from pygame.locals import *

import cafeinagame
from cafeinagame import *

import types

class Worlder():
    def __init__(self, content, out_X, out_Y):
        self.content = content
        # Outter limits to build from lists a world
        self.out_X = out_X
        self.out_Y = out_Y
        self.robot_position = [0,0]
        self.objective_position = [0,0]

    def build_world(self, world):
        if isinstance(world, types.ListType):
            return self.build_world_lst(world)
        else:
            return self.build_world_str(world)
            
    
    def build_world_lst(self, world):
        entities = []
        image = self.content.load_image('Wall.bmp')
        width = image.get_width()
        height = image.get_height()

        # Building the world
        # Initial y-position
        y = height * self.out_Y
        for row in world:
            # Reset x-position
            x = width * self.out_X
            for wall in row:
                # Set wall, robot or objective
                if wall == 1:
                    wallAnimation = cafeinagame.entities.Animation([image])
                    wallEntity = cafeinagame.entities.Entity(wallAnimation, [x,y])
                    entities.append(wallEntity)
                elif wall == 2:
                    self.robot_position = [x,y]
                elif wall == 3:
                    self.objective_position = [x,y]
                x += width
            y += height
        return entities
        
        
    def build_world_str(self, world):
        if world == '':
            return []
        entities = []
        walls = world.split('#')
        image = self.content.load_image('Wall.bmp')
        for wall in walls:
            positionXY = wall.split(';')
            x = int(positionXY[0])
            y = int(positionXY[1])

            wallAnimation = cafeinagame.entities.Animation([image])
            wallEntity = cafeinagame.entities.Entity(wallAnimation, [x,y])
            entities.append(wallEntity)            
        return entities

    def build_background(self, width, height):
        entities = []
        image = self.content.load_image('Back.bmp')
        for x in range(0, width, image.get_width()):
            for y in range(0, width, image.get_height()):
                backAnimation = cafeinagame.entities.Animation([image])
                backEntity = cafeinagame.entities.Entity(backAnimation, [x,y])
                entities.append(backEntity)            
        return entities

    

    def build_objective(self, position):
        images = self.content.load_images([['Objective-1.bmp', (255,0,255)],
                                           ['Objective-2.bmp', (255,0,255)],])
        animation = cafeinagame.entities.Animation(images, 120)
        return cafeinagame.entities.Entity(animation, position)
        
        
        
        
