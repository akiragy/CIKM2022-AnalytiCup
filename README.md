To run the code:
```bash
# step1  prepare dataset
cp -r data/CIKM22Competition/{{1..8},11,12} data_group1/CIKM22Competition/
mv data_group1/CIKM22Competition/11 data_group1/CIKM22Competition/9
mv data_group1/CIKM22Competition/12 data_group1/CIKM22Competition/10

cp -r data/CIKM22Competition/{9,10,13} data_group2/CIKM22Competition/
mv data_group2/CIKM22Competition/9 data_group2/CIKM22Competition/1
mv data_group2/CIKM22Competition/10 data_group2/CIKM22Competition/2
mv data_group2/CIKM22Competition/13 data_group2/CIKM22Competition/3

cp -r data/CIKM22Competition/{1..5} data_group3/CIKM22Competition/

# step 2  train and predict
sh run_exp.sh

# step3  output file will be './prediction.csv'
```


Brief introduction of the developed algorithm:
> We divide the 13 clients into 3 groups according to the size of dataset: client 6.7.8.11.12 -> group1, client 9.10.13 -> group2, client 1.2.3.4.5 -> group3.
> We use GCFL+ for group1, FedAvg with FedProx constraint for group2 and GCFL+ for group3.
> The base model for each client is GIN, key hyperparameters are the number of layers and embedding size of GIN, learning rate and gradient clipping value for optimizer. 
> We choose the round with the highest val_imp_ratio for each client to output the result, instead of using the result of the last round.