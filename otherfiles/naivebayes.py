import time
import numpy as np

class NaiveBayes():

    def __init__(self) -> None:
        pass

    def fit(self,X,y):
        n_sample,n_features = X.shape
        self._classes = np.unique(y)
        n_classes = len(self._classes)


        self._mean  = np.zeros((n_classes,n_features),dtype=np.float32)
        self._var = np.zeros((n_classes,n_features),dtype=np.float32)
        self._priors = np.zeros(n_classes,dtype=np.float32)


        for idx,c in enumerate(self._classes):
            X_c = X[y == c]
            self._mean[idx] = np.mean(X_c,axis=0)
            self._var[idx] = np.var(X_c,axis=0)
            self._priors[idx] = X_c.shape[0]/float(n_sample) 

    def predict(self, X):
        y_pred = [self._predict(x) for x in X]
        return np.array(y_pred)

    def _predict(self,x):
        posteriars = []
        for idx in range(len(self._classes)):
            prior = np.log(self._priors[idx])
            posteriar = np.sum(np.log(self._pdf(idx,x)))
            posteriar = posteriar + prior
            posteriars.append(posteriar)

        return self._classes[np.argmax(posteriars)]

    def _pdf(self, class_idx,x):
        mean = self._mean[class_idx]
        var = self._var[class_idx]
        numerator = np.exp(-((x-mean)**2)/(2*var))
        denominator = np.sqrt(2*np.pi*var)
        return numerator/denominator

if __name__ == '__main__':
    st = time.time()
    from sklearn.model_selection import train_test_split
    from sklearn import datasets

    def accuracy(y_true,y_pred):
        accuracy = np.sum(y_true==y_pred)/len(y_true)
        return accuracy

    X, y = datasets.make_classification(n_samples=10000000, n_features=30,n_classes=3,random_state=123,n_informative=3)
    X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=123)

    nb = NaiveBayes()

    nb.fit(X_train,y_train)
    y_pred = nb.predict(X_test)
    print(accuracy(y_test,y_pred))
    print(time.time()-st)