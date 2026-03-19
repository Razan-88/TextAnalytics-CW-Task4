# Task 4: Mining Insights from Customer Feedback

## Project Objective
This project analyses customer support tickets to identify and summmarise the most common issues raidsed by customers, with the aim of generating actionable insights for product and services improvenment. The project also evaluates how different text analytics methods influence the quality, consistency, and interpertability of the extraced insights. 

## Technical Objectives
- Clustering: Apply k-means and Hierachical (HAC) using TF-IDF vectors and embedding based representations.
- Stability: Evaluate cluster coherence and stability across different values of k.
- Pipeline Development: Build a system for preprocessing, text representation, and issue identification\ranking
- Analytics Axes: compare 2-3 approaches across two distinct design axes
- Evaluation: Assess findings based on robustness, consistency, and alignment with data patterns.

## Infrastructure and Setup
The following foundational work has been completed to establish the project environment:
- Directory Structure: A modular workspace was created to separate data (/data), experimental drafts(/research_notebooks), and the final pipeline(/analytics_pipeline).
- Environments Control: A .gitignore file was implemented to prevent the upload of local virtual environments and system metadata.
- Baseline Staging: The dataset and initial task4_customer_support.ipynb were integrated into the repository as a starting point.
- Governance: Team roles were defined (##TODO## to be completed )

## Repositry Structure
- /data: Raw customer_support_tickets.csv
- /research_notebooks: individual workspaces for EDA and clustering experiments.
- /analytics_pipeline: Madular Python scripts and baseline models
- /results_and_plots: Final outputs for the group reports

## Workflow (for Us)
1. Sync: Run git pull before starting any work
2. Isolate: Use named notebookes in /research_notebooks to prevent merge conflicts
3. Document: commit and push frequently with clear descriptions to document individual contributions. 
