import os, sys, argparse, ManageConfigs, ManageLogs, ManageTemplates

def create():
    try:
        data, skips = ManageConfigs.GroupParameters(args.path)
        for file in skips:
            for parameter in skips[file]:
                print(f"Skipped {parameter} at {file} while checking config file syntax. {skips[file][parameter]}")
        customdata = {}
        if data:
            for file in data:
                print(f"Editing '{file}' parameters:")
                params = {}
                for param in data[file]:
                    print(f"Parameter: '{param}', '{data[file][param]}'")
                    params[param] = input("Type in the value of the parameter: ")
                customdata[file] = params
            customdata = ManageConfigs.CheckCustomParameters(args.path, customdata)
            for file in customdata:
                print(f"Creating template {file}...")
                templatefile = os.path.join(os.path.split(ManageConfigs.CheckPath(args.path))[0], file)
                path = ManageTemplates.SaveTemplate(file, ManageTemplates.CreateTemplate(templatefile, customdata[file]))
                print(f"Template created: {path}.")
    except Exception as e:
        print(e)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument("command", help="Command list: create.")
    parser.add_argument("--path", help="Path to the ct-config.json", default="./ct-config.json")
    parser.add_argument('-v', '--version', action='version',
                    version='Clever Template: BETA', help="Shows program's version number.")
    parser.add_argument('-h', '--help', action='help', default=argparse.SUPPRESS,
                    help='Show help about the program.')
    args = parser.parse_args()
    globals()[args.command]()