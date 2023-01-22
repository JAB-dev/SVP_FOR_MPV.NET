# SVP_FOR_MPV.NET
Scripts for mpv (although support will be for mpv.net) that allow the use of SVP frame interpolation without having to use svp

1. Install [python](https://www.python.org/downloads/) and [vapoursynth](http://www.vapoursynth.com/doc/installation.html). Right now the 2 needed versions are Python 3.10.8 and VapourSynthR60. 

**INSTALL FOR ALL USERS**

2. Test vapoursynth in python

```
from vapoursynth import core

print(core.version())
```
3. Move the dlls into %APPDATA%\VapourSynth\plugins64

4. If all is well you can now setup input.conf and mpv.conf located in %AppData%\mpv.net

input.conf add 

**Only nessecary on old versions, new versions already have a profile swap menu**

```ini
_ set profile YourProfileNameHere #menu: Profiles > profile YourProfileNameHere
```
mpv.conf add 
```ini
[YourProfileNameHere]
vf=vapoursynth="PATH_TO_YOUR_SCRIPT"
profile-restore = copy
```

5. inside of mpv you can now right click and use the profile menu to select the profile you created

### For debugging you can enable an osd console by pressing tilde `

# Extras!
You can fix audio desync (which might occur on lower end hardware) by including the segment below in your mpv.conf
```ini
hr-seek-framedrop=no
```
Some versions of the svpflow dlls require svp to be running in the background, if you get a red square install svp

You can adjust the output fps inside the script by changing 
```
desired_fps = 60
```
To make the script use your displays fps use
```
desired_fps=display_fps
```
