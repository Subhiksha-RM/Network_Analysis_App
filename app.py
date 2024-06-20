import streamlit as st
import pandas as pd
import critical_edge_algo, coreness_centrality, betweeness_centrality
from coreness_centrality import Coreness
from betweeness_centrality import Betweeness
from pagerank_centrality import Pagerank
from katz_centrality import Katz
from laplacian_centrality import Laplacian
from closeness_centrality import Closeness
from eigenvector_centrality import Eigenvector
from degree_centrality import Degree
from local_clustering_coefficient import LClustering
from percolation_centrality import Percolation
from semi_local_centrality import Semilocal
from load_centrality import Load
from cluster_rank_centrality import Clusterrank
from max_neighborhood_centrality import MaxNeighborhood

st.set_page_config(page_title="Network Analysis", layout="centered")
st.write("Network Analysis. .")

def main():
    # Check node_data var to get node.csv in session state or not
    if 'node_data' not in st.session_state:
        st.session_state['node_data'] = None

    # Check edge_data var to get edge.csv in session state or not
    if 'edge_data' not in st.session_state:
        st.session_state['edge_data'] = None

    node_data = st.sidebar.file_uploader("Upload the Node CSV file", type="csv")
    if node_data is not None:
        st.session_state['node_data'] = pd.read_csv(node_data)
        #node_df = pd.read_csv(node_data)
        #st.dataframe(node_data,height=500, width=500)
        st.write(st.session_state['node_data'])
        #critical_node_algo.process_data(st.session_state['node_data'])

    feature_option = ["Select a feature","Whole Network"]
    feature_option1 = ["Select feature","Whole Network"]

    edge_data = st.sidebar.file_uploader("Upload the Edge CSV file", type="csv")
    if edge_data is not None:
        st.session_state['edge_data'] = pd.read_csv(edge_data)
        st.write(st.session_state['edge_data'])
        processed_data=critical_edge_algo.process_edge_data(st.session_state['edge_data'])
        
        c, b, p, k, l, cl, ev, d, lc, pc, slc, loc, clr, mnc = critical_edge_algo.process_edge_data(st.session_state['edge_data'])
        processed_data = loc.process_edge_data(st.session_state['edge_data'])
        processed_data = slc.process_edge_data(st.session_state['edge_data'])
        processed_data = pc.process_edge_data(st.session_state['edge_data'])
        processed_data = lc.process_edge_data(st.session_state['edge_data'])
        processed_data = d.process_edge_data(st.session_state['edge_data'])
        processed_data = ev.process_edge_data(st.session_state['edge_data'])
        processed_data = c.process_edge_data(st.session_state['edge_data'])
        processed_data = p.process_edge_data(st.session_state['edge_data']) 
        processed_data = k.process_edge_data(st.session_state['edge_data'])
        processed_data = b.process_edge_data(st.session_state['edge_data'])
        processed_data = l.process_edge_data(st.session_state['edge_data'])
        processed_data = cl.process_edge_data(st.session_state['edge_data'])
        processed_data = clr.process_edge_data(st.session_state['edge_data'])
        processed_data = mnc.process_edge_data(st.session_state['edge_data'])
        edge_df = st.session_state['edge_data'].copy()
        edge_df1 = st.session_state['edge_data'].copy()
        feature_unique1 = edge_df['feature'].unique()
        feature_unique = edge_df['feature'].unique()
        #feature_unique=str(feature_unique)
        feature_option.extend(feature_unique)
        feature_option1.extend(feature_unique1)
        #st.write(feature_unique) # dynamic feature list from the edge.csv
        
        
    graph_option = ['Select the Graph','Static', 'Dynamic']
    graph_type = st.sidebar.selectbox('Select the graph type', graph_option)
   
   
    options = ["Select Analysis","critical node", "bottleneck"]
    selected_option = st.sidebar.selectbox('Select an option', options)
    

    cent_option = ["List of Node Centralities","Coreness", "PageRank", "Betweenness",          
                "Closeness Centrality",
                "Eigenvector Centrality",
                "Local Cluserting Coefficient",
                "Degree Centrality",
                "Percolation Centrality",
                "Katz Centrality",
                "Cluster Rank Centrality",
                "Maximum Neighborhood Component",
                "Semi Local Centrality",
                "Load Centrality",
                #"Aggregate Measure"
                "Laplacian Centrality",]  
    
    if graph_type == 'Static':
     st.write("Static Graph Analysis")
     if selected_option == "critical node":
        
        st.write("Measure Node Centrality")
        cent_option = st.selectbox("Select Centrality Measure", cent_option)
        feature_option = st.selectbox("Select the required feature", feature_option)
        st.write("Compare two Centrality Algorithms")
        
        # Define your algorithms
        algorithms_left = ["Coreness", "PageRank", "Betweenness","Closeness Centrality","Eigenvector Centrality",
                           "Local Cluserting Coefficient", "Percolation Centrality",]
        
                
        algorithms_right = ["Katz Centrality", "Cluster Rank Centrality","Maximum Neighborhood Component","Semi Local Centrality",
                            "Load Centrality","Laplacian Centrality","Degree Centrality",]
        

        # Create checkboxes for algorithms in the sidebar
        st.write('Select Algorithms')
        feature_option1 = st.selectbox("Select feature", feature_option1)
        col1, col2 = st.columns(2)
        selected_algorithms_left = {algo: col1.checkbox(algo, key=f'left_{algo}') for algo in algorithms_left}
        selected_algorithms_right = {algo: col2.checkbox(algo, key=f'right_{algo}') for algo in algorithms_right}

       
                  
        if cent_option == "Coreness":  
           if feature_option in feature_unique:
            st.write("Coreness Centrality")
            result = c.coreness_centrality(feature_option)
            #st.write(result)
           elif feature_option in feature_option=="Whole Network":
            st.write("Coreness Centrality")
            result = c.coreness_whole(feature_option)
            #st.write(result)

        if cent_option == "Betweenness":  
           #b=betweeness_centrality.Betweeness()
           if feature_option in feature_unique:
            st.write("Betweeness Centrality")
            result = b.betweeness_centrality(feature_option)
            #st.write(result)
           elif feature_option in feature_option=="Whole Network":
            st.write("Betweeness Centrality")
            result = b.betweeness_whole(feature_option)
            #st.write(result)

        if cent_option == "PageRank":  
           if feature_option in feature_unique:
            st.write("PageRank Centrality")
            result = p.pagerank_centrality(feature_option)
            #st.write(result)
           elif feature_option in feature_option=="Whole Network":
            st.write("PageRank Centrality")
            result = p.pagerank_whole(feature_option)
            #st.write(result)

        if cent_option == "Katz Centrality":
           if feature_option in feature_unique:
            st.write("Katz Centrality")
            result = k.katz_centrality(feature_option)
            #st.write(result)
           elif feature_option in feature_option=="Whole Network":
            st.write("Katz Centrality")
            result = k.katz_whole(feature_option)
            #st.write(result)

        if cent_option == "Laplacian Centrality":
           if feature_option in feature_unique:
            st.write("Laplacian Centrality")
            result = l.laplacian_centrality(feature_option)
            #st.write(result)
           elif feature_option in feature_option=="Whole Network":
            st.write("Laplacian Centrality")
            result = l.laplacian_whole(feature_option)
            #st.write(result)

        if cent_option == "Closeness Centrality":
           if feature_option in feature_unique:
            st.write("Closeness Centrality")
            result = cl.closeness_centrality(feature_option)
            #st.write(result)
           elif feature_option in feature_option=="Whole Network":
            st.write("Closeness Centrality")
            result = cl.closeness_whole(feature_option)
            #st.write(result)

        if cent_option == "Eigenvector Centrality":
           if feature_option in feature_unique:
            st.write("Eigenvector Centrality")
            result = ev.eigenvector_centrality(feature_option)
            #st.write(result)
           elif feature_option in feature_option=="Whole Network":
            st.write("Eigenvector Centrality")
            result = ev.eigenvector_whole(feature_option)
            #st.write(result)
        
        if cent_option == "Degree Centrality":
           if feature_option in feature_unique:
            st.write("Degree Centrality")
            result = d.degree_centrality(feature_option)
            #st.write(result)
           elif feature_option in feature_option=="Whole Network":
            st.write("Degree Centrality")
            result = d.degree_whole(feature_option)
            #st.write(result)

        if cent_option == "Local Cluserting Coefficient":
           if feature_option in feature_unique:
            st.write("Local Cluserting Coefficient")
            result = lc.local_clustering_centrality(feature_option)
            #st.write(result)
           elif feature_option in feature_option=="Whole Network":
            st.write("Local Cluserting Coefficient")
            result = lc.local_clustering_whole(feature_option)
            #st.write(result)
        
        if cent_option == "Percolation Centrality":
           if feature_option in feature_unique:
            st.write("Percolation Centrality")
            result = pc.percolation_centrality(feature_option)
            #st.write(result)
           elif feature_option in feature_option=="Whole Network":
            st.write("Percolation Centrality")
            result = pc.percolation_whole(feature_option)
            #st.write(result)

        if cent_option == "Semi Local Centrality":
           if feature_option in feature_unique:
            st.write("Semi Local Centrality")
            result = slc.semi_local_centrality(feature_option)
            #st.write(result)
           elif feature_option in feature_option=="Whole Network":
            st.write("Semi Local Centrality")
            result = slc.semi_local_whole(feature_option)
            #st.write(result)

        if cent_option == "Load Centrality":
           if feature_option in feature_unique:
            st.write("Load Centrality")
            result = loc.load_centrality(feature_option)
            #st.write(result)
           elif feature_option in feature_option=="Whole Network":
            st.write("Load Centrality")
            result = loc.load_whole(feature_option)
            #st.write(result)
        
        if cent_option == "Cluster Rank Centrality":
           if feature_option in feature_unique:
            st.write("Cluster Rank Centrality")
            result = clr.cluster_rank_centrality(feature_option)
            #st.write(result)
           elif feature_option in feature_option=="Whole Network":
            st.write("Cluster Rank Centrality")
            result = clr.cluster_rank_whole(feature_option)
            #st.write(result)  
            
        if cent_option == "Maximum Neighborhood Component":
           if feature_option in feature_unique:
            st.write("Maximum Neighborhood Component")
            result = mnc.max_neighborhood_centrality(feature_option)
            #st.write(result)
           elif feature_option in feature_option=="Whole Network":
            st.write("Maximum Neighborhood Component")
            result = mnc.max_neighborhood_whole(feature_option)
            #st.write(result)   
        

        if selected_algorithms_left["Coreness"]:
          
           if feature_option1 in feature_unique1:
            col1.write("Coreness Centrality")
            result = c.coreness_centrality(feature_option1)
            #col1.write(result)
           elif feature_option1 in feature_option1=="Whole Network":
            col1.write("Coreness Centrality")
            result = c.coreness_whole(feature_option1)
            #col1.write(result)

        if selected_algorithms_right["Katz Centrality"]:
          
          if feature_option1 in feature_unique1:
            col2.write("Katz Centrality")
            result = k.katz_centrality(feature_option1)
            #col2.write(result)
          elif feature_option1 in feature_option1=="Whole Network":
            col2.write("Katz Centrality")
            result = k.katz_whole(feature_option1)
            #col2.write(result)

        if selected_algorithms_left["PageRank"]:
          
           if feature_option1 in feature_unique1:
            col1.write("PageRank Centrality")
            result = p.pagerank_centrality_centrality(feature_option1)
            #col1.write(result)
           elif feature_option1 in feature_option1=="Whole Network":
            col1.write("PageRank Centrality")
            result = p.pagerank_whole(feature_option1)
            #col1.write(result)

        if selected_algorithms_right["Load Centrality"]:
          
          if feature_option1 in feature_unique1:
            col2.write("Load Centrality")
            result = loc.load_centrality_centrality(feature_option1)
            #col2.write(result)
          elif feature_option1 in feature_option1=="Whole Network":
            col2.write("Load Centrality")
            result = loc.load_whole(feature_option1)
            #col2.write(result)

        if selected_algorithms_left["Betweenness"]:
          
           if feature_option1 in feature_unique1:
            col1.write("Betweeness Centrality")
            result = b.betweeness_centrality(feature_option1)
            #col1.write(result)
           elif feature_option1 in feature_option1=="Whole Network":
            col1.write("Coreness Centrality")
            result = b.betweeness_whole(feature_option1)
            #col1.write(result)

        if selected_algorithms_right["Laplacian Centrality"]:
          
          if feature_option1 in feature_unique1:
            col2.write("Laplacian Centrality")
            result = l.laplacian_centrality(feature_option1)
            #col2.write(result)
          elif feature_option1 in feature_option1=="Whole Network":
            col2.write("Laplacian Centrality")
            result = l.laplacian_whole(feature_option1)
            #col2.write(result)

        if selected_algorithms_left["Closeness Centrality"]:
          
           if feature_option1 in feature_unique1:
            col1.write("Closeness Centrality")
            result = cl.closeness_centrality(feature_option1)
            #col1.write(result)
           elif feature_option1 in feature_option1=="Whole Network":
            col1.write("Closeness Centrality")
            result = cl.closeness_whole(feature_option1)
            #col1.write(result)

        if selected_algorithms_right["Degree Centrality"]:
          
          if feature_option1 in feature_unique1:
            col2.write("Degree Centrality")
            result = d.degree_centrality(feature_option1)
            #col2.write(result)
          elif feature_option1 in feature_option1=="Whole Network":
            col2.write("Degree Centrality")
            result = d.degree_whole(feature_option1)
            #col2.write(result)

        if selected_algorithms_left["Local Cluserting Coefficient"]:
          
           if feature_option1 in feature_unique1:
            col1.write("Local Cluserting Coefficient")
            result = lc.local_clustering_centrality(feature_option1)
            #col1.write(result)
           elif feature_option1 in feature_option1=="Whole Network":
            col1.write("Local Cluserting Coefficient")
            result = lc.local_clustering_whole(feature_option1)
            #col1.write(result)

        if selected_algorithms_left["Percolation Centrality"]:
          
          if feature_option1 in feature_unique1:
            col2.write("Percolation Centrality")
            result = pc.percolation_centrality(feature_option1)
            #col2.write(result)
          elif feature_option1 in feature_option1=="Whole Network":
            col2.write("Percolation Centrality")
            result = pc.percolation_whole(feature_option1)
            #col2.write(result)
        
        if selected_algorithms_right["Cluster Rank Centrality"]:
          if feature_option1 in feature_unique1:
            st.write("Cluster Rank Centrality")
            result = clr.cluster_rank_centrality(feature_option1)
            #st.write(result)
          elif feature_option1 in feature_option1=="Whole Network":
            st.write("Cluster Rank Centrality")
            result = clr.cluster_rank_whole(feature_option1)
            #st.write(result)  

        if selected_algorithms_right["Maximum Neighborhood Component"]:      
          if feature_option1 in feature_unique1:
            st.write("Maximum Neighborhood Component")
            result = mnc.max_neighborhood_centrality(feature_option1)
            #st.write(result)
          elif feature_option1 in feature_option1=="Whole Network":
            st.write("Maximum Neighborhood Component")
            result = mnc.max_neighborhood_whole(feature_option1)
            #st.write(result) 

        if selected_algorithms_left["Eigenvector Centrality"]: 
           if feature_option1 in feature_unique1:
            st.write("Eigenvector Centrality")
            result = ev.eigenvector_centrality(feature_option1)
            #st.write(result)
           elif feature_option1 in feature_option1=="Whole Network":
            st.write("Eigenvector Centrality")
            result = ev.eigenvector_whole(feature_option1)
            #st.write(result


    if graph_type=="Dynamic":
       st.write("Work in Progress")
        

if __name__ == "__main__":
        main()

    
     

