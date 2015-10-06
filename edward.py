import xml.etree.ElementTree as ET
import uuid
import os
import json
import re
import configparser

config = configparser.RawConfigParser()
config.read("config.ini")

# class bcolors:
#     HEADER = '\033[95m'
#     OKBLUE = '\033[94m'
#     OKGREEN = '\033[92m'
#     WARNING = '\033[93m'
#     FAIL = '\033[91m'
#     ENDC = '\033[0m'
#     BOLD = '\033[1m'
#     UNDERLINE = '\033[4m'

class bcolors:
    HEADER = ''
    OKBLUE = ''
    OKGREEN = ''
    WARNING = ''
    FAIL = ''
    ENDC = ''
    BOLD = ''
    UNDERLINE = ''

def printWarning(message):

    print(bcolors.WARNING, "\tWarning:\t",message,bcolors.ENDC)

def printError(message):
    print(bcolors.FAIL, "\tError  :\t",message,bcolors.ENDC)

def printBoldError(message):
    print(bcolors.FAIL,bcolors.BOLD, "\tError:\t",message,bcolors.ENDC)

def createVoiceAttackCommand( commandname, keycode, context):
    "Creates a new standard command"
    commandNodeFile = ET.parse(parsePath(config["files"]["commandtemplate"]))
    commandNode = commandNodeFile.getroot()
    commandActionNode=commandNode.findall("./ActionSequence/CommandAction")

    # When i say...
    commandNameNode=commandNode.findall("./CommandString")
    commandNameNode[0].text=context
    commandNameNodeId=commandNode.findall("./Id")
    commandNameNodeId[0].text=str(uuid.uuid4())
    # ..you say...
    sayAction=commandActionNode[1].findall("./Context")
    sayAction[0].text="OK, "+context+";"+"Verstanden, "+context
    sayId=commandActionNode[1].findall("./Id")
    sayId[0].text=str(uuid.uuid4())
    # Description of the voicecommand will be the
    # action name from custom.binds of Elite
    descriptionNameNode=commandNode.find("Description")
    if descriptionNameNode is None:
        descriptionNameNode = ET.Element("Description")
    else:
        descriptionNameNode.text = commandname
        ET.SubElement(commandNode, descriptionNameNode)    

    keyAction=commandActionNode[0].findall("./KeyCodes/unsignedShort")
    keyAction[0].text=keycode
    keyId=commandActionNode[0].findall("./Id")
    keyId[0].text=str(uuid.uuid4())
    return commandNode

def getContext(vaMapping,action):
    # Elite has different keymappings for open space and landing situations.
    # But the voicecommands will always be the same. You will always say "forward" if you want your ship to move forward.
    # We will map the "normal" voicecommand to the "landing" key.
    if action[-8:] == "_Landing":
        action = action[:-8]
    try:        
        # device = map["Device"]
        context = vaMapping.find(action)
        # remove tabs and newlines
        context = context.text
        context = context.replace("\t","")
        context = context.replace("\n","")
        context = context.strip(" ")
    except:
        printError("Voicecommand not set for '{0}'! Edit binds.xml".format(action))
        context = None
    return context

def getKeycode(keycodes,keyname):
    keyNode = keycodes.find(keyname)
    if keyNode is None:
        printError("Keyname not found:\t{0}".format(keyname))
        keyCode=None
    else:
        keyAttribs = keyNode.attrib
        keyCode = keyAttribs["code"]
    return keyCode

def getKey(element):
    keyNode = element.attrib
    key = keyNode["Key"]
    return key

def getDevice(element):
    deviceNode = element.attrib
    device = deviceNode["Device"]
    return device

def parsePath(path):
    envVarDelimiter="%"
    path=path.split(envVarDelimiter)
    pathStr=""
    if len(path)>1:
        i=0
        while i<len(path)-1:
            envVar=os.environ[path[i+1]]
            pathStr=os.path.join(pathStr,envVar)
            pathStr=pathStr+path[i+2]
            i=i+2
    else:
        pathStr=path[0]
    return os.path.normpath(pathStr)

eliteCustomBinds = parsePath(config["files"]["elite"])
eliteConfigFile = ET.parse(eliteCustomBinds)
eliteConfig = eliteConfigFile.getroot()

vaProfileFile = ET.parse(parsePath(config["files"]["profiletemplate"]))
vaProfile = vaProfileFile.getroot()
commands = vaProfile.find("Commands")

vaMappingFile = ET.parse(parsePath(config["files"]["commands"]))
vaMapping = vaMappingFile.getroot()

keycodesFile = ET.parse(parsePath(config["files"]["keycodes"]))
keycodes = keycodesFile.getroot()

# iterate through every action in eliteconfig
for keyconfig in eliteConfig:
    # get the actionname from the elite config
    action = keyconfig.tag
    # get the primary button mapping from the elite config
    keyNode = keyconfig.find("Primary")
    keyCode= None
    isAButton = False
    isKeyboard = False
    isGamepad = False
    # There is a "Primary" element so it must be a button
    if keyNode is not None:
        isAButton = True
        device  = getDevice(keyNode)
        if device is "Keyboard":
            isKeyboard = True
        if device is "GamePad":
            isGamepad = True

    # when its a button
    if isAButton is True:
        # Get the voicecommand(context)
        context = getContext(vaMapping,action)
        keyName = getKey(keyNode)
        if keyName is "":
            printWarning("No key configured:\t{0}".format(action))
        else:
            keyCode = getKeycode(keycodes, keyName)
        if keyCode is not None:        
            command = createVoiceAttackCommand(action, keyCode, context)
            commands.append(command)


vaProfileFile.write(parsePath(config["files"]["output"]), encoding="utf-8")
