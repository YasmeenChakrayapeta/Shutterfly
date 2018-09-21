#Shutterfly Customer Lifetime Value

**Assumptions**


1.While updating customer considering updating last_name, adr_city, adr_state and not updating event_time assuming that we will lose the customer event_time needed for LTV calculation.

2.While updating orders considering updating event_time, total_amount and not customer_id assuming that we need the customer id corresponding to a particular order.

3.If an order has been placed then assuming that, there will be a site_visit entry in the input event data corresponding to that order.
