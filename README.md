#   Analysis
- 1_keyword_correlations.ipynb: The script that analyzes the keyword correlations for the paragraph dataset.
- 2_temporal_correlations.ipynb: The script that analyzes the temporal correlations for the paragraph dataset.
- a2_dates.ipynb: The script that determines which datasets have dates. This is required for the temporal analysis.
- a3_label_distributions.ipynb: The script that analyzes the label distributions for the paragraph dataset.

#   Datasets
- 0_data.csv: This is the full dataset.
- 1_data_paragraph.csv: This is the paragraph dataset.
- 2_data_paragraph_veracity.csv: This is the paragraph dataset with veracity mappings.
- 3_data_paragraph_veracity_prepared.csv: This is the paragraph dataset with veracity mappings and prepared with the preprocessing script.
- 4_data_paragraph_veracity_prepared_flagged_{type}.csv: This is the paragraph dataset with veracity mappings and prepared and flagged with the flagging script.

#   Pipeline
- 0_pipeline.ipynb: This converts the full dataset into the paragraph dataset.
- 1_mapping.ipynb: This converts the paragraph dataset into having veracity mappings.
- 2_preprocessing.ipynb: This prepares the paragraph dataset into being in the right order.
- 3_flagging.ipynb: This adds the paragraph flag to the paragraph dataset.
- 4_merge.ipynb: This allows viewing of the paragraph dataset, preparing it for the merge with the claims dataset.

#   Intended Usage
- To generate the datasets, run the pipeline scripts in order. The assumption is that you have the all_data.csv file in the datasets directory as o_data.csv.
- The final version of the dataset is 4_data_paragraph_veracity_prepared_flagged.csv. This is the dataset that will be eventually merged with the claims dataset.
- The repo attaches a submodule of the preprocessing script in misinfo-dataset-preprocessing, which is used in 2_preprocessing.ipynb.
- The repo attaches a submodule of the huggingface, which is used after the pipeline as a way to store the final dataset.
- The submodules are not included in the repo to avoid cluttering the repo with large files. However, the intended usage is for them to be cloned at the root of the repo.
