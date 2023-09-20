# Engineering_4_Notebook

&nbsp;

## Table of Contents
* [Raspberry_Pi_Assignments](#Raspberry_Pi_Assignments)
  * [Launch Pad Part 1](#Launch_Pad_Part_1)
  * [Launch Pad Part 2](#Launch_Pad_Part_2)
  * [Launch_Pad_Part_3](#Launch_Pad_Part_3)
  * [Launch_Pad_Part_4](#Launch_Pad_Part_4)
  * [Crash_Introduction_Part_1](#crashintroductionpart1)
* [Onshape_Assignment_Template](#onshape_assignment_template)

&nbsp;

# Raspberry_Pi_Assignments

## Launch_Pad_Part_1

### **Assignment Description**

Our purpose is to lay the baseline of Pi in the sky. We are creating a countdown on the serial monitor from 10 to zero (liftoff). 

### **Evidence** 

<img src="https://github.com/dhalber11/Engineering_4_Notebook/assets/113122357/551b4867-9bc9-444a-9c25-2ef04950ca29" width="200">

##### The image above shows the entire sequence of counting down from 10 to LIFTOFF. 

### **Wiring**

The only wiring for this assignment was to plug the pico into the computer.  

### **Code**
For a link to the **commented code** [click here](https://github.com/dhalber11/Engineering_4_Notebook/blob/main/raspberry-pi/launchpad1.py) 

### **Reflection**
This was a very simple and easy first assignment. Bringing in elements of what I had learned in previous years and simply a refresher on how to use variables and count down. There are many different ways to code this assignment and this is just one of them. 
&nbsp;



## Launch_Pad_Part_2

### **Assignment Description**

For this assignment we are told to add two LEDs to the previous assignment. Simply a red LED that blinks as the timer is counting down. Then a green LED that turns on and stays on once the countdown reaches zero. 
### **Evidence** 

<img src="https://github.com/dhalber11/Engineering_4_Notebook/blob/main/images/ezgif-1-launchpad2.gif?raw=true" width="300">

##### This shows the full countdown process

### **Wiring**

<img src="https://github.com/dhalber11/Engineering_4_Notebook/blob/main/images/Screenshot%202023-09-08%20104811.png?raw=true" width="300">

##### This wiring was very straightforward only using two leds and one resistor.

### **Code**
Find a link to the **commented code** [here](raspberry-pi/launchpad2.py)

### **Reflection**

As this was a simple assignment there really was nothing that went wrong. I used a straightforward variable from the previous assignment and simply added the LED code where neccesary. The LEDs did not blink exactly on time the first upload but tweaking the time.sleep in the code fixed that. 

## Launch_Pad_Part_3

### **Assignment Description**

For this assignment we are still building on the previous two assignments of the Launch Pad sequence. In this assignment we are attempting to add a button to start the launch sequence. A relatively simple assignment with little added wiring as we are coding in circuitpython. 

### **Evidence**

<img src="https://github.com/dhalber11/Engineering_4_Notebook/blob/main/images/ezgif-5-launchpad3.gif?raw=true" width="300">

##### Shows the countdown initiating after a button press.

### **Wiring**

<img src="https://github.com/dhalber11/Engineering_4_Notebook/blob/main/images/launchpad3%20wiring.png?raw=true" width="200">

##### Very straightforward wiring for this assignment.

### **Code**

Find a link to the **commented** code for this asignment [here](raspberry-pi/launchpad3.py)

### **Reflection**
This assignment was not much more difficult than the previous. Simply adding a button to start the entire "if" statement. It was all things that we have done in the past however a good refresher on some simple coding. The only issue I ran into was telling the pico that the button was being continuously pressed instead of having to hold it. Attaching a variable to the button was a simple way of doing this. 


## Launch_Pad_Part_4

### **Description**
For this assignment in the launchpad series we are tasked to add a servo to our launch system. When the countdown reaches zero, rotate the servo 180 degrees. This is all in all a simple assignment and only requires initializing a servo and then turning it on time. 


### **Evidence**

<img src="https://github.com/dhalber11/Engineering_4_Notebook/blob/main/images/ezgif-1-launchpad4.gif?raw=true" width="300">


### **Wiring**

<img src="https://github.com/dhalber11/Engineering_4_Notebook/blob/main/images/Pic3.png?raw=true" width="200">

### **Code**

Find a link to the **commented** code [here](raspberry-pi/launchpad4.py)

Credit for the code to [Anton](https://github.com/aweder05/Engineering_4_Notebook)
### **Reflection**
This assignment was a little bit more difficult for me but still very very straightforward. When I say difficult it maybe took me three more minutes than the previous. These are all very helpful assignments to relearn the basics of code. This is the final launchpad assignment as well.

## Crash_Introduction_Part_1 

### **Description**
For this assignment we needed to simply wire an accelerometer and then print the values that come out of that accelerometer. This was a relatively straightforward assignment.
### **Evidence**
<img src="https://github.com/dhalber11/Engineering_4_Notebook/blob/main/images/ezgif-4-crashintroduction1.gif?raw=true" width="300">

### **Wiring**
<img src="https://github.com/dhalber11/Engineering_4_Notebook/blob/main/images/crashintro1%20wiring.png?raw=true" width="300">

### **Code** 

Find a link to the **commented** code [here](C:\Users\dhalber11\Documents\Engineering_4_Notebook\raspberry-pi\crashavoidance1.py)

### **Reflection**
This assignment was the first that used some different language I had not known yet. As this was a new piece of equipment this was a harder assignment but still very straightforward. I used the f string to print the variables and another print of a blank space to seperate them for readability. As this was only an assignment printing something to the serial monitor it was relatively easy.

## Crash_Avoidance_Part_2
### **Description**
For this assignment we were building on the previous and simply adding an LED that turns on when the board is turned to 90 degrees. As well as adding a battery that powers the board so it can be disconnected from the board.  
### **Evidence**
<img src="https://github.com/dhalber11/Engineering_4_Notebook/blob/main/images/crashavoidance2.gif?raw=true" width="400">

### **Wiring
<img src="https://github.com/dhalber11/Engineering_4_Notebook/blob/main/images/crashavoidance2wiring.png?raw=true" width="300">

### **Code**

Find a link to the **commented** code [here](https://github.com/dhalber11/Engineering_4_Notebook/blob/main/raspberry-pi/crashavoidance2.py)

### **Reflection**
While I did fry a board in the pursuit of education during this assignment (RIP 2022-2023). This was a fun assignment to complete and the wiring was very straightforward. The code as well was a total of about 4 lines added onto the end of the last assignment. Simply looking at the values and turning the LED on. The fun part was wiring the LIPO to the pico and then having a mobile board for the first time. That was satisfying to see. 
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
[test link](https://github.com/dhalber11/Engineering_4_Notebook/blob/9cbf281a8663adb27f6d2fc0ac80ec9b03e19794/raspberry-pi/test.py) 
### Test Image
![image](https://github.com/dhalber11/Engineering_4_Notebook/assets/113122357/f5303f98-df58-47e6-a544-607746d2887f)

### Test GIF
![image](https://github.com/dhalber11/Engineering_4_Notebook/assets/113122357/704be1ee-01c6-4994-b658-98002b45fe6c)
