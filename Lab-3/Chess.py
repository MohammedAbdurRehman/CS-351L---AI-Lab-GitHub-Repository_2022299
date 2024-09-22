# Step 1: Define the graph with knight moves on a 3x3 chessboard (9 vertices)
import networkx as nx
import matplotlib.pyplot as plt

# Step 1: Define the graph with 9 vertices (0 to 8) and edges representing knight moves
G = nx.Graph()

# These edges represent the valid moves a knight can make on a 3x3 board
# Each edge is a move from one square to another
knight_moves = [(0, 7), (0, 5), (1, 6), (1, 8), (2, 7), (2, 5), (3, 8), (3, 6), (4, 5), (4, 7), (4, 8)]
G.add_edges_from(knight_moves)

# Step 2: Visualize the uncolored graph (initial chessboard with no knights)
def visualize_uncolored_graph():
    plt.figure(figsize=(6, 6))
    pos = nx.spring_layout(G, seed=42)  # Use spring layout for spacing nodes
    node_colors = ['#ffffff'] * len(G.nodes)  # White color for uncolored nodes
    edge_colors = 'black'
    node_border_color = 'black'

    nx.draw(G, pos, with_labels=True, node_color=node_colors, font_weight='bold',
            node_size=2000, font_size=16, font_color='black', edge_color=edge_colors,
            linewidths=2, node_shape='o', edgecolors=node_border_color)

    plt.title("Chessboard (3x3) with Knight Moves (Uncolored)")
    plt.show()

# Step 3: Apply a greedy coloring algorithm to place knights
def greedy_coloring(G):
    # Use a greedy algorithm to color the graph
    colors = nx.coloring.greedy_color(G, strategy="largest_first")
    return colors

# Step 4: Visualize the colored chessboard with knights
def visualize_colored_graph(colors):
    plt.figure(figsize=(6, 6))
    pos = nx.spring_layout(G, seed=42)
    # Define a color map for the knight placement (colors correspond to knights)
    knight_colors = ['#ff9999', '#99ccff', '#ffff99', '#66ff66', '#ffcc66', '#ff6666', '#66cccc', '#cc99ff', '#ff9966']
    node_colors = [knight_colors[colors[node]] for node in G.nodes]  # Assign colors based on the result of greedy coloring
    edge_colors = 'black'
    node_border_color = 'black'

    nx.draw(G, pos, with_labels=True, node_color=node_colors, font_weight='bold',
            node_size=2000, font_size=16, font_color='black', edge_color=edge_colors,
            linewidths=2, node_shape='o', edgecolors=node_border_color)

    plt.title("Knight Placement using Graph Coloring")
    plt.show()

# Step 5: Display the uncolored graph (initial state)
visualize_uncolored_graph()

# Step 6: Color the graph using the greedy algorithm and visualize
colors = greedy_coloring(G)
visualize_colored_graph(colors)
