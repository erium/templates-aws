
# this is a simple dict for the test pipeline in which the categories and template names are listed.
# the purpose is to ensure that the templates are found by the collect templates function.
# the actual testing of the templates happens in separate tests, so we only need the category and template names here.

expected_templates = {
    "Data Preparation": [  # category name
        "Data Preparation"  # template name
    ],
    "Prediction": [
        "Overview",
        "Regression",
    ],
    "Outlier Detection": [
        "Overview",
        "Autoencoder",
        "Bayesian Supervised",
        "Bayesian Unsupervised",
        "Supervised",
        "Unsupervised",
    ],
    "Hypothesis Testing": [
        "Overview",
        "Classical Hypothesis Testing",
        "Causal Hypothesis Testing",
        "Equation Hypothesis Testing",
    ],
    "Design of Experiments": [
        "Overview",
        "Bayesian Optimization",
        "Bayesian Modelling",
        "Classical DOE",
    ],
    "Workflow": [
        "Data Prototype",
        "Data Strategy Workshop",
    ],
    "Workspaces": [
        "Project Workspace",
        "Strategy Workspace",
    ],
}

