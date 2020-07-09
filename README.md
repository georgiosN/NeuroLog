# NeuroLog 
This repository represents the work completed by Georgios Nikolopoulos
for his dissertation at UCL. This is work in progress.
## Explanation of Files
Please use -h with any script for mode information
### requirements.txt
Describes the pip packages that are needed to run the code. Using a venv is advisable.
### graph_pb2.py
Google's autogenerated library using proto.exe and the graph.proto format. Used in most of the scripts
to parse or to create the proto files.
### retrieveLogs.py
Automatically detects logs in java protocol buffer files that have been generated with the 
[javac features library](https://github.com/acr31/features-javac). Outputs a JSON file that contains the logs and
 can be further used to generate the new modified corpus via nodeParsing.py.
### NodeParsing.py
Uses the unmodified java protocol buffer corpus in combination with the JSON file generated by retrieveLogs to 
create a new, modified corpus. The logging statements in the graphs have been removed,
getting replaced by a special node. This corpus can be further used with the AI training.
### unitTesting.py
Runs tests on the corpus to ensure that the generated graphs are formatted correctly.
### toDot.py
Converts a single graph file to a dot file, which can be parsed by graphviz or any other graph visualisation software. 
Currently not optimized and can fail to generate a proper dot file, depending on the inputted graph file. 
### /results
Contains both the individual results obtained by running retrieveLogs.py over a single project
as well as running it over all projects (all_projects.json).
### /stats/gatherStats.py
Performs a statistical analysis of a single JSON file.
### /stats/gatherCorpusStats.py
Analyzes a set of JSON files to calculate statistics per file. Usefull for analysis of many different repositories.
### /stats/gatherGeneratedCorpusStats.py
Analyzes the generated corpus, displaying various statistics on it. (currently only log leak information)

