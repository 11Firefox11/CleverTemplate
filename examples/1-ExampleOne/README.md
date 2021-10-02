<h1 align="center" id="CleverTemplate">Clever Template</h1>
<p align="center">Example - Start with defaults</p>
<p align="center"><img src="../../assets/icon_ct.jpg" height="175"></p>

## Introduction
This example is about the [default optional arguments](../../README.md#default-optional-arguments), and their in action use.

## Description
### Argument `help` with the app
Run `help` optional argument, just simply with the main app.
It will just print out a help about the app.

#### Terminal illustration
```console
@consoleapp:~$ CleverTemplate -h
```
```
usage: Main.py [--version] [--help] {create} ...

Clever Template - 1.0

positional arguments:
  {create}       List of available commands.
    create       Create template.

optional arguments:
  --version, -v  Shows app's version number.
  --help, -h     Shows help about the app.

For more information and help, go to the app's github page: https://github.com/11Firefox11/CleverTemplate.
```
---
### Argument `version` with the `create` command
Run `version` optional argument, just simply with the `create` command.
It will just print out the version of the command.

#### Terminal illustration
```console
@consoleapp:~$ CleverTemplate create -v
```
```
INFO: Command 'create' version: 1.0
```
---
> In this document, console based examples, '**@consoleapp:~$**' will be referenced as the main user, or/and current directory in a console, the main program (Clever Template), will be referenced as '**CleverTemplate**.  