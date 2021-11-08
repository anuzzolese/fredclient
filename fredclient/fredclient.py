import urllib.request
from rdflib import Graph
from typing import List

class FREDDefaults:
  DEFAULT_SERIALIZATION = "text/turtle"
  AVAILABLE_SERIALIZATIONS = [DEFAULT_SERIALIZATION, "trix"]
  DEFAULT_FRED_PREFIX = "fred:"
  DEFAULT_FRED_NAMESPACE = "http://www.ontologydesignpatterns.org/ont/fred/"

class FREDParameters:
    def __init__(self, 
                 output : Graph = None, 
                 format : str = FREDDefaults.DEFAULT_SERIALIZATION,
                 prefix : str = FREDDefaults.DEFAULT_FRED_PREFIX,
                 namespace : str = FREDDefaults.DEFAULT_FRED_NAMESPACE,
                 ctxNamespaces : str = False,
                 wsd : bool = True,
                 semantic_subgraph : bool = True):
        self.__output : Graph = output
        self.__format : str = format
        self.__namespace = namespace
        self.__ctxNamespaces = ctxNamespaces,
        self.__wsd = wsd
        self.__semantic_subgraph = semantic_subgraph
    
    def getOutput(self) -> Graph:
        return self.__output
    
    def setOutput(self, output : Graph):
        self.__output = output
        
    def getFormat(self) -> str:
        return self.__format
    
    def setFormat(self, format : str):
        self.__format = format
        
    def getNamespace(self) -> str:
        return self.__namespace
    
    def setNamespace(self, namespace : str):
        self.__namespace = namespace
        
    def isCtxNamespaces(self) -> bool:
        return self.__ctxNamespacesctxNamespaces
    
    def setCtxNamespaces(self, ctxNamespaces : List[str]):
        self.__ctxNamespaces = ctxNamespaces
        
    def isWSD(self) -> bool:
        return self.__wsd
    
    def setWSD(self, wsd : bool):
        self.__wsd = wsd
        
    def isSemanticSubgraph(self):
        return self.__semantic_subgraph
        
    def setSemanticSubgraph(self, semantic_subgraph : bool):
        self.__semantic_subgraph = semantic_subgraph
        
    def to_dict(self):
        return {'format': self.__format,
            'namespace': self.__namespace,
            'wsd': str(self.__wsd).lower(),
            'semantic_subgraph': str(self.__semantic_subgraph).lower()}

class FREDClient:
    def __init__(self, fred_endpoint : str, requestMimeType : str = FREDDefaults.DEFAULT_SERIALIZATION):
        self.__fred_endpoint : str = fred_endpoint + "?%s"
        self.__requestMimeType : str = requestMimeType
    
    def execute_request(self, text : str, fredParameters : FREDParameters = FREDParameters()) -> Graph:

        params = fredParameters.to_dict()
        params.update({'text': text})
        
        params = urllib.parse.urlencode(params)
        
        #print(self.__requestMimeType)
        print(self.__fred_endpoint % params)
        graph=Graph()
        request = urllib.request.Request(self.__fred_endpoint % params, headers={"Accept": self.__requestMimeType})
        try:
            response = urllib.request.urlopen(request)
            output = response.read()
            
            graph.parse(data = output, format=self.__requestMimeType)
        except Exception as e:
            print(e)
        return graph
