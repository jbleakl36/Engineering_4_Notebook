# Engineering_4_Notebook

&nbsp;

## Table of Contents
* [Raspberry_Pi_Assignment_Template](#raspberry_pi_assignment_template)
* [Onshape_Assignment_Template](#onshape_assignment_template)

&nbsp;

## Raspberry Pi Pico Introduction

### Assignment Description

We were tasked with our first usage of the pico. We were told to create code that made it's led blink. Furthermore we were tasked with  installing a plethora of add-ons so that we can be fully ready (coding wise) for engineering 4.

### Evidence 

https://iad.cdn.nv.instructuremedia.com/originals/o-52TLZN7UMcqafjYCqDzbSEVyDfiL8pEn/transcodings/t-539mNVqHdMku1Mc2vhbSRokPPmBtCNRk.mp4?&Expires=1694182799&Signature=TMsGiLxAXvQ99iV2gE5xxqTmTW1pqvxG8BCVtLrYbha1Pa3wCCSvQmM1tJpY67cdFzlhXHm2-F9GvLIl1XvdOEPsGz2vrGDPA~bzBObWVe2iyTNmEvIovnp6arrY3j4AyoKlvKnqGm6nSIxce3HBK7mk6IXsSvJwPgOMpy9iiac1U2aseY36qV2XdsnpoUSxV0nS9KwnTdC-uybbkOlIg3dvqy3iSA5rzqbGqpCRG0rEsBCi7Gc2I121uM5jgKW058PkmHnCamkyYdFFwMpb09EpOZrIijhY11sbjHYkcUvXUN4iwuHBM5YAMbLOHekwLLH9VXtG4EUfD3zBECHaVQ__&Key-Pair-Id=APKAJLP4NHW7VFATZNDQ

### Wiring

It's just the pico on a breadboard. 

### Code
https://github.com/jbleakl36/Engineering_4_Notebook/blob/main/raspberry-pi/LED_blink.py

### Reflection

The assingment was inherently simple, but challanges did arise. First off setting up everything was a bit of a hassle. There were a lot of moving pieces to follow. Luckily though the instructions were clear and easy to follow. The LED binking process was straightforward. I just need to refresh on my coding knowledge.


##  Launch Pad part 1

### Assignment Description
We were tasked with creating a countdown from 10 to 1 and at 0 we announce LIFTOFF! Also at the start we were tasked to
announce the question "Ready for liftoff?"

### Evidence

https://github.com/jbleakl36/Engineering_4_Notebook/assets/112979207/7757d7f3-c398-4efb-9771-40724eec4372


### Wiring
Literally zero wiring required.

### Code
https://github.com/jbleakl36/Engineering_4_Notebook/blob/main/raspberry-pi/launchPad1
### Reflection
This assigment was my first real re-introduction into coding again. I learned the use of the range function 
and discovered that you should print (10-x) instead of ((x-1), x=10). That was the one thing preventing me from progress.
Make sure to ask your friends who got the assingment working, they probably have a few tips they can give you.


##  Launch Pad part 2

### Assignment Description
This assignment adds to part 1, we were tasked with adding a red and green ight to the mix. The red light blinks every second
during countdown, while the green light blinks at liftoff.

### Evidence


https://github.com/jbleakl36/Engineering_4_Notebook/assets/112979207/25c4f317-ea2c-4034-b265-35092e9cbe3d



### Wiring

![Screenshot 2023-09-12 102330](https://github.com/jbleakl36/Engineering_4_Notebook/assets/112979207/ecf8e1a9-95c3-441e-8ecb-4bb63ffff780)


### Code
https://github.com/jbleakl36/Engineering_4_Notebook/blob/main/raspberry-pi/launchpad2

### Reflection
I found the addition of the lights to be slightly challanging. Although with some help the vision became clear.
I had trouble with my green LED because of the fact that it wasn't turning on (because it was dead). But after that
the only other problem I had was writing a proper "if" statement, I forgot the ":" at the end.



##  Launch Pad part 3

### Assignment Description
We were tasked to incorperate a button that starts the entire code from the last two parts.

### Evidence

https://github.com/jbleakl36/Engineering_4_Notebook/assets/112979207/f5446eb3-611d-4981-b285-10241400cae2

### Wiring


![Screenshot 2023-09-13 104229](https://github.com/jbleakl36/Engineering_4_Notebook/assets/112979207/1d2f5411-e085-4665-b7b0-52683f621c18)



### Code

https://github.com/jbleakl36/Engineering_4_Notebook/blob/main/raspberry-pi/launchpad3

### Reflection
This assingment was tricky at first, learning how to use a button again was definetely a blast
from the past. I redid parts of my code with the help of some friends, they had knowledge that
was vital for a proper redoing of some of my code. I learned some cool tidbits and got a larger
understanding of the coding language. Ask for help if you need it, trust me it's worth it.


##  Launch Pad part 4

### Assignment Description
We were tasked to activate a sevro and have it rotate 180 degrees at liftoff on top of the previous
three steps.

### Evidence



https://github.com/jbleakl36/Engineering_4_Notebook/assets/112979207/bc85481e-87f3-4b37-838e-b806fd88d9df



### Wiring


![W rizz](https://github.com/jbleakl36/Engineering_4_Notebook/assets/112979207/f760b84a-7678-4946-9506-0af155fbee21)



### Code

https://github.com/jbleakl36/Engineering_4_Notebook/blob/main/raspberry-pi/launchpad4normal

### Reflection
As of writing this, I have not yet done the spicy version. I feel close to completeing it but I'm falling behind
schedule. The non-spicy version of the assingment is incredibly easy. Just set up your servo and make the angle go
to zero when it is liftoff. I hope to return to the spicy version soon.

##  Crash Avoidance Part 1

### Assignment Description
We were tasked with using an accelerometer to report the x, y and z values to the serial monitor.
### Evidence



https://github.com/jbleakl36/Engineering_4_Notebook/assets/112979207/f4f0b12a-c54a-4914-ab18-9c694ec53293



### Wiring

![Crash Acc 1](https://github.com/jbleakl36/Engineering_4_Notebook/assets/112979207/2e22b971-111a-439c-bdad-39bf9151d937)


### Code

https://github.com/jbleakl36/Engineering_4_Notebook/blob/main/raspberry-pi/crashavoidance1

### Reflection
The task was simple. The assingment told me everything I needed to know. I didn't use an f string despite my intrege with
them. The hardest part was finding a method to loop the code. I did a simple x = 3, while x == 3 loop, it did the job well.


##  Crash Avoidance Part 2

### Assignment Description
We were tasked to add an LED that would turn on once the "Helicopter"/Breadboard was turned 90 degrees.
### Evidence

https://cvilleschools.instructure.com/courses/40384/assignments/539319/submissions/4669?preview=1&rand=266401#

### Wiring

![Crash Acc 2](https://github.com/jbleakl36/Engineering_4_Notebook/assets/112979207/8afc3c85-133c-4a48-a808-55c0af5ce57c)

### Code

https://github.com/jbleakl36/Engineering_4_Notebook/blob/main/raspberry-pi/carshavoidance2

### Reflection
This is the first assignment where you don't pug the pico to the computer. I found lots of trouble with my LED,
I put it in the wrong way putting ground into power and such. I learned how to use f strings which boaded well for
me. It was exciting to see this project finally work! We fixed other wiring issues that plauged my progress too.

##  Crash Avoidance Part 3

### Assignment Description
We were tasked with utilizing an OLED screen to broadcast the 3 various x, y, and z coordinates. Values are required
to be rounded to only 3 decimals.
### Evidence



### Wiring


### Code

### Reflection



##  Crash Avoidance Part 1

### Assignment Description

### Evidence



### Wiring


### Code

### Reflection



##  Crash Avoidance Part 1

### Assignment Description

### Evidence



### Wiring


### Code

### Reflection


## Onshape_Assignment_Template

### Assignment Description

Write your assignment description here. What is the purpose of this assignment? It should be at least a few sentences.

### Part Link 

[Create a link to your Onshape document](https://cvilleschools.onshape.com/documents/003e413cee57f7ccccaa15c2/w/ea71050bb283bf3bf088c96c/e/c85ae532263d3b551e1795d0?renderMode=0&uiState=62d9b9d7883c4f335ec42021). Don't forget to turn on link sharing in your Onshape document so that others can see it. 

### Part Image

Take a nice screenshot of your Onshape document. 

### Reflection

What went wrong / was challenging, how'd you figure it out, and what did you learn from that experience? Your goal for the reflection is to pass on knowledge that will make this assignment better or easier for the next person. Think about your audience for this one, which may be "future you" (when you realize you need some of this code in three months), me, or your college admission committee!

&nbsp;

## Media Test

Your readme will have various images and gifs on it. Upload a test image and test gif to make sure you've got the process figured out. Pick whatever image and gif you want!

### Test Link
[Hyperlink text](https://www.redbull.com/car-en/gaming-among-us-popularity)      

### Test Image
![Pikachu dies](![CoolClips_peop3337](https://github.com/jbleakl36/Engineering_4_Notebook/assets/112979207/ae1f350e-1c9d-4603-bcb8-e568cb4da344.png)  

### Test GIF
![Pikachu dies again](![0dTPMn](https://github.com/jbleakl36/Engineering_4_Notebook/assets/112979207/dd7e89aa-cf23-444e-a1d4-cb937cf3eee4.png)  

