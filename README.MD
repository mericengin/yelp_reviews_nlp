# Yelp Reviews NLP Classification Project

## Overview
This project implements Natural Language Processing (NLP) techniques to classify Yelp reviews into 1-star or 5-star categories based on review text content. The project uses various machine learning models including Multinomial Naive Bayes, Support Vector Machines and Random Forest Classifier.

## Dataset
The project uses the [Yelp Review Dataset from Kaggle](https://www.kaggle.com/c/yelp-recsys-2013), which includes:
- Business reviews
- Star ratings (1-5)
- Engagement metrics (cool, useful, funny votes)
- Review text

## Features
- Text preprocessing using CountVectorizer and TF-IDF
- Machine learning pipeline implementation
- Model comparison between Naive Bayes, Random Forest and Support Vector Machine
- Comprehensive EDA (Exploratory Data Analysis)
- Performance metrics evaluation

## Technical Stack
- Python 3.x
- Libraries:
  - pandas
  - matplotlib
  - seaborn
  - scikit-learn

## Key Findings
- Random Forest Classifier achieved better overall performance (84% accuracy)
- Naive Bayes showed strong bias towards 5-star predictions
- Text length correlates with review ratings
- Significant class imbalance between 1-star and 5-star reviews
- SVM model exhibited:
    - High precision for predicting 1-star reviews (96%) but lower recall (59%) for the same class, indicating it missed a significant number of 1-star predictions.
    - High recall for 5-star reviews (99%) but slightly lower precision (91%), suggesting the model tended to predict more 5-star reviews, some of which were false positives.
    - Overall accuracy of 92%, with a notable performance gap between the two classes. 
    - Macro average F1-score of 0.84, highlighting the imbalance in class performance.
    - Weighted average F1-score of 0.91, showing the model’s solid overall performance despite the class imbalance.

## Usage
Run the Jupyter notebook `yelp_reviews_nlp.ipynb` to see the complete analysis and model implementation.

## Results
### Random Forest Classifier
- Accuracy: 84%
- Better balanced performance across classes
- Strong precision for both classes

### Naive Bayes
- Accuracy: 81%
- Perfect recall for 5-star reviews
- Poor performance on 1-star reviews

## Future Improvements
- Address class imbalance
- Implement more advanced text preprocessing
- Feature engineering for better 1-star detection