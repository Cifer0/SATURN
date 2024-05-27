# -*- coding: cp1252 -*-
#########################################################
#########################################################
################### BOILERPLATE STUFF ###################
#########################################################
#########################################################

import os
import random
import math
import VisionEgg
from VisionEgg import *
from PIL import Image, ImageDraw
VisionEgg.start_default_logging(); VisionEgg.watch_exceptions()
from VisionEgg.Core import *
from VisionEgg.FlowControl import Presentation
#from VisionEgg.Dots import DotArea2D
from VisionEgg.Textures import *
from VisionEgg.Text import *
from VisionEgg.MoreStimuli import *
from numpy import *
import pygame
from time import time, clock
import copy
#import winsound
import OpenGL.GL as gl
#### Note: the clock() function needs to be called once to provide a zero-mark.
print clock()
from array import array
import OpenGL.GL as gl

### timestamp
from time import gmtime, strftime, localtime
from time import sleep
print strftime("%Y-%m-%d %H:%M:%S", localtime())


## in case the program is stored ina  convoluted folder,
## this marks "home" for us
BASEPATH=os.path.realpath('')

RESET = "False"

##########################################
##########################################
####### Open a Vision Egg window #########
##########################################
##########################################
## This little module let's us bypass the VisionEgg screen that usually comes up.
## Modify screen width, etc. by modifying the values in the next four lines.
os.environ['SDL_VIDEO_WINDOW_POS']="1500,300"
refresh_rate = 120
screen_width = 1024 ##1024 x 600 for the tab
screen_height = 600
bits_per_pixel = 8
def __VEggConfig():
    VisionEgg.start_default_logging(); VisionEgg.watch_exceptions()
    VisionEgg.config.VISIONEGG_GUI_INIT = 0
    VisionEgg.config.VISIONEGG_FRAMELESS_WINDOW = 1
    VisionEgg.config.VISIONEGG_FULLSCREEN = 0
    VisionEgg.config.VISIONEGG_MONITOR_REFRESH_HZ = refresh_rate
    VisionEgg.config.VISIONEGG_SCREEN_W = screen_width
    VisionEgg.config.VISIONEGG_SCREEN_H = screen_height
    VisionEgg.config.VISIONEGG_PREFERRED_BPP = bits_per_pixel
## Now, we'll initialize VisionEgg:
__VEggConfig()
screen = get_default_screen()
screen.parameters.bgcolor = (0,0,0)


########################################################################
########################  Load up all the images  ######################
########################################################################
os.chdir("bin/")
##


#<$%^>
if not os.path.isfile("DO_NOT_DELETE_THIS_STATE.txt"):
    A=open("DO_NOT_DELETE_THIS_STATE.txt","w")
    A.write('OREGON')
    A.close()
A=open("DO_NOT_DELETE_THIS_STATE.txt","r")
## STATE_WHEN_PROGRAM_INITIATED will double as the correct answer...
## if we change it, it will close the program in the process of changing...
STATE_WHEN_PROGRAM_INITIATED=A.read().splitlines()
A.close()
STATE_SELECTION_BLUEBOX=Texture("__mask_STATE_selection.png")
STATE_SELECTION_BACKGROUND=Texture("__STATE_selection.png")
list_states_for_selecting_current_state=["ALABAMA",  "ALASKA","ARIZONA",
                                         "ARKANSAS","CALIFORNIA","COLORADO",
                                         "CONNECTICUT","DELAWARE","FLORIDA", 
                                         "GEORGIA","HAWAII","IDAHO",
                                         "ILLINOIS",  "INDIANA","IOWA",
                                         "KANSAS","KENTUCKY","LOUISIANA", 
                                         "MAINE","MARYLAND","MASSACHUSETTS",
                                         "MICHIGAN","MINNESOTA","MISSISSIPPI",
                                         "MISSOURI",  "MONTANA","NEBRASKA",
                                         "NEVADA","NEW HAMPSHIRE","NEW JERSEY",
                                         "NEW MEXICO","NEW YORK","NORTH CAROLINA",
                                         "NORTH DAKOTA","OHIO","OKLAHOMA",
                                         "OREGON",   "PENNSYLVANIA","RHODE ISLAND",
                                         "SOUTH CAROLINA","SOUTH DAKOTA","TENNESSEE",
                                         "TEXAS","UTAH","VERMONT","VIRGINIA",
                                         "WASHINGTON","WEST VIRGINIA","WISCONSON",
                                         "WYOMING"]
CURRENTLIST=list_states_for_selecting_current_state
sat101 = Text(text=CURRENTLIST[0],color=(0,0,0),position=(56,541),font_size=42,anchor='upperleft')
sat102 = Text(text=CURRENTLIST[1],color=(0,0,0),position=(56,511),font_size=42,anchor='upperleft')
sat103 = Text(text=CURRENTLIST[2],color=(0,0,0),position=(56,481),font_size=42,anchor='upperleft')
sat104 = Text(text=CURRENTLIST[3],color=(0,0,0),position=(56,451),font_size=42,anchor='upperleft')
sat105 = Text(text=CURRENTLIST[4],color=(0,0,0),position=(56,421),font_size=42,anchor='upperleft')
sat106 = Text(text=CURRENTLIST[5],color=(0,0,0),position=(56,391),font_size=42,anchor='upperleft')
sat107 = Text(text=CURRENTLIST[6],color=(0,0,0),position=(56,361),font_size=42,anchor='upperleft')
sat108 = Text(text=CURRENTLIST[7],color=(0,0,0),position=(56,331),font_size=42,anchor='upperleft')
sat109 = Text(text=CURRENTLIST[8],color=(0,0,0),position=(56,301),font_size=42,anchor='upperleft')
sat110 = Text(text=CURRENTLIST[9],color=(0,0,0),position=(56,270),font_size=42,anchor='upperleft')
sat111 = Text(text=CURRENTLIST[10],color=(0,0,0),position=(56,241),font_size=42,anchor='upperleft')
sat112 = Text(text=CURRENTLIST[11],color=(0,0,0),position=(56,211),font_size=42,anchor='upperleft')
sat113 = Text(text=CURRENTLIST[12],color=(0,0,0),position=(56,181),font_size=42,anchor='upperleft')
sat114 = Text(text=CURRENTLIST[13],color=(0,0,0),position=(56,151),font_size=42,anchor='upperleft')
sat115 = Text(text=CURRENTLIST[14],color=(0,0,0),position=(56,121),font_size=42,anchor='upperleft')
sat116 = Text(text=CURRENTLIST[15],color=(0,0,0),position=(56,91),font_size=42,anchor='upperleft')
sat117 = Text(text=CURRENTLIST[16],color=(0,0,0),position=(56,61),font_size=42,anchor='upperleft')
sat118 = Text(text=CURRENTLIST[17],color=(0,0,0),position=(56,31),font_size=42,anchor='upperleft')
#
sat201 = Text(text=CURRENTLIST[18],color=(0,0,0),position=(367,541),font_size=42,anchor='upperleft')
sat202 = Text(text=CURRENTLIST[19],color=(0,0,0),position=(367,511),font_size=42,anchor='upperleft')
sat203 = Text(text=CURRENTLIST[20],color=(0,0,0),position=(367,481),font_size=42,anchor='upperleft')
sat204 = Text(text=CURRENTLIST[21],color=(0,0,0),position=(367,451),font_size=42,anchor='upperleft')
sat205 = Text(text=CURRENTLIST[22],color=(0,0,0),position=(367,421),font_size=42,anchor='upperleft')
sat206 = Text(text=CURRENTLIST[23],color=(0,0,0),position=(367,391),font_size=42,anchor='upperleft')
sat207 = Text(text=CURRENTLIST[24],color=(0,0,0),position=(367,361),font_size=42,anchor='upperleft')
sat208 = Text(text=CURRENTLIST[25],color=(0,0,0),position=(367,331),font_size=42,anchor='upperleft')
sat209 = Text(text=CURRENTLIST[26],color=(0,0,0),position=(367,301),font_size=42,anchor='upperleft')
sat210 = Text(text=CURRENTLIST[27],color=(0,0,0),position=(367,270),font_size=42,anchor='upperleft')
sat211 = Text(text=CURRENTLIST[28],color=(0,0,0),position=(367,241),font_size=42,anchor='upperleft')
sat212 = Text(text=CURRENTLIST[29],color=(0,0,0),position=(367,211),font_size=42,anchor='upperleft')
sat213 = Text(text=CURRENTLIST[30],color=(0,0,0),position=(367,181),font_size=42,anchor='upperleft')
sat214 = Text(text=CURRENTLIST[31],color=(0,0,0),position=(367,151),font_size=42,anchor='upperleft')
sat215 = Text(text=CURRENTLIST[32],color=(0,0,0),position=(367,121),font_size=42,anchor='upperleft')
sat216 = Text(text=CURRENTLIST[33],color=(0,0,0),position=(367,91),font_size=42,anchor='upperleft')
sat217 = Text(text=CURRENTLIST[34],color=(0,0,0),position=(367,61),font_size=42,anchor='upperleft')
sat218 = Text(text=CURRENTLIST[35],color=(0,0,0),position=(367,31),font_size=42,anchor='upperleft')
#
sat301 = Text(text=CURRENTLIST[36],color=(0,0,0),position=(679,541),font_size=42,anchor='upperleft')
sat302 = Text(text=CURRENTLIST[37],color=(0,0,0),position=(679,511),font_size=42,anchor='upperleft')
sat303 = Text(text=CURRENTLIST[38],color=(0,0,0),position=(679,481),font_size=42,anchor='upperleft')
sat304 = Text(text=CURRENTLIST[39],color=(0,0,0),position=(679,451),font_size=42,anchor='upperleft')
sat305 = Text(text=CURRENTLIST[40],color=(0,0,0),position=(679,421),font_size=42,anchor='upperleft')
sat306 = Text(text=CURRENTLIST[41],color=(0,0,0),position=(679,391),font_size=42,anchor='upperleft')
sat307 = Text(text=CURRENTLIST[42],color=(0,0,0),position=(679,361),font_size=42,anchor='upperleft')
sat308 = Text(text=CURRENTLIST[43],color=(0,0,0),position=(679,331),font_size=42,anchor='upperleft')
sat309 = Text(text=CURRENTLIST[44],color=(0,0,0),position=(679,301),font_size=42,anchor='upperleft')
sat310 = Text(text=CURRENTLIST[45],color=(0,0,0),position=(679,270),font_size=42,anchor='upperleft')
sat311 = Text(text=CURRENTLIST[46],color=(0,0,0),position=(679,241),font_size=42,anchor='upperleft')
sat312 = Text(text=CURRENTLIST[47],color=(0,0,0),position=(679,211),font_size=42,anchor='upperleft')
sat313 = Text(text=CURRENTLIST[48],color=(0,0,0),position=(679,181),font_size=42,anchor='upperleft')
sat314 = Text(text=CURRENTLIST[49],color=(0,0,0),position=(679,151),font_size=42,anchor='upperleft')

PREMADE_VIEWPORT_STATES_SELECT= VisionEgg.Core.Viewport(screen=screen, size=screen.size, stimuli=[sat101,sat102,sat103,sat104,sat105,sat106,sat107,sat108,
                                                                                                  sat109,sat110,sat111,sat112,sat113,sat114,sat115,sat116,
                                                                                                  sat117,sat118,
                                                                                                  sat201,sat202,sat203,sat204,sat205,sat206,sat207,sat208,
                                                                                                  sat209,sat210,sat211,sat212,sat213,sat214,sat215,sat216,
                                                                                                  sat217,sat218,
                                                                                                  sat301,sat302,sat303,sat304,sat305,sat306,sat307,sat308,
                                                                                                  sat309,sat310,sat311,sat312,sat313,sat314])
#</$%^>


REVIEWSCREEN=Texture("_review_screen.png")

HOMESCREEN=Texture("_homescreen2.png")
NURSESCREEN=Texture("_NurseScreen.png")
EPICSCREEN=Texture("_EPICscreen.png")
ESCAPESCREEN=[Texture("_escapeScreen_1stRound.png"),
              Texture("_escapeScreen_2ndRound.png"),
              Texture("_escapeScreen_early.png"),
              Texture("_escapeScreen_late.png")]
FINALSCREEN=Texture("_FINALscreen.png")

wordscreens=[
  Texture("_blankgray.png"),
  Texture("_apple.png"),
  Texture("_blankgray.png"),
  Texture("_pen.png"),
  Texture("_blankgray.png"),
  Texture("_tie.png"),
  Texture("_blankgray.png"),
  Texture("_house.png"),
  Texture("_blankgray.png"),
  Texture("_car.png"),
  Texture("_blankgray.png")]

instructbackgrounds=[
  Texture("_instruction01.png"),
  Texture("_instruction02.png"),
  Texture("_instruction03.png"),
  Texture("_instruction04.png"),
  Texture("placeholder_as_tasks_are_removed.png"),
  Texture("_instruction06b.png"),
  Texture("_instruction07.png"),
  Texture("placeholder_as_tasks_are_removed.png"),
  Texture("_instruction09.png"),
  Texture("_instruction10.png"),
  Texture("_instruction11.png"),
  Texture("placeholder_as_tasks_are_removed.png")]

## a couple buttons to help us out...
greensquare=Texture("_greenbox.png")
redsquare=Texture("_redbox.png")

notyetboxes=[
  Texture("_notYetboxJ.png"),
  Texture("_notYetboxFRUIT_toFEW.png"),
  Texture("_notYetboxFRUIT_toMANY.png"),
  Texture("_notYetboxNUMBER_first.png"),
  Texture("_notYetboxMONTH.png"),
  Texture("_notYetboxDAY.png"),
  Texture("_notYetboxYEAR.png"),
  Texture("_notYetboxSTATE.png"),
  Texture("_notYetboxSTATEMENT.png"),
  Texture("_notYetboxLETTER.png"),
  Texture("_notYetboxNUMBER_recall.png"),
  Texture("_notYetboxJagain.png"),
  Texture("_notYetboxSHAPE.png"),
  Texture("_notYetboxDOLLAR.png"),
  Texture("_notYetbox5_tooFEW.png"),
  Texture("_notYetbox5_tooMANY.png"),
  Texture("_notYetboxTRAILSa.png"),
  Texture("_notYetbox2_tooFEW.png"),
  Texture("_notYetbox2_tooMANY.png")]
  
masks=[
  Texture("_mask_PICK_the_J_word.png"),
  Texture("_mask_PICK_the_FRUIT.png"),
  Texture("_mask_MONTH.png"),
  Texture("_mask_DAY.png"),
  Texture("_mask_STATE.png"),
  Texture("_mask_PHRASE.png"),
  Texture("_mask_5word.png"),
  Texture("_mask_DRAWINGs.png")]

taskbackgrounds=[
  Texture("_PICK_the_J_word.png"), ## 0
  Texture("_PICK_the_FRUIT.png"), ## 1
  Texture("_NUMBERPAD.png"),
  Texture("placeholder_as_tasks_are_removed.png"), 
  Texture("_WHATyear.png"),
  Texture("_MONTHS.png"),
  Texture("_DAYS.png"),
  Texture("_STATE.png"),
  Texture("_PHRASE.png"),
  Texture("_NUMBERPAD_again.png"),
  Texture("_PICK_the_J_word_again.png"),
  Texture("placeholder_as_tasks_are_removed.png"),
  Texture("_fiveWORDS.png"),
  Texture("_SLUMS_math1.png"),
  Texture("_SLUMS_math2.png"), #14
  Texture("placeholder_as_tasks_are_removed.png"),
  Texture("_instruction_drawings.png")]

drawingbackgrounds=[
  Texture("_drawings_01.png"), ## 0
  Texture("_drawings_02.png"), ## 1
  Texture("_drawings_03.png"),
  Texture("_drawings_04.png")]

trailsbackgrounds=[
    Texture("_backgroundTRAILS_A_sample.png"),
    Texture("_backgroundTRAILS_B_sample.png")]

TRAILSmaskRED=Texture("_TRAILSmaskRED.png")
TRAILSmaskGREEN=Texture("_TRAILSmaskGREEN.png")


stroopMASK=Texture("_mask_PICK_the_J_word.png")
stroopINSTRUCT=Texture("_instruction_stroop2.png")
stroopSCREEN=[
    Texture("_stroop_01b.png"), 
    Texture("_stroop_02b.png"), 
    Texture("_stroop_03b.png"),
    Texture("_stroop_04.png"),
    Texture("_stroop_05.png"),
    Texture("_stroop_06.png"),
    Texture("_stroop_07.png"),
    Texture("_stroop_08.png"),
    Texture("_stroop_09.png"),
    Texture("_stroop_10.png"),
    Texture("_stroop_11.png"),
    Texture("_stroop_12.png"),
    Texture("_stroop_13.png"),
    Texture("_stroop_14.png"),
    Texture("_stroop_15.png")]
stroopNOTYETreselect=Texture("_notYetbox_STROOP_REselect.png")
stroopNOTYETselect=Texture("_notYetbox_STROOP_select.png")
## the actual stroop items are hard-coded (not randomized)
## this way, in 15 items, "red", "green" and "blue" each appear five times. #<--update: this all changes slightly with the three-trial lead-in with "and" "book" "table"
## also, the color options (red, green, and blue) are each used five times.
## and each word is matched with one incongruent color twice, and the other three times.
## and there are no back-to-back uses of "red", "blue", or "green"
## and the correct color choice changes from each trial to the next.
stroopWORDorder=["hand","book","table","green","red",
                 "blue","red","blue","green","red",
                 "blue","red","green","blue","green"]
stroopWORDcolor=["blue","red","green","blue","green",
                 "red","blue","green","red","green",
                 "red","blue","red","green","blue"]


ERRORBUNDLE=[0,0]

os.chdir(BASEPATH)


  ### to change your state, go to the line
#             if RESPONSE == list_states[36]:
  ### and switch as needed. (numbered list, starting at zero, corresponding
  ### to position in list_states defined here)
  ##  For instance, change 36 to 0 if you're in ALABAMA,
  ### change the 36 to 2 if you're in ARIZONA, 


list_states=["ALABAMA",  "ALASKA","ARIZONA",
             "ARKANSAS","CALIFORNIA","COLORADO",
             "CONNECTICUT","DELAWARE","FLORIDA", 
             "GEORGIA","HAWAII","IDAHO",
             "ILLINOIS",  "INDIANA","IOWA",
             "KANSAS","KENTUCKY","LOUISIANA", 
             "MAINE","MARYLAND","MASSACHUSETTS",
             "MICHIGAN","MINNESOTA","MISSISSIPPI",
             "MISSOURI",  "MONTANA","NEBRASKA",
             "NEVADA","NEW HAMPSHIRE","NEW JERSEY",
             "NEW MEXICO","NEW YORK","NORTH CAROLINA",
             "NORTH DAKOTA","OHIO","OKLAHOMA",
             "OREGON",   "PENNSYLVANIA","RHODE ISLAND",
             "SOUTH CAROLINA","SOUTH DAKOTA","TENNESSEE",
             "TEXAS","UTAH","VERMONT","VIRGINIA",
             "WASHINGTON","WEST VIRGINIA","WISCONSON",
             "WYOMING"]
CURRENTLIST=list_states
st101 = Text(text=CURRENTLIST[0],color=(0,0,0),position=(56,541),font_size=42,anchor='upperleft')
st102 = Text(text=CURRENTLIST[1],color=(0,0,0),position=(56,511),font_size=42,anchor='upperleft')
st103 = Text(text=CURRENTLIST[2],color=(0,0,0),position=(56,481),font_size=42,anchor='upperleft')
st104 = Text(text=CURRENTLIST[3],color=(0,0,0),position=(56,451),font_size=42,anchor='upperleft')
st105 = Text(text=CURRENTLIST[4],color=(0,0,0),position=(56,421),font_size=42,anchor='upperleft')
st106 = Text(text=CURRENTLIST[5],color=(0,0,0),position=(56,391),font_size=42,anchor='upperleft')
st107 = Text(text=CURRENTLIST[6],color=(0,0,0),position=(56,361),font_size=42,anchor='upperleft')
st108 = Text(text=CURRENTLIST[7],color=(0,0,0),position=(56,331),font_size=42,anchor='upperleft')
st109 = Text(text=CURRENTLIST[8],color=(0,0,0),position=(56,301),font_size=42,anchor='upperleft')
st110 = Text(text=CURRENTLIST[9],color=(0,0,0),position=(56,270),font_size=42,anchor='upperleft')
st111 = Text(text=CURRENTLIST[10],color=(0,0,0),position=(56,241),font_size=42,anchor='upperleft')
st112 = Text(text=CURRENTLIST[11],color=(0,0,0),position=(56,211),font_size=42,anchor='upperleft')
st113 = Text(text=CURRENTLIST[12],color=(0,0,0),position=(56,181),font_size=42,anchor='upperleft')
st114 = Text(text=CURRENTLIST[13],color=(0,0,0),position=(56,151),font_size=42,anchor='upperleft')
st115 = Text(text=CURRENTLIST[14],color=(0,0,0),position=(56,121),font_size=42,anchor='upperleft')
st116 = Text(text=CURRENTLIST[15],color=(0,0,0),position=(56,91),font_size=42,anchor='upperleft')
st117 = Text(text=CURRENTLIST[16],color=(0,0,0),position=(56,61),font_size=42,anchor='upperleft')
st118 = Text(text=CURRENTLIST[17],color=(0,0,0),position=(56,31),font_size=42,anchor='upperleft')
#
st201 = Text(text=CURRENTLIST[18],color=(0,0,0),position=(367,541),font_size=42,anchor='upperleft')
st202 = Text(text=CURRENTLIST[19],color=(0,0,0),position=(367,511),font_size=42,anchor='upperleft')
st203 = Text(text=CURRENTLIST[20],color=(0,0,0),position=(367,481),font_size=42,anchor='upperleft')
st204 = Text(text=CURRENTLIST[21],color=(0,0,0),position=(367,451),font_size=42,anchor='upperleft')
st205 = Text(text=CURRENTLIST[22],color=(0,0,0),position=(367,421),font_size=42,anchor='upperleft')
st206 = Text(text=CURRENTLIST[23],color=(0,0,0),position=(367,391),font_size=42,anchor='upperleft')
st207 = Text(text=CURRENTLIST[24],color=(0,0,0),position=(367,361),font_size=42,anchor='upperleft')
st208 = Text(text=CURRENTLIST[25],color=(0,0,0),position=(367,331),font_size=42,anchor='upperleft')
st209 = Text(text=CURRENTLIST[26],color=(0,0,0),position=(367,301),font_size=42,anchor='upperleft')
st210 = Text(text=CURRENTLIST[27],color=(0,0,0),position=(367,270),font_size=42,anchor='upperleft')
st211 = Text(text=CURRENTLIST[28],color=(0,0,0),position=(367,241),font_size=42,anchor='upperleft')
st212 = Text(text=CURRENTLIST[29],color=(0,0,0),position=(367,211),font_size=42,anchor='upperleft')
st213 = Text(text=CURRENTLIST[30],color=(0,0,0),position=(367,181),font_size=42,anchor='upperleft')
st214 = Text(text=CURRENTLIST[31],color=(0,0,0),position=(367,151),font_size=42,anchor='upperleft')
st215 = Text(text=CURRENTLIST[32],color=(0,0,0),position=(367,121),font_size=42,anchor='upperleft')
st216 = Text(text=CURRENTLIST[33],color=(0,0,0),position=(367,91),font_size=42,anchor='upperleft')
st217 = Text(text=CURRENTLIST[34],color=(0,0,0),position=(367,61),font_size=42,anchor='upperleft')
st218 = Text(text=CURRENTLIST[35],color=(0,0,0),position=(367,31),font_size=42,anchor='upperleft')
#
st301 = Text(text=CURRENTLIST[36],color=(0,0,0),position=(679,541),font_size=42,anchor='upperleft')
st302 = Text(text=CURRENTLIST[37],color=(0,0,0),position=(679,511),font_size=42,anchor='upperleft')
st303 = Text(text=CURRENTLIST[38],color=(0,0,0),position=(679,481),font_size=42,anchor='upperleft')
st304 = Text(text=CURRENTLIST[39],color=(0,0,0),position=(679,451),font_size=42,anchor='upperleft')
st305 = Text(text=CURRENTLIST[40],color=(0,0,0),position=(679,421),font_size=42,anchor='upperleft')
st306 = Text(text=CURRENTLIST[41],color=(0,0,0),position=(679,391),font_size=42,anchor='upperleft')
st307 = Text(text=CURRENTLIST[42],color=(0,0,0),position=(679,361),font_size=42,anchor='upperleft')
st308 = Text(text=CURRENTLIST[43],color=(0,0,0),position=(679,331),font_size=42,anchor='upperleft')
st309 = Text(text=CURRENTLIST[44],color=(0,0,0),position=(679,301),font_size=42,anchor='upperleft')
st310 = Text(text=CURRENTLIST[45],color=(0,0,0),position=(679,270),font_size=42,anchor='upperleft')
st311 = Text(text=CURRENTLIST[46],color=(0,0,0),position=(679,241),font_size=42,anchor='upperleft')
st312 = Text(text=CURRENTLIST[47],color=(0,0,0),position=(679,211),font_size=42,anchor='upperleft')
st313 = Text(text=CURRENTLIST[48],color=(0,0,0),position=(679,181),font_size=42,anchor='upperleft')
st314 = Text(text=CURRENTLIST[49],color=(0,0,0),position=(679,151),font_size=42,anchor='upperleft')

PREMADE_VIEWPORT_STATES= VisionEgg.Core.Viewport(screen=screen, size=screen.size, stimuli=[st101,st102,st103,st104,st105,st106,st107,st108,
                                                                                           st109,st110,st111,st112,st113,st114,st115,st116,
                                                                                           st117,st118,
                                                                                           st201,st202,st203,st204,st205,st206,st207,st208,
                                                                                           st209,st210,st211,st212,st213,st214,st215,st216,
                                                                                           st217,st218,
                                                                                           st301,st302,st303,st304,st305,st306,st307,st308,
                                                                                           st309,st310,st311,st312,st313,st314])

ATTENTION_BLANK=[["TASK","SIMPLE_ATTENTION_J","SIMPLE_ATTENTION_FRUIT","SIMPLE_ATTENTION_1239"],
                 ["POINTS","NA","NA","NA"],["TIME_MS","NA","NA","NA"]]

SPATIAL_BLANK=[["TASK","SIMPLE_SHAPE","FACE","LINE_DRAW","CUBE"],
               ["POINTS","NA","NA","NA","NA"],["TIME_MS","NA","NA","NA","NA"]]

ORIENTATION_BLANK=[["TASK","MONTH","YEAR","DAY_OF_WEEK","STATE"],
                   ["POINTS","NA","NA","NA","NA"],["TIME_MS","NA","NA","NA","NA"]]

MEMORY_BLANK=[["TASK","INCIDENTAL_MEMORY_PHRASE","INCIDENTAL_MEMORY_J","INCIDENTAL_MEMORY_NUMBER","RECALL_FIVEWORDS"],
              ["POINTS","NA","NA","NA","NA"],["TIME_MS","NA","NA","NA","NA"]]

MATH_BLANK=[["TASK","ADD_67","SUBTRACT_33"],
            ["POINTS","NA","NA"],["TIME_MS","NA","NA"]]

TRAILS_BLANK=[["TASK","MINI_TRAILS_A","MINI_TRAILS_B","FULL_TRAILS_B"],
              ["POINTS","NA","NA","NA"],["TIME_MS","NA","NA","NA"]]

STROOP_BLANK=[["TASK","WARMUP1","WARMUP2","WARMUP3","STROOP04","STROOP05","STROOP06","STROOP07","STROOP08","STROOP09",
               "STROOP10","STROOP11","STROOP12","STROOP13","STROOP14","STROOP15"],
              ["ERRORS","NA","NA","NA","NA","NA","NA","NA","NA","NA","NA","NA","NA","NA","NA","NA"],
              ["TIME_MS","NA","NA","NA","NA","NA","NA","NA","NA","NA","NA","NA","NA","NA","NA","NA"]]

## these will be vectors, just append to it with each task
READING_SPEED_BLANK=["NA"]
MOTOR_SPEED_BLANK=["NA"]          


########################################################################
########################  CREATE YOUR DICTIONARY  ######################
########################################################################
## the SLUMS words are
#
## APPLE
## PEN
## TIE
## HOUSE
## CAR
#
## These are favored, because SLUMS is public domain.
##
## All lures should be concrete nouns (you can draw a picture of it)
##
## As lures, we want 3-6 letter words, and a distribution of starting letters
## similar to in English overall.
##
## for a practice task, I have ACID, JAZZ, MUG, NUT, and YARN,
## which I'll keep as familiar lures.

## we also want some orthographically similar (but semantically distinct) lures
## trying to get first and last couple letters, and length within +/- 1 letter:
##
## for APPLE, "APRON" [first two letters], and "MAPLE" [last three letters]
## for PEN, "PEAR" and "PENCIL", and "OVEN" 
## for TIE, (between "TICKET", "TOE", I think I got it; left out "TINT") and "LIE"
## for HOUSE, "HONEY", and "FUSE"
## for CAR, "CAKE" and "STAR"

## we also want some orthographically different but similar category words:
##
## for APPLE(fruits, veggies) BANANA, ORANGE, LEMON, PEAR
## for PEN (office supply) PENCIL, STAPLE
## for TIE (clothing, or the knot), BELT, SHOE, KNOT
## for HOUSE (building, domicile), CHURCH, GARAGE, HUT, ROOM, SHED, STORE
## for CAR (vehicle), AUTO, BIKE, BOAT, TRUCK, VAN

## we'll have a few colors as lures as well:
## "RED", "GREEN" ("GOLD"), "WHITE", "BLUE",

## we want 99 words total (I think I can fit a 13x7 or a 14x6, but we''l plan for
##  a 13x8 just in case.)

## From Peter Norvig (head of research at Google) analysis of Google Books
## http://norvig.com/mayzner.html
## "a" 11.6 % = 11 words ("ACID", "ACTOR", "APPLE", "APRON", "ALBUM", "ANT", "ARCH", "ARM", "ASH", "ATTIC", "AUTO")
## "b"  4.4 % = 5 words	("BANANA","BELT","BIKE","BLUE","BOAT") 
## "c"	5.2 % = 5 words ("CAKE","CAR","CHURCH","COFFEE","COW")
## "d"	3.1 % = 3 words	("DIME","DOG","DOLLAR")
## "e"  2.8 % = 3 words ("EAR","EAGLE","EGG")
## "f" 	4.0 % = 4 words	("FABRIC","FARM","FLAG","FUSE")
## "g" 	1.6 % = 3 words ("GARAGE","GOLD","GREEN")
## "h" 	4.2 % = 5 words	("HANDLE","HAT","HONEY","HOUSE","HUT")
## "j"  0.5 % = 1 word  ("JAZZ") 
## "k" 	0.5 % = 1 word  ("KNOT")
## "l" 	2.4 % = 3 words ("LIE","LEMON","LOG")	
## "m" 	3.8 % = 4 words ("MAN","MAPLE","MILK","MUG")
## "n" 	2.3 % = 3 words ("NICKEL","NOSE","NUT")
## "o"  7.6 % = 5 words ("OAK","OIL","ORANGE","OVEN","OWL")
## "p" 	4.3 % = 5 words ("PEAR","PEN","PENCIL","PIG")
## "q" 	0.2 % = 1 word  ("QUIZ")  <--- we can use the word "QUIZ" in instructions for familiariy.
## "r" 	2.8 % = 4 words ("RED", "RIB", "ROOM", "ROSE")
## "s" 	6.7 % = 8 words  ("SAIL","SHED","SHOE","SISTER","SKY","STAPLE","STAR","STORE")
## "t"	16.0% = 16 words ("TABLE","TEA","TEEN","TENNIS","THROAT","THUMB","TICKET",
##                        "TIE", "TOE","TONGUE","TOOTH","TOWN","TRAIN","TREE","TRUCK","TUB")
## "u" 	1.2 % = 1 word  ("URGE")
## "v" 	0.8 % = 1 word	("VAN")
## "w" 	5.5 % = 6 words	("WAVE","WHITE","WEB","WOLF","WOMAN","WOOD")
## "x"	0.04% = 0 words 	
## "y" 	0.76% = 2 words ("YARN","YOGA")
## "z"  0.05% = 0 words
## being that the above count gives us 94, we'll through a couple random ones on at the end)

list_words=["ACID", "ACTOR", "APPLE", "APRON", "ALBUM",
              "ANT", "ARCH", "ARM", "ASH", "ATTIC",
              "AUTO",
              "BANANA","BELT","BIKE","BLUE","BOAT", 
              "CAKE","CAR","CHURCH","COFFEE","COW",
              "DIME","DOG","DOLLAR","DRESS",
              "EAR","EAGLE","EGG",
              "FABRIC","FARM","FLAG","FUSE",
              "GARAGE","GOLD","GREEN",
              "HANDLE","HAT","HONEY","HOUSE","HUT",
              "JAZZ",
              "KNOT",
              "LIE","LEMON","LOG",
              "MAN","MAPLE","MILK","MUG",
              "NICKEL","NOSE","NUT",
              "OAK","OIL","ORANGE","OVEN","OWL",
              "PEAR","PEN","PENCIL","PIG",
              "QUIZ",
              "RED", "RIB", "ROOM", "ROSE",
              "SAIL","SHED","SHOE","SISTER","SKY",
              "STAPLE","STAR","STORE",
              "TABLE","TEA","TEEN","TENNIS","THROAT",
              "THUMB","TICKET","TIE","TOE","TONGUE",
              "TOOTH","TOWN","TRAIN","TREE","TRUCK",
              "TUB",
              "URGE",
              "VAN",
              "WAVE","WEB","WHITE","WOLF","WOMAN",
              "WOOD",
              "YARN","YOGA"]

CURRENTLIST=list_words
t101 = Text(text=CURRENTLIST[0],color=(0,0,0),position=(25,514),font_size=42,anchor='upperleft')
t102 = Text(text=CURRENTLIST[1],color=(0,0,0),position=(25,484),font_size=42,anchor='upperleft')
t103 = Text(text=CURRENTLIST[2],color=(0,0,0),position=(25,454),font_size=42,anchor='upperleft')
t104 = Text(text=CURRENTLIST[3],color=(0,0,0),position=(25,424),font_size=42,anchor='upperleft')
t105 = Text(text=CURRENTLIST[4],color=(0,0,0),position=(25,394),font_size=42,anchor='upperleft')
t106 = Text(text=CURRENTLIST[5],color=(0,0,0),position=(25,364),font_size=42,anchor='upperleft')
t107 = Text(text=CURRENTLIST[6],color=(0,0,0),position=(25,334),font_size=42,anchor='upperleft')
t108 = Text(text=CURRENTLIST[7],color=(0,0,0),position=(25,304),font_size=42,anchor='upperleft')
t109 = Text(text=CURRENTLIST[8],color=(0,0,0),position=(25,274),font_size=42,anchor='upperleft')
t110 = Text(text=CURRENTLIST[9],color=(0,0,0),position=(25,244),font_size=42,anchor='upperleft')
t111 = Text(text=CURRENTLIST[10],color=(0,0,0),position=(25,214),font_size=42,anchor='upperleft')
t112 = Text(text=CURRENTLIST[11],color=(0,0,0),position=(25,184),font_size=42,anchor='upperleft')
t113 = Text(text=CURRENTLIST[12],color=(0,0,0),position=(25,154),font_size=42,anchor='upperleft')
t114 = Text(text=CURRENTLIST[13],color=(0,0,0),position=(25,124),font_size=42,anchor='upperleft')
t115 = Text(text=CURRENTLIST[14],color=(0,0,0),position=(25,94),font_size=42,anchor='upperleft')
t116 = Text(text=CURRENTLIST[15],color=(0,0,0),position=(25,64),font_size=42,anchor='upperleft')
t117 = Text(text=CURRENTLIST[16],color=(0,0,0),position=(25,34),font_size=42,anchor='upperleft')
t201 = Text(text=CURRENTLIST[17],color=(0,0,0),position=(189,514),font_size=42,anchor='upperleft')
t202 = Text(text=CURRENTLIST[18],color=(0,0,0),position=(189,484),font_size=42,anchor='upperleft')
t203 = Text(text=CURRENTLIST[19],color=(0,0,0),position=(189,454),font_size=42,anchor='upperleft')
t204 = Text(text=CURRENTLIST[20],color=(0,0,0),position=(189,424),font_size=42,anchor='upperleft')
t205 = Text(text=CURRENTLIST[21],color=(0,0,0),position=(189,394),font_size=42,anchor='upperleft')
t206 = Text(text=CURRENTLIST[22],color=(0,0,0),position=(189,364),font_size=42,anchor='upperleft')
t207 = Text(text=CURRENTLIST[23],color=(0,0,0),position=(189,334),font_size=42,anchor='upperleft')
t208 = Text(text=CURRENTLIST[24],color=(0,0,0),position=(189,304),font_size=42,anchor='upperleft')
t209 = Text(text=CURRENTLIST[25],color=(0,0,0),position=(189,274),font_size=42,anchor='upperleft')
t210 = Text(text=CURRENTLIST[26],color=(0,0,0),position=(189,244),font_size=42,anchor='upperleft')
t211 = Text(text=CURRENTLIST[27],color=(0,0,0),position=(189,214),font_size=42,anchor='upperleft')
t212 = Text(text=CURRENTLIST[28],color=(0,0,0),position=(189,184),font_size=42,anchor='upperleft')
t213 = Text(text=CURRENTLIST[29],color=(0,0,0),position=(189,154),font_size=42,anchor='upperleft')
t214 = Text(text=CURRENTLIST[30],color=(0,0,0),position=(189,124),font_size=42,anchor='upperleft')
t215 = Text(text=CURRENTLIST[31],color=(0,0,0),position=(189,94),font_size=42,anchor='upperleft')
t216 = Text(text=CURRENTLIST[32],color=(0,0,0),position=(189,64),font_size=42,anchor='upperleft')
t217 = Text(text=CURRENTLIST[33],color=(0,0,0),position=(189,34),font_size=42,anchor='upperleft')
t301 = Text(text=CURRENTLIST[34],color=(0,0,0),position=(355,514),font_size=42,anchor='upperleft')
t302 = Text(text=CURRENTLIST[35],color=(0,0,0),position=(355,484),font_size=42,anchor='upperleft')
t303 = Text(text=CURRENTLIST[36],color=(0,0,0),position=(355,454),font_size=42,anchor='upperleft')
t304 = Text(text=CURRENTLIST[37],color=(0,0,0),position=(355,424),font_size=42,anchor='upperleft')
t305 = Text(text=CURRENTLIST[38],color=(0,0,0),position=(355,394),font_size=42,anchor='upperleft')
t306 = Text(text=CURRENTLIST[39],color=(0,0,0),position=(355,364),font_size=42,anchor='upperleft')
t307 = Text(text=CURRENTLIST[40],color=(0,0,0),position=(355,334),font_size=42,anchor='upperleft')
t308 = Text(text=CURRENTLIST[41],color=(0,0,0),position=(355,304),font_size=42,anchor='upperleft')
t309 = Text(text=CURRENTLIST[42],color=(0,0,0),position=(355,274),font_size=42,anchor='upperleft')
t310 = Text(text=CURRENTLIST[43],color=(0,0,0),position=(355,244),font_size=42,anchor='upperleft')
t311 = Text(text=CURRENTLIST[44],color=(0,0,0),position=(355,214),font_size=42,anchor='upperleft')
t312 = Text(text=CURRENTLIST[45],color=(0,0,0),position=(355,184),font_size=42,anchor='upperleft')
t313 = Text(text=CURRENTLIST[46],color=(0,0,0),position=(355,154),font_size=42,anchor='upperleft')
t314 = Text(text=CURRENTLIST[47],color=(0,0,0),position=(355,124),font_size=42,anchor='upperleft')
t315 = Text(text=CURRENTLIST[48],color=(0,0,0),position=(355,94),font_size=42,anchor='upperleft')
t316 = Text(text=CURRENTLIST[49],color=(0,0,0),position=(355,64),font_size=42,anchor='upperleft')
t317 = Text(text=CURRENTLIST[50],color=(0,0,0),position=(355,34),font_size=42,anchor='upperleft')
t401 = Text(text=CURRENTLIST[51],color=(0,0,0),position=(520,514),font_size=42,anchor='upperleft')
t402 = Text(text=CURRENTLIST[52],color=(0,0,0),position=(520,484),font_size=42,anchor='upperleft')
t403 = Text(text=CURRENTLIST[53],color=(0,0,0),position=(520,454),font_size=42,anchor='upperleft')
t404 = Text(text=CURRENTLIST[54],color=(0,0,0),position=(520,424),font_size=42,anchor='upperleft')
t405 = Text(text=CURRENTLIST[55],color=(0,0,0),position=(520,394),font_size=42,anchor='upperleft')
t406 = Text(text=CURRENTLIST[56],color=(0,0,0),position=(520,364),font_size=42,anchor='upperleft')
t407 = Text(text=CURRENTLIST[57],color=(0,0,0),position=(520,334),font_size=42,anchor='upperleft')
t408 = Text(text=CURRENTLIST[58],color=(0,0,0),position=(520,304),font_size=42,anchor='upperleft')
t409 = Text(text=CURRENTLIST[59],color=(0,0,0),position=(520,274),font_size=42,anchor='upperleft')
t410 = Text(text=CURRENTLIST[60],color=(0,0,0),position=(520,244),font_size=42,anchor='upperleft')
t411 = Text(text=CURRENTLIST[61],color=(0,0,0),position=(520,214),font_size=42,anchor='upperleft')
t412 = Text(text=CURRENTLIST[62],color=(0,0,0),position=(520,184),font_size=42,anchor='upperleft')
t413 = Text(text=CURRENTLIST[63],color=(0,0,0),position=(520,154),font_size=42,anchor='upperleft')
t414 = Text(text=CURRENTLIST[64],color=(0,0,0),position=(520,124),font_size=42,anchor='upperleft')
t415 = Text(text=CURRENTLIST[65],color=(0,0,0),position=(520,94),font_size=42,anchor='upperleft')
t416 = Text(text=CURRENTLIST[66],color=(0,0,0),position=(520,64),font_size=42,anchor='upperleft')
t417 = Text(text=CURRENTLIST[67],color=(0,0,0),position=(520,34),font_size=42,anchor='upperleft')
t501 = Text(text=CURRENTLIST[68],color=(0,0,0),position=(688,514),font_size=42,anchor='upperleft')
t502 = Text(text=CURRENTLIST[69],color=(0,0,0),position=(688,484),font_size=42,anchor='upperleft')
t503 = Text(text=CURRENTLIST[70],color=(0,0,0),position=(688,454),font_size=42,anchor='upperleft')
t504 = Text(text=CURRENTLIST[71],color=(0,0,0),position=(688,424),font_size=42,anchor='upperleft')
t505 = Text(text=CURRENTLIST[72],color=(0,0,0),position=(688,394),font_size=42,anchor='upperleft')
t506 = Text(text=CURRENTLIST[73],color=(0,0,0),position=(688,364),font_size=42,anchor='upperleft')
t507 = Text(text=CURRENTLIST[74],color=(0,0,0),position=(688,334),font_size=42,anchor='upperleft')
t508 = Text(text=CURRENTLIST[75],color=(0,0,0),position=(688,304),font_size=42,anchor='upperleft')
t509 = Text(text=CURRENTLIST[76],color=(0,0,0),position=(688,274),font_size=42,anchor='upperleft')
t510 = Text(text=CURRENTLIST[77],color=(0,0,0),position=(688,244),font_size=42,anchor='upperleft')
t511 = Text(text=CURRENTLIST[78],color=(0,0,0),position=(688,214),font_size=42,anchor='upperleft')
t512 = Text(text=CURRENTLIST[79],color=(0,0,0),position=(688,184),font_size=42,anchor='upperleft')
t513 = Text(text=CURRENTLIST[80],color=(0,0,0),position=(688,154),font_size=42,anchor='upperleft')
t514 = Text(text=CURRENTLIST[81],color=(0,0,0),position=(688,124),font_size=42,anchor='upperleft')
t515 = Text(text=CURRENTLIST[82],color=(0,0,0),position=(688,94),font_size=42,anchor='upperleft')
t516 = Text(text=CURRENTLIST[83],color=(0,0,0),position=(688,64),font_size=42,anchor='upperleft')
t517 = Text(text=CURRENTLIST[84],color=(0,0,0),position=(688,34),font_size=42,anchor='upperleft')
t601 = Text(text=CURRENTLIST[85],color=(0,0,0),position=(853,514),font_size=42,anchor='upperleft')
t602 = Text(text=CURRENTLIST[86],color=(0,0,0),position=(853,484),font_size=42,anchor='upperleft')
t603 = Text(text=CURRENTLIST[87],color=(0,0,0),position=(853,454),font_size=42,anchor='upperleft')
t604 = Text(text=CURRENTLIST[88],color=(0,0,0),position=(853,424),font_size=42,anchor='upperleft')
t605 = Text(text=CURRENTLIST[89],color=(0,0,0),position=(853,394),font_size=42,anchor='upperleft')
t606 = Text(text=CURRENTLIST[90],color=(0,0,0),position=(853,364),font_size=42,anchor='upperleft')
t607 = Text(text=CURRENTLIST[91],color=(0,0,0),position=(853,334),font_size=42,anchor='upperleft')
t608 = Text(text=CURRENTLIST[92],color=(0,0,0),position=(853,304),font_size=42,anchor='upperleft')
t609 = Text(text=CURRENTLIST[93],color=(0,0,0),position=(853,274),font_size=42,anchor='upperleft')
t610 = Text(text=CURRENTLIST[94],color=(0,0,0),position=(853,244),font_size=42,anchor='upperleft')
t611 = Text(text=CURRENTLIST[95],color=(0,0,0),position=(853,214),font_size=42,anchor='upperleft')
t612 = Text(text=CURRENTLIST[96],color=(0,0,0),position=(853,184),font_size=42,anchor='upperleft')
t613 = Text(text=CURRENTLIST[97],color=(0,0,0),position=(853,154),font_size=42,anchor='upperleft')
t614 = Text(text=CURRENTLIST[98],color=(0,0,0),position=(853,124),font_size=42,anchor='upperleft')
t615 = Text(text=CURRENTLIST[99],color=(0,0,0),position=(853,94),font_size=42,anchor='upperleft')
FREErecallVIEWPORT = VisionEgg.Core.Viewport(screen=screen, size=screen.size, stimuli=[t101,t102,t103,t104,t105,t106,t107,t108,
                                                                                 t109,t110,t111,t112,t113,t114,t115,t116,
                                                                                 t117,
                                                                                 t201,t202,t203,t204,t205,t206,t207,t208,
                                                                                 t209,t210,t211,t212,t213,t214,t215,t216,
                                                                                 t217,
                                                                                 t301,t302,t303,t304,t305,t306,t307,t308,
                                                                                 t309,t310,t311,t312,t313,t314,t315,t316,
                                                                                 t317,
                                                                                 t401,t402,t403,t404,t405,t406,t407,t408,
                                                                                 t409,t410,t411,t412,t413,t414,t415,t416,
                                                                                 t417,
                                                                                 t501,t502,t503,t504,t505,t506,t507,t508,
                                                                                 t509,t510,t511,t512,t513,t514,t515,t516,
                                                                                 t517,
                                                                                 t601,t602,t603,t604,t605,t606,t607,t608,
                                                                                 t609,t610,t611,t612,t613,t614,t615])



################################################
################################################




def review_screen(ScreenNumber, RESET):
    EXITLIST=[0,0,0]
    os.chdir("data/")
    backgroundIMAGE = TextureStimulus(texture=Texture("_LATEST_SUBJECT.jpg"),position=(0,0))
    os.chdir(BASEPATH)
    viewport = VisionEgg.Core.Viewport(screen=screen, size=screen.size, stimuli=[backgroundIMAGE,backgroundIMAGE])
    screen.clear()
    viewport.draw()
    VisionEgg.Core.swap_buffers()
    screen.clear()
    viewport.draw()
    StartTrial=False
    while not StartTrial:
        for event in pygame.event.get():
            if event.type == pygame.locals.MOUSEBUTTONDOWN:
                x,y = pygame.mouse.get_pos()
## pygame.mouse.get_pos() gives coordinates with the LOWER LEFT, not UPPER LEFT (as in visionegg) corner as the origin.
## before we get too complicated, will probably want to flip things around:
                y=600-y
                ##
                ## now we see the practical application of the EXITLIST:
                if x >= 0 and x <=24 and y >= 584 and y <=600:
                   if EXITLIST==[0,0,0]:
                       EXITLIST[0]=1
                       text0 = Text(text="O",color=(0,0,0),position=(0,600),font_size=30,anchor='center')
                       text1 = Text(text="O",color=(0,0,0),position=(0,600),font_size=30,anchor='center')
                       viewportTEXT = VisionEgg.Core.Viewport(screen=screen, size=screen.size, stimuli=[text0, text1])
                       VisionEgg.Core.swap_buffers()
                       screen.clear()
                       viewport.draw()
                       viewportTEXT.draw()
                       viewportTEXT2.draw()
                       VisionEgg.Core.swap_buffers()
                elif x >= 1008 and x <=1024 and y >= 584 and y <=600:
                    if EXITLIST==[1,0,0]:
                       EXITLIST[1]=1
                       text0 = Text(text="O",color=(0,0,0),position=(0,600),font_size=30,anchor='center')
                       text1 = Text(text="O",color=(0,0,0),position=(1024,600),font_size=30,anchor='center')
                       viewportTEXT = VisionEgg.Core.Viewport(screen=screen, size=screen.size, stimuli=[text0, text1])
                       VisionEgg.Core.swap_buffers()
                       screen.clear()
                       viewport.draw()
                       viewportTEXT.draw()
                       viewportTEXT2.draw()
                       VisionEgg.Core.swap_buffers()
                elif x >= 1008 and x <=1024 and y >= 0 and y <=16:
                    if EXITLIST==[1,1,0]:
                        ScreenNumber, RESET = ESCAPEscreenFirstPageFirstRun(ScreenNumber, RESET)
###  ###   ###  # #     ### ALWAYS REMEMBER TO UPDATE THE RETURN INFO!  ##   #   #   #####  ##  ###    ### ### 
                        return ScreenNumber, RESET
                        StartTrial=True



################################################  BELOW HERE, CONTROL FOR THE INTRO SCREENS:
################################################
################################################
## this lets us make an escape screen
def ESCAPEscreen(ScreenNumber, RESET):
    homebutton=0
    stim = TextureStimulus(texture=ESCAPESCREEN[2],position=(0,0))
    screen.clear()
    viewport = VisionEgg.Core.Viewport(screen=screen, size=screen.size, stimuli=[stim,stim])
    viewport.draw()
    VisionEgg.Core.swap_buffers()
    viewport.draw()
    VisionEgg.Core.swap_buffers()
    while homebutton==0:
        for event in pygame.event.get():
            if event.type == pygame.locals.MOUSEBUTTONDOWN:
                x,y = pygame.mouse.get_pos()
                if x >= 752 and x <= 902 and y >= 20 and y <= 72:
                    screen.close()
                    screen.close()
                    raise SystemExit
                elif x >= 188 and x <= 839 and y >= 245 and y <= 358:
                    RESET = "True"
                    ScreenNumber=9995
                    return ScreenNumber, RESET
                    homebutton=1

def ESCAPEscreenLATE(ScreenNumber, RESET):
    homebutton=0
    stim = TextureStimulus(texture=ESCAPESCREEN[3],position=(0,0))
    screen.clear()
    viewport = VisionEgg.Core.Viewport(screen=screen, size=screen.size, stimuli=[stim,stim])
    viewport.draw()
    VisionEgg.Core.swap_buffers()
    viewport.draw()
    VisionEgg.Core.swap_buffers()
    while homebutton==0:
        for event in pygame.event.get():
            if event.type == pygame.locals.MOUSEBUTTONDOWN:
                x,y = pygame.mouse.get_pos()
                if x >= 926 and x <= 989 and y >= 431 and y <= 460:
                    screen.close()
                    screen.close()
                    raise SystemExit
                elif x >= 188 and x <= 839 and y >= 245 and y <= 358:
                    RESET = "True"
                    ScreenNumber=9999
                    return ScreenNumber, RESET
                    homebutton=1

def ESCAPEscreenFirstPageFirstRun(ScreenNumber, RESET):
    homebutton=0
    stim = TextureStimulus(texture=ESCAPESCREEN[0],position=(0,0))
    screen.clear()
    viewport = VisionEgg.Core.Viewport(screen=screen, size=screen.size, stimuli=[stim,stim])
    viewport.draw()
    VisionEgg.Core.swap_buffers()
    viewport.draw()
    VisionEgg.Core.swap_buffers()
    while homebutton==0:
        for event in pygame.event.get():
            if event.type == pygame.locals.MOUSEBUTTONDOWN:
                x,y = pygame.mouse.get_pos()
                if x >= 752 and x <= 902 and y >= 20 and y <= 72:
                    screen.close()
                    screen.close()
                    raise SystemExit
                elif x >= 188 and x <= 839 and y >= 245 and y <= 358:
                    RESET = "True"
                    ScreenNumber=9999
                    return ScreenNumber, RESET
                    homebutton=1

def ESCAPEscreenFirstPageSecondRun(ScreenNumber, RESET):
    homebutton=0
    stim = TextureStimulus(texture=ESCAPESCREEN[1],position=(0,0))
    screen.clear()
    viewport = VisionEgg.Core.Viewport(screen=screen, size=screen.size, stimuli=[stim,stim])
    viewport.draw()
    VisionEgg.Core.swap_buffers()
    viewport.draw()
    VisionEgg.Core.swap_buffers()
    while homebutton==0:
        for event in pygame.event.get():
            if event.type == pygame.locals.MOUSEBUTTONDOWN:
                x,y = pygame.mouse.get_pos()
                if x >= 752 and x <= 902 and y >= 20 and y <= 72:
                    screen.close()
                    screen.close()
                    raise SystemExit
                elif x >= 130 and x <= 282 and y >= 112 and y <= 168:
                    RESET = "True"
                    ScreenNumber=9997
                    # don't think I'll need a direct call to review_screen() here, but that would be an alternative
                    return ScreenNumber, RESET
                    homebutton=1
                elif x >= 188 and x <= 839 and y >= 245 and y <= 358:
                    RESET = "True"
                    ScreenNumber=9999
                    return ScreenNumber, RESET
                    homebutton=1


####################################################################################################
####################################################################################################
####################################################################################################
####################################################################################################
####################################################################################################



                    #<$%^> HOMEscreen is updated to make state change option
def HOMEscreen(ScreenNumber, RESET):
    RESET = "False"
    EXITLIST=[0,0,0]
    ENTER=False
    CHANGE_STATE=False
    homebutton=0
    stim = TextureStimulus(texture=HOMESCREEN,position=(0,0))
    screen.clear()
    textSTATE = Text(text=STATE_WHEN_PROGRAM_INITIATED[0],color=(0,0.3,0),position=(400,200),font_size=20,anchor='left')
    viewport = VisionEgg.Core.Viewport(screen=screen, size=screen.size, stimuli=[stim,stim,textSTATE])
    viewport.draw()
    VisionEgg.Core.swap_buffers()
    screen.clear()
    viewport.draw()
    VisionEgg.Core.swap_buffers()
    while homebutton==0:
        for event in pygame.event.get():
            if event.type == pygame.locals.MOUSEBUTTONDOWN:
## the next two lines basically say to get the x and y position of the cursor when a mousedown happens...
                x,y = pygame.mouse.get_pos()
## pygame.mouse.get_pos() gives coordinates with the LOWER LEFT, not UPPER LEFT (as in visionegg) corner as the origin.
                y=600-y
## the following handles actions related to clicking a button...
                if x >= 704 and x <= 953 and y >= 237 and y <= 356:
                    EXITLIST=[0,0,0]
                    if ENTER:
                        return ScreenNumber, RESET
                        homebutton=1                       
                elif x >= 704 and x <= 953 and y >= 409 and y <= 529:
                    EXITLIST=[0,0,0]
                    ENTER=True
                    CHANGE_STATE=False
                    text0 = Text(text="O",color=(0.5,1.0,0.5),position=(829,469),font_size=30,anchor='center')
                    text1 = Text(text="O",color=(0.5,0.5,0.5),position=(-100,-100),font_size=30,anchor='center')
                    viewportTEXT = VisionEgg.Core.Viewport(screen=screen, size=screen.size, stimuli=[text0, text1])
                    VisionEgg.Core.swap_buffers()
                    screen.clear()
                    viewport.draw()
                    viewportTEXT.draw()
                    VisionEgg.Core.swap_buffers()

                elif x >= 558 and x <= 642 and y >= 70 and y <= 135:
                    EXITLIST=[0,0,0]
                    if CHANGE_STATE:
                        ## go to state selection
                        TrialTime=0
                        RESPONSE=0
                        TrialTime=-1  
                        RESPONSE=0
                        ERRORS=0
                        ScreenNumber, TrialTime, RESPONSE, ERRORS, RESET = STATEselection(ScreenNumber, TrialTime, RESPONSE, ERRORS, RESET)
                        os.chdir("bin\\")
                        revise_file = open("DO_NOT_DELETE_THIS_STATE.txt","w")
                        revise_file.write('%s'%RESPONSE)
                        revise_file.close()
                        ## if we made a change, close it out. 
                        screen.close()
                        screen.close()
                        raise SystemExit
                elif x >= 558 and x <= 642 and y >= 167 and y <= 234:
                    EXITLIST=[0,0,0]
                    ENTER=False
                    CHANGE_STATE=True
                    text0 = Text(text="O",color=(0.5,1.0,0.5),position=(600,202),font_size=30,anchor='center')
                    text1 = Text(text="O",color=(0.5,0.5,0.5),position=(-100,-100),font_size=30,anchor='center')
                    viewportTEXT = VisionEgg.Core.Viewport(screen=screen, size=screen.size, stimuli=[text0, text1])
                    VisionEgg.Core.swap_buffers()
                    screen.clear()
                    viewport.draw()
                    viewportTEXT.draw()
                    VisionEgg.Core.swap_buffers()

                elif x >= 0 and x <=24 and y >= 584 and y <=601:
                   ## now we see the practical application of the EXITLIST:
                    if EXITLIST==[0,0,0]:
                       EXITLIST[0]=1
                       ENTER=False
                       CHANGE_STATE=False
                       text0 = Text(text="O",color=(0.5,0.5,0.5),position=(0,600),font_size=30,anchor='center')
                       text1 = Text(text="O",color=(0.5,0.5,0.5),position=(0,600),font_size=30,anchor='center')
                       viewportTEXT = VisionEgg.Core.Viewport(screen=screen, size=screen.size, stimuli=[text0, text1])
                       VisionEgg.Core.swap_buffers()
                       screen.clear()
                       viewport.draw()
                       viewportTEXT.draw()
                       VisionEgg.Core.swap_buffers()
                elif x >= 1008 and x <=1024 and y >= 584 and y <=601:
                   ## now we see the practical application of the EXITLIST:
                    if EXITLIST==[1,0,0]:
                       EXITLIST[1]=1
                       ENTER=False
                       CHANGE_STATE=False
                       text0 = Text(text="O",color=(0.5,0.5,0.5),position=(0,600),font_size=30,anchor='center')
                       text1 = Text(text="O",color=(0.5,0.5,0.5),position=(1024,600),font_size=30,anchor='center')
                       viewportTEXT = VisionEgg.Core.Viewport(screen=screen, size=screen.size, stimuli=[text0, text1])
                       VisionEgg.Core.swap_buffers()
                       screen.clear()
                       viewport.draw()
                       viewportTEXT.draw()
                       VisionEgg.Core.swap_buffers()
                elif x >= 1008 and x <=1024 and y >= 0 and y <=24:
                   ## now we see the practical application of the EXITLIST:
                    if EXITLIST==[1,1,0]:
                        if FIRST_SUBJECT:
                            ScreenNumber, RESET = ESCAPEscreenFirstPageFirstRun(ScreenNumber, RESET)
                            return ScreenNumber, RESET
                        else:
                            ScreenNumber, RESET = ESCAPEscreenFirstPageSecondRun(ScreenNumber, RESET)
                            return ScreenNumber, RESET
                else:
                    EXITLIST=[0,0,0]
                    ENTER=False
                    CHANGE_STATE=False
                    text0 = Text(text="O",color=(0.5,0.5,0.5),position=(-100,-100),font_size=30,anchor='center')
                    text1 = Text(text="O",color=(0.5,0.5,0.5),position=(-100,-100),font_size=30,anchor='center')
                    viewportTEXT = VisionEgg.Core.Viewport(screen=screen, size=screen.size, stimuli=[text0, text1])
                    VisionEgg.Core.swap_buffers()
                    screen.clear()
                    viewport.draw()
                    viewportTEXT.draw()
                    VisionEgg.Core.swap_buffers()
#</$%^> end of update/revision to HOMEscreen


####################################################################################################
####################################################################################################
####################################################################################################
####################################################################################################
####################################################################################################    
def NURSEscreen(ScreenNumber, canRead, RESET):
    EXITLIST=[0,0,0]
    backgroundIMAGE = TextureStimulus(texture=NURSESCREEN,position=(0,0))
    ## add to that background image a potential list of masks
    maskred1 = TextureStimulus(texture=redsquare,position=(863,600-540), anchor='upperleft', max_alpha=0.90)
    maskgreen1 = TextureStimulus(texture=greensquare,position=(798,600-540), anchor='upperleft', max_alpha=0.50) 
    MASKLIST=[maskred1]
     ## we'll modify the MASKLIST depending on button presses....
    viewportmasks = VisionEgg.Core.Viewport(screen=screen, size=screen.size, stimuli=MASKLIST)
    viewport = VisionEgg.Core.Viewport(screen=screen, size=screen.size, stimuli=[backgroundIMAGE,backgroundIMAGE])
    VisionEgg.Core.swap_buffers()
    screen.clear()
    viewport.draw()
    viewportmasks.draw()
    VisionEgg.Core.swap_buffers()
    StartTrial=False
    while not StartTrial:
        for event in pygame.event.get():
            if event.type == pygame.locals.MOUSEBUTTONDOWN:
                xpos,ypos = pygame.mouse.get_pos()
## pygame.mouse.get_pos() gives coordinates with the LOWER LEFT, not UPPER LEFT (as in visionegg) corner as the origin.
## before we get too complicated, will probably want to flip things around:
                ypos=600-ypos
                if xpos >= 798 and xpos <=860 and ypos >=16 and ypos <=60:
                    ## the sequence of leaving the screen by touching upper lefthand corner, then upper righthand corner,
                    ## then right lowerhand corner is reset with a new button push:
                    EXITLIST=[0,0,0]
                    canRead=True
                    MASKLIST[0]=maskgreen1
                    screen.clear()
                    viewport.draw()
                    viewportmasks.draw()
                    VisionEgg.Core.swap_buffers()
                elif xpos >= 863 and xpos <=925 and ypos >=16 and ypos <=60:
                    EXITLIST=[0,0,0]
                    canRead=False
                    MASKLIST[0]=maskred1
                    screen.clear()
                    viewport.draw()
                    viewportmasks.draw()
                    VisionEgg.Core.swap_buffers()

                ## next is for "NEXT" screen
                elif xpos >= 930 and xpos <=1014 and ypos >=18 and ypos <=58:
                    ## the sequence of leaving the screen by touching upper lefthand corner, then upper righthand corner,
                    ## then right lowerhand corner is reset with a new button push:
                    EXITLIST=[0,0,0]
                    if canRead==True:
                        RESET = "False"
                        return ScreenNumber, canRead, RESET
                        StartTrial=True
                    else:
                        RESET = "True"
                        ScreenNumber, RESET = ESCAPEscreen(ScreenNumber, RESET)
                        return ScreenNumber, canRead, RESET
                        StartTrial=True
                ##
                ##
                ## now we see the practical application of the EXITLIST:    
                elif xpos >= 0 and xpos <=24 and ypos >= 584 and ypos <=600:
                   ## now we see the practical application of the EXITLIST:
                   if EXITLIST==[0,0,0]:
                       EXITLIST[0]=1
                       text0 = Text(text="O",color=(0,0,0),position=(0,600),font_size=30,anchor='center')
                       text1 = Text(text="O",color=(0,0,0),position=(0,600),font_size=30,anchor='center')
                       viewportTEXT = VisionEgg.Core.Viewport(screen=screen, size=screen.size, stimuli=[text0, text1])
                       screen.clear()
                       viewport.draw()
                       viewportmasks.draw()
                       viewportTEXT.draw()
                       VisionEgg.Core.swap_buffers()
                elif xpos >= 1008 and xpos <=1024 and ypos >= 584 and ypos <=600:
                   ## now we see the practical application of the EXITLIST:
                    if EXITLIST==[1,0,0]:
                       EXITLIST[1]=1
                       text0 = Text(text="O",color=(0,0,0),position=(0,600),font_size=30,anchor='center')
                       text1 = Text(text="O",color=(0,0,0),position=(1024,600),font_size=30,anchor='center')
                       viewportTEXT = VisionEgg.Core.Viewport(screen=screen, size=screen.size, stimuli=[text0, text1])
                       screen.clear()
                       viewport.draw()
                       viewportmasks.draw()
                       viewportTEXT.draw()
                       VisionEgg.Core.swap_buffers()
                elif xpos >= 1008 and xpos <=1024 and ypos >= 0 and ypos <=16:
                   ## now we see the practical application of the EXITLIST:
                    if EXITLIST==[1,1,0]:
                        ScreenNumber, RESET = ESCAPEscreen(ScreenNumber, RESET)
                        return ScreenNumber, canRead, RESET
                        StartTrial=True


####################################################################################################
####################################################################################################
####################################################################################################
####################################################################################################
####################################################################################################
def EPICscreen(ScreenNumber, RESET):
    EXITLIST=[0,0,0]
    text0 = Text(text="%d"%subject_number,
                 color=(0,0,0),
                 position=(screen.size[0]/2,screen.size[1]*12.5/24), ## can change 12/24 to 13/24 for different line
                 font_size=60,
                 anchor='center')
    text1 = Text(text="%d"%subject_number,
                 color=(0,0,0),
                 position=(screen.size[0]/2,screen.size[1]*12.5/24),
                 font_size=60,
                 anchor='center')
    stim = TextureStimulus(texture=EPICSCREEN,position=(0,0))
    viewport = VisionEgg.Core.Viewport(screen=screen, size=screen.size, stimuli=[stim,stim])
    viewportTEXT2 = VisionEgg.Core.Viewport(screen=screen, size=screen.size, stimuli=[text0, text1])
    screen.clear()
    viewport.draw()
    viewportTEXT2.draw()
    VisionEgg.Core.swap_buffers()
    screen.clear()
    viewport.draw()
    viewportTEXT2.draw()
    StartTrial=False
    VisionEgg.Core.swap_buffers()
    while not StartTrial:
        for event in pygame.event.get():
            if event.type == pygame.locals.MOUSEBUTTONDOWN:
                xpos,ypos = pygame.mouse.get_pos()
## pygame.mouse.get_pos() gives coordinates with the LOWER LEFT, not UPPER LEFT (as in visionegg) corner as the origin.
## before we get too complicated, will probably want to flip things around:
                ypos=600-ypos
                if xpos >= 266 and xpos <=499 and ypos >= 125 and ypos <=267:
                    return ScreenNumber, RESET
                    StartTrial=True
                if xpos >= 0 and xpos <=24 and ypos >= 584 and ypos <=600:
                   ## now we see the practical application of the EXITLIST:
                   if EXITLIST==[0,0,0]:
                       EXITLIST[0]=1
                       text0 = Text(text="O",color=(0,0,0),position=(0,600),font_size=30,anchor='center')
                       text1 = Text(text="O",color=(0,0,0),position=(0,600),font_size=30,anchor='center')
                       viewportTEXT = VisionEgg.Core.Viewport(screen=screen, size=screen.size, stimuli=[text0, text1])
                       VisionEgg.Core.swap_buffers()
                       screen.clear()
                       viewport.draw()
                       viewportTEXT.draw()
                       viewportTEXT2.draw()
                       VisionEgg.Core.swap_buffers()
                elif xpos >= 1008 and xpos <=1024 and ypos >= 584 and ypos <=600:
                   ## now we see the practical application of the EXITLIST:
                    if EXITLIST==[1,0,0]:
                       EXITLIST[1]=1
                       text0 = Text(text="O",color=(0,0,0),position=(0,600),font_size=30,anchor='center')
                       text1 = Text(text="O",color=(0,0,0),position=(1024,600),font_size=30,anchor='center')
                       viewportTEXT = VisionEgg.Core.Viewport(screen=screen, size=screen.size, stimuli=[text0, text1])
                       VisionEgg.Core.swap_buffers()
                       screen.clear()
                       viewport.draw()
                       viewportTEXT.draw()
                       viewportTEXT2.draw()
                       VisionEgg.Core.swap_buffers()
                elif xpos >= 1008 and xpos <=1024 and ypos >= 0 and ypos <=16:
                   ## now we see the practical application of the EXITLIST:
                    if EXITLIST==[1,1,0]:
                        ScreenNumber, RESET = ESCAPEscreen(ScreenNumber, RESET)
                        return ScreenNumber, RESET
                        StartTrial=True

####################################################################################################
####################################################################################################
####################################################################################################
####################################################################################################
####################################################################################################
def PATIENTstartSCREEN(ScreenNumber, RESET):
    xpos=-1
    ypos=-1
    EXITLIST=[0,0,0]  ## we won't track time for this one, since there's a nurse handoff to the patient.
    stim = TextureStimulus(texture=instructbackgrounds[0],position=(0,0))
    viewport = VisionEgg.Core.Viewport(screen=screen, size=screen.size, stimuli=[stim])
    screen.clear()
    viewport.draw()
    VisionEgg.Core.swap_buffers()
    screen.clear()
    viewport.draw()
    StartTrial=False
    startTIME=int(round(time() * 1000))
    #VisionEgg.Core.swap_buffers()
    while not StartTrial:
        for event in pygame.event.get():
            if event.type == pygame.locals.MOUSEBUTTONDOWN:
                if (int(round(time() * 1000))-startTIME) > 100:
                    xpos,ypos = pygame.mouse.get_pos()
## pygame.mouse.get_pos() gives coordinates with the LOWER LEFT, not UPPER LEFT (as in visionegg) corner as the origin.
## before we get too complicated, will probably want to flip things around:
                ypos=600-ypos
                if xpos >= 904  and xpos <= 997  and ypos >= 0  and ypos <=36 :
                    return ScreenNumber, RESET
                    StartTrial=True
                if xpos >= 0 and xpos <=24 and ypos >= 584 and ypos <=600:
                   ## now we see the practical application of the EXITLIST:
                   if EXITLIST==[0,0,0]:
                       EXITLIST[0]=1
                       text0 = Text(text="O",color=(0,0,0),position=(0,600),font_size=30,anchor='center')
                       text1 = Text(text="O",color=(0,0,0),position=(0,600),font_size=30,anchor='center')
                       viewportTEXT = VisionEgg.Core.Viewport(screen=screen, size=screen.size, stimuli=[text0, text1])
                       VisionEgg.Core.swap_buffers()
                       screen.clear()
                       viewport.draw()
                       viewportTEXT.draw()
                       VisionEgg.Core.swap_buffers()
                elif xpos >= 1008 and xpos <=1024 and ypos >= 584 and ypos <=600:
                   ## now we see the practical application of the EXITLIST:
                    if EXITLIST==[1,0,0]:
                       EXITLIST[1]=1
                       text0 = Text(text="O",color=(0,0,0),position=(0,600),font_size=30,anchor='center')
                       text1 = Text(text="O",color=(0,0,0),position=(1024,600),font_size=30,anchor='center')
                       viewportTEXT = VisionEgg.Core.Viewport(screen=screen, size=screen.size, stimuli=[text0, text1])
                       VisionEgg.Core.swap_buffers()
                       screen.clear()
                       viewport.draw()
                       viewportTEXT.draw()
                       VisionEgg.Core.swap_buffers()
                elif xpos >= 1008 and xpos <=1024 and ypos >= 0 and ypos <=16:
                   ## now we see the practical application of the EXITLIST:
                    if EXITLIST==[1,1,0]:
                        ScreenNumber, RESET = ESCAPEscreen(ScreenNumber, RESET)
                        return ScreenNumber, RESET
                        StartTrial=True


####################################################################################################
####################################################################################################
####################################################################################################
####################################################################################################
####################################################################################################
def INSTRUCTIONscreen(ScreenNumber, BACKGROUNDIMAGE, InstructionTime, RESET):
    x=-1
    y=-1
    EXITLIST=[0,0,0]
    stim = TextureStimulus(texture=BACKGROUNDIMAGE,position=(0,0))
    viewport = VisionEgg.Core.Viewport(screen=screen, size=screen.size, stimuli=[stim])
    screen.clear()
    viewport.draw()
    VisionEgg.Core.swap_buffers()
    startTIME=int(round(time() * 1000))
    screen.clear()
    viewport.draw()
    StartTrial=False
    #VisionEgg.Core.swap_buffers()
    while not StartTrial:
        for event in pygame.event.get():
            if event.type == pygame.locals.MOUSEBUTTONDOWN:
                if (int(round(time() * 1000))-startTIME) > 100:
                    x,y = pygame.mouse.get_pos()
## pygame.mouse.get_pos() gives coordinates with the LOWER LEFT, not UPPER LEFT (as in visionegg) corner as the origin.
## before we get too complicated, will probably want to flip things around:
                y=600-y
                if x >= 930  and x <= 1024  and y >= 35  and y <=71:
                    endTIME=int(round(time() * 1000))
                    InstructionTime=endTIME-startTIME
                    return ScreenNumber, BACKGROUNDIMAGE, InstructionTime, RESET
                    StartTrial=True
                ##
                ## now we see the practical application of the EXITLIST:
                elif x >= 0 and x <=24 and y >= 584 and y <=600:
                   if EXITLIST==[0,0,0]:
                       EXITLIST[0]=1
                       text0 = Text(text="O",color=(0,0,0),position=(0,600),font_size=30,anchor='center')
                       text1 = Text(text="O",color=(0,0,0),position=(0,600),font_size=30,anchor='center')
                       viewportTEXT = VisionEgg.Core.Viewport(screen=screen, size=screen.size, stimuli=[text0, text1])
                       VisionEgg.Core.swap_buffers()
                       screen.clear()
                       viewport.draw()
                       viewportTEXT.draw()
                       VisionEgg.Core.swap_buffers()
                elif x >= 1008 and x <=1024 and y >= 584 and y <=600:
                   ## now we see the practical application of the EXITLIST:
                    if EXITLIST==[1,0,0]:
                       EXITLIST[1]=1
                       text0 = Text(text="O",color=(0,0,0),position=(0,600),font_size=30,anchor='center')
                       text1 = Text(text="O",color=(0,0,0),position=(1024,600),font_size=30,anchor='center')
                       viewportTEXT = VisionEgg.Core.Viewport(screen=screen, size=screen.size, stimuli=[text0, text1])
                       VisionEgg.Core.swap_buffers()
                       screen.clear()
                       viewport.draw()
                       viewportTEXT.draw()
                       VisionEgg.Core.swap_buffers()
                elif x >= 1008 and x <=1024 and y >= 0 and y <=16:
                   ## now we see the practical application of the EXITLIST:
                    if EXITLIST==[1,1,0]:
                        if ScreenNumber > 11:
                            ScreenNumber, RESET = ESCAPEscreenLATE(ScreenNumber, RESET)
                        else:
                            ScreenNumber, RESET = ESCAPEscreen(ScreenNumber, RESET)
                        return ScreenNumber, BACKGROUNDIMAGE, InstructionTime, RESET
                        StartTrial=True
                        
####################################################################################################
####################################################################################################
####################################################################################################
####################################################################################################
####################################################################################################
def INSTRUCTIONscreenODD(ScreenNumber, BACKGROUNDIMAGE, InstructionTime, RESET):  ## for moved hitbox, currently screens 38 and 40
    x=-1
    y=-1
    EXITLIST=[0,0,0]
    stim = TextureStimulus(texture=BACKGROUNDIMAGE,position=(0,0))
    viewport = VisionEgg.Core.Viewport(screen=screen, size=screen.size, stimuli=[stim])
    screen.clear()
    viewport.draw()
    VisionEgg.Core.swap_buffers()
    startTIME=int(round(time() * 1000))
    screen.clear()
    viewport.draw()
    StartTrial=False
    #VisionEgg.Core.swap_buffers()
    while not StartTrial:
        for event in pygame.event.get():
            if event.type == pygame.locals.MOUSEBUTTONDOWN:
                if (int(round(time() * 1000))-startTIME) > 100:
                    x,y = pygame.mouse.get_pos()
## pygame.mouse.get_pos() gives coordinates with the LOWER LEFT, not UPPER LEFT (as in visionegg) corner as the origin.
## before we get too complicated, will probably want to flip things around:
                y=600-y
                if x >= 904  and x <= 996  and y >= 0  and y <=37:
                    endTIME=int(round(time() * 1000))
                    InstructionTime=endTIME-startTIME
                    return ScreenNumber, BACKGROUNDIMAGE, InstructionTime, RESET
                    StartTrial=True
                ##
                ## now we see the practical application of the EXITLIST:
                elif x >= 0 and x <=24 and y >= 584 and y <=600:
                   if EXITLIST==[0,0,0]:
                       EXITLIST[0]=1
                       text0 = Text(text="O",color=(0,0,0),position=(0,600),font_size=30,anchor='center')
                       text1 = Text(text="O",color=(0,0,0),position=(0,600),font_size=30,anchor='center')
                       viewportTEXT = VisionEgg.Core.Viewport(screen=screen, size=screen.size, stimuli=[text0, text1])
                       VisionEgg.Core.swap_buffers()
                       screen.clear()
                       viewport.draw()
                       viewportTEXT.draw()
                       VisionEgg.Core.swap_buffers()
                elif x >= 1008 and x <=1024 and y >= 584 and y <=600:
                   ## now we see the practical application of the EXITLIST:
                    if EXITLIST==[1,0,0]:
                       EXITLIST[1]=1
                       text0 = Text(text="O",color=(0,0,0),position=(0,600),font_size=30,anchor='center')
                       text1 = Text(text="O",color=(0,0,0),position=(1024,600),font_size=30,anchor='center')
                       viewportTEXT = VisionEgg.Core.Viewport(screen=screen, size=screen.size, stimuli=[text0, text1])
                       VisionEgg.Core.swap_buffers()
                       screen.clear()
                       viewport.draw()
                       viewportTEXT.draw()
                       VisionEgg.Core.swap_buffers()
                elif x >= 1008 and x <=1024 and y >= 0 and y <=16:
                   ## now we see the practical application of the EXITLIST:
                    if EXITLIST==[1,1,0]:
                        if ScreenNumber > 11:
                            ScreenNumber, RESET = ESCAPEscreenLATE(ScreenNumber, RESET)
                        else:
                            ScreenNumber, RESET = ESCAPEscreen(ScreenNumber, RESET)
                        return ScreenNumber, BACKGROUNDIMAGE, InstructionTime, RESET
                        StartTrial=True


####################################################################################################
####################################################################################################
####################################################################################################
####################################################################################################
####################################################################################################
def PICKtheJword(ScreenNumber, TrialTime, ERRORS, Choice, RESET):
    x=-1
    y=-1
    #reset variables
    EXITLIST=[0,0,0]
    ANSWERED=0
    Choice=[" "]
    ERRORS=0
    #make and show background
    backgroundIMAGE = TextureStimulus(texture=taskbackgrounds[0],position=(0,0))
    viewport = VisionEgg.Core.Viewport(screen=screen, size=screen.size, stimuli=[backgroundIMAGE])
    warnBOX = TextureStimulus(texture=notyetboxes[0],position=(830,150), anchor='center', max_alpha=0.80)
    viewportwarnBOX = VisionEgg.Core.Viewport(screen=screen, size=screen.size, stimuli=[warnBOX])
    useTHISmask=masks[0]
    maskblue = TextureStimulus(texture=useTHISmask,position=(-100,-100), anchor='center', max_alpha=0.50)    
    MASKLIST=[maskblue]
     ## we'll modify the MASKLIST depending on button presses....
    viewportmasks = VisionEgg.Core.Viewport(screen=screen, size=screen.size, stimuli=MASKLIST)
    screen.clear()
    viewport.draw()
    VisionEgg.Core.swap_buffers()
    screen.clear()
    viewport.draw()
    VisionEgg.Core.swap_buffers()
    # start clock
    startTIME=int(round(time() * 1000))
    StartTrial=False
    while not StartTrial:
        for event in pygame.event.get():
            if event.type == pygame.locals.MOUSEBUTTONDOWN:
                if (int(round(time() * 1000))-startTIME) > 100:
                    x,y = pygame.mouse.get_pos()
## pygame.mouse.get_pos() gives coordinates with the LOWER LEFT, not UPPER LEFT (as in visionegg) corner as the origin.
## before we get too complicated, will probably want to flip things around:
                y=600-y
                if x >= 904  and x <= 997  and y >= 0  and y <=36 :
                    EXITLIST=[0,0,0]
                    ## the "touch here when done" box. Action depends on ANSWERED
                    if ANSWERED == 1 and Choice[0]=="Jazz":
                        ## trial time is in seconds
                        TrialTime=int(round(time() * 1000))-startTIME
                        #YearAnswer=int(NUMBERBANK[0]+NUMBERBANK[1]+NUMBERBANK[2]+NUMBERBANK[3])
                        return ScreenNumber, TrialTime, ERRORS, Choice, RESET
                        StartTrial=True                       
                    else:
                        ERRORS=ERRORS+1
                        screen.clear()
                        viewport.draw()
                        viewportmasks.draw()
                        #show the warning box, since this is a "practice" screen
                        viewportwarnBOX.draw()
                        VisionEgg.Core.swap_buffers()
                        #it'll stay up until something else is clicked


                elif x >= 351  and x <= 507  and y <= 486  and y >=427 :
                   ## ACID
                    EXITLIST=[0,0,0]
                    if Choice[0]=="Acid":
                        # if already selected, unselect and move pertinent mask offscreen
                        maskblue = TextureStimulus(texture=useTHISmask,position=(-200,-200), anchor='upperleft', max_alpha=0.50)
                        MASKLIST[0]=maskblue
                        Choice[0]=" "
                        ANSWERED=0
                    else:
                        # otherwise, select and move pertinent mask over the word
                        maskblue = TextureStimulus(texture=useTHISmask,position=(351,486), anchor='upperleft', max_alpha=0.50)
                        MASKLIST[0]=maskblue
                        Choice[0]="Acid"
                        ANSWERED=1
                    screen.clear()
                    viewport.draw()
                    viewportmasks.draw()
                    VisionEgg.Core.swap_buffers()
                elif x >= 351  and x <= 507  and y <= 419  and y >=360 :
                   ## DIME
                    EXITLIST=[0,0,0]
                    if Choice[0]=="Dime":
                        # if already selected, unselect and move pertinent mask offscreen
                        maskblue = TextureStimulus(texture=useTHISmask,position=(-200,-200), anchor='upperleft', max_alpha=0.50)
                        MASKLIST[0]=maskblue
                        Choice[0]=" "
                        ANSWERED=0
                    else:
                        # otherwise, select and move pertinent mask over the word
                        maskblue = TextureStimulus(texture=useTHISmask,position=(351,419), anchor='upperleft', max_alpha=0.50)
                        MASKLIST[0]=maskblue
                        Choice[0]="Dime"
                        ANSWERED=1
                    screen.clear()
                    viewport.draw()
                    viewportmasks.draw()
                    VisionEgg.Core.swap_buffers()
                elif x >= 351  and x <= 507  and y <= 352  and y >=293 :
                  ## FARM
                    EXITLIST=[0,0,0]
                    if Choice[0]=="Farm":
                        # if already selected, unselect and move pertinent mask offscreen
                        maskblue = TextureStimulus(texture=useTHISmask,position=(-200,-200), anchor='upperleft', max_alpha=0.50)
                        MASKLIST[0]=maskblue
                        Choice[0]=" "
                        ANSWERED=0
                    else:
                        # otherwise, select and move pertinent mask over the word
                        maskblue = TextureStimulus(texture=useTHISmask,position=(351,352), anchor='upperleft', max_alpha=0.50)
                        MASKLIST[0]=maskblue
                        Choice[0]="Farm"
                        ANSWERED=1
                    screen.clear()
                    viewport.draw()
                    viewportmasks.draw()
                    VisionEgg.Core.swap_buffers()
                elif x >= 351  and x <= 507  and y <= 285  and y >=226 :
                  ## GOLD
                    EXITLIST=[0,0,0]
                    if Choice[0]=="Gold":
                        # if already selected, unselect and move pertinent mask offscreen
                        maskblue = TextureStimulus(texture=useTHISmask,position=(-200,-200), anchor='upperleft', max_alpha=0.50)
                        MASKLIST[0]=maskblue
                        Choice[0]=" "
                        ANSWERED=0
                    else:
                        # otherwise, select and move pertinent mask over the word
                        maskblue = TextureStimulus(texture=useTHISmask,position=(351,286), anchor='upperleft', max_alpha=0.50)
                        MASKLIST[0]=maskblue
                        Choice[0]="Gold"
                        ANSWERED=1
                    screen.clear()
                    viewport.draw()
                    viewportmasks.draw()
                    VisionEgg.Core.swap_buffers()
                elif x >= 351  and x <= 507  and y <= 220  and y >=159 :
                  ## JAZZ
                    EXITLIST=[0,0,0]
                    if Choice[0]=="Jazz":
                        # if already selected, unselect and move pertinent mask offscreen
                        maskblue = TextureStimulus(texture=useTHISmask,position=(-200,-200), anchor='upperleft', max_alpha=0.50)
                        MASKLIST[0]=maskblue
                        Choice[0]=" "
                        ANSWERED=0
                    else:
                        # otherwise, select and move pertinent mask over the word
                        maskblue = TextureStimulus(texture=useTHISmask,position=(351,220), anchor='upperleft', max_alpha=0.50)
                        MASKLIST[0]=maskblue
                        Choice[0]="Jazz"
                        ANSWERED=1
                    screen.clear()
                    viewport.draw()
                    viewportmasks.draw()
                    VisionEgg.Core.swap_buffers()

                elif x >= 516  and x <= 671  and y <= 486  and y >=427 :
                  ## KNOT
                    EXITLIST=[0,0,0]
                    if Choice[0]=="Knot":
                        # if already selected, unselect and move pertinent mask offscreen
                        maskblue = TextureStimulus(texture=useTHISmask,position=(-200,-200), anchor='upperleft', max_alpha=0.50)
                        MASKLIST[0]=maskblue
                        Choice[0]=" "
                        ANSWERED=0
                    else:
                        # otherwise, select and move pertinent mask over the word
                        maskblue = TextureStimulus(texture=useTHISmask,position=(516,486), anchor='upperleft', max_alpha=0.50)
                        MASKLIST[0]=maskblue
                        Choice[0]="Knot"
                        ANSWERED=1
                    screen.clear()
                    viewport.draw()
                    viewportmasks.draw()
                    VisionEgg.Core.swap_buffers()
                elif x >= 516  and x <= 671  and y <= 419  and y >=360 :
                  ## OVEN
                    EXITLIST=[0,0,0]
                    if Choice[0]=="Oven":
                        # if already selected, unselect and move pertinent mask offscreen
                        maskblue = TextureStimulus(texture=useTHISmask,position=(-200,-200), anchor='upperleft', max_alpha=0.50)
                        MASKLIST[0]=maskblue
                        Choice[0]=" "
                        ANSWERED=0
                    else:
                        # otherwise, select and move pertinent mask over the word
                        maskblue = TextureStimulus(texture=useTHISmask,position=(516,419), anchor='upperleft', max_alpha=0.50)
                        MASKLIST[0]=maskblue
                        Choice[0]="Oven"
                        ANSWERED=1
                    screen.clear()
                    viewport.draw()
                    viewportmasks.draw()
                    VisionEgg.Core.swap_buffers()
                elif x >= 516  and x <= 671  and y <= 352  and y >=293 :
                  ## SHOE
                    EXITLIST=[0,0,0]
                    if Choice[0]=="Shoe":
                        # if already selected, unselect and move pertinent mask offscreen
                        maskblue = TextureStimulus(texture=useTHISmask,position=(-200,-200), anchor='upperleft', max_alpha=0.50)
                        MASKLIST[0]=maskblue
                        Choice[0]=" "
                        ANSWERED=0
                    else:
                        # otherwise, select and move pertinent mask over the word
                        maskblue = TextureStimulus(texture=useTHISmask,position=(516,352), anchor='upperleft', max_alpha=0.50)
                        MASKLIST[0]=maskblue
                        Choice[0]="Shoe"
                        ANSWERED=1
                    screen.clear()
                    viewport.draw()
                    viewportmasks.draw()
                    VisionEgg.Core.swap_buffers()
                elif x >= 516  and x <= 671  and y <= 285  and y >=226 :
                  ## TREE
                    EXITLIST=[0,0,0]
                    if Choice[0]=="Tree":
                        # if already selected, unselect and move pertinent mask offscreen
                        maskblue = TextureStimulus(texture=useTHISmask,position=(-200,-200), anchor='upperleft', max_alpha=0.50)
                        MASKLIST[0]=maskblue
                        Choice[0]=" "
                        ANSWERED=0
                    else:
                        # otherwise, select and move pertinent mask over the word
                        maskblue = TextureStimulus(texture=useTHISmask,position=(516,286), anchor='upperleft', max_alpha=0.50)
                        MASKLIST[0]=maskblue
                        Choice[0]="Tree"
                        ANSWERED=1
                    screen.clear()
                    viewport.draw()
                    viewportmasks.draw()
                    VisionEgg.Core.swap_buffers()
                elif x >= 516  and x <= 671  and y <= 220  and y >=159 :
                  ## WOLF
                    EXITLIST=[0,0,0]
                    if Choice[0]=="Wolf":
                        # if already selected, unselect and move pertinent mask offscreen
                        maskblue = TextureStimulus(texture=useTHISmask,position=(-200,-200), anchor='upperleft', max_alpha=0.50)
                        MASKLIST[0]=maskblue
                        Choice[0]=" "
                        ANSWERED=0
                    else:
                        # otherwise, select and move pertinent mask over the word
                        maskblue = TextureStimulus(texture=useTHISmask,position=(516,220), anchor='upperleft', max_alpha=0.50)
                        MASKLIST[0]=maskblue
                        Choice[0]="Wolf"
                        ANSWERED=1
                    screen.clear()
                    viewport.draw()
                    viewportmasks.draw()
                    VisionEgg.Core.swap_buffers()
                ##
                ## now we see the practical application of the EXITLIST:
                elif x >= 0 and x <=24 and y >= 584 and y <=600:
                   if EXITLIST==[0,0,0]:
                       EXITLIST[0]=1
                       text0 = Text(text="O",color=(0,0,0),position=(0,600),font_size=30,anchor='center')
                       text1 = Text(text="O",color=(0,0,0),position=(0,600),font_size=30,anchor='center')
                       viewportTEXT = VisionEgg.Core.Viewport(screen=screen, size=screen.size, stimuli=[text0, text1])
                       VisionEgg.Core.swap_buffers()
                       screen.clear()
                       viewport.draw()
                       viewportmasks.draw()
                       viewportTEXT.draw()
                       VisionEgg.Core.swap_buffers()
                elif x >= 1008 and x <=1024 and y >= 584 and y <=600:
                    if EXITLIST==[1,0,0]:
                       EXITLIST[1]=1
                       text0 = Text(text="O",color=(0,0,0),position=(0,600),font_size=30,anchor='center')
                       text1 = Text(text="O",color=(0,0,0),position=(1024,600),font_size=30,anchor='center')
                       viewportTEXT = VisionEgg.Core.Viewport(screen=screen, size=screen.size, stimuli=[text0, text1])
                       VisionEgg.Core.swap_buffers()
                       screen.clear()
                       viewport.draw()
                       viewportmasks.draw()
                       viewportTEXT.draw()
                       VisionEgg.Core.swap_buffers()
                elif x >= 1008 and x <=1024 and y >= 0 and y <=16:
                    if EXITLIST==[1,1,0]:
                        ScreenNumber, RESET = ESCAPEscreen(ScreenNumber, RESET)
###  ###   ###  # #     ### ALWAYS REMEMBER TO UPDATE THE RETURN INFO!  ##   #   #   #####  ##  ###    ### ### 
                        return ScreenNumber, TrialTime, ERRORS, Choice, RESET
                        StartTrial=True


####################################################################################################
####################################################################################################
####################################################################################################
####################################################################################################
####################################################################################################
def PICKmanyWORDS(ScreenNumber, TrialTime, ERRORS, Choice, RESET):
    x=-1
    y=-1
    #reset variables (in case not done already)
    EXITLIST=[0,0,0]
    ANSWERS=0
    Choice=[" "] 
    ERRORS=0
    #make and show background
    backgroundIMAGE = TextureStimulus(texture=taskbackgrounds[1],position=(0,0))
    viewport = VisionEgg.Core.Viewport(screen=screen, size=screen.size, stimuli=[backgroundIMAGE])
    screen.clear()
    viewport.draw()
    warnBOX_early = TextureStimulus(texture=notyetboxes[1],position=(830,150), anchor='center', max_alpha=0.80)
    warnBOX_late = TextureStimulus(texture=notyetboxes[2],position=(830,150), anchor='center', max_alpha=0.80)
    viewportwarnBOX_early = VisionEgg.Core.Viewport(screen=screen, size=screen.size, stimuli=[warnBOX_early])
    viewportwarnBOX_late = VisionEgg.Core.Viewport(screen=screen, size=screen.size, stimuli=[warnBOX_late])
    useTHISmask=masks[1]
    maskblue = TextureStimulus(texture=useTHISmask,position=(-100,-100), anchor='center', max_alpha=0.50)    
    MASKLIST=[maskblue]
     ## we'll modify the MASKLIST depending on button presses....
    viewportmasks = VisionEgg.Core.Viewport(screen=screen, size=screen.size, stimuli=MASKLIST)
    VisionEgg.Core.swap_buffers()
    # start clock
    startTIME=int(round(time() * 1000))
    StartTrial=False
    screen.clear()
    viewport.draw()
    VisionEgg.Core.swap_buffers()
    while not StartTrial:
        for event in pygame.event.get():
            if event.type == pygame.locals.MOUSEBUTTONDOWN:
                if (int(round(time() * 1000))-startTIME) > 100:
                    x,y = pygame.mouse.get_pos()
## pygame.mouse.get_pos() gives coordinates with the LOWER LEFT, not UPPER LEFT (as in visionegg) corner as the origin.
## before we get too complicated, will probably want to flip things around:
                y=600-y
                if x >= 904  and x <= 997  and y >= 0  and y <=36 :
                    EXITLIST=[0,0,0]
                    ## the "touch here when done" box. Action depends on ANSWERED
                    if ANSWERS == 2 and "BANANA" in Choice and "ORANGE" in Choice:
                        ## trial time is in seconds
                        TrialTime=int(round(time() * 1000))-startTIME
                        #YearAnswer=int(NUMBERBANK[0]+NUMBERBANK[1]+NUMBERBANK[2]+NUMBERBANK[3])
                        return ScreenNumber, TrialTime, ERRORS, Choice, RESET
                        StartTrial=True                       
                    elif ANSWERS < 2:
                        ERRORS=ERRORS+1
                        screen.clear()
                        viewport.draw()
                        viewportmasks.draw()
                        #show the warning box, since this is a "practice" screen
                        viewportwarnBOX_early.draw()
                        VisionEgg.Core.swap_buffers()
                        #it'll stay up until something else is clicked
                    else:
                        # this last "else" would cover ANSWERS==2 but not BANANA and ORANGE, so instructed to pick only fruit,
                        # or, ANSWERS > 2 in which case same applies
                        ERRORS=ERRORS+1
                        screen.clear()
                        viewport.draw()
                        viewportmasks.draw()
                        #show the warning box, since this is a "practice" screen
                        viewportwarnBOX_late.draw()
                        VisionEgg.Core.swap_buffers()
                        #it'll stay up until something else is clicked

                elif x >= 411  and x <= 613  and y <=485  and y >= 428 :
                   ## BANANA
                    EXITLIST=[0,0,0]
                    if "BANANA" in Choice:
                        ANSWERS=ANSWERS-1
                        which_is_it=Choice.index("BANANA")
                        # which_is_it also helps us find the mask in the list, so that can be removed. 
                        # if already selected, unselect and move pertinent mask offscreen
                        del Choice[which_is_it]
                        del MASKLIST[which_is_it]
                    else:
                        # otherwise, select and move pertinent mask over the word
                        maskblue = TextureStimulus(texture=useTHISmask,position=(411,485), anchor='upperleft', max_alpha=0.50)
                        MASKLIST.append(maskblue)
                        Choice.append("BANANA")
                        ANSWERS=ANSWERS+1
                    screen.clear()
                    viewport.draw()
                    viewportmasks.draw()
                    VisionEgg.Core.swap_buffers()
                elif x >= 411  and x <= 613  and y <=419  and y >= 362 :
                   ## CHURCH
                    EXITLIST=[0,0,0]
                    if "CHURCH" in Choice:
                        ANSWERS=ANSWERS-1
                        which_is_it=Choice.index("CHURCH")
                        # which_is_it also helps us find the mask in the list, so that can be removed. 
                        # if already selected, unselect and move pertinent mask offscreen
                        del Choice[which_is_it]
                        del MASKLIST[which_is_it]
                    else:
                        # otherwise, select and move pertinent mask over the word
                        maskblue = TextureStimulus(texture=useTHISmask,position=(411,419), anchor='upperleft', max_alpha=0.50)
                        MASKLIST.append(maskblue)
                        Choice.append("CHURCH")
                        ANSWERS=ANSWERS+1
                    screen.clear()
                    viewport.draw()
                    viewportmasks.draw()
                    VisionEgg.Core.swap_buffers()
                elif x >= 411  and x <= 613  and y <=353  and y >= 296 :
                   ## ORANGE
                    EXITLIST=[0,0,0]
                    if "ORANGE" in Choice:
                        ANSWERS=ANSWERS-1
                        which_is_it=Choice.index("ORANGE")
                        # which_is_it also helps us find the mask in the list, so that can be removed. 
                        # if already selected, unselect and move pertinent mask offscreen
                        del Choice[which_is_it]
                        del MASKLIST[which_is_it]
                    else:
                        # otherwise, select and move pertinent mask over the word
                        maskblue = TextureStimulus(texture=useTHISmask,position=(411,353), anchor='upperleft', max_alpha=0.50)
                        MASKLIST.append(maskblue)
                        Choice.append("ORANGE")
                        ANSWERS=ANSWERS+1
                    screen.clear()
                    viewport.draw()
                    viewportmasks.draw()
                    VisionEgg.Core.swap_buffers()
                elif x >= 411  and x <= 613  and y <=287  and y >= 230 :
                   ## STAPLE
                    EXITLIST=[0,0,0]
                    if "STAPLE" in Choice:
                        ANSWERS=ANSWERS-1
                        which_is_it=Choice.index("STAPLE")
                        # which_is_it also helps us find the mask in the list, so that can be removed. 
                        # if already selected, unselect and move pertinent mask offscreen
                        del Choice[which_is_it]
                        del MASKLIST[which_is_it]
                    else:
                        # otherwise, select and move pertinent mask over the word
                        maskblue = TextureStimulus(texture=useTHISmask,position=(411,287), anchor='upperleft', max_alpha=0.50)
                        MASKLIST.append(maskblue)
                        Choice.append("STAPLE")
                        ANSWERS=ANSWERS+1
                    screen.clear()
                    viewport.draw()
                    viewportmasks.draw()
                    VisionEgg.Core.swap_buffers()
                ##
                ## now we see the practical application of the EXITLIST:
                elif x >= 0 and x <=24 and y >= 584 and y <=600:
                   if EXITLIST==[0,0,0]:
                       EXITLIST[0]=1
                       text0 = Text(text="O",color=(0,0,0),position=(0,600),font_size=30,anchor='center')
                       text1 = Text(text="O",color=(0,0,0),position=(0,600),font_size=30,anchor='center')
                       viewportTEXT = VisionEgg.Core.Viewport(screen=screen, size=screen.size, stimuli=[text0, text1])
                       VisionEgg.Core.swap_buffers()
                       screen.clear()
                       viewport.draw()
                       viewportmasks.draw()
                       viewportTEXT.draw()
                       VisionEgg.Core.swap_buffers()
                elif x >= 1008 and x <=1024 and y >= 584 and y <=600:
                    if EXITLIST==[1,0,0]:
                       EXITLIST[1]=1
                       text0 = Text(text="O",color=(0,0,0),position=(0,600),font_size=30,anchor='center')
                       text1 = Text(text="O",color=(0,0,0),position=(1024,600),font_size=30,anchor='center')
                       viewportTEXT = VisionEgg.Core.Viewport(screen=screen, size=screen.size, stimuli=[text0, text1])
                       VisionEgg.Core.swap_buffers()
                       screen.clear()
                       viewport.draw()
                       viewportmasks.draw()
                       viewportTEXT.draw()
                       VisionEgg.Core.swap_buffers()
                elif x >= 1008 and x <=1024 and y >= 0 and y <=16:
                    if EXITLIST==[1,1,0]:
                        ScreenNumber, RESET = ESCAPEscreen(ScreenNumber, RESET)
###  ###   ###  # #     ### ALWAYS REMEMBER TO UPDATE THE RETURN INFO!  ##   #   #   #####  ##  ###    ### ### 
                        return ScreenNumber, TrialTime, ERRORS, Choice, RESET
                        StartTrial=True


####################################################################################################
####################################################################################################
####################################################################################################
####################################################################################################
####################################################################################################
def NUMBERPAD(ScreenNumber, TrialTime, ERRORS, RESET):
    x=-1
    y=-1
    EXITLIST=[0,0,0]
    POSITION=0 # which of the four number positions are we at? (in NUMBERBANK)
    ERRORS=0
    TrialTime=-1
    NUMBERBANK=[" "," "," "," "]
    text0 = Text(text=NUMBERBANK[0],
                 color=(0,0.5,0),
                 position=(408,450), 
                 font_size=60,
                 anchor='center')
    text1 = Text(text=NUMBERBANK[1],
                 color=(0,0,0),
                 position=(477,450),
                 font_size=60,
                 anchor='center')
    text2 = Text(text=NUMBERBANK[2],
                 color=(0,0,0),
                 position=(546,450),
                 font_size=60,
                 anchor='center')
    text3 = Text(text=NUMBERBANK[3],
                 color=(0,0,0),
                 position=(615,450),
                 font_size=60,
                 anchor='center')
    warnBOX = TextureStimulus(texture=notyetboxes[3],position=(830,150), anchor='center', max_alpha=0.80)
    viewportwarnBOX = VisionEgg.Core.Viewport(screen=screen, size=screen.size, stimuli=[warnBOX])
    backgroundIMAGE = TextureStimulus(texture=taskbackgrounds[2],position=(0,0))
    viewport = VisionEgg.Core.Viewport(screen=screen, size=screen.size, stimuli=[backgroundIMAGE])
    viewportTEXT2 = VisionEgg.Core.Viewport(screen=screen, size=screen.size, stimuli=[text0, text1, text2, text3])
    #VisionEgg.Core.swap_buffers()
    screen.clear()
    viewport.draw()
    viewportTEXT2.draw()
    VisionEgg.Core.swap_buffers()
    StartTrial=False
    LASTTAP=0
    startTIME=int(round(time() * 1000))
    screen.clear()
    viewport.draw()
    viewportTEXT2.draw()
    VisionEgg.Core.swap_buffers()
    while not StartTrial:
        for event in pygame.event.get():
            if event.type == pygame.locals.MOUSEBUTTONDOWN:
                if (int(round(time() * 1000))-startTIME) > 100:
                    x,y = pygame.mouse.get_pos()
## pygame.mouse.get_pos() gives coordinates with the LOWER LEFT, not UPPER LEFT (as in visionegg) corner as the origin.
## before we get too complicated, will probably want to flip things around:
                y=600-y
                if x >= 904  and x <= 997  and y >= 0  and y <=36 :
                    EXITLIST=[0,0,0]
                    ## the "touch here when done" box. Actuion depends on whether there's a full answer.
                    ## i.e., if POSITION=4
                    if NUMBERBANK[0] != " ":
                        MOTOR_SPEED_LOG.append(int((round(time() * 1000))-startTIME)-LASTTAP)
                        LASTTAP=int((round(time() * 1000))-startTIME)
                    if POSITION == 3 and NUMBERBANK[0] == "1" and NUMBERBANK[1] == "2" and NUMBERBANK[2] == "3" and NUMBERBANK[3] == "9":
                        out_file.write('   NEXT_at_ms %d NA NA NA 2\n'%(int(round(time() * 1000))-startTIME))
                        TrialTime=int(round(time() * 1000))-startTIME
                        return ScreenNumber, TrialTime, ERRORS, RESET
                        StartTrial=True                       
                    else:
                        out_file.write('   NEXT_at_ms %d NA NA NA 2\n'%(int(round(time() * 1000))-startTIME))
                        ERRORS=ERRORS+1
                        screen.clear()
                        viewport.draw()
                        viewportTEXT2.draw()
                        viewportwarnBOX.draw()
                        VisionEgg.Core.swap_buffers()
  
                        
                elif x >= 406 and x <=474 and y >=322 and y <=386:
                    MOTOR_SPEED_LOG.append(int((round(time() * 1000))-startTIME)-LASTTAP)
                    LASTTAP=int((round(time() * 1000))-startTIME)
                    EXITLIST=[0,0,0]
                    ## button 1
                    NUMBERBANK[POSITION]="1"
                    out_file.write('   button1_at_ms %d NA NA NA 2\n'%(int(round(time() * 1000))-startTIME))
                    screen.clear()
                    text0 = Text(text=NUMBERBANK[0],color=(0,0,0),position=(408,450),font_size=60,anchor='center')
                    text1 = Text(text=NUMBERBANK[1],color=(0,0,0),position=(477,450),font_size=60,anchor='center')
                    text2 = Text(text=NUMBERBANK[2],color=(0,0,0),position=(546,450),font_size=60,anchor='center')
                    text3 = Text(text=NUMBERBANK[3],color=(0,0,0),position=(615,450),font_size=60,anchor='center')
                    viewportTEXT2 = VisionEgg.Core.Viewport(screen=screen, size=screen.size, stimuli=[text0, text1, text2, text3])
                    viewport.draw()
                    viewportTEXT2.draw()
                    VisionEgg.Core.swap_buffers()
                    if POSITION < 3:
                        ## advance position
                        POSITION=POSITION+1
                elif x >= 406 and x <=474 and y >=251 and y <=314:
                    MOTOR_SPEED_LOG.append(int((round(time() * 1000))-startTIME)-LASTTAP)
                    LASTTAP=int((round(time() * 1000))-startTIME)
                    EXITLIST=[0,0,0]
                    ## button 4
                    NUMBERBANK[POSITION]="4"
                    out_file.write('   button4_at_ms %d NA NA NA 2\n'%(int(round(time() * 1000))-startTIME))
                    screen.clear()
                    text0 = Text(text=NUMBERBANK[0],color=(0,0,0),position=(408,450),font_size=60,anchor='center')
                    text1 = Text(text=NUMBERBANK[1],color=(0,0,0),position=(477,450),font_size=60,anchor='center')
                    text2 = Text(text=NUMBERBANK[2],color=(0,0,0),position=(546,450),font_size=60,anchor='center')
                    text3 = Text(text=NUMBERBANK[3],color=(0,0,0),position=(615,450),font_size=60,anchor='center')
                    viewportTEXT2 = VisionEgg.Core.Viewport(screen=screen, size=screen.size, stimuli=[text0, text1, text2, text3])
                    viewport.draw()
                    viewportTEXT2.draw()
                    VisionEgg.Core.swap_buffers()
                    if POSITION < 3:
                        ## advance position
                        POSITION=POSITION+1
                elif x >= 406 and x <=474 and y >=180 and y <=245:
                    MOTOR_SPEED_LOG.append(int((round(time() * 1000))-startTIME)-LASTTAP)
                    LASTTAP=int((round(time() * 1000))-startTIME)
                    EXITLIST=[0,0,0]
                    ## button 7
                    NUMBERBANK[POSITION]="7"
                    out_file.write('   button7_at_ms %d NA NA NA 2\n'%(int(round(time() * 1000))-startTIME))
                    screen.clear()
                    text0 = Text(text=NUMBERBANK[0],color=(0,0,0),position=(408,450),font_size=60,anchor='center')
                    text1 = Text(text=NUMBERBANK[1],color=(0,0,0),position=(477,450),font_size=60,anchor='center')
                    text2 = Text(text=NUMBERBANK[2],color=(0,0,0),position=(546,450),font_size=60,anchor='center')
                    text3 = Text(text=NUMBERBANK[3],color=(0,0,0),position=(615,450),font_size=60,anchor='center')
                    viewportTEXT2 = VisionEgg.Core.Viewport(screen=screen, size=screen.size, stimuli=[text0, text1, text2, text3])
                    viewport.draw()
                    viewportTEXT2.draw()
                    VisionEgg.Core.swap_buffers()
                    if POSITION < 3:
                        ## advance position
                        POSITION=POSITION+1
                    
                elif x >= 479 and x <=546 and y >=109 and y <=174:
                    MOTOR_SPEED_LOG.append(int((round(time() * 1000))-startTIME)-LASTTAP)
                    LASTTAP=int((round(time() * 1000))-startTIME)
                    EXITLIST=[0,0,0]
                    ## button 0
                    NUMBERBANK[POSITION]="0"
                    out_file.write('   button0_at_ms %d NA NA NA 2\n'%(int(round(time() * 1000))-startTIME))
                    screen.clear()
                    text0 = Text(text=NUMBERBANK[0],color=(0,0,0),position=(408,450),font_size=60,anchor='center')
                    text1 = Text(text=NUMBERBANK[1],color=(0,0,0),position=(477,450),font_size=60,anchor='center')
                    text2 = Text(text=NUMBERBANK[2],color=(0,0,0),position=(546,450),font_size=60,anchor='center')
                    text3 = Text(text=NUMBERBANK[3],color=(0,0,0),position=(615,450),font_size=60,anchor='center')
                    viewportTEXT2 = VisionEgg.Core.Viewport(screen=screen, size=screen.size, stimuli=[text0, text1, text2, text3])
                    viewport.draw()
                    viewportTEXT2.draw()
                    VisionEgg.Core.swap_buffers()
                    if POSITION < 3:
                        ## advance position
                        POSITION=POSITION+1

                elif x >= 479 and x <=546 and y >=322 and y <=386:
                    MOTOR_SPEED_LOG.append(int((round(time() * 1000))-startTIME)-LASTTAP)
                    LASTTAP=int((round(time() * 1000))-startTIME)
                    EXITLIST=[0,0,0]
                    ## button 2
                    NUMBERBANK[POSITION]="2"
                    out_file.write('   button2_at_ms %d NA NA NA 2\n'%(int(round(time() * 1000))-startTIME))
                    screen.clear()
                    text0 = Text(text=NUMBERBANK[0],color=(0,0,0),position=(408,450),font_size=60,anchor='center')
                    text1 = Text(text=NUMBERBANK[1],color=(0,0,0),position=(477,450),font_size=60,anchor='center')
                    text2 = Text(text=NUMBERBANK[2],color=(0,0,0),position=(546,450),font_size=60,anchor='center')
                    text3 = Text(text=NUMBERBANK[3],color=(0,0,0),position=(615,450),font_size=60,anchor='center')
                    viewportTEXT2 = VisionEgg.Core.Viewport(screen=screen, size=screen.size, stimuli=[text0, text1, text2, text3])
                    viewport.draw()
                    viewportTEXT2.draw()
                    VisionEgg.Core.swap_buffers()
                    if POSITION < 3:
                        ## advance position
                        POSITION=POSITION+1
                elif x >= 479 and x <=546 and y >=251 and y <=314:
                    MOTOR_SPEED_LOG.append(int((round(time() * 1000))-startTIME)-LASTTAP)
                    LASTTAP=int((round(time() * 1000))-startTIME)
                    EXITLIST=[0,0,0]
                    ## button 5
                    NUMBERBANK[POSITION]="5"
                    out_file.write('   button5_at_ms %d NA NA NA 2\n'%(int(round(time() * 1000))-startTIME))
                    screen.clear()
                    text0 = Text(text=NUMBERBANK[0],color=(0,0,0),position=(408,450),font_size=60,anchor='center')
                    text1 = Text(text=NUMBERBANK[1],color=(0,0,0),position=(477,450),font_size=60,anchor='center')
                    text2 = Text(text=NUMBERBANK[2],color=(0,0,0),position=(546,450),font_size=60,anchor='center')
                    text3 = Text(text=NUMBERBANK[3],color=(0,0,0),position=(615,450),font_size=60,anchor='center')
                    viewportTEXT2 = VisionEgg.Core.Viewport(screen=screen, size=screen.size, stimuli=[text0, text1, text2, text3])
                    viewport.draw()
                    viewportTEXT2.draw()
                    VisionEgg.Core.swap_buffers()
                    if POSITION < 3:
                        ## advance position
                        POSITION=POSITION+1
                elif x >= 479 and x <=546 and y >=180 and y <=245:
                    MOTOR_SPEED_LOG.append(int((round(time() * 1000))-startTIME)-LASTTAP)
                    LASTTAP=int((round(time() * 1000))-startTIME)
                    EXITLIST=[0,0,0]
                    ## button 8
                    NUMBERBANK[POSITION]="8"
                    out_file.write('   button8_at_ms %d NA NA NA 2\n'%(int(round(time() * 1000))-startTIME))
                    screen.clear()
                    text0 = Text(text=NUMBERBANK[0],color=(0,0,0),position=(408,450),font_size=60,anchor='center')
                    text1 = Text(text=NUMBERBANK[1],color=(0,0,0),position=(477,450),font_size=60,anchor='center')
                    text2 = Text(text=NUMBERBANK[2],color=(0,0,0),position=(546,450),font_size=60,anchor='center')
                    text3 = Text(text=NUMBERBANK[3],color=(0,0,0),position=(615,450),font_size=60,anchor='center')
                    viewportTEXT2 = VisionEgg.Core.Viewport(screen=screen, size=screen.size, stimuli=[text0, text1, text2, text3])
                    viewport.draw()
                    viewportTEXT2.draw()
                    VisionEgg.Core.swap_buffers()
                    if POSITION < 3:
                        ## advance position
                        POSITION=POSITION+1

                elif x >= 552 and x <=620 and y >=322 and y <=386:
                    MOTOR_SPEED_LOG.append(int((round(time() * 1000))-startTIME)-LASTTAP)
                    LASTTAP=int((round(time() * 1000))-startTIME)
                    EXITLIST=[0,0,0]
                    ## button 3
                    NUMBERBANK[POSITION]="3"
                    out_file.write('   button3_at_ms %d NA NA NA 2\n'%(int(round(time() * 1000))-startTIME))
                    screen.clear()
                    text0 = Text(text=NUMBERBANK[0],color=(0,0,0),position=(408,450),font_size=60,anchor='center')
                    text1 = Text(text=NUMBERBANK[1],color=(0,0,0),position=(477,450),font_size=60,anchor='center')
                    text2 = Text(text=NUMBERBANK[2],color=(0,0,0),position=(546,450),font_size=60,anchor='center')
                    text3 = Text(text=NUMBERBANK[3],color=(0,0,0),position=(615,450),font_size=60,anchor='center')
                    viewportTEXT2 = VisionEgg.Core.Viewport(screen=screen, size=screen.size, stimuli=[text0, text1, text2, text3])
                    viewport.draw()
                    viewportTEXT2.draw()
                    VisionEgg.Core.swap_buffers()
                    if POSITION < 3:
                        ## advance position
                        POSITION=POSITION+1
                elif x >= 552 and x <=620 and y >=251 and y <=314:
                    MOTOR_SPEED_LOG.append(int((round(time() * 1000))-startTIME)-LASTTAP)
                    LASTTAP=int((round(time() * 1000))-startTIME)
                    EXITLIST=[0,0,0]
                    ## button 6
                    NUMBERBANK[POSITION]="6"
                    out_file.write('   button6_at_ms %d NA NA NA 2\n'%(int(round(time() * 1000))-startTIME))
                    screen.clear()
                    text0 = Text(text=NUMBERBANK[0],color=(0,0,0),position=(408,450),font_size=60,anchor='center')
                    text1 = Text(text=NUMBERBANK[1],color=(0,0,0),position=(477,450),font_size=60,anchor='center')
                    text2 = Text(text=NUMBERBANK[2],color=(0,0,0),position=(546,450),font_size=60,anchor='center')
                    text3 = Text(text=NUMBERBANK[3],color=(0,0,0),position=(615,450),font_size=60,anchor='center')
                    viewportTEXT2 = VisionEgg.Core.Viewport(screen=screen, size=screen.size, stimuli=[text0, text1, text2, text3])
                    viewport.draw()
                    viewportTEXT2.draw()
                    VisionEgg.Core.swap_buffers()
                    if POSITION < 3:
                        ## advance position
                        POSITION=POSITION+1
                elif x >= 552 and x <=620 and y >=180 and y <=245:
                    MOTOR_SPEED_LOG.append(int((round(time() * 1000))-startTIME)-LASTTAP)
                    LASTTAP=int((round(time() * 1000))-startTIME)
                    EXITLIST=[0,0,0]
                    ## button 9
                    NUMBERBANK[POSITION]="9"
                    out_file.write('   button9_at_ms %d NA NA NA 2\n'%(int(round(time() * 1000))-startTIME))
                    screen.clear()
                    text0 = Text(text=NUMBERBANK[0],color=(0,0,0),position=(408,450),font_size=60,anchor='center')
                    text1 = Text(text=NUMBERBANK[1],color=(0,0,0),position=(477,450),font_size=60,anchor='center')
                    text2 = Text(text=NUMBERBANK[2],color=(0,0,0),position=(546,450),font_size=60,anchor='center')
                    text3 = Text(text=NUMBERBANK[3],color=(0,0,0),position=(615,450),font_size=60,anchor='center')
                    viewportTEXT2 = VisionEgg.Core.Viewport(screen=screen, size=screen.size, stimuli=[text0, text1, text2, text3])
                    viewport.draw()
                    viewportTEXT2.draw()
                    VisionEgg.Core.swap_buffers()
                    if POSITION < 3:
                        ## advance position
                        POSITION=POSITION+1
 
                elif x >= 419 and x <=609 and y >=40 and y <=94:
                    MOTOR_SPEED_LOG.append(int((round(time() * 1000))-startTIME)-LASTTAP)
                    LASTTAP=int((round(time() * 1000))-startTIME)
                    EXITLIST=[0,0,0]
                    out_file.write('   buttonDELETE_at_ms %d NA NA NA 2\n'%(int(round(time() * 1000))-startTIME))
                    ## DELETE button
                    ## if POSITION == 0, do nothing. This means there are no numbers
                    ## if POSITION == 1, you just wrote your first number (in POSITION 0) and then shifted over
                    ##  OR, you were in POSITION 2 ready to write there, but instead hit delete, which made you step back
                    ##  a position and wipe the value in NUMBERBANK[1].
                    ##  either way, if POSITION == 1, we want to wipe NUMBERBANK[0] and set POSITION to 0
                    if POSITION > 0:
                        if POSITION == 3 and NUMBERBANK[3] != " ":
                            NUMBERBANK[POSITION]=" "
                        else:
                            POSITION=POSITION-1
                            NUMBERBANK[POSITION]=" "                            
                        screen.clear()
                        text0 = Text(text=NUMBERBANK[0],color=(0,0,0),position=(408,450),font_size=60,anchor='center')
                        text1 = Text(text=NUMBERBANK[1],color=(0,0,0),position=(477,450),font_size=60,anchor='center')
                        text2 = Text(text=NUMBERBANK[2],color=(0,0,0),position=(546,450),font_size=60,anchor='center')
                        text3 = Text(text=NUMBERBANK[3],color=(0,0,0),position=(615,450),font_size=60,anchor='center')
                        viewportTEXT2 = VisionEgg.Core.Viewport(screen=screen, size=screen.size, stimuli=[text0, text1, text2, text3])
                        viewport.draw()
                        viewportTEXT2.draw()
                        VisionEgg.Core.swap_buffers()
                ##
                ## now we see the practical application of the EXITLIST:
                elif x >= 0 and x <=24 and y >= 584 and y <=600:
                   if EXITLIST==[0,0,0]:
                       EXITLIST[0]=1
                       text0 = Text(text="O",color=(0,0,0),position=(0,600),font_size=30,anchor='center')
                       text1 = Text(text="O",color=(0,0,0),position=(0,600),font_size=30,anchor='center')
                       viewportTEXT = VisionEgg.Core.Viewport(screen=screen, size=screen.size, stimuli=[text0, text1])
                       VisionEgg.Core.swap_buffers()
                       screen.clear()
                       viewport.draw()
                       viewportTEXT2.draw()
                       viewportTEXT.draw()
                       VisionEgg.Core.swap_buffers()
                elif x >= 1008 and x <=1024 and y >= 584 and y <=600:
                    if EXITLIST==[1,0,0]:
                       EXITLIST[1]=1
                       text0 = Text(text="O",color=(0,0,0),position=(0,600),font_size=30,anchor='center')
                       text1 = Text(text="O",color=(0,0,0),position=(1024,600),font_size=30,anchor='center')
                       viewportTEXT = VisionEgg.Core.Viewport(screen=screen, size=screen.size, stimuli=[text0, text1])
                       VisionEgg.Core.swap_buffers()
                       screen.clear()
                       viewport.draw()
                       viewportTEXT2.draw()
                       viewportTEXT.draw()
                       VisionEgg.Core.swap_buffers()
                elif x >= 1008 and x <=1024 and y >= 0 and y <=16:
                    if EXITLIST==[1,1,0]:
                        ScreenNumber, RESET = ESCAPEscreen(ScreenNumber, RESET)
###  ###   ###  # #     ### ALWAYS REMEMBER TO UPDATE THE RETURN INFO!  ##   #   #   #####  ##  ###    ### ### 
                        return ScreenNumber, TrialTime, ERRORS, RESET
                        StartTrial=True


  
####################################################################################################
####################################################################################################
####################################################################################################
####################################################################################################
####################################################################################################
## note, in FLASHwords, in 0-7-0, I noticed that rubbing the touchscreen during a word could
## crash python.
## hypothesis is that pygame.time.delay is just logging all the "mouse" activity and waiting to act until then.
## and so too much builds up causing a crash.
## clumsy solution is to use several smaller units of time
## (e.g., instead of pygame.time.delay(2000), do pygame.time.delay(100) twenty times.
## but this didn't work in 0-7-1.
## so, replaced with loop checking time. 
def FLASHwords(ScreenNumber):
    text0 = Text(text="O",color=(0,0,0),position=(-100,-100),font_size=60,anchor='center')
    text1 = text0
    if ScreenNumber==13:
        stim = TextureStimulus(texture=wordscreens[0],position=(0,0))
        text0 = Text(text="REMEMBER THE WORDS",color=(1.0,1.0,1.0),position=(512,350),font_size=72,anchor='center')
        text1 = Text(text="...HERE THEY COME!...",color=(1.0,1.0,1.0),position=(512,250),font_size=72,anchor='center')
    elif ScreenNumber==14:
        stim = TextureStimulus(texture=wordscreens[1],position=(0,0))
    elif ScreenNumber==15:
        stim = TextureStimulus(texture=wordscreens[2],position=(0,0))
    elif ScreenNumber==16:
        stim = TextureStimulus(texture=wordscreens[3],position=(0,0))
    elif ScreenNumber==17:
        stim = TextureStimulus(texture=wordscreens[4],position=(0,0))
    elif ScreenNumber==18:
        stim = TextureStimulus(texture=wordscreens[5],position=(0,0))
    elif ScreenNumber==19:
        stim = TextureStimulus(texture=wordscreens[6],position=(0,0))    
    elif ScreenNumber==20:
        stim = TextureStimulus(texture=wordscreens[7],position=(0,0))
    elif ScreenNumber==21:
        stim = TextureStimulus(texture=wordscreens[8],position=(0,0))
    elif ScreenNumber==22:
        stim = TextureStimulus(texture=wordscreens[9],position=(0,0))
    elif ScreenNumber==23:
        stim = TextureStimulus(texture=wordscreens[10],position=(0,0))
    viewport = VisionEgg.Core.Viewport(screen=screen, size=screen.size, stimuli=[stim,stim])
    screen.clear()
    viewportTEXT = VisionEgg.Core.Viewport(screen=screen, size=screen.size, stimuli=[text0, text1])
    viewport.draw()
    viewportTEXT.draw()
    startTIMEscreen=int(round(time() * 1000))
    VisionEgg.Core.swap_buffers()
    screen.clear()
    viewport.draw()
    viewportTEXT.draw()
    VisionEgg.Core.swap_buffers()
    if ScreenNumber==13:
        currentTIMEscreen=int(round(time() * 1000))
        while (currentTIMEscreen-startTIMEscreen) < 2000:  # 2 s of promt/cue
            currentTIMEscreen=int(round(time() * 1000))
            for event in pygame.event.get():
                if event.type == pygame.locals.MOUSEBUTTONDOWN:
                    x,y = pygame.mouse.get_pos()
    elif ScreenNumber==14:
        currentTIMEscreen=int(round(time() * 1000))
        while (currentTIMEscreen-startTIMEscreen) < 2000:  # 2 s first word
            currentTIMEscreen=int(round(time() * 1000))
            for event in pygame.event.get():
                if event.type == pygame.locals.MOUSEBUTTONDOWN:
                    x,y = pygame.mouse.get_pos()
    elif ScreenNumber==15:
        currentTIMEscreen=int(round(time() * 1000))
        while (currentTIMEscreen-startTIMEscreen) < 1000:  # 1 s between words
            currentTIMEscreen=int(round(time() * 1000))
            for event in pygame.event.get():
                if event.type == pygame.locals.MOUSEBUTTONDOWN:
                    x,y = pygame.mouse.get_pos()
    elif ScreenNumber==16:
        currentTIMEscreen=int(round(time() * 1000))
        while (currentTIMEscreen-startTIMEscreen) < 2000:  # 2 s first word
            currentTIMEscreen=int(round(time() * 1000))
            for event in pygame.event.get():
                if event.type == pygame.locals.MOUSEBUTTONDOWN:
                    x,y = pygame.mouse.get_pos()
    elif ScreenNumber==17:
        currentTIMEscreen=int(round(time() * 1000))
        while (currentTIMEscreen-startTIMEscreen) < 1000:  # 1 s between words
            currentTIMEscreen=int(round(time() * 1000))
            for event in pygame.event.get():
                if event.type == pygame.locals.MOUSEBUTTONDOWN:
                    x,y = pygame.mouse.get_pos()
    elif ScreenNumber==18:
        currentTIMEscreen=int(round(time() * 1000))
        while (currentTIMEscreen-startTIMEscreen) < 2000:  # 2 s first word
            currentTIMEscreen=int(round(time() * 1000))
            for event in pygame.event.get():
                if event.type == pygame.locals.MOUSEBUTTONDOWN:
                    x,y = pygame.mouse.get_pos()
    elif ScreenNumber==19:
        currentTIMEscreen=int(round(time() * 1000))
        while (currentTIMEscreen-startTIMEscreen) < 1000:  # 1 s between words
            currentTIMEscreen=int(round(time() * 1000))
            for event in pygame.event.get():
                if event.type == pygame.locals.MOUSEBUTTONDOWN:
                    x,y = pygame.mouse.get_pos()
    elif ScreenNumber==20:
        currentTIMEscreen=int(round(time() * 1000))
        while (currentTIMEscreen-startTIMEscreen) < 2000:  # 2 s first word
            currentTIMEscreen=int(round(time() * 1000))
            for event in pygame.event.get():
                if event.type == pygame.locals.MOUSEBUTTONDOWN:
                    x,y = pygame.mouse.get_pos()
    elif ScreenNumber==21:
        currentTIMEscreen=int(round(time() * 1000))
        while (currentTIMEscreen-startTIMEscreen) < 1000:  # 1 s between words
            currentTIMEscreen=int(round(time() * 1000))
            for event in pygame.event.get():
                if event.type == pygame.locals.MOUSEBUTTONDOWN:
                    x,y = pygame.mouse.get_pos()
    elif ScreenNumber==22:
        currentTIMEscreen=int(round(time() * 1000))
        while (currentTIMEscreen-startTIMEscreen) < 2000:  # 2 s first word
            currentTIMEscreen=int(round(time() * 1000))
            for event in pygame.event.get():
                if event.type == pygame.locals.MOUSEBUTTONDOWN:
                    x,y = pygame.mouse.get_pos()
    elif ScreenNumber==23:
        currentTIMEscreen=int(round(time() * 1000))
        while (currentTIMEscreen-startTIMEscreen) < 1000:  # 1 s between words
            currentTIMEscreen=int(round(time() * 1000))
            for event in pygame.event.get():
                if event.type == pygame.locals.MOUSEBUTTONDOWN:
                    x,y = pygame.mouse.get_pos()
    ScreenNumber=ScreenNumber+1
    return(ScreenNumber)


####################################################################################################
####################################################################################################
####################################################################################################
####################################################################################################
####################################################################################################
def YEARPAD(ScreenNumber, TrialTime, RESPONSE, ERRORS, RESET):
    x=-1
    y=-1
    EXITLIST=[0,0,0]
    POSITION=0 # which of the four number positions are we at? (in NUMBERBANK)
    RESPONSE=0
    ERRORS=0
    TrialTime=-1
    NUMBERBANK=[" "," "," "," "]
    text0 = Text(text=NUMBERBANK[0],
                 color=(0,0.5,0),
                 position=(408,450), 
                 font_size=60,
                 anchor='center')
    text1 = Text(text=NUMBERBANK[1],
                 color=(0,0,0),
                 position=(477,450),
                 font_size=60,
                 anchor='center')
    text2 = Text(text=NUMBERBANK[2],
                 color=(0,0,0),
                 position=(546,450),
                 font_size=60,
                 anchor='center')
    text3 = Text(text=NUMBERBANK[3],
                 color=(0,0,0),
                 position=(615,450),
                 font_size=60,
                 anchor='center')
    warnBOX = TextureStimulus(texture=notyetboxes[6],position=(830,150), anchor='center', max_alpha=0.80)
    viewportwarnBOX = VisionEgg.Core.Viewport(screen=screen, size=screen.size, stimuli=[warnBOX])
    backgroundIMAGE = TextureStimulus(texture=taskbackgrounds[4],position=(0,0))
    viewport = VisionEgg.Core.Viewport(screen=screen, size=screen.size, stimuli=[backgroundIMAGE])
    viewportTEXT2 = VisionEgg.Core.Viewport(screen=screen, size=screen.size, stimuli=[text0, text1, text2, text3])
    #VisionEgg.Core.swap_buffers()
    screen.clear()
    viewport.draw()
    viewportTEXT2.draw()
    VisionEgg.Core.swap_buffers()
    StartTrial=False
    startTIME=int(round(time() * 1000))
    screen.clear()
    viewport.draw()
    LASTTAP=0
    viewportTEXT2.draw()
    VisionEgg.Core.swap_buffers()
    while not StartTrial:
        for event in pygame.event.get():
            if event.type == pygame.locals.MOUSEBUTTONDOWN:
                if (int(round(time() * 1000))-startTIME) > 100:
                    x,y = pygame.mouse.get_pos()
## pygame.mouse.get_pos() gives coordinates with the LOWER LEFT, not UPPER LEFT (as in visionegg) corner as the origin.
## before we get too complicated, will probably want to flip things around:
                y=600-y
                if x >= 904  and x <= 997  and y >= 0  and y <=36 :
                    EXITLIST=[0,0,0]
                    ## the "touch here when done" box. Action depends on whether there's a full answer.
                    ## i.e., if POSITION=4
                    if NUMBERBANK[0] != " ":
                        MOTOR_SPEED_LOG.append(int((round(time() * 1000))-startTIME)-LASTTAP)
                        LASTTAP=int((round(time() * 1000))-startTIME)
                    if POSITION == 3 and NUMBERBANK[3] != " ":
                        out_file.write('   NEXT_at_ms %d NA NA NA 4\n'%(int(round(time() * 1000))-startTIME))
                        TrialTime=int(round(time() * 1000))-startTIME
                        RESPONSE=int(NUMBERBANK[0]+NUMBERBANK[1]+NUMBERBANK[2]+NUMBERBANK[3])
                        return ScreenNumber, TrialTime, RESPONSE, ERRORS, RESET
                        StartTrial=True                       
                    else:
                        out_file.write('   NEXT_at_ms %d NA NA NA 4\n'%(int(round(time() * 1000))-startTIME))
                        ERRORS=ERRORS+1
                        screen.clear()
                        viewport.draw()
                        viewportTEXT2.draw()
                        viewportwarnBOX.draw()
                        VisionEgg.Core.swap_buffers()
  
                        
                elif x >= 406 and x <=474 and y >=322 and y <=386:
                    MOTOR_SPEED_LOG.append(int((round(time() * 1000))-startTIME)-LASTTAP)
                    LASTTAP=int((round(time() * 1000))-startTIME)
                    EXITLIST=[0,0,0]
                    ## button 1
                    NUMBERBANK[POSITION]="1"
                    out_file.write('   button1_at_ms %d NA NA NA 4\n'%(int(round(time() * 1000))-startTIME))
                    screen.clear()
                    text0 = Text(text=NUMBERBANK[0],color=(0,0,0),position=(408,450),font_size=60,anchor='center')
                    text1 = Text(text=NUMBERBANK[1],color=(0,0,0),position=(477,450),font_size=60,anchor='center')
                    text2 = Text(text=NUMBERBANK[2],color=(0,0,0),position=(546,450),font_size=60,anchor='center')
                    text3 = Text(text=NUMBERBANK[3],color=(0,0,0),position=(615,450),font_size=60,anchor='center')
                    viewportTEXT2 = VisionEgg.Core.Viewport(screen=screen, size=screen.size, stimuli=[text0, text1, text2, text3])
                    viewport.draw()
                    viewportTEXT2.draw()
                    VisionEgg.Core.swap_buffers()
                    if POSITION < 3:
                        ## advance position
                        POSITION=POSITION+1
                elif x >= 406 and x <=474 and y >=251 and y <=314:
                    MOTOR_SPEED_LOG.append(int((round(time() * 1000))-startTIME)-LASTTAP)
                    LASTTAP=int((round(time() * 1000))-startTIME)
                    EXITLIST=[0,0,0]
                    ## button 4
                    NUMBERBANK[POSITION]="4"
                    out_file.write('   button4_at_ms %d NA NA NA 4\n'%(int(round(time() * 1000))-startTIME))
                    screen.clear()
                    text0 = Text(text=NUMBERBANK[0],color=(0,0,0),position=(408,450),font_size=60,anchor='center')
                    text1 = Text(text=NUMBERBANK[1],color=(0,0,0),position=(477,450),font_size=60,anchor='center')
                    text2 = Text(text=NUMBERBANK[2],color=(0,0,0),position=(546,450),font_size=60,anchor='center')
                    text3 = Text(text=NUMBERBANK[3],color=(0,0,0),position=(615,450),font_size=60,anchor='center')
                    viewportTEXT2 = VisionEgg.Core.Viewport(screen=screen, size=screen.size, stimuli=[text0, text1, text2, text3])
                    viewport.draw()
                    viewportTEXT2.draw()
                    VisionEgg.Core.swap_buffers()
                    if POSITION < 3:
                        ## advance position
                        POSITION=POSITION+1
                elif x >= 406 and x <=474 and y >=180 and y <=245:
                    MOTOR_SPEED_LOG.append(int((round(time() * 1000))-startTIME)-LASTTAP)
                    LASTTAP=int((round(time() * 1000))-startTIME)
                    EXITLIST=[0,0,0]
                    ## button 7
                    NUMBERBANK[POSITION]="7"
                    out_file.write('   button7_at_ms %d NA NA NA 4\n'%(int(round(time() * 1000))-startTIME))
                    screen.clear()
                    text0 = Text(text=NUMBERBANK[0],color=(0,0,0),position=(408,450),font_size=60,anchor='center')
                    text1 = Text(text=NUMBERBANK[1],color=(0,0,0),position=(477,450),font_size=60,anchor='center')
                    text2 = Text(text=NUMBERBANK[2],color=(0,0,0),position=(546,450),font_size=60,anchor='center')
                    text3 = Text(text=NUMBERBANK[3],color=(0,0,0),position=(615,450),font_size=60,anchor='center')
                    viewportTEXT2 = VisionEgg.Core.Viewport(screen=screen, size=screen.size, stimuli=[text0, text1, text2, text3])
                    viewport.draw()
                    viewportTEXT2.draw()
                    VisionEgg.Core.swap_buffers()
                    if POSITION < 3:
                        ## advance position
                        POSITION=POSITION+1
                    
                elif x >= 479 and x <=546 and y >=109 and y <=174:
                    MOTOR_SPEED_LOG.append(int((round(time() * 1000))-startTIME)-LASTTAP)
                    LASTTAP=int((round(time() * 1000))-startTIME)
                    EXITLIST=[0,0,0]
                    ## button 0
                    NUMBERBANK[POSITION]="0"
                    out_file.write('   button0_at_ms %d NA NA NA 4\n'%(int(round(time() * 1000))-startTIME))
                    screen.clear()
                    text0 = Text(text=NUMBERBANK[0],color=(0,0,0),position=(408,450),font_size=60,anchor='center')
                    text1 = Text(text=NUMBERBANK[1],color=(0,0,0),position=(477,450),font_size=60,anchor='center')
                    text2 = Text(text=NUMBERBANK[2],color=(0,0,0),position=(546,450),font_size=60,anchor='center')
                    text3 = Text(text=NUMBERBANK[3],color=(0,0,0),position=(615,450),font_size=60,anchor='center')
                    viewportTEXT2 = VisionEgg.Core.Viewport(screen=screen, size=screen.size, stimuli=[text0, text1, text2, text3])
                    viewport.draw()
                    viewportTEXT2.draw()
                    VisionEgg.Core.swap_buffers()
                    if POSITION < 3:
                        ## advance position
                        POSITION=POSITION+1

                elif x >= 479 and x <=546 and y >=322 and y <=386:
                    MOTOR_SPEED_LOG.append(int((round(time() * 1000))-startTIME)-LASTTAP)
                    LASTTAP=int((round(time() * 1000))-startTIME)
                    EXITLIST=[0,0,0]
                    ## button 2
                    NUMBERBANK[POSITION]="2"
                    out_file.write('   button2_at_ms %d NA NA NA 4\n'%(int(round(time() * 1000))-startTIME))
                    screen.clear()
                    text0 = Text(text=NUMBERBANK[0],color=(0,0,0),position=(408,450),font_size=60,anchor='center')
                    text1 = Text(text=NUMBERBANK[1],color=(0,0,0),position=(477,450),font_size=60,anchor='center')
                    text2 = Text(text=NUMBERBANK[2],color=(0,0,0),position=(546,450),font_size=60,anchor='center')
                    text3 = Text(text=NUMBERBANK[3],color=(0,0,0),position=(615,450),font_size=60,anchor='center')
                    viewportTEXT2 = VisionEgg.Core.Viewport(screen=screen, size=screen.size, stimuli=[text0, text1, text2, text3])
                    viewport.draw()
                    viewportTEXT2.draw()
                    VisionEgg.Core.swap_buffers()
                    if POSITION < 3:
                        ## advance position
                        POSITION=POSITION+1
                elif x >= 479 and x <=546 and y >=251 and y <=314:
                    MOTOR_SPEED_LOG.append(int((round(time() * 1000))-startTIME)-LASTTAP)
                    LASTTAP=int((round(time() * 1000))-startTIME)
                    EXITLIST=[0,0,0]
                    ## button 5
                    NUMBERBANK[POSITION]="5"
                    out_file.write('   button5_at_ms %d NA NA NA 4\n'%(int(round(time() * 1000))-startTIME))
                    screen.clear()
                    text0 = Text(text=NUMBERBANK[0],color=(0,0,0),position=(408,450),font_size=60,anchor='center')
                    text1 = Text(text=NUMBERBANK[1],color=(0,0,0),position=(477,450),font_size=60,anchor='center')
                    text2 = Text(text=NUMBERBANK[2],color=(0,0,0),position=(546,450),font_size=60,anchor='center')
                    text3 = Text(text=NUMBERBANK[3],color=(0,0,0),position=(615,450),font_size=60,anchor='center')
                    viewportTEXT2 = VisionEgg.Core.Viewport(screen=screen, size=screen.size, stimuli=[text0, text1, text2, text3])
                    viewport.draw()
                    viewportTEXT2.draw()
                    VisionEgg.Core.swap_buffers()
                    if POSITION < 3:
                        ## advance position
                        POSITION=POSITION+1
                elif x >= 479 and x <=546 and y >=180 and y <=245:
                    MOTOR_SPEED_LOG.append(int((round(time() * 1000))-startTIME)-LASTTAP)
                    LASTTAP=int((round(time() * 1000))-startTIME)
                    EXITLIST=[0,0,0]
                    ## button 8
                    NUMBERBANK[POSITION]="8"
                    out_file.write('   button8_at_ms %d NA NA NA 4\n'%(int(round(time() * 1000))-startTIME))
                    screen.clear()
                    text0 = Text(text=NUMBERBANK[0],color=(0,0,0),position=(408,450),font_size=60,anchor='center')
                    text1 = Text(text=NUMBERBANK[1],color=(0,0,0),position=(477,450),font_size=60,anchor='center')
                    text2 = Text(text=NUMBERBANK[2],color=(0,0,0),position=(546,450),font_size=60,anchor='center')
                    text3 = Text(text=NUMBERBANK[3],color=(0,0,0),position=(615,450),font_size=60,anchor='center')
                    viewportTEXT2 = VisionEgg.Core.Viewport(screen=screen, size=screen.size, stimuli=[text0, text1, text2, text3])
                    viewport.draw()
                    viewportTEXT2.draw()
                    VisionEgg.Core.swap_buffers()
                    if POSITION < 3:
                        ## advance position
                        POSITION=POSITION+1

                elif x >= 552 and x <=620 and y >=322 and y <=386:
                    MOTOR_SPEED_LOG.append(int((round(time() * 1000))-startTIME)-LASTTAP)
                    LASTTAP=int((round(time() * 1000))-startTIME)
                    EXITLIST=[0,0,0]
                    ## button 3
                    NUMBERBANK[POSITION]="3"
                    out_file.write('   button3_at_ms %d NA NA NA 4\n'%(int(round(time() * 1000))-startTIME))
                    screen.clear()
                    text0 = Text(text=NUMBERBANK[0],color=(0,0,0),position=(408,450),font_size=60,anchor='center')
                    text1 = Text(text=NUMBERBANK[1],color=(0,0,0),position=(477,450),font_size=60,anchor='center')
                    text2 = Text(text=NUMBERBANK[2],color=(0,0,0),position=(546,450),font_size=60,anchor='center')
                    text3 = Text(text=NUMBERBANK[3],color=(0,0,0),position=(615,450),font_size=60,anchor='center')
                    viewportTEXT2 = VisionEgg.Core.Viewport(screen=screen, size=screen.size, stimuli=[text0, text1, text2, text3])
                    viewport.draw()
                    viewportTEXT2.draw()
                    VisionEgg.Core.swap_buffers()
                    if POSITION < 3:
                        ## advance position
                        POSITION=POSITION+1
                elif x >= 552 and x <=620 and y >=251 and y <=314:
                    MOTOR_SPEED_LOG.append(int((round(time() * 1000))-startTIME)-LASTTAP)
                    LASTTAP=int((round(time() * 1000))-startTIME)
                    EXITLIST=[0,0,0]
                    ## button 6
                    NUMBERBANK[POSITION]="6"
                    out_file.write('   button6_at_ms %d NA NA NA 4\n'%(int(round(time() * 1000))-startTIME))
                    screen.clear()
                    text0 = Text(text=NUMBERBANK[0],color=(0,0,0),position=(408,450),font_size=60,anchor='center')
                    text1 = Text(text=NUMBERBANK[1],color=(0,0,0),position=(477,450),font_size=60,anchor='center')
                    text2 = Text(text=NUMBERBANK[2],color=(0,0,0),position=(546,450),font_size=60,anchor='center')
                    text3 = Text(text=NUMBERBANK[3],color=(0,0,0),position=(615,450),font_size=60,anchor='center')
                    viewportTEXT2 = VisionEgg.Core.Viewport(screen=screen, size=screen.size, stimuli=[text0, text1, text2, text3])
                    viewport.draw()
                    viewportTEXT2.draw()
                    VisionEgg.Core.swap_buffers()
                    if POSITION < 3:
                        ## advance position
                        POSITION=POSITION+1
                elif x >= 552 and x <=620 and y >=180 and y <=245:
                    MOTOR_SPEED_LOG.append(int((round(time() * 1000))-startTIME)-LASTTAP)
                    LASTTAP=int((round(time() * 1000))-startTIME)
                    EXITLIST=[0,0,0]
                    ## button 9
                    NUMBERBANK[POSITION]="9"
                    out_file.write('   button9_at_ms %d NA NA NA 4\n'%(int(round(time() * 1000))-startTIME))
                    screen.clear()
                    text0 = Text(text=NUMBERBANK[0],color=(0,0,0),position=(408,450),font_size=60,anchor='center')
                    text1 = Text(text=NUMBERBANK[1],color=(0,0,0),position=(477,450),font_size=60,anchor='center')
                    text2 = Text(text=NUMBERBANK[2],color=(0,0,0),position=(546,450),font_size=60,anchor='center')
                    text3 = Text(text=NUMBERBANK[3],color=(0,0,0),position=(615,450),font_size=60,anchor='center')
                    viewportTEXT2 = VisionEgg.Core.Viewport(screen=screen, size=screen.size, stimuli=[text0, text1, text2, text3])
                    viewport.draw()
                    viewportTEXT2.draw()
                    VisionEgg.Core.swap_buffers()
                    if POSITION < 3:
                        ## advance position
                        POSITION=POSITION+1
 
                elif x >= 419 and x <=609 and y >=40 and y <=94:
                    MOTOR_SPEED_LOG.append(int((round(time() * 1000))-startTIME)-LASTTAP)
                    LASTTAP=int((round(time() * 1000))-startTIME)
                    EXITLIST=[0,0,0]
                    out_file.write('   buttonDELETE_at_ms %d NA NA NA 4\n'%(int(round(time() * 1000))-startTIME))
                    ## DELETE button
                    ## if POSITION == 0, do nothing. This means there are no numbers
                    ## if POSITION == 1, you just wrote your first number (in POSITION 0) and then shifted over
                    ##  OR, you were in POSITION 2 ready to write there, but instead hit delete, which made you step back
                    ##  a position and wipe the value in NUMBERBANK[1].
                    ##  either way, if POSITION == 1, we want to wipe NUMBERBANK[0] and set POSITION to 0
                    if POSITION > 0:
                        if POSITION == 3 and NUMBERBANK[3] != " ":
                            NUMBERBANK[POSITION]=" "
                        else:
                            POSITION=POSITION-1
                            NUMBERBANK[POSITION]=" "                            
                        screen.clear()
                        text0 = Text(text=NUMBERBANK[0],color=(0,0,0),position=(408,450),font_size=60,anchor='center')
                        text1 = Text(text=NUMBERBANK[1],color=(0,0,0),position=(477,450),font_size=60,anchor='center')
                        text2 = Text(text=NUMBERBANK[2],color=(0,0,0),position=(546,450),font_size=60,anchor='center')
                        text3 = Text(text=NUMBERBANK[3],color=(0,0,0),position=(615,450),font_size=60,anchor='center')
                        viewportTEXT2 = VisionEgg.Core.Viewport(screen=screen, size=screen.size, stimuli=[text0, text1, text2, text3])
                        viewport.draw()
                        viewportTEXT2.draw()
                        VisionEgg.Core.swap_buffers()
                ##
                ## now we see the practical application of the EXITLIST:
                elif x >= 0 and x <=24 and y >= 584 and y <=600:
                   if EXITLIST==[0,0,0]:
                       EXITLIST[0]=1
                       text0 = Text(text="O",color=(0,0,0),position=(0,600),font_size=30,anchor='center')
                       text1 = Text(text="O",color=(0,0,0),position=(0,600),font_size=30,anchor='center')
                       viewportTEXT = VisionEgg.Core.Viewport(screen=screen, size=screen.size, stimuli=[text0, text1])
                       VisionEgg.Core.swap_buffers()
                       screen.clear()
                       viewport.draw()
                       viewportTEXT.draw()
                       viewportTEXT2.draw()
                       VisionEgg.Core.swap_buffers()
                elif x >= 1008 and x <=1024 and y >= 584 and y <=600:
                    if EXITLIST==[1,0,0]:
                       EXITLIST[1]=1
                       text0 = Text(text="O",color=(0,0,0),position=(0,600),font_size=30,anchor='center')
                       text1 = Text(text="O",color=(0,0,0),position=(1024,600),font_size=30,anchor='center')
                       viewportTEXT = VisionEgg.Core.Viewport(screen=screen, size=screen.size, stimuli=[text0, text1])
                       VisionEgg.Core.swap_buffers()
                       screen.clear()
                       viewport.draw()
                       viewportTEXT.draw()
                       viewportTEXT2.draw()
                       VisionEgg.Core.swap_buffers()
                elif x >= 1008 and x <=1024 and y >= 0 and y <=16:
                    if EXITLIST==[1,1,0]:
                        ScreenNumber, RESET = ESCAPEscreenLATE(ScreenNumber, RESET)
###  ###   ###  # #     ### ALWAYS REMEMBER TO UPDATE THE RETURN INFO!  ##   #   #   #####  ##  ###    ### ### 
                        return ScreenNumber, TrialTime, RESPONSE, ERRORS, RESET
                        StartTrial=True


####################################################################################################
####################################################################################################
####################################################################################################
####################################################################################################
####################################################################################################
def MONTHS(ScreenNumber, TrialTime, RESPONSE, ERRORS, RESET):
    x=-1
    y=-1
    #make and show background
    backgroundIMAGE = TextureStimulus(texture=taskbackgrounds[5],position=(0,0))
    viewport = VisionEgg.Core.Viewport(screen=screen, size=screen.size, stimuli=[backgroundIMAGE])
    warnBOX = TextureStimulus(texture=notyetboxes[4],position=(830,150), anchor='center', max_alpha=0.90)
    viewportwarnBOX = VisionEgg.Core.Viewport(screen=screen, size=screen.size, stimuli=[warnBOX])
    useTHISmask=masks[2]
    maskblue = TextureStimulus(texture=useTHISmask,position=(-100,-100), anchor='center', max_alpha=0.50)    
    MASKLIST=[maskblue]
     ## we'll modify the MASKLIST depending on button presses....
    viewportmasks = VisionEgg.Core.Viewport(screen=screen, size=screen.size, stimuli=MASKLIST)
    ##
    EXITLIST=[0,0,0]
    ANSWERED=0
    MonthAnswer=0  # 1 of Jan, 2, for Feb, etc.
    ERRORS=0
    ##
    screen.clear()
    viewport.draw()
    VisionEgg.Core.swap_buffers()
    startTIME=int(round(time() * 1000))
    screen.clear()
    viewport.draw()
    VisionEgg.Core.swap_buffers()
    StartTrial=False
    while not StartTrial:
        for event in pygame.event.get():
            if event.type == pygame.locals.MOUSEBUTTONDOWN:
                if (int(round(time() * 1000))-startTIME) > 100:
                    x,y = pygame.mouse.get_pos()
## pygame.mouse.get_pos() gives coordinates with the LOWER LEFT, not UPPER LEFT (as in visionegg) corner as the origin.
## before we get too complicated, will probably want to flip things around:
                y=600-y
                if x >= 930 and x <=1024 and y >=36 and y <=71:
                    EXITLIST=[0,0,0]
                    ## the "touch here when done" box. Action depends on whether there's a full answer.
                    if ANSWERED == 1 and MonthAnswer > 0:
                        ## trial time is in seconds
                        TrialTime=int(round(time() * 1000))-startTIME
                        RESPONSE=MonthAnswer
                        return ScreenNumber, TrialTime, RESPONSE, ERRORS, RESET
                        StartTrial=True                       
                    else:
                        ERRORS=ERRORS+1
                        screen.clear()
                        viewport.draw()
                        viewportmasks.draw()
                        viewportwarnBOX.draw() #it'll stay up until something else is clicked
                        VisionEgg.Core.swap_buffers()


                elif x >= 225 and x <= 507 and y <= 484 and y >= 428:
                   ## Jan
                    EXITLIST=[0,0,0]
                    if MonthAnswer==1:
                        # if already selected, unselect and move pertinent mask offscreen
                        maskblue = TextureStimulus(texture=useTHISmask,position=(-200,-200), anchor='upperleft', max_alpha=0.50)
                        MASKLIST[0]=maskblue
                        MonthAnswer=0
                        ANSWERED=0
                    else:
                        # otherwise, select and move pertinent mask over the word
                        maskblue = TextureStimulus(texture=useTHISmask,position=(225,484), anchor='upperleft', max_alpha=0.50)
                        MASKLIST[0]=maskblue
                        MonthAnswer=1
                        ANSWERED=1
                    screen.clear()
                    viewport.draw()
                    viewportmasks.draw()
                    VisionEgg.Core.swap_buffers()
                elif x >= 225 and x <= 507 and y <= 418 and y >= 362:
                   ## Feb
                    EXITLIST=[0,0,0]
                    if MonthAnswer==2:
                        # if already selected, unselect and move pertinent mask offscreen
                        maskblue = TextureStimulus(texture=useTHISmask,position=(-200,-200), anchor='upperleft', max_alpha=0.50)
                        MASKLIST[0]=maskblue
                        MonthAnswer=0
                        ANSWERED=0
                    else:
                        # otherwise, select and move pertinent mask over the word
                        maskblue = TextureStimulus(texture=useTHISmask,position=(225,418), anchor='upperleft', max_alpha=0.50)
                        MASKLIST[0]=maskblue
                        MonthAnswer=2
                        ANSWERED=1
                    screen.clear()
                    viewport.draw()
                    viewportmasks.draw()
                    VisionEgg.Core.swap_buffers()
                elif x >= 225 and x <= 507 and y <= 352 and y >= 296:
                   ## Mar
                    EXITLIST=[0,0,0]
                    if MonthAnswer==3:
                        # if already selected, unselect and move pertinent mask offscreen
                        maskblue = TextureStimulus(texture=useTHISmask,position=(-200,-200), anchor='upperleft', max_alpha=0.50)
                        MASKLIST[0]=maskblue
                        MonthAnswer=0
                        ANSWERED=0
                    else:
                        # otherwise, select and move pertinent mask over the word
                        maskblue = TextureStimulus(texture=useTHISmask,position=(225,352), anchor='upperleft', max_alpha=0.50)
                        MASKLIST[0]=maskblue
                        MonthAnswer=3
                        ANSWERED=1
                    screen.clear()
                    viewport.draw()
                    viewportmasks.draw()
                    VisionEgg.Core.swap_buffers()
                elif x >= 225 and x <= 507 and y <= 286 and y >= 230:
                   ## Apr
                    EXITLIST=[0,0,0]
                    if MonthAnswer==4:
                        # if already selected, unselect and move pertinent mask offscreen
                        maskblue = TextureStimulus(texture=useTHISmask,position=(-200,-200), anchor='upperleft', max_alpha=0.50)
                        MASKLIST[0]=maskblue
                        MonthAnswer=0
                        ANSWERED=0
                    else:
                        # otherwise, select and move pertinent mask over the word
                        maskblue = TextureStimulus(texture=useTHISmask,position=(225,286), anchor='upperleft', max_alpha=0.50)
                        MASKLIST[0]=maskblue
                        MonthAnswer=4
                        ANSWERED=1
                    screen.clear()
                    viewport.draw()
                    viewportmasks.draw()
                    VisionEgg.Core.swap_buffers()
                elif x >= 225 and x <= 507 and y <= 220 and y >= 164:
                   ## May
                    EXITLIST=[0,0,0]
                    if MonthAnswer==5:
                        # if already selected, unselect and move pertinent mask offscreen
                        maskblue = TextureStimulus(texture=useTHISmask,position=(-200,-200), anchor='upperleft', max_alpha=0.50)
                        MASKLIST[0]=maskblue
                        MonthAnswer=0
                        ANSWERED=0
                    else:
                        # otherwise, select and move pertinent mask over the word
                        maskblue = TextureStimulus(texture=useTHISmask,position=(225,220), anchor='upperleft', max_alpha=0.50)
                        MASKLIST[0]=maskblue
                        MonthAnswer=5
                        ANSWERED=1
                    screen.clear()
                    viewport.draw()
                    viewportmasks.draw()
                    VisionEgg.Core.swap_buffers()
                elif x >= 225 and x <= 507 and y <= 154 and y >= 98:
                   ## Jun
                    EXITLIST=[0,0,0]
                    if MonthAnswer==6:
                        # if already selected, unselect and move pertinent mask offscreen
                        maskblue = TextureStimulus(texture=useTHISmask,position=(-200,-200), anchor='upperleft', max_alpha=0.50)
                        MASKLIST[0]=maskblue
                        MonthAnswer=0
                        ANSWERED=0
                    else:
                        # otherwise, select and move pertinent mask over the word
                        maskblue = TextureStimulus(texture=useTHISmask,position=(225,154), anchor='upperleft', max_alpha=0.50)
                        MASKLIST[0]=maskblue
                        MonthAnswer=6
                        ANSWERED=1
                    screen.clear()
                    viewport.draw()
                    viewportmasks.draw()
                    VisionEgg.Core.swap_buffers()

                elif x >= 517 and x <= 798 and y <= 484 and y >= 428:
                   ## Jul
                    EXITLIST=[0,0,0]
                    if MonthAnswer==7:
                        # if already selected, unselect and move pertinent mask offscreen
                        maskblue = TextureStimulus(texture=useTHISmask,position=(-200,-200), anchor='upperleft', max_alpha=0.50)
                        MASKLIST[0]=maskblue
                        MonthAnswer=0
                        ANSWERED=0
                    else:
                        # otherwise, select and move pertinent mask over the word
                        maskblue = TextureStimulus(texture=useTHISmask,position=(517,484), anchor='upperleft', max_alpha=0.50)
                        MASKLIST[0]=maskblue
                        MonthAnswer=7
                        ANSWERED=1
                    screen.clear()
                    viewport.draw()
                    viewportmasks.draw()
                    VisionEgg.Core.swap_buffers()
                elif x >= 517 and x <= 798 and y <= 418 and y >= 362:
                   ## Aug
                    EXITLIST=[0,0,0]
                    if MonthAnswer==8:
                        # if already selected, unselect and move pertinent mask offscreen
                        maskblue = TextureStimulus(texture=useTHISmask,position=(-200,-200), anchor='upperleft', max_alpha=0.50)
                        MASKLIST[0]=maskblue
                        MonthAnswer=0
                        ANSWERED=0
                    else:
                        # otherwise, select and move pertinent mask over the word
                        maskblue = TextureStimulus(texture=useTHISmask,position=(517,418), anchor='upperleft', max_alpha=0.50)
                        MASKLIST[0]=maskblue
                        MonthAnswer=8
                        ANSWERED=1
                    screen.clear()
                    viewport.draw()
                    viewportmasks.draw()
                    VisionEgg.Core.swap_buffers()
                elif x >= 517 and x <= 798 and y <= 352 and y >= 296:
                   ## Sept
                    EXITLIST=[0,0,0]
                    if MonthAnswer==9:
                        # if already selected, unselect and move pertinent mask offscreen
                        maskblue = TextureStimulus(texture=useTHISmask,position=(-200,-200), anchor='upperleft', max_alpha=0.50)
                        MASKLIST[0]=maskblue
                        MonthAnswer=0
                        ANSWERED=0
                    else:
                        # otherwise, select and move pertinent mask over the word
                        maskblue = TextureStimulus(texture=useTHISmask,position=(517,352), anchor='upperleft', max_alpha=0.50)
                        MASKLIST[0]=maskblue
                        MonthAnswer=9
                        ANSWERED=1
                    screen.clear()
                    viewport.draw()
                    viewportmasks.draw()
                    VisionEgg.Core.swap_buffers()
                elif x >= 517 and x <= 798 and y <= 286 and y >= 230:
                   ## Oct
                    EXITLIST=[0,0,0]
                    if MonthAnswer==10:
                        # if already selected, unselect and move pertinent mask offscreen
                        maskblue = TextureStimulus(texture=useTHISmask,position=(-200,-200), anchor='upperleft', max_alpha=0.50)
                        MASKLIST[0]=maskblue
                        MonthAnswer=0
                        ANSWERED=0
                    else:
                        # otherwise, select and move pertinent mask over the word
                        maskblue = TextureStimulus(texture=useTHISmask,position=(517,286), anchor='upperleft', max_alpha=0.50)
                        MASKLIST[0]=maskblue
                        MonthAnswer=10
                        ANSWERED=1
                    screen.clear()
                    viewport.draw()
                    viewportmasks.draw()
                    VisionEgg.Core.swap_buffers()
                elif x >= 517 and x <= 798 and y <= 220 and y >= 164:
                   ## Nov
                    EXITLIST=[0,0,0]
                    if MonthAnswer==11:
                        # if already selected, unselect and move pertinent mask offscreen
                        maskblue = TextureStimulus(texture=useTHISmask,position=(-200,-200), anchor='upperleft', max_alpha=0.50)
                        MASKLIST[0]=maskblue
                        MonthAnswer=0
                        ANSWERED=0
                    else:
                        # otherwise, select and move pertinent mask over the word
                        maskblue = TextureStimulus(texture=useTHISmask,position=(517,220), anchor='upperleft', max_alpha=0.50)
                        MASKLIST[0]=maskblue
                        MonthAnswer=11
                        ANSWERED=1
                    screen.clear()
                    viewport.draw()
                    viewportmasks.draw()
                    VisionEgg.Core.swap_buffers()
                elif x >= 517 and x <= 798 and y <= 154 and y >= 98:
                   ## Dec
                    EXITLIST=[0,0,0]
                    if MonthAnswer==12:
                        # if already selected, unselect and move pertinent mask offscreen
                        maskblue = TextureStimulus(texture=useTHISmask,position=(-200,-200), anchor='upperleft', max_alpha=0.50)
                        MASKLIST[0]=maskblue
                        MonthAnswer=0
                        ANSWERED=0
                    else:
                        # otherwise, select and move pertinent mask over the word
                        maskblue = TextureStimulus(texture=useTHISmask,position=(517,154), anchor='upperleft', max_alpha=0.50)
                        MASKLIST[0]=maskblue
                        MonthAnswer=12
                        ANSWERED=1
                    screen.clear()
                    viewport.draw()
                    viewportmasks.draw()
                    VisionEgg.Core.swap_buffers()                        
                ##
                ## now we see the practical application of the EXITLIST:
                elif x >= 0 and x <=24 and y >= 584 and y <=600:
                   if EXITLIST==[0,0,0]:
                       EXITLIST[0]=1
                       text0 = Text(text="O",color=(0,0,0),position=(0,600),font_size=30,anchor='center')
                       text1 = Text(text="O",color=(0,0,0),position=(0,600),font_size=30,anchor='center')
                       viewportTEXT = VisionEgg.Core.Viewport(screen=screen, size=screen.size, stimuli=[text0, text1])
                       VisionEgg.Core.swap_buffers()
                       screen.clear()
                       viewport.draw()
                       viewportmasks.draw()
                       viewportTEXT.draw()
                       VisionEgg.Core.swap_buffers()
                elif x >= 1008 and x <=1024 and y >= 584 and y <=600:
                    if EXITLIST==[1,0,0]:
                       EXITLIST[1]=1
                       text0 = Text(text="O",color=(0,0,0),position=(0,600),font_size=30,anchor='center')
                       text1 = Text(text="O",color=(0,0,0),position=(1024,600),font_size=30,anchor='center')
                       viewportTEXT = VisionEgg.Core.Viewport(screen=screen, size=screen.size, stimuli=[text0, text1])
                       VisionEgg.Core.swap_buffers()
                       screen.clear()
                       viewport.draw()
                       viewportmasks.draw()
                       viewportTEXT.draw()
                       VisionEgg.Core.swap_buffers()
                elif x >= 1008 and x <=1024 and y >= 0 and y <=16:
                    if EXITLIST==[1,1,0]:
                        ScreenNumber, RESET = ESCAPEscreenLATE(ScreenNumber, RESET)
###  ###   ###  # #     ### ALWAYS REMEMBER TO UPDATE THE RETURN INFO!  ##   #   #   #####  ##  ###    ### ### 
                        return ScreenNumber, TrialTime, RESPONSE, ERRORS, RESET
                        StartTrial=True


####################################################################################################
####################################################################################################
####################################################################################################
####################################################################################################
####################################################################################################
def DAYofWEEK(ScreenNumber, TrialTime, RESPONSE, ERRORS, RESET):
    x=-1
    y=-1
    #make and show background
    backgroundIMAGE = TextureStimulus(texture=taskbackgrounds[6],position=(0,0))
    viewport = VisionEgg.Core.Viewport(screen=screen, size=screen.size, stimuli=[backgroundIMAGE])
    warnBOX = TextureStimulus(texture=notyetboxes[5],position=(830,150), anchor='center', max_alpha=0.80)
    viewportwarnBOX = VisionEgg.Core.Viewport(screen=screen, size=screen.size, stimuli=[warnBOX])
    useTHISmask=masks[3]
    maskblue = TextureStimulus(texture=useTHISmask,position=(-100,-100), anchor='center', max_alpha=0.50)    
    MASKLIST=[maskblue]
     ## we'll modify the MASKLIST depending on button presses....
    viewportmasks = VisionEgg.Core.Viewport(screen=screen, size=screen.size, stimuli=MASKLIST)
    ##
    EXITLIST=[0,0,0]
    ANSWERED=0
    DayAnswer=0  # 1 is Sun, 2 is Mon, and so on.
    ERRORS=0
    ##
    screen.clear()
    viewport.draw()
    VisionEgg.Core.swap_buffers()
    startTIME=int(round(time() * 1000))
    screen.clear()
    viewport.draw()
    VisionEgg.Core.swap_buffers()
    StartTrial=False
    while not StartTrial:
        for event in pygame.event.get():
            if event.type == pygame.locals.MOUSEBUTTONDOWN:
                if (int(round(time() * 1000))-startTIME) > 100:
                    x,y = pygame.mouse.get_pos()
## pygame.mouse.get_pos() gives coordinates with the LOWER LEFT, not UPPER LEFT (as in visionegg) corner as the origin.
## before we get too complicated, will probably want to flip things around:
                y=600-y
                if x >= 930 and x <= 1024 and y >= 34 and y <=71 :
                    EXITLIST=[0,0,0]
                    ## the "touch here when done" box. Action depends on whether there's a full answer.
                    if ANSWERED == 1 and DayAnswer > 0:
                        ## trial time is in seconds
                        RESPONSE=DayAnswer
                        TrialTime=int(round(time() * 1000))-startTIME
                        return ScreenNumber, TrialTime, RESPONSE, ERRORS, RESET
                        StartTrial=True                       
                    else:
                        ERRORS=ERRORS+1
                        screen.clear()
                        viewport.draw()
                        viewportmasks.draw()
                        viewportwarnBOX.draw() #it'll stay up until something else is clicked
                        VisionEgg.Core.swap_buffers()

                elif x >= 372 and x <= 652 and y <= 484 and y >= 428:
                   ## Sun
                    EXITLIST=[0,0,0]
                    if DayAnswer==1:
                        # if already selected, unselect and move pertinent mask offscreen
                        maskblue = TextureStimulus(texture=useTHISmask,position=(-200,-200), anchor='upperleft', max_alpha=0.50)
                        MASKLIST[0]=maskblue
                        DayAnswer=0
                        ANSWERED=0
                    else:
                        # otherwise, select and move pertinent mask over the word
                        maskblue = TextureStimulus(texture=useTHISmask,position=(372,484), anchor='upperleft', max_alpha=0.50)
                        MASKLIST[0]=maskblue
                        DayAnswer=1
                        ANSWERED=1
                    screen.clear()
                    viewport.draw()
                    viewportmasks.draw()
                    VisionEgg.Core.swap_buffers()
                elif x >= 372 and x <= 652 and y <= 418 and y >= 362:
                   ## Mon
                    EXITLIST=[0,0,0]
                    if DayAnswer==2:
                        # if already selected, unselect and move pertinent mask offscreen
                        maskblue = TextureStimulus(texture=useTHISmask,position=(-200,-200), anchor='upperleft', max_alpha=0.50)
                        MASKLIST[0]=maskblue
                        DayAnswer=0
                        ANSWERED=0
                    else:
                        # otherwise, select and move pertinent mask over the word
                        maskblue = TextureStimulus(texture=useTHISmask,position=(372,418), anchor='upperleft', max_alpha=0.50)
                        MASKLIST[0]=maskblue
                        DayAnswer=2
                        ANSWERED=1
                    screen.clear()
                    viewport.draw()
                    viewportmasks.draw()
                    VisionEgg.Core.swap_buffers()
                elif x >= 372 and x <= 652 and y <= 352 and y >= 296:
                   ## Tues
                    EXITLIST=[0,0,0]
                    if DayAnswer==3:
                        # if already selected, unselect and move pertinent mask offscreen
                        maskblue = TextureStimulus(texture=useTHISmask,position=(-200,-200), anchor='upperleft', max_alpha=0.50)
                        MASKLIST[0]=maskblue
                        DayAnswer=0
                        ANSWERED=0
                    else:
                        # otherwise, select and move pertinent mask over the word
                        maskblue = TextureStimulus(texture=useTHISmask,position=(372,352), anchor='upperleft', max_alpha=0.50)
                        MASKLIST[0]=maskblue
                        DayAnswer=3
                        ANSWERED=1
                    screen.clear()
                    viewport.draw()
                    viewportmasks.draw()
                    VisionEgg.Core.swap_buffers()
                elif x >= 372 and x <= 652 and y <= 286 and y >= 230:
                   ## Wed
                    EXITLIST=[0,0,0]
                    if DayAnswer==4:
                        # if already selected, unselect and move pertinent mask offscreen
                        maskblue = TextureStimulus(texture=useTHISmask,position=(-200,-200), anchor='upperleft', max_alpha=0.50)
                        MASKLIST[0]=maskblue
                        DayAnswer=0
                        ANSWERED=0
                    else:
                        # otherwise, select and move pertinent mask over the word
                        maskblue = TextureStimulus(texture=useTHISmask,position=(372,286), anchor='upperleft', max_alpha=0.50)
                        MASKLIST[0]=maskblue
                        DayAnswer=4
                        ANSWERED=1
                    screen.clear()
                    viewport.draw()
                    viewportmasks.draw()
                    VisionEgg.Core.swap_buffers()
                elif x >= 372 and x <= 652 and y <= 220 and y >= 164:
                   ## Thurs
                    EXITLIST=[0,0,0]
                    if DayAnswer==5:
                        # if already selected, unselect and move pertinent mask offscreen
                        maskblue = TextureStimulus(texture=useTHISmask,position=(-200,-200), anchor='upperleft', max_alpha=0.50)
                        MASKLIST[0]=maskblue
                        DayAnswer=0
                        ANSWERED=0
                    else:
                        # otherwise, select and move pertinent mask over the word
                        maskblue = TextureStimulus(texture=useTHISmask,position=(372,220), anchor='upperleft', max_alpha=0.50)
                        MASKLIST[0]=maskblue
                        DayAnswer=5
                        ANSWERED=1
                    screen.clear()
                    viewport.draw()
                    viewportmasks.draw()
                    VisionEgg.Core.swap_buffers()
                elif x >= 372 and x <= 652 and y <= 154 and y >= 98:
                   ## Fri
                    EXITLIST=[0,0,0]
                    if DayAnswer==6:
                        # if already selected, unselect and move pertinent mask offscreen
                        maskblue = TextureStimulus(texture=useTHISmask,position=(-200,-200), anchor='upperleft', max_alpha=0.50)
                        MASKLIST[0]=maskblue
                        DayAnswer=0
                        ANSWERED=0
                    else:
                        # otherwise, select and move pertinent mask over the word
                        maskblue = TextureStimulus(texture=useTHISmask,position=(372,154), anchor='upperleft', max_alpha=0.50)
                        MASKLIST[0]=maskblue
                        DayAnswer=6
                        ANSWERED=1
                    screen.clear()
                    viewport.draw()
                    viewportmasks.draw()
                    VisionEgg.Core.swap_buffers()
                elif x >= 372 and x <= 652 and y <= 88 and y >= 32:
                   ## Sat
                    EXITLIST=[0,0,0]
                    if DayAnswer==7:
                        # if already selected, unselect and move pertinent mask offscreen
                        maskblue = TextureStimulus(texture=useTHISmask,position=(-200,-200), anchor='upperleft', max_alpha=0.50)
                        MASKLIST[0]=maskblue
                        DayAnswer=0
                        ANSWERED=0
                    else:
                        # otherwise, select and move pertinent mask over the word
                        maskblue = TextureStimulus(texture=useTHISmask,position=(372,88), anchor='upperleft', max_alpha=0.50)
                        MASKLIST[0]=maskblue
                        DayAnswer=7
                        ANSWERED=1
                    screen.clear()
                    viewport.draw()
                    viewportmasks.draw()
                    VisionEgg.Core.swap_buffers()

                  
                ##
                ## now we see the practical application of the EXITLIST:
                elif x >= 0 and x <=24 and y >= 584 and y <=600:
                   if EXITLIST==[0,0,0]:
                       EXITLIST[0]=1
                       text0 = Text(text="O",color=(0,0,0),position=(0,600),font_size=30,anchor='center')
                       text1 = Text(text="O",color=(0,0,0),position=(0,600),font_size=30,anchor='center')
                       viewportTEXT = VisionEgg.Core.Viewport(screen=screen, size=screen.size, stimuli=[text0, text1])
                       VisionEgg.Core.swap_buffers()
                       screen.clear()
                       viewport.draw()
                       viewportmasks.draw()
                       viewportTEXT.draw()
                       VisionEgg.Core.swap_buffers()
                elif x >= 1008 and x <=1024 and y >= 584 and y <=600:
                    if EXITLIST==[1,0,0]:
                       EXITLIST[1]=1
                       text0 = Text(text="O",color=(0,0,0),position=(0,600),font_size=30,anchor='center')
                       text1 = Text(text="O",color=(0,0,0),position=(1024,600),font_size=30,anchor='center')
                       viewportTEXT = VisionEgg.Core.Viewport(screen=screen, size=screen.size, stimuli=[text0, text1])
                       VisionEgg.Core.swap_buffers()
                       screen.clear()
                       viewport.draw()
                       viewportmasks.draw()
                       viewportTEXT.draw()
                       VisionEgg.Core.swap_buffers()
                elif x >= 1008 and x <=1024 and y >= 0 and y <=16:
                    if EXITLIST==[1,1,0]:
                        ScreenNumber, RESET = ESCAPEscreenLATE(ScreenNumber, RESET)
###  ###   ###  # #     ### ALWAYS REMEMBER TO UPDATE THE RETURN INFO!  ##   #   #   #####  ##  ###    ### ### 
                        return ScreenNumber, TrialTime, RESPONSE, ERRORS, RESET
                        StartTrial=True


####################################################################################################
####################################################################################################
####################################################################################################
####################################################################################################
####################################################################################################
def STATE(ScreenNumber, TrialTime, RESPONSE, ERRORS, RESET):
    x=-1
    y=-1
    #make and show background
    backgroundIMAGE = TextureStimulus(texture=taskbackgrounds[7],position=(0,0))
    viewport = VisionEgg.Core.Viewport(screen=screen, size=screen.size, stimuli=[backgroundIMAGE])
    warnBOX = TextureStimulus(texture=notyetboxes[7],position=(830,150), anchor='center', max_alpha=0.90)
    viewportwarnBOX = VisionEgg.Core.Viewport(screen=screen, size=screen.size, stimuli=[warnBOX])
    useTHISmask=masks[4]
    maskblue = TextureStimulus(texture=useTHISmask,position=(-100,-100), anchor='center', max_alpha=0.50)    
    MASKLIST=[maskblue]
     ## we'll modify the MASKLIST depending on button presses....
    viewportmasks = VisionEgg.Core.Viewport(screen=screen, size=screen.size, stimuli=MASKLIST)
    ##
    EXITLIST=[0,0,0]
    ANSWERED=0
    RESPONSE=" "
    ERRORS=0
    ##
    CURRENTLIST=list_states
##    t101 = Text(text=CURRENTLIST[0],color=(0,0,0),position=(56,541),font_size=42,anchor='upperleft')
##    t102 = Text(text=CURRENTLIST[1],color=(0,0,0),position=(56,511),font_size=42,anchor='upperleft')
##    t103 = Text(text=CURRENTLIST[2],color=(0,0,0),position=(56,481),font_size=42,anchor='upperleft')
##    t104 = Text(text=CURRENTLIST[3],color=(0,0,0),position=(56,451),font_size=42,anchor='upperleft')
##    t105 = Text(text=CURRENTLIST[4],color=(0,0,0),position=(56,421),font_size=42,anchor='upperleft')
##    t106 = Text(text=CURRENTLIST[5],color=(0,0,0),position=(56,391),font_size=42,anchor='upperleft')
##    t107 = Text(text=CURRENTLIST[6],color=(0,0,0),position=(56,361),font_size=42,anchor='upperleft')
##    t108 = Text(text=CURRENTLIST[7],color=(0,0,0),position=(56,331),font_size=42,anchor='upperleft')
##    t109 = Text(text=CURRENTLIST[8],color=(0,0,0),position=(56,301),font_size=42,anchor='upperleft')
##    t110 = Text(text=CURRENTLIST[9],color=(0,0,0),position=(56,270),font_size=42,anchor='upperleft')
##    t111 = Text(text=CURRENTLIST[10],color=(0,0,0),position=(56,241),font_size=42,anchor='upperleft')
##    t112 = Text(text=CURRENTLIST[11],color=(0,0,0),position=(56,211),font_size=42,anchor='upperleft')
##    t113 = Text(text=CURRENTLIST[12],color=(0,0,0),position=(56,181),font_size=42,anchor='upperleft')
##    t114 = Text(text=CURRENTLIST[13],color=(0,0,0),position=(56,151),font_size=42,anchor='upperleft')
##    t115 = Text(text=CURRENTLIST[14],color=(0,0,0),position=(56,121),font_size=42,anchor='upperleft')
##    t116 = Text(text=CURRENTLIST[15],color=(0,0,0),position=(56,91),font_size=42,anchor='upperleft')
##    t117 = Text(text=CURRENTLIST[16],color=(0,0,0),position=(56,61),font_size=42,anchor='upperleft')
##    t118 = Text(text=CURRENTLIST[17],color=(0,0,0),position=(56,31),font_size=42,anchor='upperleft')
##    #
##    t201 = Text(text=CURRENTLIST[18],color=(0,0,0),position=(367,541),font_size=42,anchor='upperleft')
##    t202 = Text(text=CURRENTLIST[19],color=(0,0,0),position=(367,511),font_size=42,anchor='upperleft')
##    t203 = Text(text=CURRENTLIST[20],color=(0,0,0),position=(367,481),font_size=42,anchor='upperleft')
##    t204 = Text(text=CURRENTLIST[21],color=(0,0,0),position=(367,451),font_size=42,anchor='upperleft')
##    t205 = Text(text=CURRENTLIST[22],color=(0,0,0),position=(367,421),font_size=42,anchor='upperleft')
##    t206 = Text(text=CURRENTLIST[23],color=(0,0,0),position=(367,391),font_size=42,anchor='upperleft')
##    t207 = Text(text=CURRENTLIST[24],color=(0,0,0),position=(367,361),font_size=42,anchor='upperleft')
##    t208 = Text(text=CURRENTLIST[25],color=(0,0,0),position=(367,331),font_size=42,anchor='upperleft')
##    t209 = Text(text=CURRENTLIST[26],color=(0,0,0),position=(367,301),font_size=42,anchor='upperleft')
##    t210 = Text(text=CURRENTLIST[27],color=(0,0,0),position=(367,270),font_size=42,anchor='upperleft')
##    t211 = Text(text=CURRENTLIST[28],color=(0,0,0),position=(367,241),font_size=42,anchor='upperleft')
##    t212 = Text(text=CURRENTLIST[29],color=(0,0,0),position=(367,211),font_size=42,anchor='upperleft')
##    t213 = Text(text=CURRENTLIST[30],color=(0,0,0),position=(367,181),font_size=42,anchor='upperleft')
##    t214 = Text(text=CURRENTLIST[31],color=(0,0,0),position=(367,151),font_size=42,anchor='upperleft')
##    t215 = Text(text=CURRENTLIST[32],color=(0,0,0),position=(367,121),font_size=42,anchor='upperleft')
##    t216 = Text(text=CURRENTLIST[33],color=(0,0,0),position=(367,91),font_size=42,anchor='upperleft')
##    t217 = Text(text=CURRENTLIST[34],color=(0,0,0),position=(367,61),font_size=42,anchor='upperleft')
##    t218 = Text(text=CURRENTLIST[35],color=(0,0,0),position=(367,31),font_size=42,anchor='upperleft')
##    #
##    t301 = Text(text=CURRENTLIST[36],color=(0,0,0),position=(679,541),font_size=42,anchor='upperleft')
##    t302 = Text(text=CURRENTLIST[37],color=(0,0,0),position=(679,511),font_size=42,anchor='upperleft')
##    t303 = Text(text=CURRENTLIST[38],color=(0,0,0),position=(679,481),font_size=42,anchor='upperleft')
##    t304 = Text(text=CURRENTLIST[39],color=(0,0,0),position=(679,451),font_size=42,anchor='upperleft')
##    t305 = Text(text=CURRENTLIST[40],color=(0,0,0),position=(679,421),font_size=42,anchor='upperleft')
##    t306 = Text(text=CURRENTLIST[41],color=(0,0,0),position=(679,391),font_size=42,anchor='upperleft')
##    t307 = Text(text=CURRENTLIST[42],color=(0,0,0),position=(679,361),font_size=42,anchor='upperleft')
##    t308 = Text(text=CURRENTLIST[43],color=(0,0,0),position=(679,331),font_size=42,anchor='upperleft')
##    t309 = Text(text=CURRENTLIST[44],color=(0,0,0),position=(679,301),font_size=42,anchor='upperleft')
##    t310 = Text(text=CURRENTLIST[45],color=(0,0,0),position=(679,270),font_size=42,anchor='upperleft')
##    t311 = Text(text=CURRENTLIST[46],color=(0,0,0),position=(679,241),font_size=42,anchor='upperleft')
##    t312 = Text(text=CURRENTLIST[47],color=(0,0,0),position=(679,211),font_size=42,anchor='upperleft')
##    t313 = Text(text=CURRENTLIST[48],color=(0,0,0),position=(679,181),font_size=42,anchor='upperleft')
##    t314 = Text(text=CURRENTLIST[49],color=(0,0,0),position=(679,151),font_size=42,anchor='upperleft')
##    viewportTEXT2 = VisionEgg.Core.Viewport(screen=screen, size=screen.size, stimuli=[t101,t102,t103,t104,t105,t106,t107,t108,
##                                                                                     t109,t110,t111,t112,t113,t114,t115,t116,
##                                                                                     t117,t118,
##                                                                                     t201,t202,t203,t204,t205,t206,t207,t208,
##                                                                                     t209,t210,t211,t212,t213,t214,t215,t216,
##                                                                                     t217,t218,
##                                                                                     t301,t302,t303,t304,t305,t306,t307,t308,
##                                                                                     t309,t310,t311,t312,t313,t314])
    viewportTEXT2=PREMADE_VIEWPORT_STATES
    screen.clear()
    viewport.draw()
    viewportTEXT2.draw()
    VisionEgg.Core.swap_buffers()
    startTIME=int(round(time() * 1000))
    screen.clear()
    viewport.draw()
    viewportTEXT2.draw()
    viewportmasks.draw()
    VisionEgg.Core.swap_buffers()
    StartTrial=False
    while not StartTrial:
        for event in pygame.event.get():
            if event.type == pygame.locals.MOUSEBUTTONDOWN:
                if (int(round(time() * 1000))-startTIME) > 100:
                    x,y = pygame.mouse.get_pos()
## pygame.mouse.get_pos() gives coordinates with the LOWER LEFT, not UPPER LEFT (as in visionegg) corner as the origin.
## before we get too complicated, will probably want to flip things around:
                y=600-y
                if x >= 903 and x <=996 and y >=0 and y <=37:
                    EXITLIST=[0,0,0]
                    ## the "touch here when done" box. Action depends on whether there's a full answer.
                    if ANSWERED == 1 and not RESPONSE == " ":
                        ## trial time is in seconds
                        TrialTime=int(round(time() * 1000))-startTIME
                        return ScreenNumber, TrialTime, RESPONSE, ERRORS, RESET
                        StartTrial=True                       
                    else:
                        ERRORS=ERRORS+1
                        screen.clear()
                        viewport.draw()
                        viewportTEXT2.draw()
                        viewportmasks.draw()
                        viewportwarnBOX.draw() #it'll stay up until something else is clicked
                        VisionEgg.Core.swap_buffers()

                elif x >= 53 and x <= 349 and y <= 544 and y >= 515:
                     ##   col1_row__1
                    EXITLIST=[0,0,0]
                    if RESPONSE==CURRENTLIST[0]:
                        # if already selected, unselect and move pertinent mask offscreen
                        maskblue = TextureStimulus(texture=useTHISmask,position=(-200,-200), anchor='upperleft', max_alpha=0.50)
                        MASKLIST[0]=maskblue
                        RESPONSE=" "
                        ANSWERED=0
                    else:
                        # otherwise, select and move pertinent mask over the word
                        maskblue = TextureStimulus(texture=useTHISmask,position=(54,543), anchor='upperleft', max_alpha=0.50)
                        MASKLIST[0]=maskblue
                        RESPONSE=CURRENTLIST[0]
                        ANSWERED=1
                    screen.clear()
                    viewport.draw()
                    viewportTEXT2.draw()
                    viewportmasks.draw()
                    VisionEgg.Core.swap_buffers()

                elif x >= 53 and x <= 349 and y <= 514 and y >= 485:
                     ##   col1_row2
                    EXITLIST=[0,0,0]
                    if RESPONSE==CURRENTLIST[1]:
                        # if already selected, unselect and move pertinent mask offscreen
                        maskblue = TextureStimulus(texture=useTHISmask,position=(-200,-200), anchor='upperleft', max_alpha=0.50)
                        MASKLIST[0]=maskblue
                        RESPONSE=" "
                        ANSWERED=0
                    else:
                        # otherwise, select and move pertinent mask over the word
                        maskblue = TextureStimulus(texture=useTHISmask,position=(54,513), anchor='upperleft', max_alpha=0.50)
                        MASKLIST[0]=maskblue
                        RESPONSE=CURRENTLIST[1]
                        ANSWERED=1
                    screen.clear()
                    viewport.draw()
                    viewportTEXT2.draw()
                    viewportmasks.draw()
                    VisionEgg.Core.swap_buffers()
                    
                elif x >= 53 and x <= 349 and y <= 484 and y >= 455:
                     ##   col1_row3
                    EXITLIST=[0,0,0]
                    if RESPONSE==CURRENTLIST[2]:
                        # if already selected, unselect and move pertinent mask offscreen
                        maskblue = TextureStimulus(texture=useTHISmask,position=(-200,-200), anchor='upperleft', max_alpha=0.50)
                        MASKLIST[0]=maskblue
                        RESPONSE=" "
                        ANSWERED=0
                    else:
                        # otherwise, select and move pertinent mask over the word
                        maskblue = TextureStimulus(texture=useTHISmask,position=(54,483), anchor='upperleft', max_alpha=0.50)
                        MASKLIST[0]=maskblue
                        RESPONSE=CURRENTLIST[2]
                        ANSWERED=1
                    screen.clear()
                    viewport.draw()
                    viewportTEXT2.draw()
                    viewportmasks.draw()
                    VisionEgg.Core.swap_buffers()
                    
                elif x >= 53 and x <= 349 and y <= 454 and y >= 425:
                     ##   col1_row4
                    EXITLIST=[0,0,0]
                    if RESPONSE==CURRENTLIST[3]:
                        # if already selected, unselect and move pertinent mask offscreen
                        maskblue = TextureStimulus(texture=useTHISmask,position=(-200,-200), anchor='upperleft', max_alpha=0.50)
                        MASKLIST[0]=maskblue
                        RESPONSE=" "
                        ANSWERED=0
                    else:
                        # otherwise, select and move pertinent mask over the word
                        maskblue = TextureStimulus(texture=useTHISmask,position=(54,453), anchor='upperleft', max_alpha=0.50)
                        MASKLIST[0]=maskblue
                        RESPONSE=CURRENTLIST[3]
                        ANSWERED=1
                    screen.clear()
                    viewport.draw()
                    viewportTEXT2.draw()
                    viewportmasks.draw()
                    VisionEgg.Core.swap_buffers()
                    
                elif x >= 53 and x <= 349 and y <= 424 and y >= 395:
                     ##   col1_row5
                    EXITLIST=[0,0,0]
                    if RESPONSE==CURRENTLIST[4]:
                        # if already selected, unselect and move pertinent mask offscreen
                        maskblue = TextureStimulus(texture=useTHISmask,position=(-200,-200), anchor='upperleft', max_alpha=0.50)
                        MASKLIST[0]=maskblue
                        RESPONSE=" "
                        ANSWERED=0
                    else:
                        # otherwise, select and move pertinent mask over the word
                        maskblue = TextureStimulus(texture=useTHISmask,position=(54,423), anchor='upperleft', max_alpha=0.50)
                        MASKLIST[0]=maskblue
                        RESPONSE=CURRENTLIST[4]
                        ANSWERED=1
                    screen.clear()
                    viewport.draw()
                    viewportTEXT2.draw()
                    viewportmasks.draw()
                    VisionEgg.Core.swap_buffers()
                    
                elif x >= 53 and x <= 349 and y <= 394 and y >= 365:
                     ##   col1_row6
                    EXITLIST=[0,0,0]
                    if RESPONSE==CURRENTLIST[5]:
                        # if already selected, unselect and move pertinent mask offscreen
                        maskblue = TextureStimulus(texture=useTHISmask,position=(-200,-200), anchor='upperleft', max_alpha=0.50)
                        MASKLIST[0]=maskblue
                        RESPONSE=" "
                        ANSWERED=0
                    else:
                        # otherwise, select and move pertinent mask over the word
                        maskblue = TextureStimulus(texture=useTHISmask,position=(54,393), anchor='upperleft', max_alpha=0.50)
                        MASKLIST[0]=maskblue
                        RESPONSE=CURRENTLIST[5]
                        ANSWERED=1
                    screen.clear()
                    viewport.draw()
                    viewportTEXT2.draw()
                    viewportmasks.draw()
                    VisionEgg.Core.swap_buffers()
                    
                elif x >= 53 and x <= 349 and y <= 364 and y >= 335:
                     ##   col1_row7
                    EXITLIST=[0,0,0]
                    if RESPONSE==CURRENTLIST[6]:
                        # if already selected, unselect and move pertinent mask offscreen
                        maskblue = TextureStimulus(texture=useTHISmask,position=(-200,-200), anchor='upperleft', max_alpha=0.50)
                        MASKLIST[0]=maskblue
                        RESPONSE=" "
                        ANSWERED=0
                    else:
                        # otherwise, select and move pertinent mask over the word
                        maskblue = TextureStimulus(texture=useTHISmask,position=(54,363), anchor='upperleft', max_alpha=0.50)
                        MASKLIST[0]=maskblue
                        RESPONSE=CURRENTLIST[6]
                        ANSWERED=1
                    screen.clear()
                    viewport.draw()
                    viewportTEXT2.draw()
                    viewportmasks.draw()
                    VisionEgg.Core.swap_buffers()
                    
                elif x >= 53 and x <= 349 and y <= 334 and y >= 305:
                     ##   col1_row8
                    EXITLIST=[0,0,0]
                    if RESPONSE==CURRENTLIST[7]:
                        # if already selected, unselect and move pertinent mask offscreen
                        maskblue = TextureStimulus(texture=useTHISmask,position=(-200,-200), anchor='upperleft', max_alpha=0.50)
                        MASKLIST[0]=maskblue
                        RESPONSE=" "
                        ANSWERED=0
                    else:
                        # otherwise, select and move pertinent mask over the word
                        maskblue = TextureStimulus(texture=useTHISmask,position=(54,333), anchor='upperleft', max_alpha=0.50)
                        MASKLIST[0]=maskblue
                        RESPONSE=CURRENTLIST[7]
                        ANSWERED=1
                    screen.clear()
                    viewport.draw()
                    viewportTEXT2.draw()
                    viewportmasks.draw()
                    VisionEgg.Core.swap_buffers()
                    
                elif x >= 53 and x <= 349 and y <= 304 and y >= 275:
                     ##   col1_row9
                    EXITLIST=[0,0,0]
                    if RESPONSE==CURRENTLIST[9]:
                        # if already selected, unselect and move pertinent mask offscreen
                        maskblue = TextureStimulus(texture=useTHISmask,position=(-200,-200), anchor='upperleft', max_alpha=0.50)
                        MASKLIST[0]=maskblue
                        RESPONSE=" "
                        ANSWERED=0
                    else:
                        # otherwise, select and move pertinent mask over the word
                        maskblue = TextureStimulus(texture=useTHISmask,position=(54,303), anchor='upperleft', max_alpha=0.50)
                        MASKLIST[0]=maskblue
                        RESPONSE=CURRENTLIST[9]
                        ANSWERED=1
                    screen.clear()
                    viewport.draw()
                    viewportTEXT2.draw()
                    viewportmasks.draw()
                    VisionEgg.Core.swap_buffers()
                    
                elif x >= 53 and x <= 349 and y <= 274 and y >= 245:
                     ##   col1_row10
                    EXITLIST=[0,0,0]
                    if RESPONSE==CURRENTLIST[9]:
                        # if already selected, unselect and move pertinent mask offscreen
                        maskblue = TextureStimulus(texture=useTHISmask,position=(-200,-200), anchor='upperleft', max_alpha=0.50)
                        MASKLIST[0]=maskblue
                        RESPONSE=" "
                        ANSWERED=0
                    else:
                        # otherwise, select and move pertinent mask over the word
                        maskblue = TextureStimulus(texture=useTHISmask,position=(54,273), anchor='upperleft', max_alpha=0.50)
                        MASKLIST[0]=maskblue
                        RESPONSE=CURRENTLIST[9]
                        ANSWERED=1
                    screen.clear()
                    viewport.draw()
                    viewportTEXT2.draw()
                    viewportmasks.draw()
                    VisionEgg.Core.swap_buffers()
                    
                elif x >= 53 and x <= 349 and y <= 244 and y >= 215:
                     ##   col1_row11
                    EXITLIST=[0,0,0]
                    if RESPONSE==CURRENTLIST[10]:
                        # if already selected, unselect and move pertinent mask offscreen
                        maskblue = TextureStimulus(texture=useTHISmask,position=(-200,-200), anchor='upperleft', max_alpha=0.50)
                        MASKLIST[0]=maskblue
                        RESPONSE=" "
                        ANSWERED=0
                    else:
                        # otherwise, select and move pertinent mask over the word
                        maskblue = TextureStimulus(texture=useTHISmask,position=(54,243), anchor='upperleft', max_alpha=0.50)
                        MASKLIST[0]=maskblue
                        RESPONSE=CURRENTLIST[10]
                        ANSWERED=1
                    screen.clear()
                    viewport.draw()
                    viewportTEXT2.draw()
                    viewportmasks.draw()
                    VisionEgg.Core.swap_buffers()
                    
                elif x >= 53 and x <= 349 and y <= 214 and y >= 185:
                     ##   col1_row12
                    EXITLIST=[0,0,0]
                    if RESPONSE==CURRENTLIST[11]:
                        # if already selected, unselect and move pertinent mask offscreen
                        maskblue = TextureStimulus(texture=useTHISmask,position=(-200,-200), anchor='upperleft', max_alpha=0.50)
                        MASKLIST[0]=maskblue
                        RESPONSE=" "
                        ANSWERED=0
                    else:
                        # otherwise, select and move pertinent mask over the word
                        maskblue = TextureStimulus(texture=useTHISmask,position=(54,213), anchor='upperleft', max_alpha=0.50)
                        MASKLIST[0]=maskblue
                        RESPONSE=CURRENTLIST[11]
                        ANSWERED=1
                    screen.clear()
                    viewport.draw()
                    viewportTEXT2.draw()
                    viewportmasks.draw()
                    VisionEgg.Core.swap_buffers()
                    
                elif x >= 53 and x <= 349 and y <= 184 and y >= 155:
                     ##   col1_row13
                    EXITLIST=[0,0,0]
                    if RESPONSE==CURRENTLIST[12]:
                        # if already selected, unselect and move pertinent mask offscreen
                        maskblue = TextureStimulus(texture=useTHISmask,position=(-200,-200), anchor='upperleft', max_alpha=0.50)
                        MASKLIST[0]=maskblue
                        RESPONSE=" "
                        ANSWERED=0
                    else:
                        # otherwise, select and move pertinent mask over the word
                        maskblue = TextureStimulus(texture=useTHISmask,position=(54,183), anchor='upperleft', max_alpha=0.50)
                        MASKLIST[0]=maskblue
                        RESPONSE=CURRENTLIST[12]
                        ANSWERED=1
                    screen.clear()
                    viewport.draw()
                    viewportTEXT2.draw()
                    viewportmasks.draw()
                    VisionEgg.Core.swap_buffers()
                    
                elif x >= 53 and x <= 349 and y <= 154 and y >= 125:
                     ##   col1_row14
                    EXITLIST=[0,0,0]
                    if RESPONSE==CURRENTLIST[13]:
                        # if already selected, unselect and move pertinent mask offscreen
                        maskblue = TextureStimulus(texture=useTHISmask,position=(-200,-200), anchor='upperleft', max_alpha=0.50)
                        MASKLIST[0]=maskblue
                        RESPONSE=" "
                        ANSWERED=0
                    else:
                        # otherwise, select and move pertinent mask over the word
                        maskblue = TextureStimulus(texture=useTHISmask,position=(54,153), anchor='upperleft', max_alpha=0.50)
                        MASKLIST[0]=maskblue
                        RESPONSE=CURRENTLIST[13]
                        ANSWERED=1
                    screen.clear()
                    viewport.draw()
                    viewportTEXT2.draw()
                    viewportmasks.draw()
                    VisionEgg.Core.swap_buffers()
                    
                elif x >= 53 and x <= 349 and y <= 124 and y >= 95:
                     ##   col1_row15
                    EXITLIST=[0,0,0]
                    if RESPONSE==CURRENTLIST[14]:
                        # if already selected, unselect and move pertinent mask offscreen
                        maskblue = TextureStimulus(texture=useTHISmask,position=(-200,-200), anchor='upperleft', max_alpha=0.50)
                        MASKLIST[0]=maskblue
                        RESPONSE=" "
                        ANSWERED=0
                    else:
                        # otherwise, select and move pertinent mask over the word
                        maskblue = TextureStimulus(texture=useTHISmask,position=(54,123), anchor='upperleft', max_alpha=0.50)
                        MASKLIST[0]=maskblue
                        RESPONSE=CURRENTLIST[14]
                        ANSWERED=1
                    screen.clear()
                    viewport.draw()
                    viewportTEXT2.draw()
                    viewportmasks.draw()
                    VisionEgg.Core.swap_buffers()
                    
                elif x >= 53 and x <= 349 and y <= 94 and y >= 65:
                     ##   col1_row16
                    EXITLIST=[0,0,0]
                    if RESPONSE==CURRENTLIST[15]:
                        # if already selected, unselect and move pertinent mask offscreen
                        maskblue = TextureStimulus(texture=useTHISmask,position=(-200,-200), anchor='upperleft', max_alpha=0.50)
                        MASKLIST[0]=maskblue
                        RESPONSE=" "
                        ANSWERED=0
                    else:
                        # otherwise, select and move pertinent mask over the word
                        maskblue = TextureStimulus(texture=useTHISmask,position=(54,93), anchor='upperleft', max_alpha=0.50)
                        MASKLIST[0]=maskblue
                        RESPONSE=CURRENTLIST[15]
                        ANSWERED=1
                    screen.clear()
                    viewport.draw()
                    viewportTEXT2.draw()
                    viewportmasks.draw()
                    VisionEgg.Core.swap_buffers()
                    
                elif x >= 53 and x <= 349 and y <= 64 and y >= 35:
                     ##   col1_row17
                    EXITLIST=[0,0,0]
                    if RESPONSE==CURRENTLIST[16]:
                        # if already selected, unselect and move pertinent mask offscreen
                        maskblue = TextureStimulus(texture=useTHISmask,position=(-200,-200), anchor='upperleft', max_alpha=0.50)
                        MASKLIST[0]=maskblue
                        RESPONSE=" "
                        ANSWERED=0
                    else:
                        # otherwise, select and move pertinent mask over the word
                        maskblue = TextureStimulus(texture=useTHISmask,position=(54,63), anchor='upperleft', max_alpha=0.50)
                        MASKLIST[0]=maskblue
                        RESPONSE=CURRENTLIST[16]
                        ANSWERED=1
                    screen.clear()
                    viewport.draw()
                    viewportTEXT2.draw()
                    viewportmasks.draw()
                    VisionEgg.Core.swap_buffers()
                    
                elif x >= 53 and x <= 349 and y <= 34 and y >= 5:
                     ##   col1_row18
                    EXITLIST=[0,0,0]
                    if RESPONSE==CURRENTLIST[17]:
                        # if already selected, unselect and move pertinent mask offscreen
                        maskblue = TextureStimulus(texture=useTHISmask,position=(-200,-200), anchor='upperleft', max_alpha=0.50)
                        MASKLIST[0]=maskblue
                        RESPONSE=" "
                        ANSWERED=0
                    else:
                        # otherwise, select and move pertinent mask over the word
                        maskblue = TextureStimulus(texture=useTHISmask,position=(54,33), anchor='upperleft', max_alpha=0.50)
                        MASKLIST[0]=maskblue
                        RESPONSE=CURRENTLIST[17]
                        ANSWERED=1
                    screen.clear()
                    viewport.draw()
                    viewportTEXT2.draw()
                    viewportmasks.draw()
                    VisionEgg.Core.swap_buffers()
                    
                elif x >= 364 and x <= 662 and y <= 544 and y >= 515:
                     ##   col2_row__1
                    EXITLIST=[0,0,0]
                    if RESPONSE==CURRENTLIST[18]:
                        # if already selected, unselect and move pertinent mask offscreen
                        maskblue = TextureStimulus(texture=useTHISmask,position=(-200,-200), anchor='upperleft', max_alpha=0.50)
                        MASKLIST[0]=maskblue
                        RESPONSE=" "
                        ANSWERED=0
                    else:
                        # otherwise, select and move pertinent mask over the word
                        maskblue = TextureStimulus(texture=useTHISmask,position=(365,543), anchor='upperleft', max_alpha=0.50)
                        MASKLIST[0]=maskblue
                        RESPONSE=CURRENTLIST[18]
                        ANSWERED=1
                    screen.clear()
                    viewport.draw()
                    viewportTEXT2.draw()
                    viewportmasks.draw()
                    VisionEgg.Core.swap_buffers()
                    
                elif x >= 364 and x <= 662 and y <= 514 and y >= 485:
                     ##   col2_row2
                    EXITLIST=[0,0,0]
                    if RESPONSE==CURRENTLIST[19]:
                        # if already selected, unselect and move pertinent mask offscreen
                        maskblue = TextureStimulus(texture=useTHISmask,position=(-200,-200), anchor='upperleft', max_alpha=0.50)
                        MASKLIST[0]=maskblue
                        RESPONSE=" "
                        ANSWERED=0
                    else:
                        # otherwise, select and move pertinent mask over the word
                        maskblue = TextureStimulus(texture=useTHISmask,position=(365,513), anchor='upperleft', max_alpha=0.50)
                        MASKLIST[0]=maskblue
                        RESPONSE=CURRENTLIST[19]
                        ANSWERED=1
                    screen.clear()
                    viewport.draw()
                    viewportTEXT2.draw()
                    viewportmasks.draw()
                    VisionEgg.Core.swap_buffers()
                    
                elif x >= 364 and x <= 662 and y <= 484 and y >= 455:
                     ##   col2_row3
                    EXITLIST=[0,0,0]
                    if RESPONSE==CURRENTLIST[20]:
                        # if already selected, unselect and move pertinent mask offscreen
                        maskblue = TextureStimulus(texture=useTHISmask,position=(-200,-200), anchor='upperleft', max_alpha=0.50)
                        MASKLIST[0]=maskblue
                        RESPONSE=" "
                        ANSWERED=0
                    else:
                        # otherwise, select and move pertinent mask over the word
                        maskblue = TextureStimulus(texture=useTHISmask,position=(365,483), anchor='upperleft', max_alpha=0.50)
                        MASKLIST[0]=maskblue
                        RESPONSE=CURRENTLIST[20]
                        ANSWERED=1
                    screen.clear()
                    viewport.draw()
                    viewportTEXT2.draw()
                    viewportmasks.draw()
                    VisionEgg.Core.swap_buffers()
                    
                elif x >= 364 and x <= 662 and y <= 454 and y >= 425:
                     ##   col2_row4
                    EXITLIST=[0,0,0]
                    if RESPONSE==CURRENTLIST[21]:
                        # if already selected, unselect and move pertinent mask offscreen
                        maskblue = TextureStimulus(texture=useTHISmask,position=(-200,-200), anchor='upperleft', max_alpha=0.50)
                        MASKLIST[0]=maskblue
                        RESPONSE=" "
                        ANSWERED=0
                    else:
                        # otherwise, select and move pertinent mask over the word
                        maskblue = TextureStimulus(texture=useTHISmask,position=(365,453), anchor='upperleft', max_alpha=0.50)
                        MASKLIST[0]=maskblue
                        RESPONSE=CURRENTLIST[21]
                        ANSWERED=1
                    screen.clear()
                    viewport.draw()
                    viewportTEXT2.draw()
                    viewportmasks.draw()
                    VisionEgg.Core.swap_buffers()
                    
                elif x >= 364 and x <= 662 and y <= 424 and y >= 395:
                     ##   col2_row5
                    EXITLIST=[0,0,0]
                    if RESPONSE==CURRENTLIST[22]:
                        # if already selected, unselect and move pertinent mask offscreen
                        maskblue = TextureStimulus(texture=useTHISmask,position=(-200,-200), anchor='upperleft', max_alpha=0.50)
                        MASKLIST[0]=maskblue
                        RESPONSE=" "
                        ANSWERED=0
                    else:
                        # otherwise, select and move pertinent mask over the word
                        maskblue = TextureStimulus(texture=useTHISmask,position=(365,423), anchor='upperleft', max_alpha=0.50)
                        MASKLIST[0]=maskblue
                        RESPONSE=CURRENTLIST[22]
                        ANSWERED=1
                    screen.clear()
                    viewport.draw()
                    viewportTEXT2.draw()
                    viewportmasks.draw()
                    VisionEgg.Core.swap_buffers()
                    
                elif x >= 364 and x <= 662 and y <= 394 and y >= 365:
                     ##   col2_row6
                    EXITLIST=[0,0,0]
                    if RESPONSE==CURRENTLIST[23]:
                        # if already selected, unselect and move pertinent mask offscreen
                        maskblue = TextureStimulus(texture=useTHISmask,position=(-200,-200), anchor='upperleft', max_alpha=0.50)
                        MASKLIST[0]=maskblue
                        RESPONSE=" "
                        ANSWERED=0
                    else:
                        # otherwise, select and move pertinent mask over the word
                        maskblue = TextureStimulus(texture=useTHISmask,position=(365,393), anchor='upperleft', max_alpha=0.50)
                        MASKLIST[0]=maskblue
                        RESPONSE=CURRENTLIST[23]
                        ANSWERED=1
                    screen.clear()
                    viewport.draw()
                    viewportTEXT2.draw()
                    viewportmasks.draw()
                    VisionEgg.Core.swap_buffers()
                    
                elif x >= 364 and x <= 662 and y <= 364 and y >= 335:
                     ##   col2_row7
                    EXITLIST=[0,0,0]
                    if RESPONSE==CURRENTLIST[24]:
                        # if already selected, unselect and move pertinent mask offscreen
                        maskblue = TextureStimulus(texture=useTHISmask,position=(-200,-200), anchor='upperleft', max_alpha=0.50)
                        MASKLIST[0]=maskblue
                        RESPONSE=" "
                        ANSWERED=0
                    else:
                        # otherwise, select and move pertinent mask over the word
                        maskblue = TextureStimulus(texture=useTHISmask,position=(365,363), anchor='upperleft', max_alpha=0.50)
                        MASKLIST[0]=maskblue
                        RESPONSE=CURRENTLIST[24]
                        ANSWERED=1
                    screen.clear()
                    viewport.draw()
                    viewportTEXT2.draw()
                    viewportmasks.draw()
                    VisionEgg.Core.swap_buffers()
                    
                elif x >= 364 and x <= 662 and y <= 334 and y >= 305:
                     ##   col2_row8
                    EXITLIST=[0,0,0]
                    if RESPONSE==CURRENTLIST[25]:
                        # if already selected, unselect and move pertinent mask offscreen
                        maskblue = TextureStimulus(texture=useTHISmask,position=(-200,-200), anchor='upperleft', max_alpha=0.50)
                        MASKLIST[0]=maskblue
                        RESPONSE=" "
                        ANSWERED=0
                    else:
                        # otherwise, select and move pertinent mask over the word
                        maskblue = TextureStimulus(texture=useTHISmask,position=(365,333), anchor='upperleft', max_alpha=0.50)
                        MASKLIST[0]=maskblue
                        RESPONSE=CURRENTLIST[25]
                        ANSWERED=1
                    screen.clear()
                    viewport.draw()
                    viewportTEXT2.draw()
                    viewportmasks.draw()
                    VisionEgg.Core.swap_buffers()
                    
                elif x >= 364 and x <= 662 and y <= 304 and y >= 275:
                     ##   col2_row9
                    EXITLIST=[0,0,0]
                    if RESPONSE==CURRENTLIST[26]:
                        # if already selected, unselect and move pertinent mask offscreen
                        maskblue = TextureStimulus(texture=useTHISmask,position=(-200,-200), anchor='upperleft', max_alpha=0.50)
                        MASKLIST[0]=maskblue
                        RESPONSE=" "
                        ANSWERED=0
                    else:
                        # otherwise, select and move pertinent mask over the word
                        maskblue = TextureStimulus(texture=useTHISmask,position=(365,303), anchor='upperleft', max_alpha=0.50)
                        MASKLIST[0]=maskblue
                        RESPONSE=CURRENTLIST[26]
                        ANSWERED=1
                    screen.clear()
                    viewport.draw()
                    viewportTEXT2.draw()
                    viewportmasks.draw()
                    VisionEgg.Core.swap_buffers()
                    
                elif x >= 364 and x <= 662 and y <= 274 and y >= 245:
                     ##   col2_row10
                    EXITLIST=[0,0,0]
                    if RESPONSE==CURRENTLIST[27]:
                        # if already selected, unselect and move pertinent mask offscreen
                        maskblue = TextureStimulus(texture=useTHISmask,position=(-200,-200), anchor='upperleft', max_alpha=0.50)
                        MASKLIST[0]=maskblue
                        RESPONSE=" "
                        ANSWERED=0
                    else:
                        # otherwise, select and move pertinent mask over the word
                        maskblue = TextureStimulus(texture=useTHISmask,position=(365,273), anchor='upperleft', max_alpha=0.50)
                        MASKLIST[0]=maskblue
                        RESPONSE=CURRENTLIST[27]
                        ANSWERED=1
                    screen.clear()
                    viewport.draw()
                    viewportTEXT2.draw()
                    viewportmasks.draw()
                    VisionEgg.Core.swap_buffers()
                    
                elif x >= 364 and x <= 662 and y <= 244 and y >= 215:
                     ##   col2_row11
                    EXITLIST=[0,0,0]
                    if RESPONSE==CURRENTLIST[28]:
                        # if already selected, unselect and move pertinent mask offscreen
                        maskblue = TextureStimulus(texture=useTHISmask,position=(-200,-200), anchor='upperleft', max_alpha=0.50)
                        MASKLIST[0]=maskblue
                        RESPONSE=" "
                        ANSWERED=0
                    else:
                        # otherwise, select and move pertinent mask over the word
                        maskblue = TextureStimulus(texture=useTHISmask,position=(365,243), anchor='upperleft', max_alpha=0.50)
                        MASKLIST[0]=maskblue
                        RESPONSE=CURRENTLIST[28]
                        ANSWERED=1
                    screen.clear()
                    viewport.draw()
                    viewportTEXT2.draw()
                    viewportmasks.draw()
                    VisionEgg.Core.swap_buffers()
                    
                elif x >= 364 and x <= 662 and y <= 214 and y >= 185:
                     ##   col2_row12
                    EXITLIST=[0,0,0]
                    if RESPONSE==CURRENTLIST[29]:
                        # if already selected, unselect and move pertinent mask offscreen
                        maskblue = TextureStimulus(texture=useTHISmask,position=(-200,-200), anchor='upperleft', max_alpha=0.50)
                        MASKLIST[0]=maskblue
                        RESPONSE=" "
                        ANSWERED=0
                    else:
                        # otherwise, select and move pertinent mask over the word
                        maskblue = TextureStimulus(texture=useTHISmask,position=(365,213), anchor='upperleft', max_alpha=0.50)
                        MASKLIST[0]=maskblue
                        RESPONSE=CURRENTLIST[29]
                        ANSWERED=1
                    screen.clear()
                    viewport.draw()
                    viewportTEXT2.draw()
                    viewportmasks.draw()
                    VisionEgg.Core.swap_buffers()
                    
                elif x >= 364 and x <= 662 and y <= 184 and y >= 155:
                     ##   col2_row13
                    EXITLIST=[0,0,0]
                    if RESPONSE==CURRENTLIST[30]:
                        # if already selected, unselect and move pertinent mask offscreen
                        maskblue = TextureStimulus(texture=useTHISmask,position=(-200,-200), anchor='upperleft', max_alpha=0.50)
                        MASKLIST[0]=maskblue
                        RESPONSE=" "
                        ANSWERED=0
                    else:
                        # otherwise, select and move pertinent mask over the word
                        maskblue = TextureStimulus(texture=useTHISmask,position=(365,183), anchor='upperleft', max_alpha=0.50)
                        MASKLIST[0]=maskblue
                        RESPONSE=CURRENTLIST[30]
                        ANSWERED=1
                    screen.clear()
                    viewport.draw()
                    viewportTEXT2.draw()
                    viewportmasks.draw()
                    VisionEgg.Core.swap_buffers()
                    
                elif x >= 364 and x <= 662 and y <= 154 and y >= 125:
                     ##   col2_row14
                    EXITLIST=[0,0,0]
                    if RESPONSE==CURRENTLIST[31]:
                        # if already selected, unselect and move pertinent mask offscreen
                        maskblue = TextureStimulus(texture=useTHISmask,position=(-200,-200), anchor='upperleft', max_alpha=0.50)
                        MASKLIST[0]=maskblue
                        RESPONSE=" "
                        ANSWERED=0
                    else:
                        # otherwise, select and move pertinent mask over the word
                        maskblue = TextureStimulus(texture=useTHISmask,position=(365,153), anchor='upperleft', max_alpha=0.50)
                        MASKLIST[0]=maskblue
                        RESPONSE=CURRENTLIST[31]
                        ANSWERED=1
                    screen.clear()
                    viewport.draw()
                    viewportTEXT2.draw()
                    viewportmasks.draw()
                    VisionEgg.Core.swap_buffers()
                    
                elif x >= 364 and x <= 662 and y <= 124 and y >= 95:
                     ##   col2_row15
                    EXITLIST=[0,0,0]
                    if RESPONSE==CURRENTLIST[32]:
                        # if already selected, unselect and move pertinent mask offscreen
                        maskblue = TextureStimulus(texture=useTHISmask,position=(-200,-200), anchor='upperleft', max_alpha=0.50)
                        MASKLIST[0]=maskblue
                        RESPONSE=" "
                        ANSWERED=0
                    else:
                        # otherwise, select and move pertinent mask over the word
                        maskblue = TextureStimulus(texture=useTHISmask,position=(365,123), anchor='upperleft', max_alpha=0.50)
                        MASKLIST[0]=maskblue
                        RESPONSE=CURRENTLIST[32]
                        ANSWERED=1
                    screen.clear()
                    viewport.draw()
                    viewportTEXT2.draw()
                    viewportmasks.draw()
                    VisionEgg.Core.swap_buffers()
                    
                elif x >= 364 and x <= 662 and y <= 94 and y >= 65:
                     ##   col2_row16
                    EXITLIST=[0,0,0]
                    if RESPONSE==CURRENTLIST[33]:
                        # if already selected, unselect and move pertinent mask offscreen
                        maskblue = TextureStimulus(texture=useTHISmask,position=(-200,-200), anchor='upperleft', max_alpha=0.50)
                        MASKLIST[0]=maskblue
                        RESPONSE=" "
                        ANSWERED=0
                    else:
                        # otherwise, select and move pertinent mask over the word
                        maskblue = TextureStimulus(texture=useTHISmask,position=(365,93), anchor='upperleft', max_alpha=0.50)
                        MASKLIST[0]=maskblue
                        RESPONSE=CURRENTLIST[33]
                        ANSWERED=1
                    screen.clear()
                    viewport.draw()
                    viewportTEXT2.draw()
                    viewportmasks.draw()
                    VisionEgg.Core.swap_buffers()
                    
                elif x >= 364 and x <= 662 and y <= 64 and y >= 35:
                     ##   col2_row17
                    EXITLIST=[0,0,0]
                    if RESPONSE==CURRENTLIST[34]:
                        # if already selected, unselect and move pertinent mask offscreen
                        maskblue = TextureStimulus(texture=useTHISmask,position=(-200,-200), anchor='upperleft', max_alpha=0.50)
                        MASKLIST[0]=maskblue
                        RESPONSE=" "
                        ANSWERED=0
                    else:
                        # otherwise, select and move pertinent mask over the word
                        maskblue = TextureStimulus(texture=useTHISmask,position=(365,63), anchor='upperleft', max_alpha=0.50)
                        MASKLIST[0]=maskblue
                        RESPONSE=CURRENTLIST[34]
                        ANSWERED=1
                    screen.clear()
                    viewport.draw()
                    viewportTEXT2.draw()
                    viewportmasks.draw()
                    VisionEgg.Core.swap_buffers()
                    
                elif x >= 364 and x <= 662 and y <= 34 and y >= 5:
                     ##   col2_row18
                    EXITLIST=[0,0,0]
                    if RESPONSE==CURRENTLIST[35]:
                        # if already selected, unselect and move pertinent mask offscreen
                        maskblue = TextureStimulus(texture=useTHISmask,position=(-200,-200), anchor='upperleft', max_alpha=0.50)
                        MASKLIST[0]=maskblue
                        RESPONSE=" "
                        ANSWERED=0
                    else:
                        # otherwise, select and move pertinent mask over the word
                        maskblue = TextureStimulus(texture=useTHISmask,position=(365,33), anchor='upperleft', max_alpha=0.50)
                        MASKLIST[0]=maskblue
                        RESPONSE=CURRENTLIST[35]
                        ANSWERED=1
                    screen.clear()
                    viewport.draw()
                    viewportTEXT2.draw()
                    viewportmasks.draw()
                    VisionEgg.Core.swap_buffers()
                    

                elif x >= 676 and x <= 974 and y <= 544 and y >= 515:
                     ##   col3_row__1
                    EXITLIST=[0,0,0]
                    if RESPONSE==CURRENTLIST[36]:
                        # if already selected, unselect and move pertinent mask offscreen
                        maskblue = TextureStimulus(texture=useTHISmask,position=(-200,-200), anchor='upperleft', max_alpha=0.50)
                        MASKLIST[0]=maskblue
                        RESPONSE=" "
                        ANSWERED=0
                    else:
                        # otherwise, select and move pertinent mask over the word
                        maskblue = TextureStimulus(texture=useTHISmask,position=(675,543), anchor='upperleft', max_alpha=0.50)
                        MASKLIST[0]=maskblue
                        RESPONSE=CURRENTLIST[36]
                        ANSWERED=1
                    screen.clear()
                    viewport.draw()
                    viewportTEXT2.draw()
                    viewportmasks.draw()
                    VisionEgg.Core.swap_buffers()
                    
                elif x >= 676 and x <= 974 and y <= 514 and y >= 485:
                     ##   col3_row2
                    EXITLIST=[0,0,0]
                    if RESPONSE==CURRENTLIST[37]:
                        # if already selected, unselect and move pertinent mask offscreen
                        maskblue = TextureStimulus(texture=useTHISmask,position=(-200,-200), anchor='upperleft', max_alpha=0.50)
                        MASKLIST[0]=maskblue
                        RESPONSE=" "
                        ANSWERED=0
                    else:
                        # otherwise, select and move pertinent mask over the word
                        maskblue = TextureStimulus(texture=useTHISmask,position=(675,513), anchor='upperleft', max_alpha=0.50)
                        MASKLIST[0]=maskblue
                        RESPONSE=CURRENTLIST[37]
                        ANSWERED=1
                    screen.clear()
                    viewport.draw()
                    viewportTEXT2.draw()
                    viewportmasks.draw()
                    VisionEgg.Core.swap_buffers()
                    
                elif x >= 676 and x <= 974 and y <= 484 and y >= 455:
                     ##   col3_row3
                    EXITLIST=[0,0,0]
                    if RESPONSE==CURRENTLIST[38]:
                        # if already selected, unselect and move pertinent mask offscreen
                        maskblue = TextureStimulus(texture=useTHISmask,position=(-200,-200), anchor='upperleft', max_alpha=0.50)
                        MASKLIST[0]=maskblue
                        RESPONSE=" "
                        ANSWERED=0
                    else:
                        # otherwise, select and move pertinent mask over the word
                        maskblue = TextureStimulus(texture=useTHISmask,position=(675,483), anchor='upperleft', max_alpha=0.50)
                        MASKLIST[0]=maskblue
                        RESPONSE=CURRENTLIST[38]
                        ANSWERED=1
                    screen.clear()
                    viewport.draw()
                    viewportTEXT2.draw()
                    viewportmasks.draw()
                    VisionEgg.Core.swap_buffers()
                    
                elif x >= 676 and x <= 974 and y <= 454 and y >= 425:
                     ##   col3_row4
                    EXITLIST=[0,0,0]
                    if RESPONSE==CURRENTLIST[39]:
                        # if already selected, unselect and move pertinent mask offscreen
                        maskblue = TextureStimulus(texture=useTHISmask,position=(-200,-200), anchor='upperleft', max_alpha=0.50)
                        MASKLIST[0]=maskblue
                        RESPONSE=" "
                        ANSWERED=0
                    else:
                        # otherwise, select and move pertinent mask over the word
                        maskblue = TextureStimulus(texture=useTHISmask,position=(675,453), anchor='upperleft', max_alpha=0.50)
                        MASKLIST[0]=maskblue
                        RESPONSE=CURRENTLIST[39]
                        ANSWERED=1
                    screen.clear()
                    viewport.draw()
                    viewportTEXT2.draw()
                    viewportmasks.draw()
                    VisionEgg.Core.swap_buffers()
                    
                elif x >= 676 and x <= 974 and y <= 424 and y >= 395:
                     ##   col3_row5
                    EXITLIST=[0,0,0]
                    if RESPONSE==CURRENTLIST[40]:
                        # if already selected, unselect and move pertinent mask offscreen
                        maskblue = TextureStimulus(texture=useTHISmask,position=(-200,-200), anchor='upperleft', max_alpha=0.50)
                        MASKLIST[0]=maskblue
                        RESPONSE=" "
                        ANSWERED=0
                    else:
                        # otherwise, select and move pertinent mask over the word
                        maskblue = TextureStimulus(texture=useTHISmask,position=(675,423), anchor='upperleft', max_alpha=0.50)
                        MASKLIST[0]=maskblue
                        RESPONSE=CURRENTLIST[40]
                        ANSWERED=1
                    screen.clear()
                    viewport.draw()
                    viewportTEXT2.draw()
                    viewportmasks.draw()
                    VisionEgg.Core.swap_buffers()
                    
                elif x >= 676 and x <= 974 and y <= 394 and y >= 365:
                     ##   col3_row6
                    EXITLIST=[0,0,0]
                    if RESPONSE==CURRENTLIST[41]:
                        # if already selected, unselect and move pertinent mask offscreen
                        maskblue = TextureStimulus(texture=useTHISmask,position=(-200,-200), anchor='upperleft', max_alpha=0.50)
                        MASKLIST[0]=maskblue
                        RESPONSE=" "
                        ANSWERED=0
                    else:
                        # otherwise, select and move pertinent mask over the word
                        maskblue = TextureStimulus(texture=useTHISmask,position=(675,393), anchor='upperleft', max_alpha=0.50)
                        MASKLIST[0]=maskblue
                        RESPONSE=CURRENTLIST[41]
                        ANSWERED=1
                    screen.clear()
                    viewport.draw()
                    viewportTEXT2.draw()
                    viewportmasks.draw()
                    VisionEgg.Core.swap_buffers()
                    
                elif x >= 676 and x <= 974 and y <= 364 and y >= 335:
                     ##   col3_row7
                    EXITLIST=[0,0,0]
                    if RESPONSE==CURRENTLIST[42]:
                        # if already selected, unselect and move pertinent mask offscreen
                        maskblue = TextureStimulus(texture=useTHISmask,position=(-200,-200), anchor='upperleft', max_alpha=0.50)
                        MASKLIST[0]=maskblue
                        RESPONSE=" "
                        ANSWERED=0
                    else:
                        # otherwise, select and move pertinent mask over the word
                        maskblue = TextureStimulus(texture=useTHISmask,position=(675,363), anchor='upperleft', max_alpha=0.50)
                        MASKLIST[0]=maskblue
                        RESPONSE=CURRENTLIST[42]
                        ANSWERED=1
                    screen.clear()
                    viewport.draw()
                    viewportTEXT2.draw()
                    viewportmasks.draw()
                    VisionEgg.Core.swap_buffers()
                    
                elif x >= 676 and x <= 974 and y <= 334 and y >= 305:
                     ##   col3_row8
                    EXITLIST=[0,0,0]
                    if RESPONSE==CURRENTLIST[43]:
                        # if already selected, unselect and move pertinent mask offscreen
                        maskblue = TextureStimulus(texture=useTHISmask,position=(-200,-200), anchor='upperleft', max_alpha=0.50)
                        MASKLIST[0]=maskblue
                        RESPONSE=" "
                        ANSWERED=0
                    else:
                        # otherwise, select and move pertinent mask over the word
                        maskblue = TextureStimulus(texture=useTHISmask,position=(675,333), anchor='upperleft', max_alpha=0.50)
                        MASKLIST[0]=maskblue
                        RESPONSE=CURRENTLIST[43]
                        ANSWERED=1
                    screen.clear()
                    viewport.draw()
                    viewportTEXT2.draw()
                    viewportmasks.draw()
                    VisionEgg.Core.swap_buffers()
                    
                elif x >= 676 and x <= 974 and y <= 304 and y >= 275:
                     ##   col3_row9
                    EXITLIST=[0,0,0]
                    if RESPONSE==CURRENTLIST[44]:
                        # if already selected, unselect and move pertinent mask offscreen
                        maskblue = TextureStimulus(texture=useTHISmask,position=(-200,-200), anchor='upperleft', max_alpha=0.50)
                        MASKLIST[0]=maskblue
                        RESPONSE=" "
                        ANSWERED=0
                    else:
                        # otherwise, select and move pertinent mask over the word
                        maskblue = TextureStimulus(texture=useTHISmask,position=(675,303), anchor='upperleft', max_alpha=0.50)
                        MASKLIST[0]=maskblue
                        RESPONSE=CURRENTLIST[44]
                        ANSWERED=1
                    screen.clear()
                    viewport.draw()
                    viewportTEXT2.draw()
                    viewportmasks.draw()
                    VisionEgg.Core.swap_buffers()
                    
                elif x >= 676 and x <= 974 and y <= 274 and y >= 245:
                     ##   col3_row10
                    EXITLIST=[0,0,0]
                    if RESPONSE==CURRENTLIST[45]:
                        # if already selected, unselect and move pertinent mask offscreen
                        maskblue = TextureStimulus(texture=useTHISmask,position=(-200,-200), anchor='upperleft', max_alpha=0.50)
                        MASKLIST[0]=maskblue
                        RESPONSE=" "
                        ANSWERED=0
                    else:
                        # otherwise, select and move pertinent mask over the word
                        maskblue = TextureStimulus(texture=useTHISmask,position=(675,273), anchor='upperleft', max_alpha=0.50)
                        MASKLIST[0]=maskblue
                        RESPONSE=CURRENTLIST[45]
                        ANSWERED=1
                    screen.clear()
                    viewport.draw()
                    viewportTEXT2.draw()
                    viewportmasks.draw()
                    VisionEgg.Core.swap_buffers()
                    
                elif x >= 676 and x <= 974 and y <= 244 and y >= 215:
                     ##   col3_row11
                    EXITLIST=[0,0,0]
                    if RESPONSE==CURRENTLIST[46]:
                        # if already selected, unselect and move pertinent mask offscreen
                        maskblue = TextureStimulus(texture=useTHISmask,position=(-200,-200), anchor='upperleft', max_alpha=0.50)
                        MASKLIST[0]=maskblue
                        RESPONSE=" "
                        ANSWERED=0
                    else:
                        # otherwise, select and move pertinent mask over the word
                        maskblue = TextureStimulus(texture=useTHISmask,position=(675,243), anchor='upperleft', max_alpha=0.50)
                        MASKLIST[0]=maskblue
                        RESPONSE=CURRENTLIST[46]
                        ANSWERED=1
                    screen.clear()
                    viewport.draw()
                    viewportTEXT2.draw()
                    viewportmasks.draw()
                    VisionEgg.Core.swap_buffers()
                    
                elif x >= 676 and x <= 974 and y <= 214 and y >= 185:
                     ##   col3_row12
                    EXITLIST=[0,0,0]
                    if RESPONSE==CURRENTLIST[47]:
                        # if already selected, unselect and move pertinent mask offscreen
                        maskblue = TextureStimulus(texture=useTHISmask,position=(-200,-200), anchor='upperleft', max_alpha=0.50)
                        MASKLIST[0]=maskblue
                        RESPONSE=" "
                        ANSWERED=0
                    else:
                        # otherwise, select and move pertinent mask over the word
                        maskblue = TextureStimulus(texture=useTHISmask,position=(675,213), anchor='upperleft', max_alpha=0.50)
                        MASKLIST[0]=maskblue
                        RESPONSE=CURRENTLIST[47]
                        ANSWERED=1
                    screen.clear()
                    viewport.draw()
                    viewportTEXT2.draw()
                    viewportmasks.draw()
                    VisionEgg.Core.swap_buffers()
                    
                elif x >= 676 and x <= 974 and y <= 184 and y >= 155:
                     ##   col3_row13
                    EXITLIST=[0,0,0]
                    if RESPONSE==CURRENTLIST[48]:
                        # if already selected, unselect and move pertinent mask offscreen
                        maskblue = TextureStimulus(texture=useTHISmask,position=(-200,-200), anchor='upperleft', max_alpha=0.50)
                        MASKLIST[0]=maskblue
                        RESPONSE=" "
                        ANSWERED=0
                    else:
                        # otherwise, select and move pertinent mask over the word
                        maskblue = TextureStimulus(texture=useTHISmask,position=(675,183), anchor='upperleft', max_alpha=0.50)
                        MASKLIST[0]=maskblue
                        RESPONSE=CURRENTLIST[48]
                        ANSWERED=1
                    screen.clear()
                    viewport.draw()
                    viewportTEXT2.draw()
                    viewportmasks.draw()
                    VisionEgg.Core.swap_buffers()
                    
                elif x >= 676 and x <= 974 and y <= 154 and y >= 125:
                     ##   col3_row14
                    EXITLIST=[0,0,0]
                    if RESPONSE==CURRENTLIST[49]:
                        # if already selected, unselect and move pertinent mask offscreen
                        maskblue = TextureStimulus(texture=useTHISmask,position=(-200,-200), anchor='upperleft', max_alpha=0.50)
                        MASKLIST[0]=maskblue
                        RESPONSE=" "
                        ANSWERED=0
                    else:
                        # otherwise, select and move pertinent mask over the word
                        maskblue = TextureStimulus(texture=useTHISmask,position=(675,153), anchor='upperleft', max_alpha=0.50)
                        MASKLIST[0]=maskblue
                        RESPONSE=CURRENTLIST[49]
                        ANSWERED=1
                    screen.clear()
                    viewport.draw()
                    viewportTEXT2.draw()
                    viewportmasks.draw()
                    VisionEgg.Core.swap_buffers()
                      
                ##
                ## now we see the practical application of the EXITLIST:
                elif x >= 0 and x <=24 and y >= 584 and y <=600:
                   if EXITLIST==[0,0,0]:
                       EXITLIST[0]=1
                       text0 = Text(text="O",color=(0,0,0),position=(0,600),font_size=30,anchor='center')
                       text1 = Text(text="O",color=(0,0,0),position=(0,600),font_size=30,anchor='center')
                       viewportTEXT = VisionEgg.Core.Viewport(screen=screen, size=screen.size, stimuli=[text0, text1])
                       VisionEgg.Core.swap_buffers()
                       screen.clear()
                       viewport.draw()
                       viewportmasks.draw()
                       viewportTEXT.draw()
                       viewportTEXT2.draw()
                       VisionEgg.Core.swap_buffers()
                elif x >= 1008 and x <=1024 and y >= 584 and y <=600:
                    if EXITLIST==[1,0,0]:
                       EXITLIST[1]=1
                       text0 = Text(text="O",color=(0,0,0),position=(0,600),font_size=30,anchor='center')
                       text1 = Text(text="O",color=(0,0,0),position=(1024,600),font_size=30,anchor='center')
                       viewportTEXT = VisionEgg.Core.Viewport(screen=screen, size=screen.size, stimuli=[text0, text1])
                       VisionEgg.Core.swap_buffers()
                       screen.clear()
                       viewport.draw()
                       viewportmasks.draw()
                       viewportTEXT.draw()
                       viewportTEXT2.draw()
                       VisionEgg.Core.swap_buffers()
                elif x >= 1008 and x <=1024 and y >= 0 and y <=16:
                    if EXITLIST==[1,1,0]:
                        ScreenNumber, RESET = ESCAPEscreenLATE(ScreenNumber, RESET)
###  ###   ###  # #     ### ALWAYS REMEMBER TO UPDATE THE RETURN INFO!  ##   #   #   #####  ##  ###    ### ### 
                        return ScreenNumber, TrialTime, RESPONSE, ERRORS, RESET
                        StartTrial=True


####################################################################################################
####################################################################################################
####################################################################################################
####################################################################################################
####################################################################################################
def STATEMENT(ScreenNumber, TrialTime, RESPONSE, ERRORS, RESET):
    x=-1
    y=-1
    #make and show background
    backgroundIMAGE = TextureStimulus(texture=taskbackgrounds[8],position=(0,0))
    viewport = VisionEgg.Core.Viewport(screen=screen, size=screen.size, stimuli=[backgroundIMAGE])
    warnBOX = TextureStimulus(texture=notyetboxes[8],position=(830,150), anchor='center', max_alpha=0.80)
    viewportwarnBOX = VisionEgg.Core.Viewport(screen=screen, size=screen.size, stimuli=[warnBOX])
    useTHISmask=masks[5]
    maskblue = TextureStimulus(texture=useTHISmask,position=(-100,-100), anchor='center', max_alpha=0.50)    
    MASKLIST=[maskblue]
     ## we'll modify the MASKLIST depending on button presses....
    viewportmasks = VisionEgg.Core.Viewport(screen=screen, size=screen.size, stimuli=MASKLIST)
    ##
    EXITLIST=[0,0,0]
    ANSWERED=0
    RESPONSE=" "
    ERRORS=0
    ##
    screen.clear()
    viewport.draw()
    VisionEgg.Core.swap_buffers()
    startTIME=int(round(time() * 1000))
    screen.clear()
    viewport.draw()
    VisionEgg.Core.swap_buffers()
    StartTrial=False
    while not StartTrial:
        for event in pygame.event.get():
            if event.type == pygame.locals.MOUSEBUTTONDOWN:
                if (int(round(time() * 1000))-startTIME) > 100:
                    x,y = pygame.mouse.get_pos()
## pygame.mouse.get_pos() gives coordinates with the LOWER LEFT, not UPPER LEFT (as in visionegg) corner as the origin.
## before we get too complicated, will probably want to flip things around:
                y=600-y
                if x >= 904 and x <=997 and y >=0 and y <=37:
                    EXITLIST=[0,0,0]
                    ## the "touch here when done" box. Action depends on whether there's a full answer.
                    if ANSWERED == 1 and not RESPONSE == " ":
                        ## trial time is in seconds
                        TrialTime=int(round(time() * 1000))-startTIME
                        return ScreenNumber, TrialTime, RESPONSE, ERRORS, RESET
                        StartTrial=True                       
                    else:
                        ERRORS=ERRORS+1
                        screen.clear()
                        viewport.draw()
                        viewportmasks.draw()
                        viewportwarnBOX.draw() #it'll stay up until something else is clicked
                        VisionEgg.Core.swap_buffers()


                elif x >= 300 and x <= 728 and y <= 484 and y >= 428:
                   ## wave goodbye
                    EXITLIST=[0,0,0]
                    if RESPONSE=="WAVE GOODBYE":
                        # if already selected, unselect and move pertinent mask offscreen
                        maskblue = TextureStimulus(texture=useTHISmask,position=(-200,-200), anchor='upperleft', max_alpha=0.50)
                        MASKLIST[0]=maskblue
                        RESPONSE=" "
                        ANSWERED=0
                    else:
                        # otherwise, select and move pertinent mask over the word
                        maskblue = TextureStimulus(texture=useTHISmask,position=(300,484), anchor='upperleft', max_alpha=0.50)
                        MASKLIST[0]=maskblue
                        RESPONSE="WAVE GOODBYE"
                        ANSWERED=1
                    screen.clear()
                    viewport.draw()
                    viewportmasks.draw()
                    VisionEgg.Core.swap_buffers()
                elif x >= 300 and x <= 728 and y <= 418 and y >= 362:
                   ## raise your arms
                    EXITLIST=[0,0,0]
                    if RESPONSE=="RAISE YOUR ARMS":
                        # if already selected, unselect and move pertinent mask offscreen
                        maskblue = TextureStimulus(texture=useTHISmask,position=(-200,-200), anchor='upperleft', max_alpha=0.50)
                        MASKLIST[0]=maskblue
                        RESPONSE=" "
                        ANSWERED=0
                    else:
                        # otherwise, select and move pertinent mask over the word
                        maskblue = TextureStimulus(texture=useTHISmask,position=(300,418), anchor='upperleft', max_alpha=0.50)
                        MASKLIST[0]=maskblue
                        RESPONSE="RAISE YOUR ARMS"
                        ANSWERED=1
                    screen.clear()
                    viewport.draw()
                    viewportmasks.draw()
                    VisionEgg.Core.swap_buffers()
                elif x >= 300 and x <= 728 and y <= 352 and y >= 296:
                   ## close your eyes
                    EXITLIST=[0,0,0]
                    if RESPONSE=="CLOSE YOUR EYES":
                        # if already selected, unselect and move pertinent mask offscreen
                        maskblue = TextureStimulus(texture=useTHISmask,position=(-200,-200), anchor='upperleft', max_alpha=0.50)
                        MASKLIST[0]=maskblue
                        RESPONSE=" "
                        ANSWERED=0
                    else:
                        # otherwise, select and move pertinent mask over the word
                        maskblue = TextureStimulus(texture=useTHISmask,position=(300,352), anchor='upperleft', max_alpha=0.50)
                        MASKLIST[0]=maskblue
                        RESPONSE="CLOSE YOUR EYES"
                        ANSWERED=1
                    screen.clear()
                    viewport.draw()
                    viewportmasks.draw()
                    VisionEgg.Core.swap_buffers()
                elif x >= 300 and x <= 728 and y <= 286 and y >= 230:
                   ## give a salute
                    EXITLIST=[0,0,0]
                    if RESPONSE=="GIVE A SALUTE":
                        # if already selected, unselect and move pertinent mask offscreen
                        maskblue = TextureStimulus(texture=useTHISmask,position=(-200,-200), anchor='upperleft', max_alpha=0.50)
                        MASKLIST[0]=maskblue
                        RESPONSE=" "
                        ANSWERED=0
                    else:
                        # otherwise, select and move pertinent mask over the word
                        maskblue = TextureStimulus(texture=useTHISmask,position=(300,286), anchor='upperleft', max_alpha=0.50)
                        MASKLIST[0]=maskblue
                        RESPONSE="GIVE A SALUTE"
                        ANSWERED=1
                    screen.clear()
                    viewport.draw()
                    viewportmasks.draw()
                    VisionEgg.Core.swap_buffers()
                elif x >= 300 and x <= 728 and y <= 220 and y >= 164:
                   ## wiggle your toes
                    EXITLIST=[0,0,0]
                    if RESPONSE=="WIGGLE YOUR TOES":
                        # if already selected, unselect and move pertinent mask offscreen
                        maskblue = TextureStimulus(texture=useTHISmask,position=(-200,-200), anchor='upperleft', max_alpha=0.50)
                        MASKLIST[0]=maskblue
                        RESPONSE=" "
                        ANSWERED=0
                    else:
                        # otherwise, select and move pertinent mask over the word
                        maskblue = TextureStimulus(texture=useTHISmask,position=(300,220), anchor='upperleft', max_alpha=0.50)
                        MASKLIST[0]=maskblue
                        RESPONSE="WIGGLE YOUR TOES"
                        ANSWERED=1
                    screen.clear()
                    viewport.draw()
                    viewportmasks.draw()
                    VisionEgg.Core.swap_buffers()
                elif x >= 300 and x <= 728 and y <= 154 and y >= 98:
                   ## clap your hands
                    EXITLIST=[0,0,0]
                    if RESPONSE=="CLAP YOUR HANDS":
                        # if already selected, unselect and move pertinent mask offscreen
                        maskblue = TextureStimulus(texture=useTHISmask,position=(-200,-200), anchor='upperleft', max_alpha=0.50)
                        MASKLIST[0]=maskblue
                        RESPONSE=" "
                        ANSWERED=0
                    else:
                        # otherwise, select and move pertinent mask over the word
                        maskblue = TextureStimulus(texture=useTHISmask,position=(300,154), anchor='upperleft', max_alpha=0.50)
                        MASKLIST[0]=maskblue
                        RESPONSE="CLAP YOUR HANDS"
                        ANSWERED=1
                    screen.clear()
                    viewport.draw()
                    viewportmasks.draw()
                    VisionEgg.Core.swap_buffers()          
                ##
                ## now we see the practical application of the EXITLIST:
                elif x >= 0 and x <=24 and y >= 584 and y <=600:
                   if EXITLIST==[0,0,0]:
                       EXITLIST[0]=1
                       text0 = Text(text="O",color=(0,0,0),position=(0,600),font_size=30,anchor='center')
                       text1 = Text(text="O",color=(0,0,0),position=(0,600),font_size=30,anchor='center')
                       viewportTEXT = VisionEgg.Core.Viewport(screen=screen, size=screen.size, stimuli=[text0, text1])
                       VisionEgg.Core.swap_buffers()
                       screen.clear()
                       viewport.draw()
                       viewportmasks.draw()
                       viewportTEXT.draw()
                       VisionEgg.Core.swap_buffers()
                elif x >= 1008 and x <=1024 and y >= 584 and y <=600:
                    if EXITLIST==[1,0,0]:
                       EXITLIST[1]=1
                       text0 = Text(text="O",color=(0,0,0),position=(0,600),font_size=30,anchor='center')
                       text1 = Text(text="O",color=(0,0,0),position=(1024,600),font_size=30,anchor='center')
                       viewportTEXT = VisionEgg.Core.Viewport(screen=screen, size=screen.size, stimuli=[text0, text1])
                       VisionEgg.Core.swap_buffers()
                       screen.clear()
                       viewport.draw()
                       viewportmasks.draw()
                       viewportTEXT.draw()
                       VisionEgg.Core.swap_buffers()
                elif x >= 1008 and x <=1024 and y >= 0 and y <=16:
                    if EXITLIST==[1,1,0]:
                        ScreenNumber, RESET = ESCAPEscreenLATE(ScreenNumber, RESET)
###  ###   ###  # #     ### ALWAYS REMEMBER TO UPDATE THE RETURN INFO!  ##   #   #   #####  ##  ###    ### ### 
                        return ScreenNumber, TrialTime, RESPONSE, ERRORS, RESET
                        StartTrial=True



####################################################################################################
####################################################################################################
####################################################################################################
####################################################################################################
####################################################################################################
def PICKtheJwordAGAIN(ScreenNumber, TrialTime, ERRORS, RESPONSE, RESET):
    x=-1
    y=-1
    #reset variables
    EXITLIST=[0,0,0]
    ANSWERED=0
    RESPONSE=" "
    Choice=[" "]
    ERRORS=0
    #make and show background
    backgroundIMAGE = TextureStimulus(texture=taskbackgrounds[10],position=(0,0))
    viewport = VisionEgg.Core.Viewport(screen=screen, size=screen.size, stimuli=[backgroundIMAGE])
    warnBOX = TextureStimulus(texture=notyetboxes[11],position=(830,150), anchor='center', max_alpha=0.80)
    viewportwarnBOX = VisionEgg.Core.Viewport(screen=screen, size=screen.size, stimuli=[warnBOX])
    useTHISmask=masks[0]
    maskblue = TextureStimulus(texture=useTHISmask,position=(-100,-100), anchor='center', max_alpha=0.50)    
    MASKLIST=[maskblue]
     ## we'll modify the MASKLIST depending on button presses....
    viewportmasks = VisionEgg.Core.Viewport(screen=screen, size=screen.size, stimuli=MASKLIST)
    screen.clear()
    viewport.draw()
    VisionEgg.Core.swap_buffers()
    screen.clear()
    viewport.draw()
    VisionEgg.Core.swap_buffers()
    # start clock
    startTIME=int(round(time() * 1000))
    StartTrial=False
    while not StartTrial:
        for event in pygame.event.get():
            if event.type == pygame.locals.MOUSEBUTTONDOWN:
                if (int(round(time() * 1000))-startTIME) > 100:
                    x,y = pygame.mouse.get_pos()
## pygame.mouse.get_pos() gives coordinates with the LOWER LEFT, not UPPER LEFT (as in visionegg) corner as the origin.
## before we get too complicated, will probably want to flip things around:
                y=600-y
                if x >= 930 and x <=1024 and y >=36 and y <=71:
                    EXITLIST=[0,0,0]
                    ## the "touch here when done" box. Action depends on ANSWERED
                    if ANSWERED == 1 and not Choice[0]==" ":
                        ## trial time is in seconds
                        RESPONSE=Choice[0]
                        #RESPONSE=Choice
                        TrialTime=int(round(time() * 1000))-startTIME
                        #YearAnswer=int(NUMBERBANK[0]+NUMBERBANK[1]+NUMBERBANK[2]+NUMBERBANK[3])
                        return ScreenNumber, TrialTime, ERRORS, RESPONSE, RESET
                        StartTrial=True                       
                    else:
                        ERRORS=ERRORS+1
                        screen.clear()
                        viewport.draw()
                        viewportmasks.draw()
                        #show the warning box, since this is a "practice" screen
                        viewportwarnBOX.draw()
                        VisionEgg.Core.swap_buffers()
                        #it'll stay up until something else is clicked


                elif x >= 351  and x <= 507  and y <= 419 and y >=360:
                    EXITLIST=[0,0,0]
                    if Choice[0]=="Acid":
                        # if already selected, unselect and move pertinent mask offscreen
                        maskblue = TextureStimulus(texture=useTHISmask,position=(-200,-200), anchor='upperleft', max_alpha=0.50)
                        MASKLIST[0]=maskblue
                        Choice[0]=" "
                        ANSWERED=0
                    else:
                        # otherwise, select and move pertinent mask over the word
                        maskblue = TextureStimulus(texture=useTHISmask,position=(351,419), anchor='upperleft', max_alpha=0.50)
                        MASKLIST[0]=maskblue
                        Choice[0]="Acid"
                        ANSWERED=1
                    screen.clear()
                    viewport.draw()
                    viewportmasks.draw()
                    VisionEgg.Core.swap_buffers()
                elif x >= 351  and x <= 507  and y <= 352  and y >=293 :
                   ## DIME
                    EXITLIST=[0,0,0]
                    if Choice[0]=="Dime":
                        # if already selected, unselect and move pertinent mask offscreen
                        maskblue = TextureStimulus(texture=useTHISmask,position=(-200,-200), anchor='upperleft', max_alpha=0.50)
                        MASKLIST[0]=maskblue
                        Choice[0]=" "
                        ANSWERED=0
                    else:
                        # otherwise, select and move pertinent mask over the word
                        maskblue = TextureStimulus(texture=useTHISmask,position=(351,352), anchor='upperleft', max_alpha=0.50)
                        MASKLIST[0]=maskblue
                        Choice[0]="Dime"
                        ANSWERED=1
                    screen.clear()
                    viewport.draw()
                    viewportmasks.draw()
                    VisionEgg.Core.swap_buffers()
                elif x >= 351  and x <= 507  and y <= 285  and y >=226 :
                  ## FARM
                    EXITLIST=[0,0,0]
                    if Choice[0]=="Farm":
                        # if already selected, unselect and move pertinent mask offscreen
                        maskblue = TextureStimulus(texture=useTHISmask,position=(-200,-200), anchor='upperleft', max_alpha=0.50)
                        MASKLIST[0]=maskblue
                        Choice[0]=" "
                        ANSWERED=0
                    else:
                        # otherwise, select and move pertinent mask over the word
                        maskblue = TextureStimulus(texture=useTHISmask,position=(351,285), anchor='upperleft', max_alpha=0.50)
                        MASKLIST[0]=maskblue
                        Choice[0]="Farm"
                        ANSWERED=1
                    screen.clear()
                    viewport.draw()
                    viewportmasks.draw()
                    VisionEgg.Core.swap_buffers()
                elif x >= 351  and x <= 507  and y <= 220  and y >=159 :
                  ## GOLD
                    EXITLIST=[0,0,0]
                    if Choice[0]=="Gold":
                        # if already selected, unselect and move pertinent mask offscreen
                        maskblue = TextureStimulus(texture=useTHISmask,position=(-200,-200), anchor='upperleft', max_alpha=0.50)
                        MASKLIST[0]=maskblue
                        Choice[0]=" "
                        ANSWERED=0
                    else:
                        # otherwise, select and move pertinent mask over the word
                        maskblue = TextureStimulus(texture=useTHISmask,position=(351,219), anchor='upperleft', max_alpha=0.50)
                        MASKLIST[0]=maskblue
                        Choice[0]="Gold"
                        ANSWERED=1
                    screen.clear()
                    viewport.draw()
                    viewportmasks.draw()
                    VisionEgg.Core.swap_buffers()
                elif x >= 351  and x <= 507  and y <= 153  and y >=92 :
                  ## JAZZ
                    EXITLIST=[0,0,0]
                    if Choice[0]=="Hat":
                        # if already selected, unselect and move pertinent mask offscreen
                        maskblue = TextureStimulus(texture=useTHISmask,position=(-200,-200), anchor='upperleft', max_alpha=0.50)
                        MASKLIST[0]=maskblue
                        Choice[0]=" "
                        ANSWERED=0
                    else:
                        # otherwise, select and move pertinent mask over the word
                        maskblue = TextureStimulus(texture=useTHISmask,position=(351,153), anchor='upperleft', max_alpha=0.50)
                        MASKLIST[0]=maskblue
                        Choice[0]="Hat"
                        ANSWERED=1
                    screen.clear()
                    viewport.draw()
                    viewportmasks.draw()
                    VisionEgg.Core.swap_buffers()

                elif x >= 516  and x <= 671  and y <= 419  and y >=360 :
                  ## KNOT
                    EXITLIST=[0,0,0]
                    if Choice[0]=="Jazz":
                        # if already selected, unselect and move pertinent mask offscreen
                        maskblue = TextureStimulus(texture=useTHISmask,position=(-200,-200), anchor='upperleft', max_alpha=0.50)
                        MASKLIST[0]=maskblue
                        Choice[0]=" "
                        ANSWERED=0
                    else:
                        # otherwise, select and move pertinent mask over the word
                        maskblue = TextureStimulus(texture=useTHISmask,position=(516,419), anchor='upperleft', max_alpha=0.50)
                        MASKLIST[0]=maskblue
                        Choice[0]="Jazz"
                        ANSWERED=1
                    screen.clear()
                    viewport.draw()
                    viewportmasks.draw()
                    VisionEgg.Core.swap_buffers()
                elif x >= 516  and x <= 671  and y <= 352  and y >=293 :
                  ## KNOT
                    EXITLIST=[0,0,0]
                    if Choice[0]=="Knot":
                        # if already selected, unselect and move pertinent mask offscreen
                        maskblue = TextureStimulus(texture=useTHISmask,position=(-200,-200), anchor='upperleft', max_alpha=0.50)
                        MASKLIST[0]=maskblue
                        Choice[0]=" "
                        ANSWERED=0
                    else:
                        # otherwise, select and move pertinent mask over the word
                        maskblue = TextureStimulus(texture=useTHISmask,position=(516,352), anchor='upperleft', max_alpha=0.50)
                        MASKLIST[0]=maskblue
                        Choice[0]="Knot"
                        ANSWERED=1
                    screen.clear()
                    viewport.draw()
                    viewportmasks.draw()
                    VisionEgg.Core.swap_buffers()
                elif x >= 516  and x <= 671  and y <= 285  and y >=226 :
                  ## SHOE
                    EXITLIST=[0,0,0]
                    if Choice[0]=="Shoe":
                        # if already selected, unselect and move pertinent mask offscreen
                        maskblue = TextureStimulus(texture=useTHISmask,position=(-200,-200), anchor='upperleft', max_alpha=0.50)
                        MASKLIST[0]=maskblue
                        Choice[0]=" "
                        ANSWERED=0
                    else:
                        # otherwise, select and move pertinent mask over the word
                        maskblue = TextureStimulus(texture=useTHISmask,position=(516,285), anchor='upperleft', max_alpha=0.50)
                        MASKLIST[0]=maskblue
                        Choice[0]="Shoe"
                        ANSWERED=1
                    screen.clear()
                    viewport.draw()
                    viewportmasks.draw()
                    VisionEgg.Core.swap_buffers()
                elif x >= 516  and x <= 671  and y <= 220  and y >=159 :
                  ## TREE
                    EXITLIST=[0,0,0]
                    if Choice[0]=="Tree":
                        # if already selected, unselect and move pertinent mask offscreen
                        maskblue = TextureStimulus(texture=useTHISmask,position=(-200,-200), anchor='upperleft', max_alpha=0.50)
                        MASKLIST[0]=maskblue
                        Choice[0]=" "
                        ANSWERED=0
                    else:
                        # otherwise, select and move pertinent mask over the word
                        maskblue = TextureStimulus(texture=useTHISmask,position=(516,219), anchor='upperleft', max_alpha=0.50)
                        MASKLIST[0]=maskblue
                        Choice[0]="Tree"
                        ANSWERED=1
                    screen.clear()
                    viewport.draw()
                    viewportmasks.draw()
                    VisionEgg.Core.swap_buffers()
                elif x >= 516  and x <= 671  and y <= 153  and y >=92 :
                  ## WOLF
                    EXITLIST=[0,0,0]
                    if Choice[0]=="Wolf":
                        # if already selected, unselect and move pertinent mask offscreen
                        maskblue = TextureStimulus(texture=useTHISmask,position=(-200,-200), anchor='upperleft', max_alpha=0.50)
                        MASKLIST[0]=maskblue
                        Choice[0]=" "
                        ANSWERED=0
                    else:
                        # otherwise, select and move pertinent mask over the word
                        maskblue = TextureStimulus(texture=useTHISmask,position=(516,153), anchor='upperleft', max_alpha=0.50)
                        MASKLIST[0]=maskblue
                        Choice[0]="Wolf"
                        ANSWERED=1
                    screen.clear()
                    viewport.draw()
                    viewportmasks.draw()
                    VisionEgg.Core.swap_buffers()
                ##
                ## now we see the practical application of the EXITLIST:
                elif x >= 0 and x <=24 and y >= 584 and y <=600:
                   if EXITLIST==[0,0,0]:
                       EXITLIST[0]=1
                       text0 = Text(text="O",color=(0,0,0),position=(0,600),font_size=30,anchor='center')
                       text1 = Text(text="O",color=(0,0,0),position=(0,600),font_size=30,anchor='center')
                       viewportTEXT = VisionEgg.Core.Viewport(screen=screen, size=screen.size, stimuli=[text0, text1])
                       VisionEgg.Core.swap_buffers()
                       screen.clear()
                       viewport.draw()
                       viewportmasks.draw()
                       viewportTEXT.draw()
                       VisionEgg.Core.swap_buffers()
                elif x >= 1008 and x <=1024 and y >= 584 and y <=600:
                    if EXITLIST==[1,0,0]:
                       EXITLIST[1]=1
                       text0 = Text(text="O",color=(0,0,0),position=(0,600),font_size=30,anchor='center')
                       text1 = Text(text="O",color=(0,0,0),position=(1024,600),font_size=30,anchor='center')
                       viewportTEXT = VisionEgg.Core.Viewport(screen=screen, size=screen.size, stimuli=[text0, text1])
                       VisionEgg.Core.swap_buffers()
                       screen.clear()
                       viewport.draw()
                       viewportmasks.draw()
                       viewportTEXT.draw()
                       VisionEgg.Core.swap_buffers()
                elif x >= 1008 and x <=1024 and y >= 0 and y <=16:
                    if EXITLIST==[1,1,0]:
                        ScreenNumber, RESET = ESCAPEscreenLATE(ScreenNumber, RESET)
###  ###   ###  # #     ### ALWAYS REMEMBER TO UPDATE THE RETURN INFO!  ##   #   #   #####  ##  ###    ### ### 
                        return ScreenNumber, TrialTime, ERRORS, Choice, RESET
                        StartTrial=True


####################################################################################################
####################################################################################################
####################################################################################################
####################################################################################################
####################################################################################################
def NUMBERPADagain(ScreenNumber, TrialTime, ERRORS, RESPONSE, RESET):
    x=-1
    y=-1
    EXITLIST=[0,0,0]
    POSITION=0 # which of the four number positions are we at? (in NUMBERBANK)
    ERRORS=0
    TrialTime=-1
    NUMBERBANK=[" "," "," "," "]
    text0 = Text(text=NUMBERBANK[0],
                 color=(0,0.5,0),
                 position=(408,450), 
                 font_size=60,
                 anchor='center')
    text1 = Text(text=NUMBERBANK[1],
                 color=(0,0,0),
                 position=(477,450),
                 font_size=60,
                 anchor='center')
    text2 = Text(text=NUMBERBANK[2],
                 color=(0,0,0),
                 position=(546,450),
                 font_size=60,
                 anchor='center')
    text3 = Text(text=NUMBERBANK[3],
                 color=(0,0,0),
                 position=(615,450),
                 font_size=60,
                 anchor='center')
    warnBOX = TextureStimulus(texture=notyetboxes[10],position=(830,150), anchor='center', max_alpha=0.80)
    viewportwarnBOX = VisionEgg.Core.Viewport(screen=screen, size=screen.size, stimuli=[warnBOX])
    backgroundIMAGE = TextureStimulus(texture=taskbackgrounds[9],position=(0,0))
    viewport = VisionEgg.Core.Viewport(screen=screen, size=screen.size, stimuli=[backgroundIMAGE])
    viewportTEXT2 = VisionEgg.Core.Viewport(screen=screen, size=screen.size, stimuli=[text0, text1, text2, text3])
    #VisionEgg.Core.swap_buffers()
    screen.clear()
    viewport.draw()
    LASTTAP=0
    viewportTEXT2.draw()
    VisionEgg.Core.swap_buffers()
    StartTrial=False
    startTIME=int(round(time() * 1000))
    screen.clear()
    viewport.draw()
    viewportTEXT2.draw()
    VisionEgg.Core.swap_buffers()
    while not StartTrial:
        for event in pygame.event.get():
            if event.type == pygame.locals.MOUSEBUTTONDOWN:
                if (int(round(time() * 1000))-startTIME) > 100:
                    x,y = pygame.mouse.get_pos()
## pygame.mouse.get_pos() gives coordinates with the LOWER LEFT, not UPPER LEFT (as in visionegg) corner as the origin.
## before we get too complicated, will probably want to flip things around:
                y=600-y
                if x >= 904  and x <= 997  and y >= 0  and y <=36 :
                    EXITLIST=[0,0,0]
                    if NUMBERBANK[0] != " ":
                        MOTOR_SPEED_LOG.append(int((round(time() * 1000))-startTIME)-LASTTAP)
                        LASTTAP=int((round(time() * 1000))-startTIME)
                    ## the "touch here when done" box. Action depends on whether there's a full answer.
                    if POSITION == 3 and not NUMBERBANK[3] == " ":
                        out_file.write('   NEXT_at_ms %d NA NA NA 3\n'%(int(round(time() * 1000))-startTIME))
                        RESPONSE=int(NUMBERBANK[0]+NUMBERBANK[1]+NUMBERBANK[2]+NUMBERBANK[3])
                        TrialTime=int(round(time() * 1000))-startTIME
                        return ScreenNumber, TrialTime, ERRORS, RESPONSE, RESET
                        StartTrial=True                       
                    else:
                        out_file.write('   NEXT_at_ms %d NA NA NA 3\n'%(int(round(time() * 1000))-startTIME))
                        ERRORS=ERRORS+1
                        screen.clear()
                        viewport.draw()
                        viewportTEXT2.draw()
                        viewportwarnBOX.draw()
                        VisionEgg.Core.swap_buffers()
  
                        
                elif x >= 406 and x <=474 and y >=322 and y <=386:
                    MOTOR_SPEED_LOG.append(int((round(time() * 1000))-startTIME)-LASTTAP)
                    LASTTAP=int((round(time() * 1000))-startTIME)
                    EXITLIST=[0,0,0]
                    ## button 1
                    NUMBERBANK[POSITION]="1"
                    out_file.write('   button1_at_ms %d NA NA NA 3\n'%(int(round(time() * 1000))-startTIME))
                    screen.clear()
                    text0 = Text(text=NUMBERBANK[0],color=(0,0,0),position=(408,450),font_size=60,anchor='center')
                    text1 = Text(text=NUMBERBANK[1],color=(0,0,0),position=(477,450),font_size=60,anchor='center')
                    text2 = Text(text=NUMBERBANK[2],color=(0,0,0),position=(546,450),font_size=60,anchor='center')
                    text3 = Text(text=NUMBERBANK[3],color=(0,0,0),position=(615,450),font_size=60,anchor='center')
                    viewportTEXT2 = VisionEgg.Core.Viewport(screen=screen, size=screen.size, stimuli=[text0, text1, text2, text3])
                    viewport.draw()
                    viewportTEXT2.draw()
                    VisionEgg.Core.swap_buffers()
                    if POSITION < 3:
                        ## advance position
                        POSITION=POSITION+1
                elif x >= 406 and x <=474 and y >=251 and y <=314:
                    MOTOR_SPEED_LOG.append(int((round(time() * 1000))-startTIME)-LASTTAP)
                    LASTTAP=int((round(time() * 1000))-startTIME)
                    EXITLIST=[0,0,0]
                    ## button 4
                    NUMBERBANK[POSITION]="4"
                    out_file.write('   button4_at_ms %d NA NA NA 3\n'%(int(round(time() * 1000))-startTIME))
                    screen.clear()
                    text0 = Text(text=NUMBERBANK[0],color=(0,0,0),position=(408,450),font_size=60,anchor='center')
                    text1 = Text(text=NUMBERBANK[1],color=(0,0,0),position=(477,450),font_size=60,anchor='center')
                    text2 = Text(text=NUMBERBANK[2],color=(0,0,0),position=(546,450),font_size=60,anchor='center')
                    text3 = Text(text=NUMBERBANK[3],color=(0,0,0),position=(615,450),font_size=60,anchor='center')
                    viewportTEXT2 = VisionEgg.Core.Viewport(screen=screen, size=screen.size, stimuli=[text0, text1, text2, text3])
                    viewport.draw()
                    viewportTEXT2.draw()
                    VisionEgg.Core.swap_buffers()
                    if POSITION < 3:
                        ## advance position
                        POSITION=POSITION+1
                elif x >= 406 and x <=474 and y >=180 and y <=245:
                    MOTOR_SPEED_LOG.append(int((round(time() * 1000))-startTIME)-LASTTAP)
                    LASTTAP=int((round(time() * 1000))-startTIME)
                    EXITLIST=[0,0,0]
                    ## button 7
                    NUMBERBANK[POSITION]="7"
                    out_file.write('   button7_at_ms %d NA NA NA 3\n'%(int(round(time() * 1000))-startTIME))
                    screen.clear()
                    text0 = Text(text=NUMBERBANK[0],color=(0,0,0),position=(408,450),font_size=60,anchor='center')
                    text1 = Text(text=NUMBERBANK[1],color=(0,0,0),position=(477,450),font_size=60,anchor='center')
                    text2 = Text(text=NUMBERBANK[2],color=(0,0,0),position=(546,450),font_size=60,anchor='center')
                    text3 = Text(text=NUMBERBANK[3],color=(0,0,0),position=(615,450),font_size=60,anchor='center')
                    viewportTEXT2 = VisionEgg.Core.Viewport(screen=screen, size=screen.size, stimuli=[text0, text1, text2, text3])
                    viewport.draw()
                    viewportTEXT2.draw()
                    VisionEgg.Core.swap_buffers()
                    if POSITION < 3:
                        ## advance position
                        POSITION=POSITION+1
                    
                elif x >= 479 and x <=546 and y >=109 and y <=174:
                    MOTOR_SPEED_LOG.append(int((round(time() * 1000))-startTIME)-LASTTAP)
                    LASTTAP=int((round(time() * 1000))-startTIME)
                    EXITLIST=[0,0,0]
                    ## button 0
                    NUMBERBANK[POSITION]="0"
                    out_file.write('   button0_at_ms %d NA NA NA 3\n'%(int(round(time() * 1000))-startTIME))
                    screen.clear()
                    text0 = Text(text=NUMBERBANK[0],color=(0,0,0),position=(408,450),font_size=60,anchor='center')
                    text1 = Text(text=NUMBERBANK[1],color=(0,0,0),position=(477,450),font_size=60,anchor='center')
                    text2 = Text(text=NUMBERBANK[2],color=(0,0,0),position=(546,450),font_size=60,anchor='center')
                    text3 = Text(text=NUMBERBANK[3],color=(0,0,0),position=(615,450),font_size=60,anchor='center')
                    viewportTEXT2 = VisionEgg.Core.Viewport(screen=screen, size=screen.size, stimuli=[text0, text1, text2, text3])
                    viewport.draw()
                    viewportTEXT2.draw()
                    VisionEgg.Core.swap_buffers()
                    if POSITION < 3:
                        ## advance position
                        POSITION=POSITION+1

                elif x >= 479 and x <=546 and y >=322 and y <=386:
                    MOTOR_SPEED_LOG.append(int((round(time() * 1000))-startTIME)-LASTTAP)
                    LASTTAP=int((round(time() * 1000))-startTIME)
                    EXITLIST=[0,0,0]
                    ## button 2
                    NUMBERBANK[POSITION]="2"
                    out_file.write('   button2_at_ms %d NA NA NA 3\n'%(int(round(time() * 1000))-startTIME))
                    screen.clear()
                    text0 = Text(text=NUMBERBANK[0],color=(0,0,0),position=(408,450),font_size=60,anchor='center')
                    text1 = Text(text=NUMBERBANK[1],color=(0,0,0),position=(477,450),font_size=60,anchor='center')
                    text2 = Text(text=NUMBERBANK[2],color=(0,0,0),position=(546,450),font_size=60,anchor='center')
                    text3 = Text(text=NUMBERBANK[3],color=(0,0,0),position=(615,450),font_size=60,anchor='center')
                    viewportTEXT2 = VisionEgg.Core.Viewport(screen=screen, size=screen.size, stimuli=[text0, text1, text2, text3])
                    viewport.draw()
                    viewportTEXT2.draw()
                    VisionEgg.Core.swap_buffers()
                    if POSITION < 3:
                        ## advance position
                        POSITION=POSITION+1
                elif x >= 479 and x <=546 and y >=251 and y <=314:
                    MOTOR_SPEED_LOG.append(int((round(time() * 1000))-startTIME)-LASTTAP)
                    LASTTAP=int((round(time() * 1000))-startTIME)
                    EXITLIST=[0,0,0]
                    ## button 5
                    NUMBERBANK[POSITION]="5"
                    out_file.write('   button5_at_ms %d NA NA NA 3\n'%(int(round(time() * 1000))-startTIME))
                    screen.clear()
                    text0 = Text(text=NUMBERBANK[0],color=(0,0,0),position=(408,450),font_size=60,anchor='center')
                    text1 = Text(text=NUMBERBANK[1],color=(0,0,0),position=(477,450),font_size=60,anchor='center')
                    text2 = Text(text=NUMBERBANK[2],color=(0,0,0),position=(546,450),font_size=60,anchor='center')
                    text3 = Text(text=NUMBERBANK[3],color=(0,0,0),position=(615,450),font_size=60,anchor='center')
                    viewportTEXT2 = VisionEgg.Core.Viewport(screen=screen, size=screen.size, stimuli=[text0, text1, text2, text3])
                    viewport.draw()
                    viewportTEXT2.draw()
                    VisionEgg.Core.swap_buffers()
                    if POSITION < 3:
                        ## advance position
                        POSITION=POSITION+1
                elif x >= 479 and x <=546 and y >=180 and y <=245:
                    MOTOR_SPEED_LOG.append(int((round(time() * 1000))-startTIME)-LASTTAP)
                    LASTTAP=int((round(time() * 1000))-startTIME)
                    EXITLIST=[0,0,0]
                    ## button 8
                    NUMBERBANK[POSITION]="8"
                    out_file.write('   button8_at_ms %d NA NA NA 3\n'%(int(round(time() * 1000))-startTIME))
                    screen.clear()
                    text0 = Text(text=NUMBERBANK[0],color=(0,0,0),position=(408,450),font_size=60,anchor='center')
                    text1 = Text(text=NUMBERBANK[1],color=(0,0,0),position=(477,450),font_size=60,anchor='center')
                    text2 = Text(text=NUMBERBANK[2],color=(0,0,0),position=(546,450),font_size=60,anchor='center')
                    text3 = Text(text=NUMBERBANK[3],color=(0,0,0),position=(615,450),font_size=60,anchor='center')
                    viewportTEXT2 = VisionEgg.Core.Viewport(screen=screen, size=screen.size, stimuli=[text0, text1, text2, text3])
                    viewport.draw()
                    viewportTEXT2.draw()
                    VisionEgg.Core.swap_buffers()
                    if POSITION < 3:
                        ## advance position
                        POSITION=POSITION+1

                elif x >= 552 and x <=620 and y >=322 and y <=386:
                    MOTOR_SPEED_LOG.append(int((round(time() * 1000))-startTIME)-LASTTAP)
                    LASTTAP=int((round(time() * 1000))-startTIME)
                    EXITLIST=[0,0,0]
                    ## button 3
                    NUMBERBANK[POSITION]="3"
                    out_file.write('   button3_at_ms %d NA NA NA 3\n'%(int(round(time() * 1000))-startTIME))
                    screen.clear()
                    text0 = Text(text=NUMBERBANK[0],color=(0,0,0),position=(408,450),font_size=60,anchor='center')
                    text1 = Text(text=NUMBERBANK[1],color=(0,0,0),position=(477,450),font_size=60,anchor='center')
                    text2 = Text(text=NUMBERBANK[2],color=(0,0,0),position=(546,450),font_size=60,anchor='center')
                    text3 = Text(text=NUMBERBANK[3],color=(0,0,0),position=(615,450),font_size=60,anchor='center')
                    viewportTEXT2 = VisionEgg.Core.Viewport(screen=screen, size=screen.size, stimuli=[text0, text1, text2, text3])
                    viewport.draw()
                    viewportTEXT2.draw()
                    VisionEgg.Core.swap_buffers()
                    if POSITION < 3:
                        ## advance position
                        POSITION=POSITION+1
                elif x >= 552 and x <=620 and y >=251 and y <=314:
                    MOTOR_SPEED_LOG.append(int((round(time() * 1000))-startTIME)-LASTTAP)
                    LASTTAP=int((round(time() * 1000))-startTIME)
                    EXITLIST=[0,0,0]
                    ## button 6
                    NUMBERBANK[POSITION]="6"
                    out_file.write('   button6_at_ms %d NA NA NA 3\n'%(int(round(time() * 1000))-startTIME))
                    screen.clear()
                    text0 = Text(text=NUMBERBANK[0],color=(0,0,0),position=(408,450),font_size=60,anchor='center')
                    text1 = Text(text=NUMBERBANK[1],color=(0,0,0),position=(477,450),font_size=60,anchor='center')
                    text2 = Text(text=NUMBERBANK[2],color=(0,0,0),position=(546,450),font_size=60,anchor='center')
                    text3 = Text(text=NUMBERBANK[3],color=(0,0,0),position=(615,450),font_size=60,anchor='center')
                    viewportTEXT2 = VisionEgg.Core.Viewport(screen=screen, size=screen.size, stimuli=[text0, text1, text2, text3])
                    viewport.draw()
                    viewportTEXT2.draw()
                    VisionEgg.Core.swap_buffers()
                    if POSITION < 3:
                        ## advance position
                        POSITION=POSITION+1
                elif x >= 552 and x <=620 and y >=180 and y <=245:
                    MOTOR_SPEED_LOG.append(int((round(time() * 1000))-startTIME)-LASTTAP)
                    LASTTAP=int((round(time() * 1000))-startTIME)
                    EXITLIST=[0,0,0]
                    ## button 9
                    NUMBERBANK[POSITION]="9"
                    out_file.write('   button9_at_ms %d NA NA NA 3\n'%(int(round(time() * 1000))-startTIME))
                    screen.clear()
                    text0 = Text(text=NUMBERBANK[0],color=(0,0,0),position=(408,450),font_size=60,anchor='center')
                    text1 = Text(text=NUMBERBANK[1],color=(0,0,0),position=(477,450),font_size=60,anchor='center')
                    text2 = Text(text=NUMBERBANK[2],color=(0,0,0),position=(546,450),font_size=60,anchor='center')
                    text3 = Text(text=NUMBERBANK[3],color=(0,0,0),position=(615,450),font_size=60,anchor='center')
                    viewportTEXT2 = VisionEgg.Core.Viewport(screen=screen, size=screen.size, stimuli=[text0, text1, text2, text3])
                    viewport.draw()
                    viewportTEXT2.draw()
                    VisionEgg.Core.swap_buffers()
                    if POSITION < 3:
                        ## advance position
                        POSITION=POSITION+1
 
                elif x >= 419 and x <=609 and y >=40 and y <=94:
                    MOTOR_SPEED_LOG.append(int((round(time() * 1000))-startTIME)-LASTTAP)
                    LASTTAP=int((round(time() * 1000))-startTIME)
                    EXITLIST=[0,0,0]
                    out_file.write('   buttonDELETE_at_ms %d NA NA NA 3\n'%(int(round(time() * 1000))-startTIME))
                    ## DELETE button
                    ## if POSITION == 0, do nothing. This means there are no numbers
                    ## if POSITION == 1, you just wrote your first number (in POSITION 0) and then shifted over
                    ##  OR, you were in POSITION 2 ready to write there, but instead hit delete, which made you step back
                    ##  a position and wipe the value in NUMBERBANK[1].
                    ##  either way, if POSITION == 1, we want to wipe NUMBERBANK[0] and set POSITION to 0
                    if POSITION > 0:
                        if POSITION == 3 and NUMBERBANK[3] != " ":
                            NUMBERBANK[POSITION]=" "
                        else:
                            POSITION=POSITION-1
                            NUMBERBANK[POSITION]=" "                            
                        screen.clear()
                        text0 = Text(text=NUMBERBANK[0],color=(0,0,0),position=(408,450),font_size=60,anchor='center')
                        text1 = Text(text=NUMBERBANK[1],color=(0,0,0),position=(477,450),font_size=60,anchor='center')
                        text2 = Text(text=NUMBERBANK[2],color=(0,0,0),position=(546,450),font_size=60,anchor='center')
                        text3 = Text(text=NUMBERBANK[3],color=(0,0,0),position=(615,450),font_size=60,anchor='center')
                        viewportTEXT2 = VisionEgg.Core.Viewport(screen=screen, size=screen.size, stimuli=[text0, text1, text2, text3])
                        viewport.draw()
                        viewportTEXT2.draw()
                        VisionEgg.Core.swap_buffers()
                ##
                ## now we see the practical application of the EXITLIST:
                elif x >= 0 and x <=24 and y >= 584 and y <=600:
                   if EXITLIST==[0,0,0]:
                       EXITLIST[0]=1
                       text0 = Text(text="O",color=(0,0,0),position=(0,600),font_size=30,anchor='center')
                       text1 = Text(text="O",color=(0,0,0),position=(0,600),font_size=30,anchor='center')
                       viewportTEXT = VisionEgg.Core.Viewport(screen=screen, size=screen.size, stimuli=[text0, text1])
                       VisionEgg.Core.swap_buffers()
                       screen.clear()
                       viewport.draw()
                       viewportTEXT2.draw()
                       viewportTEXT.draw()
                       VisionEgg.Core.swap_buffers()
                elif x >= 1008 and x <=1024 and y >= 584 and y <=600:
                    if EXITLIST==[1,0,0]:
                       EXITLIST[1]=1
                       text0 = Text(text="O",color=(0,0,0),position=(0,600),font_size=30,anchor='center')
                       text1 = Text(text="O",color=(0,0,0),position=(1024,600),font_size=30,anchor='center')
                       viewportTEXT = VisionEgg.Core.Viewport(screen=screen, size=screen.size, stimuli=[text0, text1])
                       VisionEgg.Core.swap_buffers()
                       screen.clear()
                       viewport.draw()
                       viewportTEXT2.draw()
                       viewportTEXT.draw()
                       VisionEgg.Core.swap_buffers()
                elif x >= 1008 and x <=1024 and y >= 0 and y <=16:
                    if EXITLIST==[1,1,0]:
                        ScreenNumber, RESET = ESCAPEscreenLATE(ScreenNumber, RESET)
###  ###   ###  # #     ### ALWAYS REMEMBER TO UPDATE THE RETURN INFO!  ##   #   #   #####  ##  ###    ### ### 
                        return ScreenNumber, TrialTime, ERRORS, RESPONSE, RESET
                        StartTrial=True



####################################################################################################
####################################################################################################
####################################################################################################
####################################################################################################
####################################################################################################

                        

#<$%^>
####################################################################################################
####################################################################################################
def STATEselection(ScreenNumber, TrialTime, RESPONSE, ERRORS, RESET):
    x=-1
    y=-1
    #make and show background
    backgroundIMAGE = TextureStimulus(texture=STATE_SELECTION_BACKGROUND,position=(0,0))
    viewport = VisionEgg.Core.Viewport(screen=screen, size=screen.size, stimuli=[backgroundIMAGE])
    warnBOX = TextureStimulus(texture=notyetboxes[7],position=(830,150), anchor='center', max_alpha=0.90)
    viewportwarnBOX = VisionEgg.Core.Viewport(screen=screen, size=screen.size, stimuli=[warnBOX])
    useTHISmask=STATE_SELECTION_BLUEBOX
    maskblue = TextureStimulus(texture=useTHISmask,position=(-100,-100), anchor='center', max_alpha=0.50)    
    MASKLIST=[maskblue]
     ## we'll modify the MASKLIST depending on button presses....
    viewportmasks = VisionEgg.Core.Viewport(screen=screen, size=screen.size, stimuli=MASKLIST)
    ##
    EXITLIST=[0,0,0]
    ANSWERED=0
    RESPONSE=" "
    ERRORS=0
    ##
    CURRENTLIST=list_states_for_selecting_current_state
##    t101 = Text(text=CURRENTLIST[0],color=(0,0,0),position=(56,541),font_size=42,anchor='upperleft')
##    t102 = Text(text=CURRENTLIST[1],color=(0,0,0),position=(56,511),font_size=42,anchor='upperleft')
##    t103 = Text(text=CURRENTLIST[2],color=(0,0,0),position=(56,481),font_size=42,anchor='upperleft')
##    t104 = Text(text=CURRENTLIST[3],color=(0,0,0),position=(56,451),font_size=42,anchor='upperleft')
##    t105 = Text(text=CURRENTLIST[4],color=(0,0,0),position=(56,421),font_size=42,anchor='upperleft')
##    t106 = Text(text=CURRENTLIST[5],color=(0,0,0),position=(56,391),font_size=42,anchor='upperleft')
##    t107 = Text(text=CURRENTLIST[6],color=(0,0,0),position=(56,361),font_size=42,anchor='upperleft')
##    t108 = Text(text=CURRENTLIST[7],color=(0,0,0),position=(56,331),font_size=42,anchor='upperleft')
##    t109 = Text(text=CURRENTLIST[8],color=(0,0,0),position=(56,301),font_size=42,anchor='upperleft')
##    t110 = Text(text=CURRENTLIST[9],color=(0,0,0),position=(56,270),font_size=42,anchor='upperleft')
##    t111 = Text(text=CURRENTLIST[10],color=(0,0,0),position=(56,241),font_size=42,anchor='upperleft')
##    t112 = Text(text=CURRENTLIST[11],color=(0,0,0),position=(56,211),font_size=42,anchor='upperleft')
##    t113 = Text(text=CURRENTLIST[12],color=(0,0,0),position=(56,181),font_size=42,anchor='upperleft')
##    t114 = Text(text=CURRENTLIST[13],color=(0,0,0),position=(56,151),font_size=42,anchor='upperleft')
##    t115 = Text(text=CURRENTLIST[14],color=(0,0,0),position=(56,121),font_size=42,anchor='upperleft')
##    t116 = Text(text=CURRENTLIST[15],color=(0,0,0),position=(56,91),font_size=42,anchor='upperleft')
##    t117 = Text(text=CURRENTLIST[16],color=(0,0,0),position=(56,61),font_size=42,anchor='upperleft')
##    t118 = Text(text=CURRENTLIST[17],color=(0,0,0),position=(56,31),font_size=42,anchor='upperleft')
##    #
##    t201 = Text(text=CURRENTLIST[18],color=(0,0,0),position=(367,541),font_size=42,anchor='upperleft')
##    t202 = Text(text=CURRENTLIST[19],color=(0,0,0),position=(367,511),font_size=42,anchor='upperleft')
##    t203 = Text(text=CURRENTLIST[20],color=(0,0,0),position=(367,481),font_size=42,anchor='upperleft')
##    t204 = Text(text=CURRENTLIST[21],color=(0,0,0),position=(367,451),font_size=42,anchor='upperleft')
##    t205 = Text(text=CURRENTLIST[22],color=(0,0,0),position=(367,421),font_size=42,anchor='upperleft')
##    t206 = Text(text=CURRENTLIST[23],color=(0,0,0),position=(367,391),font_size=42,anchor='upperleft')
##    t207 = Text(text=CURRENTLIST[24],color=(0,0,0),position=(367,361),font_size=42,anchor='upperleft')
##    t208 = Text(text=CURRENTLIST[25],color=(0,0,0),position=(367,331),font_size=42,anchor='upperleft')
##    t209 = Text(text=CURRENTLIST[26],color=(0,0,0),position=(367,301),font_size=42,anchor='upperleft')
##    t210 = Text(text=CURRENTLIST[27],color=(0,0,0),position=(367,270),font_size=42,anchor='upperleft')
##    t211 = Text(text=CURRENTLIST[28],color=(0,0,0),position=(367,241),font_size=42,anchor='upperleft')
##    t212 = Text(text=CURRENTLIST[29],color=(0,0,0),position=(367,211),font_size=42,anchor='upperleft')
##    t213 = Text(text=CURRENTLIST[30],color=(0,0,0),position=(367,181),font_size=42,anchor='upperleft')
##    t214 = Text(text=CURRENTLIST[31],color=(0,0,0),position=(367,151),font_size=42,anchor='upperleft')
##    t215 = Text(text=CURRENTLIST[32],color=(0,0,0),position=(367,121),font_size=42,anchor='upperleft')
##    t216 = Text(text=CURRENTLIST[33],color=(0,0,0),position=(367,91),font_size=42,anchor='upperleft')
##    t217 = Text(text=CURRENTLIST[34],color=(0,0,0),position=(367,61),font_size=42,anchor='upperleft')
##    t218 = Text(text=CURRENTLIST[35],color=(0,0,0),position=(367,31),font_size=42,anchor='upperleft')
##    #
##    t301 = Text(text=CURRENTLIST[36],color=(0,0,0),position=(679,541),font_size=42,anchor='upperleft')
##    t302 = Text(text=CURRENTLIST[37],color=(0,0,0),position=(679,511),font_size=42,anchor='upperleft')
##    t303 = Text(text=CURRENTLIST[38],color=(0,0,0),position=(679,481),font_size=42,anchor='upperleft')
##    t304 = Text(text=CURRENTLIST[39],color=(0,0,0),position=(679,451),font_size=42,anchor='upperleft')
##    t305 = Text(text=CURRENTLIST[40],color=(0,0,0),position=(679,421),font_size=42,anchor='upperleft')
##    t306 = Text(text=CURRENTLIST[41],color=(0,0,0),position=(679,391),font_size=42,anchor='upperleft')
##    t307 = Text(text=CURRENTLIST[42],color=(0,0,0),position=(679,361),font_size=42,anchor='upperleft')
##    t308 = Text(text=CURRENTLIST[43],color=(0,0,0),position=(679,331),font_size=42,anchor='upperleft')
##    t309 = Text(text=CURRENTLIST[44],color=(0,0,0),position=(679,301),font_size=42,anchor='upperleft')
##    t310 = Text(text=CURRENTLIST[45],color=(0,0,0),position=(679,270),font_size=42,anchor='upperleft')
##    t311 = Text(text=CURRENTLIST[46],color=(0,0,0),position=(679,241),font_size=42,anchor='upperleft')
##    t312 = Text(text=CURRENTLIST[47],color=(0,0,0),position=(679,211),font_size=42,anchor='upperleft')
##    t313 = Text(text=CURRENTLIST[48],color=(0,0,0),position=(679,181),font_size=42,anchor='upperleft')
##    t314 = Text(text=CURRENTLIST[49],color=(0,0,0),position=(679,151),font_size=42,anchor='upperleft')
##    viewportTEXT2 = VisionEgg.Core.Viewport(screen=screen, size=screen.size, stimuli=[t101,t102,t103,t104,t105,t106,t107,t108,
##                                                                                     t109,t110,t111,t112,t113,t114,t115,t116,
##                                                                                     t117,t118,
##                                                                                     t201,t202,t203,t204,t205,t206,t207,t208,
##                                                                                     t209,t210,t211,t212,t213,t214,t215,t216,
##                                                                                     t217,t218,
##                                                                                     t301,t302,t303,t304,t305,t306,t307,t308,
##                                                                                     t309,t310,t311,t312,t313,t314])
    viewportTEXT2=PREMADE_VIEWPORT_STATES_SELECT
    screen.clear()
    viewport.draw()
    viewportTEXT2.draw()
    VisionEgg.Core.swap_buffers()
    startTIME=int(round(time() * 1000))
    screen.clear()
    viewport.draw()
    viewportTEXT2.draw()
    viewportmasks.draw()
    VisionEgg.Core.swap_buffers()
    StartTrial=False
    while not StartTrial:
        for event in pygame.event.get():
            if event.type == pygame.locals.MOUSEBUTTONDOWN:
                if (int(round(time() * 1000))-startTIME) > 100:
                    x,y = pygame.mouse.get_pos()
## pygame.mouse.get_pos() gives coordinates with the LOWER LEFT, not UPPER LEFT (as in visionegg) corner as the origin.
## before we get too complicated, will probably want to flip things around:
                y=600-y
                if x >= 903 and x <=996 and y >=0 and y <=37:
                    EXITLIST=[0,0,0]
                    ## the "touch here when done" box. Action depends on whether there's a full answer.
                    if ANSWERED == 1 and not RESPONSE == " ":
                        ## trial time is in seconds
                        TrialTime=int(round(time() * 1000))-startTIME
                        return ScreenNumber, TrialTime, RESPONSE, ERRORS, RESET
                        StartTrial=True                       
                    else:
                        ERRORS=ERRORS+1
                        screen.clear()
                        viewport.draw()
                        viewportTEXT2.draw()
                        viewportmasks.draw()
                        viewportwarnBOX.draw() #it'll stay up until something else is clicked
                        VisionEgg.Core.swap_buffers()

                elif x >= 53 and x <= 349 and y <= 544 and y >= 515:
                     ##   col1_row__1
                    EXITLIST=[0,0,0]
                    if RESPONSE==CURRENTLIST[0]:
                        # if already selected, unselect and move pertinent mask offscreen
                        maskblue = TextureStimulus(texture=useTHISmask,position=(-200,-200), anchor='upperleft', max_alpha=0.50)
                        MASKLIST[0]=maskblue
                        RESPONSE=" "
                        ANSWERED=0
                    else:
                        # otherwise, select and move pertinent mask over the word
                        maskblue = TextureStimulus(texture=useTHISmask,position=(54,543), anchor='upperleft', max_alpha=0.50)
                        MASKLIST[0]=maskblue
                        RESPONSE=CURRENTLIST[0]
                        ANSWERED=1
                    screen.clear()
                    viewport.draw()
                    viewportTEXT2.draw()
                    viewportmasks.draw()
                    VisionEgg.Core.swap_buffers()

                elif x >= 53 and x <= 349 and y <= 514 and y >= 485:
                     ##   col1_row2
                    EXITLIST=[0,0,0]
                    if RESPONSE==CURRENTLIST[1]:
                        # if already selected, unselect and move pertinent mask offscreen
                        maskblue = TextureStimulus(texture=useTHISmask,position=(-200,-200), anchor='upperleft', max_alpha=0.50)
                        MASKLIST[0]=maskblue
                        RESPONSE=" "
                        ANSWERED=0
                    else:
                        # otherwise, select and move pertinent mask over the word
                        maskblue = TextureStimulus(texture=useTHISmask,position=(54,513), anchor='upperleft', max_alpha=0.50)
                        MASKLIST[0]=maskblue
                        RESPONSE=CURRENTLIST[1]
                        ANSWERED=1
                    screen.clear()
                    viewport.draw()
                    viewportTEXT2.draw()
                    viewportmasks.draw()
                    VisionEgg.Core.swap_buffers()
                    
                elif x >= 53 and x <= 349 and y <= 484 and y >= 455:
                     ##   col1_row3
                    EXITLIST=[0,0,0]
                    if RESPONSE==CURRENTLIST[2]:
                        # if already selected, unselect and move pertinent mask offscreen
                        maskblue = TextureStimulus(texture=useTHISmask,position=(-200,-200), anchor='upperleft', max_alpha=0.50)
                        MASKLIST[0]=maskblue
                        RESPONSE=" "
                        ANSWERED=0
                    else:
                        # otherwise, select and move pertinent mask over the word
                        maskblue = TextureStimulus(texture=useTHISmask,position=(54,483), anchor='upperleft', max_alpha=0.50)
                        MASKLIST[0]=maskblue
                        RESPONSE=CURRENTLIST[2]
                        ANSWERED=1
                    screen.clear()
                    viewport.draw()
                    viewportTEXT2.draw()
                    viewportmasks.draw()
                    VisionEgg.Core.swap_buffers()
                    
                elif x >= 53 and x <= 349 and y <= 454 and y >= 425:
                     ##   col1_row4
                    EXITLIST=[0,0,0]
                    if RESPONSE==CURRENTLIST[3]:
                        # if already selected, unselect and move pertinent mask offscreen
                        maskblue = TextureStimulus(texture=useTHISmask,position=(-200,-200), anchor='upperleft', max_alpha=0.50)
                        MASKLIST[0]=maskblue
                        RESPONSE=" "
                        ANSWERED=0
                    else:
                        # otherwise, select and move pertinent mask over the word
                        maskblue = TextureStimulus(texture=useTHISmask,position=(54,453), anchor='upperleft', max_alpha=0.50)
                        MASKLIST[0]=maskblue
                        RESPONSE=CURRENTLIST[3]
                        ANSWERED=1
                    screen.clear()
                    viewport.draw()
                    viewportTEXT2.draw()
                    viewportmasks.draw()
                    VisionEgg.Core.swap_buffers()
                    
                elif x >= 53 and x <= 349 and y <= 424 and y >= 395:
                     ##   col1_row5
                    EXITLIST=[0,0,0]
                    if RESPONSE==CURRENTLIST[4]:
                        # if already selected, unselect and move pertinent mask offscreen
                        maskblue = TextureStimulus(texture=useTHISmask,position=(-200,-200), anchor='upperleft', max_alpha=0.50)
                        MASKLIST[0]=maskblue
                        RESPONSE=" "
                        ANSWERED=0
                    else:
                        # otherwise, select and move pertinent mask over the word
                        maskblue = TextureStimulus(texture=useTHISmask,position=(54,423), anchor='upperleft', max_alpha=0.50)
                        MASKLIST[0]=maskblue
                        RESPONSE=CURRENTLIST[4]
                        ANSWERED=1
                    screen.clear()
                    viewport.draw()
                    viewportTEXT2.draw()
                    viewportmasks.draw()
                    VisionEgg.Core.swap_buffers()
                    
                elif x >= 53 and x <= 349 and y <= 394 and y >= 365:
                     ##   col1_row6
                    EXITLIST=[0,0,0]
                    if RESPONSE==CURRENTLIST[5]:
                        # if already selected, unselect and move pertinent mask offscreen
                        maskblue = TextureStimulus(texture=useTHISmask,position=(-200,-200), anchor='upperleft', max_alpha=0.50)
                        MASKLIST[0]=maskblue
                        RESPONSE=" "
                        ANSWERED=0
                    else:
                        # otherwise, select and move pertinent mask over the word
                        maskblue = TextureStimulus(texture=useTHISmask,position=(54,393), anchor='upperleft', max_alpha=0.50)
                        MASKLIST[0]=maskblue
                        RESPONSE=CURRENTLIST[5]
                        ANSWERED=1
                    screen.clear()
                    viewport.draw()
                    viewportTEXT2.draw()
                    viewportmasks.draw()
                    VisionEgg.Core.swap_buffers()
                    
                elif x >= 53 and x <= 349 and y <= 364 and y >= 335:
                     ##   col1_row7
                    EXITLIST=[0,0,0]
                    if RESPONSE==CURRENTLIST[6]:
                        # if already selected, unselect and move pertinent mask offscreen
                        maskblue = TextureStimulus(texture=useTHISmask,position=(-200,-200), anchor='upperleft', max_alpha=0.50)
                        MASKLIST[0]=maskblue
                        RESPONSE=" "
                        ANSWERED=0
                    else:
                        # otherwise, select and move pertinent mask over the word
                        maskblue = TextureStimulus(texture=useTHISmask,position=(54,363), anchor='upperleft', max_alpha=0.50)
                        MASKLIST[0]=maskblue
                        RESPONSE=CURRENTLIST[6]
                        ANSWERED=1
                    screen.clear()
                    viewport.draw()
                    viewportTEXT2.draw()
                    viewportmasks.draw()
                    VisionEgg.Core.swap_buffers()
                    
                elif x >= 53 and x <= 349 and y <= 334 and y >= 305:
                     ##   col1_row8
                    EXITLIST=[0,0,0]
                    if RESPONSE==CURRENTLIST[7]:
                        # if already selected, unselect and move pertinent mask offscreen
                        maskblue = TextureStimulus(texture=useTHISmask,position=(-200,-200), anchor='upperleft', max_alpha=0.50)
                        MASKLIST[0]=maskblue
                        RESPONSE=" "
                        ANSWERED=0
                    else:
                        # otherwise, select and move pertinent mask over the word
                        maskblue = TextureStimulus(texture=useTHISmask,position=(54,333), anchor='upperleft', max_alpha=0.50)
                        MASKLIST[0]=maskblue
                        RESPONSE=CURRENTLIST[7]
                        ANSWERED=1
                    screen.clear()
                    viewport.draw()
                    viewportTEXT2.draw()
                    viewportmasks.draw()
                    VisionEgg.Core.swap_buffers()
                    
                elif x >= 53 and x <= 349 and y <= 304 and y >= 275:
                     ##   col1_row9
                    EXITLIST=[0,0,0]
                    if RESPONSE==CURRENTLIST[9]:
                        # if already selected, unselect and move pertinent mask offscreen
                        maskblue = TextureStimulus(texture=useTHISmask,position=(-200,-200), anchor='upperleft', max_alpha=0.50)
                        MASKLIST[0]=maskblue
                        RESPONSE=" "
                        ANSWERED=0
                    else:
                        # otherwise, select and move pertinent mask over the word
                        maskblue = TextureStimulus(texture=useTHISmask,position=(54,303), anchor='upperleft', max_alpha=0.50)
                        MASKLIST[0]=maskblue
                        RESPONSE=CURRENTLIST[9]
                        ANSWERED=1
                    screen.clear()
                    viewport.draw()
                    viewportTEXT2.draw()
                    viewportmasks.draw()
                    VisionEgg.Core.swap_buffers()
                    
                elif x >= 53 and x <= 349 and y <= 274 and y >= 245:
                     ##   col1_row10
                    EXITLIST=[0,0,0]
                    if RESPONSE==CURRENTLIST[9]:
                        # if already selected, unselect and move pertinent mask offscreen
                        maskblue = TextureStimulus(texture=useTHISmask,position=(-200,-200), anchor='upperleft', max_alpha=0.50)
                        MASKLIST[0]=maskblue
                        RESPONSE=" "
                        ANSWERED=0
                    else:
                        # otherwise, select and move pertinent mask over the word
                        maskblue = TextureStimulus(texture=useTHISmask,position=(54,273), anchor='upperleft', max_alpha=0.50)
                        MASKLIST[0]=maskblue
                        RESPONSE=CURRENTLIST[9]
                        ANSWERED=1
                    screen.clear()
                    viewport.draw()
                    viewportTEXT2.draw()
                    viewportmasks.draw()
                    VisionEgg.Core.swap_buffers()
                    
                elif x >= 53 and x <= 349 and y <= 244 and y >= 215:
                     ##   col1_row11
                    EXITLIST=[0,0,0]
                    if RESPONSE==CURRENTLIST[10]:
                        # if already selected, unselect and move pertinent mask offscreen
                        maskblue = TextureStimulus(texture=useTHISmask,position=(-200,-200), anchor='upperleft', max_alpha=0.50)
                        MASKLIST[0]=maskblue
                        RESPONSE=" "
                        ANSWERED=0
                    else:
                        # otherwise, select and move pertinent mask over the word
                        maskblue = TextureStimulus(texture=useTHISmask,position=(54,243), anchor='upperleft', max_alpha=0.50)
                        MASKLIST[0]=maskblue
                        RESPONSE=CURRENTLIST[10]
                        ANSWERED=1
                    screen.clear()
                    viewport.draw()
                    viewportTEXT2.draw()
                    viewportmasks.draw()
                    VisionEgg.Core.swap_buffers()
                    
                elif x >= 53 and x <= 349 and y <= 214 and y >= 185:
                     ##   col1_row12
                    EXITLIST=[0,0,0]
                    if RESPONSE==CURRENTLIST[11]:
                        # if already selected, unselect and move pertinent mask offscreen
                        maskblue = TextureStimulus(texture=useTHISmask,position=(-200,-200), anchor='upperleft', max_alpha=0.50)
                        MASKLIST[0]=maskblue
                        RESPONSE=" "
                        ANSWERED=0
                    else:
                        # otherwise, select and move pertinent mask over the word
                        maskblue = TextureStimulus(texture=useTHISmask,position=(54,213), anchor='upperleft', max_alpha=0.50)
                        MASKLIST[0]=maskblue
                        RESPONSE=CURRENTLIST[11]
                        ANSWERED=1
                    screen.clear()
                    viewport.draw()
                    viewportTEXT2.draw()
                    viewportmasks.draw()
                    VisionEgg.Core.swap_buffers()
                    
                elif x >= 53 and x <= 349 and y <= 184 and y >= 155:
                     ##   col1_row13
                    EXITLIST=[0,0,0]
                    if RESPONSE==CURRENTLIST[12]:
                        # if already selected, unselect and move pertinent mask offscreen
                        maskblue = TextureStimulus(texture=useTHISmask,position=(-200,-200), anchor='upperleft', max_alpha=0.50)
                        MASKLIST[0]=maskblue
                        RESPONSE=" "
                        ANSWERED=0
                    else:
                        # otherwise, select and move pertinent mask over the word
                        maskblue = TextureStimulus(texture=useTHISmask,position=(54,183), anchor='upperleft', max_alpha=0.50)
                        MASKLIST[0]=maskblue
                        RESPONSE=CURRENTLIST[12]
                        ANSWERED=1
                    screen.clear()
                    viewport.draw()
                    viewportTEXT2.draw()
                    viewportmasks.draw()
                    VisionEgg.Core.swap_buffers()
                    
                elif x >= 53 and x <= 349 and y <= 154 and y >= 125:
                     ##   col1_row14
                    EXITLIST=[0,0,0]
                    if RESPONSE==CURRENTLIST[13]:
                        # if already selected, unselect and move pertinent mask offscreen
                        maskblue = TextureStimulus(texture=useTHISmask,position=(-200,-200), anchor='upperleft', max_alpha=0.50)
                        MASKLIST[0]=maskblue
                        RESPONSE=" "
                        ANSWERED=0
                    else:
                        # otherwise, select and move pertinent mask over the word
                        maskblue = TextureStimulus(texture=useTHISmask,position=(54,153), anchor='upperleft', max_alpha=0.50)
                        MASKLIST[0]=maskblue
                        RESPONSE=CURRENTLIST[13]
                        ANSWERED=1
                    screen.clear()
                    viewport.draw()
                    viewportTEXT2.draw()
                    viewportmasks.draw()
                    VisionEgg.Core.swap_buffers()
                    
                elif x >= 53 and x <= 349 and y <= 124 and y >= 95:
                     ##   col1_row15
                    EXITLIST=[0,0,0]
                    if RESPONSE==CURRENTLIST[14]:
                        # if already selected, unselect and move pertinent mask offscreen
                        maskblue = TextureStimulus(texture=useTHISmask,position=(-200,-200), anchor='upperleft', max_alpha=0.50)
                        MASKLIST[0]=maskblue
                        RESPONSE=" "
                        ANSWERED=0
                    else:
                        # otherwise, select and move pertinent mask over the word
                        maskblue = TextureStimulus(texture=useTHISmask,position=(54,123), anchor='upperleft', max_alpha=0.50)
                        MASKLIST[0]=maskblue
                        RESPONSE=CURRENTLIST[14]
                        ANSWERED=1
                    screen.clear()
                    viewport.draw()
                    viewportTEXT2.draw()
                    viewportmasks.draw()
                    VisionEgg.Core.swap_buffers()
                    
                elif x >= 53 and x <= 349 and y <= 94 and y >= 65:
                     ##   col1_row16
                    EXITLIST=[0,0,0]
                    if RESPONSE==CURRENTLIST[15]:
                        # if already selected, unselect and move pertinent mask offscreen
                        maskblue = TextureStimulus(texture=useTHISmask,position=(-200,-200), anchor='upperleft', max_alpha=0.50)
                        MASKLIST[0]=maskblue
                        RESPONSE=" "
                        ANSWERED=0
                    else:
                        # otherwise, select and move pertinent mask over the word
                        maskblue = TextureStimulus(texture=useTHISmask,position=(54,93), anchor='upperleft', max_alpha=0.50)
                        MASKLIST[0]=maskblue
                        RESPONSE=CURRENTLIST[15]
                        ANSWERED=1
                    screen.clear()
                    viewport.draw()
                    viewportTEXT2.draw()
                    viewportmasks.draw()
                    VisionEgg.Core.swap_buffers()
                    
                elif x >= 53 and x <= 349 and y <= 64 and y >= 35:
                     ##   col1_row17
                    EXITLIST=[0,0,0]
                    if RESPONSE==CURRENTLIST[16]:
                        # if already selected, unselect and move pertinent mask offscreen
                        maskblue = TextureStimulus(texture=useTHISmask,position=(-200,-200), anchor='upperleft', max_alpha=0.50)
                        MASKLIST[0]=maskblue
                        RESPONSE=" "
                        ANSWERED=0
                    else:
                        # otherwise, select and move pertinent mask over the word
                        maskblue = TextureStimulus(texture=useTHISmask,position=(54,63), anchor='upperleft', max_alpha=0.50)
                        MASKLIST[0]=maskblue
                        RESPONSE=CURRENTLIST[16]
                        ANSWERED=1
                    screen.clear()
                    viewport.draw()
                    viewportTEXT2.draw()
                    viewportmasks.draw()
                    VisionEgg.Core.swap_buffers()
                    
                elif x >= 53 and x <= 349 and y <= 34 and y >= 5:
                     ##   col1_row18
                    EXITLIST=[0,0,0]
                    if RESPONSE==CURRENTLIST[17]:
                        # if already selected, unselect and move pertinent mask offscreen
                        maskblue = TextureStimulus(texture=useTHISmask,position=(-200,-200), anchor='upperleft', max_alpha=0.50)
                        MASKLIST[0]=maskblue
                        RESPONSE=" "
                        ANSWERED=0
                    else:
                        # otherwise, select and move pertinent mask over the word
                        maskblue = TextureStimulus(texture=useTHISmask,position=(54,33), anchor='upperleft', max_alpha=0.50)
                        MASKLIST[0]=maskblue
                        RESPONSE=CURRENTLIST[17]
                        ANSWERED=1
                    screen.clear()
                    viewport.draw()
                    viewportTEXT2.draw()
                    viewportmasks.draw()
                    VisionEgg.Core.swap_buffers()
                    
                elif x >= 364 and x <= 662 and y <= 544 and y >= 515:
                     ##   col2_row__1
                    EXITLIST=[0,0,0]
                    if RESPONSE==CURRENTLIST[18]:
                        # if already selected, unselect and move pertinent mask offscreen
                        maskblue = TextureStimulus(texture=useTHISmask,position=(-200,-200), anchor='upperleft', max_alpha=0.50)
                        MASKLIST[0]=maskblue
                        RESPONSE=" "
                        ANSWERED=0
                    else:
                        # otherwise, select and move pertinent mask over the word
                        maskblue = TextureStimulus(texture=useTHISmask,position=(365,543), anchor='upperleft', max_alpha=0.50)
                        MASKLIST[0]=maskblue
                        RESPONSE=CURRENTLIST[18]
                        ANSWERED=1
                    screen.clear()
                    viewport.draw()
                    viewportTEXT2.draw()
                    viewportmasks.draw()
                    VisionEgg.Core.swap_buffers()
                    
                elif x >= 364 and x <= 662 and y <= 514 and y >= 485:
                     ##   col2_row2
                    EXITLIST=[0,0,0]
                    if RESPONSE==CURRENTLIST[19]:
                        # if already selected, unselect and move pertinent mask offscreen
                        maskblue = TextureStimulus(texture=useTHISmask,position=(-200,-200), anchor='upperleft', max_alpha=0.50)
                        MASKLIST[0]=maskblue
                        RESPONSE=" "
                        ANSWERED=0
                    else:
                        # otherwise, select and move pertinent mask over the word
                        maskblue = TextureStimulus(texture=useTHISmask,position=(365,513), anchor='upperleft', max_alpha=0.50)
                        MASKLIST[0]=maskblue
                        RESPONSE=CURRENTLIST[19]
                        ANSWERED=1
                    screen.clear()
                    viewport.draw()
                    viewportTEXT2.draw()
                    viewportmasks.draw()
                    VisionEgg.Core.swap_buffers()
                    
                elif x >= 364 and x <= 662 and y <= 484 and y >= 455:
                     ##   col2_row3
                    EXITLIST=[0,0,0]
                    if RESPONSE==CURRENTLIST[20]:
                        # if already selected, unselect and move pertinent mask offscreen
                        maskblue = TextureStimulus(texture=useTHISmask,position=(-200,-200), anchor='upperleft', max_alpha=0.50)
                        MASKLIST[0]=maskblue
                        RESPONSE=" "
                        ANSWERED=0
                    else:
                        # otherwise, select and move pertinent mask over the word
                        maskblue = TextureStimulus(texture=useTHISmask,position=(365,483), anchor='upperleft', max_alpha=0.50)
                        MASKLIST[0]=maskblue
                        RESPONSE=CURRENTLIST[20]
                        ANSWERED=1
                    screen.clear()
                    viewport.draw()
                    viewportTEXT2.draw()
                    viewportmasks.draw()
                    VisionEgg.Core.swap_buffers()
                    
                elif x >= 364 and x <= 662 and y <= 454 and y >= 425:
                     ##   col2_row4
                    EXITLIST=[0,0,0]
                    if RESPONSE==CURRENTLIST[21]:
                        # if already selected, unselect and move pertinent mask offscreen
                        maskblue = TextureStimulus(texture=useTHISmask,position=(-200,-200), anchor='upperleft', max_alpha=0.50)
                        MASKLIST[0]=maskblue
                        RESPONSE=" "
                        ANSWERED=0
                    else:
                        # otherwise, select and move pertinent mask over the word
                        maskblue = TextureStimulus(texture=useTHISmask,position=(365,453), anchor='upperleft', max_alpha=0.50)
                        MASKLIST[0]=maskblue
                        RESPONSE=CURRENTLIST[21]
                        ANSWERED=1
                    screen.clear()
                    viewport.draw()
                    viewportTEXT2.draw()
                    viewportmasks.draw()
                    VisionEgg.Core.swap_buffers()
                    
                elif x >= 364 and x <= 662 and y <= 424 and y >= 395:
                     ##   col2_row5
                    EXITLIST=[0,0,0]
                    if RESPONSE==CURRENTLIST[22]:
                        # if already selected, unselect and move pertinent mask offscreen
                        maskblue = TextureStimulus(texture=useTHISmask,position=(-200,-200), anchor='upperleft', max_alpha=0.50)
                        MASKLIST[0]=maskblue
                        RESPONSE=" "
                        ANSWERED=0
                    else:
                        # otherwise, select and move pertinent mask over the word
                        maskblue = TextureStimulus(texture=useTHISmask,position=(365,423), anchor='upperleft', max_alpha=0.50)
                        MASKLIST[0]=maskblue
                        RESPONSE=CURRENTLIST[22]
                        ANSWERED=1
                    screen.clear()
                    viewport.draw()
                    viewportTEXT2.draw()
                    viewportmasks.draw()
                    VisionEgg.Core.swap_buffers()
                    
                elif x >= 364 and x <= 662 and y <= 394 and y >= 365:
                     ##   col2_row6
                    EXITLIST=[0,0,0]
                    if RESPONSE==CURRENTLIST[23]:
                        # if already selected, unselect and move pertinent mask offscreen
                        maskblue = TextureStimulus(texture=useTHISmask,position=(-200,-200), anchor='upperleft', max_alpha=0.50)
                        MASKLIST[0]=maskblue
                        RESPONSE=" "
                        ANSWERED=0
                    else:
                        # otherwise, select and move pertinent mask over the word
                        maskblue = TextureStimulus(texture=useTHISmask,position=(365,393), anchor='upperleft', max_alpha=0.50)
                        MASKLIST[0]=maskblue
                        RESPONSE=CURRENTLIST[23]
                        ANSWERED=1
                    screen.clear()
                    viewport.draw()
                    viewportTEXT2.draw()
                    viewportmasks.draw()
                    VisionEgg.Core.swap_buffers()
                    
                elif x >= 364 and x <= 662 and y <= 364 and y >= 335:
                     ##   col2_row7
                    EXITLIST=[0,0,0]
                    if RESPONSE==CURRENTLIST[24]:
                        # if already selected, unselect and move pertinent mask offscreen
                        maskblue = TextureStimulus(texture=useTHISmask,position=(-200,-200), anchor='upperleft', max_alpha=0.50)
                        MASKLIST[0]=maskblue
                        RESPONSE=" "
                        ANSWERED=0
                    else:
                        # otherwise, select and move pertinent mask over the word
                        maskblue = TextureStimulus(texture=useTHISmask,position=(365,363), anchor='upperleft', max_alpha=0.50)
                        MASKLIST[0]=maskblue
                        RESPONSE=CURRENTLIST[24]
                        ANSWERED=1
                    screen.clear()
                    viewport.draw()
                    viewportTEXT2.draw()
                    viewportmasks.draw()
                    VisionEgg.Core.swap_buffers()
                    
                elif x >= 364 and x <= 662 and y <= 334 and y >= 305:
                     ##   col2_row8
                    EXITLIST=[0,0,0]
                    if RESPONSE==CURRENTLIST[25]:
                        # if already selected, unselect and move pertinent mask offscreen
                        maskblue = TextureStimulus(texture=useTHISmask,position=(-200,-200), anchor='upperleft', max_alpha=0.50)
                        MASKLIST[0]=maskblue
                        RESPONSE=" "
                        ANSWERED=0
                    else:
                        # otherwise, select and move pertinent mask over the word
                        maskblue = TextureStimulus(texture=useTHISmask,position=(365,333), anchor='upperleft', max_alpha=0.50)
                        MASKLIST[0]=maskblue
                        RESPONSE=CURRENTLIST[25]
                        ANSWERED=1
                    screen.clear()
                    viewport.draw()
                    viewportTEXT2.draw()
                    viewportmasks.draw()
                    VisionEgg.Core.swap_buffers()
                    
                elif x >= 364 and x <= 662 and y <= 304 and y >= 275:
                     ##   col2_row9
                    EXITLIST=[0,0,0]
                    if RESPONSE==CURRENTLIST[26]:
                        # if already selected, unselect and move pertinent mask offscreen
                        maskblue = TextureStimulus(texture=useTHISmask,position=(-200,-200), anchor='upperleft', max_alpha=0.50)
                        MASKLIST[0]=maskblue
                        RESPONSE=" "
                        ANSWERED=0
                    else:
                        # otherwise, select and move pertinent mask over the word
                        maskblue = TextureStimulus(texture=useTHISmask,position=(365,303), anchor='upperleft', max_alpha=0.50)
                        MASKLIST[0]=maskblue
                        RESPONSE=CURRENTLIST[26]
                        ANSWERED=1
                    screen.clear()
                    viewport.draw()
                    viewportTEXT2.draw()
                    viewportmasks.draw()
                    VisionEgg.Core.swap_buffers()
                    
                elif x >= 364 and x <= 662 and y <= 274 and y >= 245:
                     ##   col2_row10
                    EXITLIST=[0,0,0]
                    if RESPONSE==CURRENTLIST[27]:
                        # if already selected, unselect and move pertinent mask offscreen
                        maskblue = TextureStimulus(texture=useTHISmask,position=(-200,-200), anchor='upperleft', max_alpha=0.50)
                        MASKLIST[0]=maskblue
                        RESPONSE=" "
                        ANSWERED=0
                    else:
                        # otherwise, select and move pertinent mask over the word
                        maskblue = TextureStimulus(texture=useTHISmask,position=(365,273), anchor='upperleft', max_alpha=0.50)
                        MASKLIST[0]=maskblue
                        RESPONSE=CURRENTLIST[27]
                        ANSWERED=1
                    screen.clear()
                    viewport.draw()
                    viewportTEXT2.draw()
                    viewportmasks.draw()
                    VisionEgg.Core.swap_buffers()
                    
                elif x >= 364 and x <= 662 and y <= 244 and y >= 215:
                     ##   col2_row11
                    EXITLIST=[0,0,0]
                    if RESPONSE==CURRENTLIST[28]:
                        # if already selected, unselect and move pertinent mask offscreen
                        maskblue = TextureStimulus(texture=useTHISmask,position=(-200,-200), anchor='upperleft', max_alpha=0.50)
                        MASKLIST[0]=maskblue
                        RESPONSE=" "
                        ANSWERED=0
                    else:
                        # otherwise, select and move pertinent mask over the word
                        maskblue = TextureStimulus(texture=useTHISmask,position=(365,243), anchor='upperleft', max_alpha=0.50)
                        MASKLIST[0]=maskblue
                        RESPONSE=CURRENTLIST[28]
                        ANSWERED=1
                    screen.clear()
                    viewport.draw()
                    viewportTEXT2.draw()
                    viewportmasks.draw()
                    VisionEgg.Core.swap_buffers()
                    
                elif x >= 364 and x <= 662 and y <= 214 and y >= 185:
                     ##   col2_row12
                    EXITLIST=[0,0,0]
                    if RESPONSE==CURRENTLIST[29]:
                        # if already selected, unselect and move pertinent mask offscreen
                        maskblue = TextureStimulus(texture=useTHISmask,position=(-200,-200), anchor='upperleft', max_alpha=0.50)
                        MASKLIST[0]=maskblue
                        RESPONSE=" "
                        ANSWERED=0
                    else:
                        # otherwise, select and move pertinent mask over the word
                        maskblue = TextureStimulus(texture=useTHISmask,position=(365,213), anchor='upperleft', max_alpha=0.50)
                        MASKLIST[0]=maskblue
                        RESPONSE=CURRENTLIST[29]
                        ANSWERED=1
                    screen.clear()
                    viewport.draw()
                    viewportTEXT2.draw()
                    viewportmasks.draw()
                    VisionEgg.Core.swap_buffers()
                    
                elif x >= 364 and x <= 662 and y <= 184 and y >= 155:
                     ##   col2_row13
                    EXITLIST=[0,0,0]
                    if RESPONSE==CURRENTLIST[30]:
                        # if already selected, unselect and move pertinent mask offscreen
                        maskblue = TextureStimulus(texture=useTHISmask,position=(-200,-200), anchor='upperleft', max_alpha=0.50)
                        MASKLIST[0]=maskblue
                        RESPONSE=" "
                        ANSWERED=0
                    else:
                        # otherwise, select and move pertinent mask over the word
                        maskblue = TextureStimulus(texture=useTHISmask,position=(365,183), anchor='upperleft', max_alpha=0.50)
                        MASKLIST[0]=maskblue
                        RESPONSE=CURRENTLIST[30]
                        ANSWERED=1
                    screen.clear()
                    viewport.draw()
                    viewportTEXT2.draw()
                    viewportmasks.draw()
                    VisionEgg.Core.swap_buffers()
                    
                elif x >= 364 and x <= 662 and y <= 154 and y >= 125:
                     ##   col2_row14
                    EXITLIST=[0,0,0]
                    if RESPONSE==CURRENTLIST[31]:
                        # if already selected, unselect and move pertinent mask offscreen
                        maskblue = TextureStimulus(texture=useTHISmask,position=(-200,-200), anchor='upperleft', max_alpha=0.50)
                        MASKLIST[0]=maskblue
                        RESPONSE=" "
                        ANSWERED=0
                    else:
                        # otherwise, select and move pertinent mask over the word
                        maskblue = TextureStimulus(texture=useTHISmask,position=(365,153), anchor='upperleft', max_alpha=0.50)
                        MASKLIST[0]=maskblue
                        RESPONSE=CURRENTLIST[31]
                        ANSWERED=1
                    screen.clear()
                    viewport.draw()
                    viewportTEXT2.draw()
                    viewportmasks.draw()
                    VisionEgg.Core.swap_buffers()
                    
                elif x >= 364 and x <= 662 and y <= 124 and y >= 95:
                     ##   col2_row15
                    EXITLIST=[0,0,0]
                    if RESPONSE==CURRENTLIST[32]:
                        # if already selected, unselect and move pertinent mask offscreen
                        maskblue = TextureStimulus(texture=useTHISmask,position=(-200,-200), anchor='upperleft', max_alpha=0.50)
                        MASKLIST[0]=maskblue
                        RESPONSE=" "
                        ANSWERED=0
                    else:
                        # otherwise, select and move pertinent mask over the word
                        maskblue = TextureStimulus(texture=useTHISmask,position=(365,123), anchor='upperleft', max_alpha=0.50)
                        MASKLIST[0]=maskblue
                        RESPONSE=CURRENTLIST[32]
                        ANSWERED=1
                    screen.clear()
                    viewport.draw()
                    viewportTEXT2.draw()
                    viewportmasks.draw()
                    VisionEgg.Core.swap_buffers()
                    
                elif x >= 364 and x <= 662 and y <= 94 and y >= 65:
                     ##   col2_row16
                    EXITLIST=[0,0,0]
                    if RESPONSE==CURRENTLIST[33]:
                        # if already selected, unselect and move pertinent mask offscreen
                        maskblue = TextureStimulus(texture=useTHISmask,position=(-200,-200), anchor='upperleft', max_alpha=0.50)
                        MASKLIST[0]=maskblue
                        RESPONSE=" "
                        ANSWERED=0
                    else:
                        # otherwise, select and move pertinent mask over the word
                        maskblue = TextureStimulus(texture=useTHISmask,position=(365,93), anchor='upperleft', max_alpha=0.50)
                        MASKLIST[0]=maskblue
                        RESPONSE=CURRENTLIST[33]
                        ANSWERED=1
                    screen.clear()
                    viewport.draw()
                    viewportTEXT2.draw()
                    viewportmasks.draw()
                    VisionEgg.Core.swap_buffers()
                    
                elif x >= 364 and x <= 662 and y <= 64 and y >= 35:
                     ##   col2_row17
                    EXITLIST=[0,0,0]
                    if RESPONSE==CURRENTLIST[34]:
                        # if already selected, unselect and move pertinent mask offscreen
                        maskblue = TextureStimulus(texture=useTHISmask,position=(-200,-200), anchor='upperleft', max_alpha=0.50)
                        MASKLIST[0]=maskblue
                        RESPONSE=" "
                        ANSWERED=0
                    else:
                        # otherwise, select and move pertinent mask over the word
                        maskblue = TextureStimulus(texture=useTHISmask,position=(365,63), anchor='upperleft', max_alpha=0.50)
                        MASKLIST[0]=maskblue
                        RESPONSE=CURRENTLIST[34]
                        ANSWERED=1
                    screen.clear()
                    viewport.draw()
                    viewportTEXT2.draw()
                    viewportmasks.draw()
                    VisionEgg.Core.swap_buffers()
                    
                elif x >= 364 and x <= 662 and y <= 34 and y >= 5:
                     ##   col2_row18
                    EXITLIST=[0,0,0]
                    if RESPONSE==CURRENTLIST[35]:
                        # if already selected, unselect and move pertinent mask offscreen
                        maskblue = TextureStimulus(texture=useTHISmask,position=(-200,-200), anchor='upperleft', max_alpha=0.50)
                        MASKLIST[0]=maskblue
                        RESPONSE=" "
                        ANSWERED=0
                    else:
                        # otherwise, select and move pertinent mask over the word
                        maskblue = TextureStimulus(texture=useTHISmask,position=(365,33), anchor='upperleft', max_alpha=0.50)
                        MASKLIST[0]=maskblue
                        RESPONSE=CURRENTLIST[35]
                        ANSWERED=1
                    screen.clear()
                    viewport.draw()
                    viewportTEXT2.draw()
                    viewportmasks.draw()
                    VisionEgg.Core.swap_buffers()
                    

                elif x >= 676 and x <= 974 and y <= 544 and y >= 515:
                     ##   col3_row__1
                    EXITLIST=[0,0,0]
                    if RESPONSE==CURRENTLIST[36]:
                        # if already selected, unselect and move pertinent mask offscreen
                        maskblue = TextureStimulus(texture=useTHISmask,position=(-200,-200), anchor='upperleft', max_alpha=0.50)
                        MASKLIST[0]=maskblue
                        RESPONSE=" "
                        ANSWERED=0
                    else:
                        # otherwise, select and move pertinent mask over the word
                        maskblue = TextureStimulus(texture=useTHISmask,position=(675,543), anchor='upperleft', max_alpha=0.50)
                        MASKLIST[0]=maskblue
                        RESPONSE=CURRENTLIST[36]
                        ANSWERED=1
                    screen.clear()
                    viewport.draw()
                    viewportTEXT2.draw()
                    viewportmasks.draw()
                    VisionEgg.Core.swap_buffers()
                    
                elif x >= 676 and x <= 974 and y <= 514 and y >= 485:
                     ##   col3_row2
                    EXITLIST=[0,0,0]
                    if RESPONSE==CURRENTLIST[37]:
                        # if already selected, unselect and move pertinent mask offscreen
                        maskblue = TextureStimulus(texture=useTHISmask,position=(-200,-200), anchor='upperleft', max_alpha=0.50)
                        MASKLIST[0]=maskblue
                        RESPONSE=" "
                        ANSWERED=0
                    else:
                        # otherwise, select and move pertinent mask over the word
                        maskblue = TextureStimulus(texture=useTHISmask,position=(675,513), anchor='upperleft', max_alpha=0.50)
                        MASKLIST[0]=maskblue
                        RESPONSE=CURRENTLIST[37]
                        ANSWERED=1
                    screen.clear()
                    viewport.draw()
                    viewportTEXT2.draw()
                    viewportmasks.draw()
                    VisionEgg.Core.swap_buffers()
                    
                elif x >= 676 and x <= 974 and y <= 484 and y >= 455:
                     ##   col3_row3
                    EXITLIST=[0,0,0]
                    if RESPONSE==CURRENTLIST[38]:
                        # if already selected, unselect and move pertinent mask offscreen
                        maskblue = TextureStimulus(texture=useTHISmask,position=(-200,-200), anchor='upperleft', max_alpha=0.50)
                        MASKLIST[0]=maskblue
                        RESPONSE=" "
                        ANSWERED=0
                    else:
                        # otherwise, select and move pertinent mask over the word
                        maskblue = TextureStimulus(texture=useTHISmask,position=(675,483), anchor='upperleft', max_alpha=0.50)
                        MASKLIST[0]=maskblue
                        RESPONSE=CURRENTLIST[38]
                        ANSWERED=1
                    screen.clear()
                    viewport.draw()
                    viewportTEXT2.draw()
                    viewportmasks.draw()
                    VisionEgg.Core.swap_buffers()
                    
                elif x >= 676 and x <= 974 and y <= 454 and y >= 425:
                     ##   col3_row4
                    EXITLIST=[0,0,0]
                    if RESPONSE==CURRENTLIST[39]:
                        # if already selected, unselect and move pertinent mask offscreen
                        maskblue = TextureStimulus(texture=useTHISmask,position=(-200,-200), anchor='upperleft', max_alpha=0.50)
                        MASKLIST[0]=maskblue
                        RESPONSE=" "
                        ANSWERED=0
                    else:
                        # otherwise, select and move pertinent mask over the word
                        maskblue = TextureStimulus(texture=useTHISmask,position=(675,453), anchor='upperleft', max_alpha=0.50)
                        MASKLIST[0]=maskblue
                        RESPONSE=CURRENTLIST[39]
                        ANSWERED=1
                    screen.clear()
                    viewport.draw()
                    viewportTEXT2.draw()
                    viewportmasks.draw()
                    VisionEgg.Core.swap_buffers()
                    
                elif x >= 676 and x <= 974 and y <= 424 and y >= 395:
                     ##   col3_row5
                    EXITLIST=[0,0,0]
                    if RESPONSE==CURRENTLIST[40]:
                        # if already selected, unselect and move pertinent mask offscreen
                        maskblue = TextureStimulus(texture=useTHISmask,position=(-200,-200), anchor='upperleft', max_alpha=0.50)
                        MASKLIST[0]=maskblue
                        RESPONSE=" "
                        ANSWERED=0
                    else:
                        # otherwise, select and move pertinent mask over the word
                        maskblue = TextureStimulus(texture=useTHISmask,position=(675,423), anchor='upperleft', max_alpha=0.50)
                        MASKLIST[0]=maskblue
                        RESPONSE=CURRENTLIST[40]
                        ANSWERED=1
                    screen.clear()
                    viewport.draw()
                    viewportTEXT2.draw()
                    viewportmasks.draw()
                    VisionEgg.Core.swap_buffers()
                    
                elif x >= 676 and x <= 974 and y <= 394 and y >= 365:
                     ##   col3_row6
                    EXITLIST=[0,0,0]
                    if RESPONSE==CURRENTLIST[41]:
                        # if already selected, unselect and move pertinent mask offscreen
                        maskblue = TextureStimulus(texture=useTHISmask,position=(-200,-200), anchor='upperleft', max_alpha=0.50)
                        MASKLIST[0]=maskblue
                        RESPONSE=" "
                        ANSWERED=0
                    else:
                        # otherwise, select and move pertinent mask over the word
                        maskblue = TextureStimulus(texture=useTHISmask,position=(675,393), anchor='upperleft', max_alpha=0.50)
                        MASKLIST[0]=maskblue
                        RESPONSE=CURRENTLIST[41]
                        ANSWERED=1
                    screen.clear()
                    viewport.draw()
                    viewportTEXT2.draw()
                    viewportmasks.draw()
                    VisionEgg.Core.swap_buffers()
                    
                elif x >= 676 and x <= 974 and y <= 364 and y >= 335:
                     ##   col3_row7
                    EXITLIST=[0,0,0]
                    if RESPONSE==CURRENTLIST[42]:
                        # if already selected, unselect and move pertinent mask offscreen
                        maskblue = TextureStimulus(texture=useTHISmask,position=(-200,-200), anchor='upperleft', max_alpha=0.50)
                        MASKLIST[0]=maskblue
                        RESPONSE=" "
                        ANSWERED=0
                    else:
                        # otherwise, select and move pertinent mask over the word
                        maskblue = TextureStimulus(texture=useTHISmask,position=(675,363), anchor='upperleft', max_alpha=0.50)
                        MASKLIST[0]=maskblue
                        RESPONSE=CURRENTLIST[42]
                        ANSWERED=1
                    screen.clear()
                    viewport.draw()
                    viewportTEXT2.draw()
                    viewportmasks.draw()
                    VisionEgg.Core.swap_buffers()
                    
                elif x >= 676 and x <= 974 and y <= 334 and y >= 305:
                     ##   col3_row8
                    EXITLIST=[0,0,0]
                    if RESPONSE==CURRENTLIST[43]:
                        # if already selected, unselect and move pertinent mask offscreen
                        maskblue = TextureStimulus(texture=useTHISmask,position=(-200,-200), anchor='upperleft', max_alpha=0.50)
                        MASKLIST[0]=maskblue
                        RESPONSE=" "
                        ANSWERED=0
                    else:
                        # otherwise, select and move pertinent mask over the word
                        maskblue = TextureStimulus(texture=useTHISmask,position=(675,333), anchor='upperleft', max_alpha=0.50)
                        MASKLIST[0]=maskblue
                        RESPONSE=CURRENTLIST[43]
                        ANSWERED=1
                    screen.clear()
                    viewport.draw()
                    viewportTEXT2.draw()
                    viewportmasks.draw()
                    VisionEgg.Core.swap_buffers()
                    
                elif x >= 676 and x <= 974 and y <= 304 and y >= 275:
                     ##   col3_row9
                    EXITLIST=[0,0,0]
                    if RESPONSE==CURRENTLIST[44]:
                        # if already selected, unselect and move pertinent mask offscreen
                        maskblue = TextureStimulus(texture=useTHISmask,position=(-200,-200), anchor='upperleft', max_alpha=0.50)
                        MASKLIST[0]=maskblue
                        RESPONSE=" "
                        ANSWERED=0
                    else:
                        # otherwise, select and move pertinent mask over the word
                        maskblue = TextureStimulus(texture=useTHISmask,position=(675,303), anchor='upperleft', max_alpha=0.50)
                        MASKLIST[0]=maskblue
                        RESPONSE=CURRENTLIST[44]
                        ANSWERED=1
                    screen.clear()
                    viewport.draw()
                    viewportTEXT2.draw()
                    viewportmasks.draw()
                    VisionEgg.Core.swap_buffers()
                    
                elif x >= 676 and x <= 974 and y <= 274 and y >= 245:
                     ##   col3_row10
                    EXITLIST=[0,0,0]
                    if RESPONSE==CURRENTLIST[45]:
                        # if already selected, unselect and move pertinent mask offscreen
                        maskblue = TextureStimulus(texture=useTHISmask,position=(-200,-200), anchor='upperleft', max_alpha=0.50)
                        MASKLIST[0]=maskblue
                        RESPONSE=" "
                        ANSWERED=0
                    else:
                        # otherwise, select and move pertinent mask over the word
                        maskblue = TextureStimulus(texture=useTHISmask,position=(675,273), anchor='upperleft', max_alpha=0.50)
                        MASKLIST[0]=maskblue
                        RESPONSE=CURRENTLIST[45]
                        ANSWERED=1
                    screen.clear()
                    viewport.draw()
                    viewportTEXT2.draw()
                    viewportmasks.draw()
                    VisionEgg.Core.swap_buffers()
                    
                elif x >= 676 and x <= 974 and y <= 244 and y >= 215:
                     ##   col3_row11
                    EXITLIST=[0,0,0]
                    if RESPONSE==CURRENTLIST[46]:
                        # if already selected, unselect and move pertinent mask offscreen
                        maskblue = TextureStimulus(texture=useTHISmask,position=(-200,-200), anchor='upperleft', max_alpha=0.50)
                        MASKLIST[0]=maskblue
                        RESPONSE=" "
                        ANSWERED=0
                    else:
                        # otherwise, select and move pertinent mask over the word
                        maskblue = TextureStimulus(texture=useTHISmask,position=(675,243), anchor='upperleft', max_alpha=0.50)
                        MASKLIST[0]=maskblue
                        RESPONSE=CURRENTLIST[46]
                        ANSWERED=1
                    screen.clear()
                    viewport.draw()
                    viewportTEXT2.draw()
                    viewportmasks.draw()
                    VisionEgg.Core.swap_buffers()
                    
                elif x >= 676 and x <= 974 and y <= 214 and y >= 185:
                     ##   col3_row12
                    EXITLIST=[0,0,0]
                    if RESPONSE==CURRENTLIST[47]:
                        # if already selected, unselect and move pertinent mask offscreen
                        maskblue = TextureStimulus(texture=useTHISmask,position=(-200,-200), anchor='upperleft', max_alpha=0.50)
                        MASKLIST[0]=maskblue
                        RESPONSE=" "
                        ANSWERED=0
                    else:
                        # otherwise, select and move pertinent mask over the word
                        maskblue = TextureStimulus(texture=useTHISmask,position=(675,213), anchor='upperleft', max_alpha=0.50)
                        MASKLIST[0]=maskblue
                        RESPONSE=CURRENTLIST[47]
                        ANSWERED=1
                    screen.clear()
                    viewport.draw()
                    viewportTEXT2.draw()
                    viewportmasks.draw()
                    VisionEgg.Core.swap_buffers()
                    
                elif x >= 676 and x <= 974 and y <= 184 and y >= 155:
                     ##   col3_row13
                    EXITLIST=[0,0,0]
                    if RESPONSE==CURRENTLIST[48]:
                        # if already selected, unselect and move pertinent mask offscreen
                        maskblue = TextureStimulus(texture=useTHISmask,position=(-200,-200), anchor='upperleft', max_alpha=0.50)
                        MASKLIST[0]=maskblue
                        RESPONSE=" "
                        ANSWERED=0
                    else:
                        # otherwise, select and move pertinent mask over the word
                        maskblue = TextureStimulus(texture=useTHISmask,position=(675,183), anchor='upperleft', max_alpha=0.50)
                        MASKLIST[0]=maskblue
                        RESPONSE=CURRENTLIST[48]
                        ANSWERED=1
                    screen.clear()
                    viewport.draw()
                    viewportTEXT2.draw()
                    viewportmasks.draw()
                    VisionEgg.Core.swap_buffers()
                    
                elif x >= 676 and x <= 974 and y <= 154 and y >= 125:
                     ##   col3_row14
                    EXITLIST=[0,0,0]
                    if RESPONSE==CURRENTLIST[49]:
                        # if already selected, unselect and move pertinent mask offscreen
                        maskblue = TextureStimulus(texture=useTHISmask,position=(-200,-200), anchor='upperleft', max_alpha=0.50)
                        MASKLIST[0]=maskblue
                        RESPONSE=" "
                        ANSWERED=0
                    else:
                        # otherwise, select and move pertinent mask over the word
                        maskblue = TextureStimulus(texture=useTHISmask,position=(675,153), anchor='upperleft', max_alpha=0.50)
                        MASKLIST[0]=maskblue
                        RESPONSE=CURRENTLIST[49]
                        ANSWERED=1
                    screen.clear()
                    viewport.draw()
                    viewportTEXT2.draw()
                    viewportmasks.draw()
                    VisionEgg.Core.swap_buffers()
                      
                ##
                ## now we see the practical application of the EXITLIST:
                elif x >= 0 and x <=24 and y >= 584 and y <=600:
                   if EXITLIST==[0,0,0]:
                       EXITLIST[0]=1
                       text0 = Text(text="O",color=(0,0,0),position=(0,600),font_size=30,anchor='center')
                       text1 = Text(text="O",color=(0,0,0),position=(0,600),font_size=30,anchor='center')
                       viewportTEXT = VisionEgg.Core.Viewport(screen=screen, size=screen.size, stimuli=[text0, text1])
                       VisionEgg.Core.swap_buffers()
                       screen.clear()
                       viewport.draw()
                       viewportmasks.draw()
                       viewportTEXT.draw()
                       viewportTEXT2.draw()
                       VisionEgg.Core.swap_buffers()
                elif x >= 1008 and x <=1024 and y >= 584 and y <=600:
                    if EXITLIST==[1,0,0]:
                       EXITLIST[1]=1
                       text0 = Text(text="O",color=(0,0,0),position=(0,600),font_size=30,anchor='center')
                       text1 = Text(text="O",color=(0,0,0),position=(1024,600),font_size=30,anchor='center')
                       viewportTEXT = VisionEgg.Core.Viewport(screen=screen, size=screen.size, stimuli=[text0, text1])
                       VisionEgg.Core.swap_buffers()
                       screen.clear()
                       viewport.draw()
                       viewportmasks.draw()
                       viewportTEXT.draw()
                       viewportTEXT2.draw()
                       VisionEgg.Core.swap_buffers()
                elif x >= 1008 and x <=1024 and y >= 0 and y <=16:
                    if EXITLIST==[1,1,0]:
                        ScreenNumber, RESET = ESCAPEscreenLATE(ScreenNumber, RESET)
###  ###   ###  # #     ### ALWAYS REMEMBER TO UPDATE THE RETURN INFO!  ##   #   #   #####  ##  ###    ### ### 
                        return ScreenNumber, TrialTime, RESPONSE, ERRORS, RESET
                        StartTrial=True
#</$%^>


####################################################################################################
####################################################################################################
####################################################################################################
####################################################################################################
####################################################################################################

                        

####################################################################################################
####################################################################################################
####################################################################################################
####################################################################################################
####################################################################################################

                        
                        
####################################################################################################
####################################################################################################
####################################################################################################
####################################################################################################
####################################################################################################

                        
                        
####################################################################################################
####################################################################################################
####################################################################################################
####################################################################################################
####################################################################################################
def FREErecall(ScreenNumber, TrialTime, RESPONSE, ERRORS, RESET):
    x=-1
    y=-1
    #make and show background
    backgroundIMAGE = TextureStimulus(texture=taskbackgrounds[12],position=(0,0))
    viewport = VisionEgg.Core.Viewport(screen=screen, size=screen.size, stimuli=[backgroundIMAGE,backgroundIMAGE])
    warnBOX_early = TextureStimulus(texture=notyetboxes[14],position=(830,150), anchor='center', max_alpha=0.90)
    warnBOX_late = TextureStimulus(texture=notyetboxes[15],position=(830,150), anchor='center', max_alpha=0.90)
    viewportwarnBOX_early = VisionEgg.Core.Viewport(screen=screen, size=screen.size, stimuli=[warnBOX_early])
    viewportwarnBOX_late = VisionEgg.Core.Viewport(screen=screen, size=screen.size, stimuli=[warnBOX_late])
    useTHISmask=masks[6]
    maskblue = TextureStimulus(texture=useTHISmask,position=(-100,-100), anchor='center', max_alpha=0.50)    
    MASKLIST=[maskblue]
     ## we'll modify the MASKLIST depending on button presses....
    viewportmasks = VisionEgg.Core.Viewport(screen=screen, size=screen.size, stimuli=MASKLIST)
    ##
    EXITLIST=[0,0,0]
    ANSWERS=0
    Choice=[" "]
    ERRORS=0
    ##
    CURRENTLIST=list_words

    viewportTEXT2=FREErecallVIEWPORT
    screen.clear()
    viewport.draw()
    viewportTEXT2.draw()
    VisionEgg.Core.swap_buffers()
    startTIME=int(round(time() * 1000))
    screen.clear()
    viewport.draw()
    viewportTEXT2.draw()
    viewportmasks.draw()
    VisionEgg.Core.swap_buffers()
    StartTrial=False
    while not StartTrial:
        for event in pygame.event.get():
            if event.type == pygame.locals.MOUSEBUTTONDOWN:
                if (int(round(time() * 1000))-startTIME) > 100:
                    x,y = pygame.mouse.get_pos()
## pygame.mouse.get_pos() gives coordinates with the LOWER LEFT, not UPPER LEFT (as in visionegg) corner as the origin.
## before we get too complicated, will probably want to flip things around:
                y=600-y
                if x >= 903 and x <=996 and y >=0 and y <=37:
                    EXITLIST=[0,0,0]
                    ## the "touch here when done" box. Action depends on whether there's a full answer.
                    if ANSWERS == 5:
                        RESPONSE=sorted(Choice)
                        ## trial time is in seconds
                        TrialTime=int(round(time() * 1000))-startTIME
                        return ScreenNumber, TrialTime, RESPONSE, ERRORS, RESET
                        StartTrial=True                       
                    elif ANSWERS < 5:
                        ERRORS=ERRORS+1
                        screen.clear()
                        viewport.draw()
                        viewportTEXT2.draw()
                        viewportmasks.draw()
                        viewportwarnBOX_early.draw() #it'll stay up until something else is clicked
                        VisionEgg.Core.swap_buffers()
                    elif ANSWERS > 5:
                        ERRORS=ERRORS+1
                        screen.clear()
                        viewport.draw()
                        viewportTEXT2.draw()
                        viewportmasks.draw()
                        viewportwarnBOX_late.draw() #it'll stay up until something else is clicked
                        VisionEgg.Core.swap_buffers()
                                        
                elif x >= 22 and x <= 174 and y <= 517 and y >= 488:
                     ##   col1_row__1
                    EXITLIST=[0,0,0]
                    if CURRENTLIST[0] in Choice:
                        ANSWERS=ANSWERS-1
                        which_is_it=Choice.index(CURRENTLIST[0])
                        del Choice[which_is_it]
                        del MASKLIST[which_is_it]
                    else:
                        maskblue = TextureStimulus(texture=useTHISmask,position=(23,518), anchor='upperleft', max_alpha=0.50)
                        MASKLIST.append(maskblue)
                        Choice.append(CURRENTLIST[0])
                        ANSWERS=ANSWERS+1
                    screen.clear()
                    viewport.draw()
                    viewportTEXT2.draw()
                    viewportmasks.draw()
                    VisionEgg.Core.swap_buffers()

                elif x >= 22 and x <= 174 and y <= 487 and y >= 458:
                     ##   col1_row__2
                    EXITLIST=[0,0,0]
                    if CURRENTLIST[1] in Choice:
                        ANSWERS=ANSWERS-1
                        which_is_it=Choice.index(CURRENTLIST[1])
                        del Choice[which_is_it]
                        del MASKLIST[which_is_it]
                    else:
                        maskblue = TextureStimulus(texture=useTHISmask,position=(23,488), anchor='upperleft', max_alpha=0.50)
                        MASKLIST.append(maskblue)
                        Choice.append(CURRENTLIST[1])
                        ANSWERS=ANSWERS+1
                    screen.clear()
                    viewport.draw()
                    viewportTEXT2.draw()
                    viewportmasks.draw()
                    VisionEgg.Core.swap_buffers()

                elif x >= 22 and x <= 174 and y <= 457 and y >= 428:
                     ##   col1_row__3
                    EXITLIST=[0,0,0]
                    if CURRENTLIST[2] in Choice:
                        ANSWERS=ANSWERS-1
                        which_is_it=Choice.index(CURRENTLIST[2])
                        del Choice[which_is_it]
                        del MASKLIST[which_is_it]
                    else:
                        maskblue = TextureStimulus(texture=useTHISmask,position=(23,458), anchor='upperleft', max_alpha=0.50)
                        MASKLIST.append(maskblue)
                        Choice.append(CURRENTLIST[2])
                        ANSWERS=ANSWERS+1
                    screen.clear()
                    viewport.draw()
                    viewportTEXT2.draw()
                    viewportmasks.draw()
                    VisionEgg.Core.swap_buffers()

                elif x >= 22 and x <= 174 and y <= 427 and y >= 398:
                     ##   col1_row__4
                    EXITLIST=[0,0,0]
                    if CURRENTLIST[3] in Choice:
                        ANSWERS=ANSWERS-1
                        which_is_it=Choice.index(CURRENTLIST[3])
                        del Choice[which_is_it]
                        del MASKLIST[which_is_it]
                    else:
                        maskblue = TextureStimulus(texture=useTHISmask,position=(23,428), anchor='upperleft', max_alpha=0.50)
                        MASKLIST.append(maskblue)
                        Choice.append(CURRENTLIST[3])
                        ANSWERS=ANSWERS+1
                    screen.clear()
                    viewport.draw()
                    viewportTEXT2.draw()
                    viewportmasks.draw()
                    VisionEgg.Core.swap_buffers()

                elif x >= 22 and x <= 174 and y <= 397 and y >= 368:
                     ##   col1_row__5
                    EXITLIST=[0,0,0]
                    if CURRENTLIST[4] in Choice:
                        ANSWERS=ANSWERS-1
                        which_is_it=Choice.index(CURRENTLIST[4])
                        del Choice[which_is_it]
                        del MASKLIST[which_is_it]
                    else:
                        maskblue = TextureStimulus(texture=useTHISmask,position=(23,398), anchor='upperleft', max_alpha=0.50)
                        MASKLIST.append(maskblue)
                        Choice.append(CURRENTLIST[4])
                        ANSWERS=ANSWERS+1
                    screen.clear()
                    viewport.draw()
                    viewportTEXT2.draw()
                    viewportmasks.draw()
                    VisionEgg.Core.swap_buffers()

                elif x >= 22 and x <= 174 and y <= 367 and y >= 338:
                     ##   col1_row__6
                    EXITLIST=[0,0,0]
                    if CURRENTLIST[5] in Choice:
                        ANSWERS=ANSWERS-1
                        which_is_it=Choice.index(CURRENTLIST[5])
                        del Choice[which_is_it]
                        del MASKLIST[which_is_it]
                    else:
                        maskblue = TextureStimulus(texture=useTHISmask,position=(23,368), anchor='upperleft', max_alpha=0.50)
                        MASKLIST.append(maskblue)
                        Choice.append(CURRENTLIST[5])
                        ANSWERS=ANSWERS+1
                    screen.clear()
                    viewport.draw()
                    viewportTEXT2.draw()
                    viewportmasks.draw()
                    VisionEgg.Core.swap_buffers()

                elif x >= 22 and x <= 174 and y <= 337 and y >= 308:
                     ##   col1_row__7
                    EXITLIST=[0,0,0]
                    if CURRENTLIST[6] in Choice:
                        ANSWERS=ANSWERS-1
                        which_is_it=Choice.index(CURRENTLIST[6])
                        del Choice[which_is_it]
                        del MASKLIST[which_is_it]
                    else:
                        maskblue = TextureStimulus(texture=useTHISmask,position=(23,338), anchor='upperleft', max_alpha=0.50)
                        MASKLIST.append(maskblue)
                        Choice.append(CURRENTLIST[6])
                        ANSWERS=ANSWERS+1
                    screen.clear()
                    viewport.draw()
                    viewportTEXT2.draw()
                    viewportmasks.draw()
                    VisionEgg.Core.swap_buffers()

                elif x >= 22 and x <= 174 and y <= 307 and y >= 278:
                     ##   col1_row__8
                    EXITLIST=[0,0,0]
                    if CURRENTLIST[7] in Choice:
                        ANSWERS=ANSWERS-1
                        which_is_it=Choice.index(CURRENTLIST[7])
                        del Choice[which_is_it]
                        del MASKLIST[which_is_it]
                    else:
                        maskblue = TextureStimulus(texture=useTHISmask,position=(23,308), anchor='upperleft', max_alpha=0.50)
                        MASKLIST.append(maskblue)
                        Choice.append(CURRENTLIST[7])
                        ANSWERS=ANSWERS+1
                    screen.clear()
                    viewport.draw()
                    viewportTEXT2.draw()
                    viewportmasks.draw()
                    VisionEgg.Core.swap_buffers()

                elif x >= 22 and x <= 174 and y <= 277 and y >= 248:
                     ##   col1_row__9
                    EXITLIST=[0,0,0]
                    if CURRENTLIST[8] in Choice:
                        ANSWERS=ANSWERS-1
                        which_is_it=Choice.index(CURRENTLIST[8])
                        del Choice[which_is_it]
                        del MASKLIST[which_is_it]
                    else:
                        maskblue = TextureStimulus(texture=useTHISmask,position=(23,278), anchor='upperleft', max_alpha=0.50)
                        MASKLIST.append(maskblue)
                        Choice.append(CURRENTLIST[8])
                        ANSWERS=ANSWERS+1
                    screen.clear()
                    viewport.draw()
                    viewportTEXT2.draw()
                    viewportmasks.draw()
                    VisionEgg.Core.swap_buffers()

                elif x >= 22 and x <= 174 and y <= 247 and y >= 218:
                     ##   col1_row__10
                    EXITLIST=[0,0,0]
                    if CURRENTLIST[9] in Choice:
                        ANSWERS=ANSWERS-1
                        which_is_it=Choice.index(CURRENTLIST[9])
                        del Choice[which_is_it]
                        del MASKLIST[which_is_it]
                    else:
                        maskblue = TextureStimulus(texture=useTHISmask,position=(23,248), anchor='upperleft', max_alpha=0.50)
                        MASKLIST.append(maskblue)
                        Choice.append(CURRENTLIST[9])
                        ANSWERS=ANSWERS+1
                    screen.clear()
                    viewport.draw()
                    viewportTEXT2.draw()
                    viewportmasks.draw()
                    VisionEgg.Core.swap_buffers()

                elif x >= 22 and x <= 174 and y <= 217 and y >= 188:
                     ##   col1_row__11
                    EXITLIST=[0,0,0]
                    if CURRENTLIST[10] in Choice:
                        ANSWERS=ANSWERS-1
                        which_is_it=Choice.index(CURRENTLIST[10])
                        del Choice[which_is_it]
                        del MASKLIST[which_is_it]
                    else:
                        maskblue = TextureStimulus(texture=useTHISmask,position=(23,218), anchor='upperleft', max_alpha=0.50)
                        MASKLIST.append(maskblue)
                        Choice.append(CURRENTLIST[10])
                        ANSWERS=ANSWERS+1
                    screen.clear()
                    viewport.draw()
                    viewportTEXT2.draw()
                    viewportmasks.draw()
                    VisionEgg.Core.swap_buffers()

                elif x >= 22 and x <= 174 and y <= 187 and y >= 158:
                     ##   col1_row__12
                    EXITLIST=[0,0,0]
                    if CURRENTLIST[11] in Choice:
                        ANSWERS=ANSWERS-1
                        which_is_it=Choice.index(CURRENTLIST[11])
                        del Choice[which_is_it]
                        del MASKLIST[which_is_it]
                    else:
                        maskblue = TextureStimulus(texture=useTHISmask,position=(23,188), anchor='upperleft', max_alpha=0.50)
                        MASKLIST.append(maskblue)
                        Choice.append(CURRENTLIST[11])
                        ANSWERS=ANSWERS+1
                    screen.clear()
                    viewport.draw()
                    viewportTEXT2.draw()
                    viewportmasks.draw()
                    VisionEgg.Core.swap_buffers()

                elif x >= 22 and x <= 174 and y <= 157 and y >= 128:
                     ##   col1_row__13
                    EXITLIST=[0,0,0]
                    if CURRENTLIST[12] in Choice:
                        ANSWERS=ANSWERS-1
                        which_is_it=Choice.index(CURRENTLIST[12])
                        del Choice[which_is_it]
                        del MASKLIST[which_is_it]
                    else:
                        maskblue = TextureStimulus(texture=useTHISmask,position=(23,158), anchor='upperleft', max_alpha=0.50)
                        MASKLIST.append(maskblue)
                        Choice.append(CURRENTLIST[12])
                        ANSWERS=ANSWERS+1
                    screen.clear()
                    viewport.draw()
                    viewportTEXT2.draw()
                    viewportmasks.draw()
                    VisionEgg.Core.swap_buffers()

                elif x >= 22 and x <= 174 and y <= 127 and y >= 98:
                     ##   col1_row__14
                    EXITLIST=[0,0,0]
                    if CURRENTLIST[13] in Choice:
                        ANSWERS=ANSWERS-1
                        which_is_it=Choice.index(CURRENTLIST[13])
                        del Choice[which_is_it]
                        del MASKLIST[which_is_it]
                    else:
                        maskblue = TextureStimulus(texture=useTHISmask,position=(23,128), anchor='upperleft', max_alpha=0.50)
                        MASKLIST.append(maskblue)
                        Choice.append(CURRENTLIST[13])
                        ANSWERS=ANSWERS+1
                    screen.clear()
                    viewport.draw()
                    viewportTEXT2.draw()
                    viewportmasks.draw()
                    VisionEgg.Core.swap_buffers()

                elif x >= 22 and x <= 174 and y <= 97 and y >= 68:
                     ##   col1_row__15
                    EXITLIST=[0,0,0]
                    if CURRENTLIST[14] in Choice:
                        ANSWERS=ANSWERS-1
                        which_is_it=Choice.index(CURRENTLIST[14])
                        del Choice[which_is_it]
                        del MASKLIST[which_is_it]
                    else:
                        maskblue = TextureStimulus(texture=useTHISmask,position=(23,98), anchor='upperleft', max_alpha=0.50)
                        MASKLIST.append(maskblue)
                        Choice.append(CURRENTLIST[14])
                        ANSWERS=ANSWERS+1
                    screen.clear()
                    viewport.draw()
                    viewportTEXT2.draw()
                    viewportmasks.draw()
                    VisionEgg.Core.swap_buffers()

                elif x >= 22 and x <= 174 and y <= 67 and y >= 38:
                     ##   col1_row__16
                    EXITLIST=[0,0,0]
                    if CURRENTLIST[15] in Choice:
                        ANSWERS=ANSWERS-1
                        which_is_it=Choice.index(CURRENTLIST[15])
                        del Choice[which_is_it]
                        del MASKLIST[which_is_it]
                    else:
                        maskblue = TextureStimulus(texture=useTHISmask,position=(23,68), anchor='upperleft', max_alpha=0.50)
                        MASKLIST.append(maskblue)
                        Choice.append(CURRENTLIST[15])
                        ANSWERS=ANSWERS+1
                    screen.clear()
                    viewport.draw()
                    viewportTEXT2.draw()
                    viewportmasks.draw()
                    VisionEgg.Core.swap_buffers()

                elif x >= 22 and x <= 174 and y <= 37 and y >= 8:
                     ##   col1_row__17
                    EXITLIST=[0,0,0]
                    if CURRENTLIST[16] in Choice:
                        ANSWERS=ANSWERS-1
                        which_is_it=Choice.index(CURRENTLIST[16])
                        del Choice[which_is_it]
                        del MASKLIST[which_is_it]
                    else:
                        maskblue = TextureStimulus(texture=useTHISmask,position=(23,38), anchor='upperleft', max_alpha=0.50)
                        MASKLIST.append(maskblue)
                        Choice.append(CURRENTLIST[16])
                        ANSWERS=ANSWERS+1
                    screen.clear()
                    viewport.draw()
                    viewportTEXT2.draw()
                    viewportmasks.draw()
                    VisionEgg.Core.swap_buffers()

                elif x >= 186 and x <= 338 and y <= 517 and y >= 488:
                     ##   col2_row__1
                    EXITLIST=[0,0,0]
                    if CURRENTLIST[17] in Choice:
                        ANSWERS=ANSWERS-1
                        which_is_it=Choice.index(CURRENTLIST[17])
                        del Choice[which_is_it]
                        del MASKLIST[which_is_it]
                    else:
                        maskblue = TextureStimulus(texture=useTHISmask,position=(187,518), anchor='upperleft', max_alpha=0.50)
                        MASKLIST.append(maskblue)
                        Choice.append(CURRENTLIST[17])
                        ANSWERS=ANSWERS+1
                    screen.clear()
                    viewport.draw()
                    viewportTEXT2.draw()
                    viewportmasks.draw()
                    VisionEgg.Core.swap_buffers()

                elif x >= 186 and x <= 338 and y <= 487 and y >= 458:
                     ##   col2_row__2
                    EXITLIST=[0,0,0]
                    if CURRENTLIST[18] in Choice:
                        ANSWERS=ANSWERS-1
                        which_is_it=Choice.index(CURRENTLIST[18])
                        del Choice[which_is_it]
                        del MASKLIST[which_is_it]
                    else:
                        maskblue = TextureStimulus(texture=useTHISmask,position=(187,488), anchor='upperleft', max_alpha=0.50)
                        MASKLIST.append(maskblue)
                        Choice.append(CURRENTLIST[18])
                        ANSWERS=ANSWERS+1
                    screen.clear()
                    viewport.draw()
                    viewportTEXT2.draw()
                    viewportmasks.draw()
                    VisionEgg.Core.swap_buffers()

                elif x >= 186 and x <= 338 and y <= 457 and y >= 428:
                     ##   col2_row__3
                    EXITLIST=[0,0,0]
                    if CURRENTLIST[19] in Choice:
                        ANSWERS=ANSWERS-1
                        which_is_it=Choice.index(CURRENTLIST[19])
                        del Choice[which_is_it]
                        del MASKLIST[which_is_it]
                    else:
                        maskblue = TextureStimulus(texture=useTHISmask,position=(187,458), anchor='upperleft', max_alpha=0.50)
                        MASKLIST.append(maskblue)
                        Choice.append(CURRENTLIST[19])
                        ANSWERS=ANSWERS+1
                    screen.clear()
                    viewport.draw()
                    viewportTEXT2.draw()
                    viewportmasks.draw()
                    VisionEgg.Core.swap_buffers()

                elif x >= 186 and x <= 338 and y <= 427 and y >= 398:
                     ##   col2_row__4
                    EXITLIST=[0,0,0]
                    if CURRENTLIST[20] in Choice:
                        ANSWERS=ANSWERS-1
                        which_is_it=Choice.index(CURRENTLIST[20])
                        del Choice[which_is_it]
                        del MASKLIST[which_is_it]
                    else:
                        maskblue = TextureStimulus(texture=useTHISmask,position=(187,428), anchor='upperleft', max_alpha=0.50)
                        MASKLIST.append(maskblue)
                        Choice.append(CURRENTLIST[20])
                        ANSWERS=ANSWERS+1
                    screen.clear()
                    viewport.draw()
                    viewportTEXT2.draw()
                    viewportmasks.draw()
                    VisionEgg.Core.swap_buffers()

                elif x >= 186 and x <= 338 and y <= 397 and y >= 368:
                     ##   col2_row__5
                    EXITLIST=[0,0,0]
                    if CURRENTLIST[21] in Choice:
                        ANSWERS=ANSWERS-1
                        which_is_it=Choice.index(CURRENTLIST[21])
                        del Choice[which_is_it]
                        del MASKLIST[which_is_it]
                    else:
                        maskblue = TextureStimulus(texture=useTHISmask,position=(187,398), anchor='upperleft', max_alpha=0.50)
                        MASKLIST.append(maskblue)
                        Choice.append(CURRENTLIST[21])
                        ANSWERS=ANSWERS+1
                    screen.clear()
                    viewport.draw()
                    viewportTEXT2.draw()
                    viewportmasks.draw()
                    VisionEgg.Core.swap_buffers()

                elif x >= 186 and x <= 338 and y <= 367 and y >= 338:
                     ##   col2_row__6
                    EXITLIST=[0,0,0]
                    if CURRENTLIST[22] in Choice:
                        ANSWERS=ANSWERS-1
                        which_is_it=Choice.index(CURRENTLIST[22])
                        del Choice[which_is_it]
                        del MASKLIST[which_is_it]
                    else:
                        maskblue = TextureStimulus(texture=useTHISmask,position=(187,368), anchor='upperleft', max_alpha=0.50)
                        MASKLIST.append(maskblue)
                        Choice.append(CURRENTLIST[22])
                        ANSWERS=ANSWERS+1
                    screen.clear()
                    viewport.draw()
                    viewportTEXT2.draw()
                    viewportmasks.draw()
                    VisionEgg.Core.swap_buffers()

                elif x >= 186 and x <= 338 and y <= 337 and y >= 308:
                     ##   col2_row__7
                    EXITLIST=[0,0,0]
                    if CURRENTLIST[23] in Choice:
                        ANSWERS=ANSWERS-1
                        which_is_it=Choice.index(CURRENTLIST[23])
                        del Choice[which_is_it]
                        del MASKLIST[which_is_it]
                    else:
                        maskblue = TextureStimulus(texture=useTHISmask,position=(187,338), anchor='upperleft', max_alpha=0.50)
                        MASKLIST.append(maskblue)
                        Choice.append(CURRENTLIST[23])
                        ANSWERS=ANSWERS+1
                    screen.clear()
                    viewport.draw()
                    viewportTEXT2.draw()
                    viewportmasks.draw()
                    VisionEgg.Core.swap_buffers()

                elif x >= 186 and x <= 338 and y <= 307 and y >= 278:
                     ##   col2_row__8
                    EXITLIST=[0,0,0]
                    if CURRENTLIST[24] in Choice:
                        ANSWERS=ANSWERS-1
                        which_is_it=Choice.index(CURRENTLIST[24])
                        del Choice[which_is_it]
                        del MASKLIST[which_is_it]
                    else:
                        maskblue = TextureStimulus(texture=useTHISmask,position=(187,308), anchor='upperleft', max_alpha=0.50)
                        MASKLIST.append(maskblue)
                        Choice.append(CURRENTLIST[24])
                        ANSWERS=ANSWERS+1
                    screen.clear()
                    viewport.draw()
                    viewportTEXT2.draw()
                    viewportmasks.draw()
                    VisionEgg.Core.swap_buffers()

                elif x >= 186 and x <= 338 and y <= 277 and y >= 248:
                     ##   col2_row__9
                    EXITLIST=[0,0,0]
                    if CURRENTLIST[25] in Choice:
                        ANSWERS=ANSWERS-1
                        which_is_it=Choice.index(CURRENTLIST[25])
                        del Choice[which_is_it]
                        del MASKLIST[which_is_it]
                    else:
                        maskblue = TextureStimulus(texture=useTHISmask,position=(187,278), anchor='upperleft', max_alpha=0.50)
                        MASKLIST.append(maskblue)
                        Choice.append(CURRENTLIST[25])
                        ANSWERS=ANSWERS+1
                    screen.clear()
                    viewport.draw()
                    viewportTEXT2.draw()
                    viewportmasks.draw()
                    VisionEgg.Core.swap_buffers()

                elif x >= 186 and x <= 338 and y <= 247 and y >= 218:
                     ##   col2_row__10
                    EXITLIST=[0,0,0]
                    if CURRENTLIST[26] in Choice:
                        ANSWERS=ANSWERS-1
                        which_is_it=Choice.index(CURRENTLIST[26])
                        del Choice[which_is_it]
                        del MASKLIST[which_is_it]
                    else:
                        maskblue = TextureStimulus(texture=useTHISmask,position=(187,248), anchor='upperleft', max_alpha=0.50)
                        MASKLIST.append(maskblue)
                        Choice.append(CURRENTLIST[26])
                        ANSWERS=ANSWERS+1
                    screen.clear()
                    viewport.draw()
                    viewportTEXT2.draw()
                    viewportmasks.draw()
                    VisionEgg.Core.swap_buffers()

                elif x >= 186 and x <= 338 and y <= 217 and y >= 188:
                     ##   col2_row__11
                    EXITLIST=[0,0,0]
                    if CURRENTLIST[27] in Choice:
                        ANSWERS=ANSWERS-1
                        which_is_it=Choice.index(CURRENTLIST[27])
                        del Choice[which_is_it]
                        del MASKLIST[which_is_it]
                    else:
                        maskblue = TextureStimulus(texture=useTHISmask,position=(187,218), anchor='upperleft', max_alpha=0.50)
                        MASKLIST.append(maskblue)
                        Choice.append(CURRENTLIST[27])
                        ANSWERS=ANSWERS+1
                    screen.clear()
                    viewport.draw()
                    viewportTEXT2.draw()
                    viewportmasks.draw()
                    VisionEgg.Core.swap_buffers()

                elif x >= 186 and x <= 338 and y <= 187 and y >= 158:
                     ##   col2_row__12
                    EXITLIST=[0,0,0]
                    if CURRENTLIST[28] in Choice:
                        ANSWERS=ANSWERS-1
                        which_is_it=Choice.index(CURRENTLIST[28])
                        del Choice[which_is_it]
                        del MASKLIST[which_is_it]
                    else:
                        maskblue = TextureStimulus(texture=useTHISmask,position=(187,188), anchor='upperleft', max_alpha=0.50)
                        MASKLIST.append(maskblue)
                        Choice.append(CURRENTLIST[28])
                        ANSWERS=ANSWERS+1
                    screen.clear()
                    viewport.draw()
                    viewportTEXT2.draw()
                    viewportmasks.draw()
                    VisionEgg.Core.swap_buffers()

                elif x >= 186 and x <= 338 and y <= 157 and y >= 128:
                     ##   col2_row__13
                    EXITLIST=[0,0,0]
                    if CURRENTLIST[29] in Choice:
                        ANSWERS=ANSWERS-1
                        which_is_it=Choice.index(CURRENTLIST[29])
                        del Choice[which_is_it]
                        del MASKLIST[which_is_it]
                    else:
                        maskblue = TextureStimulus(texture=useTHISmask,position=(187,158), anchor='upperleft', max_alpha=0.50)
                        MASKLIST.append(maskblue)
                        Choice.append(CURRENTLIST[29])
                        ANSWERS=ANSWERS+1
                    screen.clear()
                    viewport.draw()
                    viewportTEXT2.draw()
                    viewportmasks.draw()
                    VisionEgg.Core.swap_buffers()

                elif x >= 186 and x <= 338 and y <= 127 and y >= 98:
                     ##   col2_row__14
                    EXITLIST=[0,0,0]
                    if CURRENTLIST[30] in Choice:
                        ANSWERS=ANSWERS-1
                        which_is_it=Choice.index(CURRENTLIST[30])
                        del Choice[which_is_it]
                        del MASKLIST[which_is_it]
                    else:
                        maskblue = TextureStimulus(texture=useTHISmask,position=(187,128), anchor='upperleft', max_alpha=0.50)
                        MASKLIST.append(maskblue)
                        Choice.append(CURRENTLIST[30])
                        ANSWERS=ANSWERS+1
                    screen.clear()
                    viewport.draw()
                    viewportTEXT2.draw()
                    viewportmasks.draw()
                    VisionEgg.Core.swap_buffers()

                elif x >= 186 and x <= 338 and y <= 97 and y >= 68:
                     ##   col2_row__15
                    EXITLIST=[0,0,0]
                    if CURRENTLIST[31] in Choice:
                        ANSWERS=ANSWERS-1
                        which_is_it=Choice.index(CURRENTLIST[31])
                        del Choice[which_is_it]
                        del MASKLIST[which_is_it]
                    else:
                        maskblue = TextureStimulus(texture=useTHISmask,position=(187,98), anchor='upperleft', max_alpha=0.50)
                        MASKLIST.append(maskblue)
                        Choice.append(CURRENTLIST[31])
                        ANSWERS=ANSWERS+1
                    screen.clear()
                    viewport.draw()
                    viewportTEXT2.draw()
                    viewportmasks.draw()
                    VisionEgg.Core.swap_buffers()

                elif x >= 186 and x <= 338 and y <= 67 and y >= 38:
                     ##   col2_row__16
                    EXITLIST=[0,0,0]
                    if CURRENTLIST[32] in Choice:
                        ANSWERS=ANSWERS-1
                        which_is_it=Choice.index(CURRENTLIST[32])
                        del Choice[which_is_it]
                        del MASKLIST[which_is_it]
                    else:
                        maskblue = TextureStimulus(texture=useTHISmask,position=(187,68), anchor='upperleft', max_alpha=0.50)
                        MASKLIST.append(maskblue)
                        Choice.append(CURRENTLIST[32])
                        ANSWERS=ANSWERS+1
                    screen.clear()
                    viewport.draw()
                    viewportTEXT2.draw()
                    viewportmasks.draw()
                    VisionEgg.Core.swap_buffers()

                elif x >= 186 and x <= 338 and y <= 37 and y >= 8:
                     ##   col2_row__17
                    EXITLIST=[0,0,0]
                    if CURRENTLIST[33] in Choice:
                        ANSWERS=ANSWERS-1
                        which_is_it=Choice.index(CURRENTLIST[33])
                        del Choice[which_is_it]
                        del MASKLIST[which_is_it]
                    else:
                        maskblue = TextureStimulus(texture=useTHISmask,position=(187,38), anchor='upperleft', max_alpha=0.50)
                        MASKLIST.append(maskblue)
                        Choice.append(CURRENTLIST[33])
                        ANSWERS=ANSWERS+1
                    screen.clear()
                    viewport.draw()
                    viewportTEXT2.draw()
                    viewportmasks.draw()
                    VisionEgg.Core.swap_buffers()

                elif x >= 352 and x <= 505 and y <= 517 and y >= 488:
                     ##   col3_row__1
                    EXITLIST=[0,0,0]
                    if CURRENTLIST[34] in Choice:
                        ANSWERS=ANSWERS-1
                        which_is_it=Choice.index(CURRENTLIST[34])
                        del Choice[which_is_it]
                        del MASKLIST[which_is_it]
                    else:
                        maskblue = TextureStimulus(texture=useTHISmask,position=(353,518), anchor='upperleft', max_alpha=0.50)
                        MASKLIST.append(maskblue)
                        Choice.append(CURRENTLIST[34])
                        ANSWERS=ANSWERS+1
                    screen.clear()
                    viewport.draw()
                    viewportTEXT2.draw()
                    viewportmasks.draw()
                    VisionEgg.Core.swap_buffers()

                elif x >= 352 and x <= 505 and y <= 487 and y >= 458:
                     ##   col3_row__2
                    EXITLIST=[0,0,0]
                    if CURRENTLIST[35] in Choice:
                        ANSWERS=ANSWERS-1
                        which_is_it=Choice.index(CURRENTLIST[35])
                        del Choice[which_is_it]
                        del MASKLIST[which_is_it]
                    else:
                        maskblue = TextureStimulus(texture=useTHISmask,position=(353,488), anchor='upperleft', max_alpha=0.50)
                        MASKLIST.append(maskblue)
                        Choice.append(CURRENTLIST[35])
                        ANSWERS=ANSWERS+1
                    screen.clear()
                    viewport.draw()
                    viewportTEXT2.draw()
                    viewportmasks.draw()
                    VisionEgg.Core.swap_buffers()

                elif x >= 352 and x <= 505 and y <= 457 and y >= 428:
                     ##   col3_row__3
                    EXITLIST=[0,0,0]
                    if CURRENTLIST[36] in Choice:
                        ANSWERS=ANSWERS-1
                        which_is_it=Choice.index(CURRENTLIST[36])
                        del Choice[which_is_it]
                        del MASKLIST[which_is_it]
                    else:
                        maskblue = TextureStimulus(texture=useTHISmask,position=(353,458), anchor='upperleft', max_alpha=0.50)
                        MASKLIST.append(maskblue)
                        Choice.append(CURRENTLIST[36])
                        ANSWERS=ANSWERS+1
                    screen.clear()
                    viewport.draw()
                    viewportTEXT2.draw()
                    viewportmasks.draw()
                    VisionEgg.Core.swap_buffers()

                elif x >= 352 and x <= 505 and y <= 427 and y >= 398:
                     ##   col3_row__4
                    EXITLIST=[0,0,0]
                    if CURRENTLIST[37] in Choice:
                        ANSWERS=ANSWERS-1
                        which_is_it=Choice.index(CURRENTLIST[37])
                        del Choice[which_is_it]
                        del MASKLIST[which_is_it]
                    else:
                        maskblue = TextureStimulus(texture=useTHISmask,position=(353,428), anchor='upperleft', max_alpha=0.50)
                        MASKLIST.append(maskblue)
                        Choice.append(CURRENTLIST[37])
                        ANSWERS=ANSWERS+1
                    screen.clear()
                    viewport.draw()
                    viewportTEXT2.draw()
                    viewportmasks.draw()
                    VisionEgg.Core.swap_buffers()

                elif x >= 352 and x <= 505 and y <= 397 and y >= 368:
                     ##   col3_row__5
                    EXITLIST=[0,0,0]
                    if CURRENTLIST[38] in Choice:
                        ANSWERS=ANSWERS-1
                        which_is_it=Choice.index(CURRENTLIST[38])
                        del Choice[which_is_it]
                        del MASKLIST[which_is_it]
                    else:
                        maskblue = TextureStimulus(texture=useTHISmask,position=(353,398), anchor='upperleft', max_alpha=0.50)
                        MASKLIST.append(maskblue)
                        Choice.append(CURRENTLIST[38])
                        ANSWERS=ANSWERS+1
                    screen.clear()
                    viewport.draw()
                    viewportTEXT2.draw()
                    viewportmasks.draw()
                    VisionEgg.Core.swap_buffers()

                elif x >= 352 and x <= 505 and y <= 367 and y >= 338:
                     ##   col3_row__6
                    EXITLIST=[0,0,0]
                    if CURRENTLIST[39] in Choice:
                        ANSWERS=ANSWERS-1
                        which_is_it=Choice.index(CURRENTLIST[39])
                        del Choice[which_is_it]
                        del MASKLIST[which_is_it]
                    else:
                        maskblue = TextureStimulus(texture=useTHISmask,position=(353,368), anchor='upperleft', max_alpha=0.50)
                        MASKLIST.append(maskblue)
                        Choice.append(CURRENTLIST[39])
                        ANSWERS=ANSWERS+1
                    screen.clear()
                    viewport.draw()
                    viewportTEXT2.draw()
                    viewportmasks.draw()
                    VisionEgg.Core.swap_buffers()

                elif x >= 352 and x <= 505 and y <= 337 and y >= 308:
                     ##   col3_row__7
                    EXITLIST=[0,0,0]
                    if CURRENTLIST[40] in Choice:
                        ANSWERS=ANSWERS-1
                        which_is_it=Choice.index(CURRENTLIST[40])
                        del Choice[which_is_it]
                        del MASKLIST[which_is_it]
                    else:
                        maskblue = TextureStimulus(texture=useTHISmask,position=(353,338), anchor='upperleft', max_alpha=0.50)
                        MASKLIST.append(maskblue)
                        Choice.append(CURRENTLIST[40])
                        ANSWERS=ANSWERS+1
                    screen.clear()
                    viewport.draw()
                    viewportTEXT2.draw()
                    viewportmasks.draw()
                    VisionEgg.Core.swap_buffers()

                elif x >= 352 and x <= 505 and y <= 307 and y >= 278:
                     ##   col3_row__8
                    EXITLIST=[0,0,0]
                    if CURRENTLIST[41] in Choice:
                        ANSWERS=ANSWERS-1
                        which_is_it=Choice.index(CURRENTLIST[41])
                        del Choice[which_is_it]
                        del MASKLIST[which_is_it]
                    else:
                        maskblue = TextureStimulus(texture=useTHISmask,position=(353,308), anchor='upperleft', max_alpha=0.50)
                        MASKLIST.append(maskblue)
                        Choice.append(CURRENTLIST[41])
                        ANSWERS=ANSWERS+1
                    screen.clear()
                    viewport.draw()
                    viewportTEXT2.draw()
                    viewportmasks.draw()
                    VisionEgg.Core.swap_buffers()

                elif x >= 352 and x <= 505 and y <= 277 and y >= 248:
                     ##   col3_row__9
                    EXITLIST=[0,0,0]
                    if CURRENTLIST[42] in Choice:
                        ANSWERS=ANSWERS-1
                        which_is_it=Choice.index(CURRENTLIST[42])
                        del Choice[which_is_it]
                        del MASKLIST[which_is_it]
                    else:
                        maskblue = TextureStimulus(texture=useTHISmask,position=(353,278), anchor='upperleft', max_alpha=0.50)
                        MASKLIST.append(maskblue)
                        Choice.append(CURRENTLIST[42])
                        ANSWERS=ANSWERS+1
                    screen.clear()
                    viewport.draw()
                    viewportTEXT2.draw()
                    viewportmasks.draw()
                    VisionEgg.Core.swap_buffers()

                elif x >= 352 and x <= 505 and y <= 247 and y >= 218:
                     ##   col3_row__10
                    EXITLIST=[0,0,0]
                    if CURRENTLIST[43] in Choice:
                        ANSWERS=ANSWERS-1
                        which_is_it=Choice.index(CURRENTLIST[43])
                        del Choice[which_is_it]
                        del MASKLIST[which_is_it]
                    else:
                        maskblue = TextureStimulus(texture=useTHISmask,position=(353,248), anchor='upperleft', max_alpha=0.50)
                        MASKLIST.append(maskblue)
                        Choice.append(CURRENTLIST[43])
                        ANSWERS=ANSWERS+1
                    screen.clear()
                    viewport.draw()
                    viewportTEXT2.draw()
                    viewportmasks.draw()
                    VisionEgg.Core.swap_buffers()

                elif x >= 352 and x <= 505 and y <= 217 and y >= 188:
                     ##   col3_row__11
                    EXITLIST=[0,0,0]
                    if CURRENTLIST[44] in Choice:
                        ANSWERS=ANSWERS-1
                        which_is_it=Choice.index(CURRENTLIST[44])
                        del Choice[which_is_it]
                        del MASKLIST[which_is_it]
                    else:
                        maskblue = TextureStimulus(texture=useTHISmask,position=(353,218), anchor='upperleft', max_alpha=0.50)
                        MASKLIST.append(maskblue)
                        Choice.append(CURRENTLIST[44])
                        ANSWERS=ANSWERS+1
                    screen.clear()
                    viewport.draw()
                    viewportTEXT2.draw()
                    viewportmasks.draw()
                    VisionEgg.Core.swap_buffers()

                elif x >= 352 and x <= 505 and y <= 187 and y >= 158:
                     ##   col3_row__12
                    EXITLIST=[0,0,0]
                    if CURRENTLIST[45] in Choice:
                        ANSWERS=ANSWERS-1
                        which_is_it=Choice.index(CURRENTLIST[45])
                        del Choice[which_is_it]
                        del MASKLIST[which_is_it]
                    else:
                        maskblue = TextureStimulus(texture=useTHISmask,position=(353,188), anchor='upperleft', max_alpha=0.50)
                        MASKLIST.append(maskblue)
                        Choice.append(CURRENTLIST[45])
                        ANSWERS=ANSWERS+1
                    screen.clear()
                    viewport.draw()
                    viewportTEXT2.draw()
                    viewportmasks.draw()
                    VisionEgg.Core.swap_buffers()

                elif x >= 352 and x <= 505 and y <= 157 and y >= 128:
                     ##   col3_row__13
                    EXITLIST=[0,0,0]
                    if CURRENTLIST[46] in Choice:
                        ANSWERS=ANSWERS-1
                        which_is_it=Choice.index(CURRENTLIST[46])
                        del Choice[which_is_it]
                        del MASKLIST[which_is_it]
                    else:
                        maskblue = TextureStimulus(texture=useTHISmask,position=(353,158), anchor='upperleft', max_alpha=0.50)
                        MASKLIST.append(maskblue)
                        Choice.append(CURRENTLIST[46])
                        ANSWERS=ANSWERS+1
                    screen.clear()
                    viewport.draw()
                    viewportTEXT2.draw()
                    viewportmasks.draw()
                    VisionEgg.Core.swap_buffers()

                elif x >= 352 and x <= 505 and y <= 127 and y >= 98:
                     ##   col3_row__14
                    EXITLIST=[0,0,0]
                    if CURRENTLIST[47] in Choice:
                        ANSWERS=ANSWERS-1
                        which_is_it=Choice.index(CURRENTLIST[47])
                        del Choice[which_is_it]
                        del MASKLIST[which_is_it]
                    else:
                        maskblue = TextureStimulus(texture=useTHISmask,position=(353,128), anchor='upperleft', max_alpha=0.50)
                        MASKLIST.append(maskblue)
                        Choice.append(CURRENTLIST[47])
                        ANSWERS=ANSWERS+1
                    screen.clear()
                    viewport.draw()
                    viewportTEXT2.draw()
                    viewportmasks.draw()
                    VisionEgg.Core.swap_buffers()

                elif x >= 352 and x <= 505 and y <= 97 and y >= 68:
                     ##   col3_row__15
                    EXITLIST=[0,0,0]
                    if CURRENTLIST[48] in Choice:
                        ANSWERS=ANSWERS-1
                        which_is_it=Choice.index(CURRENTLIST[48])
                        del Choice[which_is_it]
                        del MASKLIST[which_is_it]
                    else:
                        maskblue = TextureStimulus(texture=useTHISmask,position=(353,98), anchor='upperleft', max_alpha=0.50)
                        MASKLIST.append(maskblue)
                        Choice.append(CURRENTLIST[48])
                        ANSWERS=ANSWERS+1
                    screen.clear()
                    viewport.draw()
                    viewportTEXT2.draw()
                    viewportmasks.draw()
                    VisionEgg.Core.swap_buffers()

                elif x >= 352 and x <= 505 and y <= 67 and y >= 38:
                     ##   col3_row__16
                    EXITLIST=[0,0,0]
                    if CURRENTLIST[49] in Choice:
                        ANSWERS=ANSWERS-1
                        which_is_it=Choice.index(CURRENTLIST[49])
                        del Choice[which_is_it]
                        del MASKLIST[which_is_it]
                    else:
                        maskblue = TextureStimulus(texture=useTHISmask,position=(353,68), anchor='upperleft', max_alpha=0.50)
                        MASKLIST.append(maskblue)
                        Choice.append(CURRENTLIST[49])
                        ANSWERS=ANSWERS+1
                    screen.clear()
                    viewport.draw()
                    viewportTEXT2.draw()
                    viewportmasks.draw()
                    VisionEgg.Core.swap_buffers()

                elif x >= 352 and x <= 505 and y <= 37 and y >= 8:
                     ##   col3_row__17
                    EXITLIST=[0,0,0]
                    if CURRENTLIST[50] in Choice:
                        ANSWERS=ANSWERS-1
                        which_is_it=Choice.index(CURRENTLIST[50])
                        del Choice[which_is_it]
                        del MASKLIST[which_is_it]
                    else:
                        maskblue = TextureStimulus(texture=useTHISmask,position=(353,38), anchor='upperleft', max_alpha=0.50)
                        MASKLIST.append(maskblue)
                        Choice.append(CURRENTLIST[50])
                        ANSWERS=ANSWERS+1
                    screen.clear()
                    viewport.draw()
                    viewportTEXT2.draw()
                    viewportmasks.draw()
                    VisionEgg.Core.swap_buffers()

                elif x >= 517 and x <= 670 and y <= 517 and y >= 488:
                     ##   col4_row__1
                    EXITLIST=[0,0,0]
                    if CURRENTLIST[51] in Choice:
                        ANSWERS=ANSWERS-1
                        which_is_it=Choice.index(CURRENTLIST[51])
                        del Choice[which_is_it]
                        del MASKLIST[which_is_it]
                    else:
                        maskblue = TextureStimulus(texture=useTHISmask,position=(518,518), anchor='upperleft', max_alpha=0.50)
                        MASKLIST.append(maskblue)
                        Choice.append(CURRENTLIST[51])
                        ANSWERS=ANSWERS+1
                    screen.clear()
                    viewport.draw()
                    viewportTEXT2.draw()
                    viewportmasks.draw()
                    VisionEgg.Core.swap_buffers()

                elif x >= 517 and x <= 670 and y <= 487 and y >= 458:
                     ##   col4_row__2
                    EXITLIST=[0,0,0]
                    if CURRENTLIST[52] in Choice:
                        ANSWERS=ANSWERS-1
                        which_is_it=Choice.index(CURRENTLIST[52])
                        del Choice[which_is_it]
                        del MASKLIST[which_is_it]
                    else:
                        maskblue = TextureStimulus(texture=useTHISmask,position=(518,488), anchor='upperleft', max_alpha=0.50)
                        MASKLIST.append(maskblue)
                        Choice.append(CURRENTLIST[52])
                        ANSWERS=ANSWERS+1
                    screen.clear()
                    viewport.draw()
                    viewportTEXT2.draw()
                    viewportmasks.draw()
                    VisionEgg.Core.swap_buffers()

                elif x >= 517 and x <= 670 and y <= 457 and y >= 428:
                     ##   col4_row__3
                    EXITLIST=[0,0,0]
                    if CURRENTLIST[53] in Choice:
                        ANSWERS=ANSWERS-1
                        which_is_it=Choice.index(CURRENTLIST[53])
                        del Choice[which_is_it]
                        del MASKLIST[which_is_it]
                    else:
                        maskblue = TextureStimulus(texture=useTHISmask,position=(518,458), anchor='upperleft', max_alpha=0.50)
                        MASKLIST.append(maskblue)
                        Choice.append(CURRENTLIST[53])
                        ANSWERS=ANSWERS+1
                    screen.clear()
                    viewport.draw()
                    viewportTEXT2.draw()
                    viewportmasks.draw()
                    VisionEgg.Core.swap_buffers()

                elif x >= 517 and x <= 670 and y <= 427 and y >= 398:
                     ##   col4_row__4
                    EXITLIST=[0,0,0]
                    if CURRENTLIST[54] in Choice:
                        ANSWERS=ANSWERS-1
                        which_is_it=Choice.index(CURRENTLIST[54])
                        del Choice[which_is_it]
                        del MASKLIST[which_is_it]
                    else:
                        maskblue = TextureStimulus(texture=useTHISmask,position=(518,428), anchor='upperleft', max_alpha=0.50)
                        MASKLIST.append(maskblue)
                        Choice.append(CURRENTLIST[54])
                        ANSWERS=ANSWERS+1
                    screen.clear()
                    viewport.draw()
                    viewportTEXT2.draw()
                    viewportmasks.draw()
                    VisionEgg.Core.swap_buffers()

                elif x >= 517 and x <= 670 and y <= 397 and y >= 368:
                     ##   col4_row__5
                    EXITLIST=[0,0,0]
                    if CURRENTLIST[55] in Choice:
                        ANSWERS=ANSWERS-1
                        which_is_it=Choice.index(CURRENTLIST[55])
                        del Choice[which_is_it]
                        del MASKLIST[which_is_it]
                    else:
                        maskblue = TextureStimulus(texture=useTHISmask,position=(518,398), anchor='upperleft', max_alpha=0.50)
                        MASKLIST.append(maskblue)
                        Choice.append(CURRENTLIST[55])
                        ANSWERS=ANSWERS+1
                    screen.clear()
                    viewport.draw()
                    viewportTEXT2.draw()
                    viewportmasks.draw()
                    VisionEgg.Core.swap_buffers()

                elif x >= 517 and x <= 670 and y <= 367 and y >= 338:
                     ##   col4_row__6
                    EXITLIST=[0,0,0]
                    if CURRENTLIST[56] in Choice:
                        ANSWERS=ANSWERS-1
                        which_is_it=Choice.index(CURRENTLIST[56])
                        del Choice[which_is_it]
                        del MASKLIST[which_is_it]
                    else:
                        maskblue = TextureStimulus(texture=useTHISmask,position=(518,368), anchor='upperleft', max_alpha=0.50)
                        MASKLIST.append(maskblue)
                        Choice.append(CURRENTLIST[56])
                        ANSWERS=ANSWERS+1
                    screen.clear()
                    viewport.draw()
                    viewportTEXT2.draw()
                    viewportmasks.draw()
                    VisionEgg.Core.swap_buffers()

                elif x >= 517 and x <= 670 and y <= 337 and y >= 308:
                     ##   col4_row__7
                    EXITLIST=[0,0,0]
                    if CURRENTLIST[57] in Choice:
                        ANSWERS=ANSWERS-1
                        which_is_it=Choice.index(CURRENTLIST[57])
                        del Choice[which_is_it]
                        del MASKLIST[which_is_it]
                    else:
                        maskblue = TextureStimulus(texture=useTHISmask,position=(518,338), anchor='upperleft', max_alpha=0.50)
                        MASKLIST.append(maskblue)
                        Choice.append(CURRENTLIST[57])
                        ANSWERS=ANSWERS+1
                    screen.clear()
                    viewport.draw()
                    viewportTEXT2.draw()
                    viewportmasks.draw()
                    VisionEgg.Core.swap_buffers()

                elif x >= 517 and x <= 670 and y <= 307 and y >= 278:
                     ##   col4_row__8
                    EXITLIST=[0,0,0]
                    if CURRENTLIST[58] in Choice:
                        ANSWERS=ANSWERS-1
                        which_is_it=Choice.index(CURRENTLIST[58])
                        del Choice[which_is_it]
                        del MASKLIST[which_is_it]
                    else:
                        maskblue = TextureStimulus(texture=useTHISmask,position=(518,308), anchor='upperleft', max_alpha=0.50)
                        MASKLIST.append(maskblue)
                        Choice.append(CURRENTLIST[58])
                        ANSWERS=ANSWERS+1
                    screen.clear()
                    viewport.draw()
                    viewportTEXT2.draw()
                    viewportmasks.draw()
                    VisionEgg.Core.swap_buffers()

                elif x >= 517 and x <= 670 and y <= 277 and y >= 248:
                     ##   col4_row__9
                    EXITLIST=[0,0,0]
                    if CURRENTLIST[59] in Choice:
                        ANSWERS=ANSWERS-1
                        which_is_it=Choice.index(CURRENTLIST[59])
                        del Choice[which_is_it]
                        del MASKLIST[which_is_it]
                    else:
                        maskblue = TextureStimulus(texture=useTHISmask,position=(518,278), anchor='upperleft', max_alpha=0.50)
                        MASKLIST.append(maskblue)
                        Choice.append(CURRENTLIST[59])
                        ANSWERS=ANSWERS+1
                    screen.clear()
                    viewport.draw()
                    viewportTEXT2.draw()
                    viewportmasks.draw()
                    VisionEgg.Core.swap_buffers()

                elif x >= 517 and x <= 670 and y <= 247 and y >= 218:
                     ##   col4_row__10
                    EXITLIST=[0,0,0]
                    if CURRENTLIST[60] in Choice:
                        ANSWERS=ANSWERS-1
                        which_is_it=Choice.index(CURRENTLIST[60])
                        del Choice[which_is_it]
                        del MASKLIST[which_is_it]
                    else:
                        maskblue = TextureStimulus(texture=useTHISmask,position=(518,248), anchor='upperleft', max_alpha=0.50)
                        MASKLIST.append(maskblue)
                        Choice.append(CURRENTLIST[60])
                        ANSWERS=ANSWERS+1
                    screen.clear()
                    viewport.draw()
                    viewportTEXT2.draw()
                    viewportmasks.draw()
                    VisionEgg.Core.swap_buffers()

                elif x >= 517 and x <= 670 and y <= 217 and y >= 188:
                     ##   col4_row__11
                    EXITLIST=[0,0,0]
                    if CURRENTLIST[61] in Choice:
                        ANSWERS=ANSWERS-1
                        which_is_it=Choice.index(CURRENTLIST[61])
                        del Choice[which_is_it]
                        del MASKLIST[which_is_it]
                    else:
                        maskblue = TextureStimulus(texture=useTHISmask,position=(518,218), anchor='upperleft', max_alpha=0.50)
                        MASKLIST.append(maskblue)
                        Choice.append(CURRENTLIST[61])
                        ANSWERS=ANSWERS+1
                    screen.clear()
                    viewport.draw()
                    viewportTEXT2.draw()
                    viewportmasks.draw()
                    VisionEgg.Core.swap_buffers()

                elif x >= 517 and x <= 670 and y <= 187 and y >= 158:
                     ##   col4_row__12
                    EXITLIST=[0,0,0]
                    if CURRENTLIST[62] in Choice:
                        ANSWERS=ANSWERS-1
                        which_is_it=Choice.index(CURRENTLIST[62])
                        del Choice[which_is_it]
                        del MASKLIST[which_is_it]
                    else:
                        maskblue = TextureStimulus(texture=useTHISmask,position=(518,188), anchor='upperleft', max_alpha=0.50)
                        MASKLIST.append(maskblue)
                        Choice.append(CURRENTLIST[62])
                        ANSWERS=ANSWERS+1
                    screen.clear()
                    viewport.draw()
                    viewportTEXT2.draw()
                    viewportmasks.draw()
                    VisionEgg.Core.swap_buffers()

                elif x >= 517 and x <= 670 and y <= 157 and y >= 128:
                     ##   col4_row__13
                    EXITLIST=[0,0,0]
                    if CURRENTLIST[63] in Choice:
                        ANSWERS=ANSWERS-1
                        which_is_it=Choice.index(CURRENTLIST[63])
                        del Choice[which_is_it]
                        del MASKLIST[which_is_it]
                    else:
                        maskblue = TextureStimulus(texture=useTHISmask,position=(518,158), anchor='upperleft', max_alpha=0.50)
                        MASKLIST.append(maskblue)
                        Choice.append(CURRENTLIST[63])
                        ANSWERS=ANSWERS+1
                    screen.clear()
                    viewport.draw()
                    viewportTEXT2.draw()
                    viewportmasks.draw()
                    VisionEgg.Core.swap_buffers()

                elif x >= 517 and x <= 670 and y <= 127 and y >= 98:
                     ##   col4_row__14
                    EXITLIST=[0,0,0]
                    if CURRENTLIST[64] in Choice:
                        ANSWERS=ANSWERS-1
                        which_is_it=Choice.index(CURRENTLIST[64])
                        del Choice[which_is_it]
                        del MASKLIST[which_is_it]
                    else:
                        maskblue = TextureStimulus(texture=useTHISmask,position=(518,128), anchor='upperleft', max_alpha=0.50)
                        MASKLIST.append(maskblue)
                        Choice.append(CURRENTLIST[64])
                        ANSWERS=ANSWERS+1
                    screen.clear()
                    viewport.draw()
                    viewportTEXT2.draw()
                    viewportmasks.draw()
                    VisionEgg.Core.swap_buffers()

                elif x >= 517 and x <= 670 and y <= 97 and y >= 68:
                     ##   col4_row__15
                    EXITLIST=[0,0,0]
                    if CURRENTLIST[65] in Choice:
                        ANSWERS=ANSWERS-1
                        which_is_it=Choice.index(CURRENTLIST[65])
                        del Choice[which_is_it]
                        del MASKLIST[which_is_it]
                    else:
                        maskblue = TextureStimulus(texture=useTHISmask,position=(518,98), anchor='upperleft', max_alpha=0.50)
                        MASKLIST.append(maskblue)
                        Choice.append(CURRENTLIST[65])
                        ANSWERS=ANSWERS+1
                    screen.clear()
                    viewport.draw()
                    viewportTEXT2.draw()
                    viewportmasks.draw()
                    VisionEgg.Core.swap_buffers()

                elif x >= 517 and x <= 670 and y <= 67 and y >= 38:
                     ##   col4_row__16
                    EXITLIST=[0,0,0]
                    if CURRENTLIST[66] in Choice:
                        ANSWERS=ANSWERS-1
                        which_is_it=Choice.index(CURRENTLIST[66])
                        del Choice[which_is_it]
                        del MASKLIST[which_is_it]
                    else:
                        maskblue = TextureStimulus(texture=useTHISmask,position=(518,68), anchor='upperleft', max_alpha=0.50)
                        MASKLIST.append(maskblue)
                        Choice.append(CURRENTLIST[66])
                        ANSWERS=ANSWERS+1
                    screen.clear()
                    viewport.draw()
                    viewportTEXT2.draw()
                    viewportmasks.draw()
                    VisionEgg.Core.swap_buffers()

                elif x >= 517 and x <= 670 and y <= 37 and y >= 8:
                     ##   col4_row__17
                    EXITLIST=[0,0,0]
                    if CURRENTLIST[67] in Choice:
                        ANSWERS=ANSWERS-1
                        which_is_it=Choice.index(CURRENTLIST[67])
                        del Choice[which_is_it]
                        del MASKLIST[which_is_it]
                    else:
                        maskblue = TextureStimulus(texture=useTHISmask,position=(518,38), anchor='upperleft', max_alpha=0.50)
                        MASKLIST.append(maskblue)
                        Choice.append(CURRENTLIST[67])
                        ANSWERS=ANSWERS+1
                    screen.clear()
                    viewport.draw()
                    viewportTEXT2.draw()
                    viewportmasks.draw()
                    VisionEgg.Core.swap_buffers()

                elif x >= 685 and x <= 836 and y <= 517 and y >= 488:
                     ##   col5_row__1
                    EXITLIST=[0,0,0]
                    if CURRENTLIST[68] in Choice:
                        ANSWERS=ANSWERS-1
                        which_is_it=Choice.index(CURRENTLIST[68])
                        del Choice[which_is_it]
                        del MASKLIST[which_is_it]
                    else:
                        maskblue = TextureStimulus(texture=useTHISmask,position=(686,518), anchor='upperleft', max_alpha=0.50)
                        MASKLIST.append(maskblue)
                        Choice.append(CURRENTLIST[68])
                        ANSWERS=ANSWERS+1
                    screen.clear()
                    viewport.draw()
                    viewportTEXT2.draw()
                    viewportmasks.draw()
                    VisionEgg.Core.swap_buffers()

                elif x >= 685 and x <= 836 and y <= 487 and y >= 458:
                     ##   col5_row__2
                    EXITLIST=[0,0,0]
                    if CURRENTLIST[69] in Choice:
                        ANSWERS=ANSWERS-1
                        which_is_it=Choice.index(CURRENTLIST[69])
                        del Choice[which_is_it]
                        del MASKLIST[which_is_it]
                    else:
                        maskblue = TextureStimulus(texture=useTHISmask,position=(686,488), anchor='upperleft', max_alpha=0.50)
                        MASKLIST.append(maskblue)
                        Choice.append(CURRENTLIST[69])
                        ANSWERS=ANSWERS+1
                    screen.clear()
                    viewport.draw()
                    viewportTEXT2.draw()
                    viewportmasks.draw()
                    VisionEgg.Core.swap_buffers()

                elif x >= 685 and x <= 836 and y <= 457 and y >= 428:
                     ##   col5_row__3
                    EXITLIST=[0,0,0]
                    if CURRENTLIST[70] in Choice:
                        ANSWERS=ANSWERS-1
                        which_is_it=Choice.index(CURRENTLIST[70])
                        del Choice[which_is_it]
                        del MASKLIST[which_is_it]
                    else:
                        maskblue = TextureStimulus(texture=useTHISmask,position=(686,458), anchor='upperleft', max_alpha=0.50)
                        MASKLIST.append(maskblue)
                        Choice.append(CURRENTLIST[70])
                        ANSWERS=ANSWERS+1
                    screen.clear()
                    viewport.draw()
                    viewportTEXT2.draw()
                    viewportmasks.draw()
                    VisionEgg.Core.swap_buffers()

                elif x >= 685 and x <= 836 and y <= 427 and y >= 398:
                     ##   col5_row__4
                    EXITLIST=[0,0,0]
                    if CURRENTLIST[71] in Choice:
                        ANSWERS=ANSWERS-1
                        which_is_it=Choice.index(CURRENTLIST[71])
                        del Choice[which_is_it]
                        del MASKLIST[which_is_it]
                    else:
                        maskblue = TextureStimulus(texture=useTHISmask,position=(686,428), anchor='upperleft', max_alpha=0.50)
                        MASKLIST.append(maskblue)
                        Choice.append(CURRENTLIST[71])
                        ANSWERS=ANSWERS+1
                    screen.clear()
                    viewport.draw()
                    viewportTEXT2.draw()
                    viewportmasks.draw()
                    VisionEgg.Core.swap_buffers()

                elif x >= 685 and x <= 836 and y <= 397 and y >= 368:
                     ##   col5_row__5
                    EXITLIST=[0,0,0]
                    if CURRENTLIST[72] in Choice:
                        ANSWERS=ANSWERS-1
                        which_is_it=Choice.index(CURRENTLIST[72])
                        del Choice[which_is_it]
                        del MASKLIST[which_is_it]
                    else:
                        maskblue = TextureStimulus(texture=useTHISmask,position=(686,398), anchor='upperleft', max_alpha=0.50)
                        MASKLIST.append(maskblue)
                        Choice.append(CURRENTLIST[72])
                        ANSWERS=ANSWERS+1
                    screen.clear()
                    viewport.draw()
                    viewportTEXT2.draw()
                    viewportmasks.draw()
                    VisionEgg.Core.swap_buffers()

                elif x >= 685 and x <= 836 and y <= 367 and y >= 338:
                     ##   col5_row__6
                    EXITLIST=[0,0,0]
                    if CURRENTLIST[73] in Choice:
                        ANSWERS=ANSWERS-1
                        which_is_it=Choice.index(CURRENTLIST[73])
                        del Choice[which_is_it]
                        del MASKLIST[which_is_it]
                    else:
                        maskblue = TextureStimulus(texture=useTHISmask,position=(686,368), anchor='upperleft', max_alpha=0.50)
                        MASKLIST.append(maskblue)
                        Choice.append(CURRENTLIST[73])
                        ANSWERS=ANSWERS+1
                    screen.clear()
                    viewport.draw()
                    viewportTEXT2.draw()
                    viewportmasks.draw()
                    VisionEgg.Core.swap_buffers()

                elif x >= 685 and x <= 836 and y <= 337 and y >= 308:
                     ##   col5_row__7
                    EXITLIST=[0,0,0]
                    if CURRENTLIST[74] in Choice:
                        ANSWERS=ANSWERS-1
                        which_is_it=Choice.index(CURRENTLIST[74])
                        del Choice[which_is_it]
                        del MASKLIST[which_is_it]
                    else:
                        maskblue = TextureStimulus(texture=useTHISmask,position=(686,338), anchor='upperleft', max_alpha=0.50)
                        MASKLIST.append(maskblue)
                        Choice.append(CURRENTLIST[74])
                        ANSWERS=ANSWERS+1
                    screen.clear()
                    viewport.draw()
                    viewportTEXT2.draw()
                    viewportmasks.draw()
                    VisionEgg.Core.swap_buffers()

                elif x >= 685 and x <= 836 and y <= 307 and y >= 278:
                     ##   col5_row__8
                    EXITLIST=[0,0,0]
                    if CURRENTLIST[75] in Choice:
                        ANSWERS=ANSWERS-1
                        which_is_it=Choice.index(CURRENTLIST[75])
                        del Choice[which_is_it]
                        del MASKLIST[which_is_it]
                    else:
                        maskblue = TextureStimulus(texture=useTHISmask,position=(686,308), anchor='upperleft', max_alpha=0.50)
                        MASKLIST.append(maskblue)
                        Choice.append(CURRENTLIST[75])
                        ANSWERS=ANSWERS+1
                    screen.clear()
                    viewport.draw()
                    viewportTEXT2.draw()
                    viewportmasks.draw()
                    VisionEgg.Core.swap_buffers()

                elif x >= 685 and x <= 836 and y <= 277 and y >= 248:
                     ##   col5_row__9
                    EXITLIST=[0,0,0]
                    if CURRENTLIST[76] in Choice:
                        ANSWERS=ANSWERS-1
                        which_is_it=Choice.index(CURRENTLIST[76])
                        del Choice[which_is_it]
                        del MASKLIST[which_is_it]
                    else:
                        maskblue = TextureStimulus(texture=useTHISmask,position=(686,278), anchor='upperleft', max_alpha=0.50)
                        MASKLIST.append(maskblue)
                        Choice.append(CURRENTLIST[76])
                        ANSWERS=ANSWERS+1
                    screen.clear()
                    viewport.draw()
                    viewportTEXT2.draw()
                    viewportmasks.draw()
                    VisionEgg.Core.swap_buffers()

                elif x >= 685 and x <= 836 and y <= 247 and y >= 218:
                     ##   col5_row__10
                    EXITLIST=[0,0,0]
                    if CURRENTLIST[77] in Choice:
                        ANSWERS=ANSWERS-1
                        which_is_it=Choice.index(CURRENTLIST[77])
                        del Choice[which_is_it]
                        del MASKLIST[which_is_it]
                    else:
                        maskblue = TextureStimulus(texture=useTHISmask,position=(686,248), anchor='upperleft', max_alpha=0.50)
                        MASKLIST.append(maskblue)
                        Choice.append(CURRENTLIST[77])
                        ANSWERS=ANSWERS+1
                    screen.clear()
                    viewport.draw()
                    viewportTEXT2.draw()
                    viewportmasks.draw()
                    VisionEgg.Core.swap_buffers()

                elif x >= 685 and x <= 836 and y <= 217 and y >= 188:
                     ##   col5_row__11
                    EXITLIST=[0,0,0]
                    if CURRENTLIST[78] in Choice:
                        ANSWERS=ANSWERS-1
                        which_is_it=Choice.index(CURRENTLIST[78])
                        del Choice[which_is_it]
                        del MASKLIST[which_is_it]
                    else:
                        maskblue = TextureStimulus(texture=useTHISmask,position=(686,218), anchor='upperleft', max_alpha=0.50)
                        MASKLIST.append(maskblue)
                        Choice.append(CURRENTLIST[78])
                        ANSWERS=ANSWERS+1
                    screen.clear()
                    viewport.draw()
                    viewportTEXT2.draw()
                    viewportmasks.draw()
                    VisionEgg.Core.swap_buffers()

                elif x >= 685 and x <= 836 and y <= 187 and y >= 158:
                     ##   col5_row__12
                    EXITLIST=[0,0,0]
                    if CURRENTLIST[79] in Choice:
                        ANSWERS=ANSWERS-1
                        which_is_it=Choice.index(CURRENTLIST[79])
                        del Choice[which_is_it]
                        del MASKLIST[which_is_it]
                    else:
                        maskblue = TextureStimulus(texture=useTHISmask,position=(686,188), anchor='upperleft', max_alpha=0.50)
                        MASKLIST.append(maskblue)
                        Choice.append(CURRENTLIST[79])
                        ANSWERS=ANSWERS+1
                    screen.clear()
                    viewport.draw()
                    viewportTEXT2.draw()
                    viewportmasks.draw()
                    VisionEgg.Core.swap_buffers()

                elif x >= 685 and x <= 836 and y <= 157 and y >= 128:
                     ##   col5_row__13
                    EXITLIST=[0,0,0]
                    if CURRENTLIST[80] in Choice:
                        ANSWERS=ANSWERS-1
                        which_is_it=Choice.index(CURRENTLIST[80])
                        del Choice[which_is_it]
                        del MASKLIST[which_is_it]
                    else:
                        maskblue = TextureStimulus(texture=useTHISmask,position=(686,158), anchor='upperleft', max_alpha=0.50)
                        MASKLIST.append(maskblue)
                        Choice.append(CURRENTLIST[80])
                        ANSWERS=ANSWERS+1
                    screen.clear()
                    viewport.draw()
                    viewportTEXT2.draw()
                    viewportmasks.draw()
                    VisionEgg.Core.swap_buffers()

                elif x >= 685 and x <= 836 and y <= 127 and y >= 98:
                     ##   col5_row__14
                    EXITLIST=[0,0,0]
                    if CURRENTLIST[81] in Choice:
                        ANSWERS=ANSWERS-1
                        which_is_it=Choice.index(CURRENTLIST[81])
                        del Choice[which_is_it]
                        del MASKLIST[which_is_it]
                    else:
                        maskblue = TextureStimulus(texture=useTHISmask,position=(686,128), anchor='upperleft', max_alpha=0.50)
                        MASKLIST.append(maskblue)
                        Choice.append(CURRENTLIST[81])
                        ANSWERS=ANSWERS+1
                    screen.clear()
                    viewport.draw()
                    viewportTEXT2.draw()
                    viewportmasks.draw()
                    VisionEgg.Core.swap_buffers()

                elif x >= 685 and x <= 836 and y <= 97 and y >= 68:
                     ##   col5_row__15
                    EXITLIST=[0,0,0]
                    if CURRENTLIST[82] in Choice:
                        ANSWERS=ANSWERS-1
                        which_is_it=Choice.index(CURRENTLIST[82])
                        del Choice[which_is_it]
                        del MASKLIST[which_is_it]
                    else:
                        maskblue = TextureStimulus(texture=useTHISmask,position=(686,98), anchor='upperleft', max_alpha=0.50)
                        MASKLIST.append(maskblue)
                        Choice.append(CURRENTLIST[82])
                        ANSWERS=ANSWERS+1
                    screen.clear()
                    viewport.draw()
                    viewportTEXT2.draw()
                    viewportmasks.draw()
                    VisionEgg.Core.swap_buffers()

                elif x >= 685 and x <= 836 and y <= 67 and y >= 38:
                     ##   col5_row__16
                    EXITLIST=[0,0,0]
                    if CURRENTLIST[83] in Choice:
                        ANSWERS=ANSWERS-1
                        which_is_it=Choice.index(CURRENTLIST[83])
                        del Choice[which_is_it]
                        del MASKLIST[which_is_it]
                    else:
                        maskblue = TextureStimulus(texture=useTHISmask,position=(686,68), anchor='upperleft', max_alpha=0.50)
                        MASKLIST.append(maskblue)
                        Choice.append(CURRENTLIST[83])
                        ANSWERS=ANSWERS+1
                    screen.clear()
                    viewport.draw()
                    viewportTEXT2.draw()
                    viewportmasks.draw()
                    VisionEgg.Core.swap_buffers()

                elif x >= 685 and x <= 836 and y <= 37 and y >= 8:
                     ##   col5_row__17
                    EXITLIST=[0,0,0]
                    if CURRENTLIST[84] in Choice:
                        ANSWERS=ANSWERS-1
                        which_is_it=Choice.index(CURRENTLIST[84])
                        del Choice[which_is_it]
                        del MASKLIST[which_is_it]
                    else:
                        maskblue = TextureStimulus(texture=useTHISmask,position=(686,38), anchor='upperleft', max_alpha=0.50)
                        MASKLIST.append(maskblue)
                        Choice.append(CURRENTLIST[84])
                        ANSWERS=ANSWERS+1
                    screen.clear()
                    viewport.draw()
                    viewportTEXT2.draw()
                    viewportmasks.draw()
                    VisionEgg.Core.swap_buffers()

                elif x >= 850 and x <= 1003 and y <= 517 and y >= 488:
                     ##   col6_row__1
                    EXITLIST=[0,0,0]
                    if CURRENTLIST[85] in Choice:
                        ANSWERS=ANSWERS-1
                        which_is_it=Choice.index(CURRENTLIST[85])
                        del Choice[which_is_it]
                        del MASKLIST[which_is_it]
                    else:
                        maskblue = TextureStimulus(texture=useTHISmask,position=(851,518), anchor='upperleft', max_alpha=0.50)
                        MASKLIST.append(maskblue)
                        Choice.append(CURRENTLIST[85])
                        ANSWERS=ANSWERS+1
                    screen.clear()
                    viewport.draw()
                    viewportTEXT2.draw()
                    viewportmasks.draw()
                    VisionEgg.Core.swap_buffers()

                elif x >= 850 and x <= 1003 and y <= 487 and y >= 458:
                     ##   col6_row__2
                    EXITLIST=[0,0,0]
                    if CURRENTLIST[86] in Choice:
                        ANSWERS=ANSWERS-1
                        which_is_it=Choice.index(CURRENTLIST[86])
                        del Choice[which_is_it]
                        del MASKLIST[which_is_it]
                    else:
                        maskblue = TextureStimulus(texture=useTHISmask,position=(851,488), anchor='upperleft', max_alpha=0.50)
                        MASKLIST.append(maskblue)
                        Choice.append(CURRENTLIST[86])
                        ANSWERS=ANSWERS+1
                    screen.clear()
                    viewport.draw()
                    viewportTEXT2.draw()
                    viewportmasks.draw()
                    VisionEgg.Core.swap_buffers()

                elif x >= 850 and x <= 1003 and y <= 457 and y >= 428:
                     ##   col6_row__3
                    EXITLIST=[0,0,0]
                    if CURRENTLIST[87] in Choice:
                        ANSWERS=ANSWERS-1
                        which_is_it=Choice.index(CURRENTLIST[87])
                        del Choice[which_is_it]
                        del MASKLIST[which_is_it]
                    else:
                        maskblue = TextureStimulus(texture=useTHISmask,position=(851,458), anchor='upperleft', max_alpha=0.50)
                        MASKLIST.append(maskblue)
                        Choice.append(CURRENTLIST[87])
                        ANSWERS=ANSWERS+1
                    screen.clear()
                    viewport.draw()
                    viewportTEXT2.draw()
                    viewportmasks.draw()
                    VisionEgg.Core.swap_buffers()

                elif x >= 850 and x <= 1003 and y <= 427 and y >= 398:
                     ##   col6_row__4
                    EXITLIST=[0,0,0]
                    if CURRENTLIST[88] in Choice:
                        ANSWERS=ANSWERS-1
                        which_is_it=Choice.index(CURRENTLIST[88])
                        del Choice[which_is_it]
                        del MASKLIST[which_is_it]
                    else:
                        maskblue = TextureStimulus(texture=useTHISmask,position=(851,428), anchor='upperleft', max_alpha=0.50)
                        MASKLIST.append(maskblue)
                        Choice.append(CURRENTLIST[88])
                        ANSWERS=ANSWERS+1
                    screen.clear()
                    viewport.draw()
                    viewportTEXT2.draw()
                    viewportmasks.draw()
                    VisionEgg.Core.swap_buffers()

                elif x >= 850 and x <= 1003 and y <= 397 and y >= 368:
                     ##   col6_row__5
                    EXITLIST=[0,0,0]
                    if CURRENTLIST[89] in Choice:
                        ANSWERS=ANSWERS-1
                        which_is_it=Choice.index(CURRENTLIST[89])
                        del Choice[which_is_it]
                        del MASKLIST[which_is_it]
                    else:
                        maskblue = TextureStimulus(texture=useTHISmask,position=(851,398), anchor='upperleft', max_alpha=0.50)
                        MASKLIST.append(maskblue)
                        Choice.append(CURRENTLIST[89])
                        ANSWERS=ANSWERS+1
                    screen.clear()
                    viewport.draw()
                    viewportTEXT2.draw()
                    viewportmasks.draw()
                    VisionEgg.Core.swap_buffers()

                elif x >= 850 and x <= 1003 and y <= 367 and y >= 338:
                     ##   col6_row__6
                    EXITLIST=[0,0,0]
                    if CURRENTLIST[90] in Choice:
                        ANSWERS=ANSWERS-1
                        which_is_it=Choice.index(CURRENTLIST[90])
                        del Choice[which_is_it]
                        del MASKLIST[which_is_it]
                    else:
                        maskblue = TextureStimulus(texture=useTHISmask,position=(851,368), anchor='upperleft', max_alpha=0.50)
                        MASKLIST.append(maskblue)
                        Choice.append(CURRENTLIST[90])
                        ANSWERS=ANSWERS+1
                    screen.clear()
                    viewport.draw()
                    viewportTEXT2.draw()
                    viewportmasks.draw()
                    VisionEgg.Core.swap_buffers()

                elif x >= 850 and x <= 1003 and y <= 337 and y >= 308:
                     ##   col6_row__7
                    EXITLIST=[0,0,0]
                    if CURRENTLIST[91] in Choice:
                        ANSWERS=ANSWERS-1
                        which_is_it=Choice.index(CURRENTLIST[91])
                        del Choice[which_is_it]
                        del MASKLIST[which_is_it]
                    else:
                        maskblue = TextureStimulus(texture=useTHISmask,position=(851,338), anchor='upperleft', max_alpha=0.50)
                        MASKLIST.append(maskblue)
                        Choice.append(CURRENTLIST[91])
                        ANSWERS=ANSWERS+1
                    screen.clear()
                    viewport.draw()
                    viewportTEXT2.draw()
                    viewportmasks.draw()
                    VisionEgg.Core.swap_buffers()

                elif x >= 850 and x <= 1003 and y <= 307 and y >= 278:
                     ##   col6_row__8
                    EXITLIST=[0,0,0]
                    if CURRENTLIST[92] in Choice:
                        ANSWERS=ANSWERS-1
                        which_is_it=Choice.index(CURRENTLIST[92])
                        del Choice[which_is_it]
                        del MASKLIST[which_is_it]
                    else:
                        maskblue = TextureStimulus(texture=useTHISmask,position=(851,308), anchor='upperleft', max_alpha=0.50)
                        MASKLIST.append(maskblue)
                        Choice.append(CURRENTLIST[92])
                        ANSWERS=ANSWERS+1
                    screen.clear()
                    viewport.draw()
                    viewportTEXT2.draw()
                    viewportmasks.draw()
                    VisionEgg.Core.swap_buffers()

                elif x >= 850 and x <= 1003 and y <= 277 and y >= 248:
                     ##   col6_row__9
                    EXITLIST=[0,0,0]
                    if CURRENTLIST[93] in Choice:
                        ANSWERS=ANSWERS-1
                        which_is_it=Choice.index(CURRENTLIST[93])
                        del Choice[which_is_it]
                        del MASKLIST[which_is_it]
                    else:
                        maskblue = TextureStimulus(texture=useTHISmask,position=(851,278), anchor='upperleft', max_alpha=0.50)
                        MASKLIST.append(maskblue)
                        Choice.append(CURRENTLIST[93])
                        ANSWERS=ANSWERS+1
                    screen.clear()
                    viewport.draw()
                    viewportTEXT2.draw()
                    viewportmasks.draw()
                    VisionEgg.Core.swap_buffers()

                elif x >= 850 and x <= 1003 and y <= 247 and y >= 218:
                     ##   col6_row__10
                    EXITLIST=[0,0,0]
                    if CURRENTLIST[94] in Choice:
                        ANSWERS=ANSWERS-1
                        which_is_it=Choice.index(CURRENTLIST[94])
                        del Choice[which_is_it]
                        del MASKLIST[which_is_it]
                    else:
                        maskblue = TextureStimulus(texture=useTHISmask,position=(851,248), anchor='upperleft', max_alpha=0.50)
                        MASKLIST.append(maskblue)
                        Choice.append(CURRENTLIST[94])
                        ANSWERS=ANSWERS+1
                    screen.clear()
                    viewport.draw()
                    viewportTEXT2.draw()
                    viewportmasks.draw()
                    VisionEgg.Core.swap_buffers()

                elif x >= 850 and x <= 1003 and y <= 217 and y >= 188:
                     ##   col6_row__11
                    EXITLIST=[0,0,0]
                    if CURRENTLIST[95] in Choice:
                        ANSWERS=ANSWERS-1
                        which_is_it=Choice.index(CURRENTLIST[95])
                        del Choice[which_is_it]
                        del MASKLIST[which_is_it]
                    else:
                        maskblue = TextureStimulus(texture=useTHISmask,position=(851,218), anchor='upperleft', max_alpha=0.50)
                        MASKLIST.append(maskblue)
                        Choice.append(CURRENTLIST[95])
                        ANSWERS=ANSWERS+1
                    screen.clear()
                    viewport.draw()
                    viewportTEXT2.draw()
                    viewportmasks.draw()
                    VisionEgg.Core.swap_buffers()

                elif x >= 850 and x <= 1003 and y <= 187 and y >= 158:
                     ##   col6_row__12
                    EXITLIST=[0,0,0]
                    if CURRENTLIST[96] in Choice:
                        ANSWERS=ANSWERS-1
                        which_is_it=Choice.index(CURRENTLIST[96])
                        del Choice[which_is_it]
                        del MASKLIST[which_is_it]
                    else:
                        maskblue = TextureStimulus(texture=useTHISmask,position=(851,188), anchor='upperleft', max_alpha=0.50)
                        MASKLIST.append(maskblue)
                        Choice.append(CURRENTLIST[96])
                        ANSWERS=ANSWERS+1
                    screen.clear()
                    viewport.draw()
                    viewportTEXT2.draw()
                    viewportmasks.draw()
                    VisionEgg.Core.swap_buffers()

                elif x >= 850 and x <= 1003 and y <= 157 and y >= 128:
                     ##   col6_row__13
                    EXITLIST=[0,0,0]
                    if CURRENTLIST[97] in Choice:
                        ANSWERS=ANSWERS-1
                        which_is_it=Choice.index(CURRENTLIST[97])
                        del Choice[which_is_it]
                        del MASKLIST[which_is_it]
                    else:
                        maskblue = TextureStimulus(texture=useTHISmask,position=(851,158), anchor='upperleft', max_alpha=0.50)
                        MASKLIST.append(maskblue)
                        Choice.append(CURRENTLIST[97])
                        ANSWERS=ANSWERS+1
                    screen.clear()
                    viewport.draw()
                    viewportTEXT2.draw()
                    viewportmasks.draw()
                    VisionEgg.Core.swap_buffers()

                elif x >= 850 and x <= 1003 and y <= 127 and y >= 98:
                     ##   col6_row__14
                    EXITLIST=[0,0,0]
                    if CURRENTLIST[98] in Choice:
                        ANSWERS=ANSWERS-1
                        which_is_it=Choice.index(CURRENTLIST[98])
                        del Choice[which_is_it]
                        del MASKLIST[which_is_it]
                    else:
                        maskblue = TextureStimulus(texture=useTHISmask,position=(851,128), anchor='upperleft', max_alpha=0.50)
                        MASKLIST.append(maskblue)
                        Choice.append(CURRENTLIST[98])
                        ANSWERS=ANSWERS+1
                    screen.clear()
                    viewport.draw()
                    viewportTEXT2.draw()
                    viewportmasks.draw()
                    VisionEgg.Core.swap_buffers()

                elif x >= 850 and x <= 1003 and y <= 97 and y >= 68:
                     ##   col6_row__15
                    EXITLIST=[0,0,0]
                    if CURRENTLIST[99] in Choice:
                        ANSWERS=ANSWERS-1
                        which_is_it=Choice.index(CURRENTLIST[99])
                        del Choice[which_is_it]
                        del MASKLIST[which_is_it]
                    else:
                        maskblue = TextureStimulus(texture=useTHISmask,position=(851,98), anchor='upperleft', max_alpha=0.50)
                        MASKLIST.append(maskblue)
                        Choice.append(CURRENTLIST[99])
                        ANSWERS=ANSWERS+1
                    screen.clear()
                    viewport.draw()
                    viewportTEXT2.draw()
                    viewportmasks.draw()
                    VisionEgg.Core.swap_buffers()

                      
                ##
                ## now we see the practical application of the EXITLIST:
                elif x >= 0 and x <=24 and y >= 584 and y <=600:
                   if EXITLIST==[0,0,0]:
                       EXITLIST[0]=1
                       text0 = Text(text="O",color=(0,0,0),position=(0,600),font_size=30,anchor='center')
                       text1 = Text(text="O",color=(0,0,0),position=(0,600),font_size=30,anchor='center')
                       viewportTEXT = VisionEgg.Core.Viewport(screen=screen, size=screen.size, stimuli=[text0, text1])
                       VisionEgg.Core.swap_buffers()
                       screen.clear()
                       viewport.draw()
                       viewportmasks.draw()
                       viewportTEXT.draw()
                       viewportTEXT2.draw()
                       VisionEgg.Core.swap_buffers()
                elif x >= 1008 and x <=1024 and y >= 584 and y <=600:
                    if EXITLIST==[1,0,0]:
                       EXITLIST[1]=1
                       text0 = Text(text="O",color=(0,0,0),position=(0,600),font_size=30,anchor='center')
                       text1 = Text(text="O",color=(0,0,0),position=(1024,600),font_size=30,anchor='center')
                       viewportTEXT = VisionEgg.Core.Viewport(screen=screen, size=screen.size, stimuli=[text0, text1])
                       VisionEgg.Core.swap_buffers()
                       screen.clear()
                       viewport.draw()
                       viewportmasks.draw()
                       viewportTEXT.draw()
                       viewportTEXT2.draw()
                       VisionEgg.Core.swap_buffers()
                elif x >= 1008 and x <=1024 and y >= 0 and y <=16:
                    if EXITLIST==[1,1,0]:
                        ScreenNumber, RESET = ESCAPEscreenLATE(ScreenNumber, RESET)
###  ###   ###  # #     ### ALWAYS REMEMBER TO UPDATE THE RETURN INFO!  ##   #   #   #####  ##  ###    ### ### 
                        return ScreenNumber, TrialTime, RESPONSE, ERRORS, RESET
                        StartTrial=True





###########################################################################################
                        ########################################################
                        #######################################################
                        ##########################################
############################################################################################
                        ##########################################

                    ################
                        ###############


###########################################################################################
                        ########################################################
                        #######################################################
                        ##########################################
############################################################################################
                        ##########################################

                    ################
                        ##########################################################################################################
                        ########################################################
                        #######################################################
                        ##########################################
############################################################################################
                        ##########################################

                    ################
                        ###############


def DRAWTASKODD(ScreenNumber, TrialTime, RESPONSE, ERRORS, RESET):
    x=-1
    y=-1
    #make and show background
    backgroundIMAGE = TextureStimulus(texture=drawingbackgrounds[(ScreenNumber-37)],position=(0,0))
    viewport = VisionEgg.Core.Viewport(screen=screen, size=screen.size, stimuli=[backgroundIMAGE,backgroundIMAGE])
    warnBOX_early = TextureStimulus(texture=notyetboxes[17],position=(830,150), anchor='center', max_alpha=0.90)
    warnBOX_late = TextureStimulus(texture=notyetboxes[18],position=(830,150), anchor='center', max_alpha=0.90)
    viewportwarnBOX_early = VisionEgg.Core.Viewport(screen=screen, size=screen.size, stimuli=[warnBOX_early])
    viewportwarnBOX_late = VisionEgg.Core.Viewport(screen=screen, size=screen.size, stimuli=[warnBOX_late])
    useTHISmask=masks[7]
    maskblue2 = TextureStimulus(texture=useTHISmask,position=(-100,-100), anchor='center', max_alpha=0.50)    
    MASKLIST=[maskblue2]
     ## we'll modify the MASKLIST depending on button presses....
    viewportmasks = VisionEgg.Core.Viewport(screen=screen, size=screen.size, stimuli=MASKLIST)
    ##
    EXITLIST=[0,0,0]
    ANSWERS=0
    Choice=[" "]
    ERRORS=0
    ##
    screen.clear()
    viewport.draw()
    VisionEgg.Core.swap_buffers()
    startTIME=int(round(time() * 1000))
    screen.clear()
    viewport.draw()
    viewportmasks.draw()
    VisionEgg.Core.swap_buffers()
    StartTrial=False
    LATESTLIST=["ONE","TWO","THREE","FOUR","FIVE","SIX"]
    while not StartTrial:
        for event in pygame.event.get():
            if event.type == pygame.locals.MOUSEBUTTONDOWN:
                if (int(round(time() * 1000))-startTIME) > 100:
                    x,y = pygame.mouse.get_pos()
## pygame.mouse.get_pos() gives coordinates with the LOWER LEFT, not UPPER LEFT (as in visionegg) corner as the origin.
## before we get too complicated, will probably want to flip things around:
                y=600-y
                if x >= 903 and x <=996 and y >=0 and y <=37:
                    EXITLIST=[0,0,0]
                    ## the "touch here when done" box. Action depends on whether there's a full answer.
                    if ANSWERS == 2:
                        RESPONSE=sorted(Choice)
                        ## trial time is in seconds
                        TrialTime=int(round(time() * 1000))-startTIME
                        return ScreenNumber, TrialTime, RESPONSE, ERRORS, RESET
                        StartTrial=True                       
                    elif ANSWERS < 2:
                        ERRORS=ERRORS+1
                        screen.clear()
                        viewport.draw()
                        viewportmasks.draw()
                        viewportwarnBOX_early.draw() #it'll stay up until something else is clicked
                        VisionEgg.Core.swap_buffers()
                    elif ANSWERS > 2:
                        ERRORS=ERRORS+1
                        screen.clear()
                        viewport.draw()
                        viewportmasks.draw()
                        viewportwarnBOX_late.draw() #it'll stay up until something else is clicked
                        VisionEgg.Core.swap_buffers()
                                        
                elif x >= 288  and x <= 431 and y <= 303 and y >= 160:
                     ##   col1_row__1
                    EXITLIST=[0,0,0]
                    if LATESTLIST[0] in Choice:
                        ANSWERS=ANSWERS-1
                        which_is_it=Choice.index(LATESTLIST[0])
                        del Choice[which_is_it]
                        del MASKLIST[which_is_it]
                    else:
                        maskblue = TextureStimulus(texture=useTHISmask,position=(288,303), anchor='upperleft', max_alpha=0.50)
                        MASKLIST.append(maskblue)
                        Choice.append(LATESTLIST[0])
                        ANSWERS=ANSWERS+1
                    screen.clear()
                    viewport.draw()
                    viewportmasks.draw()
                    VisionEgg.Core.swap_buffers()

                elif x >= 439 and x <= 585 and y <= 303 and y >= 160:
                     ##   col2_row__1
                    EXITLIST=[0,0,0]
                    if LATESTLIST[1] in Choice:
                        ANSWERS=ANSWERS-1
                        which_is_it=Choice.index(LATESTLIST[1])
                        del Choice[which_is_it]
                        del MASKLIST[which_is_it]
                    else:
                        maskblue = TextureStimulus(texture=useTHISmask,position=(439,303), anchor='upperleft', max_alpha=0.50)
                        MASKLIST.append(maskblue)
                        Choice.append(LATESTLIST[1])
                        ANSWERS=ANSWERS+1
                    screen.clear()
                    viewport.draw()
                    viewportmasks.draw()
                    VisionEgg.Core.swap_buffers()

                elif x >= 592 and x <= 738 and y <= 303 and y >= 160:
                     ##   col3_row__1
                    EXITLIST=[0,0,0]
                    if LATESTLIST[2] in Choice:
                        ANSWERS=ANSWERS-1
                        which_is_it=Choice.index(LATESTLIST[2])
                        del Choice[which_is_it]
                        del MASKLIST[which_is_it]
                    else:
                        maskblue = TextureStimulus(texture=useTHISmask,position=(592,303), anchor='upperleft', max_alpha=0.50)
                        MASKLIST.append(maskblue)
                        Choice.append(LATESTLIST[2])
                        ANSWERS=ANSWERS+1
                    screen.clear()
                    viewport.draw()
                    viewportmasks.draw()
                    VisionEgg.Core.swap_buffers()
                                        
                elif x >= 288  and x <= 431 and y <= 151 and y >= 7:
                     ##   col1_row__2
                    EXITLIST=[0,0,0]
                    if LATESTLIST[3] in Choice:
                        ANSWERS=ANSWERS-1
                        which_is_it=Choice.index(LATESTLIST[3])
                        del Choice[which_is_it]
                        del MASKLIST[which_is_it]
                    else:
                        maskblue = TextureStimulus(texture=useTHISmask,position=(288,151), anchor='upperleft', max_alpha=0.50)
                        MASKLIST.append(maskblue)
                        Choice.append(LATESTLIST[3])
                        ANSWERS=ANSWERS+1
                    screen.clear()
                    viewport.draw()
                    viewportmasks.draw()
                    VisionEgg.Core.swap_buffers()

                elif x >= 439 and x <= 585 and y <= 151 and y >= 7:
                     ##   col2_row__2
                    EXITLIST=[0,0,0]
                    if LATESTLIST[4] in Choice:
                        ANSWERS=ANSWERS-1
                        which_is_it=Choice.index(LATESTLIST[4])
                        del Choice[which_is_it]
                        del MASKLIST[which_is_it]
                    else:
                        maskblue = TextureStimulus(texture=useTHISmask,position=(439,151), anchor='upperleft', max_alpha=0.50)
                        MASKLIST.append(maskblue)
                        Choice.append(LATESTLIST[4])
                        ANSWERS=ANSWERS+1
                    screen.clear()
                    viewport.draw()
                    viewportmasks.draw()
                    VisionEgg.Core.swap_buffers()

                elif x >= 592 and x <= 738 and y <= 151 and y >= 7:
                     ##   col3_row__2
                    EXITLIST=[0,0,0]
                    if LATESTLIST[5] in Choice:
                        ANSWERS=ANSWERS-1
                        which_is_it=Choice.index(LATESTLIST[5])
                        del Choice[which_is_it]
                        del MASKLIST[which_is_it]
                    else:
                        maskblue = TextureStimulus(texture=useTHISmask,position=(592,151), anchor='upperleft', max_alpha=0.50)
                        MASKLIST.append(maskblue)
                        Choice.append(LATESTLIST[5])
                        ANSWERS=ANSWERS+1
                    screen.clear()
                    viewport.draw()
                    viewportmasks.draw()
                    VisionEgg.Core.swap_buffers()
                ##
                ## now we see the practical application of the EXITLIST:
                elif x >= 0 and x <=24 and y >= 584 and y <=600:
                   if EXITLIST==[0,0,0]:
                       EXITLIST[0]=1
                       text0 = Text(text="O",color=(0,0,0),position=(0,600),font_size=30,anchor='center')
                       text1 = Text(text="O",color=(0,0,0),position=(0,600),font_size=30,anchor='center')
                       viewportTEXT = VisionEgg.Core.Viewport(screen=screen, size=screen.size, stimuli=[text0, text1])
                       VisionEgg.Core.swap_buffers()
                       screen.clear()
                       viewport.draw()
                       viewportmasks.draw()
                       viewportTEXT.draw()
                       VisionEgg.Core.swap_buffers()
                elif x >= 1008 and x <=1024 and y >= 584 and y <=600:
                    if EXITLIST==[1,0,0]:
                       EXITLIST[1]=1
                       text0 = Text(text="O",color=(0,0,0),position=(0,600),font_size=30,anchor='center')
                       text1 = Text(text="O",color=(0,0,0),position=(1024,600),font_size=30,anchor='center')
                       viewportTEXT = VisionEgg.Core.Viewport(screen=screen, size=screen.size, stimuli=[text0, text1])
                       VisionEgg.Core.swap_buffers()
                       screen.clear()
                       viewport.draw()
                       viewportmasks.draw()
                       viewportTEXT.draw()
                       VisionEgg.Core.swap_buffers()
                elif x >= 1008 and x <=1024 and y >= 0 and y <=16:
                    if EXITLIST==[1,1,0]:
                        ScreenNumber, RESET = ESCAPEscreenLATE(ScreenNumber, RESET)
###  ###   ###  # #     ### ALWAYS REMEMBER TO UPDATE THE RETURN INFO!  ##   #   #   #####  ##  ###    ### ### 
                        return ScreenNumber, TrialTime, RESPONSE, ERRORS, RESET
                        StartTrial=True



def DRAWTASKEVEN(ScreenNumber, TrialTime, RESPONSE, ERRORS, RESET):
    x=-1
    y=-1
    #make and show background
    backgroundIMAGE = TextureStimulus(texture=drawingbackgrounds[(ScreenNumber-37)],position=(0,0))
    viewport = VisionEgg.Core.Viewport(screen=screen, size=screen.size, stimuli=[backgroundIMAGE,backgroundIMAGE])
    warnBOX_early = TextureStimulus(texture=notyetboxes[17],position=(830,150), anchor='center', max_alpha=0.90)
    warnBOX_late = TextureStimulus(texture=notyetboxes[18],position=(830,150), anchor='center', max_alpha=0.90)
    viewportwarnBOX_early = VisionEgg.Core.Viewport(screen=screen, size=screen.size, stimuli=[warnBOX_early])
    viewportwarnBOX_late = VisionEgg.Core.Viewport(screen=screen, size=screen.size, stimuli=[warnBOX_late])
    useTHISmask=masks[7]
    maskblue = TextureStimulus(texture=useTHISmask,position=(-100,-100), anchor='center', max_alpha=0.50)    
    MASKLIST=[maskblue]
     ## we'll modify the MASKLIST depending on button presses....
    viewportmasks = VisionEgg.Core.Viewport(screen=screen, size=screen.size, stimuli=MASKLIST)
    ##
    EXITLIST=[0,0,0]
    ANSWERS=0
    Choice=[" "]
    ERRORS=0
    ##
    screen.clear()
    viewport.draw()
    VisionEgg.Core.swap_buffers()
    startTIME=int(round(time() * 1000))
    screen.clear()
    viewport.draw()
    viewportmasks.draw()
    VisionEgg.Core.swap_buffers()
    StartTrial=False
    LATESTLIST=["ONE","TWO","THREE","FOUR","FIVE","SIX"]
    while not StartTrial:
        for event in pygame.event.get():
            if event.type == pygame.locals.MOUSEBUTTONDOWN:
                if (int(round(time() * 1000))-startTIME) > 100:
                    x,y = pygame.mouse.get_pos()
## pygame.mouse.get_pos() gives coordinates with the LOWER LEFT, not UPPER LEFT (as in visionegg) corner as the origin.
## before we get too complicated, will probably want to flip things around:
                y=600-y
                if x >= 930 and x <=1024 and y >=36 and y <=71:
                    EXITLIST=[0,0,0]
                    ## the "touch here when done" box. Action depends on whether there's a full answer.
                    if ANSWERS == 2:
                        RESPONSE=sorted(Choice)
                        ## trial time is in seconds
                        TrialTime=int(round(time() * 1000))-startTIME
                        return ScreenNumber, TrialTime, RESPONSE, ERRORS, RESET
                        StartTrial=True                       
                    elif ANSWERS < 2:
                        ERRORS=ERRORS+1
                        screen.clear()
                        viewport.draw()
                        viewportmasks.draw()
                        viewportwarnBOX_early.draw() #it'll stay up until something else is clicked
                        VisionEgg.Core.swap_buffers()
                    elif ANSWERS > 2:
                        ERRORS=ERRORS+1
                        screen.clear()
                        viewport.draw()
                        viewportmasks.draw()
                        viewportwarnBOX_late.draw() #it'll stay up until something else is clicked
                        VisionEgg.Core.swap_buffers()
                                        
                elif x >= 288  and x <= 431 and y <= 303 and y >= 160:
                     ##   col1_row__1
                    EXITLIST=[0,0,0]
                    if LATESTLIST[0] in Choice:
                        ANSWERS=ANSWERS-1
                        which_is_it=Choice.index(LATESTLIST[0])
                        del Choice[which_is_it]
                        del MASKLIST[which_is_it]
                    else:
                        maskblue = TextureStimulus(texture=useTHISmask,position=(288,303), anchor='upperleft', max_alpha=0.50)
                        MASKLIST.append(maskblue)
                        Choice.append(LATESTLIST[0])
                        ANSWERS=ANSWERS+1
                    screen.clear()
                    viewport.draw()
                    viewportmasks.draw()
                    VisionEgg.Core.swap_buffers()

                elif x >= 439 and x <= 585 and y <= 303 and y >= 160:
                     ##   col2_row__1
                    EXITLIST=[0,0,0]
                    if LATESTLIST[1] in Choice:
                        ANSWERS=ANSWERS-1
                        which_is_it=Choice.index(LATESTLIST[1])
                        del Choice[which_is_it]
                        del MASKLIST[which_is_it]
                    else:
                        maskblue = TextureStimulus(texture=useTHISmask,position=(439,303), anchor='upperleft', max_alpha=0.50)
                        MASKLIST.append(maskblue)
                        Choice.append(LATESTLIST[1])
                        ANSWERS=ANSWERS+1
                    screen.clear()
                    viewport.draw()
                    viewportmasks.draw()
                    VisionEgg.Core.swap_buffers()

                elif x >= 592 and x <= 738 and y <= 303 and y >= 160:
                     ##   col3_row__1
                    EXITLIST=[0,0,0]
                    if LATESTLIST[2] in Choice:
                        ANSWERS=ANSWERS-1
                        which_is_it=Choice.index(LATESTLIST[2])
                        del Choice[which_is_it]
                        del MASKLIST[which_is_it]
                    else:
                        maskblue = TextureStimulus(texture=useTHISmask,position=(592,303), anchor='upperleft', max_alpha=0.50)
                        MASKLIST.append(maskblue)
                        Choice.append(LATESTLIST[2])
                        ANSWERS=ANSWERS+1
                    screen.clear()
                    viewport.draw()
                    viewportmasks.draw()
                    VisionEgg.Core.swap_buffers()
                                        
                elif x >= 288  and x <= 431 and y <= 151 and y >= 7:
                     ##   col1_row__2
                    EXITLIST=[0,0,0]
                    if LATESTLIST[3] in Choice:
                        ANSWERS=ANSWERS-1
                        which_is_it=Choice.index(LATESTLIST[3])
                        del Choice[which_is_it]
                        del MASKLIST[which_is_it]
                    else:
                        maskblue = TextureStimulus(texture=useTHISmask,position=(288,151), anchor='upperleft', max_alpha=0.50)
                        MASKLIST.append(maskblue)
                        Choice.append(LATESTLIST[3])
                        ANSWERS=ANSWERS+1
                    screen.clear()
                    viewport.draw()
                    viewportmasks.draw()
                    VisionEgg.Core.swap_buffers()

                elif x >= 439 and x <= 585 and y <= 151 and y >= 7:
                     ##   col2_row__2
                    EXITLIST=[0,0,0]
                    if LATESTLIST[4] in Choice:
                        ANSWERS=ANSWERS-1
                        which_is_it=Choice.index(LATESTLIST[4])
                        del Choice[which_is_it]
                        del MASKLIST[which_is_it]
                    else:
                        maskblue = TextureStimulus(texture=useTHISmask,position=(439,151), anchor='upperleft', max_alpha=0.50)
                        MASKLIST.append(maskblue)
                        Choice.append(LATESTLIST[4])
                        ANSWERS=ANSWERS+1
                    screen.clear()
                    viewport.draw()
                    viewportmasks.draw()
                    VisionEgg.Core.swap_buffers()

                elif x >= 592 and x <= 738 and y <= 151 and y >= 7:
                     ##   col3_row__2
                    EXITLIST=[0,0,0]
                    if LATESTLIST[5] in Choice:
                        ANSWERS=ANSWERS-1
                        which_is_it=Choice.index(LATESTLIST[5])
                        del Choice[which_is_it]
                        del MASKLIST[which_is_it]
                    else:
                        maskblue = TextureStimulus(texture=useTHISmask,position=(592,151), anchor='upperleft', max_alpha=0.50)
                        MASKLIST.append(maskblue)
                        Choice.append(LATESTLIST[5])
                        ANSWERS=ANSWERS+1
                    screen.clear()
                    viewport.draw()
                    viewportmasks.draw()
                    VisionEgg.Core.swap_buffers()
                ##
                ## now we see the practical application of the EXITLIST:
                elif x >= 0 and x <=24 and y >= 584 and y <=600:
                   if EXITLIST==[0,0,0]:
                       EXITLIST[0]=1
                       text0 = Text(text="O",color=(0,0,0),position=(0,600),font_size=30,anchor='center')
                       text1 = Text(text="O",color=(0,0,0),position=(0,600),font_size=30,anchor='center')
                       viewportTEXT = VisionEgg.Core.Viewport(screen=screen, size=screen.size, stimuli=[text0, text1])
                       VisionEgg.Core.swap_buffers()
                       screen.clear()
                       viewport.draw()
                       viewportmasks.draw()
                       viewportTEXT.draw()
                       VisionEgg.Core.swap_buffers()
                elif x >= 1008 and x <=1024 and y >= 584 and y <=600:
                    if EXITLIST==[1,0,0]:
                       EXITLIST[1]=1
                       text0 = Text(text="O",color=(0,0,0),position=(0,600),font_size=30,anchor='center')
                       text1 = Text(text="O",color=(0,0,0),position=(1024,600),font_size=30,anchor='center')
                       viewportTEXT = VisionEgg.Core.Viewport(screen=screen, size=screen.size, stimuli=[text0, text1])
                       VisionEgg.Core.swap_buffers()
                       screen.clear()
                       viewport.draw()
                       viewportmasks.draw()
                       viewportTEXT.draw()
                       VisionEgg.Core.swap_buffers()
                elif x >= 1008 and x <=1024 and y >= 0 and y <=16:
                    if EXITLIST==[1,1,0]:
                        ScreenNumber, RESET = ESCAPEscreenLATE(ScreenNumber, RESET)
###  ###   ###  # #     ### ALWAYS REMEMBER TO UPDATE THE RETURN INFO!  ##   #   #   #####  ##  ###    ### ### 
                        return ScreenNumber, TrialTime, RESPONSE, ERRORS, RESET
                        StartTrial=True



####################################################################################################
####################################################################################################
####################################################################################################
####################################################################################################
####################################################################################################
def MONEYPAD(ScreenNumber, TrialTime, RESPONSE, ERRORS, RESET):
    x=-1
    y=-1
    EXITLIST=[0,0,0]
    POSITION=0 # which of the four number positions are we at? (in NUMBERBANK)
    RESPONSE=0
    ERRORS=0
    TrialTime=-1
    FIRST_OR_SECOND=1
    NUMBERBANK=[" "," "]
    text0 = Text(text=NUMBERBANK[0],
                 color=(0,0.5,0),
                 position=(511,450), 
                 font_size=60,
                 anchor='center')
    text1 = Text(text=NUMBERBANK[1],
                 color=(0,0,0),
                 position=(590,450),
                 font_size=60,
                 anchor='center')
    warnBOX = TextureStimulus(texture=notyetboxes[13],position=(830,150), anchor='center', max_alpha=0.80)
    viewportwarnBOX = VisionEgg.Core.Viewport(screen=screen, size=screen.size, stimuli=[warnBOX])
    if ScreenNumber == 34:
        backgroundIMAGE = TextureStimulus(texture=taskbackgrounds[13],position=(0,0))
        viewport = VisionEgg.Core.Viewport(screen=screen, size=screen.size, stimuli=[backgroundIMAGE])
    elif ScreenNumber == 35:
        backgroundIMAGE = TextureStimulus(texture=taskbackgrounds[14],position=(0,0))
        viewport = VisionEgg.Core.Viewport(screen=screen, size=screen.size, stimuli=[backgroundIMAGE]) 
        FIRST_OR_SECOND=2
    viewportTEXT2 = VisionEgg.Core.Viewport(screen=screen, size=screen.size, stimuli=[text0, text1])
    #VisionEgg.Core.swap_buffers()
    screen.clear()
    LASTTAP=0
    viewport.draw()
    viewportTEXT2.draw()
    VisionEgg.Core.swap_buffers()
    StartTrial=False
    startTIME=int(round(time() * 1000))
    screen.clear()
    viewport.draw()
    viewportTEXT2.draw()
    VisionEgg.Core.swap_buffers()
    while not StartTrial:
        for event in pygame.event.get():
            if event.type == pygame.locals.MOUSEBUTTONDOWN:
                if (int(round(time() * 1000))-startTIME) > 100:
                    x,y = pygame.mouse.get_pos()
## pygame.mouse.get_pos() gives coordinates with the LOWER LEFT, not UPPER LEFT (as in visionegg) corner as the origin.
## before we get too complicated, will probably want to flip things around:
                y=600-y
                if x >= 930 and x <=1024 and y >=36 and y <=71 and FIRST_OR_SECOND==1:
                    EXITLIST=[0,0,0]
                    ## the "touch here when done" box. Action depends on whether there's a full answer.
                    ## i.e., if POSITION=4
                    if NUMBERBANK[0] != " ":
                        MOTOR_SPEED_LOG.append(int((round(time() * 1000))-startTIME)-LASTTAP)
                        LASTTAP=int((round(time() * 1000))-startTIME)
                    if POSITION == 1 and NUMBERBANK[1] != " ":
                        out_file.write('   NEXT_at_ms %d NA NA NA %d\n'%((int(round(time() * 1000))-startTIME),ScreenNumber))
                        TrialTime=int(round(time() * 1000))-startTIME
                        RESPONSE=int(NUMBERBANK[0]+NUMBERBANK[1])
                        return ScreenNumber, TrialTime, RESPONSE, ERRORS, RESET
                        StartTrial=True                       
                    else:
                        out_file.write('   NEXT_at_ms %d NA NA NA %d\n'%((int(round(time() * 1000))-startTIME),ScreenNumber))
                        ERRORS=ERRORS+1
                        screen.clear()
                        viewport.draw()
                        viewportTEXT2.draw()
                        viewportwarnBOX.draw()
                        VisionEgg.Core.swap_buffers()
                elif x >= 904  and x <= 997  and y >= 0  and y <=36 and FIRST_OR_SECOND==2:
                    EXITLIST=[0,0,0]
                    ## the "touch here when done" box. Action depends on whether there's a full answer.
                    ## i.e., if POSITION=4
                    if NUMBERBANK[1] != " ":
                        MOTOR_SPEED_LOG.append(int((round(time() * 1000))-startTIME)-LASTTAP)
                        LASTTAP=int((round(time() * 1000))-startTIME)
                    if POSITION == 1 and NUMBERBANK[1] != " ":
                        out_file.write('   NEXT_at_ms %d NA NA NA %d\n'%((int(round(time() * 1000))-startTIME),ScreenNumber))
                        TrialTime=int(round(time() * 1000))-startTIME
                        RESPONSE=int(NUMBERBANK[0]+NUMBERBANK[1])
                        return ScreenNumber, TrialTime, RESPONSE, ERRORS, RESET
                        StartTrial=True                       
                    else:
                        out_file.write('   NEXT_at_ms %d NA NA NA %d\n'%((int(round(time() * 1000))-startTIME),ScreenNumber))
                        ERRORS=ERRORS+1
                        screen.clear()
                        viewport.draw()
                        viewportTEXT2.draw()
                        viewportwarnBOX.draw()
                        VisionEgg.Core.swap_buffers()
    
                        
                elif x >= 406 and x <=474 and y >=322 and y <=386:
                    MOTOR_SPEED_LOG.append(int((round(time() * 1000))-startTIME)-LASTTAP)
                    LASTTAP=int((round(time() * 1000))-startTIME)
                    EXITLIST=[0,0,0]
                    ## button 1
                    NUMBERBANK[POSITION]="1"
                    out_file.write('   button1_at_ms %d NA NA NA %d\n'%((int(round(time() * 1000))-startTIME),ScreenNumber))
                    screen.clear()
                    text0 = Text(text=NUMBERBANK[0],color=(0,0,0),position=(511,450),font_size=60,anchor='center')
                    text1 = Text(text=NUMBERBANK[1],color=(0,0,0),position=(580,450),font_size=60,anchor='center')
                    viewportTEXT2 = VisionEgg.Core.Viewport(screen=screen, size=screen.size, stimuli=[text0, text1])
                    viewport.draw()
                    viewportTEXT2.draw()
                    VisionEgg.Core.swap_buffers()
                    if POSITION < 1:
                        ## advance position
                        POSITION=POSITION+1
                elif x >= 406 and x <=474 and y >=251 and y <=314:
                    MOTOR_SPEED_LOG.append(int((round(time() * 1000))-startTIME)-LASTTAP)
                    LASTTAP=int((round(time() * 1000))-startTIME)
                    EXITLIST=[0,0,0]
                    ## button 4
                    NUMBERBANK[POSITION]="4"
                    out_file.write('   button4_at_ms %d NA NA NA %d\n'%((int(round(time() * 1000))-startTIME),ScreenNumber))
                    screen.clear()
                    text0 = Text(text=NUMBERBANK[0],color=(0,0,0),position=(511,450),font_size=60,anchor='center')
                    text1 = Text(text=NUMBERBANK[1],color=(0,0,0),position=(580,450),font_size=60,anchor='center')
                    viewportTEXT2 = VisionEgg.Core.Viewport(screen=screen, size=screen.size, stimuli=[text0, text1])
                    viewport.draw()
                    viewportTEXT2.draw()
                    VisionEgg.Core.swap_buffers()
                    if POSITION < 1:
                        ## advance position
                        POSITION=POSITION+1
                elif x >= 406 and x <=474 and y >=180 and y <=245:
                    MOTOR_SPEED_LOG.append(int((round(time() * 1000))-startTIME)-LASTTAP)
                    LASTTAP=int((round(time() * 1000))-startTIME)
                    EXITLIST=[0,0,0]
                    ## button 7
                    NUMBERBANK[POSITION]="7"
                    out_file.write('   button7_at_ms %d NA NA NA %d\n'%((int(round(time() * 1000))-startTIME),ScreenNumber))
                    screen.clear()
                    text0 = Text(text=NUMBERBANK[0],color=(0,0,0),position=(511,450),font_size=60,anchor='center')
                    text1 = Text(text=NUMBERBANK[1],color=(0,0,0),position=(580,450),font_size=60,anchor='center')
                    viewportTEXT2 = VisionEgg.Core.Viewport(screen=screen, size=screen.size, stimuli=[text0, text1])
                    viewport.draw()
                    viewportTEXT2.draw()
                    VisionEgg.Core.swap_buffers()
                    if POSITION < 1:
                        ## advance position
                        POSITION=POSITION+1
                    
                elif x >= 479 and x <=546 and y >=109 and y <=174:
                    MOTOR_SPEED_LOG.append(int((round(time() * 1000))-startTIME)-LASTTAP)
                    LASTTAP=int((round(time() * 1000))-startTIME)
                    EXITLIST=[0,0,0]
                    ## button 0
                    NUMBERBANK[POSITION]="0"
                    out_file.write('   button0_at_ms %d NA NA NA %d\n'%((int(round(time() * 1000))-startTIME),ScreenNumber))
                    screen.clear()
                    text0 = Text(text=NUMBERBANK[0],color=(0,0,0),position=(511,450),font_size=60,anchor='center')
                    text1 = Text(text=NUMBERBANK[1],color=(0,0,0),position=(580,450),font_size=60,anchor='center')
                    viewportTEXT2 = VisionEgg.Core.Viewport(screen=screen, size=screen.size, stimuli=[text0, text1])
                    viewport.draw()
                    viewportTEXT2.draw()
                    VisionEgg.Core.swap_buffers()
                    if POSITION < 1:
                        ## advance position
                        POSITION=POSITION+1

                elif x >= 479 and x <=546 and y >=322 and y <=386:
                    MOTOR_SPEED_LOG.append(int((round(time() * 1000))-startTIME)-LASTTAP)
                    LASTTAP=int((round(time() * 1000))-startTIME)
                    EXITLIST=[0,0,0]
                    ## button 2
                    NUMBERBANK[POSITION]="2"
                    out_file.write('   button2_at_ms %d NA NA NA %d\n'%((int(round(time() * 1000))-startTIME),ScreenNumber))
                    screen.clear()
                    text0 = Text(text=NUMBERBANK[0],color=(0,0,0),position=(511,450),font_size=60,anchor='center')
                    text1 = Text(text=NUMBERBANK[1],color=(0,0,0),position=(580,450),font_size=60,anchor='center')
                    viewportTEXT2 = VisionEgg.Core.Viewport(screen=screen, size=screen.size, stimuli=[text0, text1])
                    viewport.draw()
                    viewportTEXT2.draw()
                    VisionEgg.Core.swap_buffers()
                    if POSITION < 1:
                        ## advance position
                        POSITION=POSITION+1
                elif x >= 479 and x <=546 and y >=251 and y <=314:
                    MOTOR_SPEED_LOG.append(int((round(time() * 1000))-startTIME)-LASTTAP)
                    LASTTAP=int((round(time() * 1000))-startTIME)
                    EXITLIST=[0,0,0]
                    ## button 5
                    NUMBERBANK[POSITION]="5"
                    out_file.write('   button5_at_ms %d NA NA NA %d\n'%((int(round(time() * 1000))-startTIME),ScreenNumber))
                    screen.clear()
                    text0 = Text(text=NUMBERBANK[0],color=(0,0,0),position=(511,450),font_size=60,anchor='center')
                    text1 = Text(text=NUMBERBANK[1],color=(0,0,0),position=(580,450),font_size=60,anchor='center')
                    viewportTEXT2 = VisionEgg.Core.Viewport(screen=screen, size=screen.size, stimuli=[text0, text1])
                    viewport.draw()
                    viewportTEXT2.draw()
                    VisionEgg.Core.swap_buffers()
                    if POSITION < 1:
                        ## advance position
                        POSITION=POSITION+1
                elif x >= 479 and x <=546 and y >=180 and y <=245:
                    MOTOR_SPEED_LOG.append(int((round(time() * 1000))-startTIME)-LASTTAP)
                    LASTTAP=int((round(time() * 1000))-startTIME)
                    EXITLIST=[0,0,0]
                    ## button 8
                    NUMBERBANK[POSITION]="8"
                    out_file.write('   button8_at_ms %d NA NA NA %d\n'%((int(round(time() * 1000))-startTIME),ScreenNumber))
                    screen.clear()
                    text0 = Text(text=NUMBERBANK[0],color=(0,0,0),position=(511,450),font_size=60,anchor='center')
                    text1 = Text(text=NUMBERBANK[1],color=(0,0,0),position=(580,450),font_size=60,anchor='center')
                    viewportTEXT2 = VisionEgg.Core.Viewport(screen=screen, size=screen.size, stimuli=[text0, text1])
                    viewport.draw()
                    viewportTEXT2.draw()
                    VisionEgg.Core.swap_buffers()
                    if POSITION < 1:
                        ## advance position
                        POSITION=POSITION+1

                elif x >= 552 and x <=620 and y >=322 and y <=386:
                    MOTOR_SPEED_LOG.append(int((round(time() * 1000))-startTIME)-LASTTAP)
                    LASTTAP=int((round(time() * 1000))-startTIME)
                    EXITLIST=[0,0,0]
                    ## button 3
                    NUMBERBANK[POSITION]="3"
                    out_file.write('   button3_at_ms %d NA NA NA %d\n'%((int(round(time() * 1000))-startTIME),ScreenNumber))
                    screen.clear()
                    text0 = Text(text=NUMBERBANK[0],color=(0,0,0),position=(511,450),font_size=60,anchor='center')
                    text1 = Text(text=NUMBERBANK[1],color=(0,0,0),position=(580,450),font_size=60,anchor='center')
                    viewportTEXT2 = VisionEgg.Core.Viewport(screen=screen, size=screen.size, stimuli=[text0, text1])
                    viewport.draw()
                    viewportTEXT2.draw()
                    VisionEgg.Core.swap_buffers()
                    if POSITION < 1:
                        ## advance position
                        POSITION=POSITION+1
                elif x >= 552 and x <=620 and y >=251 and y <=314:
                    MOTOR_SPEED_LOG.append(int((round(time() * 1000))-startTIME)-LASTTAP)
                    LASTTAP=int((round(time() * 1000))-startTIME)
                    EXITLIST=[0,0,0]
                    ## button 6
                    NUMBERBANK[POSITION]="6"
                    out_file.write('   button6_at_ms %d NA NA NA %d\n'%((int(round(time() * 1000))-startTIME),ScreenNumber))
                    screen.clear()
                    text0 = Text(text=NUMBERBANK[0],color=(0,0,0),position=(511,450),font_size=60,anchor='center')
                    text1 = Text(text=NUMBERBANK[1],color=(0,0,0),position=(580,450),font_size=60,anchor='center')
                    viewportTEXT2 = VisionEgg.Core.Viewport(screen=screen, size=screen.size, stimuli=[text0, text1])
                    viewport.draw()
                    viewportTEXT2.draw()
                    VisionEgg.Core.swap_buffers()
                    if POSITION < 1:
                        ## advance position
                        POSITION=POSITION+1
                elif x >= 552 and x <=620 and y >=180 and y <=245:
                    MOTOR_SPEED_LOG.append(int((round(time() * 1000))-startTIME)-LASTTAP)
                    LASTTAP=int((round(time() * 1000))-startTIME)
                    EXITLIST=[0,0,0]
                    ## button 9
                    NUMBERBANK[POSITION]="9"
                    out_file.write('   button9_at_ms %d NA NA NA %d\n'%((int(round(time() * 1000))-startTIME),ScreenNumber))
                    screen.clear()
                    text0 = Text(text=NUMBERBANK[0],color=(0,0,0),position=(511,450),font_size=60,anchor='center')
                    text1 = Text(text=NUMBERBANK[1],color=(0,0,0),position=(580,450),font_size=60,anchor='center')
                    viewportTEXT2 = VisionEgg.Core.Viewport(screen=screen, size=screen.size, stimuli=[text0, text1])
                    viewport.draw()
                    viewportTEXT2.draw()
                    VisionEgg.Core.swap_buffers()
                    if POSITION < 1:
                        ## advance position
                        POSITION=POSITION+1
 
                elif x >= 419 and x <=609 and y >=40 and y <=94:
                    MOTOR_SPEED_LOG.append(int((round(time() * 1000))-startTIME)-LASTTAP)
                    LASTTAP=int((round(time() * 1000))-startTIME)
                    EXITLIST=[0,0,0]
                    out_file.write('   buttonDELETE_at_ms %d NA NA NA %d\n'%((int(round(time() * 1000))-startTIME),ScreenNumber))
                    ## DELETE button
                    ## if POSITION == 0, do nothing. This means there are no numbers
                    ## if POSITION == 1, you just wrote your first number (in POSITION 0) and then shifted over
                    ##  OR, you were in POSITION 2 ready to write there, but instead hit delete, which made you step back
                    ##  a position and wipe the value in NUMBERBANK[1].
                    ##  either way, if POSITION == 1, we want to wipe NUMBERBANK[0] and set POSITION to 0
                    if POSITION > 0:
                        if POSITION == 1 and NUMBERBANK[1] != " ":
                            NUMBERBANK[POSITION]=" "
                        else:
                            POSITION=POSITION-1
                            NUMBERBANK[POSITION]=" "                            
                        screen.clear()
                        text0 = Text(text=NUMBERBANK[0],color=(0,0,0),position=(511,450),font_size=60,anchor='center')
                        text1 = Text(text=NUMBERBANK[1],color=(0,0,0),position=(580,450),font_size=60,anchor='center')
                        viewportTEXT2 = VisionEgg.Core.Viewport(screen=screen, size=screen.size, stimuli=[text0, text1])
                        viewport.draw()
                        viewportTEXT2.draw()
                        VisionEgg.Core.swap_buffers()
                ##
                ## now we see the practical application of the EXITLIST:
                elif x >= 0 and x <=24 and y >= 584 and y <=600:
                   if EXITLIST==[0,0,0]:
                       EXITLIST[0]=1
                       text0 = Text(text="O",color=(0,0,0),position=(0,600),font_size=30,anchor='center')
                       text1 = Text(text="O",color=(0,0,0),position=(0,600),font_size=30,anchor='center')
                       viewportTEXT = VisionEgg.Core.Viewport(screen=screen, size=screen.size, stimuli=[text0, text1])
                       VisionEgg.Core.swap_buffers()
                       screen.clear()
                       viewport.draw()
                       viewportTEXT.draw()
                       viewportTEXT2.draw()
                       VisionEgg.Core.swap_buffers()
                elif x >= 1008 and x <=1024 and y >= 584 and y <=600:
                    if EXITLIST==[1,0,0]:
                       EXITLIST[1]=1
                       text0 = Text(text="O",color=(0,0,0),position=(0,600),font_size=30,anchor='center')
                       text1 = Text(text="O",color=(0,0,0),position=(1024,600),font_size=30,anchor='center')
                       viewportTEXT = VisionEgg.Core.Viewport(screen=screen, size=screen.size, stimuli=[text0, text1])
                       VisionEgg.Core.swap_buffers()
                       screen.clear()
                       viewport.draw()
                       viewportTEXT.draw()
                       viewportTEXT2.draw()
                       VisionEgg.Core.swap_buffers()
                elif x >= 1008 and x <=1024 and y >= 0 and y <=16:
                    if EXITLIST==[1,1,0]:
                        ScreenNumber, RESET = ESCAPEscreenLATE(ScreenNumber, RESET)
###  ###   ###  # #     ### ALWAYS REMEMBER TO UPDATE THE RETURN INFO!  ##   #   #   #####  ##  ###    ### ### 
                        return ScreenNumber, TrialTime, RESPONSE, ERRORS, RESET
                        StartTrial=True






####################################################################################################
####################################################################################################
####################################################################################################
####################################################################################################
####################################################################################################
def STROOPODD(ScreenNumber, TrialTime, ERRORBUNDLE, RESET, WORD, TEXTCOLOR, SelectionTime):
    #reset variables
    x=-1
    y=-1
    ERRORS=ERRORBUNDLE[0]
    TRUEERRORS=ERRORBUNDLE[1]
    EXITLIST=[0,0,0]
    ANSWERED=0
    Choice=[" "]
    ERRORS=0
    TRUEERRORS=0
    #make and show background
    backgroundIMAGE = TextureStimulus(texture=stroopSCREEN[(ScreenNumber-42)],position=(0,0))
    viewport = VisionEgg.Core.Viewport(screen=screen, size=screen.size, stimuli=[backgroundIMAGE])
    warnBOX = TextureStimulus(texture=stroopNOTYETselect,position=(830,150), anchor='center', max_alpha=0.80)
    warnBOX2 = TextureStimulus(texture=stroopNOTYETreselect,position=(830,150), anchor='center', max_alpha=0.80)
    viewportwarnBOX = VisionEgg.Core.Viewport(screen=screen, size=screen.size, stimuli=[warnBOX])
    viewportwarnBOX2 = VisionEgg.Core.Viewport(screen=screen, size=screen.size, stimuli=[warnBOX2])
    useTHISmask=stroopMASK
    maskblue = TextureStimulus(texture=useTHISmask,position=(-100,-100), anchor='center', max_alpha=0.50)    
    MASKLIST=[maskblue]
     ## we'll modify the MASKLIST depending on button presses....
    viewportmasks = VisionEgg.Core.Viewport(screen=screen, size=screen.size, stimuli=MASKLIST)
    screen.clear()
    viewport.draw()
    VisionEgg.Core.swap_buffers()
    screen.clear()
    viewport.draw()
    VisionEgg.Core.swap_buffers()
    # start clock
    startTIME=int(round(time() * 1000))
    StartTrial=False
    while not StartTrial:
        for event in pygame.event.get():
            if event.type == pygame.locals.MOUSEBUTTONDOWN:
                #
                if (int(round(time() * 1000))-startTIME) > 100:
                    x,y = pygame.mouse.get_pos()
## pygame.mouse.get_pos() gives coordinates with the LOWER LEFT, not UPPER LEFT (as in visionegg) corner as the origin.
## before we get too complicated, will probably want to flip things around:
                y=600-y
                if x >= 930 and x <=1024 and y >=36 and y <=71:  ##<-this is only difference between stroopEVEN and stroopODD
#                if x >= 904  and x <= 997  and y >= 0  and y <=36 :  ##<-this is only difference between stroopEVEN and stroopODD
                    EXITLIST=[0,0,0]
                    ## the "touch here when done" box. Action depends on ANSWERED
                    if ANSWERED == 1 and Choice[0]==TEXTCOLOR:
                        ## trial time is in seconds
                        TrialTime=int(round(time() * 1000))-startTIME
                        #YearAnswer=int(NUMBERBANK[0]+NUMBERBANK[1]+NUMBERBANK[2]+NUMBERBANK[3])
                        ERRORBUNDLE[0]=ERRORS
                        ERRORBUNDLE[1]=TRUEERRORS
                        return ScreenNumber, TrialTime, ERRORBUNDLE, RESET, WORD, TEXTCOLOR, SelectionTime
                        StartTrial=True                       
                    elif ANSWERED == 1 and Choice[0]!=TEXTCOLOR:
                        TRUEERRORS=TRUEERRORS+1
                        screen.clear()
                        viewport.draw()
                        viewportmasks.draw()
                        #show the warning box to select something different
                        viewportwarnBOX2.draw()
                        VisionEgg.Core.swap_buffers()
                        #it'll stay up until something else is clicked
                    else:
                        ERRORS=ERRORS+1
                        screen.clear()
                        viewport.draw()
                        viewportmasks.draw()
                        #show the warning box to select something
                        viewportwarnBOX.draw()
                        VisionEgg.Core.swap_buffers()
                        #it'll stay up until something else is clicked


                elif x >= 352  and x <= 505  and y <= 215  and y >= 160 :
                   ## GREEN
                    EXITLIST=[0,0,0]
                    if Choice[0]=="green":
                        # if already selected, unselect and move pertinent mask offscreen
                        maskblue = TextureStimulus(texture=useTHISmask,position=(-200,-200), anchor='upperleft', max_alpha=0.50)
                        MASKLIST[0]=maskblue
                        Choice[0]=" "
                        ANSWERED=0
                    else:
                        # otherwise, select and move pertinent mask over the word
                        maskblue = TextureStimulus(texture=useTHISmask,position=(352,215), anchor='upperleft', max_alpha=0.50)
                        MASKLIST[0]=maskblue
                        Choice[0]="green"
                        ANSWERED=1
                        SelectionTime=int(round(time() * 1000))-startTIME
                    screen.clear()
                    viewport.draw()
                    viewportmasks.draw()
                    VisionEgg.Core.swap_buffers()
                elif x >= 519  and x <= 674  and y <= 215  and y >=160 :
                   ## RED
                    EXITLIST=[0,0,0]
                    if Choice[0]=="red":
                        # if already selected, unselect and move pertinent mask offscreen
                        maskblue = TextureStimulus(texture=useTHISmask,position=(-200,-200), anchor='upperleft', max_alpha=0.50)
                        MASKLIST[0]=maskblue
                        Choice[0]=" "
                        ANSWERED=0
                    else:
                        # otherwise, select and move pertinent mask over the word
                        maskblue = TextureStimulus(texture=useTHISmask,position=(519,215), anchor='upperleft', max_alpha=0.50)
                        MASKLIST[0]=maskblue
                        Choice[0]="red"
                        ANSWERED=1
                        SelectionTime=int(round(time() * 1000))-startTIME
                    screen.clear()
                    viewport.draw()
                    viewportmasks.draw()
                    VisionEgg.Core.swap_buffers()
                elif x >= 352  and x <= 505  and y <= 146  and y >= 90 :
                   ## BLUE
                    EXITLIST=[0,0,0]
                    if Choice[0]=="blue":
                        # if already selected, unselect and move pertinent mask offscreen
                        maskblue = TextureStimulus(texture=useTHISmask,position=(-200,-200), anchor='upperleft', max_alpha=0.50)
                        MASKLIST[0]=maskblue
                        Choice[0]=" "
                        ANSWERED=0
                    else:
                        # otherwise, select and move pertinent mask over the word
                        maskblue = TextureStimulus(texture=useTHISmask,position=(352,146), anchor='upperleft', max_alpha=0.50)
                        MASKLIST[0]=maskblue
                        Choice[0]="blue"
                        ANSWERED=1
                        SelectionTime=int(round(time() * 1000))-startTIME
                    screen.clear()
                    viewport.draw()
                    viewportmasks.draw()
                    VisionEgg.Core.swap_buffers()
                ##
                ## now we see the practical application of the EXITLIST:
                elif x >= 0 and x <=24 and y >= 584 and y <=600:
                   if EXITLIST==[0,0,0]:
                       EXITLIST[0]=1
                       text0 = Text(text="O",color=(0,0,0),position=(0,600),font_size=30,anchor='center')
                       text1 = Text(text="O",color=(0,0,0),position=(0,600),font_size=30,anchor='center')
                       viewportTEXT = VisionEgg.Core.Viewport(screen=screen, size=screen.size, stimuli=[text0, text1])
                       VisionEgg.Core.swap_buffers()
                       screen.clear()
                       viewport.draw()
                       viewportmasks.draw()
                       viewportTEXT.draw()
                       VisionEgg.Core.swap_buffers()
                elif x >= 1008 and x <=1024 and y >= 584 and y <=600:
                    if EXITLIST==[1,0,0]:
                       EXITLIST[1]=1
                       text0 = Text(text="O",color=(0,0,0),position=(0,600),font_size=30,anchor='center')
                       text1 = Text(text="O",color=(0,0,0),position=(1024,600),font_size=30,anchor='center')
                       viewportTEXT = VisionEgg.Core.Viewport(screen=screen, size=screen.size, stimuli=[text0, text1])
                       VisionEgg.Core.swap_buffers()
                       screen.clear()
                       viewport.draw()
                       viewportmasks.draw()
                       viewportTEXT.draw()
                       VisionEgg.Core.swap_buffers()
                elif x >= 1008 and x <=1024 and y >= 0 and y <=16:
                    if EXITLIST==[1,1,0]:
                        ScreenNumber, RESET = ESCAPEscreenLATE(ScreenNumber, RESET)
###  ###   ###  # #     ### ALWAYS REMEMBER TO UPDATE THE RETURN INFO!  ##   #   #   #####  ##  ###    ### ### 
                        return ScreenNumber, TrialTime, ERRORBUNDLE, RESET, WORD, TEXTCOLOR, SelectionTime
                        StartTrial=True


def STROOPEVEN(ScreenNumber, TrialTime, ERRORBUNDLE, RESET, WORD, TEXTCOLOR, SelectionTime):
    #reset variables
    x=-1
    y=-1
    EXITLIST=[0,0,0]
    ANSWERED=0
    ERRORS=ERRORBUNDLE[0]
    TRUEERRORS=ERRORBUNDLE[1]
    Choice=[" "]
    ERRORS=0
    TRUEERRORS=0
    #make and show background
    backgroundIMAGE = TextureStimulus(texture=stroopSCREEN[(ScreenNumber-42)],position=(0,0))
    viewport = VisionEgg.Core.Viewport(screen=screen, size=screen.size, stimuli=[backgroundIMAGE])
    warnBOX = TextureStimulus(texture=stroopNOTYETselect,position=(830,150), anchor='center', max_alpha=0.80)
    warnBOX2 = TextureStimulus(texture=stroopNOTYETreselect,position=(830,150), anchor='center', max_alpha=0.80)
    viewportwarnBOX = VisionEgg.Core.Viewport(screen=screen, size=screen.size, stimuli=[warnBOX])
    viewportwarnBOX2 = VisionEgg.Core.Viewport(screen=screen, size=screen.size, stimuli=[warnBOX2])
    useTHISmask=stroopMASK
    maskblue = TextureStimulus(texture=useTHISmask,position=(-100,-100), anchor='center', max_alpha=0.50)    
    MASKLIST=[maskblue]
     ## we'll modify the MASKLIST depending on button presses....
    viewportmasks = VisionEgg.Core.Viewport(screen=screen, size=screen.size, stimuli=MASKLIST)
    screen.clear()
    viewport.draw()
    VisionEgg.Core.swap_buffers()
    screen.clear()
    viewport.draw()
    VisionEgg.Core.swap_buffers()
    # start clock
    startTIME=int(round(time() * 1000))
    StartTrial=False
    while not StartTrial:
        for event in pygame.event.get():
            if event.type == pygame.locals.MOUSEBUTTONDOWN:
                # only update x and y with values if more than 50ms have passed
                if (int(round(time() * 1000))-startTIME) > 100:
                    x,y = pygame.mouse.get_pos()
## pygame.mouse.get_pos() gives coordinates with the LOWER LEFT, not UPPER LEFT (as in visionegg) corner as the origin.
## before we get too complicated, will probably want to flip things around:
                y=600-y
                if x >= 904  and x <= 997  and y >= 0  and y <=36 :  ##<-this is only difference between stroopEVEN and stroopODD
#                if x >= 930 and x <=1024 and y >=36 and y <=71:  ##<-this is only difference between stroopEVEN and stroopODD
                    EXITLIST=[0,0,0]
                    ## the "touch here when done" box. Action depends on ANSWERED
                    if ANSWERED == 1 and Choice[0]==TEXTCOLOR:
                        ## trial time is in seconds
                        TrialTime=int(round(time() * 1000))-startTIME
                        #YearAnswer=int(NUMBERBANK[0]+NUMBERBANK[1]+NUMBERBANK[2]+NUMBERBANK[3])
                        ERRORBUNDLE[0]=ERRORS
                        ERRORBUNDLE[1]=TRUEERRORS
                        return ScreenNumber, TrialTime, ERRORBUNDLE, RESET, WORD, TEXTCOLOR, SelectionTime
                        StartTrial=True                       
                    elif ANSWERED == 1 and Choice[0]!=TEXTCOLOR:
                        TRUEERRORS=TRUEERRORS+1
                        screen.clear()
                        viewport.draw()
                        viewportmasks.draw()
                        #show the warning box to select something different
                        viewportwarnBOX2.draw()
                        VisionEgg.Core.swap_buffers()
                        #it'll stay up until something else is clicked
                    else:
                        ERRORS=ERRORS+1
                        screen.clear()
                        viewport.draw()
                        viewportmasks.draw()
                        #show the warning box to select something
                        viewportwarnBOX.draw()
                        VisionEgg.Core.swap_buffers()
                        #it'll stay up until something else is clicked


                elif x >= 352  and x <= 505  and y <= 215  and y >= 160 :
                   ## GREEN
                    EXITLIST=[0,0,0]
                    if Choice[0]=="green":
                        # if already selected, unselect and move pertinent mask offscreen
                        maskblue = TextureStimulus(texture=useTHISmask,position=(-200,-200), anchor='upperleft', max_alpha=0.50)
                        MASKLIST[0]=maskblue
                        Choice[0]=" "
                        ANSWERED=0
                    else:
                        # otherwise, select and move pertinent mask over the word
                        maskblue = TextureStimulus(texture=useTHISmask,position=(352,215), anchor='upperleft', max_alpha=0.50)
                        MASKLIST[0]=maskblue
                        Choice[0]="green"
                        ANSWERED=1
                        SelectionTime=int(round(time() * 1000))-startTIME
                    screen.clear()
                    viewport.draw()
                    viewportmasks.draw()
                    VisionEgg.Core.swap_buffers()
                elif x >= 519  and x <= 674  and y <= 215  and y >=160 :
                   ## RED
                    EXITLIST=[0,0,0]
                    if Choice[0]=="red":
                        # if already selected, unselect and move pertinent mask offscreen
                        maskblue = TextureStimulus(texture=useTHISmask,position=(-200,-200), anchor='upperleft', max_alpha=0.50)
                        MASKLIST[0]=maskblue
                        Choice[0]=" "
                        ANSWERED=0
                    else:
                        # otherwise, select and move pertinent mask over the word
                        maskblue = TextureStimulus(texture=useTHISmask,position=(519,215), anchor='upperleft', max_alpha=0.50)
                        MASKLIST[0]=maskblue
                        Choice[0]="red"
                        ANSWERED=1
                        SelectionTime=int(round(time() * 1000))-startTIME
                    screen.clear()
                    viewport.draw()
                    viewportmasks.draw()
                    VisionEgg.Core.swap_buffers()
                elif x >= 352  and x <= 505  and y <= 146  and y >= 90 :
                   ## BLUE
                    EXITLIST=[0,0,0]
                    if Choice[0]=="blue":
                        # if already selected, unselect and move pertinent mask offscreen
                        maskblue = TextureStimulus(texture=useTHISmask,position=(-200,-200), anchor='upperleft', max_alpha=0.50)
                        MASKLIST[0]=maskblue
                        Choice[0]=" "
                        ANSWERED=0
                    else:
                        # otherwise, select and move pertinent mask over the word
                        maskblue = TextureStimulus(texture=useTHISmask,position=(352,146), anchor='upperleft', max_alpha=0.50)
                        MASKLIST[0]=maskblue
                        Choice[0]="blue"
                        ANSWERED=1
                        SelectionTime=int(round(time() * 1000))-startTIME
                    screen.clear()
                    viewport.draw()
                    viewportmasks.draw()
                    VisionEgg.Core.swap_buffers()
                ##
                ## now we see the practical application of the EXITLIST:
                elif x >= 0 and x <=24 and y >= 584 and y <=600:
                   if EXITLIST==[0,0,0]:
                       EXITLIST[0]=1
                       text0 = Text(text="O",color=(0,0,0),position=(0,600),font_size=30,anchor='center')
                       text1 = Text(text="O",color=(0,0,0),position=(0,600),font_size=30,anchor='center')
                       viewportTEXT = VisionEgg.Core.Viewport(screen=screen, size=screen.size, stimuli=[text0, text1])
                       VisionEgg.Core.swap_buffers()
                       screen.clear()
                       viewport.draw()
                       viewportmasks.draw()
                       viewportTEXT.draw()
                       VisionEgg.Core.swap_buffers()
                elif x >= 1008 and x <=1024 and y >= 584 and y <=600:
                    if EXITLIST==[1,0,0]:
                       EXITLIST[1]=1
                       text0 = Text(text="O",color=(0,0,0),position=(0,600),font_size=30,anchor='center')
                       text1 = Text(text="O",color=(0,0,0),position=(1024,600),font_size=30,anchor='center')
                       viewportTEXT = VisionEgg.Core.Viewport(screen=screen, size=screen.size, stimuli=[text0, text1])
                       VisionEgg.Core.swap_buffers()
                       screen.clear()
                       viewport.draw()
                       viewportmasks.draw()
                       viewportTEXT.draw()
                       VisionEgg.Core.swap_buffers()
                elif x >= 1008 and x <=1024 and y >= 0 and y <=16:
                    if EXITLIST==[1,1,0]:
                        ScreenNumber, RESET = ESCAPEscreenLATE(ScreenNumber, RESET)
###  ###   ###  # #     ### ALWAYS REMEMBER TO UPDATE THE RETURN INFO!  ##   #   #   #####  ##  ###    ### ### 
                        return ScreenNumber, TrialTime, ERRORBUNDLE, RESET, WORD, TEXTCOLOR, SelectionTime
                        StartTrial=True




#######################################################################################################
#######################################################################################################
################################  TRAILS MODULES BELOW HERE ###########################################
#######################################################################################################
#######################################################################################################

#######################################################################################################
#######################################################################################################
################################  TRAILS MODULES BELOW HERE ###########################################
#######################################################################################################
#######################################################################################################

#######################################################################################################
#######################################################################################################
################################  TRAILS MODULES BELOW HERE ###########################################
#######################################################################################################
#######################################################################################################

#######################################################################################################
#######################################################################################################
################################  TRAILS MODULES BELOW HERE ###########################################
#######################################################################################################
#######################################################################################################
                        
#######################################################################################################
#######################################################################################################
################################  TRAILS MODULES BELOW HERE ###########################################
#######################################################################################################
#######################################################################################################
def TRAILSa(ScreenNumber, TrialTime, ERRORS, ATTEMPTS_TO_END_EARLY):
    warnBOX = TextureStimulus(texture=notyetboxes[16],position=(785,282), anchor='upperleft', max_alpha=1.0)
    viewportwarnBOX = VisionEgg.Core.Viewport(screen=screen, size=screen.size, stimuli=[warnBOX])
    BUTTON=0
    ERRORS=0
    ID=" "
    JustFlagged=False
    ATTEMPTS_TO_END_EARLY=0
    POINTSx=-100
    POINTSy=-100
    EndTrial=False
    ## PRE-populate lineLIST with the connecting lines, so that we don't have to recaclulate them each time we loop through.
    ## the first line is a blank.
    line = Target2D(size  = (1.0,1.0),
                    color      = (0.0,0.0,0.0),
                    orientation = 0, #angle
                    position=(-100,-100),
                    anchor='upperleft')
    lineLIST=[line]
    # the center of each button:
    #centerXs=[383,544,654,525,561]
    #centerYs=[252,439,239,298,143]
    # leads to the following (just do in excel and hard-code before-hand to limit load on python)
    # coordinates for the N_tials-1 connecting lines:    
    lineXcenters=[463,599,589,543]
    lineYcenters=[291,285,214,166]
    line_angles=[49.3,-61.2,-24.6,-76.9]
    line_lengths=[247,229,141,160]
#    for x in range(0,(len(lineXcenters)-1)):
    for x in range(0,(len(lineXcenters))):
        line = Target2D(size  = (line_lengths[x],5.0),
                    color      = (0.0,0.0,0.0),
                    orientation = line_angles[x],
                    position=(lineXcenters[x],lineYcenters[x]),
                    anchor='center')
        lineLIST.append(line)
    stim = TextureStimulus(texture=trailsbackgrounds[0],position=(0,0))
    screen.clear()
    background = VisionEgg.Core.Viewport(screen=screen, size=screen.size, stimuli=[stim])
    maskGREEN = TextureStimulus(texture=TRAILSmaskGREEN,position=(-100,-100), anchor='center', max_alpha=0.50)
    maskLIST=[maskGREEN,maskGREEN]
    masks = VisionEgg.Core.Viewport(screen=screen, size=screen.size, stimuli=maskLIST)
    lines = Viewport(screen=screen, stimuli=[lineLIST[0]])
## this is from tutorial:
#    target = Target2D(size  = (25.0,10.0),
#                      color      = (0.0,0.0,0.0,1.0), # Set the target color (RGBA) black
#                      orientation = -45.0)
#    lines = Viewport(screen=screen, stimuli=[target])
## </>this is from tutorial:
#    lines = Viewport(screen=screen, stimuli=[line])
    screen.clear()
    background.draw()
    masks.draw()
    lines.draw()
    VisionEgg.Core.swap_buffers()
    startTIME=int(round(time() * 1000))
    while not EndTrial:
        for event in pygame.event.get():
            if event.type == pygame.locals.MOUSEBUTTONDOWN:
                ## next few lines new for 0-6-4. trying to get tabelt to behave well.
                xOld,yOld = pygame.mouse.get_pos()
                yOld=600-yOld
                downtime=int(round(time() * 1000))
                MouseUp=False
                while not MouseUp:
                    ## next few lines new for 0-6-4. trying to get tabelt to behave well.
                    if (int(round(time() * 1000))-downtime) > 50:
                        if xOld==x and yOld==y:
                            MouseUp=True
    ## the next two lines basically say to get the x and y position of the cursor when a mousedown happens...
                    x,y = pygame.mouse.get_pos()
    ## pygame.mouse.get_pos() gives coordinates with the LOWER LEFT, not UPPER LEFT (as in visionegg) corner as the origin.
                    y=600-y
                    screen.clear()
                    background.draw()
                    masks.draw()
                    lines.draw()
                    if JustFlagged:
                        viewportwarnBOX.draw()
                    if x >= 930 and x <= 1024 and y >= 34 and y <=71 and not JustFlagged:
                        if BUTTON == 5:
                            TrialTime=int(round(time() * 1000))-startTIME
                            out_file.write('   NEXT_at_ms %d\n'%(int(round(time() * 1000))-startTIME))
                            return ScreenNumber, TrialTime, ERRORS, ATTEMPTS_TO_END_EARLY
                            StartTrial=True                     
                        elif BUTTON < 5:
                            out_file.write('   NEXT_at_ms %d\n'%(int(round(time() * 1000))-startTIME))
                            ATTEMPTS_TO_END_EARLY=ATTEMPTS_TO_END_EARLY+1
##                            screen.clear()
##                            background.draw()
##                            masks.draw()
##                            lines.draw()
                            viewportwarnBOX.draw()
                            VisionEgg.Core.swap_buffers()
##                            screen.clear()
##                            background.draw()
##                            masks.draw()
##                            lines.draw()
                            viewportwarnBOX.draw()
                            VisionEgg.Core.swap_buffers()
                            JustFlagged=True
                    else:
                        # draw a line from wherever the inital point is to the current.
                        if POINTSx > -100 and not JustFlagged:  ## if we haven't really started yet,ignore next stuff
                            ydiff=float(int(y-POINTSy))+0.1
                            xdiff=float(int(x-POINTSx))+0.1
                            line_length=int(((xdiff**2)+(ydiff**2))**0.5)
                            angler=180*(arctan(ydiff/xdiff)/3.14159)
                            #angler=int(angler*-10)/10
                            newline = Target2D(size  = (line_length,5.0),
                                            color      = (0.0,0.0,0.0),
                                            orientation = angler,
                                            position=((x-xdiff/2),(y-ydiff/2)),
                                            anchor='center')
                            viewport_newline = Viewport(screen=screen, stimuli=[newline])
                            viewport_newline.draw()
                        VisionEgg.Core.swap_buffers()
                        if JustFlagged: ## if you just came back from trying to prematurely leave the task, wipe the buffers one extra time.
                            JustFlagged=False
                        #
                        #
                        #
                        ##
                        ##
                        ## for each button, we will log when the mouse/finger enters the button space.
                        ## if it's the right button, then TRAILSmaskGREEN will be overlaid, and stay there, being a permenant addition to 
                        ## the masks.
                        ## if it's the wrong time, then the red mask will be shown until another button is touched.
                        ##
                        ##
                        ##
                        ## start with the first button
                        ##1
                        if x >= 356 and x <= 410 and y >= 171 and y <=225  :
                            
                            if BUTTON==0:
                                if not ID=="1":
                                    out_file.write('   CORRECT_button1@ %d ms into trial\n'%(int(round(time() * 1000))-startTIME))
                                maskGREEN = TextureStimulus(texture=TRAILSmaskGREEN,position=(356,225), anchor='upperleft', max_alpha=0.50)
                                maskLIST.append(maskGREEN)
                                masks = VisionEgg.Core.Viewport(screen=screen, size=screen.size, stimuli=maskLIST)
                                screen.clear()
                                background.draw()
                                masks.draw()
                                lines.draw()
                                VisionEgg.Core.swap_buffers()
                                POINTSx=383
                                POINTSy=198
                                BUTTON=BUTTON+1
                                ID="1"
                            ## while at the button you just pushed, you're not wrong to dawdle there for a moment, but if BUTTON >= 2, that is looping around after hitting
                            ## the next button in order, and should be marked wrong. 
                            elif BUTTON>=2:
                                if not ID=="1":
                                    out_file.write('   _!_WRONG_button1@ %d ms into trial\n'%(int(round(time() * 1000))-startTIME))
                                    ERRORS=ERRORS+1
                                    ID="1"
                                maskRED = TextureStimulus(texture=TRAILSmaskRED,position=(356,225), anchor='upperleft', max_alpha=0.50)
                                screen.clear()
                                background.draw()
                                masks.draw()
                                lines.draw()
                                maskRED.draw()
                                VisionEgg.Core.swap_buffers()

                        ##
                        ##
                        ##2
                        elif x >= 517 and x <= 571 and y >= 358 and y <=412  :
                            if BUTTON==1:
                                if not ID=="2":
                                    out_file.write('   CORRECT_button2@ %d ms into trial\n'%(int(round(time() * 1000))-startTIME))
                                maskGREEN = TextureStimulus(texture=TRAILSmaskGREEN,position=(517,412), anchor='upperleft', max_alpha=0.50)
                                maskLIST.append(maskGREEN)
                                ### need to make a new connecting line for all but the first button
                                ### in practice (since we pre-populated a list of lines) is that we now include the next line in the list:
                                lines = Viewport(screen=screen, stimuli=lineLIST[0:2])
                                masks = VisionEgg.Core.Viewport(screen=screen, size=screen.size, stimuli=maskLIST)
                                screen.clear()
                                background.draw()
                                masks.draw()
                                lines.draw()
                                VisionEgg.Core.swap_buffers()
                                POINTSx=544
                                POINTSy=385
                                BUTTON=BUTTON+1
                                ID="2"
                            elif BUTTON>=3 or BUTTON <1:
                                if not ID=="2":
                                    out_file.write('   _!_WRONG_button2@ %d ms into trial\n'%(int(round(time() * 1000))-startTIME))
                                    ERRORS=ERRORS+1
                                    ID="2"
                                maskRED = TextureStimulus(texture=TRAILSmaskRED,position=(517,412), anchor='upperleft', max_alpha=0.50)
                                screen.clear()
                                background.draw()
                                masks.draw()
                                maskRED.draw()
                                lines.draw()
                                VisionEgg.Core.swap_buffers()
                        ##
                        ##
                        ##3    
                        elif x >= 627 and x <= 681 and y >= 158 and y <=212  :
                            if BUTTON==2:
                                if not ID=="3":
                                    out_file.write('   CORRECT_button3@ %d ms into trial\n'%(int(round(time() * 1000))-startTIME))
                                maskGREEN = TextureStimulus(texture=TRAILSmaskGREEN,position=(627,212), anchor='upperleft', max_alpha=0.50)
                                maskLIST.append(maskGREEN)
                                ### need to make a new connecting line for all but the first button
                                ### in practice (since we pre-populated a list of lines) is that we now include the next line in the list:
                                lines = Viewport(screen=screen, stimuli=lineLIST[0:3])
                                masks = VisionEgg.Core.Viewport(screen=screen, size=screen.size, stimuli=maskLIST)
                                screen.clear()
                                background.draw()
                                masks.draw()
                                lines.draw()
                                VisionEgg.Core.swap_buffers()
                                POINTSx=654
                                POINTSy=185
                                BUTTON=BUTTON+1
                                ID="3"
                            elif BUTTON>=4 or BUTTON <2:
                                if not ID=="3":
                                    out_file.write('   _!_WRONG_button3@ %d ms into trial\n'%(int(round(time() * 1000))-startTIME))
                                    ERRORS=ERRORS+1
                                    ID="3"
                                maskRED = TextureStimulus(texture=TRAILSmaskRED,position=(627,212), anchor='upperleft', max_alpha=0.50)
                                screen.clear()
                                background.draw()
                                masks.draw()
                                maskRED.draw()
                                lines.draw()
                                VisionEgg.Core.swap_buffers()

                        ##
                        ##
                        ##4
                        elif x >= 498 and x <= 552 and y >= 217 and y <=271  :
                            if BUTTON==3:
                                if not ID=="4":
                                    out_file.write('   CORRECT_button4@ %d ms into trial\n'%(int(round(time() * 1000))-startTIME))
                                maskGREEN = TextureStimulus(texture=TRAILSmaskGREEN,position=(498,271), anchor='upperleft', max_alpha=0.50)
                                maskLIST.append(maskGREEN)
                                ### need to make a new connecting line for all but the first button
                                ### in practice (since we pre-populated a list of lines) is that we now include the next line in the list:
                                lines = Viewport(screen=screen, stimuli=lineLIST[0:4])
                                masks = VisionEgg.Core.Viewport(screen=screen, size=screen.size, stimuli=maskLIST)
                                screen.clear()
                                background.draw()
                                masks.draw()
                                lines.draw()
                                VisionEgg.Core.swap_buffers()
                                POINTSx=525
                                POINTSy=244
                                BUTTON=BUTTON+1
                                ID="4"
                            elif BUTTON>=5 or BUTTON <3:
                                if not ID=="4":
                                    out_file.write('   _!_WRONG_button4@ %d ms into trial\n'%(int(round(time() * 1000))-startTIME))
                                    ERRORS=ERRORS+1
                                    ID="4"
                                maskRED = TextureStimulus(texture=TRAILSmaskRED,position=(498,271), anchor='upperleft', max_alpha=0.50)
                                screen.clear()
                                background.draw()
                                masks.draw()
                                maskRED.draw()
                                lines.draw()
                                VisionEgg.Core.swap_buffers()

                        ##
                        ##
                        ##5
                        elif x >= 534 and x <= 588 and y >= 62 and y <=116 :
                            if BUTTON==4:
                                if not ID=="5":
                                    out_file.write('   CORRECT_button5@ %d ms into trial\n'%(int(round(time() * 1000))-startTIME))
                                maskGREEN = TextureStimulus(texture=TRAILSmaskGREEN,position=(534,116), anchor='upperleft', max_alpha=0.50)
                                maskLIST.append(maskGREEN)
                                ### need to make a new connecting line for all but the first button
                                ### in practice (since we pre-populated a list of lines) is that we now include the next line in the list:
                                lines = Viewport(screen=screen, stimuli=lineLIST[0:5])
                                masks = VisionEgg.Core.Viewport(screen=screen, size=screen.size, stimuli=maskLIST)
                                screen.clear()
                                background.draw()
                                masks.draw()
                                lines.draw()
                                VisionEgg.Core.swap_buffers()
                                POINTSx=561
                                POINTSy=89
                                BUTTON=BUTTON+1
                                ID="5"
                            elif BUTTON>=6 or BUTTON <4:
                                if not ID=="5":
                                    out_file.write('   _!_WRONG_button5@ %d ms into trial\n'%(int(round(time() * 1000))-startTIME))
                                    ERRORS=ERRORS+1
                                    ID="5"
                                maskRED = TextureStimulus(texture=TRAILSmaskRED,position=(534,116), anchor='upperleft', max_alpha=0.50)
                                screen.clear()
                                background.draw()
                                masks.draw()
                                maskRED.draw()
                                lines.draw()
                                VisionEgg.Core.swap_buffers()
                        for event in pygame.event.get():
                            if event.type == pygame.locals.MOUSEBUTTONUP:
                                screen.clear()
                                background.draw()
                                masks.draw()
                                lines.draw()
                                VisionEgg.Core.swap_buffers()
                                screen.clear()
                                background.draw()
                                masks.draw()
                                lines.draw()
                                MouseUp=True



                        
#######################################################################################################
#######################################################################################################
#######################################################################################################
#######################################################################################################
#######################################################################################################
def TRAILSbSAMPLE(ScreenNumber, TrialTime, ERRORS, ATTEMPTS_TO_END_EARLY):
    warnBOX = TextureStimulus(texture=notyetboxes[16],position=(785,282), anchor='upperleft', max_alpha=1.0)
    viewportwarnBOX = VisionEgg.Core.Viewport(screen=screen, size=screen.size, stimuli=[warnBOX])
    BUTTON=0
    ERRORS=0
    ID=" "
    JustFlagged=False
    ATTEMPTS_TO_END_EARLY=0
    POINTSx=-100
    POINTSy=-100
    EndTrial=False
    ## PRE-populate lineLIST with the connecting lines, so that we don't have to recaclulate them each time we loop through.
    ## the first line is a blank.
    line = Target2D(size  = (1.0,1.0),
                    color      = (0.0,0.0,0.0),
                    orientation = 0, #angle
                    position=(-100,-100),
                    anchor='upperleft')
    lineLIST=[line]
    # the center of each button:
    #centerXs=[383,544,654,525,561]
    #centerYs=[252,439,239,298,143]
    # leads to the following (just do in excel and hard-code before-hand to limit load on python)
    # coordinates for the N_tials-1 connecting lines:    
    lineXcenters=[591,783,777,714,499,227,328]
    lineYcenters=[251,246,192,142,76,198,304]
    line_angles=[32.7,-42.3,-13.5,-69.3,-1.4,-75.2,-4.1]
    line_lengths=[259,224,184,153,484,239,264]
#    for x in range(0,(len(lineXcenters)-1)):
    for x in range(0,(len(lineXcenters))):
        line = Target2D(size  = (line_lengths[x],5.0),
                    color      = (0.0,0.0,0.0),
                    orientation = line_angles[x],
                    position=(lineXcenters[x],lineYcenters[x]),
                    anchor='center')
        lineLIST.append(line)
    stim = TextureStimulus(texture=trailsbackgrounds[1],position=(0,0))
    screen.clear()
    background = VisionEgg.Core.Viewport(screen=screen, size=screen.size, stimuli=[stim])
    maskGREEN = TextureStimulus(texture=TRAILSmaskGREEN,position=(-100,-100), anchor='center', max_alpha=0.50)
    maskLIST=[maskGREEN,maskGREEN]
    masks = VisionEgg.Core.Viewport(screen=screen, size=screen.size, stimuli=maskLIST)
    lines = Viewport(screen=screen, stimuli=[lineLIST[0]])
## this is from tutorial:
#    target = Target2D(size  = (25.0,10.0),
#                      color      = (0.0,0.0,0.0,1.0), # Set the target color (RGBA) black
#                      orientation = -45.0)
#    lines = Viewport(screen=screen, stimuli=[target])
## </>this is from tutorial:
#    lines = Viewport(screen=screen, stimuli=[line])
    screen.clear()
    background.draw()
    masks.draw()
    lines.draw()
    VisionEgg.Core.swap_buffers()
    startTIME=int(round(time() * 1000))
    while not EndTrial:
        for event in pygame.event.get():
            if event.type == pygame.locals.MOUSEBUTTONDOWN:
                ## next few lines new for 0-6-4. trying to get tabelt to behave well.
                xOld,yOld = pygame.mouse.get_pos()
                yOld=600-yOld
                downtime=int(round(time() * 1000))
                MouseUp=False
                while not MouseUp:
                    ## next few lines new for 0-6-4. trying to get tabelt to behave well.
                    if (int(round(time() * 1000))-downtime) > 50:
                        if xOld==x and yOld==y:
                            MouseUp=True
    ## the next two lines basically say to get the x and y position of the cursor when a mousedown happens...
                    x,y = pygame.mouse.get_pos()
    ## pygame.mouse.get_pos() gives coordinates with the LOWER LEFT, not UPPER LEFT (as in visionegg) corner as the origin.
                    y=600-y
                    screen.clear()
                    background.draw()
                    masks.draw()
                    lines.draw()
                    if JustFlagged:
                        viewportwarnBOX.draw()
                    if x >= 905 and x <= 996 and y >= 0 and y <=35 and not JustFlagged:
                        if BUTTON == 8:
                            out_file.write('   NEXT_at_ms %d\n'%(int(round(time() * 1000))-startTIME))
                            TrialTime=int(round(time() * 1000))-startTIME
                            return ScreenNumber, TrialTime, ERRORS, ATTEMPTS_TO_END_EARLY
                            StartTrial=True                       
                        elif BUTTON < 8:
                            out_file.write('   NEXT_at_ms %d\n'%(int(round(time() * 1000))-startTIME))
                            ATTEMPTS_TO_END_EARLY=ATTEMPTS_TO_END_EARLY+1
##                            screen.clear()
##                            background.draw()
##                            masks.draw()
##                            lines.draw()
                            viewportwarnBOX.draw()
                            VisionEgg.Core.swap_buffers()
##                            screen.clear()
##                            background.draw()
##                            masks.draw()
##                            lines.draw()
                            viewportwarnBOX.draw()
                            VisionEgg.Core.swap_buffers()
                            JustFlagged=True
                    else:
                        # draw a line from wherever the inital point is to the current.
                        if POINTSx > -100 and not JustFlagged:  ## if we haven't really started yet,ignore next stuff
                            ydiff=float(int(y-POINTSy))+0.1
                            xdiff=float(int(x-POINTSx))+0.1
                            line_length=int(((xdiff**2)+(ydiff**2))**0.5)
                            angler=180*(arctan(ydiff/xdiff)/3.14159)
                            #angler=int(angler*-10)/10
                            newline = Target2D(size  = (line_length,5.0),
                                            color      = (0.0,0.0,0.0),
                                            orientation = angler,
                                            position=((x-xdiff/2),(y-ydiff/2)),
                                            anchor='center')
                            viewport_newline = Viewport(screen=screen, stimuli=[newline])
                            viewport_newline.draw()
                        VisionEgg.Core.swap_buffers()
                        if JustFlagged: ## if you just came back from trying to prematurely leave the task, wipe the buffers one extra time.
                            if not (x >= 930 and x <= 1024 and y >= 34 and y <=71):
                                JustFlagged=False
                        #
                        #
                        #
                        ##
                        ##
                        ## for each button, we will log when the mouse/finger enters the button space.
                        ## if it's the right button, then TRAILSmaskGREEN will be overlaid, and stay there, being a permenant addition to 
                        ## the masks.
                        ## if it's the wrong time, then the red mask will be shown until another button is touched.
                        ##
                        ##
                        ##
                        ## start with the first button
                        ## 1
                        if x >= 456 and x <= 508 and y <= 207 and y >= 155:
                            if BUTTON==0:
                                if not ID=="1":
                                    out_file.write('   CORRECT_button1,@ %d ms into trial\n'%(int(round(time() * 1000))-startTIME))
                                maskGREEN = TextureStimulus(texture=TRAILSmaskGREEN,position=(456,207), anchor='upperleft', max_alpha=0.50)
                                maskLIST.append(maskGREEN)
                                masks = VisionEgg.Core.Viewport(screen=screen, size=screen.size, stimuli=maskLIST)

                                screen.clear()
                                background.draw()
                                masks.draw()
                                lines.draw()
                                VisionEgg.Core.swap_buffers()
                                POINTSx=482
                                POINTSy=181
                                BUTTON=BUTTON+1
                                ID="1"
                            elif BUTTON>=2:
                                if not ID=="1":
                                    out_file.write('   _!_WRONG_button1,@ %d ms into trial\n'%(int(round(time() * 1000))-startTIME))
                                    ERRORS=ERRORS+1
                                    ID="0"
                                maskRED = TextureStimulus(texture=TRAILSmaskRED,position=(456,207), anchor='upperleft', max_alpha=0.50)
                                screen.clear()
                                background.draw()
                                masks.draw()
                                lines.draw()
                                maskRED.draw()
                                VisionEgg.Core.swap_buffers()
                        
                        ## A
                        elif x >= 674 and x <= 726 and y <= 347 and y >= 295:
                            if BUTTON==1:
                                if not ID=="A":
                                    out_file.write('   CORRECT_buttonA,@ %d ms into trial\n'%(int(round(time() * 1000))-startTIME))
                                maskGREEN = TextureStimulus(texture=TRAILSmaskGREEN,position=(674,347), anchor='upperleft', max_alpha=0.50)
                                maskLIST.append(maskGREEN)
                                masks = VisionEgg.Core.Viewport(screen=screen, size=screen.size, stimuli=maskLIST)
                                lines = Viewport(screen=screen, stimuli=lineLIST[0:2])
                                screen.clear()
                                background.draw()
                                masks.draw()
                                lines.draw()
                                VisionEgg.Core.swap_buffers()
                                POINTSx=700
                                POINTSy=321
                                BUTTON=BUTTON+1
                                ID="A"
                            elif BUTTON>=3 or BUTTON <1:
                                if not ID=="A":
                                    out_file.write('   _!_WRONG_buttonA,@ %d ms into trial\n'%(int(round(time() * 1000))-startTIME))
                                    ERRORS=ERRORS+1
                                    ID="0"
                                maskRED = TextureStimulus(texture=TRAILSmaskRED,position=(674,347), anchor='upperleft', max_alpha=0.50)
                                screen.clear()
                                background.draw()
                                masks.draw()
                                lines.draw()
                                maskRED.draw()
                                VisionEgg.Core.swap_buffers()
                        
                        ## 2
                        elif x >= 840 and x <= 892 and y <= 196 and y >= 144:
                            if BUTTON==2:
                                if not ID=="2":
                                    out_file.write('   CORRECT_button2,@ %d ms into trial\n'%(int(round(time() * 1000))-startTIME))
                                maskGREEN = TextureStimulus(texture=TRAILSmaskGREEN,position=(840,196), anchor='upperleft', max_alpha=0.50)
                                maskLIST.append(maskGREEN)
                                masks = VisionEgg.Core.Viewport(screen=screen, size=screen.size, stimuli=maskLIST)
                                lines = Viewport(screen=screen, stimuli=lineLIST[0:3])
                                screen.clear()
                                background.draw()
                                masks.draw()
                                lines.draw()
                                VisionEgg.Core.swap_buffers()
                                POINTSx=866
                                POINTSy=170
                                BUTTON=BUTTON+1
                                ID="2"
                            elif BUTTON>=4 or BUTTON <2:
                                if not ID=="2":
                                    out_file.write('   _!_WRONG_button2,@ %d ms into trial\n'%(int(round(time() * 1000))-startTIME))
                                    ERRORS=ERRORS+1
                                    ID="0"
                                maskRED = TextureStimulus(texture=TRAILSmaskRED,position=(840,196), anchor='upperleft', max_alpha=0.50)
                                screen.clear()
                                background.draw()
                                masks.draw()
                                lines.draw()
                                maskRED.draw()
                                VisionEgg.Core.swap_buffers()
                        
                        ## B
                        elif x >= 661 and x <= 713 and y <= 239 and y >= 187:
                            if BUTTON==3:
                                if not ID=="B":
                                    out_file.write('   CORRECT_buttonB,@ %d ms into trial\n'%(int(round(time() * 1000))-startTIME))
                                maskGREEN = TextureStimulus(texture=TRAILSmaskGREEN,position=(661,239), anchor='upperleft', max_alpha=0.50)
                                maskLIST.append(maskGREEN)
                                masks = VisionEgg.Core.Viewport(screen=screen, size=screen.size, stimuli=maskLIST)
                                lines = Viewport(screen=screen, stimuli=lineLIST[0:4])
                                screen.clear()
                                background.draw()
                                masks.draw()
                                lines.draw()
                                VisionEgg.Core.swap_buffers()
                                POINTSx=687
                                POINTSy=213
                                BUTTON=BUTTON+1
                                ID="B"
                            elif BUTTON>=5 or BUTTON <3:
                                if not ID=="B":
                                    out_file.write('   _!_WRONG_buttonB,@ %d ms into trial\n'%(int(round(time() * 1000))-startTIME))
                                    ERRORS=ERRORS+1
                                    ID="0"
                                maskRED = TextureStimulus(texture=TRAILSmaskRED,position=(661,239), anchor='upperleft', max_alpha=0.50)
                                screen.clear()
                                background.draw()
                                masks.draw()
                                lines.draw()
                                maskRED.draw()
                                VisionEgg.Core.swap_buffers()
                        
                        ## 3
                        elif x >= 715 and x <= 767 and y <= 96 and y >= 44:
                            if BUTTON==4:
                                if not ID=="3":
                                    out_file.write('   CORRECT_button3,@ %d ms into trial\n'%(int(round(time() * 1000))-startTIME))
                                maskGREEN = TextureStimulus(texture=TRAILSmaskGREEN,position=(715,96), anchor='upperleft', max_alpha=0.50)
                                maskLIST.append(maskGREEN)
                                masks = VisionEgg.Core.Viewport(screen=screen, size=screen.size, stimuli=maskLIST)
                                lines = Viewport(screen=screen, stimuli=lineLIST[0:5])
                                screen.clear()
                                background.draw()
                                masks.draw()
                                lines.draw()
                                VisionEgg.Core.swap_buffers()
                                POINTSx=741
                                POINTSy=70
                                BUTTON=BUTTON+1
                                ID="3"
                            elif BUTTON>=6 or BUTTON <4:
                                if not ID=="3":
                                    out_file.write('   _!_WRONG_button3,@ %d ms into trial\n'%(int(round(time() * 1000))-startTIME))
                                    ERRORS=ERRORS+1
                                    ID="0"
                                maskRED = TextureStimulus(texture=TRAILSmaskRED,position=(715,96), anchor='upperleft', max_alpha=0.50)
                                screen.clear()
                                background.draw()
                                masks.draw()
                                lines.draw()
                                maskRED.draw()
                                VisionEgg.Core.swap_buffers()
                        
                        ## C
                        elif x >= 231 and x <= 283 and y <= 108 and y >= 56:
                            if BUTTON==5:
                                if not ID=="C":
                                    out_file.write('   CORRECT_buttonC,@ %d ms into trial\n'%(int(round(time() * 1000))-startTIME))
                                maskGREEN = TextureStimulus(texture=TRAILSmaskGREEN,position=(231,108), anchor='upperleft', max_alpha=0.50)
                                maskLIST.append(maskGREEN)
                                masks = VisionEgg.Core.Viewport(screen=screen, size=screen.size, stimuli=maskLIST)
                                lines = Viewport(screen=screen, stimuli=lineLIST[0:6])
                                screen.clear()
                                background.draw()
                                masks.draw()
                                lines.draw()
                                VisionEgg.Core.swap_buffers()
                                POINTSx=257
                                POINTSy=82
                                BUTTON=BUTTON+1
                                ID="C"
                            elif BUTTON>=7 or BUTTON <5:
                                if not ID=="C":
                                    out_file.write('   _!_WRONG_buttonC,@ %d ms into trial\n'%(int(round(time() * 1000))-startTIME))
                                    ERRORS=ERRORS+1
                                    ID="0"
                                maskRED = TextureStimulus(texture=TRAILSmaskRED,position=(231,108), anchor='upperleft', max_alpha=0.50)
                                screen.clear()
                                background.draw()
                                masks.draw()
                                lines.draw()
                                maskRED.draw()
                                VisionEgg.Core.swap_buffers()
                        
                        ## 4
                        elif x >= 170 and x <= 222 and y <= 339 and y >= 287:
                            if BUTTON==6:
                                if not ID=="4":
                                    out_file.write('   CORRECT_button4,@ %d ms into trial\n'%(int(round(time() * 1000))-startTIME))
                                maskGREEN = TextureStimulus(texture=TRAILSmaskGREEN,position=(170,339), anchor='upperleft', max_alpha=0.50)
                                maskLIST.append(maskGREEN)
                                masks = VisionEgg.Core.Viewport(screen=screen, size=screen.size, stimuli=maskLIST)
                                lines = Viewport(screen=screen, stimuli=lineLIST[0:7])
                                screen.clear()
                                background.draw()
                                masks.draw()
                                lines.draw()
                                VisionEgg.Core.swap_buffers()
                                POINTSx=196
                                POINTSy=313
                                BUTTON=BUTTON+1
                                ID="4"
                            elif BUTTON>=8 or BUTTON <6:
                                if not ID=="4":
                                    out_file.write('   _!_WRONG_button4,@ %d ms into trial\n'%(int(round(time() * 1000))-startTIME))
                                    ERRORS=ERRORS+1
                                    ID="0"
                                maskRED = TextureStimulus(texture=TRAILSmaskRED,position=(170,339), anchor='upperleft', max_alpha=0.50)
                                screen.clear()
                                background.draw()
                                masks.draw()
                                lines.draw()
                                maskRED.draw()
                                VisionEgg.Core.swap_buffers()
                        
                        ## D
                        elif x >= 433 and x <= 485 and y <= 320 and y >= 268:
                            if BUTTON==7:
                                if not ID=="D":
                                    out_file.write('   CORRECT_buttonD,@ %d ms into trial\n'%(int(round(time() * 1000))-startTIME))
                                maskGREEN = TextureStimulus(texture=TRAILSmaskGREEN,position=(433,320), anchor='upperleft', max_alpha=0.50)
                                maskLIST.append(maskGREEN)
                                masks = VisionEgg.Core.Viewport(screen=screen, size=screen.size, stimuli=maskLIST)
                                lines = Viewport(screen=screen, stimuli=lineLIST[0:8])
                                screen.clear()
                                background.draw()
                                masks.draw()
                                lines.draw()
                                VisionEgg.Core.swap_buffers()
                                POINTSx=459
                                POINTSy=294
                                BUTTON=BUTTON+1
                                ID="D"
                            elif BUTTON>=9 or BUTTON <7:
                                if not ID=="D":
                                    out_file.write('   _!_WRONG_buttonD,@ %d ms into trial\n'%(int(round(time() * 1000))-startTIME))
                                    ERRORS=ERRORS+1
                                    ID="0"
                                maskRED = TextureStimulus(texture=TRAILSmaskRED,position=(433,320), anchor='upperleft', max_alpha=0.50)
                                screen.clear()
                                background.draw()
                                masks.draw()
                                lines.draw()
                                maskRED.draw()
                                VisionEgg.Core.swap_buffers()


                                
                        for event in pygame.event.get():
                            if event.type == pygame.locals.MOUSEBUTTONUP:
                                screen.clear()
                                background.draw()
                                masks.draw()
                                lines.draw()
                                VisionEgg.Core.swap_buffers()
                                screen.clear()
                                background.draw()
                                masks.draw()
                                lines.draw()
                                MouseUp=True



    
##  FINAL THANKYOU SCREEN
def final_screen():
    backgroundIMAGE = TextureStimulus(texture=FINALSCREEN,position=(0,0))
    viewport = VisionEgg.Core.Viewport(screen=screen, size=screen.size, stimuli=[backgroundIMAGE,backgroundIMAGE])
    screen.clear()
    viewport.draw()
    VisionEgg.Core.swap_buffers()
    screen.clear()
    startTIMEscreen=int(round(time() * 1000))
    currentTIMEscreen=int(round(time() * 1000))
    while (currentTIMEscreen-startTIMEscreen) < 10000:  # 10 s
        currentTIMEscreen=int(round(time() * 1000))
        for event in pygame.event.get():
            if event.type == pygame.locals.MOUSEBUTTONDOWN:
                x,y = pygame.mouse.get_pos()




####################################################################
####################################################################
####################################################################
####################################################################
####################################################################
####################################################################
########################  NOW, START THE LOOP, AND   ###############
########################  USE THE MODULES WE WROTE.  ###############
####################################################################
####################################################################
####################################################################
####################################################################
####################################################################
####################################################################
####################################################################
####################################################################

## Set the cursor in pygame... (this works well with the touchscreen)
pygame.mouse.set_cursor(*pygame.cursors.arrow)
pygame.mouse.set_visible(True)

FIRST_SUBJECT=True



INLOOP=0
while INLOOP == 0:
    WordCount=0
    InstructionTime=-1
    YearAnswer=0
    TrialTime=-1
    MonthAnswer=0
    ScreenNumber=0
    PENALTIES=0
    ERRORS=0
    Choice=[" "]
    ## fresh logs with each initialization
    ATTENTION_LOG=[["TASK","SIMPLE_ATTENTION_J","SIMPLE_ATTENTION_FRUIT","SIMPLE_ATTENTION_1239"],
                     ["POINTS","NA","NA","NA"],["TIME_MS","NA","NA","NA"]]

    SPATIAL_LOG=[["TASK","SIMPLE_SHAPE","FACE","LINE_DRAW","CUBE"],
                   ["POINTS","NA","NA","NA","NA"],["TIME_MS","NA","NA","NA","NA"]]

    ORIENTATION_LOG=[["TASK","MONTH","YEAR","DAY_OF_WEEK","STATE"],
                       ["POINTS","NA","NA","NA","NA"],["TIME_MS","NA","NA","NA","NA"]]

    MEMORY_LOG=[["TASK","INCIDENTAL_MEMORY_PHRASE","INCIDENTAL_MEMORY_J","INCIDENTAL_MEMORY_NUMBER","RECALL_FIVEWORDS"],
                  ["POINTS","NA","NA","NA","NA"],["TIME_MS","NA","NA","NA","NA"]]

    MATH_LOG=[["TASK","ADD_67","SUBTRACT_33"],
                ["POINTS","NA","NA"],["TIME_MS","NA","NA"]]

    TRAILS_LOG=[["TASK","MINI_TRAILS_A","MINI_TRAILS_B","FULL_TRAILS_B"],
                  ["POINTS","NA","NA","NA"],["TIME_MS","NA","NA","NA"]]

    STROOP_LOG=[["TASK","WARMUP1","WARMUP2","WARMUP3","STROOP04","STROOP05","STROOP06","STROOP07","STROOP08","STROOP09",
                   "STROOP10","STROOP11","STROOP12","STROOP13","STROOP14","STROOP15"],
                  ["ERRORS","NA","NA","NA","NA","NA","NA","NA","NA","NA","NA","NA","NA","NA","NA","NA"],
                  ["TIME_MS","NA","NA","NA","NA","NA","NA","NA","NA","NA","NA","NA","NA","NA","NA","NA"]]
    READING_SPEED_LOG=["NA"]
    MOTOR_SPEED_LOG=["NA"]    
##    ATTENTION_LOG=ATTENTION_BLANK
##    SPATIAL_LOG=SPATIAL_BLANK
##    ORIENTATION_LOG=ORIENTATION_BLANK
##    MEMORY_LOG=MEMORY_BLANK
##    MATH_LOG=MATH_BLANK
##    TRAILS_LOG=TRAILS_BLANK
##    STROOP_LOG=STROOP_BLANK
##    READING_SPEED_LOG=READING_SPEED_BLANK
##    MOTOR_SPEED_LOG=MOTOR_SPEED_BLANK
    VERY_BEGINNING_NUMERIC="NA"
    VERY_END_NUMERIC="NA"
    SUM_TIME_SPENT_MS="NA"
    VERY_BEGINNING="NA"
    VERY_END="NA"
    ##
    ##START ON THE HOME SCREEN
    ScreenNumber, RESET = HOMEscreen(ScreenNumber, RESET)

    if (ScreenNumber == 9997) or (ScreenNumber == 9998):
        ScreenNumber, RESET = review_screen(ScreenNumber, RESET) 

    ##
    ##MOVE TO SCREEN #1 (assuming we didn't advance to 9995 already, which is a reset), WHICH IS THE READING CHECK.
    if ScreenNumber < 9995:
        ScreenNumber=ScreenNumber+1
        canRead=False
        ScreenNumber, canRead, RESET = NURSEscreen(ScreenNumber, canRead, RESET)
    #### output file if we get past the GCS rating screen
    subject_number=int(copy.deepcopy(random.randint(100000, 999999)))
    filename_prelim= "%s_%d.txt"%(strftime("%Y-%m-%d", localtime()), subject_number)
    filename=copy.deepcopy(filename_prelim)
    if RESET == "True":
        # it will reset if GCS is too low, can't read, etc. 
        ScreenNumber=9995
    if RESET == "False":
        if ScreenNumber < 9995:
            #### if we don't reset, and instead continue,
            #### start writing a file
            #
            os.chdir("data/")
            out_file = open(filename,"w")
            # henceforth, need to change the mode from "w" to "a"
            # and make conditional on consentObt, e.g.
            # if consentObt==True:
            #   out_file = open(filename,"a")
            out_file.write('subject= %d\n'%subject_number)
            out_file.write('date= %s\n'%(strftime("%Y_%m_%d", localtime())))
            out_file.write('PATIENT_CAN_READ?= %s\n'%canRead)
            out_file.write('___________________________________________\n')
            out_file.write(' \n')
            out_file.write(' \n')
            out_file.close()
            os.chdir(BASEPATH)


            ScreenNumber=2

    ##
    #while debugging, take a shortcut
    #ScreenNumber = 33  #                                                                                     ######

    ### <<THIS BLOCK IS WHAT MAKES IT 0-3-3 instead of 0-3-3depricated; AVOIDING ODD ERROR WHERE AN
    ###   EARLY EXIT BY PRIOR SUBJECT MAY PRE-FILL SOME OF THIS FOR NEXT SUBJECT... OR SOME SUCH...
    ## for chinese version, WordCount is character count
    WordCount=0
    InstructionTime=-1
    YearAnswer=0
    TrialTime=-1
    MonthAnswer=0
    PENALTIES=0
    ERRORS=0
    Choice=[" "]
    ## fresh logs with each initialization
    ATTENTION_LOG=[["TASK","SIMPLE_ATTENTION_J","SIMPLE_ATTENTION_FRUIT","SIMPLE_ATTENTION_1239"],
                     ["POINTS","NA","NA","NA"],["TIME_MS","NA","NA","NA"]]

    SPATIAL_LOG=[["TASK","SIMPLE_SHAPE","FACE","LINE_DRAW","CUBE"],
                   ["POINTS","NA","NA","NA","NA"],["TIME_MS","NA","NA","NA","NA"]]

    ORIENTATION_LOG=[["TASK","MONTH","YEAR","DAY_OF_WEEK","STATE"],
                       ["POINTS","NA","NA","NA","NA"],["TIME_MS","NA","NA","NA","NA"]]

    MEMORY_LOG=[["TASK","INCIDENTAL_MEMORY_PHRASE","INCIDENTAL_MEMORY_J","INCIDENTAL_MEMORY_NUMBER","RECALL_FIVEWORDS"],
                  ["POINTS","NA","NA","NA","NA"],["TIME_MS","NA","NA","NA","NA"]]

    MATH_LOG=[["TASK","ADD_67","SUBTRACT_33"],
                ["POINTS","NA","NA"],["TIME_MS","NA","NA"]]

    TRAILS_LOG=[["TASK","MINI_TRAILS_A","MINI_TRAILS_B","FULL_TRAILS_B"],
                  ["POINTS","NA","NA","NA"],["TIME_MS","NA","NA","NA"]]

    STROOP_LOG=[["TASK","WARMUP1","WARMUP2","WARMUP3","STROOP04","STROOP05","STROOP06","STROOP07","STROOP08","STROOP09",
                   "STROOP10","STROOP11","STROOP12","STROOP13","STROOP14","STROOP15"],
                  ["ERRORS","NA","NA","NA","NA","NA","NA","NA","NA","NA","NA","NA","NA","NA","NA","NA"],
                  ["TIME_MS","NA","NA","NA","NA","NA","NA","NA","NA","NA","NA","NA","NA","NA","NA","NA"]]
    READING_SPEED_LOG=["NA"]
    MOTOR_SPEED_LOG=["NA"]      
##    ATTENTION_LOG=ATTENTION_BLANK
##    SPATIAL_LOG=SPATIAL_BLANK
##    ORIENTATION_LOG=ORIENTATION_BLANK
##    MEMORY_LOG=MEMORY_BLANK
##    MATH_LOG=MATH_BLANK
##    TRAILS_LOG=TRAILS_BLANK
##    STROOP_LOG=STROOP_BLANK
##    READING_SPEED_LOG=READING_SPEED_BLANK
##    MOTOR_SPEED_LOG=MOTOR_SPEED_BLANK
    VERY_BEGINNING_NUMERIC="NA"
    VERY_END_NUMERIC="NA"
    SUM_TIME_SPENT_MS="NA"
    VERY_BEGINNING="NA"
    VERY_END="NA"
       
    while ScreenNumber == 2:
        ScreenNumber, RESET = EPICscreen(ScreenNumber, RESET)
        ScreenNumber=ScreenNumber+1
        
    while ScreenNumber == 3:   ### THIS IS THE STARTING SCREEN FOR THE PATIENT
        ScreenNumber, RESET = PATIENTstartSCREEN(ScreenNumber, RESET)
        ScreenNumber=ScreenNumber+1

    while ScreenNumber == 4:   ### INSTRUCTION SCREEN
        ## for [almost] every instruction screen, 
        ## we hard-code how many words there are (not counting the "NEXT" button; it's words of novel instruction)
        ## and the background image (which is also hard-coded).
        ## and we montior how long until they clicked.
        ## the idea is that we are getting a coarse idea of reading time.
        WordCount=18
        BACKGROUNDIMAGE=instructbackgrounds[1]
        InstructionTime=-1
        VERY_BEGINNING=strftime("%Y-%m-%d %H:%M:%S", localtime())
        VERY_BEGINNING_NUMERIC=int(round(time() * 1000))
        ScreenNumber, BACKGROUNDIMAGE, InstructionTime, RESET = INSTRUCTIONscreen(ScreenNumber, BACKGROUNDIMAGE, InstructionTime, RESET)
        os.chdir("data/")
        out_file = open(filename,"a")
        out_file.write('sometimes_you_pick_a_word\n')
        out_file.write('wordcount= %d\n'%WordCount)
        out_file.write('InstructionTime_ms= %d\n'%InstructionTime)
        #out_file.write('words_per_s= %d\n'%(int((float(WordCount)/(float(InstructionTime)/1000))*100)/100.0))
        out_file.write('words_per_s= %f NA NA NA NA 1\n'%round((float(WordCount)/(float(InstructionTime)/1000)), 3))
        READING_SPEED_LOG.append(round((float(WordCount)/(float(InstructionTime)/1000)), 3))
        TIME_END_TRIAL=strftime("%Y-%m-%d %H:%M:%S", localtime())
        out_file.write('timestamp_at_end_of_this_instruction_screen= %s\n'%TIME_END_TRIAL)
        out_file.write(' \n')
        out_file.close()
        os.chdir(BASEPATH) 
        ScreenNumber=ScreenNumber+1

    TrialTime=-1  
    ERRORS=0
    Choice=[" "]
    while ScreenNumber == 5:   ### PICK THE J WORD
        ScreenNumber, TrialTime, ERRORS, Choice, RESET = PICKtheJword(ScreenNumber, TrialTime, ERRORS, Choice, RESET)
        os.chdir("data/")
        out_file = open(filename,"a")
        out_file.write('J_word\n')
        out_file.write('TrialTime_ms= %d\n'%TrialTime)
        out_file.write('Errors= %d\n'%ERRORS)
        ## assign time and points
        ATTENTION_LOG[2][1]=TrialTime
        if ERRORS == 0:
            ATTENTION_LOG[1][1]=2
        elif ERRORS > 0:
            ATTENTION_LOG[1][1]=0
        TIME_END_TRIAL=strftime("%Y-%m-%d %H:%M:%S", localtime())
        out_file.write('timestamp_at_end_of_this_trial= %s\n'%TIME_END_TRIAL)
        out_file.write(' \n')
        out_file.close()
        os.chdir(BASEPATH) 
        ScreenNumber=ScreenNumber+1

    ## time limit skips to the end if 15 mins (900000 ms) have now passed.
    if VERY_BEGINNING_NUMERIC != "NA":
        LATEST_TIME_NUMERIC=int(round(time() * 1000))
        TIME_SPENT_MS=int(round(LATEST_TIME_NUMERIC-VERY_BEGINNING_NUMERIC,0))
        if TIME_SPENT_MS > 900000:
            final_screen()
            ScreenNumber=9997
            
    while ScreenNumber == 6:   ### INSTRUCTION SCREEN
        WordCount=30
        BACKGROUNDIMAGE=instructbackgrounds[2]
        InstructionTime=-1
        ScreenNumber, BACKGROUNDIMAGE, InstructionTime, RESET = INSTRUCTIONscreen(ScreenNumber, BACKGROUNDIMAGE, InstructionTime, RESET)
        os.chdir("data/")
        out_file = open(filename,"a")
        out_file.write('sometimes_you_pick_many_words\n')
        out_file.write('wordcount= %d\n'%WordCount)
        out_file.write('InstructionTime_ms= %d\n'%InstructionTime)
        out_file.write('words_per_s= %f NA NA NA NA 1\n'%(int((float(WordCount)/(float(InstructionTime)/1000))*100)/100.0))
        TIME_END_TRIAL=strftime("%Y-%m-%d %H:%M:%S", localtime())
        out_file.write('timestamp_at_end_of_this_trial= %s\n'%TIME_END_TRIAL)
        READING_SPEED_LOG.append(round((float(WordCount)/(float(InstructionTime)/1000)), 3))
        out_file.write(' \n')
        out_file.close()
        os.chdir(BASEPATH) 
        ScreenNumber=ScreenNumber+1

    while ScreenNumber == 7:   ### PICK THE FRUIT
        TrialTime=-1  
        ERRORS=0
        Choice=[" "]
        ScreenNumber, TrialTime, ERRORS, Choice, RESET = PICKmanyWORDS(ScreenNumber, TrialTime, ERRORS, Choice, RESET)
        os.chdir("data/")
        out_file = open(filename,"a")
        out_file.write('many_word\n')
        out_file.write('TrialTime_ms= %d\n'%TrialTime)
        out_file.write('Errors= %d\n'%ERRORS)
        ## assign time and points
        ATTENTION_LOG[2][2]=TrialTime
        if ERRORS == 0:
            ATTENTION_LOG[1][2]=2
        elif ERRORS > 0:
            ATTENTION_LOG[1][2]=0
        TIME_END_TRIAL=strftime("%Y-%m-%d %H:%M:%S", localtime())
        out_file.write('timestamp_at_end_of_this_trial= %s\n'%TIME_END_TRIAL)
        out_file.write(' \n')
        out_file.close()
        os.chdir(BASEPATH) 
        ScreenNumber=ScreenNumber+1

    ## time limit skips to the end if 15 mins (900000 ms) have now passed.
    if VERY_BEGINNING_NUMERIC != "NA":
        LATEST_TIME_NUMERIC=int(round(time() * 1000))
        TIME_SPENT_MS=int(round(LATEST_TIME_NUMERIC-VERY_BEGINNING_NUMERIC,0))
        if TIME_SPENT_MS > 900000:
            final_screen()
            ScreenNumber=9997
            
    while ScreenNumber == 8:   ### INSTRUCTION SCREEN
        WordCount=14
        BACKGROUNDIMAGE=instructbackgrounds[3]
        InstructionTime=-1
        ScreenNumber, BACKGROUNDIMAGE, InstructionTime, RESET = INSTRUCTIONscreen(ScreenNumber, BACKGROUNDIMAGE, InstructionTime, RESET)
        os.chdir("data/")
        out_file = open(filename,"a")
        out_file.write('sometimes_you_use_numberpad\n')
        out_file.write('wordcount= %d\n'%WordCount)
        out_file.write('InstructionTime_ms= %d\n'%InstructionTime)
        #out_file.write('words_per_s= %d\n'%(int((float(WordCount)/(float(InstructionTime)/1000))*100)/100.0))
        #out_file.write('words_per_s= %d\n'%(int((float(WordCount)/(float(InstructionTime)/1000))*100)/100.0))
        out_file.write('words_per_s= %f NA NA NA NA 1\n'%round((float(WordCount)/(float(InstructionTime)/1000)), 3))
        TIME_END_TRIAL=strftime("%Y-%m-%d %H:%M:%S", localtime())
        out_file.write('timestamp_at_end_of_this_instruction_screen= %s\n'%TIME_END_TRIAL)
        READING_SPEED_LOG.append(round((float(WordCount)/(float(InstructionTime)/1000)), 3))
        out_file.write(' \n')
        out_file.close()
        os.chdir(BASEPATH) 
        ScreenNumber=ScreenNumber+1

    while ScreenNumber == 9:   ### PRACTICE SCREEN FOR NUMBER PAD
        TrialTime=-1  
        ERRORS=0
        os.chdir("data/")
        out_file = open(filename,"a")
        out_file.write('_____________________\n') 
        out_file.write('numberpad_running_log\n')
        out_file.write('_____________________\n') ## we will enter the loop while writing the log file. We can enter each button press. Maybe "time between buttons" is important.
        ScreenNumber, TrialTime, ERRORS, RESET = NUMBERPAD(ScreenNumber, TrialTime, ERRORS, RESET)
        out_file.write('_____________________\n') 
        out_file.write('numberpad_summary\n')
        out_file.write('_____________________\n')
        out_file.write('TrialTime_ms= %d\n'%TrialTime)
        out_file.write('Errors= %d\n'%ERRORS)
        ## assign time and points
        ATTENTION_LOG[2][3]=TrialTime
        if ERRORS == 0:
            ATTENTION_LOG[1][3]=2
        elif ERRORS > 0:
            ATTENTION_LOG[1][3]=0
        TIME_END_TRIAL=strftime("%Y-%m-%d %H:%M:%S", localtime())
        out_file.write('timestamp_at_end_of_this_trial= %s\n'%TIME_END_TRIAL)
        out_file.write(' \n')
        out_file.close()
        os.chdir(BASEPATH) 
        ScreenNumber=ScreenNumber+3
        ## there is now enough data since the initiation of this program to be able to review a summary sheet.
        FIRST_SUBJECT=False
        global FIRST_SUBJECT

    ## time limit skips to the end if 15 mins (900000 ms) have now passed.
    if VERY_BEGINNING_NUMERIC != "NA":
        LATEST_TIME_NUMERIC=int(round(time() * 1000))
        TIME_SPENT_MS=int(round(LATEST_TIME_NUMERIC-VERY_BEGINNING_NUMERIC,0))
        if TIME_SPENT_MS > 900000:
            final_screen()
            ScreenNumber=9997
            
    while ScreenNumber == 12:   ### INSTRUCTION SCREEN
        WordCount=37
        BACKGROUNDIMAGE=instructbackgrounds[5]
        InstructionTime=-1
        ScreenNumber, BACKGROUNDIMAGE, InstructionTime, RESET = INSTRUCTIONscreen(ScreenNumber, BACKGROUNDIMAGE, InstructionTime, RESET)
        os.chdir("data/")
        out_file = open(filename,"a")
        out_file.write('remember_five_words\n')
        out_file.write('wordcount= %d\n'%WordCount)
        out_file.write('InstructionTime_ms= %d\n'%InstructionTime)
        #out_file.write('words_per_s= %d\n'%(int((float(WordCount)/(float(InstructionTime)/1000))*100)/100.0))
        #out_file.write('words_per_s= %d\n'%(int((float(WordCount)/(float(InstructionTime)/1000))*100)/100.0))
        out_file.write('words_per_s= %f NA NA NA NA 1\n'%round((float(WordCount)/(float(InstructionTime)/1000)), 3))
        TIME_END_TRIAL=strftime("%Y-%m-%d %H:%M:%S", localtime())
        out_file.write('timestamp_at_end_of_this_instruction_screen= %s\n'%TIME_END_TRIAL)
        READING_SPEED_LOG.append(round((float(WordCount)/(float(InstructionTime)/1000)), 3))
        out_file.write(' \n')
        out_file.close()
        os.chdir(BASEPATH) 
        ScreenNumber=ScreenNumber+1

    ## these are timestamps for when word presentation starts.
    ## not sure which will be best, but can't do math with c, so probably log as a backup in case
    ## the difference for the other two is discrepent or negative
    TIME_WORDS_PRESENTED_a=int(round(time() * 1000))
    TIME_WORDS_PRESENTED_b=clock()
    TIME_WORDS_PRESENTED_c=strftime("%Y-%m-%d %H:%M:%S", localtime())
    while ScreenNumber >12 and ScreenNumber< 24:   ### THIS IS THE STARTING SCREEN FOR THE PATIENT TO SHOW THE FIVE WORDS
        ScreenNumber = FLASHwords(ScreenNumber)

    while ScreenNumber == 24:   ### INSTRUCTION SCREEN
        WordCount=14 
        BACKGROUNDIMAGE=instructbackgrounds[6]
        InstructionTime=-1
        ScreenNumber, BACKGROUNDIMAGE, InstructionTime, RESET = INSTRUCTIONscreen(ScreenNumber, BACKGROUNDIMAGE, InstructionTime, RESET)
        os.chdir("data/")
        out_file = open(filename,"a")
        out_file.write('few_more_questions\n')
        out_file.write('wordcount= %d\n'%WordCount)
        out_file.write('InstructionTime_ms= %d\n'%InstructionTime)
        #out_file.write('words_per_s= %d\n'%(int((float(WordCount)/(float(InstructionTime)/1000))*100)/100.0))
        #out_file.write('words_per_s= %d\n'%(int((float(WordCount)/(float(InstructionTime)/1000))*100)/100.0))
        out_file.write('words_per_s= %f NA NA NA NA 1\n'%round((float(WordCount)/(float(InstructionTime)/1000)), 3))
        TIME_END_TRIAL=strftime("%Y-%m-%d %H:%M:%S", localtime())
        out_file.write('timestamp_at_end_of_this_instruction_screen= %s\n'%TIME_END_TRIAL)
        READING_SPEED_LOG.append(round((float(WordCount)/(float(InstructionTime)/1000)), 3))
        out_file.write(' \n')
        out_file.close()
        os.chdir(BASEPATH) 
        ScreenNumber=ScreenNumber+1

    TrialTime=-1  
    RESPONSE=" "
    ERRORS=0
    while ScreenNumber == 25:   ### what was that phrase?
        ScreenNumber, TrialTime, RESPONSE, ERRORS, RESET = STATEMENT(ScreenNumber, TrialTime, RESPONSE, ERRORS, RESET)
        os.chdir("data/")
        out_file = open(filename,"a")
        out_file.write('What_was_that_phrase?___summary\n')
        out_file.write('TrialTime_ms= %d\n'%TrialTime)
        out_file.write('with_this_many_premature_attempts_to_end= %d\n'%ERRORS)
        out_file.write('RESPONSE= %s\n'%RESPONSE)
        ## assign time and points
        MEMORY_LOG[2][1]=TrialTime
        if RESPONSE == "CLOSE YOUR EYES":
            MEMORY_LOG[1][1]=1
            out_file.write('answer_correct(Y/N)?= Y\n')    
        else:
            MEMORY_LOG[1][1]=0
            out_file.write('answer_correct(Y/N)?= N\n')
        TIME_END_TRIAL=strftime("%Y-%m-%d %H:%M:%S", localtime())
        out_file.write('timestamp_at_end_of_this_trial= %s\n'%TIME_END_TRIAL)
        out_file.write(' \n')
        out_file.close()
        os.chdir(BASEPATH) 
        ScreenNumber=ScreenNumber+1

    ## time limit skips to the end if 15 mins (900000 ms) have now passed.
    if VERY_BEGINNING_NUMERIC != "NA":
        LATEST_TIME_NUMERIC=int(round(time() * 1000))
        TIME_SPENT_MS=int(round(LATEST_TIME_NUMERIC-VERY_BEGINNING_NUMERIC,0))
        if TIME_SPENT_MS > 900000:
            final_screen()
            ScreenNumber=9997
            
    TrialTime=-1  
    RESPONSE=0
    ERRORS=0
    while ScreenNumber == 26:   ### what was that "J" word?
        ScreenNumber, TrialTime, ERRORS, RESPONSE, RESET = PICKtheJwordAGAIN(ScreenNumber, TrialTime, ERRORS, RESPONSE, RESET)
        os.chdir("data/")
        out_file = open(filename,"a")
        out_file.write('What_was_that_J_word?___summary\n')
        out_file.write('TrialTime_ms= %d\n'%TrialTime)
        out_file.write('with_this_many_premature_attempts_to_end= %d\n'%ERRORS)
        out_file.write('RESPONSE= %s\n'%RESPONSE)
        ## assign time and points
        MEMORY_LOG[2][2]=TrialTime
        if RESPONSE == "Jazz":
            MEMORY_LOG[1][2]=1
            out_file.write('answer_correct(Y/N)?= Y\n')    
        else:
            MEMORY_LOG[1][2]=0
            out_file.write('answer_correct(Y/N)?= N\n')
        TIME_END_TRIAL=strftime("%Y-%m-%d %H:%M:%S", localtime())
        out_file.write('timestamp_at_end_of_this_trial= %s\n'%TIME_END_TRIAL)
        out_file.write(' \n')
        out_file.close()
        os.chdir(BASEPATH) 
        ScreenNumber=ScreenNumber+1

    ## time limit skips to the end if 15 mins (900000 ms) have now passed.
    if VERY_BEGINNING_NUMERIC != "NA":
        LATEST_TIME_NUMERIC=int(round(time() * 1000))
        TIME_SPENT_MS=int(round(LATEST_TIME_NUMERIC-VERY_BEGINNING_NUMERIC,0))
        if TIME_SPENT_MS > 900000:
            final_screen()
            ScreenNumber=9997
            
    TrialTime=-1  
    RESPONSE=0
    ERRORS=0
    while ScreenNumber == 27:   ### what was that number again?
        os.chdir("data/")
        out_file = open(filename,"a")
        out_file.write('_______________________________________________________\n') 
        out_file.write('What_was_prior_numberpad_input?___numberpad_running_log\n')
        out_file.write('_______________________________________________________\n')  ## we will enter the loop while writing the log file. We can enter each button press. Maybe "time between buttons" is important.
        ScreenNumber, TrialTime, ERRORS, RESPONSE, RESET = NUMBERPADagain(ScreenNumber, TrialTime, ERRORS, RESPONSE, RESET)
        out_file.write('__________________________\n') 
        out_file.write('What_was_prior_numberpad_input?___summary\n')
        out_file.write('__________________________\n')
        out_file.write('TrialTime_ms= %d\n'%TrialTime)
        out_file.write('with_this_many_premature_attempts_to_end= %d\n'%ERRORS)
        out_file.write('RESPONSE= %d\n'%RESPONSE)
        MEMORY_LOG[0][3]=RESPONSE
        MEMORY_LOG[2][3]=TrialTime
        if RESPONSE == 1239:
            MEMORY_LOG[1][3]=1
            out_file.write('answer_correct(Y/N)?= Y\n')    
        else:
            MEMORY_LOG[1][3]=0
            out_file.write('answer_correct(Y/N)?= N\n')
        TIME_END_TRIAL=strftime("%Y-%m-%d %H:%M:%S", localtime())
        out_file.write('timestamp_at_end_of_this_trial= %s\n'%TIME_END_TRIAL)
        out_file.write(' \n')
        out_file.close()
        os.chdir(BASEPATH) 
        ScreenNumber=ScreenNumber+1

    ## time limit skips to the end if 15 mins (900000 ms) have now passed.
    if VERY_BEGINNING_NUMERIC != "NA":
        LATEST_TIME_NUMERIC=int(round(time() * 1000))
        TIME_SPENT_MS=int(round(LATEST_TIME_NUMERIC-VERY_BEGINNING_NUMERIC,0))
        if TIME_SPENT_MS > 900000:
            final_screen()
            ScreenNumber=9997
            
    TrialTime=-1  
    RESPONSE=0
    ERRORS=0
    while ScreenNumber == 28:   ### what month is it?
        ScreenNumber, TrialTime, RESPONSE, ERRORS, RESET = MONTHS(ScreenNumber, TrialTime, RESPONSE, ERRORS, RESET)
        os.chdir("data/")
        out_file = open(filename,"a")
        out_file.write('What_month_is_it?___summary\n')
        out_file.write('TrialTime_ms= %d\n'%TrialTime)
        out_file.write('with_this_many_premature_attempts_to_end= %d\n'%ERRORS)
        MonthsINtext=["January","February","March","April","May","June","July","August","September","October","November","December"]
        out_file.write('RESPONSE= %s\n'%MonthsINtext[(RESPONSE-1)])
        ORIENTATION_LOG[2][1]=TrialTime
        if RESPONSE == localtime()[1]:
            ORIENTATION_LOG[1][1]=1
            out_file.write('answer_correct(Y/N)?= Y\n')    
        else:
            ORIENTATION_LOG[1][1]=0
            out_file.write('answer_correct(Y/N)?= N\n')
        TIME_END_TRIAL=strftime("%Y-%m-%d %H:%M:%S", localtime())
        out_file.write('timestamp_at_end_of_this_trial= %s\n'%TIME_END_TRIAL)
        out_file.write(' \n')
        out_file.close()
        os.chdir(BASEPATH) 
        ScreenNumber=ScreenNumber+1

    ## time limit skips to the end if 15 mins (900000 ms) have now passed.
    if VERY_BEGINNING_NUMERIC != "NA":
        LATEST_TIME_NUMERIC=int(round(time() * 1000))
        TIME_SPENT_MS=int(round(LATEST_TIME_NUMERIC-VERY_BEGINNING_NUMERIC,0))
        if TIME_SPENT_MS > 900000:
            final_screen()
            ScreenNumber=9997
            
    TrialTime=-1  
    RESPONSE=0
    ERRORS=0
    while ScreenNumber == 29:   ### what year is it?
        os.chdir("data/")
        out_file = open(filename,"a")
        out_file.write('________________________________________\n') 
        out_file.write('What_year_is_it?___numberpad_running_log\n')
        out_file.write('________________________________________\n')  ## we will enter the loop while writing the log file. We can enter each button press. Maybe "time between buttons" is important.
        ScreenNumber, TrialTime, RESPONSE, ERRORS, RESET = YEARPAD(ScreenNumber, TrialTime, RESPONSE, ERRORS, RESET)
        out_file.write('__________________________\n') 
        out_file.write('What_year_is_it?___summary\n')
        out_file.write('__________________________\n')
        out_file.write('TrialTime_ms= %d\n'%TrialTime)
        out_file.write('with_this_many_premature_attempts_to_end= %d\n'%ERRORS)
        out_file.write('RESPONSE= %d\n'%RESPONSE)
        ORIENTATION_LOG[2][2]=TrialTime
        if RESPONSE == localtime()[0]:
            ORIENTATION_LOG[1][2]=1
            out_file.write('answer_correct(Y/N)?= Y\n')    
        else:
            ORIENTATION_LOG[1][2]=0
            out_file.write('answer_correct(Y/N)?= N\n')
        TIME_END_TRIAL=strftime("%Y-%m-%d %H:%M:%S", localtime())
        out_file.write('timestamp_at_end_of_this_trial= %s\n'%TIME_END_TRIAL)
        out_file.write(' \n')
        out_file.close()
        os.chdir(BASEPATH) 
        ScreenNumber=ScreenNumber+1

    ## time limit skips to the end if 15 mins (900000 ms) have now passed.
    if VERY_BEGINNING_NUMERIC != "NA":
        LATEST_TIME_NUMERIC=int(round(time() * 1000))
        TIME_SPENT_MS=int(round(LATEST_TIME_NUMERIC-VERY_BEGINNING_NUMERIC,0))
        if TIME_SPENT_MS > 900000:
            final_screen()
            ScreenNumber=9997
            
    TrialTime=-1  
    RESPONSE=0
    ERRORS=0
    while ScreenNumber == 30:   ### what day is it?
        ScreenNumber, TrialTime, RESPONSE, ERRORS, RESET = DAYofWEEK(ScreenNumber, TrialTime, RESPONSE, ERRORS, RESET)
        os.chdir("data/")
        out_file = open(filename,"a")
        out_file.write('What_day_of_week_is_it?___summary\n')
        out_file.write('TrialTime_ms= %d\n'%TrialTime)
        out_file.write('with_this_many_premature_attempts_to_end= %d\n'%ERRORS)
        DaysINtext=["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
        out_file.write('RESPONSE= %s\n'%DaysINtext[(RESPONSE-1)])
        ORIENTATION_LOG[0][3]=DaysINtext[(RESPONSE-1)]
        ORIENTATION_LOG[2][3]=TrialTime
        if (RESPONSE-1) == int(strftime("%w", localtime())):
            ORIENTATION_LOG[1][3]=1
            out_file.write('answer_correct(Y/N)?= Y\n')    
        else:
            ORIENTATION_LOG[1][3]=0
            out_file.write('answer_correct(Y/N)?= N\n')
        TIME_END_TRIAL=strftime("%Y-%m-%d %H:%M:%S", localtime())
        out_file.write('timestamp_at_end_of_this_trial= %s\n'%TIME_END_TRIAL)
        out_file.write(' \n')
        out_file.close()
        os.chdir(BASEPATH) 
        ScreenNumber=ScreenNumber+1

    ## time limit skips to the end if 15 mins (900000 ms) have now passed.
    if VERY_BEGINNING_NUMERIC != "NA":
        LATEST_TIME_NUMERIC=int(round(time() * 1000))
        TIME_SPENT_MS=int(round(LATEST_TIME_NUMERIC-VERY_BEGINNING_NUMERIC,0))
        if TIME_SPENT_MS > 900000:
            final_screen()
            ScreenNumber=9997
            
    TrialTime=-1  
    RESPONSE=0
    ERRORS=0
    while ScreenNumber == 31:   ### what state are we in?
        ScreenNumber, TrialTime, RESPONSE, ERRORS, RESET = STATE(ScreenNumber, TrialTime, RESPONSE, ERRORS, RESET)
        os.chdir("data/")
        out_file = open(filename,"a")
        out_file.write('What_state_are_we_in?___summary\n')
        out_file.write('TrialTime_ms= %d\n'%TrialTime)
        out_file.write('with_this_many_premature_attempts_to_end= %d\n'%ERRORS)
        out_file.write('RESPONSE= %s\n'%RESPONSE)
        ORIENTATION_LOG[0][4]=RESPONSE
        ORIENTATION_LOG[2][4]=TrialTime
        #<$%^> RESPONSE changed from a direct reference to the hard-coded list of states to the modifiable STATE_WHEN_PROGRAM_INITIATED[0]
        if RESPONSE == STATE_WHEN_PROGRAM_INITIATED[0]:
        #</$%^>
            ORIENTATION_LOG[1][4]=1
            out_file.write('answer_correct(Y/N)?= Y\n')    
        else:
            ORIENTATION_LOG[1][4]=0
            out_file.write('answer_correct(Y/N)?= N\n')
        TIME_END_TRIAL=strftime("%Y-%m-%d %H:%M:%S", localtime())
        out_file.write('timestamp_at_end_of_this_trial= %s\n'%TIME_END_TRIAL)
        out_file.write(' \n')
        out_file.close()
        os.chdir(BASEPATH) 
        ScreenNumber=ScreenNumber+1

    ## time limit skips to the end if 15 mins (900000 ms) have now passed.
    if VERY_BEGINNING_NUMERIC != "NA":
        LATEST_TIME_NUMERIC=int(round(time() * 1000))
        TIME_SPENT_MS=int(round(LATEST_TIME_NUMERIC-VERY_BEGINNING_NUMERIC,0))
        if TIME_SPENT_MS > 900000:
            final_screen()
            ScreenNumber=9997
            
    ## if someone makes it this far, should be able to at least assign a partial score (like the six-item-screener):
    while ScreenNumber == 32:   ### what state are we in?
        os.chdir("data/")
        filename_simple_firstFEW = "%s_%d_simple_firstFEW.txt"%(strftime("%Y-%m-%d", localtime()), subject_number)
        out_file = open(filename_simple_firstFEW,"w")
        out_file.write('subject= %d\n'%subject_number)
        out_file.write('date= %s\n'%(strftime("%Y_%m_%d", localtime())))
        out_file.write('___________________________________________\n')
        out_file.write('%s %s %s \n'%(ORIENTATION_LOG[0][0], ORIENTATION_LOG[1][0], ORIENTATION_LOG[2][0]))
        out_file.write('%s %s %s \n'%(ORIENTATION_LOG[0][1], ORIENTATION_LOG[1][1], ORIENTATION_LOG[2][1]))
        out_file.write('%s %s %s \n'%(ORIENTATION_LOG[0][2], ORIENTATION_LOG[1][2], ORIENTATION_LOG[2][2]))
        out_file.write('%s %s %s \n'%(ORIENTATION_LOG[0][3], ORIENTATION_LOG[1][3], ORIENTATION_LOG[2][3]))
        out_file.write('%s %s %s \n'%(ORIENTATION_LOG[0][4], ORIENTATION_LOG[1][4], ORIENTATION_LOG[2][4]))
        out_file.write('___________________________________________\n')
        out_file.write('%s %s %s \n'%(MEMORY_LOG[0][0], MEMORY_LOG[1][0], MEMORY_LOG[2][0]))
        out_file.write('%s %s %s \n'%(MEMORY_LOG[0][1], MEMORY_LOG[1][1], MEMORY_LOG[2][1]))
        out_file.write('%s %s %s \n'%(MEMORY_LOG[0][2], MEMORY_LOG[1][2], MEMORY_LOG[2][2]))
        out_file.write('%s %s %s \n'%(MEMORY_LOG[0][3], MEMORY_LOG[1][3], MEMORY_LOG[2][3]))
        out_file.close()
        os.chdir(BASEPATH)
        ScreenNumber=ScreenNumber+1

    ## these are timestamps for when word recall starts.
    ## not sure which will be best, but can't do math with c, so probably log as a backup in case
    ## the difference for the other two is discrepent or negative
    TIME_WORDS_RECALLED_a=int(round(time() * 1000))
    TIME_WORDS_RECALLED_b=clock()
    TIME_WORDS_RECALLED_c=strftime("%Y-%m-%d %H:%M:%S", localtime())
    TrialTime=-1  
    RESPONSE=0
    ERRORS=0
    while ScreenNumber == 33:   ### Free Recall
        ScreenNumber, TrialTime, RESPONSE, ERRORS, RESET = FREErecall(ScreenNumber, TrialTime, RESPONSE, ERRORS, RESET)
        os.chdir("data/")
        out_file = open(filename,"a")
        out_file.write('FIVE_WORD_RECALL\n')
        out_file.write('TrialTime_ms= %d\n'%TrialTime)
        out_file.write('with_this_many_inappropriate(too_few_or_too_many_words)_attempts_to_end= %d\n'%ERRORS)
        out_file.write('alphabetized_RESPONSES= %s %s %s %s %s %s\n'%(RESPONSE[0],RESPONSE[1],RESPONSE[2],RESPONSE[3],RESPONSE[4],RESPONSE[5])) #<- RESPONSE has unusual length because the initial [" "] takes up a slot.
        SUM_POINTS=0
        if "APPLE" in RESPONSE:
            SUM_POINTS=SUM_POINTS+1
        if "CAR" in RESPONSE:
            SUM_POINTS=SUM_POINTS+1
        if "HOUSE" in RESPONSE:
            SUM_POINTS=SUM_POINTS+1
        if "PEN" in RESPONSE:
            SUM_POINTS=SUM_POINTS+1
        if "TIE" in RESPONSE:
            SUM_POINTS=SUM_POINTS+1
        out_file.write('freely_recalled_how_many_of_5?= %s\n'%SUM_POINTS)
        MEMORY_LOG[1][4]=SUM_POINTS
        MEMORY_LOG[2][4]=TrialTime
        out_file.write('timestamp_of_first_word_presentation_hr_min_sec?= %s\n'%TIME_WORDS_PRESENTED_c)
        out_file.write('timestamp_of_word_recall_start_hr_min_sec?= %s\n'%TIME_WORDS_RECALLED_c)
        TIME_DIFFERENCE_b=(TIME_WORDS_RECALLED_b-TIME_WORDS_PRESENTED_b) ##<- in seconds
        TIME_DIFFERENCE_a=int(round(TIME_WORDS_RECALLED_a-TIME_WORDS_PRESENTED_a))/1000 ##<- in seconds
        out_file.write('seconds_between_present_and_recall(method_1)?= %s\n'%TIME_DIFFERENCE_a)
        out_file.write('seconds_between_present_and_recall(method_2)?= %s\n'%TIME_DIFFERENCE_b)
        TIME_END_TRIAL=strftime("%Y-%m-%d %H:%M:%S", localtime())
        out_file.write('timestamp_at_end_of_this_trial= %s\n'%TIME_END_TRIAL)
        out_file.write(' \n')
        out_file.close()
        os.chdir(BASEPATH) 
        ScreenNumber=ScreenNumber+1

    ## time limit skips to the end if 15 mins (900000 ms) have now passed.
    if VERY_BEGINNING_NUMERIC != "NA":
        LATEST_TIME_NUMERIC=int(round(time() * 1000))
        TIME_SPENT_MS=int(round(LATEST_TIME_NUMERIC-VERY_BEGINNING_NUMERIC,0))
        if TIME_SPENT_MS > 900000:
            final_screen()
            ScreenNumber=9997
            
    TrialTime=-1  
    RESPONSE=0
    ERRORS=0
    while ScreenNumber == 34:   ### SLUMS money questions
        os.chdir("data/")
        out_file = open(filename,"a")
        out_file.write('_____________________________________________\n') 
        out_file.write('SLUMS_how_much_spent?___numberpad_running_log\n')
        out_file.write('_____________________________________________\n')  ## we will enter the loop while writing the log file. We can enter each button press. Maybe "time between buttons" is important.
        ScreenNumber, TrialTime, RESPONSE, ERRORS, RESET = MONEYPAD(ScreenNumber, TrialTime, RESPONSE, ERRORS, RESET)
        out_file.write('_______________________________\n') 
        out_file.write('SLUMS_how_much_spent?___summary\n')
        out_file.write('_______________________________\n')
        out_file.write('TrialTime_ms= %d\n'%TrialTime)
        MATH_LOG[2][1]=TrialTime
        out_file.write('with_this_many_premature_attempts_to_end= %d\n'%ERRORS)
        out_file.write('RESPONSE= %d\n'%RESPONSE)
        if RESPONSE == 67:
            MATH_LOG[1][1]=1
            out_file.write('answer_correct(Y/N)?= Y\n')    
        else:
            MATH_LOG[1][1]=0
            out_file.write('answer_correct(Y/N)?= N\n')
        TIME_END_TRIAL=strftime("%Y-%m-%d %H:%M:%S", localtime())
        out_file.write('timestamp_at_end_of_this_trial= %s\n'%TIME_END_TRIAL)
        out_file.write(' \n')
        out_file.close()
        os.chdir(BASEPATH) 
        ScreenNumber=ScreenNumber+1

    ## time limit skips to the end if 15 mins (900000 ms) have now passed.
    if VERY_BEGINNING_NUMERIC != "NA":
        LATEST_TIME_NUMERIC=int(round(time() * 1000))
        TIME_SPENT_MS=int(round(LATEST_TIME_NUMERIC-VERY_BEGINNING_NUMERIC,0))
        if TIME_SPENT_MS > 900000:
            final_screen()
            ScreenNumber=9997
            
    TrialTime=-1  
    RESPONSE=0
    ERRORS=0
    while ScreenNumber == 35:   ### SLUMS money question # 2
        os.chdir("data/")
        out_file = open(filename,"a")
        out_file.write('_____________________________________________\n') 
        out_file.write('SLUMS_how_much_left?____numberpad_running_log\n')
        out_file.write('_____________________________________________\n')  ## we will enter the loop while writing the log file. We can enter each button press. Maybe "time between buttons" is important.
        ScreenNumber, TrialTime, RESPONSE, ERRORS, RESET = MONEYPAD(ScreenNumber, TrialTime, RESPONSE, ERRORS, RESET)
        out_file.write('_______________________________\n') 
        out_file.write('SLUMS_how_much_left?____summary\n')
        out_file.write('_______________________________\n')
        out_file.write('TrialTime_ms= %d\n'%TrialTime)
        out_file.write('with_this_many_premature_attempts_to_end= %d\n'%ERRORS)
        out_file.write('RESPONSE= %d\n'%RESPONSE)
        MATH_LOG[2][2]=TrialTime
        if RESPONSE == 33:
            MATH_LOG[1][2]=2
            out_file.write('answer_correct(Y/N)?= Y\n')    
        else:
            MATH_LOG[1][2]=0
            out_file.write('answer_correct(Y/N)?= N\n')
        TIME_END_TRIAL=strftime("%Y-%m-%d %H:%M:%S", localtime())
        out_file.write('timestamp_at_end_of_this_trial= %s\n'%TIME_END_TRIAL)
        out_file.write(' \n')
        out_file.close()
        os.chdir(BASEPATH) 
        ScreenNumber=ScreenNumber+1

    ## time limit skips to the end if 15 mins (900000 ms) have now passed.
    if VERY_BEGINNING_NUMERIC != "NA":
        LATEST_TIME_NUMERIC=int(round(time() * 1000))
        TIME_SPENT_MS=int(round(LATEST_TIME_NUMERIC-VERY_BEGINNING_NUMERIC,0))
        if TIME_SPENT_MS > 900000:
            final_screen()
            ScreenNumber=9997
            
### INSTRUCTION SCREEN FOR DRAWING COMPLETION TASK
    while ScreenNumber == 36:
        WordCount=18
        BACKGROUNDIMAGE=taskbackgrounds[16]
        InstructionTime=-1
        ScreenNumber, BACKGROUNDIMAGE, InstructionTime, RESET = INSTRUCTIONscreen(ScreenNumber, BACKGROUNDIMAGE, InstructionTime, RESET)
        os.chdir("data/")
        out_file = open(filename,"a")
        out_file.write('next_you_will_see_some_drawings\n')
        out_file.write('wordcount= %d\n'%WordCount)
        out_file.write('InstructionTime_ms= %d\n'%InstructionTime)
        #out_file.write('words_per_s= %d\n'%(int((float(WordCount)/(float(InstructionTime)/1000))*100)/100.0))
        out_file.write('words_per_s= %f NA NA NA NA 1\n'%round((float(WordCount)/(float(InstructionTime)/1000)), 3))
        TIME_END_TRIAL=strftime("%Y-%m-%d %H:%M:%S", localtime())
        READING_SPEED_LOG.append(round((float(WordCount)/(float(InstructionTime)/1000)), 3))
        out_file.write('timestamp_at_end_of_this_instruction_screen= %s\n'%TIME_END_TRIAL)
        out_file.write(' \n')
        out_file.close()
        os.chdir(BASEPATH) 
        ScreenNumber=ScreenNumber+1

## ACUAL DRAWING (we alternate between DRAWTASKODD and DRAWTASKEVEN)
    TrialTime=-1  
    RESPONSE=0
    ERRORS=0
    while ScreenNumber == 37:
        ScreenNumber, TrialTime, RESPONSE, ERRORS, RESET = DRAWTASKODD(ScreenNumber, TrialTime, RESPONSE, ERRORS, RESET)
        os.chdir("data/")
        out_file = open(filename,"a")
        out_file.write('DRAWING_TASK_01\n')
        out_file.write('TrialTime_ms= %d\n'%TrialTime)
        out_file.write('with_this_many_inappropriate(too_few_or_too_many_selection)_attempts_to_end= %d\n'%ERRORS)
        out_file.write('alphabetized_RESPONSES= %s %s %s\n'%(RESPONSE[0],RESPONSE[1],RESPONSE[2])) #<- RESPONSE has unusual length because the initial [" "] takes up a slot.
        SUM_POINTS=0
        if "ONE" in RESPONSE:
            SUM_POINTS=SUM_POINTS+1
        if "FIVE" in RESPONSE:
            SUM_POINTS=SUM_POINTS+1
        out_file.write('correct_out_of_2?= %s\n'%SUM_POINTS)
        # log results
        SPATIAL_LOG[2][1]=TrialTime
        if SUM_POINTS == 2:
            SPATIAL_LOG[1][1]=1
        elif SUM_POINTS < 2:
            SPATIAL_LOG[1][1]=0
        out_file.write(' \n')
        out_file.close()
        os.chdir(BASEPATH) 
        ScreenNumber=ScreenNumber+1
    TrialTime=-1  
    RESPONSE=0
    ERRORS=0
    while ScreenNumber == 38:
        ScreenNumber, TrialTime, RESPONSE, ERRORS, RESET = DRAWTASKEVEN(ScreenNumber, TrialTime, RESPONSE, ERRORS, RESET)
        os.chdir("data/")
        out_file = open(filename,"a")
        out_file.write('DRAWING_TASK_02\n')
        out_file.write('TrialTime_ms= %d\n'%TrialTime)
        out_file.write('with_this_many_inappropriate(too_few_or_too_many_selection)_attempts_to_end= %d\n'%ERRORS)
        out_file.write('alphabetized_RESPONSES= %s %s %s\n'%(RESPONSE[0],RESPONSE[1],RESPONSE[2])) #<- RESPONSE has unusual length because the initial [" "] takes up a slot.
        SUM_POINTS=0
        if "TWO" in RESPONSE:
            SUM_POINTS=SUM_POINTS+1
        if "SIX" in RESPONSE:
            SUM_POINTS=SUM_POINTS+1
        out_file.write('correct_out_of_2?= %s\n'%SUM_POINTS)
        # log results
        SPATIAL_LOG[2][2]=TrialTime
        if SUM_POINTS == 2:
            SPATIAL_LOG[1][2]=1
        elif SUM_POINTS < 2:
            SPATIAL_LOG[1][2]=0
        out_file.write(' \n')
        out_file.close()
        os.chdir(BASEPATH) 
        ScreenNumber=ScreenNumber+1  
    TrialTime=-1  
    RESPONSE=0
    ERRORS=0
    while ScreenNumber == 39:
        ScreenNumber, TrialTime, RESPONSE, ERRORS, RESET = DRAWTASKODD(ScreenNumber, TrialTime, RESPONSE, ERRORS, RESET)
        os.chdir("data/")
        out_file = open(filename,"a")
        out_file.write('DRAWING_TASK_03\n')
        out_file.write('TrialTime_ms= %d\n'%TrialTime)
        out_file.write('with_this_many_inappropriate(too_few_or_too_many_selection)_attempts_to_end= %d\n'%ERRORS)
        out_file.write('alphabetized_RESPONSES= %s %s %s\n'%(RESPONSE[0],RESPONSE[1],RESPONSE[2])) #<- RESPONSE has unusual length because the initial [" "] takes up a slot.
        SUM_POINTS=0
        if "THREE" in RESPONSE:
            SUM_POINTS=SUM_POINTS+1
        if "SIX" in RESPONSE:
            SUM_POINTS=SUM_POINTS+1
        out_file.write('correct_out_of_2?= %s\n'%SUM_POINTS)
        # log results
        SPATIAL_LOG[2][3]=TrialTime
        if SUM_POINTS == 2:
            SPATIAL_LOG[1][3]=1
        elif SUM_POINTS < 2:
            SPATIAL_LOG[1][3]=0
        out_file.write(' \n')
        out_file.close()
        os.chdir(BASEPATH) 
        ScreenNumber=ScreenNumber+1
    TrialTime=-1  
    RESPONSE=0
    ERRORS=0
    while ScreenNumber == 40:
        ScreenNumber, TrialTime, RESPONSE, ERRORS, RESET = DRAWTASKEVEN(ScreenNumber, TrialTime, RESPONSE, ERRORS, RESET)
        os.chdir("data/")
        out_file = open(filename,"a")
        out_file.write('DRAWING_TASK_04\n')
        out_file.write('TrialTime_ms= %d\n'%TrialTime)
        out_file.write('with_this_many_inappropriate(too_few_or_too_many_selection)_attempts_to_end= %d\n'%ERRORS)
        out_file.write('alphabetized_RESPONSES= %s %s %s\n'%(RESPONSE[0],RESPONSE[1],RESPONSE[2])) #<- RESPONSE has unusual length because the initial [" "] takes up a slot.
        SUM_POINTS=0
        if "THREE" in RESPONSE:
            SUM_POINTS=SUM_POINTS+1
        if "FOUR" in RESPONSE:
            SUM_POINTS=SUM_POINTS+1
        out_file.write('correct_out_of_2?= %s\n'%SUM_POINTS)
        # log results
        SPATIAL_LOG[2][4]=TrialTime
        if SUM_POINTS == 2:
            SPATIAL_LOG[1][4]=1
        elif SUM_POINTS < 2:
            SPATIAL_LOG[1][4]=0
        out_file.write(' \n')
        out_file.close()
        os.chdir(BASEPATH) 
        ScreenNumber=ScreenNumber+1


    ## time limit skips to the end if 15 mins (900000 ms) have now passed.
    if VERY_BEGINNING_NUMERIC != "NA":
        LATEST_TIME_NUMERIC=int(round(time() * 1000))
        TIME_SPENT_MS=int(round(LATEST_TIME_NUMERIC-VERY_BEGINNING_NUMERIC,0))
        if TIME_SPENT_MS > 900000:
            final_screen()
            ScreenNumber=9997


### INSTRUCTION SCREEN FOR STROOP
    while ScreenNumber == 41:
        WordCount=14
        BACKGROUNDIMAGE=stroopINSTRUCT
        InstructionTime=-1
        ScreenNumber, BACKGROUNDIMAGE, InstructionTime, RESET = INSTRUCTIONscreenODD(ScreenNumber, BACKGROUNDIMAGE, InstructionTime, RESET)
        os.chdir("data/")
        out_file = open(filename,"a")
        out_file.write('next_you_will_see_some_words\n')
        out_file.write('wordcount= %d\n'%WordCount)
        out_file.write('InstructionTime_ms= %d\n'%InstructionTime)
        #out_file.write('words_per_s= %d\n'%(int((float(WordCount)/(float(InstructionTime)/1000))*100)/100.0))
        #out_file.write('words_per_s= %d\n'%(int((float(WordCount)/(float(InstructionTime)/1000))*100)/100.0))
        out_file.write('words_per_s= %f NA NA NA NA 1\n'%round((float(WordCount)/(float(InstructionTime)/1000)), 3))
        TIME_END_TRIAL=strftime("%Y-%m-%d %H:%M:%S", localtime())
        READING_SPEED_LOG.append(round((float(WordCount)/(float(InstructionTime)/1000)), 3))
        out_file.write('timestamp_at_end_of_this_instruction_screen= %s\n'%TIME_END_TRIAL)
        out_file.write(' \n')
        out_file.close()
        os.chdir(BASEPATH) 
        ScreenNumber=ScreenNumber+1

## ACUAL STROOP (we alternate between STROOPEVEN and STROOPODD)
    while ScreenNumber == 42:
        SelectionTime=0
        TrialTime=-1  
        RESPONSE=0
        ERRORS=0
        WORD=stroopWORDorder[(ScreenNumber-42)]
        TEXTCOLOR=stroopWORDcolor[(ScreenNumber-42)]
        TRUEERRORS=0
        ## the stroop won't let you advance until you pick the correct answer, hence "ERRORS" and "TRUEERRORS"
        ## logged, but not "RESPONSE",since "REPSONSE" is always = TEXTCOLOR
        ERRORBUNDLE=[0,0]
        ScreenNumber, TrialTime, ERRORBUNDLE, RESET, WORD, TEXTCOLOR, SelectionTime = STROOPODD(ScreenNumber, TrialTime, ERRORBUNDLE, RESET, WORD, TEXTCOLOR, SelectionTime)
        ERRORS=ERRORBUNDLE[0]
        TRUEERRORS=ERRORBUNDLE[1]
        os.chdir("data/")
        out_file = open(filename,"a")
        out_file.write(' \n')
        out_file.write('___STROOP_TRIAL_01\n')
        out_file.write('word_says= %s\n'%WORD)
        out_file.write('text_color_is= %s\n'%TEXTCOLOR)
        out_file.write('TrialTime_ms= %d NA NA NA NA 999\n'%TrialTime)
        out_file.write('with_this_many_premature_attempts_to_end= %d\n'%ERRORS)
        out_file.write('with_this_many_ERRORS= %d\n'%TRUEERRORS)
        out_file.write('motor_speed__time_between_last_selection_and_next_button_push_ms= %d\n'%(TrialTime-SelectionTime))
        TIME_END_TRIAL=strftime("%Y-%m-%d %H:%M:%S", localtime())
        out_file.write('timestamp_at_end_of_this_trial= %s\n'%TIME_END_TRIAL)
        out_file.write(' \n')
        out_file.close()
        STROOP_LOG[2][1]=TrialTime
        STROOP_LOG[1][1]=TRUEERRORS
        os.chdir(BASEPATH) 
        ScreenNumber=ScreenNumber+1
    while ScreenNumber == 43:
        SelectionTime=0
        TrialTime=-1  
        RESPONSE=0
        ERRORS=0
        WORD=stroopWORDorder[(ScreenNumber-42)]
        TEXTCOLOR=stroopWORDcolor[(ScreenNumber-42)]
        TRUEERRORS=0
        ## the stroop won't let you advance until you pick the correct answer, hence "ERRORS" and "TRUEERRORS"
        ## logged, but not "RESPONSE",since "REPSONSE" is always = TEXTCOLOR
        ERRORBUNDLE=[0,0]
        ScreenNumber, TrialTime, ERRORBUNDLE, RESET, WORD, TEXTCOLOR, SelectionTime = STROOPEVEN(ScreenNumber, TrialTime, ERRORBUNDLE, RESET, WORD, TEXTCOLOR, SelectionTime)
        ERRORS=ERRORBUNDLE[0]
        TRUEERRORS=ERRORBUNDLE[1]
        os.chdir("data/")
        out_file = open(filename,"a")
        out_file.write(' \n')
        out_file.write('___STROOP_TRIAL_02\n')
        out_file.write('word_says= %s\n'%WORD)
        out_file.write('text_color_is= %s\n'%TEXTCOLOR)
        out_file.write('TrialTime_ms= %d NA NA NA NA 999\n'%TrialTime)
        out_file.write('with_this_many_premature_attempts_to_end= %d\n'%ERRORS)
        out_file.write('with_this_many_ERRORS= %d\n'%TRUEERRORS)
        out_file.write('motor_speed__time_between_last_selection_and_next_button_push_ms= %d\n'%(TrialTime-SelectionTime))
        TIME_END_TRIAL=strftime("%Y-%m-%d %H:%M:%S", localtime())
        out_file.write('timestamp_at_end_of_this_trial= %s\n'%TIME_END_TRIAL)
        out_file.write(' \n')
        out_file.close()
        STROOP_LOG[2][2]=TrialTime
        STROOP_LOG[1][2]=TRUEERRORS
        os.chdir(BASEPATH) 
        ScreenNumber=ScreenNumber+1
    while ScreenNumber == 44:
        SelectionTime=0
        TrialTime=-1  
        RESPONSE=0
        ERRORS=0
        WORD=stroopWORDorder[(ScreenNumber-42)]
        TEXTCOLOR=stroopWORDcolor[(ScreenNumber-42)]
        TRUEERRORS=0
        ## the stroop won't let you advance until you pick the correct answer, hence "ERRORS" and "TRUEERRORS"
        ## logged, but not "RESPONSE",since "REPSONSE" is always = TEXTCOLOR
        ERRORBUNDLE=[0,0]
        ScreenNumber, TrialTime, ERRORBUNDLE, RESET, WORD, TEXTCOLOR, SelectionTime = STROOPODD(ScreenNumber, TrialTime, ERRORBUNDLE, RESET, WORD, TEXTCOLOR, SelectionTime)
        ERRORS=ERRORBUNDLE[0]
        TRUEERRORS=ERRORBUNDLE[1]
        os.chdir("data/")
        out_file = open(filename,"a")
        out_file.write(' \n')
        out_file.write('___STROOP_TRIAL_03\n')
        out_file.write('word_says= %s\n'%WORD)
        out_file.write('text_color_is= %s\n'%TEXTCOLOR)
        out_file.write('TrialTime_ms= %d NA NA NA NA 999\n'%TrialTime)
        out_file.write('with_this_many_premature_attempts_to_end= %d\n'%ERRORS)
        out_file.write('with_this_many_ERRORS= %d\n'%TRUEERRORS)
        out_file.write('motor_speed__time_between_last_selection_and_next_button_push_ms= %d\n'%(TrialTime-SelectionTime))
        TIME_END_TRIAL=strftime("%Y-%m-%d %H:%M:%S", localtime())
        out_file.write('timestamp_at_end_of_this_trial= %s\n'%TIME_END_TRIAL)
        out_file.write(' \n')
        out_file.close()
        STROOP_LOG[2][3]=TrialTime
        STROOP_LOG[1][3]=TRUEERRORS
        os.chdir(BASEPATH) 
        ScreenNumber=ScreenNumber+1
    while ScreenNumber == 45:
        SelectionTime=0
        TrialTime=-1  
        RESPONSE=0
        ERRORS=0
        WORD=stroopWORDorder[(ScreenNumber-42)]
        TEXTCOLOR=stroopWORDcolor[(ScreenNumber-42)]
        TRUEERRORS=0
        ## the stroop won't let you advance until you pick the correct answer, hence "ERRORS" and "TRUEERRORS"
        ## logged, but not "RESPONSE",since "REPSONSE" is always = TEXTCOLOR
        ERRORBUNDLE=[0,0]
        ScreenNumber, TrialTime, ERRORBUNDLE, RESET, WORD, TEXTCOLOR, SelectionTime = STROOPEVEN(ScreenNumber, TrialTime, ERRORBUNDLE, RESET, WORD, TEXTCOLOR, SelectionTime)
        ERRORS=ERRORBUNDLE[0]
        TRUEERRORS=ERRORBUNDLE[1]
        os.chdir("data/")
        out_file = open(filename,"a")
        out_file.write(' \n')
        out_file.write('___STROOP_TRIAL_04\n')
        out_file.write('word_says= %s\n'%WORD)
        out_file.write('text_color_is= %s\n'%TEXTCOLOR)
        out_file.write('TrialTime_ms= %d NA NA NA NA 999\n'%TrialTime)
        out_file.write('with_this_many_premature_attempts_to_end= %d\n'%ERRORS)
        out_file.write('with_this_many_ERRORS= %d\n'%TRUEERRORS)
        out_file.write('motor_speed__time_between_last_selection_and_next_button_push_ms= %d\n'%(TrialTime-SelectionTime))
        TIME_END_TRIAL=strftime("%Y-%m-%d %H:%M:%S", localtime())
        out_file.write('timestamp_at_end_of_this_trial= %s\n'%TIME_END_TRIAL)
        out_file.write(' \n')
        out_file.close()
        STROOP_LOG[2][4]=TrialTime
        STROOP_LOG[1][4]=TRUEERRORS
        os.chdir(BASEPATH) 
        ScreenNumber=ScreenNumber+1
    while ScreenNumber == 46:
        SelectionTime=0
        TrialTime=-1  
        RESPONSE=0
        ERRORS=0
        WORD=stroopWORDorder[(ScreenNumber-42)]
        TEXTCOLOR=stroopWORDcolor[(ScreenNumber-42)]
        TRUEERRORS=0
        ## the stroop won't let you advance until you pick the correct answer, hence "ERRORS" and "TRUEERRORS"
        ## logged, but not "RESPONSE",since "REPSONSE" is always = TEXTCOLOR
        ERRORBUNDLE=[0,0]
        ScreenNumber, TrialTime, ERRORBUNDLE, RESET, WORD, TEXTCOLOR, SelectionTime = STROOPODD(ScreenNumber, TrialTime, ERRORBUNDLE, RESET, WORD, TEXTCOLOR, SelectionTime)
        ERRORS=ERRORBUNDLE[0]
        TRUEERRORS=ERRORBUNDLE[1]
        os.chdir("data/")
        out_file = open(filename,"a")
        out_file.write(' \n')
        out_file.write('___STROOP_TRIAL_05\n')
        out_file.write('word_says= %s\n'%WORD)
        out_file.write('text_color_is= %s\n'%TEXTCOLOR)
        out_file.write('TrialTime_ms= %d NA NA NA NA 999\n'%TrialTime)
        out_file.write('with_this_many_premature_attempts_to_end= %d\n'%ERRORS)
        out_file.write('with_this_many_ERRORS= %d\n'%TRUEERRORS)
        out_file.write('motor_speed__time_between_last_selection_and_next_button_push_ms= %d\n'%(TrialTime-SelectionTime))
        TIME_END_TRIAL=strftime("%Y-%m-%d %H:%M:%S", localtime())
        out_file.write('timestamp_at_end_of_this_trial= %s\n'%TIME_END_TRIAL)
        out_file.write(' \n')
        out_file.close()
        STROOP_LOG[2][5]=TrialTime
        STROOP_LOG[1][5]=TRUEERRORS
        os.chdir(BASEPATH) 
        ScreenNumber=ScreenNumber+1
    while ScreenNumber == 47:
        SelectionTime=0
        TrialTime=-1  
        RESPONSE=0
        ERRORS=0
        WORD=stroopWORDorder[(ScreenNumber-42)]
        TEXTCOLOR=stroopWORDcolor[(ScreenNumber-42)]
        TRUEERRORS=0
        ## the stroop won't let you advance until you pick the correct answer, hence "ERRORS" and "TRUEERRORS"
        ## logged, but not "RESPONSE",since "REPSONSE" is always = TEXTCOLOR
        ERRORBUNDLE=[0,0]
        ScreenNumber, TrialTime, ERRORBUNDLE, RESET, WORD, TEXTCOLOR, SelectionTime = STROOPEVEN(ScreenNumber, TrialTime, ERRORBUNDLE, RESET, WORD, TEXTCOLOR, SelectionTime)
        ERRORS=ERRORBUNDLE[0]
        TRUEERRORS=ERRORBUNDLE[1]
        os.chdir("data/")
        out_file = open(filename,"a")
        out_file.write(' \n')
        out_file.write('___STROOP_TRIAL_06\n')
        out_file.write('word_says= %s\n'%WORD)
        out_file.write('text_color_is= %s\n'%TEXTCOLOR)
        out_file.write('TrialTime_ms= %d NA NA NA NA 999\n'%TrialTime)
        out_file.write('with_this_many_premature_attempts_to_end= %d\n'%ERRORS)
        out_file.write('with_this_many_ERRORS= %d\n'%TRUEERRORS)
        out_file.write('motor_speed__time_between_last_selection_and_next_button_push_ms= %d\n'%(TrialTime-SelectionTime))
        TIME_END_TRIAL=strftime("%Y-%m-%d %H:%M:%S", localtime())
        out_file.write('timestamp_at_end_of_this_trial= %s\n'%TIME_END_TRIAL)
        out_file.write(' \n')
        out_file.close()
        STROOP_LOG[2][6]=TrialTime
        STROOP_LOG[1][6]=TRUEERRORS
        os.chdir(BASEPATH) 
        ScreenNumber=ScreenNumber+1
    while ScreenNumber == 48:
        SelectionTime=0
        TrialTime=-1  
        RESPONSE=0
        ERRORS=0
        WORD=stroopWORDorder[(ScreenNumber-42)]
        TEXTCOLOR=stroopWORDcolor[(ScreenNumber-42)]
        TRUEERRORS=0
        ## the stroop won't let you advance until you pick the correct answer, hence "ERRORS" and "TRUEERRORS"
        ## logged, but not "RESPONSE",since "REPSONSE" is always = TEXTCOLOR
        ERRORBUNDLE=[0,0]
        ScreenNumber, TrialTime, ERRORBUNDLE, RESET, WORD, TEXTCOLOR, SelectionTime = STROOPODD(ScreenNumber, TrialTime, ERRORBUNDLE, RESET, WORD, TEXTCOLOR, SelectionTime)
        ERRORS=ERRORBUNDLE[0]
        TRUEERRORS=ERRORBUNDLE[1]
        os.chdir("data/")
        out_file = open(filename,"a")
        out_file.write(' \n')
        out_file.write('___STROOP_TRIAL_07\n')
        out_file.write('word_says= %s\n'%WORD)
        out_file.write('text_color_is= %s\n'%TEXTCOLOR)
        out_file.write('TrialTime_ms= %d NA NA NA NA 999\n'%TrialTime)
        out_file.write('with_this_many_premature_attempts_to_end= %d\n'%ERRORS)
        out_file.write('with_this_many_ERRORS= %d\n'%TRUEERRORS)
        out_file.write('motor_speed__time_between_last_selection_and_next_button_push_ms= %d\n'%(TrialTime-SelectionTime))
        TIME_END_TRIAL=strftime("%Y-%m-%d %H:%M:%S", localtime())
        out_file.write('timestamp_at_end_of_this_trial= %s\n'%TIME_END_TRIAL)
        out_file.write(' \n')
        out_file.close()
        os.chdir(BASEPATH)
        STROOP_LOG[2][7]=TrialTime
        STROOP_LOG[1][7]=TRUEERRORS
        ScreenNumber=ScreenNumber+1
    while ScreenNumber == 49:
        SelectionTime=0
        TrialTime=-1  
        RESPONSE=0
        ERRORS=0
        WORD=stroopWORDorder[(ScreenNumber-42)]
        TEXTCOLOR=stroopWORDcolor[(ScreenNumber-42)]
        TRUEERRORS=0
        ## the stroop won't let you advance until you pick the correct answer, hence "ERRORS" and "TRUEERRORS"
        ## logged, but not "RESPONSE",since "REPSONSE" is always = TEXTCOLOR
        ERRORBUNDLE=[0,0]
        ScreenNumber, TrialTime, ERRORBUNDLE, RESET, WORD, TEXTCOLOR, SelectionTime = STROOPEVEN(ScreenNumber, TrialTime, ERRORBUNDLE, RESET, WORD, TEXTCOLOR, SelectionTime)
        ERRORS=ERRORBUNDLE[0]
        TRUEERRORS=ERRORBUNDLE[1]
        os.chdir("data/")
        out_file = open(filename,"a")
        out_file.write(' \n')
        out_file.write('___STROOP_TRIAL_08\n')
        out_file.write('word_says= %s\n'%WORD)
        out_file.write('text_color_is= %s\n'%TEXTCOLOR)
        out_file.write('TrialTime_ms= %d NA NA NA NA 999\n'%TrialTime)
        out_file.write('with_this_many_premature_attempts_to_end= %d\n'%ERRORS)
        out_file.write('with_this_many_ERRORS= %d\n'%TRUEERRORS)
        out_file.write('motor_speed__time_between_last_selection_and_next_button_push_ms= %d\n'%(TrialTime-SelectionTime))
        TIME_END_TRIAL=strftime("%Y-%m-%d %H:%M:%S", localtime())
        out_file.write('timestamp_at_end_of_this_trial= %s\n'%TIME_END_TRIAL)
        out_file.write(' \n')
        out_file.close()
        os.chdir(BASEPATH)
        STROOP_LOG[2][8]=TrialTime
        STROOP_LOG[1][8]=TRUEERRORS
        ScreenNumber=ScreenNumber+1
    while ScreenNumber == 50:
        SelectionTime=0
        TrialTime=-1  
        RESPONSE=0
        ERRORS=0
        WORD=stroopWORDorder[(ScreenNumber-42)]
        TEXTCOLOR=stroopWORDcolor[(ScreenNumber-42)]
        TRUEERRORS=0
        ## the stroop won't let you advance until you pick the correct answer, hence "ERRORS" and "TRUEERRORS"
        ## logged, but not "RESPONSE",since "REPSONSE" is always = TEXTCOLOR
        ERRORBUNDLE=[0,0]
        ScreenNumber, TrialTime, ERRORBUNDLE, RESET, WORD, TEXTCOLOR, SelectionTime = STROOPODD(ScreenNumber, TrialTime, ERRORBUNDLE, RESET, WORD, TEXTCOLOR, SelectionTime)
        ERRORS=ERRORBUNDLE[0]
        TRUEERRORS=ERRORBUNDLE[1]
        os.chdir("data/")
        out_file = open(filename,"a")
        out_file.write(' \n')
        out_file.write('___STROOP_TRIAL_09\n')
        out_file.write('word_says= %s\n'%WORD)
        out_file.write('text_color_is= %s\n'%TEXTCOLOR)
        out_file.write('TrialTime_ms= %d NA NA NA NA 999\n'%TrialTime)
        out_file.write('with_this_many_premature_attempts_to_end= %d\n'%ERRORS)
        out_file.write('with_this_many_ERRORS= %d\n'%TRUEERRORS)
        out_file.write('motor_speed__time_between_last_selection_and_next_button_push_ms= %d\n'%(TrialTime-SelectionTime))
        TIME_END_TRIAL=strftime("%Y-%m-%d %H:%M:%S", localtime())
        out_file.write('timestamp_at_end_of_this_trial= %s\n'%TIME_END_TRIAL)
        out_file.write(' \n')
        out_file.close()
        os.chdir(BASEPATH)
        STROOP_LOG[2][9]=TrialTime
        STROOP_LOG[1][9]=TRUEERRORS
        ScreenNumber=ScreenNumber+1
    while ScreenNumber == 51:
        SelectionTime=0
        TrialTime=-1  
        RESPONSE=0
        ERRORS=0
        WORD=stroopWORDorder[(ScreenNumber-42)]
        TEXTCOLOR=stroopWORDcolor[(ScreenNumber-42)]
        TRUEERRORS=0
        ## the stroop won't let you advance until you pick the correct answer, hence "ERRORS" and "TRUEERRORS"
        ## logged, but not "RESPONSE",since "REPSONSE" is always = TEXTCOLOR
        ERRORBUNDLE=[0,0]
        ScreenNumber, TrialTime, ERRORBUNDLE, RESET, WORD, TEXTCOLOR, SelectionTime = STROOPEVEN(ScreenNumber, TrialTime, ERRORBUNDLE, RESET, WORD, TEXTCOLOR, SelectionTime)
        ERRORS=ERRORBUNDLE[0]
        TRUEERRORS=ERRORBUNDLE[1]
        os.chdir("data/")
        out_file = open(filename,"a")
        out_file.write(' \n')
        out_file.write('___STROOP_TRIAL_10\n')
        out_file.write('word_says= %s\n'%WORD)
        out_file.write('text_color_is= %s\n'%TEXTCOLOR)
        out_file.write('TrialTime_ms= %d NA NA NA NA 999\n'%TrialTime)
        out_file.write('with_this_many_premature_attempts_to_end= %d\n'%ERRORS)
        out_file.write('with_this_many_ERRORS= %d\n'%TRUEERRORS)
        out_file.write('motor_speed__time_between_last_selection_and_next_button_push_ms= %d\n'%(TrialTime-SelectionTime))
        TIME_END_TRIAL=strftime("%Y-%m-%d %H:%M:%S", localtime())
        out_file.write('timestamp_at_end_of_this_trial= %s\n'%TIME_END_TRIAL)
        out_file.write(' \n')
        out_file.close()
        os.chdir(BASEPATH)
        STROOP_LOG[2][10]=TrialTime
        STROOP_LOG[1][10]=TRUEERRORS
        ScreenNumber=ScreenNumber+1
    while ScreenNumber == 52:
        SelectionTime=0
        TrialTime=-1  
        RESPONSE=0
        ERRORS=0
        WORD=stroopWORDorder[(ScreenNumber-42)]
        TEXTCOLOR=stroopWORDcolor[(ScreenNumber-42)]
        TRUEERRORS=0
        ## the stroop won't let you advance until you pick the correct answer, hence "ERRORS" and "TRUEERRORS"
        ## logged, but not "RESPONSE",since "REPSONSE" is always = TEXTCOLOR
        ERRORBUNDLE=[0,0]
        ScreenNumber, TrialTime, ERRORBUNDLE, RESET, WORD, TEXTCOLOR, SelectionTime = STROOPODD(ScreenNumber, TrialTime, ERRORBUNDLE, RESET, WORD, TEXTCOLOR, SelectionTime)
        ERRORS=ERRORBUNDLE[0]
        TRUEERRORS=ERRORBUNDLE[1]
        os.chdir("data/")
        out_file = open(filename,"a")
        out_file.write(' \n')
        out_file.write('___STROOP_TRIAL_11\n')
        out_file.write('word_says= %s\n'%WORD)
        out_file.write('text_color_is= %s\n'%TEXTCOLOR)
        out_file.write('TrialTime_ms= %d NA NA NA NA 999\n'%TrialTime)
        out_file.write('with_this_many_premature_attempts_to_end= %d\n'%ERRORS)
        out_file.write('with_this_many_ERRORS= %d\n'%TRUEERRORS)
        out_file.write('motor_speed__time_between_last_selection_and_next_button_push_ms= %d\n'%(TrialTime-SelectionTime))
        TIME_END_TRIAL=strftime("%Y-%m-%d %H:%M:%S", localtime())
        out_file.write('timestamp_at_end_of_this_trial= %s\n'%TIME_END_TRIAL)
        out_file.write(' \n')
        out_file.close()
        os.chdir(BASEPATH)
        STROOP_LOG[2][11]=TrialTime
        STROOP_LOG[1][11]=TRUEERRORS
        ScreenNumber=ScreenNumber+1
    while ScreenNumber == 53:
        SelectionTime=0
        TrialTime=-1  
        RESPONSE=0
        ERRORS=0
        WORD=stroopWORDorder[(ScreenNumber-42)]
        TEXTCOLOR=stroopWORDcolor[(ScreenNumber-42)]
        TRUEERRORS=0
        ## the stroop won't let you advance until you pick the correct answer, hence "ERRORS" and "TRUEERRORS"
        ## logged, but not "RESPONSE",since "REPSONSE" is always = TEXTCOLOR
        ERRORBUNDLE=[0,0]
        ScreenNumber, TrialTime, ERRORBUNDLE, RESET, WORD, TEXTCOLOR, SelectionTime = STROOPEVEN(ScreenNumber, TrialTime, ERRORBUNDLE, RESET, WORD, TEXTCOLOR, SelectionTime)
        ERRORS=ERRORBUNDLE[0]
        TRUEERRORS=ERRORBUNDLE[1]
        os.chdir("data/")
        out_file = open(filename,"a")
        out_file.write(' \n')
        out_file.write('___STROOP_TRIAL_12\n')
        out_file.write('word_says= %s\n'%WORD)
        out_file.write('text_color_is= %s\n'%TEXTCOLOR)
        out_file.write('TrialTime_ms= %d NA NA NA NA 999\n'%TrialTime)
        out_file.write('with_this_many_premature_attempts_to_end= %d\n'%ERRORS)
        out_file.write('with_this_many_ERRORS= %d\n'%TRUEERRORS)
        out_file.write('motor_speed__time_between_last_selection_and_next_button_push_ms= %d\n'%(TrialTime-SelectionTime))
        TIME_END_TRIAL=strftime("%Y-%m-%d %H:%M:%S", localtime())
        out_file.write('timestamp_at_end_of_this_trial= %s\n'%TIME_END_TRIAL)
        out_file.write(' \n')
        out_file.close()
        os.chdir(BASEPATH)
        STROOP_LOG[2][12]=TrialTime
        STROOP_LOG[1][12]=TRUEERRORS
        ScreenNumber=ScreenNumber+1
    while ScreenNumber == 54:
        SelectionTime=0
        TrialTime=-1  
        RESPONSE=0
        ERRORS=0
        WORD=stroopWORDorder[(ScreenNumber-42)]
        TEXTCOLOR=stroopWORDcolor[(ScreenNumber-42)]
        TRUEERRORS=0
        ## the stroop won't let you advance until you pick the correct answer, hence "ERRORS" and "TRUEERRORS"
        ## logged, but not "RESPONSE",since "REPSONSE" is always = TEXTCOLOR
        ERRORBUNDLE=[0,0]
        ScreenNumber, TrialTime, ERRORBUNDLE, RESET, WORD, TEXTCOLOR, SelectionTime = STROOPODD(ScreenNumber, TrialTime, ERRORBUNDLE, RESET, WORD, TEXTCOLOR, SelectionTime)
        ERRORS=ERRORBUNDLE[0]
        TRUEERRORS=ERRORBUNDLE[1]
        os.chdir("data/")
        out_file = open(filename,"a")
        out_file.write(' \n')
        out_file.write('___STROOP_TRIAL_13\n')
        out_file.write('word_says= %s\n'%WORD)
        out_file.write('text_color_is= %s\n'%TEXTCOLOR)
        out_file.write('TrialTime_ms= %d NA NA NA NA 999\n'%TrialTime)
        out_file.write('with_this_many_premature_attempts_to_end= %d\n'%ERRORS)
        out_file.write('with_this_many_ERRORS= %d\n'%TRUEERRORS)
        out_file.write('motor_speed__time_between_last_selection_and_next_button_push_ms= %d\n'%(TrialTime-SelectionTime))
        TIME_END_TRIAL=strftime("%Y-%m-%d %H:%M:%S", localtime())
        out_file.write('timestamp_at_end_of_this_trial= %s\n'%TIME_END_TRIAL)
        out_file.write(' \n')
        out_file.close()
        os.chdir(BASEPATH)
        STROOP_LOG[2][13]=TrialTime
        STROOP_LOG[1][13]=TRUEERRORS
        ScreenNumber=ScreenNumber+1
    while ScreenNumber == 55:
        SelectionTime=0
        TrialTime=-1  
        RESPONSE=0
        ERRORS=0
        WORD=stroopWORDorder[(ScreenNumber-42)]
        TEXTCOLOR=stroopWORDcolor[(ScreenNumber-42)]
        TRUEERRORS=0
        ## the stroop won't let you advance until you pick the correct answer, hence "ERRORS" and "TRUEERRORS"
        ## logged, but not "RESPONSE",since "REPSONSE" is always = TEXTCOLOR
        ERRORBUNDLE=[0,0]
        ScreenNumber, TrialTime, ERRORBUNDLE, RESET, WORD, TEXTCOLOR, SelectionTime = STROOPEVEN(ScreenNumber, TrialTime, ERRORBUNDLE, RESET, WORD, TEXTCOLOR, SelectionTime)
        ERRORS=ERRORBUNDLE[0]
        TRUEERRORS=ERRORBUNDLE[1]
        os.chdir("data/")
        out_file = open(filename,"a")
        out_file.write(' \n')
        out_file.write('___STROOP_TRIAL_14\n')
        out_file.write('word_says= %s\n'%WORD)
        out_file.write('text_color_is= %s\n'%TEXTCOLOR)
        out_file.write('TrialTime_ms= %d NA NA NA NA 999\n'%TrialTime)
        out_file.write('with_this_many_premature_attempts_to_end= %d\n'%ERRORS)
        out_file.write('with_this_many_ERRORS= %d\n'%TRUEERRORS)
        out_file.write('motor_speed__time_between_last_selection_and_next_button_push_ms= %d\n'%(TrialTime-SelectionTime))
        TIME_END_TRIAL=strftime("%Y-%m-%d %H:%M:%S", localtime())
        out_file.write('timestamp_at_end_of_this_trial= %s\n'%TIME_END_TRIAL)
        out_file.write(' \n')
        out_file.close()
        os.chdir(BASEPATH)
        STROOP_LOG[2][14]=TrialTime
        STROOP_LOG[1][14]=TRUEERRORS
        ScreenNumber=ScreenNumber+1
    while ScreenNumber == 56:
        SelectionTime=0
        TrialTime=-1  
        RESPONSE=0
        ERRORS=0
        WORD=stroopWORDorder[(ScreenNumber-42)]
        TEXTCOLOR=stroopWORDcolor[(ScreenNumber-42)]
        TRUEERRORS=0
        ## the stroop won't let you advance until you pick the correct answer, hence "ERRORS" and "TRUEERRORS"
        ## logged, but not "RESPONSE",since "REPSONSE" is always = TEXTCOLOR
        ERRORBUNDLE=[0,0]
        ScreenNumber, TrialTime, ERRORBUNDLE, RESET, WORD, TEXTCOLOR, SelectionTime = STROOPODD(ScreenNumber, TrialTime, ERRORBUNDLE, RESET, WORD, TEXTCOLOR, SelectionTime)
        ERRORS=ERRORBUNDLE[0]
        TRUEERRORS=ERRORBUNDLE[1]
        os.chdir("data/")
        out_file = open(filename,"a")
        out_file.write(' \n')
        out_file.write('___STROOP_TRIAL_15\n')
        out_file.write('word_says= %s\n'%WORD)
        out_file.write('text_color_is= %s\n'%TEXTCOLOR)
        out_file.write('TrialTime_ms= %d NA NA NA NA 999\n'%TrialTime)
        out_file.write('with_this_many_premature_attempts_to_end= %d\n'%ERRORS)
        out_file.write('with_this_many_ERRORS= %d\n'%TRUEERRORS)
        out_file.write('motor_speed__time_between_last_selection_and_next_button_push_ms= %d\n'%(TrialTime-SelectionTime))
        TIME_END_TRIAL=strftime("%Y-%m-%d %H:%M:%S", localtime())
        out_file.write('timestamp_at_end_of_this_trial= %s\n'%TIME_END_TRIAL)
        out_file.write(' \n')
        out_file.close()
        os.chdir(BASEPATH)
        STROOP_LOG[2][15]=TrialTime
        STROOP_LOG[1][15]=TRUEERRORS
        ScreenNumber=ScreenNumber+1

    ## write most results in simple form [we'll do as much as we can before the actual trails tasks; as this in when someone might quit early]
    os.chdir("data/")
    filename_simple_full = "%s_%d_simple_full.txt"%(strftime("%Y-%m-%d", localtime()), subject_number)
    out_file = open(filename_simple_full,"w")
    out_file.write('subject= %d\n'%subject_number)
    out_file.write('date= %s\n'%(strftime("%Y_%m_%d", localtime())))
    out_file.write('___________________________________________\n')
    out_file.write('CATEGORY %s %s %s TOTAL_ERRORS\n'%(ATTENTION_LOG[0][0], ATTENTION_LOG[1][0], ATTENTION_LOG[2][0]))
    out_file.write('ATTENTION %s %s %s NA\n'%(ATTENTION_LOG[0][1], ATTENTION_LOG[1][1], ATTENTION_LOG[2][1]))
    out_file.write('ATTENTION %s %s %s NA\n'%(ATTENTION_LOG[0][2], ATTENTION_LOG[1][2], ATTENTION_LOG[2][2]))
    out_file.write('ATTENTION %s %s %s NA\n'%(ATTENTION_LOG[0][3], ATTENTION_LOG[1][3], ATTENTION_LOG[2][3]))
    out_file.write('SPATIAL %s %s %s NA\n'%(SPATIAL_LOG[0][1], SPATIAL_LOG[1][1], SPATIAL_LOG[2][1]))
    out_file.write('SPATIAL %s %s %s NA\n'%(SPATIAL_LOG[0][2], SPATIAL_LOG[1][2], SPATIAL_LOG[2][2]))
    out_file.write('SPATIAL %s %s %s NA\n'%(SPATIAL_LOG[0][3], SPATIAL_LOG[1][3], SPATIAL_LOG[2][3]))
    out_file.write('SPATIAL %s %s %s NA\n'%(SPATIAL_LOG[0][4], SPATIAL_LOG[1][4], SPATIAL_LOG[2][4]))
    out_file.write('ORIENTATION %s %s %s NA\n'%(ORIENTATION_LOG[0][1], ORIENTATION_LOG[1][1], ORIENTATION_LOG[2][1]))
    out_file.write('ORIENTATION %s %s %s NA\n'%(ORIENTATION_LOG[0][2], ORIENTATION_LOG[1][2], ORIENTATION_LOG[2][2]))
    out_file.write('ORIENTATION %s %s %s NA\n'%(ORIENTATION_LOG[0][3], ORIENTATION_LOG[1][3], ORIENTATION_LOG[2][3]))
    out_file.write('ORIENTATION %s %s %s NA\n'%(ORIENTATION_LOG[0][4], ORIENTATION_LOG[1][4], ORIENTATION_LOG[2][4]))
    out_file.write('MEMORY %s %s %s NA\n'%(MEMORY_LOG[0][1], MEMORY_LOG[1][1], MEMORY_LOG[2][1]))
    out_file.write('MEMORY %s %s %s NA\n'%(MEMORY_LOG[0][2], MEMORY_LOG[1][2], MEMORY_LOG[2][2]))
    out_file.write('MEMORY %s %s %s NA\n'%(MEMORY_LOG[0][3], MEMORY_LOG[1][3], MEMORY_LOG[2][3]))
    out_file.write('MEMORY %s %s %s NA\n'%(MEMORY_LOG[0][4], MEMORY_LOG[1][4], MEMORY_LOG[2][4]))
    out_file.write('MATH %s %s %s NA\n'%(MATH_LOG[0][1], MATH_LOG[1][1], MATH_LOG[2][1]))
    out_file.write('MATH %s %s %s NA\n'%(MATH_LOG[0][2], MATH_LOG[1][2], MATH_LOG[2][2]))
    ## a little loop for stroop... basically, find the sum total of true errors
    ## for the 12 "real" trials.
    ##
    ## also find the sum total time spent on those trials (up to twelve)(divided by number of completed trials)
    STROOP_SUM_OF_ERRORS=0
    STROOP_SUM_OF_TIME=0
    STROOP_NUMBER_ANSWERED=0
    for x in range(4,16):
         if STROOP_LOG[1][x] != "NA":
             STROOP_SUM_OF_ERRORS=STROOP_SUM_OF_ERRORS+STROOP_LOG[1][x]
             STROOP_SUM_OF_TIME=STROOP_SUM_OF_TIME+STROOP_LOG[2][x]
             STROOP_NUMBER_ANSWERED=STROOP_NUMBER_ANSWERED+1
    ## if no data, NA out the veriables
    if STROOP_SUM_OF_TIME == 0:
        STROOP_SUM_OF_TIME="NA"
        STROOP_SUM_OF_ERRORS="NA"
    ## try to accomodate missing trials (whatever you didn't complete counts against you). 
    if STROOP_SUM_OF_ERRORS != "NA":
        STROOP_SUM_OF_ERRORS=STROOP_SUM_OF_ERRORS+(12-STROOP_NUMBER_ANSWERED)
    if STROOP_SUM_OF_ERRORS==0:
        out_file.write('STROOP SUM %s %s %s\n'%(3, STROOP_SUM_OF_TIME/STROOP_NUMBER_ANSWERED, STROOP_SUM_OF_ERRORS))
    elif STROOP_SUM_OF_ERRORS==1:
        out_file.write('STROOP SUM %s %s %s\n'%(2, STROOP_SUM_OF_TIME/STROOP_NUMBER_ANSWERED, STROOP_SUM_OF_ERRORS))
    elif STROOP_SUM_OF_ERRORS==2:
        out_file.write('STROOP SUM %s %s %s\n'%(1, STROOP_SUM_OF_TIME/STROOP_NUMBER_ANSWERED, STROOP_SUM_OF_ERRORS))
    else:
        if STROOP_LOG[1][x] != "NA":
            out_file.write('STROOP SUM %s %s %s\n'%(0, STROOP_SUM_OF_TIME/STROOP_NUMBER_ANSWERED, STROOP_SUM_OF_ERRORS))
        else:
            out_file.write('STROOP SUM NA NA NA\n')
            
    out_file.close()
    os.chdir(BASEPATH)

    ## time limit skips to the end if 15 mins (900000 ms) have now passed.
    if VERY_BEGINNING_NUMERIC != "NA":
        LATEST_TIME_NUMERIC=int(round(time() * 1000))
        TIME_SPENT_MS=int(round(LATEST_TIME_NUMERIC-VERY_BEGINNING_NUMERIC,0))
        if TIME_SPENT_MS > 900000:
            final_screen()
            ScreenNumber=9997
    
    while ScreenNumber == 57:   ### INSTRUCTION SCREEN "ODD" for moved hitbox
        WordCount=11 ##<- "CONNECT-THE-DOTS" IS COUNTED AS ONE WORD [as microsoft word will do] even though ellipses aren't really words...
        BACKGROUNDIMAGE=instructbackgrounds[8]
        InstructionTime=-1
        ScreenNumber, BACKGROUNDIMAGE, InstructionTime, RESET = INSTRUCTIONscreenODD(ScreenNumber, BACKGROUNDIMAGE, InstructionTime, RESET)
        os.chdir("data/")
        out_file = open(filename,"a")
        out_file.write('dots_instruction_almost_done\n')
        out_file.write('wordcount= %d\n'%WordCount)
        out_file.write('InstructionTime_ms= %d\n'%InstructionTime)
        #out_file.write('words_per_s= %d\n'%(int((float(WordCount)/(float(InstructionTime)/1000))*100)/100.0))
        #out_file.write('words_per_s= %d\n'%(int((float(WordCount)/(float(InstructionTime)/1000))*100)/100.0))
        out_file.write('words_per_s= %f NA NA NA NA 1\n'%round((float(WordCount)/(float(InstructionTime)/1000)), 3))
        TIME_END_TRIAL=strftime("%Y-%m-%d %H:%M:%S", localtime())
        READING_SPEED_LOG.append(round((float(WordCount)/(float(InstructionTime)/1000)), 3))
        out_file.write('timestamp_at_end_of_this_instruction_screen= %s\n'%TIME_END_TRIAL)
        out_file.write(' \n')
        out_file.close()
        os.chdir(BASEPATH) 
        ScreenNumber=ScreenNumber+1

    while ScreenNumber == 58:   ### INSTRUCTION SCREEN
        WordCount=22 ##<- the nubers or letters in the paranthetical are not counted as words.
        BACKGROUNDIMAGE=instructbackgrounds[9]
        InstructionTime=-1
        ScreenNumber, BACKGROUNDIMAGE, InstructionTime, RESET = INSTRUCTIONscreen(ScreenNumber, BACKGROUNDIMAGE, InstructionTime, RESET)
        os.chdir("data/")
        out_file = open(filename,"a")
        out_file.write('dots_instruction_numbered_dots_go_1_2_3\n')
        out_file.write('wordcount= %d\n'%WordCount)
        out_file.write('InstructionTime_ms= %d\n'%InstructionTime)
        #out_file.write('words_per_s= %d\n'%(int((float(WordCount)/(float(InstructionTime)/1000))*100)/100.0))
        #out_file.write('words_per_s= %d\n'%(int((float(WordCount)/(float(InstructionTime)/1000))*100)/100.0))
        out_file.write('words_per_s= %f NA NA NA NA 1\n'%round((float(WordCount)/(float(InstructionTime)/1000)), 3))
        TIME_END_TRIAL=strftime("%Y-%m-%d %H:%M:%S", localtime())
        READING_SPEED_LOG.append(round((float(WordCount)/(float(InstructionTime)/1000)), 3))
        out_file.write('timestamp_at_end_of_this_instruction_screen= %s\n'%TIME_END_TRIAL)
        out_file.write(' \n')
        out_file.close()
        os.chdir(BASEPATH) 
        ScreenNumber=ScreenNumber+1    

    while ScreenNumber == 59:   ### INSTRUCTION SCREEN "ODD" for moved hitbox
        WordCount=25 ##<- here, elipses counted as words, [as microsoft word will do] even though ellipses aren't really words...
                     ##    but the "dots" with numbers in them are objects, not words, so those are ignored in this count
        BACKGROUNDIMAGE=instructbackgrounds[10]
        InstructionTime=-1
        ScreenNumber, BACKGROUNDIMAGE, InstructionTime, RESET = INSTRUCTIONscreenODD(ScreenNumber, BACKGROUNDIMAGE, InstructionTime, RESET)
        os.chdir("data/")
        out_file = open(filename,"a")
        out_file.write('dots_instruction_dots_look_like_this\n')
        out_file.write('wordcount= %d\n'%WordCount)
        out_file.write('InstructionTime_ms= %d\n'%InstructionTime)
        #out_file.write('words_per_s= %d\n'%(int((float(WordCount)/(float(InstructionTime)/1000))*100)/100.0))
        #out_file.write('words_per_s= %d\n'%(int((float(WordCount)/(float(InstructionTime)/1000))*100)/100.0))
        out_file.write('words_per_s= %f NA NA NA NA 1\n'%round((float(WordCount)/(float(InstructionTime)/1000)), 3))
        TIME_END_TRIAL=strftime("%Y-%m-%d %H:%M:%S", localtime())
        READING_SPEED_LOG.append(round((float(WordCount)/(float(InstructionTime)/1000)), 3))
        out_file.write('timestamp_at_end_of_this_instruction_screen= %s\n'%TIME_END_TRIAL)
        out_file.write(' \n')
        out_file.close()
        os.chdir(BASEPATH) 
        ScreenNumber=ScreenNumber+1
        
    BUTTON=0
    ERRORS=0
    TrialTime=-1
    ATTEMPTS_TO_END_EARLY=0
    while ScreenNumber == 60:  ## TRAILS A
        os.chdir("data/")
        out_file = open(filename,"a")
        out_file.write('_______________________\n') 
        out_file.write('Trails_A___running_log\n')
        out_file.write('_______________________\n')  ## we will enter the loop while writing the log file. We can enter each button press. Maybe "time between buttons" is important.
        ScreenNumber, TrialTime, ERRORS, ATTEMPTS_TO_END_EARLY = TRAILSa(ScreenNumber, TrialTime, ERRORS, ATTEMPTS_TO_END_EARLY)
        out_file.write('__________________\n') 
        out_file.write('Trails_A___summary\n')
        out_file.write('___________________\n')
        out_file.write('total_time_spent_ms= %d\n'%TrialTime)
        out_file.write('number_of_trail_errors_(not_counting_attempts_to_end_early)= %d\n'%ERRORS)
        TRAILS_LOG[2][1]=TrialTime
        if ERRORS == 0:
            TRAILS_LOG[1][1]=1
        elif ERRORS > 0:
            TRAILS_LOG[1][1]=0
        out_file.write('number_of_attempts_to_end_early= %d\n'%ATTEMPTS_TO_END_EARLY)
        TIME_END_TRIAL=strftime("%Y-%m-%d %H:%M:%S", localtime())
        out_file.write('timestamp_at_end_of_this_trial= %s\n'%TIME_END_TRIAL)
        out_file.write(' \n')
        out_file.close()
        ## add to the summary sheet!
        out_file = open(filename_simple_full,"a")
        out_file.write('TRAILS %s %s %s %d\n'%(TRAILS_LOG[0][1], TRAILS_LOG[1][1], TRAILS_LOG[2][1], ERRORS))
        out_file.close()
        os.chdir(BASEPATH)
        ScreenNumber=ScreenNumber+1

    ## time limit skips to the end if 15 mins (900000 ms) have now passed.
    if VERY_BEGINNING_NUMERIC != "NA":
        LATEST_TIME_NUMERIC=int(round(time() * 1000))
        TIME_SPENT_MS=int(round(LATEST_TIME_NUMERIC-VERY_BEGINNING_NUMERIC,0))
        if TIME_SPENT_MS > 900000:
            final_screen()
            ScreenNumber=9997

    BUTTON=0
    ERRORS=0
    TrialTime=-1
    ATTEMPTS_TO_END_EARLY=0
    while ScreenNumber == 61:  ## TRAILS B small/mini/"sample"
        os.chdir("data/")
        out_file = open(filename,"a")
        out_file.write('_______________________\n') 
        out_file.write('Trails_Bsmall___running_log\n')
        out_file.write('_______________________\n')  ## we will enter the loop while writing the log file. We can enter each button press. Maybe "time between buttons" is important.
        ScreenNumber, TrialTime, ERRORS, ATTEMPTS_TO_END_EARLY = TRAILSbSAMPLE(ScreenNumber, TrialTime, ERRORS, ATTEMPTS_TO_END_EARLY) 
        out_file.write('__________________\n') 
        out_file.write('Trails_Bsmall___summary\n')
        out_file.write('___________________\n')
        out_file.write('total_time_spent_ms= %d\n'%TrialTime)
        out_file.write('number_of_trail_errors_(not_counting_attempts_to_end_early)= %d\n'%ERRORS)
        TRAILS_LOG[2][2]=TrialTime
        if ERRORS == 0:
            TRAILS_LOG[1][2]=1
        elif ERRORS > 0:
            TRAILS_LOG[1][2]=0
        out_file.write('number_of_attempts_to_end_early= %d\n'%ATTEMPTS_TO_END_EARLY)
        TIME_END_TRIAL=strftime("%Y-%m-%d %H:%M:%S", localtime())
        out_file.write('timestamp_at_end_of_this_trial= %s\n'%TIME_END_TRIAL)
        out_file.write(' \n')
        out_file.close()
        ## add to the summary sheet!
        out_file = open(filename_simple_full,"a")
        out_file.write('TRAILS %s %s %s %d\n'%(TRAILS_LOG[0][2], TRAILS_LOG[1][2], TRAILS_LOG[2][2], ERRORS))
        out_file.close()
        ##
        os.chdir(BASEPATH)
        final_screen()
        ScreenNumber=9997

    VERY_END=strftime("%Y-%m-%d %H:%M:%S", localtime())
    VERY_END_NUMERIC=int(round(time() * 1000))
    os.chdir("data/")
    out_file = open(filename_simple_full,"a")
    ## figure out the sum total of points earned:
    SUM_TOTAL_POINTS=0
    if ATTENTION_LOG[1][1] != "NA":
        SUM_TOTAL_POINTS=SUM_TOTAL_POINTS+ATTENTION_LOG[1][1]
    if ATTENTION_LOG[1][2] != "NA":
        SUM_TOTAL_POINTS=SUM_TOTAL_POINTS+ATTENTION_LOG[1][2]
    if ATTENTION_LOG[1][3] != "NA":
        SUM_TOTAL_POINTS=SUM_TOTAL_POINTS+ATTENTION_LOG[1][3]
    if SPATIAL_LOG[1][1] != "NA":
        SUM_TOTAL_POINTS=SUM_TOTAL_POINTS+SPATIAL_LOG[1][1]
    if SPATIAL_LOG[1][2] != "NA":
        SUM_TOTAL_POINTS=SUM_TOTAL_POINTS+SPATIAL_LOG[1][2]
    if SPATIAL_LOG[1][3] != "NA":
        SUM_TOTAL_POINTS=SUM_TOTAL_POINTS+SPATIAL_LOG[1][3]
    if SPATIAL_LOG[1][4] != "NA":
        SUM_TOTAL_POINTS=SUM_TOTAL_POINTS+SPATIAL_LOG[1][4]
    if ORIENTATION_LOG[1][1] != "NA":
        SUM_TOTAL_POINTS=SUM_TOTAL_POINTS+ORIENTATION_LOG[1][1]
    if ORIENTATION_LOG[1][2] != "NA":
        SUM_TOTAL_POINTS=SUM_TOTAL_POINTS+ORIENTATION_LOG[1][2]
    if ORIENTATION_LOG[1][3] != "NA":
        SUM_TOTAL_POINTS=SUM_TOTAL_POINTS+ORIENTATION_LOG[1][3]
    if ORIENTATION_LOG[1][4] != "NA":
        SUM_TOTAL_POINTS=SUM_TOTAL_POINTS+ORIENTATION_LOG[1][4]
    if MEMORY_LOG[1][1] != "NA":
        SUM_TOTAL_POINTS=SUM_TOTAL_POINTS+MEMORY_LOG[1][1]
    if MEMORY_LOG[1][2] != "NA":
        SUM_TOTAL_POINTS=SUM_TOTAL_POINTS+MEMORY_LOG[1][2]
    if MEMORY_LOG[1][3] != "NA":
        SUM_TOTAL_POINTS=SUM_TOTAL_POINTS+MEMORY_LOG[1][3]
    if MEMORY_LOG[1][4] != "NA":
        SUM_TOTAL_POINTS=SUM_TOTAL_POINTS+MEMORY_LOG[1][4]
    if MATH_LOG[1][1] != "NA":
        SUM_TOTAL_POINTS=SUM_TOTAL_POINTS+MATH_LOG[1][1]
    if MATH_LOG[1][2] != "NA":
        SUM_TOTAL_POINTS=SUM_TOTAL_POINTS+MATH_LOG[1][2]
    if STROOP_SUM_OF_ERRORS==0:
        SUM_TOTAL_POINTS=SUM_TOTAL_POINTS+3
    elif STROOP_SUM_OF_ERRORS==1:
        SUM_TOTAL_POINTS=SUM_TOTAL_POINTS+2
    elif STROOP_SUM_OF_ERRORS==2:
        SUM_TOTAL_POINTS=SUM_TOTAL_POINTS+1
    ## unwritten: if > 2 errors on stroop, SUM_TOTAL=SUM+TOTAL+0
    if TRAILS_LOG[1][1] != "NA":
        SUM_TOTAL_POINTS=SUM_TOTAL_POINTS+TRAILS_LOG[1][1]
    if TRAILS_LOG[1][2] != "NA":
        SUM_TOTAL_POINTS=SUM_TOTAL_POINTS+TRAILS_LOG[1][2]
    ## calculate time spent in ms
    if VERY_BEGINNING_NUMERIC != "NA":
        SUM_TIME_SPENT_MS=int(round(VERY_END_NUMERIC-VERY_BEGINNING_NUMERIC,0))
    ## and write it
    if SUM_TIME_SPENT_MS != "NA":
        out_file.write('TOTAL NA %s %d NA\n'%(SUM_TOTAL_POINTS, SUM_TIME_SPENT_MS))
    ## also log reading speed
    ## we want the median
    MEDIAN_READING_SPEED=0
    n = len(READING_SPEED_LOG)-1
    if n > 1:
        t = sorted(READING_SPEED_LOG)
        s = t[0:(len(t)-1)]
        MEDIAN_READING_SPEED=(sum(s[n//2-1:n//2+1])/2.0, s[n//2])[n % 2]
    out_file.write('READING WORDS_PER_S NA %s NA\n'%(MEDIAN_READING_SPEED))
    ## also log motor speed
    ## we want the median
    MEDIAN_MOTOR_SPEED=0
    n = len(MOTOR_SPEED_LOG)-1
    if n > 1:
        t = sorted(MOTOR_SPEED_LOG)
        s = t[0:(len(t)-1)]
        MEDIAN_MOTOR_SPEED=(sum(s[n//2-1:n//2+1])/2.0, s[n//2])[n % 2]
    out_file.write('MOTOR MS_PER_BUTTON NA %s NA\n'%(MEDIAN_MOTOR_SPEED))
    ##
    out_file.write('___________________________________________\n')
    out_file.write('___________________________________________\n')
    out_file.write('timestamp_at_experiment_start= %s\n'%VERY_BEGINNING)
    out_file.write('timestamp_at_experiment_end= %s\n'%VERY_END)
    out_file.write('___________________________________________\n')
    out_file.write('___________________________________________\n')
    out_file.write('%s %s %s \n'%(STROOP_LOG[0][0], STROOP_LOG[1][0], STROOP_LOG[2][0]))
    out_file.write('%s %s %s \n'%(STROOP_LOG[0][1], STROOP_LOG[1][1], STROOP_LOG[2][1]))
    out_file.write('%s %s %s \n'%(STROOP_LOG[0][2], STROOP_LOG[1][2], STROOP_LOG[2][2]))
    out_file.write('%s %s %s \n'%(STROOP_LOG[0][3], STROOP_LOG[1][3], STROOP_LOG[2][3]))
    out_file.write('%s %s %s \n'%(STROOP_LOG[0][4], STROOP_LOG[1][4], STROOP_LOG[2][4]))
    out_file.write('%s %s %s \n'%(STROOP_LOG[0][5], STROOP_LOG[1][5], STROOP_LOG[2][5]))
    out_file.write('%s %s %s \n'%(STROOP_LOG[0][6], STROOP_LOG[1][6], STROOP_LOG[2][6]))
    out_file.write('%s %s %s \n'%(STROOP_LOG[0][7], STROOP_LOG[1][7], STROOP_LOG[2][7]))
    out_file.write('%s %s %s \n'%(STROOP_LOG[0][8], STROOP_LOG[1][8], STROOP_LOG[2][8]))
    out_file.write('%s %s %s \n'%(STROOP_LOG[0][9], STROOP_LOG[1][9], STROOP_LOG[2][9]))
    out_file.write('%s %s %s \n'%(STROOP_LOG[0][10], STROOP_LOG[1][10], STROOP_LOG[2][10]))
    out_file.write('%s %s %s \n'%(STROOP_LOG[0][11], STROOP_LOG[1][11], STROOP_LOG[2][11]))
    out_file.write('%s %s %s \n'%(STROOP_LOG[0][12], STROOP_LOG[1][12], STROOP_LOG[2][12]))
    out_file.write('%s %s %s \n'%(STROOP_LOG[0][13], STROOP_LOG[1][13], STROOP_LOG[2][13]))
    out_file.write('%s %s %s \n'%(STROOP_LOG[0][14], STROOP_LOG[1][14], STROOP_LOG[2][14]))
    out_file.write('%s %s %s \n'%(STROOP_LOG[0][15], STROOP_LOG[1][15], STROOP_LOG[2][15]))
    out_file.write('_________________________________________________\n')
    out_file.write('_BELOW_HERE_READ_SPEEDS_to_calculate_IQR_if_desired__\n')
    out_file.write('_________________________________________________\n')
    for i in xrange(1,len(READING_SPEED_LOG)):
        out_file.write('%s\n'%(READING_SPEED_LOG[i]))
    out_file.write('_________________________________________________\n')
    out_file.write('___BELOW_HERE_MOTOR_SPEEDS_to_calculate_IQR_if_desired___\n')
    out_file.write('_________________________________________________\n')
    for i in xrange(1,len(MOTOR_SPEED_LOG)):
        out_file.write('%s\n'%(MOTOR_SPEED_LOG[i]))
    out_file.close()
    ## I'll need to make a data summary page
    ## ...it won't actually be shown to the subject...
    ##
    #### <summary image>
    ##  REVIEW_SCREEN
    ## info for this:
    ##
    ## <update for APR-2020>
    ##  linear fit based on 79 participants phases 1 through 3 of development
    ##
    ##
    #tablet  est     |-50%CI for MoCA-|
    #score   MoCA
    #         fit       lwr      upr
    # 0  5.663542  3.556069  7.771014
    # 1  6.450000  4.426942  8.473058
    # 2  7.236458  5.297564  9.175353
    # 3  8.022917  6.167900  9.877934
    # 4  8.809375  7.037910 10.580840
    # 5  9.595833  7.907545 11.284122
    # 6 10.382292  8.776748 11.987835
    # 7 11.168750  9.645448 12.692052
    # 8 11.955208 10.513558 13.396859
    # 9 12.741667 11.380973 14.102361
    #10 13.528125 12.247560 14.808690
    #11 14.314583 13.113155 15.516012
    #12 15.101042 13.977547 16.224536
    #13 15.887500 14.840468 16.934532
    #14 16.673958 15.701571 17.646346
    #15 17.460417 16.560402 18.360431
    #16 18.246875 17.416369 19.077381
    #17 19.033333 18.268689 19.797977
    #18 19.819792 19.116338 20.523245
    #19 20.606250 19.957992 21.254508
    #20 21.392708 20.791994 21.993422
    #21 22.179167 21.616404 22.741929
    #22 22.965625 22.429181 23.502069
    #23 23.752083 23.228567 24.275599
    #24 24.538542 24.013574 25.063510
    #25 25.325000 24.784315 25.865685
    #26 26.111458 25.541972 26.680945
    #27 26.897917 26.288396 27.507438
    #28 27.684375 27.025632 28.343118
    #29 28.470833 27.755574 29.186092
    #30 29.257292 28.479812 30.034771
    #
    # the mean of non-demented (n=38) was 27.1, sd=2.51
    # the mean of MCI (CDR 0.5; n=10) was 21.3, sd=5.1
    # the mean of demented (CDR >= 1.0; n=12) was 13.7, sd 5.1
    # leading to the following z scores:
    ##tablet
    #score|Normal | MCI  |   DEMENTED
    # 0 -10.84 -4.17647059 -2.68627451
    # 1 -10.44 -3.98039216 -2.49019608
    # 2 -10.04 -3.78431373 -2.29411765
    # 3  -9.64 -3.58823529 -2.09803922
    # 4  -9.24 -3.39215686 -1.90196078
    # 5  -8.84 -3.19607843 -1.70588235
    # 6  -8.44 -3.00000000 -1.50980392
    # 7  -8.04 -2.80392157 -1.31372549
    # 8  -7.64 -2.60784314 -1.11764706
    # 9  -7.24 -2.41176471 -0.92156863
    #10  -6.84 -2.21568627 -0.72549020
    #11  -6.44 -2.01960784 -0.52941176
    #12  -6.04 -1.82352941 -0.33333333
    #13  -5.64 -1.62745098 -0.13725490
    #14  -5.24 -1.43137255  0.05882353
    #15  -4.84 -1.23529412  0.25490196
    #16  -4.44 -1.03921569  0.45098039
    #17  -4.04 -0.84313725  0.64705882
    #18  -3.64 -0.64705882  0.84313725
    #19  -3.24 -0.45098039  1.03921569
    #20  -2.84 -0.25490196  1.23529412
    #21  -2.44 -0.05882353  1.43137255
    #22  -2.04  0.13725490  1.62745098
    #23  -1.64  0.33333333  1.82352941
    #24  -1.24  0.52941176  2.01960784
    #25  -0.84  0.72549020  2.21568627
    #26  -0.44  0.92156863  2.41176471
    #27  -0.04  1.11764706  2.60784314
    #28   0.36  1.31372549  2.80392157
    #29   0.76  1.50980392  3.00000000
    #30   1.16  1.70588235  3.19607843
    ##
    ##
    ################# NEW ADDITION; the inclusion of tentative post-test probabilities.
    
    ##
    ##
    ##
    ## basically, (this is from https://ani.stat.fsu.edu/~debdeep/p2_s14.pdf)
    ## your Baysean probability of cognitive impairment (B) given this test score (A)
    ##                            sensitivity * x
    ## P(B | A) = -----------------------------------------------
    ##              sensitivity * x + (1 - specificity) * (1 - x)
    ##
    ##
    ##                             P(abnormal)*P(getting that score (or higher) given CDR>0)
    ##=  -----------------------------------------------------------------------------------------------------------------------------------
    ##   P(abnormal)*P(getting that score (or higher) given CDR>0) + P(NOT getting that score (or higher) given CDR=0) * (1 - P(abnormal))
    ##
    ##
    ##  P(abnormal) is based on simple averaging (i.e., not weighted by study size) of
    ## population prevenence dementia versus age in PMIDs: 12933919, 19478230, 2725870, 4026605, 7113661, 7936280, 18596243, 3324647, 23305823, and DOI: 10.1192/pb.25.10.384
    ##  which is Percent = 100/(1+exp(-(-14.6325+0.1547*Age)))
    ##...and then added to a best-fit curve of that data, is the population prevalence of MCI / CIND
    ##  from  PMIDs: 10894316, 16954687, 11083505, 16377428, 18347351, 12928907, 11706107, 14568808, 16286549, 18028343, 15557506
    ##...and the best-fit for P(dementia or MCI or CIND) is
    ##  Percent = 100/(1+exp(-(-8.9353106+0.1018231*Age)))
    ##
    ##   we know this underestimates prevalence for some groups, like stroke since
    ##    ~20-35% of those with a stroke in their 40s have cognitive deficits 10yr later (PMID: 23652272)
    ##    and prevalence of cognitive impairment in those who had a stroke in young adulthoos is ~12% for those under 49 (PMID: 17169527)
    ##
    ##   P(getting that score (or higher) given CDR>0) is 1-"sens"
    ##     where "sens" would be the sensitivity in a different meaning than the above equation, and instead meaning
    ##     "probability that the impaired patient will fail the test, given score must be at least [this much] to pass" and [this much] is replaced with 30, 29, 28, and so on.
    ##
    ##   P(NOT getting that score (or higher) given CDR=0)  is 1-"spec"
    ##     where "spec" would be specifcity with a different meaning than in the above question, and instead meaning
    ##     "probability that the cognitively normal patient will pass the test, given score must be at least [this much] to pass"
    ##
    ##   one can hand-calculate the empiric probabilities. We have 60 people with a CDR global score.
#CDR    SATURN
#0	19
#0	21
#0	23
#0	24
#0	24
#0	25
#0	25
#0	26
#0	26
#0	26
#0	26
#0	26
#0	27
#0	27
#0	27
#0	27
#0	27
#0	27
#0	27
#0	27
#0	28
#0	28
#0	28
#0	29
#0	29
#0	29
#0	29
#0	29
#0	29
#0	29
#0	29
#0	29
#0	29
#0	30
#0	30
#0	30
#0	30
#0	30
#2	8
#1	10
#2	10
#1	11
#1	11
#1	12
#2	12
#1	14
#0.5	15
#0.5	15
#1	15
#1	15
#0.5	17
#0.5	19
#0.5	19
#1	19
#0.5	22
#0.5	23
#0.5	27
#1	27
#0.5	28
#0.5	28
    ##   cutoff score    "sens"    "spec"      P(getting that score (or higher) given CDR>0)     P(NOT getting that score (or higher) given CDR=0)
    ##             30    1.0000	    0.1316      0.000	                                            0.868
    ##             29    1.0000     0.3947      0.000                                               0.605
    ##             28    0.9091	    0.4737      0.091                                               0.526
    ##             27    0.8182	    0.6842      0.182	                                            0.316
    ##             26    0.8182	    0.8158	0.182	                                            0.184
    ##             25	 0.8182	    0.8684	0.182	                                            0.132
    ##             24	 0.8182	    0.9211	0.182	                                            0.079
    ##             23	 0.7727	    0.9474	0.227	                                            0.053
    ##             22	 0.7273	    0.9474	0.273	                                            0.053
    ##             21	 0.7273	    0.9737	0.273	                                            0.026
    ##             20	 0.7273	    0.9737	0.273	                                            0.026
    ##             19	 0.5909	    1.0000	0.409	                                            0.000
    ##             18	 0.5909	    1.0000	0.409	                                            0.000
    ##             17	 0.5455	    1.0000	0.455	                                            0.000
    ##             16	 0.5455	    1.0000	0.455	                                            0.000
    ##             15	 0.3636	    1.0000	0.636	                                            0.000
    ##             14	 0.3182	    1.0000	0.682	                                            0.000
    ##             13	 0.3182	    1.0000	0.682	                                            0.000
    ##             12	 0.2273	    1.0000	0.773	                                            0.000
    ##             11	 0.1364	    1.0000	0.864	                                            0.000
    ##             10	 0.0455	    1.0000	0.955	                                            0.000
    ##             9	 0.0455	    1.0000	0.955	                                            0.000
    ##             8	 0.0000	    1.0000	1.000	                                            0.000
    ##             7	 0.0000	    1.0000	1.000	                                            0.000
    ##             6	 0.0000	    1.0000	1.000	                                            0.000
    ##             5	 0.0000	    1.0000	1.000	                                            0.000
    ##             4	 0.0000	    1.0000	1.000	                                            0.000
    ##             3	 0.0000	    1.0000	1.000	                                            0.000
    ##             2	 0.0000	    1.0000	1.000	                                            0.000
    ##             1	 0.0000	    1.0000	1.000	                                            0.000
    ##             0	 0.0000	    1.0000	1.000	                                            0.000


    ## instead of the raw data, though, I instead used a Gompertz curve fit to "sens" and "spec" (G.3())
    ##  which lead to slightly different values, which is nice because we should not completely exclude possibility of
    ##  mild cognitive impairment even when someone gets a perfect score.
    ##   cutoff score    "sens"    "spec"        P(getting that score (or higher) given CDR>0)     P(NOT getting that score (or higher) given CDR=0)
    ##             30    0.926	   0.162	 0.074	                                            0.838
    ##             29    0.916	   0.337	 0.084	                                            0.663
    ##             28    0.903	   0.523	 0.097	                                            0.477
    ##             27    0.888	   0.679	 0.112	                                            0.321
    ##             26	0.871	    0.793	0.129	                                            0.207
    ##             25	0.850	    0.870	0.150	                                            0.130
    ##             24	0.826	    0.920	0.174	                                            0.080
    ##             23	0.798	    0.951	0.202	                                            0.049
    ##             22	0.766	    0.970	0.234	                                            0.030
    ##             21	0.728	    0.982	0.272	                                            0.018
    ##             20	0.686	    0.989	0.314	                                            0.011
    ##             19	0.638	    0.993	0.362	                                            0.007
    ##             18	0.584	    0.995	0.416	                                            0.005
    ##             17	0.526	    0.997	0.474	                                            0.003
    ##             16	0.463	    0.998	0.537	                                            0.002
    ##             15	0.398	    0.998	0.602	                                            0.002
    ##             14	0.331	    0.998	0.669	                                            0.002
    ##             13	0.265	    0.999	0.735	                                            0.001
    ##             12	0.203	    0.999	0.797	                                            0.001
    ##             11	0.148	    0.999	0.852	                                            0.001
    ##             10	0.100	    0.999	0.900	                                            0.001
    ##             9	0.063	    0.999	0.937	                                            0.001
    ##             8	0.036	    0.999	0.964	                                            0.001
    ##             7	0.018	    0.999	0.982	                                            0.001
    ##             6	0.008	    0.999	0.992	                                            0.001
    ##             5	0.003	    0.999	0.997	                                            0.001
    ##             4	0.001	    0.999	0.999	                                            0.001
    ##             3	0.000	    0.999	1.000	                                            0.001
    ##             2	0.000	    0.999	1.000	                                            0.001
    ##             1	0.000	    0.999	1.000	                                            0.001
    ##             0	0.000	    0.999	1.000	                                            0.001
    ##
    ##  ### and so those values are used with the above Baysean equation and multiplied into either this (or the inverse, P(abnormal), depending on your formulation)
    ## P(normal, i.e. neither has MCI nor dementia) stratified by age							
    ###age_50	    age_60	        age_65	        age_70	        age_75	        age_80	        age_85	        age_90
    ###0.979044082  0.944060769	        0.910259626	0.859082894	0.785595582	0.687715929	0.569631318	0.44305603
    ##
    ##
    ## IMPORTANT: THIS ASSUMES NO EFFECT OF NORMAL AGING ON SATURN SCORES (i.e., that a given score's sensitivity and specificity for impairment is unchanged with age)
    ##  which is probably not true, though we suspect the effect of age on "normal" performance is smaller than for the MoCA.
    ##
    ### although a bit labor intensive, we'll just prep some blanks, and then write in the results for each SUM_TOTAL_POINTS
    posttest50=""
    posttest60=""
    posttest65=""
    posttest70=""
    posttest75=""
    posttest80=""
    posttest85=""
    posttest90=""
    ###
    ##
    ##
    
    explanation=""
    CDRzero=""
    CDRzeroPfive=""
    CDRatLEASTone=""
    ## for the "Most" ...we're rounding down the lower bound and rounding up the upper
    ## bound of 50%CI. That way, we report in integers, and are confident at least half
    ## will be in that range.
    ## for the z-scores, we're just rounding to the nearest 0.1
    if SUM_TOTAL_POINTS == 0:
        #        explanation="Most with this SATURN score have a MoCA score < 8."
        explanation="< 8"
        CDRzero="z-score for CDR = 0.0 [cognitively intact] is -10.8"
        CDRzeroPfive="z-score for CDR = 0.5 [mild cognitive impairment] is -4.2"
        CDRatLEASTone="z-score for CDR >= 1.0 [dementia] is -2.7"
        posttest50="95%"
        posttest60="98%"
        posttest65="99%"
        posttest70=">99%"
        posttest75=">99%"
        posttest80=">99%"
        posttest85=">99%"
        posttest90=">99%"
    if SUM_TOTAL_POINTS == 1:
        explanation="4 to 9"
        CDRzero="z-score for CDR = 0.0 [cognitively intact] is -10.4"
        CDRzeroPfive="z-score for CDR = 0.5 [mild cognitive impairment] is -4.0"
        CDRatLEASTone="z-score for CDR >= 1.0 [dementia] is -2.5"
        posttest50="95%"
        posttest60="98%"
        posttest65="99%"
        posttest70=">99%"
        posttest75=">99%"
        posttest80=">99%"
        posttest85=">99%"
        posttest90=">99%"
    if SUM_TOTAL_POINTS == 2:
        explanation="5 to 10"
        CDRzero="z-score for CDR = 0.0 [cognitively intact] is -10.0"
        CDRzeroPfive="z-score for CDR = 0.5 [mild cognitive impairment] is -3.8"
        CDRatLEASTone="z-score for CDR >= 1.0 [dementia] is -2.3"
        posttest50="95%"
        posttest60="98%"
        posttest65="99%"
        posttest70=">99%"
        posttest75=">99%"
        posttest80=">99%"
        posttest85=">99%"
        posttest90=">99%"
    if SUM_TOTAL_POINTS == 3:
        explanation="6 to 10"
        CDRzero="z-score for CDR = 0.0 [cognitively intact] is -9.6"
        CDRzeroPfive="z-score for CDR = 0.5 [mild cognitive impairment] is -3.6"
        CDRatLEASTone="z-score for CDR >= 1.0 [dementia] is -2.1"
        posttest50="95%"
        posttest60="98%"
        posttest65="99%"
        posttest70=">99%"
        posttest75=">99%"
        posttest80=">99%"
        posttest85=">99%"
        posttest90=">99%"
    if SUM_TOTAL_POINTS == 4:
        explanation="7 to 11"
        CDRzero="z-score for CDR = 0.0 [cognitively intact] is -9.2"
        CDRzeroPfive="z-score for CDR = 0.5 [mild cognitive impairment] is -3.4"
        CDRatLEASTone="z-score for CDR >= 1.0 [dementia] is -1.9"
        posttest50="95%"
        posttest60="98%"
        posttest65="99%"
        posttest70=">99%"
        posttest75=">99%"
        posttest80=">99%"
        posttest85=">99%"
        posttest90=">99%"
    if SUM_TOTAL_POINTS == 5:
        explanation="7 to 12"
        CDRzero="z-score for CDR = 0.0 [cognitively intact] is -8.8"
        CDRzeroPfive="z-score for CDR = 0.5 [mild cognitive impairment] is -3.2"
        CDRatLEASTone="z-score for CDR >= 1.0 [dementia] is -1.7"
        posttest50="95%"
        posttest60="98%"
        posttest65="99%"
        posttest70=">99%"
        posttest75=">99%"
        posttest80=">99%"
        posttest85=">99%"
        posttest90=">99%"
    if SUM_TOTAL_POINTS == 6:
        explanation="8 to 12"
        CDRzero="z-score for CDR = 0.0 [cognitively intact] is -8.4"
        CDRzeroPfive="z-score for CDR = 0.5 [mild cognitive impairment] is -3.0"
        CDRatLEASTone="z-score for CDR >= 1.0 [dementia] is -1.5"
        posttest50="95%"
        posttest60="98%"
        posttest65="99%"
        posttest70=">99%"
        posttest75=">99%"
        posttest80=">99%"
        posttest85=">99%"
        posttest90=">99%"
    if SUM_TOTAL_POINTS == 7:
        explanation="9 to 13"
        CDRzero="z-score for CDR = 0.0 [cognitively intact] is -8.0"
        CDRzeroPfive="z-score for CDR = 0.5 [mild cognitive impairment] is -2.8"
        CDRatLEASTone="z-score for CDR >= 1.0 [dementia] is -1.3"
        posttest50="95%"
        posttest60="98%"
        posttest65="99%"
        posttest70=">99%"
        posttest75=">99%"
        posttest80=">99%"
        posttest85=">99%"
        posttest90=">99%"
    if SUM_TOTAL_POINTS == 8:
        explanation="10 to 14"
        CDRzero="z-score for CDR = 0.0 [cognitively intact] is -7.6"
        CDRzeroPfive="z-score for CDR = 0.5 [mild cognitive impairment] is -2.6"
        CDRatLEASTone="z-score for CDR >= 1.0 [dementia] is -1.1"
        posttest50="95%"
        posttest60="98%"
        posttest65="99%"
        posttest70=">99%"
        posttest75=">99%"
        posttest80=">99%"
        posttest85=">99%"
        posttest90=">99%"
    if SUM_TOTAL_POINTS == 9:
        explanation="11 to 15"
        CDRzero="z-score for CDR = 0.0 [cognitively intact] is -7.2"
        CDRzeroPfive="z-score for CDR = 0.5 [mild cognitive impairment] is -2.4"
        CDRatLEASTone="z-score for CDR >= 1.0 [dementia] is -0.9"
        posttest50="94%"
        posttest60="98%"
        posttest65="99%"
        posttest70=">99%"
        posttest75=">99%"
        posttest80=">99%"
        posttest85=">99%"
        posttest90=">99%"
    if SUM_TOTAL_POINTS == 10:
        explanation="12 to 15"
        CDRzero="z-score for CDR = 0.0 [cognitively intact] is -6.8"
        CDRzeroPfive="z-score for CDR = 0.5 [mild cognitive impairment] is -2.2"
        CDRatLEASTone="z-score for CDR >= 1.0 [dementia] is -0.7"
        posttest50="94%"
        posttest60="98%"
        posttest65="99%"
        posttest70=">99%"
        posttest75=">99%"
        posttest80=">99%"
        posttest85=">99%"
        posttest90=">99%"
    if SUM_TOTAL_POINTS == 11:
        explanation="13 to 16"
        CDRzero="z-score for CDR = 0.0 [cognitively intact] is -6.4"
        CDRzeroPfive="z-score for CDR = 0.5 [mild cognitive impairment] is -2.0"
        CDRatLEASTone="z-score for CDR >= 1.0 [dementia] is -0.5"
        posttest50="94%"
        posttest60="98%"
        posttest65="99%"
        posttest70=">99%"
        posttest75=">99%"
        posttest80=">99%"
        posttest85=">99%"
        posttest90=">99%"
    if SUM_TOTAL_POINTS == 12:
        explanation="13 to 17"
        CDRzero="z-score for CDR = 0.0 [cognitively intact] is -6.0"
        CDRzeroPfive="z-score for CDR = 0.5 [mild cognitive impairment] is -1.8"
        CDRatLEASTone="z-score for CDR >= 1.0 [dementia] is -0.3"
        posttest50="93%"
        posttest60="97%"
        posttest65="98%"
        posttest70="99%"
        posttest75=">99%"
        posttest80=">99%"
        posttest85=">99%"
        posttest90=">99%"
    if SUM_TOTAL_POINTS == 13:
        explanation="14 to 17"
        CDRzero="z-score for CDR = 0.0 [cognitively intact] is -5.6"
        CDRzeroPfive="z-score for CDR = 0.5 [mild cognitive impairment] is -1.6"
        CDRatLEASTone="z-score for CDR >= 1.0 [dementia] is -0.1"
        posttest50="92%"
        posttest60="97%"
        posttest65="98%"
        posttest70="99%"
        posttest75=">99%"
        posttest80=">99%"
        posttest85=">99%"
        posttest90=">99%"
    if SUM_TOTAL_POINTS == 14:
        explanation="15 to 18"
        CDRzero="z-score for CDR = 0.0 [cognitively intact] is -5.2"
        CDRzeroPfive="z-score for CDR = 0.5 [mild cognitive impairment] is -1.4"
        CDRatLEASTone="z-score for CDR >= 1.0 [dementia] is +0.1"
        posttest50="90%"
        posttest60="96%"
        posttest65="98%"
        posttest70="99%"
        posttest75=">99%"
        posttest80=">99%"
        posttest85=">99%"
        posttest90=">99%"
    if SUM_TOTAL_POINTS == 15:
        explanation="16 to 19"
        CDRzero="z-score for CDR = 0.0 [cognitively intact] is -4.8"
        CDRzeroPfive="z-score for CDR = 0.5 [mild cognitive impairment] is -1.2"
        CDRatLEASTone="z-score for CDR >= 1.0 [dementia] is +0.3"
        posttest50="87%"
        posttest60="95%"
        posttest65="97%"
        posttest70="98%"
        posttest75="99%"
        posttest80=">99%"
        posttest85=">99%"
        posttest90=">99%"
    if SUM_TOTAL_POINTS == 16:
        explanation="17 to 20"
        CDRzero="z-score for CDR = 0.0 [cognitively intact] is -4.4"
        CDRzeroPfive="z-score for CDR = 0.5 [mild cognitive impairment] is -1.0"
        CDRatLEASTone="z-score for CDR >= 1.0 [dementia] is +0.5"
        posttest50="82%"
        posttest60="93%"
        posttest65="96%"
        posttest70="97%"
        posttest75="98%"
        posttest80="99%"
        posttest85=">99%"
        posttest90=">99%"
    if SUM_TOTAL_POINTS == 17:
        explanation="18 to 20"
        CDRzero="z-score for CDR = 0.0 [cognitively intact] is -4.0"
        CDRzeroPfive="z-score for CDR = 0.5 [mild cognitive impairment] is -0.8"
        CDRatLEASTone="z-score for CDR >= 1.0 [dementia] is +0.6"
        posttest50="75%"
        posttest60="89%"
        posttest65="93%"
        posttest70="96%"
        posttest75="97%"
        posttest80="98%"
        posttest85=">99%"
        posttest90=">99%"
    if SUM_TOTAL_POINTS == 18:
        explanation="19 to 21"
        CDRzero="z-score for CDR = 0.0 [cognitively intact] is -3.6"
        CDRzeroPfive="z-score for CDR = 0.5 [mild cognitive impairment] is -0.6"
        CDRatLEASTone="z-score for CDR >= 1.0 [dementia] is +0.8"
        posttest50="65%"
        posttest60="84%"
        posttest65="89%"
        posttest70="93%"
        posttest75="96%"
        posttest80="98%"
        posttest85="98%"
        posttest90=">99%"
    if SUM_TOTAL_POINTS == 19:
        explanation="19 to 22"
        CDRzero="z-score for CDR = 0.0 [cognitively intact] is -3.2"
        CDRzeroPfive="z-score for CDR = 0.5 [mild cognitive impairment] is -0.5"
        CDRatLEASTone="z-score for CDR >= 1.0 [dementia] is +1.0"
        posttest50="51%"
        posttest60="75%"
        posttest65="83%"
        posttest70="89%"
        posttest75="93%"
        posttest80="96%"
        posttest85="97%"
        posttest90="98%"
    if SUM_TOTAL_POINTS == 20:
        explanation="20 to 22"
        CDRzero="z-score for CDR = 0.0 [cognitively intact] is -2.8"
        CDRzeroPfive="z-score for CDR = 0.5 [mild cognitive impairment] is -0.3"
        CDRatLEASTone="z-score for CDR >= 1.0 [dementia] is +1.2"
        posttest50="37%"
        posttest60="62%"
        posttest65="73%"
        posttest70="82%"
        posttest75="88%"
        posttest80="93%"
        posttest85="95%"
        posttest90="97%"
    if SUM_TOTAL_POINTS == 21:
        explanation="21 to 23"
        CDRzero="z-score for CDR = 0.0 [cognitively intact] is -2.4"
        CDRzeroPfive="z-score for CDR = 0.5 [mild cognitive impairment] is -0.1"
        CDRatLEASTone="z-score for CDR >= 1.0 [dementia] is +1.4"
        posttest50="24%"
        posttest60="47%"
        posttest65="59%"
        posttest70="71%"
        posttest75="80%"
        posttest80="87%"
        posttest85="92%"
        posttest90="95%"
    if SUM_TOTAL_POINTS == 22:
        explanation="22 to 24"
        CDRzero="z-score for CDR = 0.0 [cognitively intact] is -2.0"
        CDRzeroPfive="z-score for CDR = 0.5 [mild cognitive impairment] is +0.1"
        CDRatLEASTone="z-score for CDR >= 1.0 [dementia] is +1.6"
        posttest50="14%"
        posttest60="32%"
        posttest65="44%"
        posttest70="56%"
        posttest75="68%"
        posttest80="78%"
        posttest85="86%"
        posttest90="91%"
    if SUM_TOTAL_POINTS == 23:
        explanation="23 to 25"
        CDRzero="z-score for CDR = 0.0 [cognitively intact] is -1.6"
        CDRzeroPfive="z-score for CDR = 0.5 [mild cognitive impairment] is +0.3"
        CDRatLEASTone="z-score for CDR >= 1.0 [dementia] is +1.8"
        posttest50="8%"
        posttest60="20%"
        posttest65="29%"
        posttest70="40%"
        posttest75="53%"
        posttest80="65%"
        posttest85="76%"
        posttest90="84%"
    if SUM_TOTAL_POINTS == 24:
        explanation="24 to 26"
        CDRzero="z-score for CDR = 0.0 [cognitively intact] is -1.2"
        CDRzeroPfive="z-score for CDR = 0.5 [mild cognitive impairment] is +0.5"
        CDRatLEASTone="z-score for CDR >= 1.0 [dementia] is +2.0"
        posttest50="4.4%"
        posttest60="11%"
        posttest65="18%"
        posttest70="26%"
        posttest75="37%"
        posttest80="50%"
        posttest85="62%"
        posttest90="73%"
    if SUM_TOTAL_POINTS == 25:
        explanation="24 to 26"
        CDRzero="z-score for CDR = 0.0 [cognitively intact] is -0.8"
        CDRzeroPfive="z-score for CDR = 0.5 [mild cognitive impairment] is +0.7"
        CDRatLEASTone="z-score for CDR >= 1.0 [dementia] is +2.2"
        posttest50="2.4%"
        posttest60="6.4%"
        posttest65="10%"
        posttest70="16%"
        posttest75="24%"
        posttest80="34%"
        posttest85="47%"
        posttest90="59%"
    if SUM_TOTAL_POINTS == 26:
        explanation="25 to 27"
        CDRzero="z-score for CDR = 0.0 [cognitively intact] is -0.4"
        CDRzeroPfive="z-score for CDR = 0.5 [mild cognitive impairment] is +0.9"
        CDRatLEASTone="z-score for CDR >= 1.0 [dementia] is +2.4"
        posttest50="1.3%"
        posttest60="3.6%"
        posttest65="5.8%"
        posttest70="9%"
        posttest75="15%"
        posttest80="22%"
        posttest85="32%"
        posttest90="44%"
    if SUM_TOTAL_POINTS == 27:
        explanation="26 to 28"
        CDRzero="z-score for CDR = 0.0 [cognitively intact] is -0.0"
        CDRzeroPfive="z-score for CDR = 0.5 [mild cognitive impairment] is +1.1"
        CDRatLEASTone="z-score for CDR >= 1.0 [dementia] is +2.6"
        posttest50="0.7%"
        posttest60="2.0%"
        posttest65="3.3%"
        posttest70="5.4%"
        posttest75="8.6%"
        posttest80="14%"
        posttest85="21%"
        posttest90="30%"
    if SUM_TOTAL_POINTS == 28:
        explanation="27 to 29"
        CDRzero="z-score for CDR = 0.0 [cognitively intact] is +0.4"
        CDRzeroPfive="z-score for CDR = 0.5 [mild cognitive impairment] is +1.3"
        CDRatLEASTone="z-score for CDR >= 1.0 [dementia] is +2.8"
        posttest50="0.4%"
        posttest60="1.2%"
        posttest65="2.0%"
        posttest70="3.2%"
        posttest75="5.2%"
        posttest80="8%"
        posttest85="13%"
        posttest90="20%"
    if SUM_TOTAL_POINTS == 29:
        explanation="27 to 30"
        CDRzero="z-score for CDR = 0.0 [cognitively intact] is +0.8"
        CDRzeroPfive="z-score for CDR = 0.5 [mild cognitive impairment] is +1.5"
        CDRatLEASTone="z-score for CDR >= 1.0 [dementia] is +3.0"
        posttest50="0.3%"
        posttest60="0.7%"
        posttest65="1.2%"
        posttest70="2.0%"
        posttest75="3.2%"
        posttest80="5%"
        posttest85="9%"
        posttest90="14%"
    if SUM_TOTAL_POINTS == 30:
        explanation="28 to 30"
        CDRzero="z-score for CDR = 0.0 [cognitively intact] is +1.2"
        CDRzeroPfive="z-score for CDR = 0.5 [mild cognitive impairment] is +1.7"
        CDRatLEASTone="z-score for CDR >= 1.0 [dementia] is +3.2"
        posttest50="0.2%"
        posttest60="0.5%"
        posttest65="0.9%"
        posttest70="1.4%"
        posttest75="2.3%"
        posttest80="4%"
        posttest85="6%"
        posttest90="10%"
    ############################################################
    ## NEXT, HARD-CODING SOME MEAN AND SD PERFORMANCE FOR Z-SCORE CALCULATIONS based on n=38 with CDR=0.0
    ############################################################
   ## </update for APR-2020>
   ## <update for MAY-2020> <to 0-3-9>    
    ## reading speed (ms per word)**
    PRIOR_read_speed_mean=float(410)
    PRIOR_read_speed_sd=float(132)
    ##
    ## motor speed (ms between button presses)**
    PRIOR_motor_speed_mean=float(922)
    PRIOR_motor_speed_sd=float(296)
    ##
    ## time on simple attention tasks (ms) [average of three]**
    PRIOR_ATTENTION_TIME_mean=float(7311)
    PRIOR_ATTENTION_TIME_sd=float(2200)
    ##)
    ## time on stroop tasks (ms) [average of 12]**
    PRIOR_STROOP_TIME_mean=float(3398)
    PRIOR_STROOP_TIME_sd=float(1233)
    ##
    ## time on trails B (mini) (ms)**
    PRIOR_TRAILSB_TIME_mean=float(24362)
    PRIOR_TRAILSB_TIME_sd=float(12653)
    ##
    ## time on trails A (mini) (ms)**
    PRIOR_TRAILSA_TIME_mean=float(10418)
    PRIOR_TRAILSA_TIME_sd=float(4186)
    ##
    ## time on the four drawing tasks (note, this is with n=32)**
    PRIOR_VISUOSPATIAL_TIME_mean=float(25102)
    PRIOR_VISUOSPATIAL_TIME_sd=float(12812)
    ##
    ## sum of time on the math tasks (total over two tasks)**
    ## 
    PRIOR_MATH_TIME_mean=float(31401)
    PRIOR_MATH_TIME_sd=float(15527)
    ##
    ## time on orientation tasks (ms) [average of 4]**
    PRIOR_ORIENTATION_TIME_mean=float(5588)
    PRIOR_ORIENTATION_TIME_sd=float(2232)
    ##
    ## time on incidental memory tasks (ms) [average of 3]**
    PRIOR_INCIDENTAL_TIME_mean=float(10178)
    PRIOR_INCIDENTAL_TIME_sd=float(4860)
    ##
    ## time on studied 5 words recall task (ms)**
    PRIOR_STUDIED_TIME_mean=float(65966)
    PRIOR_STUDIED_TIME_sd=float(57959)
    ############################################################
    ## NEXT, HARD-CODING SOME MEAN AND SD PERFORMANCE FOR Z-SCORE CALCULATIONS based on n=19 study partners
    ############################################################
    #
    # <reading time>
    MS_PER_WORD="NA"
    MS_PER_WORD_Z="NA"
    n = len(READING_SPEED_LOG)-1
    if n > 1:
        MS_PER_WORD=(1000/float(MEDIAN_READING_SPEED))
        MS_PER_WORD_Z=(MS_PER_WORD-PRIOR_read_speed_mean)/PRIOR_read_speed_sd
    textREAD=Text(text="NA",color=(0,0,0),position=(215,70),font_size=24,anchor='center')
    if MS_PER_WORD != "NA":
        textREAD=Text(text="%.1f"%MS_PER_WORD,color=(0,0,0),position=(215,70),font_size=24,anchor='center')
    #
    textREADz=Text(text="NA",color=(0,0,0),position=(215,22),font_size=24,anchor='center')
    if MS_PER_WORD_Z != "NA":
        if MS_PER_WORD_Z > 2:
            textREADz=Text(text="%.1f"%MS_PER_WORD_Z,color=(20,0,0),position=(215,22),font_size=24,anchor='center')
        elif MS_PER_WORD_Z > 3:
            textREADz=Text(text="%.1f"%MS_PER_WORD_Z,color=(50,0,0),position=(215,22),font_size=24,anchor='center')
        else:
            textREADz=Text(text="%.1f"%MS_PER_WORD_Z,color=(0,0,0),position=(215,22),font_size=24,anchor='center')
    # </reading time>
    #
    # <motor time>
    MS_PER_PRESS="NA"
    MS_PER_PRESS_Z="NA"
    n = len(MOTOR_SPEED_LOG)-1
    if n > 1:
        MS_PER_PRESS=float(MEDIAN_MOTOR_SPEED)
        MS_PER_PRESS_Z=(MS_PER_PRESS-PRIOR_motor_speed_mean)/PRIOR_motor_speed_sd
    textMOVE=Text(text="NA",color=(0,0,0),position=(348,70),font_size=24,anchor='center')
    if MS_PER_PRESS != "NA":
        textMOVE=Text(text="%.1f"%MS_PER_PRESS,color=(0,0,0),position=(348,70),font_size=24,anchor='center')
    textMOVEz=Text(text="NA",color=(0,0,0),position=(348,22),font_size=24,anchor='center')
    if MS_PER_PRESS_Z != "NA":
        textMOVEz=Text(text="%.1f"%MS_PER_PRESS_Z,color=(0,0,0),position=(348,22),font_size=24,anchor='center')
        if MS_PER_PRESS_Z > 2:
            textMOVEz=Text(text="%.1f"%MS_PER_PRESS_Z,color=(20,0,0),position=(348,22),font_size=24,anchor='center')
        if MS_PER_PRESS_Z > 3:
            textMOVEz=Text(text="%.1f"%MS_PER_PRESS_Z,color=(50,0,0),position=(348,22),font_size=24,anchor='center')
    # </motor time>
    #
    # <attention time>
    MS_ATTENTION="NA"
    MS_ATTENTION_Z="NA"
    ATTENTION_TIME="NA"
    n = 0
    if ATTENTION_LOG[2][1] != "NA":
        n=n+1
        ATTENTION_TIME=float(ATTENTION_LOG[2][1])
    if ATTENTION_LOG[2][2] != "NA":
        n=n+1
        ATTENTION_TIME=ATTENTION_TIME+float(ATTENTION_LOG[2][2])
    if ATTENTION_LOG[2][3] != "NA":
        n=n+1
        ATTENTION_TIME=ATTENTION_TIME+float(ATTENTION_LOG[2][3])
    if n > 0:
        MS_ATTENTION=ATTENTION_TIME/float(n)
        MS_ATTENTION_Z=(MS_ATTENTION-PRIOR_ATTENTION_TIME_mean)/PRIOR_ATTENTION_TIME_sd
        ## put into seconds:
        MS_ATTENTION=MS_ATTENTION/1000
    textATTENTION=Text(text="NA",color=(0,0,0),position=(66,560),font_size=24,anchor='upperright')
    if MS_ATTENTION != "NA":
        textATTENTION=Text(text="%.1f"%MS_ATTENTION,color=(0,0,0),position=(66,560),font_size=24,anchor='upperright')
    textATTENTIONz=Text(text="NA",color=(0,0,0),position=(125,560),font_size=24,anchor='upperright')
    if MS_ATTENTION_Z != "NA":
        textATTENTIONz=Text(text="%.1f"%MS_ATTENTION_Z,color=(0,0,0),position=(125,560),font_size=24,anchor='upperright')
    # start log of "useful" z.scores (keep sum and n):
    #
    USEFULsum="NA"
    USEFULn="NA"
    if MS_ATTENTION != "NA":
        USEFULsum=(MS_ATTENTION-PRIOR_ATTENTION_TIME_mean)/PRIOR_ATTENTION_TIME_sd
        USEFULn=1
    # later, use USEFUL.append( )                        
    # </attention time>
    #
    # <stroop time>
    MS_STROOP="NA"
    MS_STROOP_Z="NA"
    textSTROOP=Text(text="NA",color=(0,0,0),position=(66,522),font_size=24,anchor='upperright')
    textSTROOPz=Text(text="NA",color=(0,0,0),position=(125,522),font_size=24,anchor='upperright')
    if STROOP_SUM_OF_TIME != "NA":
        ##         
        MS_STROOP=float(STROOP_SUM_OF_TIME)/float(STROOP_NUMBER_ANSWERED)
        MS_STROOP_Z=(MS_STROOP-PRIOR_STROOP_TIME_mean)/PRIOR_STROOP_TIME_sd
        ## put into seconds:
        MS_STROOP=MS_STROOP/1000
        # continue log of "useful" z.scores:
        USEFULsum=USEFULsum+MS_STROOP_Z
        USEFULn=USEFULn+1
        textSTROOP=Text(text="%.1f"%MS_STROOP,color=(0,0,0),position=(66,522),font_size=24,anchor='upperright')
        textSTROOPz=Text(text="%.1f"%MS_STROOP_Z,color=(0,0,0),position=(125,522),font_size=24,anchor='upperright')                        
    # </stroop time>
    #
    #
    # <trails B time>
    MS_TRAILSB="NA"
    MS_TRAILSB_Z="NA"
    textTRAILSB=Text(text="NA",color=(0,0,0),position=(66,484),font_size=24,anchor='upperright')
    textTRAILSBz=Text(text="NA",color=(0,0,0),position=(125,484),font_size=24,anchor='upperright')
    if TRAILS_LOG[2][2] != "NA":
        ##         
        MS_TRAILSB=float(TRAILS_LOG[2][2])
        MS_TRAILSB_Z=(MS_TRAILSB-PRIOR_TRAILSB_TIME_mean)/PRIOR_TRAILSB_TIME_sd
        ## put into seconds:
        MS_TRAILSB=MS_TRAILSB/1000
##        # continue log of "useful" z.scores:  ## not useful as of APR/MAY-2020 per Kruskal–Wallis one-way analysis of variance comparing CDR_global scores of 0.0, 0.5, and 1.0
                                                ## this might be a false negative to due low n of CDR=1.0 patients who got far enough in SATURN to actually complete this task within the 15 min time limit
##        USEFULsum=USEFULsum+MS_TRAILSB_Z
##        USEFULn=USEFULn+1
        textTRAILSB=Text(text="%.1f"%MS_TRAILSB,color=(0,0,0),position=(66,484),font_size=24,anchor='upperright')
        textTRAILSBz=Text(text="%.1f"%MS_TRAILSB_Z,color=(0,0,0),position=(125,484),font_size=24,anchor='upperright')
    # </trails B time>
    #
    # <trails A time>
    MS_TRAILSA="NA"
    MS_TRAILSA_Z="NA"
    textTRAILSA=Text(text="NA",color=(0,0,0),position=(66,446),font_size=24,anchor='upperright')
    textTRAILSAz=Text(text="NA",color=(0,0,0),position=(125,446),font_size=24,anchor='upperright')
    if TRAILS_LOG[2][1] != "NA":
        ##         
        MS_TRAILSA=float(TRAILS_LOG[2][1])
        MS_TRAILSA_Z=(MS_TRAILSA-PRIOR_TRAILSA_TIME_mean)/PRIOR_TRAILSA_TIME_sd
        ## put into seconds (integer):
        MS_TRAILSA=MS_TRAILSA/1000
##        # continue log of "useful" z.scores:  ## not useful as of APR/MAY-2020 per Kruskal–Wallis one-way analysis of variance comparing CDR_global scores of 0.0, 0.5, and 1.0
                                                ## this might be a false negative to due low n of CDR=1.0 patients who got far enough in SATURN to actually complete this task within the 15 min time limit
##        USEFULsum=USEFULsum+MS_TRAILSA_Z
##        USEFULn=USEFULn+1
        textTRAILSA=Text(text="%.1f"%MS_TRAILSA,color=(0,0,0),position=(66,446),font_size=24,anchor='upperright')
        textTRAILSAz=Text(text="%.1f"%MS_TRAILSA_Z,color=(0,0,0),position=(125,446),font_size=24,anchor='upperright')
    # </trails A time>
    #
    # <visuospatial time>
    MS_VISUOSPATIAL="NA"
    MS_VISUOSPATIAL_Z="NA"
    VISUOSPATIAL_TIME="NA"
    n = 0
    textVISUOSPATIAL=Text(text="NA",color=(0,0,0),position=(66,408),font_size=24,anchor='upperright')
    textVISUOSPATIALz=Text(text="NA",color=(0,0,0),position=(125,408),font_size=24,anchor='upperright')
    if SPATIAL_LOG[2][1] != "NA":
        n=n+1
        VISUOSPATIAL_TIME=float(SPATIAL_LOG[2][1])
    if SPATIAL_LOG[2][2] != "NA":
        n=n+1
        VISUOSPATIAL_TIME=VISUOSPATIAL_TIME+float(SPATIAL_LOG[2][2])
    if SPATIAL_LOG[2][3] != "NA":
        n=n+1
        VISUOSPATIAL_TIME=VISUOSPATIAL_TIME+float(SPATIAL_LOG[2][3])
    if SPATIAL_LOG[2][4] != "NA":
        n=n+1
        VISUOSPATIAL_TIME=VISUOSPATIAL_TIME+float(SPATIAL_LOG[2][4])
    if n > 0:
        MS_VISUOSPATIAL=VISUOSPATIAL_TIME/float(n)
        MS_VISUOSPATIAL_Z=(MS_VISUOSPATIAL-PRIOR_VISUOSPATIAL_TIME_mean)/PRIOR_VISUOSPATIAL_TIME_sd
        ## put into seconds:
        MS_VISUOSPATIAL=MS_VISUOSPATIAL/1000
        textVISUOSPATIAL=Text(text="%.1f"%MS_VISUOSPATIAL,color=(0,0,0),position=(66,408),font_size=24,anchor='upperright')
        textVISUOSPATIALz=Text(text="%.1f"%MS_VISUOSPATIAL_Z,color=(0,0,0),position=(125,408),font_size=24,anchor='upperright')
    # this is not a "useful" Z score, so no .append for visuospatial time
    #
    # later, use USEFUL.append( )                        
    # </visuospatial time>
    #
    #
    # <math time>
    ## calculate SUM of time on math problems;
    ## only calculate if both were done. 
    MS_MATH="NA"
    MS_MATH_Z="NA"
    textMATH=Text(text="NA",color=(0,0,0),position=(66,370),font_size=24,anchor='upperright')
    textMATHz=Text(text="NA",color=(0,0,0),position=(125,370),font_size=24,anchor='upperright')     
    if MATH_LOG[2][2] != "NA":
        MS_MATH=float(MATH_LOG[2][1])+float(MATH_LOG[2][2])
        MS_MATH_Z=(MS_MATH-PRIOR_MATH_TIME_mean)/PRIOR_MATH_TIME_sd
        ## put into seconds:
        MS_MATH=MS_MATH/1000
        # continue log of "useful" z.scores:
        USEFULsum=USEFULsum+MS_MATH_Z
        USEFULn=USEFULn+1
        textMATH=Text(text="%.1f"%MS_MATH,color=(0,0,0),position=(66,370),font_size=24,anchor='upperright')
        textMATHz=Text(text="%.1f"%MS_MATH_Z,color=(0,0,0),position=(125,370),font_size=24,anchor='upperright')                      
    # </math time>
    #
    #
    # <orientation time>
    MS_ORIENTATION="NA"
    MS_ORIENTATION_Z="NA"
    ORIENTATION_TIME="NA"
    n = 0
    textORIENTATION=Text(text="NA",color=(0,0,0),position=(66,332),font_size=24,anchor='upperright')
    textORIENTATIONz=Text(text="NA",color=(0,0,0),position=(125,332),font_size=24,anchor='upperright')    
    if ORIENTATION_LOG[2][1] != "NA":
        n=n+1
        ORIENTATION_TIME=float(ORIENTATION_LOG[2][1])
    if ORIENTATION_LOG[2][2] != "NA":
        n=n+1
        ORIENTATION_TIME=ORIENTATION_TIME+float(ORIENTATION_LOG[2][2])
    if ORIENTATION_LOG[2][3] != "NA":
        n=n+1
        ORIENTATION_TIME=ORIENTATION_TIME+float(ORIENTATION_LOG[2][3])
    if ORIENTATION_LOG[2][4] != "NA":
        n=n+1
        ORIENTATION_TIME=ORIENTATION_TIME+float(ORIENTATION_LOG[2][4])
    if n > 0:
        MS_ORIENTATION=ORIENTATION_TIME/float(n)
        MS_ORIENTATION_Z=(MS_ORIENTATION-PRIOR_ORIENTATION_TIME_mean)/PRIOR_ORIENTATION_TIME_sd
        ## put into seconds:
        MS_ORIENTATION=MS_ORIENTATION/1000
        USEFULsum=USEFULsum+MS_ORIENTATION_Z
        USEFULn=USEFULn+1
        textORIENTATION=Text(text="%.1f"%MS_ORIENTATION,color=(0,0,0),position=(66,332),font_size=24,anchor='upperright')
        textORIENTATIONz=Text(text="%.1f"%MS_ORIENTATION_Z,color=(0,0,0),position=(125,332),font_size=24,anchor='upperright')                     
    # </orientation time>
    #
    #
    #
    # <incidental memory time>
    MS_INCIDENTAL="NA"
    MS_INCIDENTAL_Z="NA"
    INCIDENTAL_TIME="NA"
    n = 0
    textINCIDENTAL=Text(text="NA",color=(0,0,0),position=(66,294),font_size=24,anchor='upperright')
    textINCIDENTALz=Text(text="NA",color=(0,0,0),position=(125,294),font_size=24,anchor='upperright')   
    if MEMORY_LOG[2][1] != "NA":
        n=n+1
        INCIDENTAL_TIME=float(MEMORY_LOG[2][1])
    if MEMORY_LOG[2][2] != "NA":
        n=n+1
        INCIDENTAL_TIME=INCIDENTAL_TIME+float(MEMORY_LOG[2][2])
    if MEMORY_LOG[2][3] != "NA":
        n=n+1
        INCIDENTAL_TIME=INCIDENTAL_TIME+float(MEMORY_LOG[2][3])
    if n > 0:
        MS_INCIDENTAL=INCIDENTAL_TIME/float(n)
        MS_INCIDENTAL_Z=(MS_INCIDENTAL-PRIOR_INCIDENTAL_TIME_mean)/PRIOR_INCIDENTAL_TIME_sd
        ## put into seconds:
        MS_INCIDENTAL=MS_INCIDENTAL/1000
        USEFULsum=USEFULsum+MS_INCIDENTAL_Z
        USEFULn=USEFULn+1
        textINCIDENTAL=Text(text="%.1f"%MS_INCIDENTAL,color=(0,0,0),position=(66,294),font_size=24,anchor='upperright')
        textINCIDENTALz=Text(text="%.1f"%MS_INCIDENTAL_Z,color=(0,0,0),position=(125,294),font_size=24,anchor='upperright')                     
    # </incidental memory time>
    #
    #
    #
    # <studied memory time>
    MS_STUDIED="NA"
    MS_STUDIED_Z="NA"
    textSTUDIED=Text(text="NA",color=(0,0,0),position=(66,256),font_size=24,anchor='upperright')
    textSTUDIEDz=Text(text="NA",color=(0,0,0),position=(125,256),font_size=24,anchor='upperright')   
    if MEMORY_LOG[2][4] != "NA":
        MS_STUDIED=float(MEMORY_LOG[2][4])
        MS_STUDIED_Z=(MS_STUDIED-PRIOR_STUDIED_TIME_mean)/PRIOR_STUDIED_TIME_sd
        ## put into seconds:
        MS_STUDIED=MS_STUDIED/1000
        ## not a useful z-score
        textSTUDIED=Text(text="%.1f"%MS_STUDIED,color=(0,0,0),position=(66,256),font_size=24,anchor='upperright')
        textSTUDIEDz=Text(text="%.1f"%MS_STUDIED_Z,color=(0,0,0),position=(125,256),font_size=24,anchor='upperright')                      
    # </studied memory time>
    #
    #
    ## now put in the total time in minutes
    textTOTALtimeMIN = Text(text="NA",color=(0,0,0),position=(79,178),font_size=28,anchor='center')
    if SUM_TIME_SPENT_MS != "NA":
        SUM_TIME_SPENT_MIN=(float(SUM_TIME_SPENT_MS)/6000)/10
        textTOTALtimeMIN = Text(text="%.1f"%SUM_TIME_SPENT_MIN,
                                color=(0,0,0),
                                position=(79,178),
                                font_size=28,
                                anchor='center')
    #
    #
    ## now put in the average of "useful" z-scores if more than one task to aggregate
    USEFUL_z_scoreTIME="NA"
    textZz=Text(text="NA",color=(0,0,0),position=(81,22),font_size=24,anchor='center')
    if USEFULn != "NA":
        if USEFULn > 1:
            USEFUL_z_scoreTIME=USEFULsum/float(USEFULn)
            if USEFUL_z_scoreTIME > 2:
                textZz=Text(text="%.1f"%USEFUL_z_scoreTIME,color=(20,0,0),position=(81,22),font_size=24,anchor='center')
            elif USEFUL_z_scoreTIME > 3:
                textZz=Text(text="%.1f"%USEFUL_z_scoreTIME,color=(50,0,0),position=(81,22),font_size=24,anchor='center')
            else:
                textZz=Text(text="%.1f"%USEFUL_z_scoreTIME,color=(0,0,0),position=(81,22),font_size=24,anchor='center') 
    ###
    ### now, make the text objects.... for the probabilities of impairment:
#        posttest50="0.2%"
#        posttest60="0.5%"
#        posttest65="0.9%"
#        posttest70="1.4%"
#        posttest75="2.3%"
#        posttest80="4%"
#        posttest85="6%"
#        posttest90="10%"
    textposttest50 = Text(text="%s"%posttest50,
                          color=(0,0,0),
                          position=(1004,105),
                          font_size=17,
                          anchor='upperright')
    textposttest60 = Text(text="%s"%posttest60,
                          color=(0,0,0),
                          position=(1004,92),
                          font_size=17,
                          anchor='upperright')
    textposttest65 = Text(text="%s"%posttest65,
                          color=(0,0,0),
                          position=(1004,79),
                          font_size=17,
                          anchor='upperright')
    textposttest70 = Text(text="%s"%posttest70,
                          color=(0,0,0),
                          position=(1004,66),
                          font_size=17,
                          anchor='upperright')
    textposttest75 = Text(text="%s"%posttest75,
                          color=(0,0,0),
                          position=(1004,53),
                          font_size=17,
                          anchor='upperright')
    textposttest80 = Text(text="%s"%posttest80,
                          color=(0,0,0),
                          position=(1004,40),
                          font_size=17,
                          anchor='upperright')
    textposttest85 = Text(text="%s"%posttest85,
                          color=(0,0,0),
                          position=(1004,27),
                          font_size=17,
                          anchor='upperright')
    textposttest90 = Text(text="%s"%posttest90,
                          color=(0,0,0),
                          position=(1004,14),
                          font_size=17,
                          anchor='upperright')
   ## </update for MAY-2020> <to 0-3-9>  
    ### now, make the text objects.... for the stuff to the right:
    text1 = Text(text="%s"%explanation,
                 color=(0,0,0),
                 position=(750,525),
                 font_size=24,
                 anchor='upperleft')
    text2 = Text(text="%s"%CDRzero,
                 color=(0,0,0),
                 position=(946,210),
                 font_size=24,
                 anchor='upperright')
    text3 = Text(text="%s"%CDRzeroPfive,
                 color=(0,0,0),
                 position=(946,192),
                 font_size=24,
                 anchor='upperright')
    text4 = Text(text="%s"%CDRatLEASTone,
                 color=(0,0,0),
                 position=(946,174),
                 font_size=24,
                 anchor='upperright')
    ## and don't forget to print the subject number on the summary sheet!
    text5 = Text(text="SUMMARY FOR PARTICIPANT NUMBER = %d"%subject_number,
                color=(0,0,0),
                 position=(1000,300),
                 font_size=24,
                 anchor='upperright')
    ###
    ### now, make the text objects for the numerical scores:
    ATTENTION_SUM="NA"
    if ATTENTION_LOG[1][1] != "NA":
        ATTENTION_SUM=ATTENTION_LOG[1][1]
    if ATTENTION_LOG[1][2] != "NA":
        ATTENTION_SUM=ATTENTION_SUM+ATTENTION_LOG[1][2]
    if ATTENTION_LOG[1][3] != "NA":
        ATTENTION_SUM=ATTENTION_SUM+ATTENTION_LOG[1][3]
    textA = Text(text="%s"%ATTENTION_SUM,color=(0,0,0),position=(282,551),
                 font_size=24,anchor='center')
    STROOP_SUM="NA"
    if STROOP_SUM_OF_ERRORS != "NA":
        if STROOP_SUM_OF_ERRORS==0:
            STROOP_SUM=3
        elif STROOP_SUM_OF_ERRORS==1:
            STROOP_SUM=2
        elif STROOP_SUM_OF_ERRORS==2:
            STROOP_SUM=1
        elif STROOP_SUM_OF_ERRORS > 2:
            STROOP_SUM=0    
    textB = Text(text="%s"%STROOP_SUM,color=(0,0,0),position=(282,513),
                 font_size=24,anchor='center')
    textC = Text(text="%s"%TRAILS_LOG[1][2],color=(0,0,0),position=(282,475),
                 font_size=24,anchor='center')
    textD = Text(text="%s"%TRAILS_LOG[1][1],color=(0,0,0),position=(282,437),
                 font_size=24,anchor='center')
    SPATIAL_SUM="NA"
    if SPATIAL_LOG[1][1] != "NA":
        SPATIAL_SUM=SPATIAL_LOG[1][1]
    if SPATIAL_LOG[1][2] != "NA":
        SPATIAL_SUM=SPATIAL_SUM+SPATIAL_LOG[1][2]
    if SPATIAL_LOG[1][3] != "NA":
        SPATIAL_SUM=SPATIAL_SUM+SPATIAL_LOG[1][3]
    if SPATIAL_LOG[1][4] != "NA":
        SPATIAL_SUM=SPATIAL_SUM+SPATIAL_LOG[1][4]
    textE = Text(text="%s"%SPATIAL_SUM,color=(0,0,0),position=(282,399),
                 font_size=24,anchor='center')
    MATH_SUM="NA"
    if MATH_LOG[1][1] != "NA":
        MATH_SUM=MATH_LOG[1][1]
    if MATH_LOG[1][2] != "NA":
        MATH_SUM=MATH_SUM+MATH_LOG[1][2]
    textF = Text(text="%s"%MATH_SUM,color=(0,0,0),position=(282,361),
                 font_size=24,anchor='center')
    ORIENTATION_SUM="NA"
    if ORIENTATION_LOG[1][1] != "NA":
        ORIENTATION_SUM=ORIENTATION_LOG[1][1]
    if ORIENTATION_LOG[1][2] != "NA":
        ORIENTATION_SUM=ORIENTATION_SUM+ORIENTATION_LOG[1][2]
    if ORIENTATION_LOG[1][3] != "NA":
        ORIENTATION_SUM=ORIENTATION_SUM+ORIENTATION_LOG[1][3]
    if ORIENTATION_LOG[1][4] != "NA":
        ORIENTATION_SUM=ORIENTATION_SUM+ORIENTATION_LOG[1][4]
    textG = Text(text="%s"%ORIENTATION_SUM,color=(0,0,0),position=(282,323),
                 font_size=24,anchor='center')
    INCIDENTAL_SUM="NA"
    if MEMORY_LOG[1][1] != "NA":
        INCIDENTAL_SUM=MEMORY_LOG[1][1]
    if MEMORY_LOG[1][2] != "NA":
        INCIDENTAL_SUM=INCIDENTAL_SUM+MEMORY_LOG[1][2]
    if MEMORY_LOG[1][3] != "NA":    
        INCIDENTAL_SUM=INCIDENTAL_SUM+MEMORY_LOG[1][3]
    textH = Text(text="%s"%INCIDENTAL_SUM,color=(0,0,0),position=(282,285),
                 font_size=24,anchor='center')
    STUDIED_SUM="NA"
    if MEMORY_LOG[1][4] != "NA":
        STUDIED_SUM=MEMORY_LOG[1][4]
    textI = Text(text="%s"%STUDIED_SUM,color=(0,0,0),position=(282,247),
                 font_size=24,anchor='center')
    textTOTAL = Text(text="%s"%SUM_TOTAL_POINTS,
                 color=(0,0,0),
                 position=(282,178),
                 font_size=28,
                 anchor='center')
    stim = TextureStimulus(texture=REVIEWSCREEN,position=(0,0))
    screen.clear()
    viewport = VisionEgg.Core.Viewport(screen=screen, size=screen.size, stimuli=[stim,stim])
    viewportTIMESandZs=VisionEgg.Core.Viewport(screen=screen, size=screen.size, stimuli=[textREAD,textREADz,
                                                                                         textMOVE,textMOVEz,
                                                                                         textATTENTION,textATTENTIONz,
                                                                                         textSTROOP,textSTROOPz,
                                                                                         textTRAILSB,textTRAILSBz,
                                                                                         textTRAILSA,textTRAILSAz,
                                                                                         textVISUOSPATIAL,textVISUOSPATIALz,
                                                                                         textMATH,textMATHz,
                                                                                         textORIENTATION,textORIENTATIONz,
                                                                                         textINCIDENTAL,textINCIDENTALz,
                                                                                         textSTUDIED,textSTUDIEDz,
                                                                                         textTOTALtimeMIN,textZz])
    viewportTEXTSCORES = VisionEgg.Core.Viewport(screen=screen, size=screen.size, stimuli=[textA, textB, textC, textD, textE, textF, textG, textH, textI, textTOTAL])
   ## <update for MAY-2020> <to 0-3-9>
    viewportTEXT2 = VisionEgg.Core.Viewport(screen=screen, size=screen.size, stimuli=[text1, text2, text3, text4, text5, textposttest50, textposttest60, textposttest65, textposttest70, textposttest75, textposttest80, textposttest85, textposttest90])
   ## viewportTEXT2 = VisionEgg.Core.Viewport(screen=screen, size=screen.size, stimuli=[text1, text2, text3, text4, text5])
   ## </update for MAY-2020> <to 0-3-9>  
    viewport.draw()
    viewportTIMESandZs.draw()
    viewportTEXTSCORES.draw()
    viewportTEXT2.draw()
    image = VisionEgg.Core.Screen.get_framebuffer_as_image(screen, buffer='back', format=6407, position=(0, 0), anchor='lowerleft', size=None)
    image.save("%s_dataSUMMARY.jpg"%filename)
    if ScreenNumber > 9996:
        image.save("_LATEST_SUBJECT.jpg")
    ###
    ###
    ### and wipe logs again to be sure...
    WordCount=0
    InstructionTime=-1
    YearAnswer=0
    TrialTime=-1
    MonthAnswer=0
    PENALTIES=0
    ERRORS=0
    Choice=[" "]
    ## fresh logs with each initialization
##    ATTENTION_LOG=ATTENTION_BLANK
##    #global ATTENTION_LOG
##    SPATIAL_LOG=SPATIAL_BLANK
##    #global SPATIAL_LOG
##    ORIENTATION_LOG=ORIENTATION_BLANK
##    #global ORIENTATION_LOG
##    MEMORY_LOG=MEMORY_BLANK
##    #global MEMORY_LOG
##    MATH_LOG=MATH_BLANK
##    #global MATH_LOG
##    TRAILS_LOG=TRAILS_BLANK
##    #global TRAILS_LOG
##    STROOP_LOG=STROOP_BLANK
##    #global STROOP_LOG
##    READING_SPEED_LOG=READING_SPEED_BLANK
##    #global READING_SPEED_LOG
##    MOTOR_SPEED_LOG=MOTOR_SPEED_BLANK
    #global MOTOR_SPEED_LOG
    ##<0-3-9>
    explanation="NA"
    CDRzero="NA"
    CDRzeroPfive="NA"
    CDRatLEASTone="NA"
    posttest50="NA"
    posttest60="NA"
    posttest65="NA"
    posttest70="NA"
    posttest75="NA"
    posttest80="NA"
    posttest85="NA"
    posttest90="NA"
    ##</0-3-9>
    VERY_BEGINNING_NUMERIC="NA"
    VERY_END_NUMERIC="NA"
    SUM_TIME_SPENT_MS="NA"
    VERY_BEGINNING="NA"
    VERY_END="NA"
    MS_PER_WORD="NA"
    MS_PER_WORD_Z="NA"
    MS_PER_PRESS="NA"
    MS_PER_PRESS_Z="NA"
    MS_ATTENTION="NA"
    MS_ATTENTION_Z="NA"
    ATTENTION_TIME="NA"
    MS_STROOP="NA"
    MS_STROOP_Z="NA"
    USEFULsum="NA"
    USEFULn="NA"
    MS_TRAILSB="NA"
    MS_TRAILSB_Z="NA"
    MS_TRAILSA="NA"
    MS_TRAILSA_Z="NA"
    MS_VISUOSPATIAL="NA"
    MS_VISUOSPATIAL_Z="NA"
    VISUOSPATIAL_TIME="NA"
    MS_MATH="NA"
    MS_MATH_Z="NA"
    MS_ORIENTATION="NA"
    MS_ORIENTATION_Z="NA"
    ORIENTATION_TIME="NA"
    MS_INCIDENTAL="NA"
    MS_INCIDENTAL_Z="NA"
    INCIDENTAL_TIME="NA"
    MS_STUDIED="NA"
    MS_STUDIED_Z="NA"
    USEFUL_z_scoreTIME="NA"
    ATTENTION_SUM="NA"
    SPATIAL_SUM="NA"
    INCIDENTAL_SUM="NA"
    MATH_SUM="NA"
    ORIENTATION_SUM="NA"
    STUDIED_SUM="NA"
    textREAD=Text(text="NA",color=(0,0,0),position=(215,70),font_size=24,anchor='center')
    textREADz=Text(text="NA",color=(0,0,0),position=(215,22),font_size=24,anchor='center')
    textMOVE=Text(text="NA",color=(0,0,0),position=(348,70),font_size=24,anchor='center')
    textMOVEz=Text(text="NA",color=(0,0,0),position=(348,22),font_size=24,anchor='center')
    textATTENTION=Text(text="NA",color=(0,0,0),position=(66,560),font_size=24,anchor='upperright')
    textATTENTIONz=Text(text="NA",color=(0,0,0),position=(125,560),font_size=24,anchor='upperright')
    textSTROOP=Text(text="NA",color=(0,0,0),position=(66,522),font_size=24,anchor='upperright')
    textSTROOPz=Text(text="NA",color=(0,0,0),position=(125,522),font_size=24,anchor='upperright')
    textTRAILSB=Text(text="NA",color=(0,0,0),position=(66,484),font_size=24,anchor='upperright')
    textTRAILSBz=Text(text="NA",color=(0,0,0),position=(125,484),font_size=24,anchor='upperright')
    textTRAILSA=Text(text="NA",color=(0,0,0),position=(66,446),font_size=24,anchor='upperright')
    textTRAILSAz=Text(text="NA",color=(0,0,0),position=(125,446),font_size=24,anchor='upperright')
    textVISUOSPATIAL=Text(text="NA",color=(0,0,0),position=(66,408),font_size=24,anchor='upperright')
    textVISUOSPATIALz=Text(text="NA",color=(0,0,0),position=(125,408),font_size=24,anchor='upperright')
    textMATH=Text(text="NA",color=(0,0,0),position=(66,370),font_size=24,anchor='upperright')
    textMATHz=Text(text="NA",color=(0,0,0),position=(125,370),font_size=24,anchor='upperright')
    textORIENTATION=Text(text="NA",color=(0,0,0),position=(66,332),font_size=24,anchor='upperright')
    textORIENTATIONz=Text(text="NA",color=(0,0,0),position=(125,332),font_size=24,anchor='upperright')
    textINCIDENTAL=Text(text="NA",color=(0,0,0),position=(66,294),font_size=24,anchor='upperright')
    textINCIDENTALz=Text(text="NA",color=(0,0,0),position=(125,294),font_size=24,anchor='upperright')
    textSTUDIED=Text(text="NA",color=(0,0,0),position=(66,256),font_size=24,anchor='upperright')
    textSTUDIEDz=Text(text="NA",color=(0,0,0),position=(125,256),font_size=24,anchor='upperright')
    textTOTALtimeMIN = Text(text="NA",color=(0,0,0),position=(79,178),font_size=28,anchor='center')
    textZz=Text(text="NA",color=(0,0,0),position=(81,22),font_size=24,anchor='center')
    textA = Text(text="NA",color=(0,0,0),position=(282,551),font_size=24,anchor='center')
    textB = Text(text="NA",color=(0,0,0),position=(282,513),font_size=24,anchor='center')
    textC = Text(text="NA",color=(0,0,0),position=(282,475),font_size=24,anchor='center')
    textD = Text(text="NA",color=(0,0,0),position=(282,437),font_size=24,anchor='center')
    textE = Text(text="NA",color=(0,0,0),position=(282,399),font_size=24,anchor='center')
    textF = Text(text="NA",color=(0,0,0),position=(282,361),font_size=24,anchor='center')
    textG = Text(text="NA",color=(0,0,0),position=(282,323),font_size=24,anchor='center')
    textH = Text(text="NA",color=(0,0,0),position=(282,285),font_size=24,anchor='center')
    textI = Text(text="NA",color=(0,0,0),position=(282,247),font_size=24,anchor='center')
    textTOTAL = Text(text="NA",color=(0,0,0),position=(282,178),font_size=28,anchor='center')
    ###
    ###
    ###
    ###
    screen.clear()
    #### </summary image>
    ##
    ##
    ##
    os.chdir(BASEPATH)












