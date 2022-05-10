"""Parser for arguments provided via cmd."""
import argparse


class ArgsParser:

    @staticmethod
    def parse():
        """Runs parser and get cmd."""
        parser = argparse.ArgumentParser()
        parser.add_argument('-l', '--load', dest="l", nargs='+')
        parser.add_argument('-d', '--dump', dest="d", nargs='+')
        parser.add_argument('-c', '--config', dest="c", nargs='?', default=None)
        return parser.parse_args()

    @staticmethod
    def load_from() -> list[str]:
        """Gets and returns the name of the file that will be parsed."""
        args = ArgsParser.parse()
        return args.l

    @staticmethod
    def dump_in() -> list[str]:
        """Gets and returns the name of the file that will be used to dump in"""
        args = ArgsParser.parse()
        return args.d

    @staticmethod
    def getargs():
        """Gets and returns the configurated file names"""
        args = ArgsParser.parse()

        if args.c is not None:
            args.l, args.d = ArgsParser.get_config(str(args.c))

        return args.d, args.l

    @staticmethod
    def get_config(config: str) -> list[str]:
        """Parses arguments from config file"""
        try:
            file = open(config, "r")
            configs = file.read()
        except Exception as e:
            print(e)
        finally:
            file.close()
            return configs.split("\n")