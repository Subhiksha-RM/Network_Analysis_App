import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
import critical_edge_algo
import streamlit as st
import matplotlib.colors as mcolors
import matplotlib.cm as cm
import numpy as np



def viz(G, centrality_values, edge_labels=None):
    
    max_bc = max(centrality_values.values())
    min_bc = min(centrality_values.values())
   
    if max_bc == min_bc:  # If all values are the same, set all normalized values to 0.1
        centrality_rank = {node: 0.1  for node in G}
        st.write("Score/Rank:",centrality_rank)
    else:
        centrality_rank = {node: 0.1 + 0.9 * (bc - min_bc) / (max_bc - min_bc) for node, bc in centrality_values.items()}
        st.write("Score/Rank:",centrality_rank)

    

    # Create a color map based on the normalized betweenness centrality values
    color_map = []
    for node in G:
        if centrality_rank[node] == 0:
            color_map.append('none')  # Nodes with 0 value are not colored
        else:
            color_map = [plt.cm.Blues(centrality_rank[node]) for node in G]# Nodes with value more than 0 are colored

    # Draw the graph with the color map
    pos = nx.spring_layout(G)
    nx.draw(G, pos, node_color=color_map, with_labels=True)
    if edge_labels is not None:
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
    #plt.show()
    st.pyplot(plt)
