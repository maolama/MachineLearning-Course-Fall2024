# Machine Learning — M.Sc. Coursework (Fall 2024)

My solutions to the graduate Machine Learning course at the **Tehran Institute for Advanced Studies (TEIAS)**, Fall 2024 (Iranian year 1403). There are six assignments and a final project, each a Jupyter notebook written in Python with scikit-learn, XGBoost, and Keras/TensorFlow.

## Final Project — Applied NLP on Persian Data
The main piece of this repository. It is four industry-style problems on real, mostly Persian, text and search data:

- **Gender detection** from social media profiles. Feature engineering plus a stacked TF-IDF + XGBoost model, test F1 ≈ 0.82.
- **Topic classification** of Persian web pages. Hazm tokenization, TF-IDF and XGBoost, weighted F1 ≈ 0.76.
- **Search-log analysis** for a travel-booking service: demand by service, city and province.
- **Typo-tolerant city autocomplete.** A hybrid rule-based and probabilistic suggester that uses Levenshtein distance, prefix and fuzzy matching, Persian normalization and wrong-keyboard-layout correction. It is evaluated with Rank-Biased Overlap.

→ [Final Project/](Final%20Project/)

## Assignments
| # | Topic | Highlights |
|---|-------|-----------|
| [HW1](HW1/) | Data exploration and an end-to-end pipeline | Pandas EDA (Adult, cardiovascular), Ames house-price regression |
| [HW2](HW2/) | Classification | ROC/PR curves and threshold tuning; multi-class user behavior; multi-label with Classifier Chains |
| [HW3](HW3/) | Regression and regularization | GD vs. SGD, LASSO/Ridge interpretation, SVR, life-expectancy prediction |
| [HW4](HW4/) | Trees and ensembles | Cost-complexity pruning; malware detection with Bagging, AdaBoost and Stacking |
| [HW5](HW5/) | Unsupervised learning | Fake-news detection, customer segmentation, t-SNE, K-Modes |
| [HW6](HW6/) | Neural networks | Perceptron vs. logistic regression, MLPs, Fashion-MNIST, CIFAR-100 training techniques |

## Notes
- The notebooks were originally run on Google Colab. Data paths point to Google Drive, so adjust them to run locally.
- Datasets are included in each folder (except the topic-modeling dataset of the final project).
