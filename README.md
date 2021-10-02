<h1 align="center" id="CleverTemplate">Clever Template</h1>

<h4 align="center">Console application for making simple <a href="https://jinja.palletsprojects.com/en/3.0.x/templates/" target="blank_">Jinja2</a> based templates. </h4>
<p align="center"><img src="./assets/icon_ct.jpg" height="175"></p>

- [Introduction](#introduction)
- [Install](#install)
- [App usage](#app-usage)
  - [Commands](#commands)
    - [`create`](#create)
    - [Default optional arguments](#default-optional-arguments)
  - [Config file](#config-file)
    - [Create a config file](#create-a-config-file)
    - [Syntax, formatting](#syntax-formatting)
        - [Main sample, syntax](#main-sample-syntax)
      - [Syntax keys](#syntax-keys)
        - [`PATH_TO_TEMPLATEFILE`](#path_to_templatefile)
        - [`VARIABLE`](#variable)
        - [`VARIABLETYPE`](#variabletype)
        - [`DEFAULTVALUE`](#defaultvalue)
  - [Custom input data file](#custom-input-data-file)
    - [Creating a custom input data file](#creating-a-custom-input-data-file)
    - [Syntax, formatting](#syntax-formatting-1)
      - [Main sample, syntax](#main-sample-syntax-1)
      - [Syntax keys](#syntax-keys-1)
        - [`PATH_TO_TEMPLATEFILE_CF`](#path_to_templatefile_cf)
        - [`VARIABLE_CF`](#variable_cf)
        - [`VARIABLEVALUE`](#variablevalue)
- [About Jinja2 templating](#about-jinja2-templating)
- [About JSON formatting](#about-json-formatting)
- [Examples](#examples)
- [Releases](#releases)

## Introduction
Clever Template is a console application, which uses a templating engine, Jinja2. Clever Template is simply just an app, what can input variables into Jinja2 typed templates.  
In the app, you have to set your own variables/parameters, what should be defined by the user when the user wants to create a new template. For this reason, the app requires a JSON file. The JSON file will contain which file should have what variable, with what type and what default value. By that config JSON file, the app will know what variables can be inputted into which template file, and it will request those variables when the user is creating  template.  
You can see examples about all types of topics in the [examples](./examples) folder.  

## Install
Download the code or the `CleverTemplate.exe` file from a release. [Github - Clever Template Releases](https://github.com/11Firefox11/CleverTemplate/releases)

## App usage
Open a terminal window on your device, and run CleverTemplate.  
If you simply run CleverTemplate, it will give a help description about the app, and its commands, arguments. You can interact with CleverTemplate by [commands](#commands).  
For the full app usage, and for better understanding, please consider reading: [Jinja2 templating](#about-jinja2-templating) and [JSON formatting](#about-json-formatting).
### Commands 
Clever Template uses simply syntaxes for commands. A command usually have arguments. There are positional arguments that must be in the command, and there are arguments which are optional, it means that it is not a must to be in the command. There are some [default optional arguments](#default-optional-arguments).
#### `create`
With this command, the user can create final files from templates, by giving the [path](#path) of the [config file](#config-file).  
After the app scanned the config file, it will ask for input from the terminal, for all [variables](#variable) that were specified in the config file. The user can enter in multiline input mode too here, by typing `!ml`, it can be exited from here, by typing `!q`. The multiline mode will ask for input till it is exited. When the app asks for input in the terminal, by hiting `CTRL + C`, the app will quit.   
The user can specify a [custom data file](#custom-input-data-file) too, that will be used instead of asking in data for all variables in the terminal.  
If any input value does not match with its variable type, it will be replaced by the default variable value.  
- #### Arguments:
`path`: This is a positional argument, it must point to a directory what conains the [config file](#config-file), or point directly to the config file.
`--customdata CUSTOMDATA`: This is an optional argument, `CUSTOMDATA` refers to be replaced with a path, pointing to a [json file](#custom-input-data-file), what contains the custom data that should be passed in, as variables.
- #### Command usage
```console
create [--customdata CUSTOMDATA] path
```
#### Default optional arguments
There are default optional arguments, what can be combined with the default app program and with any command. These are trigger arguments, that means, if they get inputted then other events will not be executed.
|  name | reference | description |
| - | - | - |
| help | --help or -h | use this argument to get help |
| version | --version or -v | use this argument to get version info |
### Config file
Clever Template has its own simple config JSON file name, and syntax. This syntax is very important.
#### Create a config file
The config file must be `ct-config.json`. Create a config file, then just open it with any text editor and start editing it.
#### Syntax, formatting
The config file is simple, it is easy to set up. The JSON file should keys, named to the template file name. Inside the template key, there should be variable keys, with their custom names. The variable keys should contain an array (list), where the first index should be a variable type, what must be defined, and on the second index, it can be defined, what the default value of the variable should be.
###### Main sample, syntax
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
### Custom input data file
As the config file, Clever Template has its own simple config JSON syntax, but the file name can be anything. This syntax is very important. 
#### Creating a custom input data file
The file can be named anything, and can have any file extension, as long as it has json formatted in it. Create a file, then just open it with any text editor and start editing it.
#### Syntax, formatting
The custom input data file is simple, it is easy to set up. The file must contain JSON syntax. It has to conatin a main object, inside it keys named as the template files, refeering from the [config file](#config-file). Inside the template file keys, there should be variable keys, with their custom value. The variable keys should contain a special value, what matches with the [config file variables](#variable), what will be matched with it.
##### Main sample, syntax
```js
{
    PATH_TO_TEMPLATEFILE_CF-1 : {
        VARIABLE_CF1:VARIABLEVALUE,
        VARIABLE_CF2:VARIABLEVALUE
    },
    PATH_TO_TEMPLATEFILE_CF-2 : {
        VARIABLE_CF1:VARIABLEVALUE,
        VARIABLE_CF2:VARIABLEVALUE
    }
}
```
##### Syntax keys
###### `PATH_TO_TEMPLATEFILE_CF` 
This is the same as it is in the [config file](#path_to_templatefile). This should refeer the same template file path as in the config file it will be matched with.
###### `VARIABLE_CF`
This is also the same as it is in the [config file](#variable). This should also refeer the same variable as in the config file it will be matched with.
###### `VARIABLEVALUE`
This can be anything, this is the value of the variable. The variable value type should match with the matching [config file variabletype](#variabletype). This special value will be inputed into a variable what will be inputed into the template it is in.
## About Jinja2 templating
Jinja is a fast, expressive, extensible templating engine. Special placeholders in the template allow writing code similar to Python syntax.  
The template files in Clever Template must include [Jinja2 syntax](https://jinja.palletsprojects.com/en/3.0.x/templates/), if the user wants to pass variables inside the template code.  
Variables will be passed in a dict named `ctdata`, so to use the custom variables the user have to refer them as `ctdata.VARIABLE`.
## About JSON formatting
JSON (JavaScript Object Notation) is a lightweight data-interchange format. It is easy for humans to read and write.  
There are objects, keys/values in this format. For the full use of Clever Template, the user needs to use this JSON format in custom files.  
Objects are what surrounded by curly braces `{}`.  
Objects contain keys/values in pairs.  
Keys and values are separated by a colon.  
To read more about JSON, visit: [json.org](https://www.json.org/json-en.html).
## Examples
See the [examples](./examples) folder for some easy examples, also to get some idea about how to use the app.
## Releases
This app is kind of in an early phase. Clever Template will be growing hopefully, new updates will be coming in the future.

---

Thank you for your time...  
[Back to the top](#CleverTemplate)