WITH minuteintervals AS (
SELECT store_id,
DATE_TRUNC('hour', transaction_datetime) + INTERVAL '15 min'* FLOOR(EXTRACT(minute from transaction_datetime )/15.0) AS timeblock,
total_amount,
order_id
FROM qsr_logs
WHERE EXTRACT (HOUR FROM transaction_datetime)>=5 OR EXTRACT(HOUR FROM transaction_datetime)<=1 
),
revenue AS (
SELECT store_id,
timeblock,
SUM(total_amount) AS block_revenue,
COUNT(order_id) AS total_orders
FROM minuteintervals
GROUP BY store_id, timeblock
)
SELECT r.store_id, r.timeblock, r.total_orders, r.block_revenue,
(SELECT COUNT(employee_id)
FROM staffing_logs s
WHERE s.store_id = r.store_id AND r.timeblock >= s.clock_IN_time AND r.timeblock < s.clock_out_time
) AS staff_count,
COALESCE(
(SELECT SUM (hourly_wage)/4.0
FROM staffing_logs s
WHERE s.store_id = r.store_id AND r.timeblock >= s.clock_IN_time AND r.timeblock < s.clock_out_time
),0) AS labor_cost

FROM revenue r
ORDER BY r.store_id, r.timeblock;