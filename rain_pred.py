def rain_prediction(var, var1):
    import numpy as np
    import pandas as pd

    raindata = pd.read_csv('rainfall in india 1901-2015.csv')

    raindata.head()

    raindata = raindata[raindata['SUBDIVISION'] == var]
    raindata

    # var1 = 'FEB'
    var2 = 'YEAR'
    raindata = raindata[['SUBDIVISION', var1, var2, 'ANNUAL']]

    mean_value = raindata['ANNUAL'].mean()
    mean_value1 = raindata[var1].mean()
    raindata['ANNUAL'].fillna(value=mean_value, inplace=True)
    raindata[var1].fillna(value=mean_value1, inplace=True)
    raindata.isnull().sum()

    X = raindata[['YEAR', 'ANNUAL']]
    y = raindata[var1]

    from sklearn.model_selection import train_test_split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

    # X_train = X_train.values.reshape(-1,1)
    # X_test = X_test.values.reshape(-1,1)

    from sklearn import preprocessing
    from sklearn import utils

    lab_enc = preprocessing.LabelEncoder()
    encoded = lab_enc.fit_transform(y_train)
    encoded1 = lab_enc.fit_transform(y_test)
    encoded3 = lab_enc.fit_transform(X_train['ANNUAL'])
    utils.multiclass.type_of_target(y_train.astype('int'))
    utils.multiclass.type_of_target(y_test.astype('int'))
    utils.multiclass.type_of_target(X_train['ANNUAL'].astype('int'))
    y_train = encoded
    y_test = encoded1
    X_train['ANNUAL'] = encoded3

    # Default Random forest classifier

    from sklearn.tree import DecisionTreeClassifier
    clf = DecisionTreeClassifier()

    clf.fit(X_train, y_train)

    subdata = pd.read_csv('Subdata.csv')
    subdata.head()


    subdata = subdata[subdata['SUBDIVISION'] == var]
    subdata

    subdata = subdata[['SUBDIVISION', var1, var2, 'ANNUAL']]
    X_subdata = subdata[['YEAR', 'ANNUAL']]
    X_subdata

    pred = clf.predict(X_subdata)

    # print("Average Rainfall (Decision Tree) of ",var," For ",var1," is ", pred[6]," mm")

    #####################################################################################################################################

    raindata1 = pd.read_csv('rainfall in india 1901-2015.csv')

    raindata1.head()

    raindata1 = raindata1[raindata1['SUBDIVISION'] == var]
    raindata1

    raindata1 = raindata1[['SUBDIVISION', var1, var2, 'ANNUAL']]

    mean_value = raindata1['ANNUAL'].mean()
    mean_value1 = raindata1[var1].mean()
    raindata1['ANNUAL'].fillna(value=mean_value, inplace=True)
    raindata1[var1].fillna(value=mean_value1, inplace=True)
    raindata1.isnull().sum()

    X = raindata1[['YEAR', 'ANNUAL']]
    y = raindata1[var1]

    from sklearn.model_selection import train_test_split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

    from sklearn import preprocessing
    from sklearn import utils

    lab_enc = preprocessing.LabelEncoder()
    encoded = lab_enc.fit_transform(y_train)
    encoded1 = lab_enc.fit_transform(y_test)
    encoded3 = lab_enc.fit_transform(X_train['ANNUAL'])
    utils.multiclass.type_of_target(y_train.astype('int'))
    utils.multiclass.type_of_target(y_test.astype('int'))
    utils.multiclass.type_of_target(X_train['ANNUAL'].astype('int'))
    y_train = encoded
    y_test = encoded1
    X_train['ANNUAL'] = encoded3

    subdata1 = pd.read_csv('Subdata.csv')

    subdata1.head()

    subdata1 = subdata1[subdata1['SUBDIVISION'] == var]
    subdata1

    subdata1 = subdata1[['SUBDIVISION', var1, var2, 'ANNUAL']]
    X_subdata1 = subdata1[['YEAR', 'ANNUAL']]
    X_subdata1

    from sklearn.ensemble import RandomForestClassifier
    clf1 = RandomForestClassifier()
    clf1.fit(X_train, y_train)
    pred1 = clf1.predict(X_subdata1)

    # print("Average Rainfall (Random Forest) of ",var11," For ",var1," is ", pred1[6]," mm")

    print("Rainfall of ", var, " is ", (pred[0] + pred1[0]) / 2)
    return (pred[0] + pred1[0]) / 2
    # See PyCharm help at https://www.jetbrains.com/help/pycharm/

