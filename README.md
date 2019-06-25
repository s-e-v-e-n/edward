

Create a Voice Attack Profile by using the Elite Dangerous Custom key binds.
============================================================================


What?
=====
You can spend a lot of time configuring your input options in [Elite Dangerous](https://www.elitedangerous.com/).
You can spend a lot of time adjusting [Voice Attack](http://www.voiceattack.com/)  to your own Elite Dangerous configuration.
Sometimes people share their voiceattack profiles so others don't have to go through the same hassle, which is really nice.
But the problem is that this is so specific to your own hardware and needs, that one has to spend time an equal amount of time adjusting everything according to their own needs.


Why?
====

Map the commands of Elite dangerous instead of their key or button configuration to the voiceattack command phrases.

This enables newbies to be up and running in very short time.

This makes shared or updated voicecommand profiles directly usable.


How?
====

If you run the edvard.exe it will take your custom Elite Dangerous Input Configuration and create a Voiceattack profile that you can import.

The words or sentences you actually have to say to voiceattack so it can fire the command in Elite are configured in the **commands.xml**.

The commands.xml is already filled with a lot of elite dangerous commands like "SetSpeed100" or "ToggleFlightAssist".

1. Configure voicecommands and responses by editing the **commands.xml** file using a decent texteditor.

     Here is an example of a command mapping.   

    ::

        <SetSpeed100>
            <CommandString>Engines to one hundred percent;Engage;Full Throttle</CommandString>
            <ReplyAccept></ReplyAccept>
        </SetSpeed100>

     The Elite command is "SetSpeed100".
     You can configure multiple voice commands inside the "CommandString" by separating them with a semicolon.
     If you have only one voice command for this you don't need the semicolon.
     The "ReplyAccept" is the text that will be spoken by your text-to-speech engine so that you have some kind of feedback.
     If you leave it empty like in this example it will take the first CommandString, in this case it would say "Engines to one hundred percent".


2. Generate a new VoiceAttack Profile.
    
    Run "python edvard.py" inside a command shell (cmd.exe). A edvard.vap file should be generated.

3. Import the edvard.vap VoiceAttack Profile.
    
    Have a look at the VoiceAttack Help if you don't know how to do that.

Understanding the output of edvard
----------------------------------
Run "python edvard.py" inside a command shell (cmd.exe) and you will see output.

The commands in elite may change or some more may be added over time.
As soon as edvard finds a command in the elite configuration which is not in your commands.xml it will output something like...

    ::

        Edvard: No CommandString for 'SAAThirdPersonYawLeftButton'

So in this case the command mapping for SAAThirdPersonYawLeftButton is missing so you would have to add something like this to your commands.xml and then run edvard again.
    ::

        <SAAThirdPersonYawLeftButton>
            <CommandString>third person yaw left</CommandString>
            <ReplyAccept></ReplyAccept>
        </SAAThirdPersonYawLeftButton>

The following warning tells you that there is no key configured for "SAAThirdPersonYawLeftButton" in Elite, so we can't map any key to the voiceattack commands. You have to configure a key for that command in Elite if you want to use it. Afterwards run edvard again.
    ::

        Elite: No key configured for 'SAAThirdPersonYawLeftButton'


What are the other files for?
-----------------------------

config.ini - contains the paths and files to use by default

defaultprofile.vap - This is the base of the generated Profile containing the global settings. Modify if you know what you're doing.

defaultcommand.xml - That's the snippet which is inserted as a new voicecommand. It contains a actionsequence which first presses the key and then uses the text-to-speech engine to repeat back to you what that command was that it has understood.

keycodes.xml - Elite uses names for the keys on the keyboard, voiceattack uses their corresponding (ascii)codes 

Troubleshooting
===============

Problem
-------
FileNotFoundError: [Errno 2] No such file or directory: 'C:\\Users\\sschmid\\AppData\\Local\\Frontier Developments\\Elite Dangerous\\Options\\Bindings\\Custom.3.0.binds'

Solution
--------
You have to start Elite at least once and configure some command otherwise the keymappings file won't exist.
If you already did that then the version number in the file might be a different one. Just check the filename in the path and edit the config.ini accordingly.




Disclaimer
==========

I want to make clear that this project is a personal project of mine. Even though i mention the brands **Voice Attack** or **Elite Dangerous** so that people can search and find this project, i have nothing to do with those trademarks or their trademark holders and this software is in no way a official thing from those companies and no where near the quality of those software products.

By using this software you fully accept to do that at your own risk!

IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

