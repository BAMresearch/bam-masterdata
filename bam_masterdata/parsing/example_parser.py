from bam_masterdata.parsing import AbstractParser


class MyParser1(AbstractParser):
    def parse(self, files: list[str], collection):
        for file in files:
            # Logic to parse the file and add data to the collection
            print(f"Parsing {file} and adding to {collection}")
