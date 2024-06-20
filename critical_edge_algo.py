import pandas as pd
import coreness_centrality, betweeness_centrality, pagerank_centrality, katz_centrality, laplacian_centrality, closeness_centrality, eigenvector_centrality, degree_centrality, local_clustering_coefficient, percolation_centrality, semi_local_centrality, load_centrality, cluster_rank_centrality, max_neighborhood_centrality


def process_edge_data(processed_data):
    df1 =processed_data
    print(df1)
    print("Got data")
    c = coreness_centrality.Coreness()
    b = betweeness_centrality.Betweeness()
    p = pagerank_centrality.Pagerank()
    k = katz_centrality.Katz()
    l = laplacian_centrality.Laplacian()
    cl = closeness_centrality.Closeness()
    ev = eigenvector_centrality.Eigenvector()
    d = degree_centrality.Degree()
    lc = local_clustering_coefficient.LClustering()
    pc = percolation_centrality.Percolation()
    slc = semi_local_centrality.Semilocal()
    loc = load_centrality.Load()
    clr = cluster_rank_centrality.Clusterrank()
    mnc = max_neighborhood_centrality.MaxNeighborhood()
    pc.process_edge_data(df1)
    lc.process_edge_data(df1)
    cl.process_edge_data(df1)
    k.process_edge_data(df1)
    b.process_edge_data(df1)
    c.process_edge_data(df1)
    p.process_edge_data(df1)
    l.process_edge_data(df1)
    ev.process_edge_data(df1)
    d.process_edge_data(df1)
    slc.process_edge_data(df1)
    loc.process_edge_data(df1)
    clr.process_edge_data(df1)
    mnc.process_edge_data(df1)
    return c, b, p, k, l, cl, ev, d, lc, pc, slc, loc, clr, mnc
    
    

