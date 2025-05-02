
---------SQL basics---------
1. select * from (table_name)

2. select column1 , column2 from table_name;

3. select * from table_name where country = 'USA';

4. select * from table_name where id  > 50;

5. INSERT INTO table_name (column1, column2) values (value1, value2);

6. UPDATE - Modify existing records
   UPDATE table_name SET column1 = value1 WHERE condition;
   UPDATE products SET price = 29.99 WHERE product_id = 101;

7. DELETE - Remove records
   DELETE FROM table_name WHERE condition;
   DELETE FROM orders WHERE order_id = 1005;

8. ORDER BY - Sort results
   SELECT * FROM products ORDER BY price DESC;  -- Descending order
   SELECT * FROM employees ORDER BY last_name ASC;  -- Ascending (default)
