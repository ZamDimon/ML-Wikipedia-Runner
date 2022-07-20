def predict(title1, title2):
    model_path = '0001.model'
    tfidf_path = "tfidf.pkl"
    bst = xgb.Booster({'nthread': 4})  # init model
    bst.load_model('0001.model')
    tfidf = pickle.load(open("tfidf.pkl",'rb'))
    #preprocessing
    predict_q1_tfidf = tfidf.transform(page_info.get(title1))
    predict_q2_tfidf = tfidf.transform(page_info.get(title2))
    X_pred = xgb.DMatrix(abs(predict_q1_tfidf - predict_q2_tfidf))
    predictions = bst.predict(X_pred)
    return predictions