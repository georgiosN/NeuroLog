# NeuroLog 
NeuroLog is a set of tools that enable the creation and training of a machine learning model capable of
predicting the logging severity of a log statement, with an example implementation having an 85% accuracy. Additionally, NeuroLog contains code to attempt to predict 
the logging message of a statement. For more details, please read the following [paper](TODO:LINK).
NeurLog was created by Georgios Nikolopoulos with assistance by Earl Barr and Miltos Alamanis
for his dissertation at UCL. NeuroLog heavily relies on and uses [ptgnn](https://github.com/microsoft/ptgnn).
###This is work in progress.
## Installation
NeuroLog requires Python 3. Linux or similar OS is reccomended, but not required.
Usage of python virtual environment advised. To install all dependencies simply run: 
```sh
$ pip install -r requirments.txt
```
Any script can then be run using a standard python execution command, such as:
```sh
$ python retrieveLogs.py PARAMS
```
NOTE: This installation downloads the required libraries for CPU only training. If you wish to use a GPU with CUDA,
please manually install the relevant libraries. Visit [ptgnn](https://github.com/microsoft/ptgnn) for details on the 
required training libraries.
### How to generate a severity prediction model
1. Gather a corpus of java.proto files using the [javac features library](https://github.com/acr31/features-javac).
The bigger the corpus, the better!
2. Use the [retrieveLogs](retrieveLogs.py) script to find all logging statements contained within the corpus.
3. Use the [nodeParsing](nodeParsing.py) script in combination with the corpus to generate a new, modified corpus that 
can be used for ML training.
4. Use the [convertCorpusForML](convertCorpusForML.py) script to generate the train, validation and test set.
Alternativly, [convertCorpusOnAzure](azure/convertCorpusOnAzure.py) can be used to generate the sets with the help of a
Azure ML CPU instance.
5. Train and test the model via ptgnn's [trainandtest](azure/ptgnn/ptgnn/implementations/graph2seq/trainandtest.py) script.
You can either use the script linked here, or download ptgnn from github and use it directly. Additionally, you may 
train the model using AzureML by using [runOnAzure](azure/ptgnn/runOnAzure.py).
### How to generate a message prediction model
To generate a model that attempts to predict the log message, the exact same steps need to be followed with two variations:
* Pass the relevant parameters to [convertCorpusForML](convertCorpusForML.py) and 
[trainandtest](azure/ptgnn/ptgnn/implementations/graph2seq/trainandtest.py)
* Use the local, modified version of ptgnn. This version is better optimized for message prediction and also calculates
bleu scores.

Please note that message prediction may not be successful out of the box. For more information read the linked paper.
# Explanation of Files and Folders
Please use -h with any script for more information

### graph_pb2.py
Google's autogenerated library using proto.exe and the graph.proto format. Used in most of the scripts
to parse or to create the proto files. 
### retrieveLogs.py
Automatically detects logs in java protocol buffer files that have been generated with the 
[javac features library](https://github.com/acr31/features-javac). Outputs a JSON file that contains the logs and
 can be further used to generate the new modified corpus via nodeParsing.py.
### nodeParsing.py
Uses the unmodified java protocol buffer corpus in combination with the JSON file generated by retrieveLogs to 
create a new, modified corpus. The logging statements in the graphs have been removed,
getting replaced by a special node. The corpus can now be fed into the following script for ML training preparation.
### convertCorpusForML.py
Converts the modified corpus into three jsonl files (train, validate, test). These files can then be fed into 
[ptgnn](https://github.com/microsoft/ptgnn) in order to train a ML model that can predict the severity or statement 
message of a logging statement. If you are trying to predict logging messages, you must use the custom ptgnn installation,
available inside the /azure/ptgnn folder. AzureML can be used to expedite training and is supported by NeuroLog.

### /azure
This folder contains all azure related files, allowing NeuroLog to be run on AzureML.
### /azure/ptgnn
This folder contains a custom version of ptgnn that can be used to predict logging messages in addition to severity. It
is not required to use this version of ptgnn for severity prediction.
### /azure/convertCorpusOnAzure
Exact same functionality as ./convertCorpusForML, but it enables execution on an Azure ML CPU cluster. Very usefull if 
dealing with very large corpuses/ graph files.
### /azure/ptgnn/runOnAzure.py
The central script to use in order to execute a ptgnn training session (severity OR statement )
on AzureML. In order to use this script, two additional JSON files must be created in the same folder, authentication.json,
which contains the cluster/datastore information and azureinfo.json which contains the required SAS authentication.
 Example of authentication.json:
```yaml
{
  "GPU": {
    "subID": "Subscript ID",
    "resGroup": "Resource name",
    "wsName": "Workspace name",
    "computeName": "Compute cluster name",
    "datastoreName" : " datastore Name that holds jsonl.gz files",
    "dataPath" : "azure:// path to the folder within the datastore "
  },
  "CPU" : {
  // similar format of data for different cluster
  }
}
```
Example of azureinfo.json:
```yaml
{
    "storage Name " : {
        "sas_token" : "SAS key authenticating datastore access",
        "cache_location" : "/tmp/logs" // leave this as is
    }
}
```
### A note on ptgnn
ptgnn contains many different scripts that perform several ML functionalities. For NeuroLog, only one folder is relevant
: azure/ptgnn/ptgnn/implementations/graph2seq/. The three files contained within are the files that are used
for the training of NeurLog's model. If you wish to manually train a model on your local machine, you need to use one of 
these scripts.
### /results
Contains both the individual results obtained by running retrieveLogs.py over a single project
as well as running it over all projects (all_projects.json). Also contains all logs and their level as a tsv file.
### /stats/analyzeData.py
Perfoms a statistical analysis of the generated TSV file containing all data.
### /stats/gatherStats.py
Performs a statistical analysis of a single JSON file, exact same functionality as analyzeData, left here to assist anyone wishing to
do severity prediction only.
### /statement_prediction
This folder contains three scripts that handle the tokenization training for statement prediction
as well as source-code log detection. Additionally, the tsv
file is generated here.
### /statement_prediction/gatherSourceLogs
This file has two purposes: First, it analyzes java source files for logging statements, writing them out for the tokenization training
and secondly: it merges all logs discovered (both in this file and in retrieveLogs) to make a tsv file which contains the project, 
severity and log message of a log statement.
### /statement_prediction/trainTokenizer
This script trains a senterpiece tokenizer, saving the generated model in place.
### /statement_prediction/createTokenExample
Generates examples of the tokenization procedure using the JSON in the results folder.
### unitTesting.py
Runs tests on the corpus to ensure that the generated graphs are formatted correctly.
### toDot.py
Converts a single graph file to a dot file, which can be parsed by graphviz or any other graph visualisation software. 
Not optimized and can fail to generate a proper dot file, depending on the inputted graph file. 
