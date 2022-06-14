# FREDclient
FREDclient is a Python implementation of a client for interacting with the REST API of [FRED](http://wit.istc.cnr.it/stlab-tools/fred). FRED is a machine reader for the Semantic Web, i.e. it is able to parse natural language text and transform it to linked data. FRED background theories are: Combinatory Categorial Grammar [C&C], Discourse Representation Theory, Frame Semantics Ontology Design Patterns. FRED leverages Natural Language Processing components for performing Named Entity Resolution, Coreference Resolution, and Word Sense Disambiguation. All FRED graphs include textual annotations and represent textual segmentation, expressed by means of EARMARK and NIF.
A detail description of FRED, its capabilities, and its theoretical grounding can be found on the [scientific article](https://content.iospress.com/articles/semantic-web/sw240) published on the [Semantic Web Journal](https://content.iospress.com/journals/semantic-web/Pre-press/Pre-press). If do not have the rights to access the article on the Semantic Web Journal you car read its [preprint version](http://www.semantic-web-journal.net/system/files/swj1379.pdf).

## Installation
FREDclient requires Python 3. Once the source code has been downladed it is possible to install the Python package by means of pip. For example:
```
pip install .
```
Alternatively, it is possible to install the pyRML package directly from GitHub in the following way:
```
pip install git+https://github.com/anuzzolese/fredclient
```

## Usage
Before going ahed with technical instruction be aware that you need a valid key for using FRED via its REST API. The key is required by FREDclient as it relies on such REST API. You can request a key by filling [this form](https://docs.google.com/forms/d/e/1FAIpQLScPO_xL_F6yw9Cf9p5rNyKpOZDsHXY1fs6C0zo8jv4NDK_EvQ/viewform).

The following is an example of how FREDClient can be used to get an RDF graph from a natural language sentence.
```py
from fredclient import FREDClient, FREDParameters, FREDDefaults


key = "YOUR_FRED_KEY";
fred_uri = "http://wit.istc.cnr.it/stlab-tools/fred"
sentence = "President Barack Obama and European Union leaders huddled in Washington amid growing fears over the future of the euro, which closed greater than 1.3 dollars."

fredclient = FREDClient(fred_uri, key=key)
g = fredclient.execute_request(sentence, FREDParameters(semantic_subgraph=False))

print(g.serialize(format="turtle"))
```
FREDClient returns RDFLib graphs as output. Hence refer to the [documentation](https://rdflib.readthedocs.io/en/stable/) of such library.
