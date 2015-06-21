# Python Script for OGame
##### A Python script to play the OGame browser game using Mechanize and Beautifulsoup

This is the second iteration of my Python OGame bot. The Program can login to the game, extract building and resource levels from the game's HTML and send build commands.
As an improvement from Version 1.0 I've completely rewritten a lot of the code to:
* Be Object Oriented: The last version was relatively messy in terms of interfacing. This time around, building an object is as simple as calling that object's build function.
* Utilize Regular Expressions: Searching HTML is messy. Especially the way I went first, using a lot of .replace() statements and a split that usually required data to be in a very specific location. This time around the search algorithms are a lot more robust.

Here is an image showcasing the hierarchy of files:
![Hierarchy Image](https://github.com/Mixmorks/Python-OGame-Bot/blob/master/Hierarchy.png "")

##Status:
Turns out OGame is using Javascript in its Galaxy view. There may be ways to send fleets to random locations but I haven't investigated the issue further. As of this point the Bot is no longer in development.

##Abilities:
This bot can login, scrape building and research data, calculate whether enough resources are available to build a certain item and send a build command. This script cannot build defenses or fleets, scan other players or attack.
