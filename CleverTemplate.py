import os, argparse, pathlib, traceback
from modules import ManageConfigs, ManageLogs, ManageTemplates

mainpath = os.path.dirname(os.path.realpath(__file__))
version = "1.0"
commands = {
    "create":{"args": {"path":{"help":"Specify path to the ct-config.json."}},"desc":"Create a template, by giving the path of the ct-config.json.", "help":"Create template."},
    "log":{"args": {"path":{"help":"Specify the output directory.", "default":"."}, "logtype":{"help":"Specify the logtype.", "default":"templates"}}, "desc":"Save log to a txt file, by giving the output directory path and the log type. The logs are created automatically by the app.", "help":"Save txt file about a log."}
}

def InitArgparse():
    parser = argparse.ArgumentParser(add_help=False, description=f"Clever Template - {version}") # epilog="For more information, read the documentation, or go to the official website."
    subparsers = parser.add_subparsers(help='Available commands.')
    for command in commands:
        commanddict = commands[command]
        commandparse = subparsers.add_parser(command, help=commanddict["help"], add_help=False, description=commanddict["desc"])
        for arg in commanddict["args"]:
            argdict = commanddict["args"][arg]
            if "default" not in argdict:
                argdict["default"] = None
            commandparse.add_argument(arg, help=argdict["help"], default=argdict["default"])
        commandparse.add_argument('--help', '-h', action='help', default=argparse.SUPPRESS, help=f"Show help about this command ({command}).")
        commandparse.set_defaults(func=globals()[command])
    parser.add_argument('--version','-v', action='version',version=f"Clever Template version: {version}", help="Shows app's version number.")
    parser.add_argument('--help','-h', action='help', default=argparse.SUPPRESS, help='Shows help about the app.')
    args = parser.parse_args()
    try:
        args.func(args)
    except Exception as e:
        if e.__class__.__name__ == "AttributeError":
            parser.print_help()
        else:
            print(e)

def log(args):
    path = ManageLogs.WriteLogs(args.path, args.logtype)
    outputpath = os.path.abspath(path)
    print(f"Log txt file successfully created at '{outputpath}''.")

def create(args):
    data, skips = ManageConfigs.GroupParameters(args.path)
    outputdir = os.path.abspath(os.path.join(pathlib.Path(ManageConfigs.CheckPath(args.path)).parent, "ct-output"))
    print(outputdir)
    for file in skips:
        for parameter in skips[file]:
            print(f"Skipped {parameter} at {file} while checking config file syntax. {skips[file][parameter]}")
    customdata = {}
    if data:
        for file in data:
            print(f"Editing '{file}' parameters:")
            params = {}
            for param in data[file]:
                print(f"Parameter: '{param}', type: '{data[file][param][0]}', default value: '{data[file][param][1]}'")
                params[param] = input("Type in the value of the parameter: ")
            customdata[file] = params
        customdata = ManageConfigs.CheckCustomParameters(args.path, customdata)
        for file in customdata:
            print(f"Creating template {file}...")
            templatefile = os.path.join(os.path.split(ManageConfigs.CheckPath(args.path))[0], file)
            path = ManageTemplates.SaveTemplate(outputdir, ManageTemplates.CreateTemplate(templatefile, customdata[file]), file)
            print(f"Template created: {path}. Parameters: {str(customdata[file])}")
            ManageLogs.LogTemplate(os.path.abspath(templatefile), path, str(customdata[file]))

if __name__ == "__main__":
    InitArgparse()