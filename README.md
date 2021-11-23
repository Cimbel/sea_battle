# Brief overview
* <a href="#chapter_about">About</a>
* <a href="#chapter_download_game">Dowload the game</a>
* <a href="#chapter_windows">Launch on Windows</a>
* <a href="#chapter_linux">Launch on Linux</a>
  * <a href="#chapter_linux_deb">Debian</a>
  * <a href="#chapter_linux_rpm">RedHat</a>
* <a href="#chapter_macos">Launch on MacOS</a>
</br>

**!NOTE!** -- Do not change the location of files, all files must be in the same directory.</br>
**!NOTE!** -- Before install the Python and etc, don't forget to install and unarchive the game's archive :blush:</br>
**!NOTE!** -- The Colorama module is required for the game, it needs to change color in a terminal.

<h2 id="chapter_about">About</h2>
<p>
  <strong>Hi there ✌️</strong></br>
  This is small console game, which is called sea battle,</br>
  written on the programming language <strong>Python</strong>.</br>
  This is my first epxperience of writing game and</br>
  program something bigger than usual not big scripts</br>
  The game represents sea battle, when you played it on</br>
  your paper with your firends or in app on your smartphones.</br>
  In this brief guide you will see how to launch the game on</br>
  the different OS. So, hope you will enjoy a little with that, and catch</br>
  some flashbacks from the past 😉
</p>

<h2 id="chapter_download_game">Download the game</h2>

<p>
  It must be easy for you do download the game. In the right panel from the main page of this <a href="https://github.com/Cimbel/sea_battle">repository</a></br>
  there is the tab "Releases", choose the name of release, then under <strong>Assest</strong> choose archive</br>
  which is the most suitable for you OS, click on that and it will download an archive. For the windows OS the</br>
  best choice will <strong>ZIP</strong> archive, for other ones it will be more suitable to choose <strong>TAR.GZ</strong> archive.</br> 
  After you downloaded it successfully, unarchive it and follow the next instructions which suitable for your OS</br>
  about how to install the Python and launch the game.
</p>

<h2 id="chapter_windows">Launch on Windows</h2>
<p>
  Follow the <a href="https://www.python.org/">link</a>, download the latest version of the Python for Windows.</br>
  Search <strong>cmd</strong> in your main search and then run the commands which are below.</br>
</p>

```
python -m pip install --upgrade pip
pip install colorama
```

<p>
  It will upgrade packet manager if need and install dependency for the game.</br>
  Then you could just open <code>game.py</code> and enjoy the game.</br>
  You are also able to launch the game from the command line.</br>
  Launch command line in Windows, then indicate the command below.</br>
</p>

```
python "path/to/game.py"
```

<h2 id="chapter_linux">Launch on Linux</h2>
<h3 id="chapter_linux_deb">Debian</h3>

<p>
  Open the terminal and run the commands below.
</p>

```
sudo apt-get -y update && sudo apt-get -y upgrade
sudo apt-get install -y python3 python3-pip
pip install colorama
```

<p>
  So, previous commands update your files to the latest version,</br>
  then download the Python, pip, and dependency. After that,</br>
  launch the game by using command below.
</p>

```
python3 "path/to/game.py"
```

<h3 id="chapter_linux_rpm">RedHat</h3>

<p>
  Open a terminal and run the commands below
</p>

```
sudo yum -y update && sudo yum -y install epel-release
sudo yum -y update && sudo yum -y install python3
pip3 install colorama
```

<p>
  It will update your OS files to the latest version, then</br>
  install additional repository, python, pip, and dependency package.</br>
  So, after that launch the game by the command below.
</p>

```
python3 "path/to/game.py"
```

<h2 id="chapter_macos">Launch on macOS</h2>

<p>
  By default, on macOS you have two different version of the Python. The first one is</br>
  python2 and the second one is python3. You can check it by opening your terminal in macOS</br>
  and type the commands below</br>
</p>

```
python -V
python3 -V
```

<p>
  In case of not having python3, follow the <a href="https://www.python.org/downloads/macos/">link</a> and find the newest stable python3 version for macOS,</br>
  and download it. After that you will be able to check your version by previous ones commands and this</br>
  must show you which exactly python3 version do you have on your macOS. After that, upgrade the pip,</br>
  python package manager for installing modules, and install one of the modules which the game required.</br>
  Use the commands which are below.</br>
</p>

```
pip3 install -U pip3
pip3 install colorama
```

<p>
  After you have done all those steps, in your terminal you just need type the command below,</br>
  for launching the sea battle game.</br>
</p>

```
python3 /path/to/game.py
```

<p>
  In the <strong>/path/to/game.py</strong> must be your path where the game.py file located on your macOS.</br>
  After that, you will successfully launch the game and hope you will have some fun with that 😃 
</p>
