from mcp.server.fastmcp import FastMCP
import requests
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

url = os.getenv("ORDERBRO_API_URL", "http://127.0.0.1:8000/")
token = os.getenv("ORDERBRO_TOKEN")

mcp = FastMCP("OrderBro-agent")
user_id = os.getenv("ORDERBRO_USER_ID", "15") 

@mcp.tool()
def fetch_available_products() -> dict:
    """
    Retrieve the list of all available products
    across all shops within the OrderBro system.
    Returns:
        dict: A list of products with their details.
    """
    response = requests.get(url + "products")
    return response.json()


@mcp.tool()
def available_users() -> dict:
    """
    Fetch the list of all available users (friends)
    who can receive orders within their allowed limits.
    Returns:
        dict: A list of users with their details.
    """
    response = requests.get(url + "users")
    return response.json()


@mcp.tool()
def ordered_me() -> dict:
    """
    Fetch all pending orders assigned to the current user.
    This helps track outstanding requests directed to you.
    Returns:
        dict: A list of pending orders for the user.
    """
    params = {
        "id": user_id,    # optional: replace with dynamic user id later
        "status": "pending"
    }
    response = requests.get(url + "orders/me", params=params)
    return response.json()


@mcp.tool()
def cancel_order(order_id) -> dict:
    """
    Cancel an existing order using its order ID.
    Requires authentication token for authorization.
    Args:
        order_id (int): The ID of the order to be cancelled.
    Returns:
        dict: API response indicating success or failure.
    """
    payload = {
        "token": token,
        "status": "cancelled",
        "id": order_id
    }
    response = requests.post(url + "orders", json=payload)
    return response.json()


@mcp.tool()
def give_order_to_friend(products: list, friend_id: int) -> dict:
    """
    Create an order and assign it to a selected friend.

    Args:
        products (list): List of dicts with {product_id, quantity}.
        friend_id (int): The user ID of the friend receiving the order.

    Returns:
        dict: API response with order details.
    """
    payload = {
        "req_to": friend_id,
        "token": token,
        "items": products
    }
    response = requests.post(url + "orders/me", json=payload)
    return response.json()


if __name__ == "__main__":
    mcp.run()
