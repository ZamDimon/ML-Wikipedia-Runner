import pickle
import xgboost as xgb
import sys
from internal.dataset_generator import page_info

model_path = '../internal/model/0003.model'
tfidf_path = '../internal/model/0003.pkl'
bst = xgb.Booster({'nthread': 4})  # init model
bst.load_model(model_path)
tfidf = pickle.load(open(tfidf_path, 'rb'))


def get_page_predict(title):
    print(page_info.get(title))
    return tfidf.transform(page_info.get(title))


def predict(title1, predict_q2_tfidf):
    predict_q1_tfidf = get_page_predict(title1)

    X_pred = xgb.DMatrix(abs(predict_q1_tfidf - predict_q2_tfidf))
    predictions = bst.predict(X_pred)
    return predictions