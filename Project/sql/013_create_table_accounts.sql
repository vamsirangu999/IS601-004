CREATE TABLE
    IS601_S_Accounts(
        id int auto_increment PRIMARY KEY,
        user_id VARCHAR(20) unique,
        balance VARCHAR(40),
        created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
        modified TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
    )