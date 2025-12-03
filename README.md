[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/LTGLDrua)
# Multi-Input, Multi-Output Circuit Project

## Overview

This project is part of Engineering: Electronics and Computer Programming.

The goal is to design and build a small embedded system that uses:
- At least **two input devices**, and
- At least **three output devices**,

and to write a MicroPython program that reads the inputs and produces at least **three distinct output behaviors** using the outputs.


---

## Inputs and Outputs

Some possible inputs and outputs:

**Inputs**

- buttons (you could use multiple)
- potentiometer (you could use multiple of these as well)
- Joystick (really just 2 potienometers and a button in one)

**Outputs**

- LEDs (you could use multiple)
- Passive Buzzer (do a little online research)
 

### Input Devices

1. Input #1:  
   - Type: Potentiometer
   - Pico pin: ADC0/GP26/Pin 31
   - What it controls: The amount of red

2. Input #2:  
   - Type: Potentiometer
   - Pico pin: ADC1/GP27/Pin 32
   - What it controls: The amount of green

3. Input #3:
   - Type: Potentiometer
   - Pico pin: ADC2/GP28/Pin 34
   - What it controls: The amount of blue


### Output Devices

1. Output #1:  
   - Type: RGB LED
   - Pico pin: GP15  
   - Behavior: Red color

2. Output #2:  
   - Type: RGB LED 
   - Pico pin: GP14
   - Behavior: Green color 

3. Output #3:  
   - Type: RGB LED
   - Pico pin: GP13
   - Behavior: Blue color  


---

## Initial Plan

Describe what you intended to build before you started wiring and coding.

- What is your system supposed to do?  
- How should the inputs affect the outputs?  
- What are the three distinct output behaviors you planned?  

My idea is to have three potentiometers each change the strength of one of the colors of an RGB LED. They change the strength by adjusting the frequency of the light being on or off. This makes it easy to make different colors by having different combinations of the three and their intensities.

---

## Circuit Design

Describe or sketch your circuit here. You may include a diagram as an image or link.

- How are power and ground distributed?  
- Which pins are used for each input and output?  
- Any special components (resistors, transistors, etc.)? 

The RGB wiring is on the top left half while the potentiometer wiring is on the right side. The RGB light has four wires, three are for the lights, each going through a resistor first. The ground is connected directly. For each potentiometer there are three wires. The top goes to the power rail, the bottom the ground rail, and the middle goes to an ADC pin. The power rail has one wire going to Pin 36 while the ground rail goes to Pin 23.

### Pin Mapping Table

| Device        | Type (Input/Output) | Pico Pin | Notes              |
|---------------|---------------------|----------|--------------------|
| Potentiometer | Input               | Pin 31   | Red Control        |
| Potentiometer | Input               | Pin 32   | Green Control      |
| Potentiometer | Input               | Pin 34   | Blue Control       |
| RGB Light     | Output              | Pin 20   | Red Lighting       |
| RGB Light     | Output              | Pin 19   | Green Lighting     |
| RGB Light     | Output              | Pin 17   | Blue Lighting      |
| Potentiometer | For Input           | Pin 23   | Ground for Pots    |
| Potentiometer | For Input           | Pin 36   | Power for Pots     |
| RGB Light     | For Output          | Pin 18   | Ground for RGB     |

---

## How to Run the Code

1. Flash MicroPython to the Pico (if needed).  
2. Copy `main.py` onto the Pico.  
3. Connect using Thonny and open the REPL.  
4. The program will start running when the Pico is reset or powered.


---

## Challenges and Debugging

Describe the main challenges you encountered while working on this project.

- Hardware issues (wiring mistakes, loose connections, wrong pin choices, power problems)  
- Software issues (bugs, logic errors, timing problems)  
- How you found and fixed each problem  

Be as specific as possible.

I did not have any major issues. I started by trying out the RGB LED to familiarize myself with it. After that, I used one potentiometer on one color to continue testing. Once that worked, I added the other potentiometers. The only issues I had were from missing code I needed to change when going from single LED to RGB LED and when adding in potentiometers.

---

## Final Design vs. Initial Plan

Explain how your final project differs from your initial plan.

- Did you change any devices (inputs or outputs)?  
- Did any behaviors change or get simplified?  
- Did you add any new features? 

In one of my very first ideas, I considered using a joystick to control two of the LEDs. I decided to use three potentiometers instead because it's easier to figure out and more intuitive to use when finished. Overall, the result is exactly how I imagined.

---

## Possible Improvements

If you had more time, what would you improve or add?

- Additional behaviors or modes  
- Better physical layout  
- More robust error handling in code  

My result leaves me satisfied since it works exactly how I expected it to. It would be nice if the wiring looked cleaner and if the potentiometers were more comfortable to turn. If I had a lot more time, I would try my other idea of using one joystick to choose a color by moving around like on a color wheel.

---

## AI Use Statement (If Applicable)

If you used AI tools (such as ChatGPT or GitHub Copilot), briefly describe how:

- What did you ask the AI to help with?  
- How did you change or adapt any code or ideas you got from AI?  


