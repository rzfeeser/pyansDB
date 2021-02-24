#!/usr/bin/python3
"""Created: RZFeeser@alta3.com
   Desc: Take Python data and dump into a file as YAML data."""

# not part of the std library
# python3 -m pip install pyyaml
import yaml

def main():
    hitchhikers = [{"name": "Zaphod Beeblebrox", "species": "Betelgeusian"}, {"name": "Arthur Dent", "species": "Human"}]

    ## display our Python data (a list containing two dictionaries)
    print(hitchhikers)

    ## open a new file in write mode
    with open("galaxyguide.yaml", "w") as zfile:
        ## use the YAML library
        ## USAGE: yaml.dump(input data, file like object)
        ## unlike JSON, the YAML lib uses .dump() to create YAML strings and write to files
        ## the JSON lib uses .dump() to create a string and .dumps() to write to files
        yaml.dump(hitchhikers, zfile)

if __name__ == "__main__":
    main()