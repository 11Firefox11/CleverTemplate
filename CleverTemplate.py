import os, sys, argparse, pathlib, ManageConfigs, ManageLogs, ManageTemplates

mainpath = os.path.dirname(os.path.realpath(__file__))

def create():
    try:
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
                print(f"Template created: {path}.")
                ManageLogs.LogTemplate(os.path.abspath(templatefile), path, str(customdata[file]))
    except Exception as e:
        print(e)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument("command", help="Command list: create, help, log.")
    parser.add_argument("--path", help="Path to the ct-config.json", default="./ct-config.json")
    parser.add_argument('-v', '--version', action='version',
                    version='Clever Template: 1.0.', help="Shows program's version number.")
    parser.add_argument('-h', '--help', action='help', default=argparse.SUPPRESS,
                    help='Show help about the program.')
    args = parser.parse_args()
    globals()[args.command]()