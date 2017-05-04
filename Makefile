all:
	@echo "Compiling text"
	@pdflatex oppgave.tex > tmp.out
	@pdflatex oppgave.tex > tmp.out
	@echo "Creating bibliography"
	@biber oppgave > tmp.out
	@echo "Creating document"
	@pdflatex oppgave.tex > tmp.out
	@echo "Cleaning up directory"
	@rm -f *.aux *.log *.synctex.gz *.idx *.toc *.bbl *.bcf *.blg *.run.xml *.out *.nav *.snm *.vrb *.tdo
