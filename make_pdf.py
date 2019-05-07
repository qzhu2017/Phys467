import sys, os
from shutil import copyfile
from optparse import OptionParser

notes = [
'Lectures/syllabus',
'Lectures/Lec01',
'Lectures/Lec02',
'Lectures/Lec03',
'Lectures/Lec04',
'Lectures/Lec05',
'Lectures/Lec06',
'Lectures/Lec07',
'Lectures/Lec08',
'Lectures/Lec09',
'Lectures/Lec10',
'Lectures/Lec11',
'Lectures/Lec12',
'Lectures/Lec13',
'Lectures/Lec14',
'Lectures/Lec15',
'Lectures/Lec16',
'Lectures/Lec17',
'Lectures/Lec18',
'Lectures/Lec19',
'Lectures/Lec20',
'Lectures/Lec21',
'Lectures/Lec22',
'Lectures/Lec23',
'Lectures/Lec24',
'Lectures/Lec25',
'Lectures/Lec26',
'Lectures/Lec27',
'Lectures/Lec28',
]

parser = OptionParser()
parser.add_option("-t",  "--target", dest="target", default='all',
                  help="target file, all or numbers between 0-28")
(options, args) = parser.parse_args()

if options.target == 'all':
    todo = notes
    fname = 'Phys467'
elif options.target.isdigit():
    id = int(options.target)
    todo = [notes[id]]
    if id < 10:
        fname = 'Lec0'+str(id)
    else:
        fname = 'Lec'+str(id)
texfile = fname+'.tex'
copyfile('template.tex', texfile)

with open(texfile, 'a') as f:
    for note in todo:
        f.write('\include{'+note+'}\n')
    f.write('\end{document}')

os.system('pdflatex ' + texfile)
os.system('pdflatex ' + texfile)
os.system('rm *.aux *.out *.log')
os.system('rm ' + texfile)
