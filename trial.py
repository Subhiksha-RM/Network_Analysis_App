
    if selected_option == "critical node":
        
        st.write("Measure Node Centrality")
        cent_option = st.selectbox("Select Centrality Measure", cent_option)
        feature_option = st.selectbox("Select the required feature", feature_option)
        if cent_option == "Coreness":
          if feature_option=='0':
           st.write("Coreness Centrality")
           result = c.coreness_centrality(feature_option)
           st.write(result)
          elif feature_option=='1':
           st.write("Coreness Centrality")
           result = c.coreness_centrality(feature_option)
           st.write(result)
          elif feature_option=='2':
           st.write("Coreness Centrality")
           result = c.coreness_centrality(feature_option)
           st.write(result)
          elif feature_option=='3':
           st.write("Coreness Centrality")
           result = c.coreness_centrality(feature_option)
           st.write(result)
          elif feature_option=='4':
           st.write("Coreness Centrality")
           result = c.coreness_centrality(feature_option)
           st.write(result)
          elif feature_option=='5':
           st.write("Coreness Centrality")
           result = c.coreness_centrality(feature_option)
           st.write(result)
          elif feature_option=='Whole Network':
           st.write("Coreness Centrality")
           result = c.coreness_whole(feature_option)
           st.write(result)
             


             G = nx.DiGraph()
            G.add_edges_from(edges)
            # Draw the graph
            pos = nx.spring_layout(G)
            nx.draw(G, pos, with_labels=True)
            # Draw edge labels if the dictionary has edge weights
            edge_labels = nx.get_edge_attributes(G, 'weight')
            nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
            #plt.show() 

            # Code_to refer
           # bt.py:
           import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
import critical_edge_algo
import streamlit as st
import matplotlib.colors as mcolors
import matplotlib.cm as cm
import numpy as np
from network_viz import viz 

class Betweeness:
    def __init__(self):
         
        self.edge_data = None
        self.df1  = None
        #self.G = None

    def process_edge_data(self, processed_data):
        self.edge_data = processed_data
        self.df1 = processed_data
        print("tis working")
        print(self.df1)
        print("This function in class")
        return self.df1

    def betweeness_centrality(self, feature_option):

      betweeness_centrality = {}
        
      feature = int(feature_option)
      print(type(feature))
        
      df = self.df1[self.df1['feature'] == feature]
      print(df)
      
      #ts = self.df1[self.df1 ['feature']==feature]['timestamp']
      #print(ts)
      #st.write(ts)


      def create_dict(df):
          if 'edge_weight' in df.columns:
          #result = df.groupby('source_node').apply(lambda x: dict(zip(x.target_node, x.edge_weight))).to_dict()
           result = df.groupby('source_node')[['source_node', 'target_node', 'edge_weight']].apply(lambda x: dict(zip(x.target_node, x.edge_weight))).to_dict()
        else: 
           if 'value' in df.columns:
            # Check if 'value' column has None or 1
            if df['value'].isin([None, 1]).any():
                # Filter rows where 'value' is 1 and create a dictionary with 'source' as keys and 'target' as values
                result = df[df['value'] == 1].groupby('source')['target'].apply(list).to_dict()
                return result
      result = create_dict(df)
      #print(result)
          
      if 'edge_weight' not in df.columns:
             G = nx.DiGraph(result)
             #graph_dr5=nx.draw(G, with_labels=True) 
             if G.edges():  # Check if the graph has any edges
              betweeness_centrality = nx.betweenness_centrality(G)
              edge_labels=None
      
             #viz(G, betweeness_centrality) 
             #st.pyplot(plt)

      else: 

            has_edge_weights = all(isinstance(wgt, (int, float)) for tgts in result.values() for wgt in tgts.values())
            
            # Convert the dictionary to a list of edges with weights if it has edge weights,
            edges = [(src, tgt, {'weight': wgt}) for src, tgts in result.items() for tgt, wgt in tgts.items()]
            # Create a directed graph and add edges from the list
            G = nx.DiGraph()
            G.add_edges_from(edges)
            # Draw the graph
            pos = nx.spring_layout(G)
            #graph_dr4=nx.draw(G, pos, with_labels=True)
            # Draw edge labels if the dictionary has edge weights
            edge_labels = nx.get_edge_attributes(G, 'weight')
            #graph_dr3=nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
            if G.edges():  # Check if the graph has any edges
             betweeness_centrality = nx.betweenness_centrality(G)
       
            #plt.show() 
            #st.pyplot(plt)

           
      betweeness_centrality = nx.betweenness_centrality(G)
      viz(G, betweeness_centrality, edge_labels)

      return betweeness_centrality
    

       
    def betweeness_whole(self, feature_option):
        
      feature = feature_option  
      df = self.df1
      print(df)
      def create_dict(df):
          if 'edge_weight' in df.columns:
          #result = df.groupby('source_node').apply(lambda x: dict(zip(x.target_node, x.edge_weight))).to_dict()
           result = df.groupby('source_node')[['source_node', 'target_node', 'edge_weight']].apply(lambda x: dict(zip(x.target_node, x.edge_weight))).to_dict()
        else: 
           if 'value' in df.columns:
            # Check if 'value' column has None or 1
            if df['value'].isin([None, 1]).any():
                # Filter rows where 'value' is 1 and create a dictionary with 'source' as keys and 'target' as values
                result = df[df['value'] == 1].groupby('source')['target'].apply(list).to_dict()
                return result
      result = create_dict(df)
      print(result)
          
      if 'edge_weight' not in df.columns:
      
        G = nx.DiGraph(result)
        #graph_dr=nx.draw(G, with_labels=True)
        if G.edges():  # Check if the graph has any edges
             betweeness_whole = nx.betweenness_centrality(G)
             edge_labels=None
             #viz(G, betweeness_whole) 

      else:
          has_edge_weights = all(isinstance(wgt, (int, float)) for tgts in result.values() for wgt in tgts.values())
            
            # Convert the dictionary to a list of edges with weights if it has edge weights,
          edges = [(src, tgt, {'weight': wgt}) for src, tgts in result.items() for tgt, wgt in tgts.items()]
          # Create a directed graph and add edges from the list
          G = nx.DiGraph()
          G.add_edges_from(edges)
          # Draw the graph
          pos = nx.spring_layout(G)
          #graph_dr1=nx.draw(G, pos, with_labels=True)
          # Draw edge labels if the dictionary has edge weights
          edge_labels = nx.get_edge_attributes(G, 'weight')
          #graph_dr2= nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
          if G.edges():  # Check if the graph has any edges
             betweeness_whole = nx.betweenness_centrality(G)
       

      
      betweeness_whole = nx.betweenness_centrality(G)
      viz(G, betweeness_whole, edge_labels)
      

      return betweeness_whole

   


    