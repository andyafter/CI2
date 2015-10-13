from utils import *


mac=pd.read_csv("MsiaAccidentCases.csv")
# malaysia data is for training and it contains 3 different types
print mac.columns.values
# pick couple lines
col_list = ['Cause ', 'Summary Case']
mac = mac[col_list]
print mac.columns.values
mac=mac.dropna()

# create a list which has "labelled" instances  alongwith the raw text
labelled = [row[1].tolist() for row in mac.iterrows()]

# Separate out the X (predictors) and the y (response)
X, y = create_tfidf_training_data(labelled)
# Create training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=30)

svm = train_svm(X_train, y_train)
# Predict on the Test set
pred = svm.predict(X_test)

# Print the classification rate
#print(svm.score(X_test, y_test))

labels = list(set(y_train))

# Print the confusion matrix
cm = confusion_matrix(y_test, pred, labels)

# Make a prettier Confusion Matrix
fig = plt.figure()
ax = fig.add_subplot(111)
cax = ax.matshow(cm)
fig = plt.figure()
ax = fig.add_subplot(111)
cax = ax.matshow(cm)
pl.title('Confusion matrix of the classifier')
fig.colorbar(cax)
ax.set_xticklabels([''] + labels)
ax.set_yticklabels([''] + labels)
pl.xlabel('Predicted')
pl.ylabel('True')
pl.show()

osha=pd.read_csv("osha.csv")
# Check the column values and retain only those of interest, namely "type" and "summary"

#print osha.columns.values
col_list = ['summary']
osha = osha[col_list]
#print osha.columns.values

# Remove all rows with no abstract

osha=osha.dropna()

# Create a list which has "labelled" instances  alongwith the raw text

labelled_osha=[]
for row in osha.iterrows():
    index, data = row
    labelled_osha.append(data.tolist())


# Separate out the X (predictors) and the y (response)
X_predict= create_tfidf_predict_data(labelled_osha)

# Predict on the Predict set
pred1 = svm.predict(X_predict)
