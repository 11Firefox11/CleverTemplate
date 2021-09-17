<h1 align="center" id="CleverTemplate">Clever Template</h1>

<h4 align="center">Console app for making simple <a href="https://jinja.palletsprojects.com/en/3.0.x/templates/" target="blank_">Jinja2</a> based templates. </h4>
<p align="center"><img src="./assets/icon_ct.jpg" height="175"></p>

- [Introduction](#introduction)
- [Install](#install)
- [App usage](#app-usage)
  - [Commands](#commands)
  - [Default optional arguments](#default-optional-arguments)
  - [Templating](#templating)
  - [Config file](#config-file)
    - [Create a config file](#create-a-config-file)
    - [Syntax, formatting](#syntax-formatting)
      - [Main sample, syntax](#main-sample-syntax)
      - [Syntax keys](#syntax-keys)
        - [`PATH_TO_TEMPLATEFILE`](#path_to_templatefile)
        - [`VARIABLE`](#variable)
        - [`VARIABLETYPE`](#variabletype)
        - [`DEFAULTVALUE`](#defaultvalue)
- [Examples](#examples)
- [Releases](#releases)

## Introduction
Clever Template is a console application, which uses a templating engine, Jinja2. Clever Template is simply just an app, what can input variables into Jinja2 typed templates.  
In the app, you have to set your own variables/parameters, what should be defined by the user when the user wants to create a new template. For this reason, the app requires a JSON file. The JSON file will contain which file should have what variable, with what type and what default value. By that config JSON file, the app will know what variables can be inputted into which template file, and it will request those variables when the user is creating  template.  
You can see examples about all types of topics in the [examples](./examples) folder.  

## Install
Download the code from a release. [Github - Clever Template Releases](https://github.com/11Firefox11/CleverTemplate/releases)

## App usage
Open a terminal window on your device, and run CleverTemplate.  
If you simply run CleverTemplate, it will give a help description about the app, and its commands, arguments. You can interact with CleverTemplate by [commands](#commands).  
### Commands 
|  name | arguments | description | curr version |
| - | - | - | - |
| create | path | Create a template, by giving the path of the ct-config.json. | 1.0 |
### Default optional arguments
There are default optional arguments, what can be combined with the default app program and with any command. These are trigger arguments, that means, if they get inputted then other events will not be executed.
|  name | reference | description |
| - | - | - |
| help | --help or -h | use this argument to get help |
| version | --version or -v | use this argument to get version info |
### Templating
The template files must include [Jinja2 syntax](https://jinja.palletsprojects.com/en/3.0.x/templates/), if the user wants to pass variables inside the template code.  
Variables will be passed in a dict named `ctdata`, so to use the custom variables you have to refer them as `ctdata.VARIABLE`.
### Config file
Clever Template has its own simple config JSON file name, and syntax. This syntax is very important.
#### Create a config file
The config file must be `ct-config.json`. Create a config file, then just open it with any text editor and start editing it.
#### Syntax, formatting
The config file is simple, it is easy to set up. The JSON file should contain objects, named to the template file name. Inside the template object, there should be variable objects, with their custom names. The variable objects should contain an array (list), where the first index should be a variable type, what must be defined, and on the second index, it can be defined, what the default value of the variable should be.
##### Main sample, syntax
```js 
{
    PATH_TO_TEMPLATEFILE-1 : {
        VARIABLE1:[VARIABLETYPE, DEFAUTVALUE],
        VARIABLE2:[VARIABLETYPE, DEFAUTVALUE]
    },
    PATH_TO_TEMPLATEFILE-2 : {
        VARIABLE1:[VARIABLETYPE, DEFAUTVALUE],
        VARIABLE2:[VARIABLETYPE]
    }
}
```
##### Syntax keys
###### `PATH_TO_TEMPLATEFILE`
This is a string, what is a path to a existing file. The variables inside this part, will be inputted in to the file content. This is the name of the template object.
###### `VARIABLE`
This is a string, what can be anything, this is simply just a variable name. This variable will be passed into the file too, if it will be given a value. This is the name of the variable object.
###### `VARIABLETYPE`
This is a string, what can be three things: 
- `text`: this is simply just a text, string, it can have any value what can be changed into a text
- `number`: this is a number, can be any type of number, a whole number or not, it does not matter
- `boolean`: this is simply just a `true` or `false` variable type   

The string must match exactly with the three variable types. Etc. it can't be `TEXT` or `Num`, all its characters should be with small letters, and the type should be fully written out. This is the first index of the array inside its variable object, this must be defined.
###### `DEFAULTVALUE`
This is a value, matched to the variable object's type. This is the second index of the array inside its variable object, this can be defined, but it is not a must. 
## Examples
See the [examples](./examples) folder for some easy examples, also to get some idea about how to use the app.
## Releases
This app is kind of in an early phase. Clever Template will be growing hopefully, new updates will be coming in the future.

---

[To the top](#CleverTemplate)