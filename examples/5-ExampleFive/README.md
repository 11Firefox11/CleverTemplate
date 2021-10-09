<h1 align="center" id="CleverTemplate">Clever Template</h1>
<h4 align="center">Example - Top level</h4>
<p align="center"><img src="../../assets/icon_ct.jpg" height="175"></p>

### Console
```console
@consoleapp:~$ CleverTemplate create .
```
```
INFO: Scanning config file at path: '.\ct-config.json'...
INFO: Scanning done.
INFO: Editing '.\index.html' parameters:
INFO: Type: `!ml` for multi line input, and type `!qml` for exiting multi line input mode!
INFO: Parameter: 'pagetitle', type: 'text', default value: 'None'
INPUT: My site
INFO: Type: `!ml` for multi line input, and type `!qml` for exiting multi line input mode!
INFO: Parameter: 'title', type: 'text', default value: 'None'
INPUT: Fox
INFO: Type: `!ml` for multi line input, and type `!qml` for exiting multi line input mode!
INFO: Parameter: 'content', type: 'text', default value: 'None'
INPUT: Foxes are small to medium-sized, omnivorous mammals belonging to several genera of the family Canidae. They have a flattened skull, upright triangular ears, a pointed, slightly upturned snout, and a long bushy tail (or brush).
INFO: Type: `!ml` for multi line input, and type `!qml` for exiting multi line input mode!
INFO: Parameter: 'showwarning', type: 'boolean', default value: 'True'
INPUT: True
INFO: Finished with '.\index.html'.
INFO: Editing '.\style.css' parameters:
INFO: Type: `!ml` for multi line input, and type `!qml` for exiting multi line input mode!
INFO: Parameter: 'h1color', type: 'text', default value: '#000000'
INPUT: #FFA500
INFO: Type: `!ml` for multi line input, and type `!qml` for exiting multi line input mode!
INFO: Parameter: 'pagecolor', type: 'text', default value: '#9596a2'
INPUT: 000000
INFO: Finished with '.\style.css'.
INFO: Creating template '.\index.html'.
INFO: Template created at '.\ct-output\index.html', with parameters: '{'pagetitle': 'My site', 'title': 'Fox', 'content': 'Foxes are small to medium-sized, omnivorous mammals belonging to several genera of the family Canidae. They have a flattened skull, upright triangular ears, a pointed, slightly upturned snout, and a long bushy tail (or brush).', 'showwarning': True}'.
INFO: Creating template '.\style.css'.
INFO: Template created at '.\ct-output\style.css', with parameters: '{'h1color': '#FFA500', 'pagecolor': '000000'}'.
```
  
> In this document, console based examples, '**@consoleapp:~$**' will be referenced as the main user, or/and current directory in a console, the main program (Clever Template), will be referenced as '**CleverTemplate**.  
> All the mentioned files what are created, are in this directory's [assets folder](./assets).