project/
│
├── explore_urls.py         # Just data exploration + cleaning
├── preprocess_and_model.py # Full pipeline from labels to model training
├── url_only_data.csv       # Your dataset
└── processed_url_data.csv  # (Optional) cleaned dataset

next steps: 
Preprocess the training set - Done by DL

Train a model using the training data

🛠️ Write a function like predict_labels_from_urls(url_list) that:

Takes in new URLs ( the 20-title test set)

Outputs predicted labels (fox or nbc)

Ensure your model works on the test set subset

Submit or plug into the "Example Test Colab" to test on the actual hidden test set
