#!/usr/bin/python3

import argparse
import os
import os.path


def main():
    parser = argparse.ArgumentParser(
        description='Catkin Tools Workspace Creator')
    parser.add_argument('-w', '--workspace',
                        help='Workspace path',
                        default='../')
    parser.add_argument('-p', '--package', default=None)
    parser.add_argument('-d', '--dependencies', default="default.txt")
    parser.add_argument('-o', '--other_dependencies', default="")
    args = parser.parse_args()

    if os.path.exists(os.path.join(args.workspace, ".catkin_tools")):
        dependencies = open(
            "./dependencies/{}".format(args.dependencies)).read()
        os.chdir(os.path.join(args.workspace, "src"))
        os.system("catkin create pkg {} --catkin-deps {} {}".format(args.package,
                                                                    dependencies, args.other_dependencies))
    else:
        print("Workspace does not exist.")


if __name__ == "__main__":
    main()
