select count(*) as USERS from USER_INFO
where date_format(JOINED, '%Y') = '2021' and AGE >= 20 and AGE <= 29;