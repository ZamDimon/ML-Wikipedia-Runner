import pickle
import xgboost as xgb
import sys
from internal.dataset_generator import page_info
def predict(title1, title2):
    print(sys.path)
    model_path = '../internal/model/0001.model'
    tfidf_path = '../internal/model/tfidf.pkl'
    bst = xgb.Booster({'nthread': 4})  # init model
    bst.load_model(model_path)
    tfidf = pickle.load(open(tfidf_path,'rb'))
    #preprocessing
    
    predict_q1_tfidf = tfidf.transform(page_info.get(title1))
    predict_q2_tfidf = tfidf.transform(page_info.get(title2))
    X_pred = xgb.DMatrix(abs(predict_q1_tfidf - predict_q2_tfidf))
    predictions = bst.predict(X_pred)
    return predictions