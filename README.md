# polybar-yeelight ||| BETA EAT A LOT OF PERFOMANCE
A [Polybar](https://github.com/jaagr/polybar) module to control your [Mi LED Desk Lamp](https://www.mi.com/global/smartlamp).
May work with all [YeeLight](YeeLight) compatible lamp.
<br>
Support power on/off, +/- brightness, +/- Color temperature
<br>
<p style="text-align:center;"><img src="gif.gif" width="200"></p>

### Dependencies 

```sh
pip install yeelight
```

***Font NerdFont*** - default icon font

### Installation

```sh
cd ~/.config/polybar/scripts/polybar-yeelight/
wget https://raw.githubusercontent.com/superbunny54/polybar-yeelight/main/lamp.py
wget https://raw.githubusercontent.com/superbunny54/polybar-yeelight/main/Funct.py
```
put your the ip address of your lamp in Funct.py
```sh
chmod +x *.py
```

### Module

```ini
[module/lamp]
type = custom/script
format = "﮳ lamp"
format-overline = "#8F5902"
tail = true
label-padding = 1
label-foreground = ${colors.foreground}

exec = ~/.config/polybar/scripts/polybar-yeelight/lamp.py 
click-left = ~/.config/polybar/scripts/polybar-yeelight/lamp.py pwr
scroll-up = ~/.config/polybar/scripts/polybar-yeelight/lamp.py brplus
scroll-down = ~/.config/polybar/scripts/polybar-yeelight/lamp.py brminus
;scroll-up = ~/.config/polybar/scripts/polybar-yeelight/lamp.py ctplus
;scroll-down = ~/.config/polybar/scripts/polybar-yeelight/lamp.py ctminus
```

### Script arguments
`pwr` - toogle the power state of the lamp

`brplus` - increase the brightness of the lamp

`brminus` - decrease the brightness of the lamp

`ctplus` - increase the color temperature of the lamp

`ctminus` - decrease the color temperature of the lamp

