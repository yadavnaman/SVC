The basic implementation with default values of tuning parameters (kernel = linear, C = 1 and gamma = 1):
	accuracy = 0.9269
	training time = 1.66 seconds
	
To decrease the training time, we reduce the training set size to 1/10th of the original size. Of course the accuracy would decrease, but we can try to tune the three parameters: kernel, C and gamma to increase the accuracy score.

Changing kernel to rbf(radial basis function) and increasing C(regularization parameter) to 100(remains the same beyond that). In this case of exercise, the low gamma values gives us strong accuracy(It would mean the data points are sparse, far enough from decision boundary in graph plot).

The implementation with tuning parameters(kernel = "rbf", C=100, gamma=0.001):
	accuracy = 0.8884
	training time = 0.01595 seconds

A decent accuracy score can be achieved even after reducing the training data set to 1/10th (we just had 72 emails in training set and achieved 89% accuracy in testing against 350 email).