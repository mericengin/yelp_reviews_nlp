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
- Text preprocessing pipeline:
  - Punctuation removal
  - Stopwords removal
  - Text vectorization using CountVectorizer
  - TF-IDF transformation
- Machine learning models comparison:
  - Multinomial Naive Bayes
  - Random Forest Classifier
  - Support Vector Machine
- Comprehensive EDA with visualization
- Performance metrics evaluation
- Model comparison before and after text preprocessing

## Technical Stack
- Python 3.x
- Libraries:
  - pandas
  - matplotlib
  - seaborn
  - scikit-learn
  - NLTK

## Key Findings
### Before Text Preprocessing:
- Random Forest: 84% accuracy
- Naive Bayes: 81% accuracy, struggled with 1-star reviews
- SVM: 92% accuracy, best overall performance

### After Text Preprocessing:
- All models showed significant improvement
- SVM maintained best performance with better balance
- Naive Bayes showed dramatic improvement in 1-star detection
- Random Forest achieved more balanced performance across classes

### Impact of Text Preprocessing:
- Reduced noise in review text
- Improved 1-star review detection
- Created more balanced classification performance
- Narrowed performance gap between models

## Usage
1. Clone the repository
2. Install dependencies: `pip install -r requirements.txt`
3. Run the Jupyter notebook: `jupyter notebook notebooks/yelp_reviews_nlp.ipynb`

## Model Selection Guide
- Choose SVM for highest accuracy
- Choose Random Forest for balance of performance and interpretability
- Choose Naive Bayes for fast training with competitive results

## Future Improvements
- Implement advanced text preprocessing techniques
- Experiment with deep learning models
- Add cross-validation
- Explore additional feature engineering
- Deploy model as web service