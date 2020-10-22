import argparse
import os
import sys
import re
import ast

# package name
PACKAGE_NAME = 'img_processing'
with open(os.path.join(os.path.dirname(__file__), '__init__.py')) as f:
    match = re.search(r'__version__\s+=\s+(.*)', f.read())
version = str(ast.literal_eval(match.group(1)))

# adding current dir to lib path
mydir = os.path.dirname(__file__)
sys.path.insert(0, mydir)

#def register_overlay(parser):
#    from overlay import setup_argument_parser, main
#    def command_overlay(args):
#        main(args)

#    setup_argument_parser(parser)
#    parser.set_defaults(handler=command_overlay)

#def register_wrinkle(parser):
#    from wrinkle import setup_argument_parser, main
#    def command_wrinkle(args):
#        main(args)
#
#    setup_argument_parser(parser)
#    parser.set_defaults(handler=command_wrinkle)

def main():
    # top-level command line parser
    parser = argparse.ArgumentParser(prog=PACKAGE_NAME.replace('_', '-'), description='Generate a defect images')
    parser.add_argument('--version', action='version', version='%(prog)s ' + version)
    subparsers = parser.add_subparsers()

    # overlay
    #parser_overlay = subparsers.add_parser('overlay', help='see `-h`')
    #register_overlay(parser_overlay)

    # wrinkle
    #parser_wrinkle = subparsers.add_parser('wrinkle', help='see `-h`')
    #register_wrinkle(parser_wrinkle)

    # to parse command line arguments, and execute processing
    args = parser.parse_args()
    if hasattr(args, 'handler'):
        args.handler(args)
    else:
        # if unknwon subcommand was given, then showing help
        parser.print_help()


if __name__ == '__main__':
    main()