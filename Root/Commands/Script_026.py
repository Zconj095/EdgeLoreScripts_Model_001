
from Language_Early_Stage import *
MAKE,LIST,FOR,DATA
    LIST,CONTAINS,THE,FOLLOWING,DATA,["HEALTH_POINTS","MAGIC_POINTS","MANA_BAR"]
        DEFINE,HEALTH_POINTS,AS,['THE NUMBER FOR HEALTH POINTS A PLAYER HAS']
        THE,NUMBER,FOR,HEALTH_POINTS,IS,100
        END,COMMANDS
        DEFINE,MAGIC_POINTS,AS,['THE AMOUNT FOR MAGIC POINTS A PLAYER HAS']
        THE,NUMBER,FOR,MAGIC_POINTS,IS,40
        END,COMMANDS
        DEFINE,MANA_BAR,AS,['THE SIZE FOR MANA GIVEN AS A SPECIFIC AMOUNT MADE INTO A BAR FOR MANA']
        SET,MANA_BAR,SIZE,TO,CONTAIN,120,MANA,AT,MOST
        SET,MANA_BAR,SIZE,TO,CONTAIN,10,MANA,AS,MIN,AMOUNT
        END,COMMANDS
    END,LIST
END,COMMAND
