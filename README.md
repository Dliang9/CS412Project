# CS412Project
Semester-long machine learning project performing data analysis on a mushroom database

Naïve Bayes classification:
	P(c|x) = (P(x|c) * P(c)) / P(x)

	P(c|x) <--- Posteriror Probability
	P(x|c) <--- Likelihood
	P(c)   <--- Class Prior Probability
	P(x)   <--- Predictor Prior Probability

Mushroom Object:
	Label
	Feature - color
	Probability - edible

Likelihood Probablity:
	Calculates P(x|c) from Naïve Bayes classification

Calulate Predictor Probability:
	Calculates P(x) from Naïve Bayes classification
