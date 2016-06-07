import os
import sys

if (len(sys.argv)<3):
    print "Needs three arguments, all directories full of images\n";
    print "Will spew a bunch of LaTeX to stdout\n";
    print "Try redirecting that to a file e.g.\n\n\n";
    print "python makebook.py dir1/ dir2/ dir3/ > book.tex\n";
else:

    directory1=os.path.abspath(os.path.join(os.getcwd(), sys.argv[1]))
    directory2=os.path.abspath(os.path.join(os.getcwd(), sys.argv[2]))
    directory3=os.path.abspath(os.path.join(os.getcwd(), sys.argv[3]))

    files3=os.listdir(directory3)
    files2=os.listdir(directory2)
    files1=os.listdir(directory1)

    files1.sort()
    files2.sort()
    files3.sort()

    print("\\documentclass{minimal}\n\n")
    print("\\usepackage{graphicx}\n\n")

    print("\\begin{document}")
    print("\\begin{flushright}")
    #iterate by id
    for i in range(0,len(files1)):
        #multiple copies of file1
        print("\\begin{tabular}{| r |}")
        print("\\hline")
        print("%d\\\\ \\vspace{2em} \\\\" %i)
        print("\\hline")
        print("\\includegraphics[width=10cm]{%s/%s} \\\\" %(directory1, files1[i]))
        print("\\hline")
        print("\\hline")
        print("%d\\\\ \\vspace{2em} \\\\" %i)
        print("\\hline")
        print("\\includegraphics[width=10cm]{%s/%s} \\\\" %(directory2, files2[i]))
        print("\\hline")
        print("\\hline")
        print("%d\\\\ \\vspace{2em} \\\\" %i)
        print("\\hline")
        print("\\includegraphics[width=10cm]{%s/%s} \\\\" %(directory3, files3[i]))
        print("\\hline")
        print("\\end{tabular}")
        #pagebreak
        print("\\newpage")

    print("\\end{flushright}")
    print("\\end{document}")

