
-------------Release 1 : Create, Update, and Delete Data-------
-- Insert Product Types
INSERT INTO product_types (type_name) VALUES ('Elektonik');
INSERT INTO product_types (type_name) VALUES ('Pakaian');
INSERT INTO product_types (type_name) VALUES ('Home Dekor');

select * from product_types pt 

-- Insert Products 2 product pada id=1
INSERT INTO products (name, product_type_id, brand) VALUES ('Iphone 15', 1, 'Dell');
INSERT INTO products (name, product_type_id, brand) VALUES ('Ipad Pro 2023', 1, 'Dell');

-- Insert Products 3 product pada id=2
INSERT INTO products (name, product_type_id, brand) VALUES ('Sweater', 2, 'Uniqlo');
INSERT INTO products (name, product_type_id, brand) VALUES ('T-Shirt', 2, 'Erigo');
INSERT INTO products (name, product_type_id, brand) VALUES ('T-Shirt', 2, 'Consina');

-- Insert Products 3 product pada id=3
insert into products (name, product_type_id, brand) values ('Chandelier', 3, 'ACE');
insert into products (name, product_type_id, brand) values ('Kaca', 3, 'informa');
insert into products (name, product_type_id, brand) values ('Wall Art', 3, 'IKEA');

select * from products

-- Insert Product Descriptions pada setiap product yang sudah dimasukkan yaitu 8 id
insert into product_descriptions (product_id, description) values (1, 'Handphone Iphone Versi KW dari Dell');
insert into product_descriptions (product_id, description) values (2, 'Ipad pro harga dengan miring dari Dell ');
insert into product_descriptions (product_id, description) values (3, 'Sweater musim semi dari Uniqlo 2024 ');
insert into product_descriptions (product_id, description) values (4, 'Baju outdoor dengan harga afforable dari Erigo');
insert into product_descriptions (product_id, description) values (5, 'T-Shirt outdoor Ekslusif dengan harga mahal dari Eiger dong');
insert into product_descriptions (product_id, description) values (6, 'Lampu hias mewah dari ACE hardware dengan promo 50%');
insert into product_descriptions (product_id, description) values (7, 'Kaca Minimalis dari informa');
insert into product_descriptions (product_id, description) values (8, 'Walt art kece by Wartadi IKEA ');

select * from product_descriptions pd 

-- Insert 3 Payment Methods
insert into payment_methods (method_name) values ('QR');
insert into payment_methods (method_name) values ('Debit');
insert into payment_methods (method_name) values ('Pay Later');

select * from payment_methods

-- Insert Users
insert into users (name, address, birth_date, status_user, gender) values ('Johnatan Christie', 'Banyuwangi', '1990-01-01', 'Aktif', 'M');
insert into users (name, address, birth_date, status_user, gender) values ('Antoni Ginting', 'Cimahi', '1985-05-15', 'Aktif', 'M');
insert into users (name, address, birth_date, status_user, gender) values ('Fajar Alfian', 'Bandung', '1992-09-23', 'NonAktif', 'M');
insert into users (name, address, birth_date, status_user, gender) values ('Gregoria Mariska', 'Kudus', '1992-09-23', 'Aktif', 'F');
insert into users (name, address, birth_date, status_user, gender) values ('Liliana Natsir', 'Medan', '1992-09-23', 'NonAktif', 'F');

select * from users u 


-- Insert Transactions 3 User
insert into transactions (user_id) values (1);
insert into transactions (user_id) values (2);
insert into transactions (user_id) values (3);
select * from transactions t 


-- Insert product Transaction Details
insert into transaction_details (transaction_id, product_id, quantity) values (1, 2, 2);
insert into transaction_details (transaction_id, product_id, quantity) values (1, 3, 2);
insert into transaction_details (transaction_id, product_id, quantity) values (1, 5, 4);
insert into transaction_details (transaction_id, product_id, quantity) values (2, 3, 1);
insert into transaction_details (transaction_id, product_id, quantity) values (2, 1, 3);
insert into transaction_details (transaction_id, product_id, quantity) values (2, 3, 2);
insert into transaction_details (transaction_id, product_id, quantity) values (2, 7, 1);
insert into transaction_details (transaction_id, product_id, quantity) values (3, 4, 2);
insert into transaction_details (transaction_id, product_id, quantity) values (3, 3, 2);
insert into transaction_details (transaction_id, product_id, quantity) values (3, 3, 1);
insert into transaction_details (transaction_id, product_id, quantity) values (3, 6, 1);

select * from transaction_details td 

-----------------------------------------
--- 2.select
--- 2.a  tampikan nama user/pelanggan dengan gender laki-laki/M.
select  name from  users where  gender = 'M';

-- 2.b tampilkan product dengan id=3
select * from products where id = 3;

-- 2.c Select Users Created in Last 7 Days Containing 'a'

------karena sebelumnya created_at = now, maka kita update terlebih dahulu data user 
update users set created_at = '2024-06-08 11:32:01.804' where id = 5;

select * from  users 
where  created_at <= (CURRENT_DATE - INTERVAL '7 days') 
AND name LIKE '%a%';

-- 2.d Hitung jumlah user/pelanggan dengan status gender Perempuan
select COUNT(*)  from  users where  gender = 'F';

-- 2.e tamplilkan pelanggan dengan urutan sesuai abjad
SELECT * FROM users ORDER BY name;

-- 2.f tampilkan 5 data transaksi dengan id=3
SELECT * FROM transaction_details WHERE product_id = 3 LIMIT 5;

--------------update --------------
----3.a update data product id 1 dengan nama 'product dummy'

UPDATE products SET name = 'product dummy' WHERE id = 1;
select * from products p 

----3.b update qty = 3 pada transaction detail dengan product id =1
UPDATE transaction_details SET quantity = 3 WHERE product_id = 1;
select * from transaction_details td 

-- 4. DELETE------
---- 4.a Delete data pada tabel product dengan id 1
DELETE FROM products WHERE id = 1;

---- 4.b delete pada tabel product dengan dengan product type 1
DELETE FROM products WHERE product_type_id = 1;

----conditioning tambahan untuk harga di Kolom Product
select * from products p 
alter table products add column price numeric (10,2);

update products set price = '25000000' where id = 1;
update products set price = '4500000' where id = 2;
update products set price = '350000' where id = 3;
update products set price = '140000' where id = 4;
update products set price = '640000' where id = 5;
update products set price = '7400000' where id = 6;
update products set price = '1504000' where id = 7;
update products set price = '840000' where id = 8;

-------------Release 2 : Join, Union, Sub-query, Functions----------

-- 1. Gabungkan data transaksi dari user id 1 dan user 2.
SELECT * FROM transactions WHERE user_id IN (1, 2);

-- 2. tampilkan jumlah harga transaksi user id 1.
SELECT SUM(td.quantity * p.price) AS total_price
FROM transaction_details td
JOIN products p ON td.product_id = p.id
WHERE td.transaction_id IN (SELECT id FROM transactions WHERE user_id = 1);

-- 3. Tampilkan total transaksi dengan product type 2.
SELECT COUNT(*) FROM transaction_details td
JOIN products p ON td.product_id = p.id
WHERE p.product_type_id = 2;

-- 4. tampilkan data semua field table product dan 
------ field name table product type yang saling berhubungan
------ product type
SELECT p.*, pt.type_name FROM products p
JOIN product_types pt ON p.product_type_id = pt.id;

-- 5. tampilkan field table transaction, field name table product 
----- dan field name table user
SELECT t.*, p.name AS product_name, u.name AS user_name
FROM transactions t
JOIN transaction_details td ON t.id = td.transaction_id
JOIN products p ON td.product_id = p.id
JOIN users u ON t.user_id = u.id;

-- 6. tampilkan data products yang tidak ada di tabel transaction_detaiks 
---- dengan sub query
SELECT * FROM products 
WHERE id NOT IN (SELECT product_id FROM transaction_details);

----7. Trigger functions

create or replace function trigger_set_gender()
returns trigger as $$
begin
	
	new.gender = L;
	return new;
end;
$$ language plpgsql;


create trigger set_gender
before update on users
for each row 
execute procedure 
trigger_set_gender()


select * from users u 


---8.