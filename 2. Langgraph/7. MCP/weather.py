from mcp.server.fastmcp import FastMCP

weather_mcp = FastMCP("WeatherServer")

@weather_mcp.tool()
async def get_weather(location:str) -> str:
  """Get weather for a particular location"""
  return f"Its always Raining in {location}" # Just for demo purposes, here code of getting weather information will come


if __name__ == "__main__":
  weather_mcp.run(transport="streamable-http")