import requests

# Set GraphQL endpoint
gql_host = "linda-cluster.mdh.quantum.com "
gql_port = "30081"
gql_endpoint = f"http://{gql_host}:{gql_port}/graphql"

# Define your GraphQL query
graphql_query = """
{
  yourGraphQLQuery {
    field1
    field2
    # Add more fields as needed
  }
}
"""

# Set headers if needed
headers = {
    "Content-Type": "application/json",
    # Add any other headers as needed
}

# Set your query variables if needed
variables = {
    "variable1": "value1",
    "variable2": "value2",
    # Add any other variables as needed
}

# Create the GraphQL request payload
payload = {
    "query": graphql_query,
    "variables": variables,
}

# Make the GraphQL request
response = requests.post(gql_endpoint, json=payload, headers=headers)

# Check the response status code
if response.status_code == 200:
    # Print the response content
    print(response.json())
else:
    print(f"GraphQL request failed with status code: {response.status_code}")
    print(response.text)
