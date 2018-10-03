.SUFFIXES:
.SUFFIXES: .svg  

awav = $(patsubst %.svg,%.pdf,$(wildcard *.svg))

DECO = ../main.py 

.PHONY: clean

todo: $(awav)


%.pdf: %.svg
	@echo ---- Generando el pdf con $< 
	# python $(DECO) $< $@
	inkscape -D -A $@ $<
	mv $@ ../pdf

clean:
	@echo  $(awav)
	rm -rf $(awav) 

