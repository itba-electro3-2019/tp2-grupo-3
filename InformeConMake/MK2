
INFORME = Informe
OTHER = *~ *.aux *.dvi *.toc *.bbl *.blg *.gz *.out *.thm *.ps *.idx *.ilg *.ind *.log *.fdb_latexmk *.fls

informe:
	latexmk -synctex=1 -interaction=nonstopmode -pdf $(INFORME).tex
	rm -rf $(OTHER)
clean:	
	rm -rf $(OTHER)
