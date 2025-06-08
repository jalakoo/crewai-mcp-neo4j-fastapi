# Graph Data Science Integration

This repository includes the Neo4j Graph Data Science (GDS) library as a Git submodule, enabling advanced graph analytics and machine learning capabilities.

## What is Neo4j Graph Data Science?

Neo4j Graph Data Science is a comprehensive library of graph algorithms and machine learning procedures that can be executed directly within Neo4j. It provides:

- **Graph Algorithms**: Centrality, community detection, path finding, and similarity algorithms
- **Machine Learning**: Node classification, link prediction, and graph embeddings
- **Graph Projections**: In-memory graph representations for efficient algorithm execution
- **Scalability**: Optimized for large-scale graph analytics

## Available Algorithms

### Centrality Algorithms
- **PageRank**: Measures the importance of nodes based on link structure
- **Betweenness Centrality**: Identifies nodes that act as bridges in the graph
- **Closeness Centrality**: Measures how close a node is to all other nodes
- **Degree Centrality**: Based on the number of connections a node has

### Community Detection
- **Louvain**: Detects communities by optimizing modularity
- **Label Propagation**: Fast community detection algorithm
- **Weakly Connected Components**: Finds connected subgraphs
- **Strongly Connected Components**: For directed graphs

### Path Finding
- **Shortest Path**: Finds the shortest path between two nodes
- **All Pairs Shortest Path**: Computes shortest paths between all node pairs
- **A* Search**: Heuristic-based pathfinding algorithm
- **Dijkstra**: Single-source shortest path algorithm

### Similarity
- **Node Similarity**: Computes similarity between nodes based on their neighborhoods
- **K-Nearest Neighbors**: Finds the k most similar nodes
- **Cosine Similarity**: Vector-based similarity computation

### Machine Learning
- **Node Classification**: Predicts node labels based on graph structure
- **Link Prediction**: Predicts missing or future relationships
- **Graph Embeddings**: Creates vector representations of nodes (Node2Vec, FastRP)

## Using GDS with CrewAI

The CrewAI agents can leverage GDS algorithms through natural language queries. Here are some examples:

### Example Queries

```bash
# Community Detection
curl -X POST "http://localhost:12000/crewai" \
     -H "Content-Type: application/json" \
     -d '{"query": "Find communities in the graph using Louvain algorithm and show the top 5 communities by size"}'

# Centrality Analysis
curl -X POST "http://localhost:12000/crewai" \
     -H "Content-Type: application/json" \
     -d '{"query": "Calculate PageRank for all nodes and identify the top 10 most influential nodes"}'

# Path Finding
curl -X POST "http://localhost:12000/crewai" \
     -H "Content-Type: application/json" \
     -d '{"query": "Find the shortest path between node A and node B"}'

# Similarity Analysis
curl -X POST "http://localhost:12000/crewai" \
     -H "Content-Type: application/json" \
     -d '{"query": "Find the 5 most similar nodes to a specific node using node similarity algorithm"}'

# Machine Learning
curl -X POST "http://localhost:12000/crewai" \
     -H "Content-Type: application/json" \
     -d '{"query": "Create node embeddings using FastRP algorithm and show the embedding dimensions"}'
```

## GDS Cypher Procedures

The Graph Data Science library provides Cypher procedures that can be called directly. Here are some common patterns:

### Graph Projection
```cypher
// Create an in-memory graph projection
CALL gds.graph.project(
    'myGraph',
    'Node',
    'RELATIONSHIP'
)
```

### Running Algorithms
```cypher
// PageRank
CALL gds.pageRank.stream('myGraph')
YIELD nodeId, score
RETURN gds.util.asNode(nodeId).name AS name, score
ORDER BY score DESC LIMIT 10

// Louvain Community Detection
CALL gds.louvain.stream('myGraph')
YIELD nodeId, communityId
RETURN communityId, count(*) AS size
ORDER BY size DESC

// Node Similarity
CALL gds.nodeSimilarity.stream('myGraph')
YIELD node1, node2, similarity
RETURN gds.util.asNode(node1).name AS node1Name,
       gds.util.asNode(node2).name AS node2Name,
       similarity
ORDER BY similarity DESC LIMIT 10
```

## Building the GDS Plugin

If you want to build the Graph Data Science plugin from source:

### Prerequisites
- Java 17 or 21
- Gradle (included via wrapper)

### Build Steps
```bash
# Navigate to the GDS submodule
cd graph-data-science

# Build the open-source version
./gradlew :open-packaging:shadowCopy

# The built JAR will be in build/distributions/
ls build/distributions/open-gds-*.jar

# Copy to Neo4j plugins directory (if running local Neo4j)
cp build/distributions/open-gds-*.jar $NEO4J_HOME/plugins/
```

### Using with Docker
```bash
# Build the plugin
cd graph-data-science
./gradlew :open-packaging:shadowCopy

# Copy to a volume that Neo4j can access
mkdir -p ../neo4j-plugins
cp build/distributions/open-gds-*.jar ../neo4j-plugins/

# Update docker-compose.yml to mount the plugins directory
# volumes:
#   - ./neo4j-plugins:/plugins
```

## Performance Considerations

### Memory Requirements
- GDS algorithms can be memory-intensive for large graphs
- Consider using graph projections to optimize memory usage
- Monitor Neo4j heap size and adjust as needed

### Algorithm Selection
- Choose algorithms based on your graph size and analysis needs
- Some algorithms (like All Pairs Shortest Path) have O(n²) complexity
- Use streaming modes for large result sets

### Best Practices
1. **Project graphs efficiently**: Only include necessary nodes and relationships
2. **Use appropriate algorithms**: Match algorithm complexity to your use case
3. **Monitor performance**: Use Neo4j's query profiling tools
4. **Batch operations**: For large-scale analysis, consider batching queries

## Integration with MCP

The Neo4j MCP tools automatically detect and can utilize GDS procedures. The CrewAI agents will:

1. **Analyze the query** to understand what graph analysis is needed
2. **Select appropriate GDS algorithms** based on the question
3. **Execute the procedures** through the MCP Neo4j tools
4. **Interpret results** and provide meaningful insights

## Troubleshooting

### Common Issues

1. **GDS Plugin Not Loaded**
   ```
   Error: Procedure `gds.pageRank.stream` is not available
   ```
   - Ensure the GDS plugin is in the Neo4j plugins directory
   - Restart Neo4j after adding the plugin
   - Check Neo4j logs for plugin loading errors

2. **Memory Issues**
   ```
   Error: Java heap space
   ```
   - Increase Neo4j heap size in neo4j.conf
   - Use graph projections to reduce memory usage
   - Consider algorithm-specific memory settings

3. **License Issues (Enterprise Features)**
   ```
   Error: This feature requires Neo4j Enterprise Edition
   ```
   - Some GDS features require Enterprise license
   - Use Neo4j Enterprise Docker image
   - Set NEO4J_ACCEPT_LICENSE_AGREEMENT=yes

### Debugging
```bash
# Check available GDS procedures
CALL gds.list()

# Check graph projections
CALL gds.graph.list()

# Monitor algorithm execution
CALL gds.beta.listProgress()
```

## Resources

- [Neo4j Graph Data Science Documentation](https://neo4j.com/docs/graph-data-science/)
- [GDS Algorithm Library](https://neo4j.com/docs/graph-data-science/current/algorithms/)
- [GDS Python Client](https://github.com/neo4j/graph-data-science-client)
- [GDS Examples](https://github.com/neo4j/graph-data-science/tree/master/examples)