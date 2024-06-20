import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
import critical_edge_algo
import streamlit as st
import matplotlib.colors as mcolors
import matplotlib.cm as cm
import numpy as np
from network_viz import viz 
import netcenlib as ncl

class Clusterrank:
    def __init__(self):
         
        self.edge_data = None
        self.df1  = None
        
    def process_edge_data(self, processed_data):
        self.edge_data = processed_data
        self.df1 = processed_data
        print("tis working")
        print(self.df1)
        print("This function in class")
        return self.df1
    

    def cluster_rank_centrality(self, feature_option):
      cluster_rank_centrality = {}
        
      feature = int(feature_option)
      print(type(feature))
        
      df = self.df1[self.df1['feature'] == feature]
      print(df)
     

      def create_dict(df):
          if 'edge_weight' in df.columns:
          #result = df.groupby('source_node').apply(lambda x: dict(zip(x.target_node, x.edge_weight))).to_dict()
           result = df.groupby('source_node')[['source_node', 'target_node', 'edge_weight']].apply(lambda x: dict(zip(x.target_node, x.edge_weight))).to_dict()
          else:
            result = df.groupby('source_node')['target_node'].apply(list).to_dict()
          return result
      result = create_dict(df)
      #print(result)

          
      if 'edge_weight' not in df.columns:
             G = nx.Graph(result)
             G.remove_edges_from(nx.selfloop_edges(G))
             pos = nx.spring_layout(G)
             #graph_dr5=nx.draw(G, with_labels=True) 
             if G.edges():  # Check if the graph has any edges
              cluster_rank_centrality = ncl.cluster_rank_centrality(G)
              edge_labels=None
      

      else: 

            has_edge_weights = all(isinstance(wgt, (int, float)) for tgts in result.values() for wgt in tgts.values())
            
            # Convert the dictionary to a list of edges with weights if it has edge weights,
            edges = [(src, tgt, {'weight': wgt}) for src, tgts in result.items() for tgt, wgt in tgts.items()]
            # Create a directed graph and add edges from the list
            G = nx.Graph()
            G.add_edges_from(edges)
            G.remove_edges_from(nx.selfloop_edges(G))
            # Draw the graph
            pos = nx.spring_layout(G)
            # Draw edge labels if the dictionary has edge weights
            edge_labels = nx.get_edge_attributes(G, 'weight')
            
            if G.edges():  # Check if the graph has any edges
             cluster_rank_centrality = ncl.cluster_rank_centrality(G)
                  
      
      viz(G, cluster_rank_centrality, edge_labels)
      return cluster_rank_centrality
    

       
    def cluster_rank_whole(self, feature_option):
        
      feature = feature_option  
      df = self.df1
      print(df)

      def create_dict(df):
          if 'edge_weight' in df.columns:
          #result = df.groupby('source_node').apply(lambda x: dict(zip(x.target_node, x.edge_weight))).to_dict()
           result = df.groupby('source_node')[['source_node', 'target_node', 'edge_weight']].apply(lambda x: dict(zip(x.target_node, x.edge_weight))).to_dict()
          else:
            result = df.groupby('source_node')['target_node'].apply(list).to_dict()
          return result
      result = create_dict(df)
      #print(result)
          
      if 'edge_weight' not in df.columns:
        G = nx.Graph(result)
        G.remove_edges_from(nx.selfloop_edges(G))
        if G.edges():  # Check if the graph has any edges
             cluster_rank_whole = ncl.cluster_rank_centrality(G)
             edge_labels=None
             
      else:
          has_edge_weights = all(isinstance(wgt, (int, float)) for tgts in result.values() for wgt in tgts.values())
            
          # Convert the dictionary to a list of edges with weights if it has edge weights,
          edges = [(src, tgt, {'weight': wgt}) for src, tgts in result.items() for tgt, wgt in tgts.items()]
          # Create a directed graph and add edges from the list
          G = nx.Graph()
          G.add_edges_from(edges)
          G.remove_edges_from(nx.selfloop_edges(G))
          # Draw the graph
          pos = nx.spring_layout(G)
          # Draw edge labels if the dictionary has edge weights
          edge_labels = nx.get_edge_attributes(G, 'weight')
          
          if G.edges():  # Check if the graph has any edges
             cluster_rank_whole = ncl.cluster_rank_centrality(G)
             
      
      viz(G, cluster_rank_whole, edge_labels)
      return cluster_rank_whole

   


    