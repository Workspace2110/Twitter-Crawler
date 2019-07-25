#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
The utility tool for elasticsearch.
---
"""

# imports packages
import json

from elasticsearch import Elasticsearch
# ==================================

def send_to_elasticsearch(host:str, port:int, index:str, doc_type:str, id:str, jsonData:json):
    """
    Sending data to elasticsearch
    ---

    Args:
    - host (:obj:`str`) -- Elasticsearch server host.
    - port (:obj:`int`) -- Elasticsearch server port.
    - doc_type (:obj:`str`) -- Data type.
    - id (:obj:`str`) -- Data index.
    - jsonData (:obj:`json`) -- The Data that you want to upload.

    Returns:
    - (:obj:`bool`) -- Is it right working?
    """
    # datetime.now().strftime("%Y-%m-%d")
    try:
        es = Elasticsearch(host=host, port=port)

        result = es.index(
            index = index,
            doc_type = doc_type,
            id = id,
            body = jsonData
        )

        es.indices.refresh(index=index)
        
        print(result["result"])
        return True

    except Exception:
        print("Saving fail")
        return False

def search_from_elasticsearch(host:str, post:int, index:str, queryJson:json):
    """
    Searching data from elasticsearch
    ---

    Args:
    - host (:obj:`str`) -- Elasticsearch server host.
    - post (:obj:`int`) -- Elasticsearch server port.
    - index (:obj:`str`) -- Data index.
    - jsonData (:obj:`json`) -- Query data.

    Returns:
    - (:obj:`dict`) -- Search result
    """
    es = Elasticsearch(host=host, post=post)

    result = es.search(
        index=index,
        body=queryJson
    )
    
    return result

def get_from_elasticsearch(host:str, post:int, index:str, doc_type:str, id:str):
    """
    Getting data from elasticsearch
    ---

    Args:
    - host (:obj:`str`) -- Elasticsearch server host.
    - post (:obj:`int`) -- Elasticsearch server port.
    - index (:obj:`str`) -- Data index.
    - doc_type (:obj:`str`) -- Data type.
    - id (:obj:`str`) -- Data id.

    Returns:
    - (:obj:`dict`) -- Search result
    """
    es = Elasticsearch(host=host, post=post)

    result = es.get(index=index, doc_type=doc_type, id=id)
    print(result["_source"])

    return result
    