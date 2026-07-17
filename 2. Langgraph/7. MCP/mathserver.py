from mcp.server.fastmcp import FastMCP

mcp = FastMCP("MathServer") # Object with a name of our server


@mcp.tool()
def add(a:int, b:int) -> int :
  """Add two numbers and accepts two numeric values only
  args:
  a : int
  b : int
  """
  return a + b

@mcp.tool()
def multiply(a:int, b:int) -> int :
  """Multiply two numbers and accepts two numeric values only
  args:
  a : int
  b : int
  """
  return a * b


if __name__ == "__main__":
  mcp.run() # Run this server using the "transport="stdio"