<h1 align="center" id="CleverTemplate">Clever Template</h1>
<h4 align="center">Example - Hello templates</h4>
<p align="center"><img src="../../assets/icon_ct.jpg" height="175"></p>

## Introduction
This example is about creating a simple template. Beginning from setting up a [template](../../README.md#templating), to configuring a [config file](../../README.md#config-file) and then [creating](../../README.md#create) an output file.  

## Description
### Our goal
We are going to create a simple html template file, what has a header with a title, and a paragraph with a content. Then we want to create a final html file, with the title of `Hello templates`, and a content of `This was created with Clever Template`. 
### Creating the config file
First we have to create the ct config file, by the name and extension what Clever Template is currently requiring. So we created the `ct-config.json`.
  
Now, we have to add data to the file, by the [main syntax](../../README.md#main-sample-syntax-for-config-file).  
  
Our [`PATH_TO_TEMPLATEFILE`](../../README.md#path_to_templatefile) will be simply just `hello.html`, because we are going to name our html file like that:
```js
{
    "hello.html":{}
}
```
  
Inside this file key, we are going to add two [`VARIABLE`](../../README.md#variable), `title`, and `content`, because these are the two variables we are going to need to reach our goal, and also we are going to create an empty array for these variables: 
```js
{
    "hello.html":{
        "title":[],
        "content":[]
    }
}
```
  
And for our last step, we are going to define the variables [VARIABLETYPE](../../README.md#variabletype) and [DEFAUTVALUE](../../README.md#defaultvalue). Both of these variables type are going to be `text`. The default value for `title` is going to be `"The title"`, and for the `content` it will be `"Some content"`:
```js
{
    "hello.html":{
        "title":["text", "The title"],
        "content":["text", "Some content"]
    }
}
```
And now we are done with the [config file](assets/ct-config.json). 
### Creating the html template
First thing to do, we have to create the main file. It can be named anything, let's name it `hello` this time. So we created `hello.html`.  
  
Now, let's add the h1 and p tag into the `hello.html` file:  
```html
<!--Content of `hello.html`-->
<h1></h1>
<p></p>
```
  
Next, we need to add content inside the tags. We want to add variables from Clever Template input. For this, we have to use [Jinja2 templating](https://jinja.palletsprojects.com/en/3.0.x/templates/). Since variables from Clever Template input will be passed as `ctdata`, we have to use `ctdata.VARIABLE`. We are going to use `ctdata.title` and `ctdata.content`, because we created these variables in the [config file](#creating-the-config-file). To get the value of variables with jinja2, we have to use `{{ VARIABLE }}`:
```html
<!--Content of `hello.html`-->
<h1>{{ ctdata.title }}</h1>
<p>{{ ctdata.content }}</p>
```
And now we are done with the [html template file](assets/hello.html).
### Creating the final file with Clever Template
For creating a file from template, we have to use a command inside Clever Template, named [`create`](../../README.md#create). We are going to run this command with the path of the config file, lets say it is now in this current directory, so we are going to pass `.` as the `path` argument: 
```console
@consoleapp:~$ CleverTemplate create .
```
```
INFO: Scanning config file at path: '.\ct-config.json'...
INFO: Scanning done.
INFO: Editing '.\hello.html' parameters:
INFO: Type: `!ml` for multi line input, and type `!q` for exiting multi line input mode!
INPUT: Parameter: 'title', type: 'text', default value: 'The title:': ▯
```
After Clever Template scanned our config file, it is going to ask one by one for input, for the parameter value. We are going to write in the texts, what were mentioned [upper](#creating-the-config-file):
```console
@consoleapp:~$ CleverTemplate create .
```
```
INFO: Scanning config file at path: '.\ct-config.json'...
INFO: Scanning done.
INFO: Editing '.\hello.html' parameters:
INFO: Type: `!ml` for multi line input, and type `!q` for exiting multi line input mode!
INPUT: Parameter: 'title', type: 'text', default value: 'The title:': Hello templates
INFO: Type: `!ml` for multi line input, and type `!q` for exiting multi line input mode!
INPUT: Parameter: 'content', type: 'text', default value: 'Some content:': This was created with Clever Template
INFO: Finished with '.\hello.html'.
INFO: Creating template '.\hello.html'.
INFO: Template created at '.\ct-output\hello.html', with parameters: '{'title': 'Hello templates', 'content': 'This was created with Clever Template'}'.
```
As the app says, we have successfully created our final file. It gives us the path to the file too! Now if we look at our [final file](assets/hello.html), we are going to see that Clever Template filled our template with data:
```html
<h1>Hello templates</h1>
<p>This was created with Clever Template</p>
```
And now we are done with the [final html file](assets/hello.html).
> In this document, console based examples, '**@consoleapp:~$**' will be referenced as the main user, or/and current directory in a console, the main program (Clever Template), will be referenced as '**CleverTemplate**.  
> All the mentioned files what are created, are in this directory's [assets folder](./assets).