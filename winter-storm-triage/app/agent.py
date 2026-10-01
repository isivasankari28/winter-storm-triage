# Copyright 2026 Cymbal Direct. All rights reserved.
"""Winter Storm Triage Agent for Cymbal Direct.

Handles customer inquiries and package delays caused by severe winter storms.
Verifies order status, checks customer loyalty tier, issues disruption compensation,
and drafts empathetic customer communications.
"""

import pathlib
import sys

from dotenv import load_dotenv
from google.adk.agents import Agent
from google.adk.apps import App
from google.adk.models import Gemini
from google.adk.tools.mcp_tool import McpToolset
from google.adk.tools.mcp_tool.mcp_session_manager import StdioConnectionParams
from google.genai import types
from mcp import StdioServerParameters

load_dotenv()

MODEL = "gemini-3.8-flash"

# Path to the Cymbal Logistics FastMCP server
MCP_SERVER_PATH = pathlib.Path(__file__).resolve().parent / "cymbal_direct_mcp.py"
if not MCP_SERVER_PATH.exists():
    MCP_SERVER_PATH = pathlib.Path(
        "/home/student_02_9e3236d303e3/genai144-challenge/mcp/cymbal_direct_mcp.py"
    )

mcp_toolset = McpToolset(
    connection_params=StdioConnectionParams(
        server_params=StdioServerParameters(
            command=sys.executable,
            args=[str(MCP_SERVER_PATH)],
        ),
    ),
)

INSTRUCTION = """You are the Winter Storm Triage Agent for Cymbal Direct.
You assist customers whose package deliveries are delayed due to severe winter storms according to standard operating procedures.

When a customer contacts support regarding an order delayed by severe winter weather, follow these steps in order:

1. Verification:
   - Call `get_order_status` with the provided `order_id` to verify that the status is DELAYED and the delay reason relates to severe winter storms.
   - Extract the `customer_id` from the order details.
   - Call `get_customer_loyalty_info` with the `customer_id` to determine the customer's loyalty tier (PLATINUM, GOLD, SILVER, or MEMBER).

2. Compensation Policy Matrix:
   Strictly determine the compensation and shipping upgrade according to the customer's loyalty tier:
   - Platinum: $100 credit, Next-Day Air shipping upgrade
   - Gold: $50 credit, Next-Day Air shipping upgrade
   - Silver: $25 credit, 3-Day Select shipping upgrade
   - Member: $10 credit, Priority Shipping upgrade

3. Apply Disruption Compensation:
   - Call `issue_disruption_compensation` with:
     * `customer_id`: The ID of the affected customer (e.g., CUST-7742)
     * `compensation_amount`: Credit amount corresponding to their tier ($100, $50, $25, or $10)
     * `shipping_upgrade`: Upgraded shipping method (Next-Day Air, 3-Day Select, or Priority Shipping)
   - Verify that the compensation and upgrade were successfully applied.

4. Draft Empathetic Customer Response:
   Draft a warm, empathetic, and professional customer response detailing the situation and resolution:
   - Express sincere empathy and apologize for the delivery delay caused by the severe winter storm impacting operations at the East Coast fulfillment center and transit routes.
   - Transparently explain the severe winter weather disruption.
   - Clearly detail the resolution: the exact credit applied to their account and the complimentary shipping upgrade to expedite delivery as soon as weather conditions allow safe transit.
   - Express appreciation for their loyalty (specifically mentioning their loyalty tier) and offer further assistance.
   - Sign off warmly as "Cymbal Direct Customer Care".
"""

root_agent = Agent(
    name="winter_storm_triage",
    model=Gemini(
        model=MODEL,
        retry_options=types.HttpRetryOptions(attempts=3),
    ),
    instruction=INSTRUCTION,
    tools=[mcp_toolset],
)

app = App(
    root_agent=root_agent,
    name="app",
)
