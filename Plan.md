# Project - Easy Template

## Project description
This project would be a simple console app, with small gui parts. The main idea would be to create an app, where from you can easily interact with jinja2 templates. 
You can create you own config json file, where you can customize the templates and their variables in that folder. It is just a simple way, to use variables in jinja2 templates.

## The main parts of implamenting this project
### Manage the config file
We need to manage the custom syntaxed config json files. The config files will contain file names, their parameters, and inside those parameters, what type of parameter is it, and what its default value. Types can be: text, number, boolean.
#### Manage parts:
- Read in json config file.
- Check the files in the config file, if they really exist or not.
- Group parameters by files, with checking their type, if that type really exist or not, then give them a default value, if it not exist.
- Check if custom parameter match with a config file parameter.
#### Example: 
```js
// ct-config.json
{
    "sass.py" : {
        "variable1":["text", "defaulttext"],
        "variable2":["text", "helo"],
        "variable3":["boolean"]
    },
    "main.css" : {
        "variable1":["number", "#333333"]
    }
}
```
### Manage templates by parameters
We need to manage templates, by the custom parameters. The templates has to be saved somewhere, or to be shown, output their content.
#### Manage parts:
- Create templates by parameters.
- Save templates.
- Create log about created templates.
### Manage logs
We need to manage the logs, for the app. To be able to manage our work with templates, it is a good thing to have a log, where you can see the previous actions within the app.
#### Manage parts:
- Create main log database.
- Create templates table in the database, log created templates in it.
### Manage small gui parts
We need to manage the small gui parts of the app. There will be some cases when the you will be able to use gui, to set your own parameters.
#### Manage parts:
- Create main window, or show a window.
- Show a simple gui.
- Get data from gui.
- Apply data from gui.
### Manage the main functions
We need to manage the main functions all in one. Upper, I listed all the things we need to create this simple app, now it is the time to goup up all the things into one main file, and use them. This is the actual console app part.
#### Manage parts:
- Create main console app manager. 
- Create a command for creating templates by giving main config file path and then giving parameters, after that save that template.
- Create a command for viewing the log.
- Create a command for help.

---
This would be the main plan to reach the 1.0. version of this app.