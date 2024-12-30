from gremlin_python.structure.graph import Graph
from gremlin_python.driver.driver_remote_connection import DriverRemoteConnection

# Replace with your Cosmos DB Gremlin endpoint and primary key
COSMOS_ENDPOINT = "wss://<your-cosmos-db-account>.gremlin.cosmos.azure.com:443/"
PRIMARY_KEY = "<your-primary-key>"

# Create a connection
graph = Graph()
connection = DriverRemoteConnection(
    COSMOS_ENDPOINT,
    'g',
    username="/dbs/<your-database>/colls/<your-graph>",
    password=PRIMARY_KEY
)
g = graph.traversal().withRemote(connection)

# Example: Add a vertex
g.addV('person').property('id', '1').property('name', 'Alice').next()

# Example: Add another vertex
g.addV('person').property('id', '2').property('name', 'Bob').next()

# Example: Create an edge between Alice and Bob
g.V('1').addE('knows').to(g.V('2')).property('since', 2023).next()

# Example: Query the graph
results = g.V().hasLabel('person').valueMap(True).toList()
for result in results:
    print(result)

# Close the connection
connection.close()
