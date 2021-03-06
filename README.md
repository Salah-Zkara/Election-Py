# Election2020
**GUI/Commands versions**
- [Election2020](#election2020)
  * [Download](#download)
  * [Requirements](#requirements)
    + [Install Tkinter](#install-tkinter)
      - [apt](#apt)
    + [Install other modules](#install-other-modules)
    + [Oracle Tables setup](#oracle-tables-setup)
  * [Execution](#execution)
    + [GUI](#gui)
      - [ Windows](#--windows)
      - [ Linux](#--linux)
  * [Links](#links)
## Download
To Download this software clone this repositorie or Download it as zip.
```bash
git clone https://github.com/Salah-Zkara/Election-Py.git
cd Election-Py
```

## Requirements
### Install Tkinter


#### apt
`$ sudo apt-get install python3-tk`

`$ sudo apt-get install python3-pil.imagetk`

or check [Tkinter Forum](https://tkdocs.com/tutorial/install.html) for other distribution or Windows or MAC
### Install other modules
to run the program you have to install the required modules so open the terminal/cmd in the root folder of the program and run this command

`$ pip install -r requirements.txt`

**or**

`$ pip3 install -r requirements.txt`

### Oracle Tables setup
- First of all, you should have [ORACLE](https://www.oracle.com/database/) database installed and working on your computer.
- Modify the connection string with yours, which is located in **"./.resources/connection.txt"** like the follow: **"username/password@localhost/ServiceName"**.
- Run installDB.py file and click install to create the required tables.
`$ python installDB.py`
**or**
`$ python3 installDB.py`
- Run Election2020_GUI_Admin.py file and add the wanted elected persons.
`$ python Election2020_GUI_Admin.py`
**or**
`$ python3 Election2020_GUI_Admin.py`
- You can add/delete the elected persons and users with the Election2020_GUI_Admin interface!


## Execution


### GUI
#### - Windows
`$ python Election2020_GUI.py`

**or** 

`$ python3 Election2020_GUI.py`
#### - Linux
**Linux version coming soon!**
<!--
`$ python Election2020_GUI_linux.py`

**or** 

`$ python3 Election2020_GUI_linux.py`
-->
## Links
[![](https://img.shields.io/badge/My-Portfolio-brightgreen)](https://salah-zkara.codes/)

[![](https://img.shields.io/badge/-Linkedin-%232867B2)](https://www.linkedin.com/in/salah-eddine-zkara-b40b091a6/)
[![](https://img.shields.io/badge/-Facebook-%234267B2)](https://www.facebook.com/salaheddine.zkara.9)
[![](https://img.shields.io/badge/-Twitter-%231DA1F2)](https://twitter.com/SalahZkara)
[![](https://img.shields.io/badge/-Github-333)](https://github.com/Salah-Zkara)
[![](https://img.shields.io/badge/-Instagram-%23E1306C)](https://www.instagram.com/salaheddine.zkara/?hl=en)

![GitHub followers](https://img.shields.io/github/followers/Salah-Zkara?style=social)
#### Supervisors: 
- **Johri Mustapha(GUI)**
- **Ziad Lamiae(Databases)**
