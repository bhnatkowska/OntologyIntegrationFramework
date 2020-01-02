# OntologyIntegrationFramework

The folder contains executable files for Ontology Integration Framework as well as testing data.

Content:
- RestTest.jar - Ontology Integration Tool (OIT); communicates with NLTK library via REST services
- server.py - REST services (WordNet functions) used by Ontology Integration Tool
- TestData - six test cases + motivating example; each test case consists of the following elements:
 1) 2 ontologies to be merged (*.owl)
 2) a file with ontologies alingment (*.rdf)
 3) dictionary files with attributes' semantics defined (*.dic); can be renamed or deleted to be skipped
- TestResults - effects of OIT application to test cases (test1.txt, ..., test6.txt) as well as manual definition of attributes' semantics

Prerequisites:
- Windows 7 or later
- java8 jre installed and accessible (via path environment variable)
- Python 3.7 (32 bit)
- NLTK library (https://www.nltk.org/)
- flask server (http://flask.pocoo.org/)

Running procedure:
1. Download resources (RestTest.jar, Python/server.py, TestData)
2. Run server.py on a local machine
3. Run RestTest.jar 
4. Click Select ontology button and navigate to an ontology to be merged (from test case folders) - *.owl; do it twice 
5. Click Mapping button and select *.rdf file with ontology mappings
6. Click Semantic definition button; if dictionaries (*.dic) are present and no data from them are deleted, ontologies will be merged without furhter interaction, and the merged ontology will be presented in a new window; you can copy its content or save it to an OWL file; otherwise, you will be asked about attributes' semantics:
- If the attribute name exists in WordNet, possible definitions of the notion will be presented; you must select one and click Next
- If the attribute name doesn't exist in WordNet, you can write its synonym which potentially is present in Wordnet, select the proper definition from the list and define if its fits the oryginal meaning (isStrict); to move to the next element, close the window
When the semantics for all attributes is established, the tool will start integration of ontologies.
