# Scikit-Learn Lab

This lab teaches the reasoning behind a reliable classical machine-learning
workflow. The first goal is not to collect estimators: it is to learn how to
define an experiment whose result can be trusted.

## Learning objectives

After these lessons, a reader should be able to:

- distinguish features, targets, parameters, and hyperparameters;
- reserve a test set and explain why it must not guide model selection;
- preserve class proportions with a stratified split;
- combine preprocessing and an estimator in a `Pipeline`;
- explain how a pipeline prevents data leakage during cross-validation;
- interpret a confusion matrix, precision, recall, and ROC AUC;
- use cross-validation to report both average performance and variability;
- tune hyperparameters with `GridSearchCV` using an appropriate metric.

## Prerequisites and setup

Complete the Python standard-library foundations and the NumPy track first.
From the repository root, create or activate a virtual environment and run:

```powershell
python -m pip install -r .\Python\requirements\scikit-learn.txt
```

The lessons use a dataset bundled with scikit-learn and need no network access.

## Lesson index

| File | Main topic | Exam question it addresses |
| --- | --- | --- |
| `000_classification_workflow.py` | Split, pipeline, metrics, cross-validation | How do we estimate generalization without leakage? |
| `001_model_selection.py` | Grid search and final evaluation | How do we select hyperparameters without tuning on the test set? |
| `002_regression_workflow.py` | Ridge regression, MAE, RMSE, R² | How do regression metrics describe different errors? |
| `003_mixed_data_preprocessing.py` | Missing and categorical values | How do we preprocess different column types without leakage? |
| `004_clustering_and_pca.py` | Scaling, PCA, K-means, clustering metrics | How do we evaluate structure when labels are not used for training? |

Run the lessons from the repository root:

```powershell
python .\Python\scikit_learn\000_classification_workflow.py
python .\Python\scikit_learn\001_model_selection.py
python .\Python\scikit_learn\002_regression_workflow.py
python .\Python\scikit_learn\003_mixed_data_preprocessing.py
python .\Python\scikit_learn\004_clustering_and_pca.py
```

## The experimental protocol

A supervised dataset contains a feature matrix `X` and a target vector `y`.
Rows are observations; columns are features. An estimator learns model
parameters from training data. Choices such as regularization strength are
hyperparameters.

Use this sequence:

1. Define the prediction task and metric before inspecting results.
2. Hold out the test set once.
3. Fit preprocessing only on training data.
4. Use cross-validation within training data for comparison and tuning.
5. Refit the selected pipeline on all training data.
6. Evaluate once on the untouched test set.

Repeatedly choosing models because they improve the test score turns the test
set into validation data and makes the final estimate optimistic.

## Pipelines and leakage

Data leakage occurs when training uses information that would be unavailable
for a genuinely new observation. Scaling all rows before splitting, for
example, lets test-set statistics influence the transformed training values.

A pipeline treats preprocessing and prediction as one estimator. During
cross-validation, scikit-learn fits the complete pipeline on each training
fold. The scaler therefore does not see that fold's validation rows. Imputation,
feature selection, dimensionality reduction, and learned encodings belong
inside the pipeline for the same reason.

## Splits and cross-validation

`train_test_split(..., stratify=y)` approximately preserves class proportions.
A fixed `random_state` makes the demonstration repeatable; it does not make one
split universally representative.

K-fold cross-validation uses every fold for validation once and the remaining
folds for fitting. Report the mean and spread. Random splitting is inappropriate
when observations have time order, groups, or repeated measurements; use a
time-series or group-aware splitter so related data cannot cross the boundary.

## Classification metrics

For a chosen positive class, the confusion matrix counts true negatives, false
positives, false negatives, and true positives.

- **Accuracy** is the fraction of all correct predictions. It can hide failure
  on a rare class.
- **Precision** is `TP / (TP + FP)`: among predicted positives, how many were
  positive?
- **Recall** is `TP / (TP + FN)`: among actual positives, how many were found?
- **F1** is the harmonic mean of precision and recall.
- **ROC AUC** evaluates score ranking across thresholds, not the quality of one
  selected threshold.

Metric choice expresses the cost of errors. With severe class imbalance, also
inspect precision-recall curves and average precision.

## Model selection

`GridSearchCV` evaluates declared hyperparameter combinations by
cross-validation. Pipeline parameters use `step__parameter` names, such as
`classifier__C`. Its best cross-validation score is a selection estimate, not
the final test result. Nested cross-validation is appropriate when an unbiased
estimate of the complete selection procedure is required and data is limited.

## Regression and regularization

Regression predicts a continuous target. A residual is `actual - predicted`;
different metrics summarize residuals differently:

- **MAE** averages absolute errors and remains in the target's units.
- **MSE** squares errors, so a few large errors receive much more weight.
- **RMSE** is the square root of MSE and returns to the target's units.
- **R²** compares the model with predicting the target mean. `1` is perfect,
  `0` matches that baseline, and negative values are possible.

Ridge regression minimizes squared error plus an L2 penalty on coefficient
magnitude. `alpha=0` removes the penalty; a larger `alpha` increases shrinkage.
Scaling matters because a penalty on coefficient size depends on feature units.

Scikit-learn names loss scorers with a `neg_` prefix because its selection API
maximizes every score. Convert them back to positive errors when reporting.

## Mixed data and missing values

Real tables often combine numeric and categorical columns. A
`ColumnTransformer` sends selected columns through separate pipelines:

- numeric values can be median-imputed and standardized;
- categorical values can be mode-imputed and one-hot encoded;
- the transformed columns are then joined for the estimator.

The complete transformer belongs inside the model pipeline. Otherwise medians,
categories, or feature-selection decisions can leak across validation folds.
`OneHotEncoder(handle_unknown="ignore")` also permits categories that appear
only after training, although domain monitoring should still record them.

Missingness is not automatically random. Imputation makes a dataset usable but
does not repair sampling bias or prove that discarded information is harmless.

## PCA and clustering

Principal component analysis creates orthogonal directions of decreasing
variance. It is unsupervised: target labels are not used. Scaling before PCA is
important when feature units differ, because high-variance units could dominate
the projection. Explained variance describes retained input variance, not
predictive accuracy or causal importance.

K-means minimizes within-cluster squared distances to centroids. Consequently,
it is sensitive to feature scale, outliers, initialization, and roughly assumes
compact spherical clusters. Cluster identifiers are arbitrary; cluster `0` is
not a known class and has no natural ordering.

- **Silhouette score** is an internal measure based on cohesion and separation.
- **Adjusted Rand Index** compares clusters with external reference labels and
  corrects for chance. Those labels must not be used to fit an unsupervised model.

Neither metric proves that clusters are useful or meaningful in the domain.

## Exam checklist

Be prepared to explain:

1. Why fitting a scaler before the split is leakage.
2. Why training accuracy does not estimate generalization.
3. Why cross-validation does not remove the need for a final test set.
4. Which error type precision and recall emphasize.
5. Why imbalanced data can yield high accuracy and a useless classifier.
6. The difference between learned parameters and selected hyperparameters.
7. Why time series and grouped observations need specialized splitters.
8. Why a metric must match the real cost of mistakes.
9. Why RMSE reacts more strongly to large errors than MAE.
10. How R² can be negative on evaluation data.
11. Why scaling affects Ridge, PCA, K-means, and nearest-neighbor methods.
12. Why cluster numbers cannot be compared directly with class numbers.

## Exercises

1. Compute confusion-matrix counts by hand and verify precision and recall.
2. Remove scaling and explain why scale-sensitive models change.
3. Replace logistic regression with k-nearest neighbors and tune neighbor count.
4. Change the decision threshold and record the precision-recall trade-off.
5. Compare accuracy, balanced accuracy, ROC AUC, and average precision on an
   imbalanced target.
6. Repeat the experiment with several split seeds and discuss variability.
7. Compare Ridge values of `alpha` with cross-validation and inspect coefficients.
8. Add a missingness-indicator feature and explain when it might help.
9. Plot the first two principal components and color points by cluster.
10. Compare K-means solutions for several cluster counts using silhouette score.

## Common mistakes

- Preprocessing the complete dataset before the split.
- Using the test set to choose features, hyperparameters, or a threshold.
- Reporting only the best fold or only the mean without variability.
- Treating probability estimates as calibrated without checking calibration.
- Interpreting association or predictive performance as causation.
- Comparing models on different splits and attributing all change to the model.

## Further reading

- [Scikit-learn getting started](https://scikit-learn.org/stable/getting_started.html)
- [Pipelines and composite estimators](https://scikit-learn.org/stable/modules/compose.html)
- [Cross-validation](https://scikit-learn.org/stable/modules/cross_validation.html)
- [Model evaluation](https://scikit-learn.org/stable/modules/model_evaluation.html)
- [Common pitfalls](https://scikit-learn.org/stable/common_pitfalls.html)
