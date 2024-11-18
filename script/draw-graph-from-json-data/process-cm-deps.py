import argparse
import networkx as nx
import matplotlib.pyplot as plt
import json

# Function to parse the nested JSON structure
def parse_json_to_edges(json_data):
    edges = []
    for root_key, nodes in json_data.items():
        for node in nodes:
            for node_key, node_details in node.items():
                edges.append((node_details["parent"], node_key))
    return edges

# Function to generate and visualize the graph
def generate_graph_from_nested_json(json_data, output_image="graph.png"):
    # Parse the JSON to extract edges
    edges = parse_json_to_edges(json_data)

    # Initialize a directed graph
    G = nx.DiGraph()

    # Add edges to the graph
    G.add_edges_from(edges)

    # Draw the graph using a spring layout for better visualization
    plt.figure(figsize=(30, 25))
    #pos = nx.spectral_layout(G, seed=42)  # Seed for consistent layout
    pos = nx.shell_layout(G)  # Seed for consistent layout
    nx.draw(
        G,
        pos,
        with_labels=True,
        node_size=7000,
        node_color="skyblue",
        font_size=9,
        font_color="darkblue",
        edge_color="gray",
        arrowsize=20,
        linewidths=1.5
    )
    plt.title("Parent-Child Graph from Nested JSON", fontsize=16)

    # Save the visualization
    plt.savefig(output_image, format="png", dpi=300)
    print(f"Graph visualization saved as {output_image}")
    plt.show()

    return G

# Function to export the graph data
def export_graph_data(graph, filename="graph.graphml"):
    nx.write_graphml(graph, filename)
    print(f"Graph data saved as {filename}")

# Main function to handle argument parsing and processing
def main():
    parser = argparse.ArgumentParser(description="Generate a graph from nested JSON input.")
    parser.add_argument("json_file", type=str, help="Path to the JSON input file.")
    parser.add_argument("--output_image", type=str, default="graph.png", help="Output image file for the graph visualization.")
    parser.add_argument("--output_graphml", type=str, default="graph.graphml", help="Output GraphML file for the graph data.")

    args = parser.parse_args()

    # Load the JSON input file
    with open(args.json_file, "r") as f:
        json_data = json.load(f)

    # Generate the graph
    G = generate_graph_from_nested_json(json_data, output_image=args.output_image)

    # Export the graph data
    export_graph_data(G, filename=args.output_graphml)

if __name__ == "__main__":
    main()
