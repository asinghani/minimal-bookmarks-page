.PHONY: generate
generate:
	python3 generate.py config.txt

.PHONY: edit
edit:
	${EDITOR} config.txt
	python3 generate.py config.txt
