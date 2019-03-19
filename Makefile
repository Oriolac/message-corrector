
SHELL:=/bin/bash
NOISE=0.2
LENGTH=40
CHECKER_NOISE=05 10 15 20 25
CORRECTOR_NOISE=05 10 15
NOISE_VALUES=$(CHECKER_NOISE)
LENGTH_VALUES=20 40 60 80 100

test-length:
	@for L in $(LENGTH_VALUES); do make test-noise LENGTH=$$L; done

test-noise:
	@for I in $(NOISE_VALUES); do make test-average NOISE=0.$$I; done

test-average:
	@for X in `seq 20`; do make test; done | grep -v Entering | grep -v Leaving | cut -c11- | ./mean.py > mean.txt
	@echo -n $(LENGTH) $(NOISE)" "; cat mean.txt

test:
#@echo Length $(LENGTH)
#@echo Noise $(NOISE)
	@./plumbus.py $(LENGTH) | tee original.txt | ./senderscribe.py | tee sent.txt | ./vitiet.py $(NOISE) | tee noisy.txt | ./receiverscribe.py > result.txt
	@./checker.py original.txt sent.txt noisy.txt result.txt

zip:
	zip nayox.zip plumbus.py vitiet.py senderscribe.py receiverscribe.py checker.py Makefile
