from utils import *

# Import the file which we will use for classification
mac=pd.read_csv("MsiaAccidentCases.csv")
osha=pd.read_csv("osha.csv")


# Check the column values and retain only those of interest, namely "type" and "summary"
col_list = ['Cause ', 'Summary Case']
mac = mac[col_list]
wrong_message = 'InspectionOpen DateSICEstablishment Name'
# Create a list which has "labelled" instances  alongwith the raw text
trainset=[]
for row in mac.iterrows():
    index, data = row
    trainset.append(data.tolist())

# Check the column values and retain only those of interest, namely "type" and "summary"
col_list = ['summary']
osha = osha[col_list]
# Create a list which has "labelled" instances  alongwith the raw text
testset=[]
for row in osha.iterrows():
    index, data = row
    '''
    if wrong_message in ' '.join(data.tolist()):
        print data.tolist()
        continue
    testset.append(data.tolist())
    '''
print len(testset)

# Create datasets without labels to transform to TF-IDF Vectorizer
train_nolab = [str(t[1]).decode('latin-1').encode("utf-8") for t in trainset]
test_nolab = [str(t[0]).decode('latin-1').encode("utf-8") for t in testset]
# Create datasets with only labels to serve as "Y"
train_lab = [t[0] for t in trainset]
# Create your Vectorizer function
vectorizer = TfidfVectorizer()
#vectorizer = TfidfVectorizer(ngram_range=(1,2))
# Create TF-IDF Vectorizer from your training features
train_vectors = vectorizer.fit_transform(train_nolab)
# Transform your test features to fit your already trained TF-IDF
test_vectors = vectorizer.transform(test_nolab)
# Check the size of your features and documents for your training and test sets
train_vectors.shape
test_vectors.shape
X_train, X_test, y_train, y_test = train_test_split(train_vectors, train_lab, test_size=0.2, random_state=42)
# Create a function which will train a Support Vector Classifier
def train_svm(X, y):
    """
    Create and train the Support Vector Machine.
    """
    svm = SVC(C=5000.0, gamma=0.0, kernel='rbf')
    svm.fit(X, y)
    return svm

# Train the SVM - using all the data
sv = train_svm(X_train, y_train)
# Predict on the Test set
pred_SVM = sv.predict(X_test)
# Print the classification rate
pred = list(pred_SVM )
# Create confusion Matrix
cm = confusion_matrix(pred, y_test)
# Print Confusion Matrix
print cm
# Print Accuracy Score
print accuracy_score(pred, y_test)
# Print a classification report
print classification_report(pred,  y_test)




predSVM= sv.predict(test_vectors)
pred = list(predSVM)
