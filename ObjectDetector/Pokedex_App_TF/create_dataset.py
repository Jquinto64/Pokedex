# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 22:44:31 2019

@author: jquin
"""

# Splits dataset into training 
import os
import shutil
import random

# Count files w/ specific names
DIR = 'C:\\Users\jquin\\desktop\\pokedex_app\\dataset'
destTrain = os.path.sep.join([DIR,'train']) # Define training destination
destTest = os.path.sep.join([DIR,'test'])# Define testing destination

fileList = os.listdir(DIR)

def MoveImages(listName, destination):
    for image in listName:
        transferName = os.path.sep.join([DIR, image])
        print("Moving: ", transferName, " to ", destination)
        shutil.move(transferName, destination)
        
def MoveFile(name):
    moveList = [] # Files to be moved
    
    # Create list of all desired files
    for x in fileList:
        if name in x:
            moveList.append(x)
    
    # Shuffle moving list
    random.seed(42)
    random.shuffle(moveList)
    
    # 20 % goes into testing, 80 % into training
    # Compute variable to determine split index
    i = int(len(moveList) * 0.8)
    
    # Split dataset/pokemon 
    trainList = moveList[:i]
    testList = moveList[i:]
    
    MoveImages(trainList, destTrain)
    MoveImages(testList, destTest)
    
def Rename(imageType):
    i = 0
    newName = "_"
    
    if imageType == destTrain:
        newName = "train"
    elif imageType == destTest:
        newName = "test"

    imageSet = os.listdir(imageType)

    for im in imageSet:
        extension = os.path.splitext(im)[1]
        saveName = os.path.sep.join([imageType, newName + str(i) + str(extension)])
        imName = os.path.sep.join([imageType, im])
        os.rename(imName, saveName)
        i += 1

############ STEP 1: SPLIT DATASETS ##################################################################
    
#pokemonList = ["bulbasaur","pikachu","mewtwo","rayquaza", "charamander", "jigglypuff", "squirtle"]
#
#for pokemon in pokemonList:
#    MoveFile(pokemon)
    
############ STEP 2: RENAME TO AVOID XML FILE CONFLICTS #############################################

#Rename(destTrain)
#Rename(destTest)

######################################################################################################
#print("Total Images:", len(fileList) - 2)
#pikachuCount = print("Pikachu Images: ", len([x for x in fileList if "pikachu" in x]))
#bulbCount = print("Bulbasaur Images: ", len([x for x in fileList if "bulbasaur" in x]))
#mewCount = print("Mewtwo Images: ", len([x for x in fileList if "mewtwo" in x]))
#charCount = print("Charamander Images: ", len([x for x in fileList if "charamander" in x]))
#sqrtlCount = print("Squirtle Images: ", len([x for x in fileList if "squirtle" in x]))
#jiggCount = print("Jigglypuff Images: ", len([x for x in fileList if "jigglypuff" in x]))
#rayCount = print("rayquaza Images: ", len([x for x in fileList if "rayquaza" in x]))




        


