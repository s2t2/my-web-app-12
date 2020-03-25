# web_app/routes/iris_routes.py

from flask import Blueprint
from sklearn.datasets import load_iris
#from sklearn.linear_model import LogisticRegression

from web_app.iris_classifier import load_model

iris_routes = Blueprint("iris_routes", __name__)

@iris_routes.route("/stats/iris")
def iris():
    X, y = load_iris(return_X_y=True)
    #clf = LogisticRegression(random_state=0, solver='lbfgs',
    #                      multi_class='multinomial').fit(X, y)
    clf = load_model()
    return str(clf.predict(X[:2, :]))
