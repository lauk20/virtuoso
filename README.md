![virtuoso](/resources/virtuoso_logo.png)

  

<p  align="center">
	<em>Play the virtual piano with ease.</em>
</p>

  

## What is this?

This project was meant to make playing the [virtual piano](https://virtualpiano.net) easier. At it's core, it's a program that helps you type a preset set of characters, but it follows the rules of virtual piano notes. This project does not condone the use of this program for virtual piano contests, competitions, or similar events; it's meant to be a fun tool used for entertainment.

  

## How do I run it?

You need two Python modules to make it work: pynput and PyAutoGUI. To install follow these instructions.

1. Install pynput

```
pip install pynput
```

2. Install PyAutoGUI

```
pip install pyautogui
```

*You need to have pip installed*

  

Once you have these modules installed, you can run the ```main.py``` which is in the ```src``` directory. The command should be ```python main.py <filename>``` where filename is the path to your input file (your music sheets).

  

There are default music sheets in the ```sheets``` directory, but you can add more.