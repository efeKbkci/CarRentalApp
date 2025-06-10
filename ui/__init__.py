from PyQt6.QtWidgets import QWidget, QPushButton, QCheckBox, QTextEdit, QLabel, QLineEdit
from PyQt6.QtGui import QPixmap, QFont
from PyQt6.uic import loadUi
from assets.fonts import ROBOTO_MONO, PATUAONE
from .uiFiles import UiFilePaths
from .window_manager import WindowManager
from .constants import Windows, Dialogs

'''
I avoided code repetition by importing the modules that are commonly used in each UI file in a single file. 
Now the desired module can be easily imported with "from ... import <package_name>".  
".." -> points to the "__init__" package in the "ui" package (the top UI package). 
'''