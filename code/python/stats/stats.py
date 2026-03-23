import argparse
from pathlib import Path
from xml.etree import ElementTree
from saxonche import PySaxonProcessor

parser = argparse.ArgumentParser(
                    prog='stats.py',
                    description='Genera semplici statistiche del corpus di documenti TEI (parole e caratteri spazi esclusi)',
                    epilog='')

parser.add_argument('-d', '--directory', required = True, nargs = 1, help = 'The directory containing the XML TEI documents')
parser.add_argument('-s', '--tei-styles-dir', required = True, nargs = 1, help = 'The base directory containing the official TEI XSLT Stylesheets')
parser.add_argument('-r', '--recursive', required = False, action = 'store_true', help = 'If present, the directory will be traversed recursively')

args = parser.parse_args()
# print(args)

processor = PySaxonProcessor()
xslt_processor = processor.new_xslt30_processor()
executable = xslt_processor.compile_stylesheet(stylesheet_file = args.tei_styles_dir[0] + '/txt/tei-to-text.xsl')

recurse : bool = args.recursive

documents_path = Path(args.directory[0])

file_list_generator = (dir[0] for dir in documents_path.walk()) if recurse else [documents_path]

tot_words = 0
tot_characters_without_spaces = 0
for dir in file_list_generator:
    for file in dir.iterdir():
        if file.suffix == '.xml': # TODO implement a configurable file filter instead
            document = processor.parse_xml(xml_file_name = str(file))
            text = executable.transform_to_string(xdm_node = document)
            tokens = text.strip().split()
            words = len(tokens)
            characters_without_spaces = 0
            for token in tokens:
                characters_without_spaces += len(token)

            tot_words += words
            tot_characters_without_spaces += characters_without_spaces

            print ('************************** ' + str(file) + ' **************************')
            print ('Words:                     %8d' % words)
            print ('Characters without spaces: %8d' % characters_without_spaces)
            print ('\n')

print ('************************** TOTALS **************************')
print ('Words:                     %8d' % tot_words)
print ('Characters without spaces: %8d' % tot_characters_without_spaces)
print ('\n')