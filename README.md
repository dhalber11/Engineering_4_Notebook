# Engineering_4_Notebook

&nbsp;

## Table of Contents
* [Raspberry_Pi_Assignments](#raspberrypiassignments)
  * [Launch Pad Part 1](#launchpadpart1)
  * [Launch Pad Part 2](#launchpadpart2)
  * [Launch_Pad_Part_3](#launchpadpart3)
  * [Launch_Pad_Part_4](#launchpadpart4)
  * [Crash_Introduction_Part_1](#crashintroductionpart1)
  * [Crash_Avoidance_Part_2](#crashavoidancepart2)
  * [Crash_Avoidance_Part_3](#crashavoidancepart3)
  * [Landing Area Part 1](#landingareapart1)
  * [Landing Area Part 2](#landingareapart2)
  * [Morse Code(-- --- .-. ... . / -.-. --- -.. .)](#morsecode)
  * [Morse Code 2](#morse-code-2)
  * [Data Part 1(Saving)](#datapart1saving)
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

## Crash_Avoidance_Part_3
### **Description**
This assignment builds on the previous in taking the velocities and acceleration from the accelerometer. Along with an led to indicate 90 degrees. Added onto this by an oled that displays the angular velocity constantly. 

### **Evidence**

<img src="https://github.com/dhalber11/Engineering_4_Notebook/blob/main/images/crashavoidance3.gif?raw=true" width="400">

### **Wiring**

<img src="https://github.com/dhalber11/Engineering_4_Notebook/blob/main/images/crashavoidance3wiring.png?raw=true" width="300">

### **Code**

Find a link to the **commented** code [here](https://github.com/dhalber11/Engineering_4_Notebook/blob/main/raspberry-pi/crashavoidance3.py)

### **Reflection** 
This was the final assignment in the crash avoidance progression. Overall I found this group of assignments very exciting as we were learning the ropes to new technology. This assignment with the oled gave me some particular issues with the code and initialization. The syntax for the oled is quite extensive to print certain things and it can be difficult. I ended up getting some hints from Graham as to a certain line that helped me to be able to display my rotation. Other than that the wiring was very straight forward and did not take that long to figure it out. 

## Landing Area Part 1
### Description
The code must ask for the user to input a set of three coordinates in (x,y) format. The triangle area must be determined using a function. If the user inputs coordinates incorrectly (letters or improper format) the code should return to the input stage, it should not throw an error or exit the script. The triangle area must be printed to the screen in this format: “The area of the triangle with vertices (x,y), (x,y), (x,y) is {area} square km. The code must return to the input stage after printing the area, and wait for user input.


### Evidence
<img src= "https://github.com/dhalber11/Engineering_4_Notebook/blob/main/images/LandingArea1.gif?raw=true" >


### Code
Credit to the code goes to [Grant](https://github.com/ggastin30/Engineering_4_Notebook/blob/main/raspberry-pi/Landing_Area_1.py). Find a link to my code [here](https://github.com/dhalber11/Engineering_4_Notebook/blob/main/raspberry-pi/LandingArea1.py)

### Wiring 
The wiring for this assignment was very straightforward and only required the pico itself. 
### Reflection
This assignment was a very difficult one for many reasons. Not only were the variables and floats new to me but they are also quite complicated when used in functions. Defining functions is the most important part of this assignment and just below that is the process of calling them. Both are very difficult and require knowledge of the process before doing it, which I did not have. 

## Landing Area Part 2

### Description
This assignment takes the same set of requirements that are found in Landing_Area_Part1 and adds to it by requiring an OLED display. We are tasked to display the triangle on a grid with the points that were given. As well as displaying the area above the triangle. 
### Evidence
<img src= "https://github.com/dhalber11/Engineering_4_Notebook/blob/main/images/My%20Project.gif?raw=true" >

### Code
Find a link to the **commented** code [here](raspberry-pi/LandingArea2.py) 
### Wiring 
<img src= "https://github.com/dhalber11/Engineering_4_Notebook/blob/main/images/LandingArea2%20wiring.png?raw=true">

### Reflection
This assignment was much easier compared to the previous. This is because the code we used for this part of the assignment was very straightforward and only added a few lines in total to complete the assignment. On top of that, the code I used to print to the OLED was used in many previous assignments making it much easier to understand and use in this assignment. This was a fun assignment as well seeing the triangles print on the OLED and it truly shows the power of these screens. 

## Morse Code(-- --- .-. ... . / -.-. --- -.. .)

### Description
..-. --- .-. / - .... .. ... / .- ... ... .. --. -. -- . -. - / .-- . / .- .-. . / - .- ... -.- . -.. / .-- .. - .... / -- .- -.- .. -. --. / .- / .--. .-. --- --. .-. .- -- / - .... .- - / - .-. .- -. ... .-.. .- - . ... / - . -..- - / .. -. - --- / -- --- .-. ... . / -.-. --- -.. . .-.-.- / - .... . / .--. .-. --- --. .-. .- -- / -- ..- ... - / - .... . -. / --.- ..- .. - / .. ..-. / - .... . / ..- ... . .-. / .. -. .--. ..- - ... / -....- --.- .-.-.- 
(For this assignment we are tasked with making a program that translates text into morse code. The program must then quit if the user inputs -q.)

### Evidence
<img src= "https://github.com/dhalber11/Engineering_4_Notebook/blob/main/images/Morsecode.gif?raw=true">

### Code
Find a link to the **commented** code [here](raspberry-pi/morse_code.py)

### Wiring 

There was no wiring for this assignment. All that was needed was the PICO.

### Reflection
This assignment was very easy and really fun to have completed. We used the dictionary to tell the board what to translate the letters into. This was referenced using strings and a for function to call each letter individually. This worked very quickly and the only difficult part to find out was the Up_Text value that changed all of the letters to uppercase. This is done to not have to worry about changing case as a variable to deal with. 

## Morse Code 2

### Description
For this assignment we take the previous code from Morse code part 1 and translate our dots and dashes into flashes on an led of varying lengths. The task must quit if the user enters -q.

### Evidence 
<img src= "https://github.com/dhalber11/Engineering_4_Notebook/blob/main/images/morsecode2.gif?raw=true">

### Wiring 
<img src= "https://github.com/dhalber11/Engineering_4_Notebook/blob/main/images/MorseCode2.png?raw=true" width = 200>

### Code
Find a link to the commented code [here](raspberry-pi/morse_code_2.py)

### Reflection
This assignment was an interesting one for me. I was hesitant to code in the way I did as it felt very similar to simply hardcoding, which is a big no for me. However this was a simple way to define what the led should do for each dot or dash. The code was straightforward as it was simply ifs and elifs for the majority of it. The only difficult part was finding a way to call the correct part of the message and print that. Overall a fun assignment and it is great to be able to input messages and get an output just like that.

## Data_Part1(Saving)
### Description
For this assignment here are the requirements:
* Your Pico must operate in “headless” mode – unplugged from the computer with a battery
* An LED must turn on when the Pico is tilted (same as Crash Avoidance Part 2)
* Your Pico must record time, X, Y, Z acceleration data, and whether or not the Pico was tilted
* You must save this information to the Pico’s onboard storage
* You must blink the onboard LED every time you save data
* You must be able to retrieve this data when plugged back into the computer


### Evidence
<img src= "https://github.com/dhalber11/Engineering_4_Notebook/blob/main/images/datasaving.gif?raw=true" width =400>

Additionally there is a link to my data [here](https://docs.google.com/spreadsheets/d/1b9W1X0muuWlZrGeX7A1UQPyReChySrfKmhwkiQL8UQg/edit?usp=sharing)

### Wiring
<img src="https://github.com/dhalber11/Engineering_4_Notebook/blob/main/images/datapart1.png?raw=true" width="300">

##### This wiring is the same as Crash_Avoidance_2. Simply add a switch running from ground to a GP pin of your choice.

### Code 
Find a link to the commented code [here](raspberry-pi/datapart1.py)
### Reflection
This assignment was very interesting to complete as unlike most assignments, when you upload code you get an output that ensures your code is working or its broken. However for this assignment that was not the case as each time you would put the pico in code mode there was an error that was thrown each time you uploaded code. You could only check the pico was working after switching back to data mode and checking the results in the data sheets. This was a fun assignment after that however as seeing the info that was written from the board straight into a spreadsheet was very interesting. It was also good to see how simple it is to find data during flight for future reference during our Pi in the sky project.

## Data Part 2(Analysis)
### Description
This assignment was to graph the data that we collected in the previous assignment to help to analyze it and understand what it was saying.
* Create a line graph with time on the X axis and acceleration on the Y axis. X, Y, and Z accelerations must be present on the same plot.
* Create a chart with time on the X axis and whether or not the Pico was tilted on the Y axis. 
* Title each graph, and label each axis including units. 


### Evidence
<img src= "https://github.com/dhalber11/Engineering_4_Notebook/blob/main/images/Accelerationgraph.png?raw=true">
<img src= "https://github.com/dhalber11/Engineering_4_Notebook/blob/main/images/Tiltgraph.png?raw=true">
### Code and Wiring 
There was no code or wiring for this assignment.

### Reflection
While this was a very simple assignment it was a good one to learn before attempting the Pi in the sky project. As we will be doing a lot of analyzing data in the future with our projects. I have never really learned anything in google sheets or any spreadsheet software so this was helpful to understand. 
## FEA Beam

### Assignment Description
For this assignment we needed to design a beam to hold the most weight possible. The beam fails if it either bends over 35 mm or breaks. The requirements are as follows.
* The beam must use the provided attachment block with no modifications. 
* The beam with the attachment block must be able to fully engage with the holder
* The beam must use the example eye bolt mounting geometry
* The center of the eyebolt hole must be 180 mm from the front face of the attachment block (in a direction perpendicular to the front face)
* No part of the beam may extend below the bottom face of the attachment block
* All vertical angles must be >= 45° measured relative to the horizontal plane (no overhangs)
* The beam must be PLA material
* **The entire beam, including attachment block, must weigh <= 13 grams**


### Part Link 

[Link to the Onshape document](https://cvilleschools.onshape.com/documents/5ca195b929dce9b9f5de0c38/w/484c080f78991bb9985dcd6a/e/202c4b844babd7b88e7d7022?renderMode=0&uiState=651ad471654b7d4777a38ffc). 

### Part Image
<img src="https://github.com/dhalber11/Engineering_4_Notebook/blob/main/images/FEA%20Beam%202.png?raw=true" >
<img src="https://github.com/dhalber11/Engineering_4_Notebook/blob/main/images/FEA%20Beam.png?raw=true" >

### Reflection
For this assignment I was working with Mathew Colvin. We decided to split up and find different ideas and then bring those together and compare to see which is better. I started trying to find ideas with triangles and the classic steel I beam design, however it did not work out. Mainly because of the constraints of overhangs and angles being no more than 45 degrees. I was having dificulty with linear patterns and getting nowhere near to the required weight of 13 grams. However Mathew found a solution involving circles with a much more organic design. This was not only visually appealing but it was easily less than 13 grams being only around 11.8-12.4 as we tweaked it near the end. It ended up coming out to 12.89 as we added as much as we could to improve stability.

&nbsp;

## FEA Beam V.3

### Description
We are told to run simulation tests on our original beam pictured above. Judging on how it performs we will then adjust the design of our beam as it requires and continue to test. This is all the process of testing and tweaking. The same criteria apply for the above assignment. 
### Part Link 
[Link to the Onshape document](https://cvilleschools.onshape.com/documents/5ca195b929dce9b9f5de0c38/w/484c080f78991bb9985dcd6a/e/202c4b844babd7b88e7d7022?renderMode=0&uiState=651ad471654b7d4777a38ffc). 


### Part Image
<img src="https://github.com/dhalber11/Engineering_4_Notebook/blob/main/images/Assembly%201%20(1).png?raw=true" >

##### Simulation of the stress
<img src="https://github.com/dhalber11/Engineering_4_Notebook/blob/main/images/Assembly%201.png?raw=true"  >

##### Simulation of the displacement

### Reflection
After testing our beams using the simulation feature in onshape. We were tasked with changing and altering the design to improve the effectiveness of the beam. However the altering is covered in the next part of this assignment. To learn the simulation in Onshape we used an Onshape tutorial that worked through the whole process. This really helped us understand how to utilize the simulation to get the results needed. These results are what help us improve on our design in the nect part of this assignment. The stress on the very base of the beam  is much higher on the edges. This is going to be fixed by tapering the beam out to include all of the attachment block so as to add more material and reinforce the beam. However the inner circles of our design are working very well and holding the stress of the beam quite well. 

## FEA Beam V.4
### Description
This part of the beam assignment is where we used the information from the previouse simulations of our beams and improved upon the design. All of the same criteria from the previous assignment still apply here.

### Part Link
[Link to the Onshape document](https://cvilleschools.onshape.com/documents/5ca195b929dce9b9f5de0c38/w/484c080f78991bb9985dcd6a/e/202c4b844babd7b88e7d7022?renderMode=0&uiState=651ad471654b7d4777a38ffc). 

### Part Image 
<img src="https://github.com/dhalber11/Engineering_4_Notebook/blob/main/images/v2.png?raw=true" >


<img src="https://github.com/dhalber11/Engineering_4_Notebook/blob/main/images/v2%20(1).png?raw=true"  >

### Reflection 
This reflection is being written after testing this beam for the max weight it can hold. This design did not test drastically better in the simulations than our first design however there were some improvements. This design with the tapering was not only to reduce weight but to spread out the stress areas to try and decrease breaking. However the final product was very thin as the holes were very close together. It did not hold nearly as much weight as expected and deflected before it broke. In the end we realized that the amount of material taken out of the main body severely weakened the beam. We should have tapered the entire body of the beam instead of cutting through it. 
## Media Test 

Your readme will have various images and gifs on it. Upload a test image and test gif to make sure you've got the process figured out. Pick whatever image and gif you want!

### Test Link
[test link](https://github.com/dhalber11/Engineering_4_Notebook/blob/9cbf281a8663adb27f6d2fc0ac80ec9b03e19794/raspberry-pi/test.py) 
### Test Image
![image](https://github.com/dhalber11/Engineering_4_Notebook/assets/113122357/f5303f98-df58-47e6-a544-607746d2887f)

### Test GIF
![image](https://github.com/dhalber11/Engineering_4_Notebook/assets/113122357/704be1ee-01c6-4994-b658-98002b45fe6c)
