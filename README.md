0_generating.ipynb
1_pipeline.ipynb
2_flag.ipynb

planning.ipynb: figures out the column space between the two datasets.
pipeline.

Preparing, i believe this is changing the name of label to the name of veracity and then creating mapping counts or something.

Step 0: Loading in the data
Step 1: Filtering for paragraph data
Step 2: Filling the veracity for labels
Step 3: Preparing the data
Step 4: Flagging the data?

Datasets:
0_data.csv
1_data_paragraph.csv
2_data_paragraph_veracity.csv
3_data_paragraph_veracity_prepared.csv
4_data_paragraph_veracity_prepared_flagged.csv
 
Scripts:
0_pipeline.ipynb: This converts the full dataset into the paragraph dataset
1_mapping.ipynb: This converts the paragraph dataset into having veracity mappings.
2_misinfo_scipts: This will prepare the paragraph dataset into being in the right order.
3_flagging.ipynb: This will flag the paragraph dataset so it is ready to be added to the claims dataset.

Pipeline (modification scripts)
0_pipeline.ipynb: This requires you take some code from the pipeline.ipynb file
1_mapping.ipynb: This requires you to take some code from the pipeline.ipynb file
2_misinfo_scripts: Just take the preprocessing code
3_flagging.ipynb: Just take the flagging.ipynb file

Analysis (analysis scripts)
0_generating.ipynb
1_planning.ipynb
1_preparing.ipynb