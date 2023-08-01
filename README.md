# WEEK5
## TASK 3 SQL CRUD
### 1. 使用 INSERT 指令新增一筆資料到 member 資料表中，這筆資料的 username 和 password 欄位必須是 test。接著繼續新增至少 4 筆隨意的資料。
```
insert into member(name,username,password,follower_count)values('Brian','test','test',30);
insert into member(name,username,password,follower_count)values('Ted','test2','test2',50);
insert into member(name,username,password,follower_count)values('Lily','test3','test3',10);
insert into member(name,username,password,follower_count)values('Kevin','test4','test4',130);
insert into member(name,username,password,follower_count)values('Kem','test5','test5',300);
```
### 2. 使用 SELECT 指令取得所有在 member 資料表中的會員資料。
```
select * from member;
```
<img width="551" alt="image" src="https://github.com/Brian-Wang0926/week1/assets/71397277/eb46a8d1-8ae9-44d4-bc9c-88af6799eda9">

### 3. 使用 SELECT 指令取得所有在 member 資料表中的會員資料，並按照 time 欄位，由近到遠排序。
```
SELECT * FROM member order by time DESC;
```
<img width="539" alt="image" src="https://github.com/Brian-Wang0926/week1/assets/71397277/4354c930-5d85-4a09-ae1e-3c67709bf508">

### 4. 使用 SELECT 指令取得 member 資料表中第 2 到第 4 筆共三筆資料，並按照 time 欄位，由近到遠排序。( 並非編號 2、3、4 的資料，而是排序後的第 2 ~ 4 筆資料 )
```
SELECT * FROM member order by time DESC LIMIT 1,3;
```
<img width="532" alt="image" src="https://github.com/Brian-Wang0926/week1/assets/71397277/2551ab61-2e2b-475e-beca-a0fb5ba6b37b">

### 5. 使用 SELECT 指令取得欄位 username 是 test 的會員資料。
```
SELECT * FROM member WHERE username='test';
```
<img width="536" alt="image" src="https://github.com/Brian-Wang0926/week1/assets/71397277/957c133b-4a96-43ce-ad3a-9ccf82c8121d">

### 6. 使用 SELECT 指令取得欄位 username 是 test、且欄位 password 也是 test 的資料。
```
SELECT * FROM member WHERE username='test' and password='test';
```
<img width="537" alt="image" src="https://github.com/Brian-Wang0926/week1/assets/71397277/6eb67949-23ec-430e-8630-9a68e141f168">

### 7. 使用 UPDATE 指令更新欄位 username 是 test 的會員資料，將資料中的 name 欄位改成 test2。
```
UPDATE member SET name='test2' WHERE username='test';
```
<img width="539" alt="image" src="https://github.com/Brian-Wang0926/week1/assets/71397277/9e06e6ec-2c5f-4710-9b7b-5bc29beb1e2a">

## TASK 4 SQL Aggregate Functions
### 1. 取得 member 資料表中，總共有幾筆資料 ( 幾位會員 )。
```
select count(*) from member;
```
<img width="99" alt="image" src="https://github.com/Brian-Wang0926/week1/assets/71397277/d00f1530-6b6f-434c-9d95-81803e84c6b6">

### 2. 取得 member 資料表中，所有會員 follower_count 欄位的總和。
```
select sum(follower_count) from member;
```
<img width="168" alt="image" src="https://github.com/Brian-Wang0926/week1/assets/71397277/076c6464-5f39-4288-922c-84b98d2bd894">

### 3. 取得 member 資料表中，所有會員 follower_count 欄位的平均數。
```
select avg(follower_count) from member;
```
<img width="169" alt="image" src="https://github.com/Brian-Wang0926/week1/assets/71397277/44c9d05d-ec9d-4b0b-b697-7603e38caa9e">


## TASK 5 SQL JOIN
### 1. 在資料庫中，建立新資料表紀錄留言資訊，取名字為 message。資料表中必須包含以下欄位設定:

<img width="516" alt="image" src="https://github.com/Brian-Wang0926/week1/assets/71397277/ad54bf92-de13-4a56-a9f8-9486c042bf9f">

<br/>

* 建立 table message

```
create table message(
  id BIGINT PRIMARY KEY AUTO_INCREMENT,
  member_id BIGINT NOT NULL,content VARCHAR(255) NOT NULL,
  like_count INT UNSIGNED NOT NULL DEFAULT 0,
  time DATETIME NOT NULL DEFAULT NOW(),
  FOREIGN KEY(member_id) references member(id)
);
```

<img width="588" alt="image" src="https://github.com/Brian-Wang0926/week1/assets/71397277/98c0189f-b120-4067-adcc-fd85ca25b455">

<br/>

* 新增資料進 table message

```
insert into message(member_id,content,like_count) values(1,"很好～",3);
insert into message(member_id,content,like_count) values(2,"goooooood",0);
insert into message(member_id,content,like_count) values(4,"+1111111111",9);
insert into message(member_id,content,like_count) values(1,"不可能留兩次言吧",30);
insert into message(member_id,content,like_count) values(5,"77777777",2);
```
<img width="570" alt="image" src="https://github.com/Brian-Wang0926/week1/assets/71397277/4b3b9916-1fba-4a2c-b81e-651a8a7d0d06">

### 2. 使用 SELECT 搭配 JOIN 語法，取得所有留言，結果須包含留言者的姓名。

* 有留言的一定是會員，但會員不一定會留言，故使用inner join 或 left join 都可以得到相同答案

```
select message.content,member.name from message
inner join member on message.member_id=member.id;
```
<img width="256" alt="image" src="https://github.com/Brian-Wang0926/week1/assets/71397277/c680782a-a781-43ff-8c2b-ccba34d74f18">

```
select message.content,member.name from message
left join member on message.member_id=member.id;
```
<img width="260" alt="image" src="https://github.com/Brian-Wang0926/week1/assets/71397277/9f711327-1c07-4b2d-80f0-99aa8767182d">

### 3. 使用 SELECT 搭配 JOIN 語法，取得 member 資料表中欄位 username 是 test 的所有留言，資料中須包含留言者的姓名。
```
select message.content,member.name from message
inner join member on message.member_id=member.id
where member.username='test';
```
<img width="264" alt="image" src="https://github.com/Brian-Wang0926/week1/assets/71397277/87f0351a-f6d5-4018-8dfa-4d6adebc94a7">

```
select message.content,member.name from message
left join member on message.member_id=member.id
where member.username='test';
```
<img width="258" alt="image" src="https://github.com/Brian-Wang0926/week1/assets/71397277/f60e47be-4db1-429e-b642-89fb3ad7e563">

### 4. 使用 SELECT、SQL Aggregate Functions 搭配 JOIN 語法，取得 member 資料表中欄位 username 是 test 的所有留言平均按讚數。
```
select avg(like_count) from message
inner join member on message.member_id=member.id
where member.username='test';
```
<img width="141" alt="image" src="https://github.com/Brian-Wang0926/week1/assets/71397277/437aeed5-301a-48d3-9ac6-2445364d8e0e">
