from bam_masterdata.parsing import AbstractParser


class ExampleParser(AbstractParser):
    def parse(self, files, collection):
        for file in files:
            # Logic to parse the file and add data to the collection
            print(f"Parsing {file} and adding to {collection}")
