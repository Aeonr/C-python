import networkx as nx
import matplotlib.pyplot as plt

# Create a bipartite graph to represent competition and cooperation relationships
G = nx.Graph()

# Define nodes for male and female eels
male_eels = ['Seven-gilled eel (Male)'] * 3  # Assuming 3 male eels for illustration
female_eels = ['Seven-gilled eel (Female)'] * 3  # Assuming 3 female eels for illustration
organisms = ['Big fish', 'Small insect', 'Small fish', 'Crustaceans', 'Crabs', 'Plankton', 'Plants']

# Add nodes to the bipartite graph
G.add_nodes_from(male_eels, bipartite=0)
G.add_nodes_from(female_eels, bipartite=1)
G.add_nodes_from(organisms, bipartite=1)

# Define edges to represent interactions with labels indicating competition (C) （竞争）or cooperation (Co)（合作）
edges = [
    ('Seven-gilled eel (Male)', 'Big fish', {'label': 'C'}),
    ('Seven-gilled eel (Male)', 'Small insect', {'label': 'C'}),
    ('Seven-gilled eel (Male)', 'Small fish', {'label': 'Co'}),
    ('Seven-gilled eel (Female)', 'Big fish', {'label': 'Co'}),
    ('Seven-gilled eel (Female)', 'Small insect', {'label': 'Co'}),
    ('Seven-gilled eel (Female)', 'Small fish', {'label': 'C'}),
    ('Big fish', 'Crustaceans', {'label': 'C'}),
    ('Crustaceans', 'Crabs', {'label': 'Co'}),
    ('Small insect', 'Plankton', {'label': 'Co'}),
    ('Plankton', 'Plants', {'label': 'C'}),
    # Add other interactions...
]

# Add edges to the bipartite graph
G.add_edges_from(edges)

# Draw the bipartite graph with different edge colors for competition and cooperation
pos = nx.spring_layout(G, iterations=200, seed=42)

edge_colors = {'C': 'red', 'Co': 'green'}
edge_labels = {(u, v): d['label'] for u, v, d in G.edges(data=True)}

nx.draw(G, pos, with_labels=True, font_size=8, font_color='black', font_weight='bold',
        node_color=['skyblue' if 'Seven-gilled eel' in node else 'lightgreen' for node in G.nodes()])

nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='black')
nx.draw_networkx_edges(G, pos, edgelist=edges, edge_color=[edge_colors[d['label']] for u, v, d in G.edges(data=True)])

plt.title('Competition (Red) and Cooperation (Green) Relationships')
plt.show()
