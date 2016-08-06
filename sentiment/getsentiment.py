#!/usr/bin/env python

from empythy import EmpathyMachines;

nlp_classifier = EmpathyMachines()


import sys
if len(sys.argv) <= 1:
	print "\nUsage: python getsentiment.py input_text";
	exit();

print "training..."
nlp_classifier.train()

print "done predicting..."
text=sys.argv[1]
res=nlp_classifier.predict(text)
print "Sentiment for \"%s\" is %s" % (text,res)

