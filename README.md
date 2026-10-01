# GenAI 144 Challenge: Winter Storm Triage Agent ❄️📦

> Complete implementation, evaluation, and production deployment of the **Winter Storm Triage Agent** using **Google Agent Development Kit (ADK)**, **FastMCP**, and **Vertex AI Agent Runtime**.

![Winter Storm Triage Demo](./demo.svg)

---

## 🚀 Overview

This repository contains the end-to-end solution for the GenAI Challenge:
- **FastMCP Server**: Custom logistics server with order lookup, loyalty tiers, and compensation actions.
- **Winter Storm Triage Agent**: ADK agent powered by `gemini-3.8-flash` enforcing standard operating procedures for delivery disruption.
- **Automated Evaluations**: Response quality benchmarks evaluated with LLM-as-a-judge.
- **Production Deployment**: Cloud-native deployment to **Google Cloud Vertex AI Agent Runtime** in `us-west1`.

---

## 🏗️ System Architecture

```mermaid
flowchart TD
    User["Customer / Client"] -->|ADK Remote Query / A2A| AgentRuntime["Vertex AI Agent Runtime (us-west1)"]
    AgentRuntime --> Agent["Winter Storm Triage Agent (Gemini 3.8 Flash)"]
    
    subgraph AgentRuntime ["Vertex AI Agent Runtime"]
        Agent -->|ADK McpToolset (stdio)| FastMCP["FastMCP Logistics Server (cymbal_direct_mcp.py)"]
        
        subgraph FastMCP ["Logistics Tools"]
            O["get_order_status"]
            L["get_customer_loyalty_info"]
            C["issue_disruption_compensation"]
        end
    end
```

---

## 📋 Winter Storm Triage Policy (SOP)

| Loyalty Tier | Disruption Account Credit | Complimentary Shipping Upgrade |
|---|---|---|
| 💎 **Platinum** | **$100 credit** | **Next-Day Air** |
| 🥇 **Gold** | **$50 credit** | **Next-Day Air** |
| 🥈 **Silver** | **$25 credit** | **3-Day Select** |
| 👤 **Member** | **$10 credit** | **Priority Shipping** |

---

## 🎬 Working Examples

### 1. Gold Tier Customer (`CYM-EC-9921`)
- **Query:** `"What is the status of order CYM-EC-9921?"`
- **MCP Calls:**
  - `get_order_status(order_id="CYM-EC-9921")` ➔ `DELAYED` due to winter storm at East Coast center.
  - `get_customer_loyalty_info(customer_id="CUST-7742")` ➔ `GOLD` tier.
  - `issue_disruption_compensation(customer_id="CUST-7742", compensation_amount="$50", shipping_upgrade="Next-Day Air")` ➔ Success.
- **Outcome:** Empathetic message with $50 credit and Next-Day Air upgrade.

### 2. Platinum Tier Customer (`CYM-EC-1002`)
- **Query:** `"What is the status of order CYM-EC-1002?"`
- **MCP Calls:**
  - `get_order_status(order_id="CYM-EC-1002")` ➔ `DELAYED`.
  - `get_customer_loyalty_info(customer_id="CUST-1002")` ➔ `PLATINUM` tier.
  - `issue_disruption_compensation(customer_id="CUST-1002", compensation_amount="$100", shipping_upgrade="Next-Day Air")` ➔ Success.
- **Outcome:** Empathetic message with $100 credit and Next-Day Air upgrade.

---

## 🛠️ Quick Commands

```bash
cd winter-storm-triage

# Install dependencies
agents-cli install

# Run locally in CLI
agents-cli run "What is the status of order CYM-EC-9921?"

# Launch interactive web playground
agents-cli playground

# Run unit and integration tests
uv run pytest -v

# Evaluate quality flywheel
agents-cli eval run

# Query deployed Agent Runtime in us-west1
agents-cli run \
  --url "https://us-west1-aiplatform.googleapis.com/v1/projects/519180330931/locations/us-west1/reasoningEngines/6878865800761966592" \
  --mode adk \
  "What is the status of order CYM-EC-9921?"
```

---

## 📁 Repository Contents

- [`winter-storm-triage/`](./winter-storm-triage/): Complete ADK agent project.
- [`mcp/cymbal_direct_mcp.py`](./mcp/cymbal_direct_mcp.py): FastMCP server.
- [`demo.svg`](./demo.svg): Animated terminal screen recording.
- [`summary_task2.md`](./summary_task2.md): MCP setup and tool registration summary.
- [`summary_task3.md`](./summary_task3.md): Custom skill and SOP rules summary.
- [`summary_task4.md`](./summary_task4.md): Agent scaffolding, test, and eval summary.
- [`summary_task5.md`](./summary_task5.md): Vertex AI Agent Runtime deployment summary.
