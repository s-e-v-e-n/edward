# edvard

Erstellen eines Voice-Attack Profils unter Verwendung der Elite Dangerous Konfiguration.
========================================================================================

Zuerst möchte ich klarstellen, dass dieses Projekt ein persönliches Projekt von mir ist. Auch wenn ich hier von den Markennamen **Voice Attack** oder **Elite Dangerous** gebrauch mache, habe ich nichts zu tun mit diesen Marken oder deren Markeninhaber. Diese Software ist in keiner Weise etwas offizielles von den genannten Marken oder deren Rechteinhaben und ist nicht annähernd die Qualität derer Software-Produkte.

Durch die Nutzung dieser Software, akzeptieren Sie, dass Sie das in vollem Umfang auf eigenes Risiko tun.

IN KEINEM FALL SIND DIE AUTOREN ODER COPYRIGHTINHABER FÜR ANSPRÜCHE ODER SCHÄDEN HAFTBAR, DIE IN VERBINDUNG MIT DER SOFTWARE ODER DEREN NUTZUNG ODER ANDEREN HANDLUNGEN MIT DER SOFTWARE ENTSTANDEN IST.


==========
QUICKSTART
==========

    - Release herunterladen und entpacken.
    - edvard.exe doppelklicken.
    - Die generierte edvard.vap-Datei in Voiceattack importieren.
    - Elite spielen und dabei den Computer anschreien.

Ob eine Weiterentwicklung an diesem Projekt eine gute Idee ist, könnt Ihr mir mir hier zeigen -> https://www.paypal.me/sevengear


Story:
======

Wie viele andere auch habe ich [Elite Dangerous] (https://www.elitedangerous.com/) in der Kickstarter-Kampagne unterstützt. Traurig ist nur, dass ich bisher nicht viel Zeit hatte zum spielen.

Ich habe drei Mal versucht [Elite Dangerous] (https://www.elitedangerous.com/) anzufangen. Im ersten und zweiten Versuch wollte ich es unter Verwendung der Oculus Rift DK2 spielen. Mit dem HMD auf meinem Kopf bemerkte ich bald, dass ich das viel verwendete [Voice Attack] (http://www.voiceattack.com/) brauchte, weil ich meine Tastatur nicht mehr sehen konnte.

Da keiner meiner Rechner stark genug war, um die Schönheit von Elites Grafik und das stereoskopische Rendering für die DK2 zu meistern, hörte ich bald wieder auf zu spielen. Mangel an GPU-Leistung ist kein Spaß im VR.

Vor kurzem hatte ich aber wieder etwas Zeit und wollte einfach nur spielen und so gab ich Elite eine weitere Chance auf einem normalen Bildschirm, ohne DK2 oder [Voice Attack] (http://www.voiceattack.com/), ganz oldschool.


Um es kurz zu machen:
---------------------

Die Lernkurve für die Tonnen von Tasten, die man sich für [Elite Dangerous] (https://www.elitedangerous.com/)  merken muss ist eine bisschen hoch um mal schnell was zu spielen. Also fing ich an, über das Internet nach Tutorials zur Konfiguration von [Voice Attack] (http://www.voiceattack.com/) zu suchen, nicht zuletzt um den Spaßfaktor zu steigern.

Stellt sich heraus, es würde mehrere Stunden dauert, nur um ein Basis-Setup zu haben, denn man muss in voiceattack eine ganze Menge Sachen zusammenklicken und immer wieder zwischen Elite und Voiceattack hin und herwechseln um eine Konfiguration zu finden mit der man zurecht kommt.


Das Hauptproblem:
-----------------

Ich fand eine Menge Leute im Internet die Elite spielen und Stunden und Tage und sogar Wochen und Monate damit verbringen, um ihr VoiceAttack so zu konfigurieren, dass es perfekt zu ihren Bedürfnissen und Tastaturbelegung in Elite passt. Hinzu kommt, dass einige mittels VoiceAttack komplizierte Logik hinzukonfigurieren um Kommandosequenzen welche häufig verwendet werden in kurzen Sprachkommandos zusammen zu fassen.

Einige dieser Leute sind so freundlich, ihre Einstellung, mit der sie schon Stunden verbracht haben zu teilen. So können Sie diese einfach herunterladen und deren VoiceAttack-Profil importieren und Ihre Elite-Einstellungen mit deren Einstellungen überschreiben und schon kann es losgehen.

Das Problem ist nur, es ist DEREN Setup, was nicht bedeutet, dass es genau Ihren Bedürfnissen entspricht. So dass Sie schließlich beginnen, die Tastenbelegung in Elite neu zu definieren. Aber dann stimmen diese wieder nicht mit den Befehlen in VoiceAttack überein und man endet immer wieder beim hin und her um alles neu einzustellen.

Selbst wenn Sie irgendwann fertig sind, mit dem nächsten Update der Konfiguration, die Sie herunterladen und importieren beginnt das Spiel wieder von vorn.


Ziel
====

Die Befehle in Elite sollten auf die Sprachbefehle von VoiceAttack direkt gebunden werden können. Unabhängig von den Geräten und deren Tasten und Knöpfe, die sie in ihrer persönlichen Elite Konfigration verwenden.

Eine erstes VoiceAttack Setup für Anfänger sollte nicht länger als ein paar Minuten dauern.

Teilen und aktualisieren von heruntergeladenen VoiceAttack Konfigurationen sollte machbar sein, ohne die bestehende
Konfiguration von Elite zu verändern.


Lösung
======

1. Binden von Elite-Kommandos direkt an ein Wort oder einen Satz.

    Bearbeiten Sie dazu die Datei **commands.xml** mit einem Editor. Im Beispiel unten sehen Sie, wie das Elite-Kommando "ForwardKey" an das Voicecommand "vorwärts" gebunden wird.

    ::

        <ForwardKey>
            vorwärts
        </ ForwardKey>

2. Erstellen Sie ein neues VoiceAttack-Profil.
    
    Führen sie dazu edvard.exe aus oder klicken Sie doppelt darauf. Eine edvard.vap-Datei wird erzeugt.

3. Importieren Sie das VoiceAttack Profil (edvard.vap).
    
    Schauen Sie sich die VoiceAttack Hilfe an, wenn Sie nicht wissen, wie man das macht.

4. Spielen sie Elite Dangerous mit Ihrem neuen VoiceAttack Profil.


Was sind die anderen Dateien?
-----------------------------

config.ini - enthält die Pfade und Dateien die standardmäßig verwendet werden

defaultprofile.vap - Dies ist die Basis des erzeugten Profil mit den globalen Einstellungen. Ändern Sie diese nach belieben, wenn Sie wissen was sie tun.

defaultcommand.xml - Das ist der Ausschnitt, der als neues Voicecommand eingesetzt wird. Es enthält eine Actionsequence die zuerst die Taste drückt und dann die Text-to-Speech-Engine verwendet um Ihnen mitzuteilen welcher Befehl verstanden wurde. Dazu wird einfach der im commands.xml festgelegte Text verwendet und ein "OK,..." bzw. "Verstanden,..." vorangeführt.

keycodes.xml - Elite verwendet Namen für die Tasten auf der Tastatur, voiceattack verwendet deren entsprechende (ASCII-Codes).



--------------------------------------------------------------------------------------------------------------
--------------------------------------------------------------------------------------------------------------
--------------------------------------------------------------------------------------------------------------

Create a Voice Attack Profile by using the Elite Dangerous Custom key binds.
============================================================================


First i want to make clear that this project is a personal project of mine. Even though i mention the brands **Voice Attack** or **Elite Dangerous** so that people can search and find this project, i have nothing to do with those trademarks or their trademark holders and this software is in no wa a official thing from those companies and no where near the quality of those software products.

By using this software you fully accept to do that at your own risk.

IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.


Story:
======

As many others did, i backed [Elite Dangerous](https://www.elitedangerous.com/). Sad enough i don't have much time for gaming, i might say i've become a casual gamer.

I tried to start playing [Elite Dangerous](https://www.elitedangerous.com/) three times now. In the first and second try i was playing it by using the Oculus Rift DK2. With the HMD on, i soon noticed that i needed that [Voice Attack](http://www.voiceattack.com/) everybody else was using, because i couldn't see my keyboard.

Since none of my machines were powerful enough to handle the beauty of Elites graphics AND the stereoscoping rendering for the DK2, i stopped playing the game soon. Lack of GPU power is no fun in VR.

But recently i had a little free time again and i just wanted to play something. So i gave Elite another chance on a normal screen, without [Voice Attack](http://www.voiceattack.com/) , oldschool.


Long story short:
-----------------

The learning curve for the tons of keys you need to remember in [Elite Dangerous](https://www.elitedangerous.com/) is kind of high IMHO, so i started to look through the internet for tutorials on how to configure [Voice Attack](http://www.voiceattack.com/) to make things more fun.

Turns out it would takes several hours just to have a basic setup, because you would need to click a ton of things in voiceattack and go back and forth into Elite and Voiceattack to get a working setup.


The Main Problem:
-----------------

I found a lot of people on the internet playing Elite and spending hours and days and even weeks and months to configure their Voice Attack so it perfectly matches their needs and keybindings in Elite. On top of that they configure some complicated logic in a macro style with voiceattack which helps them getting along with commandsequences they frequently have to use in Elite.

Some of those people are kind enough to share their setup, which they've spent hours with, so you can just download and import their voiceattack-profile and overwrite your Elite-settings with theirs and you're good to go.

The problem is, it's THEIR setup which might not be exactly matching YOUR needs. So you eventually start to redefine the keys in Elite. But then that doesn't match to the commands of the imported voiceattack anymore and you go back and forth again. Even when you're done, with the next update of said voicattack logics that you download and import into your voiceattack setup, you still have to readjust everything all over again.


Goal
====

The commands in Elite should be bound to the spoken commands of voiceattack directly. Independent of the devices and their keys and buttons which they are related to in the individual elite configration.

A first voicecommand setup for newbies should not take longer than a few minutes.

A updated or downloaded voicecommand configuration should be usable without tampering the existing
configuration of Elite.


Solution
========

1. Bind Elite commands directly to a word or sentence.

    Edit the **commands.xml** file using a editor. In the sample of that file below you see the elite command "ForwardKey" is bound to the voicecommand "vorwärts", which is the german word for "forward".

    ::

        <ForwardKey>
            vorwärts
        </ForwardKey>

2. Generate a new VoiceAttack Profile.
    
    Run edvard.exe or doubleclick on it. A edvard.vap file should be generated.

3. Import the VoiceAttack Profile.
    
    Have a look at the VoiceAttack Help if you don't know how to do that.

4. Play Elite Dangerous with your new VoiceAttack Profile.


What are the other files for?
-----------------------------

config.ini - contains the paths and files to use by default

defaultprofile.vap - This is the base of the generated Profile containing the global settings. Modify if you know what you're doing.

defaultcommand.xml - That's the snippet which is inserted as a new voicecommand. It contains a actionsequence which first presses the key and then uses the text-to-speech engine to repeat back to you what that command was that it has understood.

keycodes.xml - Elite uses names for the keys on the keyboard, voiceattack uses their corresponding (ascii)codes 
