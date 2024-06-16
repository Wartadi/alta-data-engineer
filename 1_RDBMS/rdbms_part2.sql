
create database alta_online_shop;

-----PART 2 RELATIONAL DATABASE
--  2.a create table user
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    address TEXT,
    birth_date DATE,
    status_user VARCHAR(50),
    gender CHAR(1),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
-- 2.b create product, product_type, product_description,payment_method
CREATE TABLE products (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    product_type_id INT REFERENCES product_types(id),
    brand VARCHAR(100)
);

CREATE TABLE product_types (
    id SERIAL PRIMARY KEY,
    type_name VARCHAR(100)
);



-- Product Description Table
CREATE TABLE product_descriptions (
    id SERIAL PRIMARY KEY,
    product_id INT REFERENCES products(id),
    description TEXT
);

-- Payment Methods Table
CREATE TABLE payment_methods (
    id SERIAL PRIMARY KEY,
    method_name VARCHAR(100)
);


--3. Create table Transaction Table & Transaction Details Table
CREATE TABLE transactions (
    id SERIAL PRIMARY KEY,
    user_id INT REFERENCES users(id),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE transaction_details (
    id SERIAL PRIMARY KEY,
    transaction_id INT REFERENCES transactions(id),
    product_id INT REFERENCES products(id),
    quantity INT
);

-- 4.Courier Table
CREATE TABLE kurir (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    ongkos_dasar DECIMAL(10, 2)
);
select * from users
select * from transactions
select * from transaction_details
select * from products
select * from product_types
select * from product_descriptions
select * from payment_methods
select * from kurir


--5.Rename Kurir Table
ALTER TABLE kurir RENAME TO shipping;

select * from shipping 

--6.Drop Shipping Table karena tidak dibutuhkan
DROP TABLE shipping;


----7. Silahkan tambahkan entity baru
---7.a One-to-One Relationship payment method dengan description
ALTER TABLE payment_methods ADD COLUMN description_id INT;
ALTER TABLE payment_methods ADD CONSTRAINT fk_description FOREIGN KEY (description_id) REFERENCES product_descriptions(id);

---7.b One-to-Many Relationship user dengan alamat
CREATE TABLE addresses (
    id SERIAL PRIMARY KEY,
    user_id INT REFERENCES users(id),
    address TEXT
);

--7.c Many-to-Many Relationship user dengan payment_method menjadi user_payment_methode_detail
CREATE TABLE user_payment_method_details (
    id SERIAL PRIMARY KEY,
    user_id INT REFERENCES users(id),
    payment_method_id INT REFERENCES payment_methods(id)
);

select * from addresses
select * from user_payment_method_details 
