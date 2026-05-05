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
Directory Structure: Created a modular workspace separating /data, /research_notebooks, and /analytics_pipeline.
Environment Control: Added a .gitignore file to prevent uploading local virtual environments and system metadata.
Baseline Staging: Integrated the dataset and the initial task4_customer_support.ipynb into the repository as a starting point.
- Governance: Team roles were defined as follow:
  - Sentence embeddings + K-means with PCA and without PCA = Rzan
  - TF-IDF + K-means with SVD and without SVD = Yannan
  - TF-IDF + HAC was performed = KainingYu
  - Sentence embeddings + HAC = KainingYu and Yannan
  - TF-IDF + LDA = Shankar
  - Sentence embeddings + BERTopic = Saranya
  

## Repositry Structure
- /data: Raw customer_support_tickets.csv
- /research_notebooks: individual workspaces for EDA and clustering experiments.
- /analytics_pipeline: Final Python scripts and baseline models
- /results_and_plots: Final outputs for the group reports

## Workflow 
1. Sync: Run git pull before starting any work
2. Isolate: Use named notebookes in /research_notebooks to prevent merge conflicts
3. Document: commit and push frequently with clear descriptions to document individual contributions. 
