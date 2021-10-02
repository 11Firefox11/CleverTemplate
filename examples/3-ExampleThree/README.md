<h1 align="center" id="CleverTemplate">Clever Template</h1>
<h4 align="center">Example - Creating email template</h4>
<p align="center"><img src="../../assets/icon_ct.jpg" height="175"></p>

## Introduction
This example is about creating a simple email template. Beginning from setting up a [template](../../README.md#templating), to configuring a [config file](../../README.md#config-file) and then [creating](../../README.md#create) an output file.

## Description
### Our goal
We are going to create a simple txt file, what will conatin a sample text, about what work we have done, and how much hour it was taking for us to do that work. So there will be a name for our work, and there will be a time period. For our first email text, we for example done work named by `Annual Report` and it took us `18` hours to do.
### Creating the config file
First we have to create the ct config file, by the name and extension what Clever Template is currently requiring. So we created the `ct-config.json`.
  
Now, we have to add data to the file, by the [main syntax](../../README.md#main-sample-syntax-for-config-file).  
  
Our [`PATH_TO_REMPLATEFILE`](../../README.md#path_to_templatefile) will be simply just `work_email.txt`, because we are going to name our txt file like that:
```js
{
    "work_email.txt":{}
}
```
  
Inside this file key, we are going to add two [`VARIABLE`](../../README.md#variable), `work_name`, and `hours`, because these are the two variables we are going to need to reach our goal, and also we are going to create an empty array for these variables: 
```js
{
    "work_email.txt":{
        "work_name":[],
        "hours":[]
    }
}
```
  
And for our last step, we are going to define the variables [VARIABLETYPE](../../README.md#variabletype) and [DEFAUTVALUE](../../README.md#defaultvalue). The first variable `work_name` will have a type of `text`, because it will be a text about the work name, and the second variable `hours` will have a type of `number`, because we want it to indicate a number, refeering how many hours did it for us, to do this work. We are not going to set default values for these variables, we will let Clever Template to fill that in for us:
```js
{
    "work_email.txt":{
        "work_name":["text"],
        "hours":["number"]
    }
}
```
And now we are done with the [config file](assets/ct-config.json). 
### Creating the txt template
First thing to do, we have to create the main file. Let's name it `work_email`. So we created `work_email.txt`.
  
Not let's add the default text into the file:
```
Dear David,
I have done my work , it only took me about  hours to make. I am sending the  files with this email!

I look forward to receiving your reply.
Tömő Viktor
```
  
Next, we need to add our custom variables into their place. For this, we have to use [Jinja2 templating](https://jinja.palletsprojects.com/en/3.0.x/templates/). Since variables from Clever Template input will be passed as `ctdata`, we have to use `ctdata.VARIABLE`. We are going to use `ctdata.work_name` and `ctdata.hours`, because we created these variables in the [config file](#creating-the-config-file). To get the value of variables with jinja2, we have to use `{{ VARIABLE }}`:
```
Dear David,
I have done my work {{ ctdata.work_name }}, it only took me about {{ ctdata.hours }} hours to make. I am sending the {{ ctdata.work_name }} files with this email!

I look forward to receiving your reply.
Tömő Viktor
```
And now we are done with the [txt template file](assets/work_email.txt).
### Creating the final file with Clever Template
For creating a file from template, we have to use a command inside Clever Template, named [`create`](../../README.md#create). We are going to run this command with the path of the config file, lets say it is now in this current directory, so we are going to pass `.` as the `path` argument: 
```console
@consoleapp:~$ CleverTemplate create .
```
```
INFO: Scanning config file at path: '.\ct-config.json'...
INFO: Scanning done.
INFO: Editing '.\work_email.txt' parameters:
INFO: Type: `!ml` for multi line input, and type `!q` for exiting multi line input mode!
INPUT: Parameter: 'work_name', type: 'text', default value: 'None:': ▯
```
After Clever Template scanned our config file, it is going to ask one by one for input, for the parameter value. We are going to write in the texts, what were mentioned [upper](#creating-the-config-file):
```console
@consoleapp:~$ CleverTemplate create .
```
```
INFO: Scanning config file at path: '.\ct-config.json'...
INFO: Scanning done.
INFO: Editing '.\work_email.txt' parameters:
INFO: Type: `!ml` for multi line input, and type `!q` for exiting multi line input mode!
INPUT: Parameter: 'work_name', type: 'text', default value: 'None:': Annual Report
INFO: Type: `!ml` for multi line input, and type `!q` for exiting multi line input mode!
INPUT: Parameter: 'hours', type: 'number', default value: '1:': 18
INFO: Finished with '.\work_email.txt'.
INFO: Creating template '.\work_email.txt'.
INFO: Template created at '.\ct-output\work_email.txt', with parameters: '{'work_name': 'Annual Report', 'hours': 18}'.
```
As the app says, we have successfully created our final file. It gives us the path to the file too! Now if we look at our [final file](assets/work_email.txt), we are going to see that Clever Template filled our template with data:
```
Dear David,
I have done my work Annual Report, it only took me about 18 hours to make. I am sending the Annual Report files with this email!

I look forward to receiving your reply.
Tömő Viktor
```
And now we are done with the [final txt file](assets/work_email.txt).
> In this document, console based examples, '**@consoleapp:~$**' will be referenced as the main user, or/and current directory in a console, the main program (Clever Template), will be referenced as '**CleverTemplate**.  
> All the mentioned files what are created, are in this directory's [assets folder](./assets).