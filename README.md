#   Analysis
- 0_generating.ipynb: This is the script that generates the analysis for the dataset.
- 1_planning.ipynb: This is the script that plans the analysis for the dataset.
- 1_preparing.ipynb: This is the script that prepares the analysis for the dataset. 

#   Datasets
- 0_data.csv: This is the full dataset.
- 1_data_paragraph.csv: This is the paragraph dataset.
- 2_data_paragraph_veracity.csv: This is the paragraph dataset with veracity mappings.
- 3_data_paragraph_veracity_prepared.csv: This is the paragraph dataset with veracity mappings and prepared with the preprocessing script.
- 4_data_paragraph_veracity_prepared_flagged.csv: This is the paragraph dataset with veracity mappings and prepared and flagged with the flagging script.

#   Pipeline
- 0_pipeline.ipynb: This converts the full dataset into the paragraph dataset.
- 1_mapping.ipynb: This converts the paragraph dataset into having veracity mappings.
- 2_preprocessing.ipynb: This prepares the paragraph dataset into being in the right order.
- 3_flagging.ipynb: This adds the paragraph flag to the paragraph dataset.

#   Intended Usage
- To generate the datasets, run the pipeline scripts in order. The assumption is that you have the all_data.csv file in the datasets directory as o_data.csv.
- The final version of the dataset is 4_data_paragraph_veracity_prepared_flagged.csv. This is the dataset that will be eventually merged with the claims dataset.

#   Future Work
- Once the claims dataset is ready to be merged, I will take the 4_data_paragraph_veracity_prepared_flagged.csv file and merge it with the claims dataset.
- This will likely take place directly in HF.
