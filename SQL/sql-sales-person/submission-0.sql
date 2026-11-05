WITH crimson_orders AS (
    SELECT o.order_id, o.sales_id
    FROM orders o
    JOIN company c ON o.com_id = c.com_id
    WHERE c.name = 'CRIMSON'
)
SELECT sp.name
FROM sales_person sp
LEFT JOIN crimson_orders co ON sp.sales_id = co.sales_id
WHERE co.order_id IS NULL;