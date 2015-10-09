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

def createVoiceAttackCommand( commandname, actionKeyCodes, command, reply):
    "Creates a new standard command"
    commandNodeFile = ET.parse(parsePath(config["files"]["commandtemplate"]))
    commandNode = commandNodeFile.getroot()
    # Description of the voicecommand will be the
    # action name from custom.binds of Elite
    voiceActionDescription=commandNode.find("Description")
    if voiceActionDescription is None:
        voiceActionDescription = ET.Element("Description")
    else:
        voiceActionDescription.text = commandname
        ET.SubElement(commandNode, voiceActionDescription)    
    # When i say...
    voiceAction=commandNode.find("CommandString")
    voiceAction.text=command
    voiceActionId=commandNode.find("Id")
    voiceActionId.text=str(uuid.uuid4())

    # ..you say...
    commandActionNodes=commandNode.findall("./ActionSequence/CommandAction")
    for commandAction in commandActionNodes:
        actionType=commandAction.find("ActionType")
        actionType = getElementText(actionType)
        if actionType == "PressKey":
            keyCodesNode=commandAction.find("KeyCodes")
            for actionKeyCode in actionKeyCodes:
                if actionKeyCode is not None:
                    unsignedShortNode = ET.Element("unsignedShort")
                    unsignedShortNode.text=actionKeyCode
                    keyCodesNode.append(unsignedShortNode)
            keyId=commandAction.find("Id")
            keyId.text=str(uuid.uuid4())
        elif actionType == "Say":
            if reply is None:
                reply = command.split(";")
                reply = reply[0]
            sayAction=commandAction.find("Context")
            sayAction.text="OK, "+reply+";"+"Verstanden, "+reply
            sayId=commandAction.find("Id")
            sayId.text=str(uuid.uuid4())
        elif actionType == "MouseAction":
            print("XXX: MouseAction")
        else:
            printError("Couldn't create Action")
    return commandNode

def getReplyAcceptString(vaMapping,action):
    # Elite has different keymappings for open space and landing situations.
    # But the voicecommands will always be the same. You will always say "forward" if you want your ship to move forward.
    # We will map the "normal" voicecommand to the "landing" key.
    if action[-8:] == "_Landing":
        action = action[:-8]
    try:        
        # device = map["Device"]
        actionNode = vaMapping.find(action)
        replyNode = actionNode.find("ReplyAccept")
        reply = getElementText(reply)
    except:
        reply = None
    return reply

def getElementText(elementNode):
    elementNode = elementNode.text
    elementNode = elementNode.replace("\t","")
    elementNode = elementNode.replace("\n","")
    elementNode = elementNode.strip(" ")
    return elementNode

def getCommandString(vaMapping,action):
    # Elite has different keymappings for open space and landing situations.
    # But the voicecommands will always be the same. You will always say "forward" if you want your ship to move forward.
    # We will map the "normal" voicecommand to the "landing" key.
    if action[-8:] == "_Landing":
        action = action[:-8]
    try:        
        # device = map["Device"]
        actionNode = vaMapping.find(action)
        command = actionNode.find("CommandString")
        # remove tabs and newlines
        command = getElementText(command)
    except:
        printError("commands:\tVoicecommand not set for '{0}'!".format(action))
        command = None
    return command

def getKeycode(device,keycodes,keyname):
    keyNode = keycodes.find(keyname)
    if keyNode is None:
        printError("keycodes:\tNot found:\t{1} for device '{0}'".format(device,keyname))
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
    actionKeyCodes= []
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
        commandString = getCommandString(vaMapping,action)
        replyAcceptString = getReplyAcceptString(vaMapping,action)
        keyName = getKey(keyNode)         
        if keyName is "":
            printWarning("eliteconfig:\tKey not set:\t{0}".format(action))
            #setRandomKey(keyNode)
        else:
            modifiers = keyNode.findall("./Modifier")
            if modifiers is not None:
                for modifierKey in modifiers:
                    modifierKeyName = getKey(modifierKey)
                    actionKeyCodes.append(getKeycode(device, keycodes, modifierKeyName))       
            actionKeyCodes.append(getKeycode(device, keycodes, keyName))
        if len(actionKeyCodes)>0:
            commandNode = createVoiceAttackCommand(action, actionKeyCodes, commandString, replyAcceptString)
            commands.append(commandNode)


vaProfileFile.write(parsePath(config["files"]["output"]), encoding="utf-8")
