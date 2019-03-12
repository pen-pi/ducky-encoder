#!/usr/bin/env python2

# https://gist.github.com/rmed/0d11b7225b3b772bb0dd89108ee93df0
# http://www.freebsddiary.org/APC/usb_hid_usages.php
# http://www.mindrunway.ru/IgorPlHex/USBKeyScan.pdf

NULL_CHAR = chr(0)
NULL_MODIFIER = 0

L_SHIFT = 2
R_SHIFT = 32

L_CTRL = 1
R_CTRL = 16

L_ALT = 4
R_ALT = 64

L_GUI = 8
R_GUI = 128

SHIFT = L_SHIFT
GUI = L_GUI
ALT = L_ALT
CTRL = L_CTRL


scancodes = {
   "a" : "04".decode("hex"),
   "b" : "05".decode("hex"),
   "c" : "06".decode("hex"),
   "d" : "07".decode("hex"),
   "e" : "08".decode("hex"),
   "f" : "09".decode("hex"),
   "g" : "0A".decode("hex"),
   "h" : "0B".decode("hex"),
   "i" : "0C".decode("hex"),
   "j" : "0D".decode("hex"),
   "k" : "0E".decode("hex"),
   "l" : "0F".decode("hex"),
   "m" : "10".decode("hex"),
   "n" : "11".decode("hex"),
   "o" : "12".decode("hex"),
   "p" : "13".decode("hex"),
   "q" : "14".decode("hex"),
   "r" : "15".decode("hex"),
   "s" : "16".decode("hex"),
   "t" : "17".decode("hex"),
   "u" : "18".decode("hex"),
   "v" : "19".decode("hex"),
   "w" : "1A".decode("hex"),
   "x" : "1B".decode("hex"),
   "y" : "1C".decode("hex"),
   "z" : "1D".decode("hex"),
   "1" : "1E".decode("hex"),
   "2" : "1F".decode("hex"),
   "3" : "20".decode("hex"),
   "4" : "21".decode("hex"),
   "5" : "22".decode("hex"),
   "6" : "23".decode("hex"),
   "7" : "24".decode("hex"),
   "8" : "25".decode("hex"),
   "9" : "26".decode("hex"),
   "0" : "27".decode("hex"),
   "A" : "04".decode("hex"),
   "B" : "05".decode("hex"),
   "C" : "06".decode("hex"),
   "D" : "07".decode("hex"),
   "E" : "08".decode("hex"),
   "F" : "09".decode("hex"),
   "G" : "0A".decode("hex"),
   "H" : "0B".decode("hex"),
   "I" : "0C".decode("hex"),
   "J" : "0D".decode("hex"),
   "K" : "0E".decode("hex"),
   "L" : "0F".decode("hex"),
   "M" : "10".decode("hex"),
   "N" : "11".decode("hex"),
   "O" : "12".decode("hex"),
   "P" : "13".decode("hex"),
   "Q" : "14".decode("hex"),
   "R" : "15".decode("hex"),
   "S" : "16".decode("hex"),
   "T" : "17".decode("hex"),
   "U" : "18".decode("hex"),
   "V" : "19".decode("hex"),
   "W" : "1A".decode("hex"),
   "X" : "1B".decode("hex"),
   "Y" : "1C".decode("hex"),
   "Z" : "1D".decode("hex"),
   "!" : "1E".decode("hex"),
   "@" : "1F".decode("hex"),
   "#" : "20".decode("hex"),
   "$" : "21".decode("hex"),
   "%" : "22".decode("hex"),
   "^" : "23".decode("hex"),
   "&" : "24".decode("hex"),
   "*" : "25".decode("hex"),
   "(" : "26".decode("hex"),
   ")" : "27".decode("hex"),
   "ENTER" : "28".decode("hex"),
   "ESCAPE" : "29".decode("hex"),
   "BACKSPACE": "2A".decode("hex"),
   "TAB": "2B".decode("hex"),
   "SPACE": "2C".decode("hex"),
   " ": "2C".decode("hex"),
   "-": "2D".decode("hex"),
   "_": "2D".decode("hex"),
   "=": "2E".decode("hex"),
   "[": "2F".decode("hex"),
   "]": "30".decode("hex"),
   "\\": "31".decode("hex"), #backslash
   "+": "2E".decode("hex"),
   "{": "2F".decode("hex"),
   "}": "30".decode("hex"),
   "|": "31".decode("hex"),
   ";": "33".decode("hex"),
   "'": "34".decode("hex"),
   "`": "35".decode("hex"),
   ",": "36".decode("hex"),
   ".": "37".decode("hex"),
   "/": "38".decode("hex"),
   ":" : "33".decode("hex"),
   '"' : "34".decode("hex"),
   "~": "35".decode("hex"),
   "<" : "36".decode("hex"),
   ">" : "37".decode("hex"),
   "?" : "38".decode("hex"),
   "CAPSLOCK": "39".decode("hex"),
   "F1": "3A".decode("hex"),
   "F2": "3B".decode("hex"),
   "F3": "3C".decode("hex"),
   "F4": "3D".decode("hex"),
   "F5": "3E".decode("hex"),
   "F6": "3F".decode("hex"),
   "F7": "40".decode("hex"),
   "F8": "41".decode("hex"),
   "F9": "42".decode("hex"),
   "F10": "43".decode("hex"),
   "F11": "44".decode("hex"),
   "F12": "45".decode("hex"),
   "PRINTSCREEN" : "46".decode("hex"),
   "SCROLLLOCK" : "47".decode("hex"),
   "PAUSE" : "48".decode("hex"),
   "INSERT" : "49".decode("hex"),
   "HOME" : "4A".decode("hex"),
   "PAGEUP" : "4B".decode("hex"),
   "DELETE" : "4C".decode("hex"),
   "END" : "4D".decode("hex"),
   "PAGEDOWN" : "4E".decode("hex"),
   "RIGHT" : "4F".decode("hex"),
   "LEFT" : "50".decode("hex"),
   "DOWN" : "51".decode("hex"),
   "UP" : "52".decode("hex"),
   "APP" : "65".decode("hex"),
   "NUMLOCK" : "53".decode("hex")

   #"GUI": "E3".decode("hex")
}




shiftedLetters = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R",
"S","T","U","V","W","X","Y","Z","!","@","#","$","%","^","&","*","(",")",":",'"',"~","<",">","?","+","{","}","|","_"]






   # 0x00  Reserved (no event indicated)
   # 0x01  Keyboard ErrorRollOver
   # 0x02  Keyboard POSTFail
   # 0x03  Keyboard ErrorUndefined
   # 0x32  Keyboard Non-US # and ~
   # 0x54  Keypad /
   # 0x55  Keypad *
   # 0x56  Keypad -
   # 0x57  Keypad +
   # 0x58  Keypad ENTER
   # 0x59  Keypad 1 and End
   # 0x5A  Keypad 2 and Down Arrow
   # 0x5B  Keypad 3 and PageDn
   # 0x5C  Keypad 4 and Left Arrow
   # 0x5D  Keypad 5
   # 0x5E  Keypad 6 and Right Arrow
   # 0x5F  Keypad 7 and Home
   # 0x60  Keypad 8 and Up Arrow
   # 0x61  Keypad 9 and PageUp
   # 0x62  Keypad 0 and Insert
   # 0x63  Keypad . and Delete
   # 0x64  Keyboard Non-US \ and |
   # 0x66  Keyboard Power
   # 0x67  Keypad =
   # 0x68  Keyboard F13
   # 0x69  Keyboard F14
   # 0x6A  Keyboard F15
   # 0x6B  Keyboard F16
   # 0x6C  Keyboard F17
   # 0x6D  Keyboard F18
   # 0x6E  Keyboard F19
   # 0x6F  Keyboard F20
   # 0x70  Keyboard F21
   # 0x71  Keyboard F22
   # 0x72  Keyboard F23
   # 0x73  Keyboard F24
   # 0x74  Keyboard Execute
   # 0x75  Keyboard Help
   # 0x76  Keyboard Menu
   # 0x77  Keyboard Select
   # 0x78  Keyboard Stop
   # 0x79  Keyboard Again
   # 0x7A  Keyboard Undo
   # 0x7B  Keyboard Cut
   # 0x7C  Keyboard Copy
   # 0x7D  Keyboard Paste
   # 0x7E  Keyboard Find
   # 0x7F  Keyboard Mute
   # 0x80  Keyboard Volume Up
   # 0x81  Keyboard Volume Down
   # 0x82  Keyboard Locking Caps Lock
   # 0x83  Keyboard Locking Num Lock
   # 0x84  Keyboard Locking Scroll Lock
   # 0x85  Keypad Comma
   # 0x86  Keypad Equal Sign
   # 0x87  Keyboard International1
   # 0x88  Keyboard International2
   # 0x89  Keyboard International3
   # 0x8A  Keyboard International4
   # 0x8B  Keyboard International5
   # 0x8C  Keyboard International6
   # 0x8D  Keyboard International7
   # 0x8E  Keyboard International8
   # 0x8F  Keyboard International9
   # 0x90  Keyboard LANG1
   # 0x91  Keyboard LANG2
   # 0x92  Keyboard LANG3
   # 0x93  Keyboard LANG4
   # 0x94  Keyboard LANG5
   # 0x95  Keyboard LANG6
   # 0x96  Keyboard LANG7
   # 0x97  Keyboard LANG8
   # 0x98  Keyboard LANG9
   # 0x99  Keyboard Alternate Erase
   # 0x9A  Keyboard SysReq/Attention
   # 0x9B  Keyboard Cancel
   # 0x9C  Keyboard Clear
   # 0x9D  Keyboard Prior
   # 0x9E  Keyboard Return
   # 0x9F  Keyboard Separator
   # 0xA0  Keyboard Out
   # 0xA1  Keyboard Oper
   # 0xA2  Keyboard Clear/Again
   # 0xA3  Keyboard CrSel/Props
   # 0xA4  Keyboard ExSel
   # 0xE0  Keyboard LeftControl
   # 0xE1  Keyboard LeftShift
   # 0xE2  Keyboard LeftAlt
   # 0xE3  Keyboard Left GUI # implemented ad GUI
   # 0xE4  Keyboard RightControl
   # 0xE5  Keyboard RightShift
   # 0xE6  Keyboard RightAlt
   # 0xE7  Keyboard Right GUI



