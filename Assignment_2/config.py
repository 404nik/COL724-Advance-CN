import argparse

def build_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('--com', help="Root Directory of commands")
    parser.add_argument('-o', help="Output will be saved here ")
    parser.add_argument('--id', help="client id for e.g. c1")
    parser.add_argument('--nc', help="Total clients Expected", type=int)
    return parser

def get_config():
    parser = build_parser()
    config, unparsed = parser.parse_known_args()
    return config, unparsed
