import os
import sys

if (len(sys.argv)<3):
    print "Needs two arguments, both directories full of images\n";
else:

    directory1=os.path.abspath(os.path.join(os.getcwd(), sys.argv[1]))
    directory2=os.path.abspath(os.path.join(os.getcwd(), sys.argv[2]))

    files2=os.listdir(directory2)
    files1=os.listdir(directory1)

    #sort files1 ascending, sort files2 descending

    files1.sort()
    files2.sort()
    files2.reverse()

    print("\\documentclass{minimal}\n\n")
    print("\\usepackage{graphicx}\n\n")

    print("\\begin{document}")
    print("\\clearpage")
    #iterate by id
    for i in range(0,len(files1)):
        #multiple copies of file1
        print("\\begin{tabular}{| c |}")
        print("\\hline")
        print("%d\\\\" %i)
        print("\\hline")
        print("\\includegraphics[width=10cm]{%s/%s} \\\\" %(sys.argv[1], files1[i]))
        print("\\hline")
        print("\\hline")
        print("%d\\\\" %i)
        print("\\hline")
        print("\\includegraphics[width=10cm]{%s/%s} \\\\" %(sys.argv[1], files1[i]))
        print("\\hline")
        print("\\hline")
        print("%d\\\\" %i)
        print("\\hline")
        print("\\includegraphics[width=10cm]{%s/%s} \\\\" %(sys.argv[1], files1[i]))
        print("\\hline")
        print("\\end{tabular}")
        #pagebreak
        print("\\newpage")
        #multiple copies of file2
        print("\\begin{tabular}{| c |}")
        print("\\hline")
        print("%d\\\\" %i)
        print("\\hline")

        print("\\includegraphics[width=10cm,angle=180]{%s/%s} \\\\" %(sys.argv[2], files2[i]))
        print("\\hline")
        print("\\hline")
        print("%d\\\\" %i)
        print("\\hline")
        print("\\includegraphics[width=10cm,angle=180]{%s/%s} \\\\" %(sys.argv[2], files2[i]))
        print("\\hline")
        print("\\hline")
        print("%d\\\\" %(i))
        print("\\hline")
        print("\\includegraphics[width=10cm,angle=180]{%s/%s} \\\\" %(sys.argv[2], files2[i]))
        print("\\hline")
        print("\\end{tabular}")
        print("\\newpage")

    print("\\end{document}")

