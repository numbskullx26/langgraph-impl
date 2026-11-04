from fastmcp import FastMCP

mcp = FastMCP("MathServer", instructions="You are a math server that can solve math problems and return the answer. You should only return the answer to the math problem, and nothing else. Do not explain your answer or provide any additional information. If you cannot solve the problem, return 'I cannot solve this problem.'")

@mcp.tool
def add(a:int , b:int) -> int:
    """Add two integers and return the result."""
    return a + b

@mcp.tool
def multiply(a:int , b:int) -> int:
    """Multiply two integers and return the result."""
    return a * b

#the transport argument "stdio" is used to specify that the server should communicate with the client using standard input and output streams. This means that the server will read input from the standard input (stdin) and write output to the standard output (stdout). This is a common way for command-line applications to interact with each other, allowing for easy integration with other tools and scripts.

if __name__ == "__main__":
    mcp.run(transport="stdio")

    