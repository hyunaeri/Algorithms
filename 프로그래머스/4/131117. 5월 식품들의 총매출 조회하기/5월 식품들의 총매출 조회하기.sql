-- FOOD_PRODUCT 테이블 : product_id, product_name, product_cd, category, price
-- FOOD_ORDER 테이블 : order_id, product_id, amount, produce_date, in_date, out_date, factory_id, warehouse_id
SELECT 
    p.product_id,
    p.product_name,
    SUM(p.price * o.amount) as total_sales
FROM food_product p
JOIN food_order o ON p.product_id = o.product_id
WHERE produce_date like "2022-05%"
GROUP BY p.product_id, p.product_name
ORDER BY total_sales DESC, p.product_id ASC;