# EnhancedClipboard

## About
The Enhanced Clipboard is a tool that allows Mac users to copy up to 10 pieces of text at once, and then choose which they want to paste.

## Motivation
A major shortcoming of the clipboard is that users can only copy one piece of text at a time. If they want to copy something else, they need to override whatever is currently on the clipboard. This leads to either having to type things out, or unnecessarily toggling between tabs, both of which reduce one's efficiency. The Enhanced Clipboard eliminates this flaw by allowing users to have multiple items copied at once. 

## Technologies
For this project I used python3, and tkinter for the GUI.

## Limitations
This tool is designed for Mac users, and only works on a Mac. 

## How to Use

### Installation
Make sure you have python3 installed, and then download the enhanced_clipboard.py file. Ensure that you have pynput installed, and if not install using pip.

### Run the program
To use, run 
```
sudo python3 enhanced_clipboard.py
```
`sudo` permissions are necessary in order for the tool to run in the background of other applications. 

To exit, press `esc`.

### Using the tool

Press `ctrl` and a number `0` - `9` to select which slot to save the next copied piece of text in. Then, copy as you normally would (`cmd` and `c`). To paste, press `ctrl` and a number `0` - `9` to choose which slot to paste from. Then, paste as you normally would (`cmd` and `v`).

### The GUI

The GUI displays the 10 slots, as well as the text that has been copied into each slot. It also has a "CURRENT" label to indicate the current slot that will be copied or pasted to.
