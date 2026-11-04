from mcp.server.fastmcp import FastMCP

mcp = FastMCP("WeatherServer", instructions="You are a weather server that can provide weather information based on the given location. You should only return the weather information, and nothing else. Do not explain your answer or provide any additional information. If you cannot provide the weather information, return 'I cannot provide the weather information for this location.'")

@mcp.tool()
def get_weather(location: str) -> str:
    """Get the weather information for a given location."""
    # Here you would implement the logic to fetch weather information based on the location.
    # For demonstration purposes, we'll return a placeholder response.
    return f"The weather in {location} is sunny with a temperature of 25°C."

if __name__ == "__main__":
    mcp.run(transport="streamable-http")