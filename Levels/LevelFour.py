import AppEngine
from AppEngine import *

import ObjectClasses.Consumable as co
import ObjectClasses.Weapon as wn
import ObjectClasses.Item as im

import LevelParser
import Spritesheet

import random


class StageFour():
    def __init__(self):
        self.groundTiles = []
        self.obstacleTiles = []
        self.hazards = []

        self.lvl4 = LevelParser.Parser("Level Four")
        self.lvl4.parse()

        self.itemInfo = [] # items here: name, x, y

        self.items = []

    def generateGround(self):
        self.lvl4.generate_ground(self.groundTiles)

    def generateObstacles(self):
        self.lvl4.generate_obstacles(self.obstacleTiles)

    def generateHazards(self):
        self.lvl4.generate_hazards(self.hazards)

    def destroy(self):
        for i in self.obstacleTiles:
            i.sprite.destroy()
        #for c in self.hazards:
        #    c.sprite.destroy()
        for f in self.groundTiles:
            f.destroy()
        self.obstacleTiles.clear()
        self.hazards.clear()
        self.groundTiles.clear()
        self.items.clear()
        self.stopMusic()

    def spawnTreasure(self):
        if len(self.items) > 0:
            temp = []
            for item in self.items:
                if item.spriteImage.y != 905:
                    item.spriteImage.destroy()
                    item.spriteImage = None
                    del item
                else:
                    temp.append(item)
            self.items = temp
                    
        else:
            for x in range(len(self.itemInfo)):
                if self.itemInfo[x][3] == "co":
                    self.items.append(co.Consumable(self.itemInfo[x][0], self.itemInfo[x][1], self.itemInfo[x][2]))
                elif self.itemInfo[x][3] == "wn":
                    self.items.append(wn.Weapon(self.itemInfo[x][0], self.itemInfo[x][1], self.itemInfo[x][2]))
                elif self.itemInfo[x][3] == "im":
                    self.items.append(im.Item(self.itemInfo[x][0], self.itemInfo[x][1], self.itemInfo[x][2]))

        return self.items

    def startMusic(self):
        au.playMusic("Music/Level1.ogg", -1)
    
    def stopMusic(self):
        au.stopMusic()

    def checkCollision(self, hero):
        heroRect = hero.main.get_rect(topleft=(hero.x, hero.y))
        heroRect.inflate_ip(10, 10)
        for f in self.obstacleTiles:
            fRect = f.sprite.main.get_rect(topleft=(f.sprite.x, f.sprite.y))
            if f.id_ == "stationary":
                if fRect.colliderect(heroRect):
                    if fRect.collidepoint(heroRect.midleft):
                        return "west"
                    if fRect.collidepoint(heroRect.midright):
                        return "east"
                    if fRect.collidepoint(heroRect.midtop):
                        return "north"
                    if fRect.collidepoint(heroRect.midbottom):
                        return "south"
        return ""
                
                
            
        

