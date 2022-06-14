import urllib.request
from rdflib import Graph
from typing import List

class FREDDefaults:
  DEFAULT_SERIALIZATION = "text/turtle"
  AVAILABLE_SERIALIZATIONS = [DEFAULT_SERIALIZATION, "trix"]
  DEFAULT_FRED_PREFIX = "fred:"
  DEFAULT_FRED_NAMESPACE = "http://www.ontologydesignpatterns.org/ont/fred/"
  
  ROLES = {
    "agentive":[
      "http://www.ontologydesignpatterns.org/ont/vn/abox/role/Agent",
      "http://www.ontologydesignpatterns.org/ont/vn/abox/role/Actor",
      "http://www.ontologydesignpatterns.org/ont/vn/abox/role/Actor1",
      "http://www.ontologydesignpatterns.org/ont/vn/abox/role/Actor2",
      "http://www.ontologydesignpatterns.org/ont/boxer/boxer.owl#agent",
      "http://www.ontologydesignpatterns.org/ont/vn/abox/role/Cause",
      "http://www.ontologydesignpatterns.org/ont/boxer/title.owl#agent"
   ],
   "passive":[
      "http://www.ontologydesignpatterns.org/ont/vn/abox/role/Patient",
      "http://www.ontologydesignpatterns.org/ont/vn/abox/role/Patient1",
      "http://www.ontologydesignpatterns.org/ont/vn/abox/role/Patient2",
      "http://www.ontologydesignpatterns.org/ont/boxer/boxer.owl#patient",
      "http://www.ontologydesignpatterns.org/ont/boxer/boxer.owl#recipient",
      "http://www.ontologydesignpatterns.org/ont/vn/abox/role/Beneficiary",
      "http://www.ontologydesignpatterns.org/ont/boxer/boxing.owl#declaration",
      "http://www.ontologydesignpatterns.org/ont/boxer/boxer.owl#declaration",
      "http://www.ontologydesignpatterns.org/ont/vn/abox/role/Predicate",
      "http://www.ontologydesignpatterns.org/ont/vn/abox/role/Product",
      "http://www.ontologydesignpatterns.org/ont/vn/abox/role/Proposition",
      "http://www.ontologydesignpatterns.org/ont/vn/abox/role/Recipient",
      "http://www.ontologydesignpatterns.org/ont/vn/abox/role/Topic",
      "http://www.ontologydesignpatterns.org/ont/vn/abox/role/Value",
      "http://www.ontologydesignpatterns.org/ont/boxer/title.owl#patient",
      "http://www.ontologydesignpatterns.org/ont/boxer/title.owl#recipient"
   ],
   "conditional_agentive":[
      "http://www.ontologydesignpatterns.org/ont/vn/abox/role/Theme",
      "http://www.ontologydesignpatterns.org/ont/vn/abox/role/Theme1",
      "http://www.ontologydesignpatterns.org/ont/vn/abox/role/Theme2",
      "http://www.ontologydesignpatterns.org/ont/boxer/boxer.owl#theme",
      "http://www.ontologydesignpatterns.org/ont/boxer/title.owl#theme",
      "http://www.ontologydesignpatterns.org/ont/vn/abox/role/Experiencer"
   ],
   "oblique":[
      "http://www.ontologydesignpatterns.org/ont/fred/domain.owl#locatedIn",
      "http://www.ontologydesignpatterns.org/ont/vn/abox/role/Asset",
      "http://www.ontologydesignpatterns.org/ont/vn/abox/role/Attribute",
      "http://www.ontologydesignpatterns.org/ont/vn/abox/role/Destination",
      "http://www.ontologydesignpatterns.org/ont/vn/abox/role/Extent",
      "http://www.ontologydesignpatterns.org/ont/vn/abox/role/Instrument",
      "http://www.ontologydesignpatterns.org/ont/vn/abox/role/Location",
      "http://www.ontologydesignpatterns.org/ont/vn/abox/role/Material",
      "http://www.ontologydesignpatterns.org/ont/vn/abox/role/Oblique",
      "http://www.ontologydesignpatterns.org/ont/vn/abox/role/Oblique1",
      "http://www.ontologydesignpatterns.org/ont/vn/abox/role/Oblique2",
      "http://www.ontologydesignpatterns.org/ont/vn/abox/role/Source",
      "http://www.ontologydesignpatterns.org/ont/vn/abox/role/Stimulus",
      "http://www.ontologydesignpatterns.org/ont/vn/abox/role/Time"
   ]}

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
            'wsd': self.__wsd,
            'semantic-subgraph': self.__semantic_subgraph}

class FREDClient:
    def __init__(self, fred_endpoint : str, requestMimeType : str = FREDDefaults.DEFAULT_SERIALIZATION, key : str = None):
        self.__fred_endpoint : str = fred_endpoint + "?%s"
        self.__requestMimeType : str = requestMimeType
        self.__key : str = key
    
    def execute_request(self, text : str, fredParameters : FREDParameters = FREDParameters()) -> Graph:

        params = fredParameters.to_dict()
        params.update({'text': text})
        
        params = urllib.parse.urlencode(params)
        
        #print(self.__requestMimeType)
        #print(self.__fred_endpoint % params)
        graph=Graph()
        
        headers={"Accept": self.__requestMimeType}
        if self.__key:
            headers.update({"Authorization": f"Bearer {self.__key}"})
        
        request = urllib.request.Request(self.__fred_endpoint % params, headers=headers)
        try:
            response = urllib.request.urlopen(request)
            output = response.read()
            
            graph.parse(data = output, format=self.__requestMimeType)
        except Exception as e:
            print(e)
        return graph
