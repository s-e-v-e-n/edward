import xml.etree.ElementTree as ET
import uuid
import os
import json
import re
import configparser

config = configparser.RawConfigParser()
config.read("config.ini")

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
            print("MouseAction not implemented yet")
        else:
            print("Couldn't create Action")
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
        print("Edvard: No CommandString for '{0}'".format(action))
        command = None
    return command

def getKeycode(device,keycodes,keyname):
    keyNode = keycodes.find(keyname)
    if keyNode is None:
        print("Edvard: Keycode not found:\t{1} for device '{0}'".format(device,keyname))
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

def getKeyboardKeyNode(keyconfig):
    # Get the setting with a keyboard device
    primaryDevice = getDevice(keyconfig.find("Primary"))
    secondaryDevice = getDevice(keyconfig.find("Secondary"))
    if primaryDevice == "Keyboard":
        setting = "Primary"
    elif secondaryDevice == "Keyboard":
        setting = "Secondary"
    else:
        if primaryDevice == "{{NoDevice}}".format() and secondaryDevice == "{{NoDevice}}".format():
            print("Elite: No key configured for \t'{0}'".format(keyconfig.tag))
        return None
        # Get the "Secondary" mapping from the elite config
    keyNode = keyconfig.find(setting)
    return keyNode

def getKeyNames(keyconfig):
    keyNode = getKeyboardKeyNode(keyconfig)
    if keyNode is None:
        return None

    # get the keys
    keyName = getKey(keyNode)

    modifiers = keyNode.findall("./Modifier")
    # Add modifier key if there is one configured
    modifierKeyName = None
    if modifiers is not None:
        for modifierKey in modifiers:
            modifierKeyName = getKey(modifierKey)

    # return the key
    return keyName, modifierKeyName       

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


# Load Elite Configuration
eliteCustomBinds = parsePath(config["files"]["elite"])
eliteConfigFile = ET.parse(eliteCustomBinds)
eliteConfig = eliteConfigFile.getroot()

# Load VoiceAttack Profile Template
vaProfileFile = ET.parse(parsePath(config["files"]["profiletemplate"]))
vaProfile = vaProfileFile.getroot()
commands = vaProfile.find("Commands")

# Load Edvard command configuration file
vaMappingFile = ET.parse(parsePath(config["files"]["commands"]))
vaMapping = vaMappingFile.getroot()

# Load keycodes
keycodesFile = ET.parse(parsePath(config["files"]["keycodes"]))
keycodes = keycodesFile.getroot()

# iterate through every action in eliteconfig
for keyconfig in eliteConfig:
    # Check if it is a digital input else skip
    keyNode = keyconfig.find("Primary") 
    if keyNode is None:
        continue

    keyNames = getKeyNames(keyconfig)
    # When its a digital input create a voiceattack command
    if keyNames:
        # Initialize KeyCodes for Voiceattack
        actionKeyCodes= []
        # Get the actionname from the elite config
        action = keyconfig.tag
        if keyNames[1] is not None:
            actionKeyCodes.append(getKeycode("Keyboard", keycodes, keyNames[1]))       
        # Add key
        actionKeyCodes.append(getKeycode("Keyboard", keycodes, keyNames[0]))

        # Get the voicecommand(context)
        commandString = getCommandString(vaMapping,action)
        replyAcceptString = getReplyAcceptString(vaMapping,action)
        # We have a key and a voicecommand string, create the voiceattack command
        if commandString is not None:
            commandNode = createVoiceAttackCommand(action, actionKeyCodes, commandString, replyAcceptString)
            commands.append(commandNode)


vaProfileFile.write(parsePath(config["files"]["output"]), encoding="utf-8")
