use test;
select * from user;
truncate table user;# 删除表全部数据，保留表结构，立刻释放磁盘空间 ，不管是 Innodb 和 MyISAM;
delete from user where id = 12;
select * from user;
#新建table user
CREATE TABLE user(
   id int not null primary key auto_increment,
   username char(20) not null,
   password char(20) not null,
   depart char(20) not null,
   photo char(20) not null

);

select count(*) from user;#获取数据个数