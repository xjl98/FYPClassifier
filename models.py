from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
import sklearn.metrics as metrics


# MULTINOMIAL NAIVE BAYES MODEL
from options import printOptions


def runBayes(X_train, trainStances, X_test):                        # get bayes model, train, test
    model = MultinomialNB()
    model.fit(X_train, trainStances)
    return model.predict(X_test)


def evalBayes(predictions, testStances, features):                  # evaluate model with f1 scores
    print("Naive Bayes Model")
    printOptions(features)
    print("Micro F1-Score: ", metrics.f1_score(testStances, predictions, average='micro'))
    print("Macro F1-score: ", metrics.f1_score(testStances, predictions, average='macro'))
    print("Number of instances correctly determined: ",
          metrics.accuracy_score(testStances, predictions, normalize=False))

# LOGISTIC REGRESSION MODEL

def runLogReg(X_train, trainStances, X_test):                       # get logreg, train, test
    model = LogisticRegression(solver='lbfgs', multi_class='auto')
    model.fit(X_train, trainStances)
    return model.predict(X_test)


def evalLogReg(predictions, testStances, features):                 # evaluation
    print("Logistic Regression Model")
    printOptions(features)
    print("Micro F1-score: ", metrics.f1_score(testStances, predictions, average='micro'))
    print("Macro F1-score: ", metrics.f1_score(testStances, predictions, average='macro'))

    print("Number of instances correctly determined: ",
          metrics.accuracy_score(testStances, predictions, normalize=False))

# SUPPORT VECTOR MACHINE MODEL

def runSVM(X_train, trainStances, X_test):                          # get svm, train, test
    model = SVC(kernel='rbf', C=1, gamma=1)
    model.fit(X_train, trainStances)
    return model.predict(X_test)


def evalSVM(predictions, testStances, features):                    # evaluation
    print("Support Vector Machine")
    printOptions(features)
    print("Micro F1-score: ", metrics.f1_score(testStances, predictions, average='micro'))
    print("Macro F1-score: ", metrics.f1_score(testStances, predictions, average='macro'))
    print("Number of instances correctly determined: ",
          metrics.accuracy_score(testStances, predictions, normalize=False))
