lastModifiedPyFile = $(shell ls -rt *\.py* | tail -1)
compile: $(lastModifiedPyFile)
	yapf -i $(lastModifiedPyFile) && python3 $(lastModifiedPyFile)
