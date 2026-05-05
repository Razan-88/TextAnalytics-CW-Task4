# Task 4: Mining Insights from Customer Feedback



## Project Objective

This project analyses customer support tickets to identify and summarise the most common issues raised by customers, with the aim of generating actionable insights for product and service improvement. The project also evaluates how different text analytics methods influence the quality, consistency, and interpretability of the extracted insights.



## Technical Objectives

Clustering: Apply k-means and hierarchical clustering (HAC) using TF-IDF vectors and embedding-based representations.
Stability: Evaluate cluster coherence and stability across different values of k.
Pipeline Development: Build a system for preprocessing, text representation, and issue identification/ranking.
Analytics Axes: Compare 2–3 approaches across two distinct design axes.
Evaluation: Assess findings based on robustness, consistency, and alignment with data patterns.



## Infrastructure and Setup

The following foundational work has been completed:
Directory Structure: Created a modular workspace separating /data, /research\_notebooks, and /analytics\_pipeline.
Environment Control: Added a .gitignore file to prevent uploading local virtual environments and system metadata.
Baseline Staging: Integrated the dataset and the initial task4\_customer\_support.ipynb into the repository as a starting point.

* Governance: Team roles were defined as follow:

  * Sentence embeddings + K-means with PCA and without PCA = Rzan
  * TF-IDF + K-means with SVD and without SVD = Yanna
  * TF-IDF + HAC was performed = KainingYu
  * Sentence embeddings + HAC = KainingYu and Yannan
  * TF-IDF + LDA = Shankar
  * Count vectorizer + LDA = Shankar
  * Gensim + LDA = Shankar
  * Sentence embeddings + BERTopic = Saranya





## Repository Structure



textanalytics-cw-task4/

│

├── README.md

├── requirements.txt

│

└── analytics\_pipeline/

&#x20;   │

&#x20;   ├── src/                                 # Main run files for the coursework

&#x20;   │   ├── eda.ipynb                        # Exploratory Data Analysis

&#x20;   │   ├── preprocessingAndModelling.ipynb  # Preprocessing \& Modelling

&#x20;   │   ├── modelTesting.ipynb               # Model Testing

&#x20;   │   │

&#x20;   │   └── services/

&#x20;   │       ├── model.py

&#x20;   │       └── utils.py

&#x20;   │

&#x20;   ├── data/

&#x20;   │   ├── cleaned\_data.csv

&#x20;   │   └── customer\_support\_tickets.csv

&#x20;   │

&#x20;   ├── models/

&#x20;   │   ├── artifacts/

&#x20;   │   │   ├── kmeans/               # KMeans images and plots

&#x20;   │   │   ├── hac/                  # HAC images and plots

&#x20;   │   │   ├── lda/                  # LDA images and plots

&#x20;   │   │   └── bert/                 # BERT images and plots

&#x20;   │   │

&#x20;   │   ├── kmeans/                   # KMeans model files and cluster labels

&#x20;   │   ├── hac/                      # HAC model files and cluster labels

&#x20;   │   ├── lda/                      # LDA model files and cluster labels

&#x20;   │   └── bert/                     # BERT model files and cluster labels

&#x20;   │

&#x20;   └── research\_notebooks/           # Individual work of each team member

&#x20;       ├── kaining\_yu/

&#x20;       ├── yannan\_li/

&#x20;       ├── shankara\_ng/

&#x20;       ├── rzan\_alkabier/

&#x20;       └── saranya\_srinivas/



## Instructions

* All the main files that needs to be run or checked is present inside the src folder in analytics pipeline folder
* eda, preprocessingAndModelling and modelTesting are the main files for this coursework
* Go inside the analytics\_pipeline
* All the codes are present in /src
* open /src you will see eda, preprocessingandmodelling and model testing
* to set up the environment run the below mentioned command
* pip install -r requriements.txt
* select the kernel to point to the environment
* run the files one after the other
* read the instructions present in the file before running





## Contact

For any instructions to run or with the setup feel free to contact any of these members



Shankara N G => cw25716@bristol.ac.uk

Saranya Srinivas => bu25681@bristol.ac.uk

Rzan Alkabier => lh25128@bristol.ac.uk

Kaining Yu => wv25265@bristol.ac.uk

Yannan Li => ex25245@bristol.ac.uk





