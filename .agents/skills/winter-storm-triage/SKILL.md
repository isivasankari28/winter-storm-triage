---
name: winter-storm-triage
description: Standard operating procedures for handling customer inquiries and package delays caused by severe winter storms. Use this skill when verifying delayed orders, determining loyalty tier compensations, issuing compensation, and drafting empathetic customer responses.
---

# Winter Storm Package Delay Triage SOP

This skill outlines the Standard Operating Procedures (SOP) for customer support agents assisting customers whose package deliveries are delayed due to severe winter storms.

## Workflow Overview

When a customer contacts support regarding a package delayed by severe winter weather, follow these steps in order:

1. **Verify the Order and Loyalty Status**: Check order status and customer loyalty information using the designated tools.
2. **Determine Compensation Tier**: Lookup the customer's loyalty tier and identify the eligible credit amount and shipping upgrade.
3. **Issue Disruption Compensation**: Apply the refund/credit and shipping upgrade via tool execution.
4. **Draft Empathetic Customer Response**: Communicate the resolution clearly and empathetically to the customer.

---

## Step 1: Verification

Before taking any compensatory actions, verify the order details and the customer's loyalty status:

1. **Verify Order Status**:
   - Call the `get_order_status` tool with the provided `order_id`.
   - Confirm that the package status is `DELAYED` and the delay reason relates to severe winter storms (e.g., severe weather at fulfillment center or transit route).
   - Extract the `customer_id` from the order details.

2. **Verify Customer Loyalty Tier**:
   - Call the `get_customer_loyalty_info` tool using the `customer_id` obtained in the previous step.
   - Note the customer's loyalty tier (`PLATINUM`, `GOLD`, `SILVER`, or `MEMBER`).

---

## Step 2: Compensation Policy Matrix

Apply the following compensation and shipping upgrade strictly according to the customer's loyalty tier:

| Loyalty Tier | Credit / Refund Amount | Shipping Upgrade |
| :--- | :--- | :--- |
| **Platinum** | $100 credit | Next-Day Air shipping upgrade |
| **Gold** | $50 credit | Next-Day Air shipping upgrade |
| **Silver** | $25 credit | 3-Day Select shipping upgrade |
| **Member** | $10 credit | Priority Shipping upgrade |

- **Platinum**: $100 credit, Next-Day Air shipping upgrade
- **Gold**: $50 credit, Next-Day Air shipping upgrade
- **Silver**: $25 credit, 3-Day Select shipping upgrade
- **Member**: $10 credit, Priority Shipping upgrade

---

## Step 3: Apply Disruption Compensation

Once the tier and corresponding compensation are determined, you must apply the compensation by calling the `issue_disruption_compensation` tool with the following parameters:

- `customer_id`: The ID of the affected customer (e.g., `CUST-7742`).
- `compensation_amount`: The credit amount corresponding to their tier (e.g., `$100`, `$50`, `$25`, or `$10`).
- `shipping_upgrade`: The upgraded shipping method corresponding to their tier (e.g., `Next-Day Air`, `3-Day Select`, or `Priority Shipping`).

Ensure the tool returns a confirmation that the compensation and shipping upgrade have been successfully applied.

---

## Step 4: Draft an Empathetic Customer Response

Draft an empathetic, professional customer response detailing the situation and resolution. The communication should include:

1. **Empathetic Acknowledgment**: Express sincere empathy and apologize for the inconvenience caused by the severe winter storm delay. Acknowledge the importance of their delivery.
2. **Transparent Explanation**: Clearly explain that severe winter weather conditions disrupted operations at the fulfillment facility or shipping transit, affecting delivery schedules.
3. **Resolution Details**:
   - State the specific credit amount applied to their account.
   - Confirm that their shipping has been upgraded (specifying the upgrade tier: Next-Day Air, 3-Day Select, or Priority Shipping) to expedite delivery as soon as weather conditions allow safe transit.
4. **Appreciation & Support**: Thank the customer for their patience, express appreciation for their loyalty (referencing their loyalty tier), and offer further assistance if needed.

### Sample Customer Response Template

> Dear [Customer Name],
>
> Thank you for reaching out to Cymbal Direct. We sincerely apologize for the delay in delivering your order ([Order ID]). A severe winter storm in the region has temporarily disrupted operations at our East Coast fulfillment center, impacting transit routes. We understand how frustrating delivery delays can be, and we appreciate your patience as our teams work safely to get your items to you.
>
> As a valued [Tier] member, we have taken the following steps to resolve this for you:
> - A **[Compensation Amount] credit** has been applied to your account.
> - Your order shipping has been upgraded to **[Shipping Upgrade]** at no additional cost to ensure it reaches you as quickly as possible once safe operations resume.
>
> We truly value your business and loyalty. If you have any further questions or need additional assistance, please do not hesitate to contact us.
>
> Warm regards,  
> Cymbal Direct Customer Care
