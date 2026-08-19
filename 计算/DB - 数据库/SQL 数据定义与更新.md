## SQL 数据定义

### 模式的定义与删除

#### 定义模式

SQL 使用 `CREATE SCHEMA` 语句定义模式：
```sql
CREATE SCHEMA [<schema_name>] AUTHORIZATION <owner_name>;
```
其中，**`<schema_name>`** 是**模式名**，**`<owner_name>`** 是该模式所有者的**用户名**；如果省略 `<schema_name>`，则创建一个以所有者用户名命名的模式。

可以在定义模式的同时在该模式下[[#定义基本表]]、视图、索引等，如
```sql
CREATE SCHEMA [<schema_name>] AUTHORIZATION <owner_name>
	CREATE TABLE <table_name> (<table_definition>);
```
注意此处**模式定义末尾没有分号**；这等价于
```sql
CREATE SCHEMA [<schema_name>] AUTHORIZATION <owner_name>;
CREATE TABLE <schema_name>.<table_name> (<table_definition>);
```

#### 删除模式

使用 `DROP SCHEMA` 语句删除模式：
```sql
DROP SCHEMA <schema_name> [CASCADE | RESTRICT];
```
其中，`<schema_name>` 是要删除的模式名；**`CASCADE`** 和 **`RESTRICT`** 是两种删除模式的方式：
+ **`CASCADE` 级联删除**：删除模式时，同时删除该模式下的所有数据库对象（如表、视图、索引等）。
+ **`RESTRICT` 限制删除**：如果该模式下存在任何数据库对象，则拒绝删除该模式，只有先将模式下数据库对象删空后才能删除该模式。

### 基本表的定义、删除与修改

#### 定义基本表

使用 `CREATE TABLE` 语句定义基本表：
```sql
CREATE TABLE [<schema_name>.]<table_name> (
	<column_definition>[, <table_constraint>]
);
```
其中，
+ `<schema_name>` 是模式名，`<table_name>` 是表名；
+ **列定义 `<column_definition>`** 列出表的每个属性（列）的名称、数据类型及可选约束，每项格式为 
	```sql
	<column_name> <data_type> [<column_constraint>]
	```
	其中，`<column_name>` 是列名，`<data_type>` 是[[#^9a9ecc|数据类型]]，`<column_constraint>` 是列级完整性约束条件，包括：
	+ `NULL` 或 **`NOT NULL`**：指定该列是否允许存储空值；
	+ **`DEFAULT <default_value>`**：指定该列的默认值；
	+ `UNIQUE`：指定该列的值必须唯一；
	+ **`PRIMARY KEY`**：指定该列为**主键**，主键列的值必须唯一且不能为空；
	+ `CHECK (<search_condition>)`：指定该列的值必须满足的条件。
+ **表约束 `<table_constraint>`** 定义表级的完整性约束条件，包括：
	+ **`PRIMARY KEY (<column_list>)`**：指定多个列联合作为表的主键；
	+ `UNIQUE (<column_list>)`：指定多个列的值组合必须唯一；
	+ `FOREIGN KEY <column_list> REFERENCES [<ref_schema_name>.]<ref_table_name> [(<ref_column_list>)]`：指定一个或多个列作为外键，引用另一个表的主键或唯一键；
	+ `CHECK (<search_condition>)`：指定表中数据必须满足的条件。

SQL 支持的数据类型包括：
```tx
| 数据类型 || 说明 |
| :--- | :--- | :--- |
| 字符串 | `CHAR(n)` | 定长字符串，长度为 n 个字符 |
| ^^     | `VARCHAR(n)` | 变长字符串，最大长度为 n 个字符 |
| ^^     | `CLOB` | 大型字符对象，存储大量文本数据 |
| ^^     | `TEXT` | 可变长度字符串，适用于存储较长文本 |
| 二进制 | `BOOLEAN` 或 `BOOL` | 布尔值，取值为 TRUE 或 FALSE |
| ^^     | `BLOB` | 大型二进制对象，存储大量二进制数据 |
| 整型数 | `INTEGER` 或 `INT` | 4 字节整数 |
| ^^     | `SMALLINT` | 2 字节整数 |
| ^^     | `BIGINT` | 8 字节整数 |
| 浮点数 | `REAL` | 单精度浮点数 |
| ^^     | `DOUBLE PRECISION` | 双精度浮点数 |
| ^^     | `FLOAT(n)` | 精度为 n 位的浮点数 |
| ^^     | `DECIMAL(p, d)` | 定点数，p 为总位数，d 为小数位数 |\
|      | 或 `DEC(p, d)` |  |\
|      | 或 `NUMBER(p, d)` |  |
| 日期时间 | `DATE` | 日期，包括年、月、日，格式为 `YYYY-MM-DD` |
| ^^     | `TIME` | 时间，包括时、分、秒，格式为 `HH:MM:SS` |
| ^^     | `DATETIME` | 日期和时间的组合 |
| ^^     | `TIMESTAMP` | 时间戳，包含日期和时间，精确到秒或更高精度 |
| ^^     | `INTERVAL` | 时间间隔，用于表示两个时间点之间的差值 |
```
^9a9ecc

> [!example] 基本表定义示例
> 综合考虑数据库完整性，生成**学生选课数据库**的学生基本表 `S`、课程基本表 `C` 和选课基本表 `SC`。
> ```sql
> CREATE TABLE S (
> 	sNo CHAR(10) PRIMARY KEY,
> 	sName VARCHAR(50) NOT NULL,
> 	age SMALLINT NOT NULL CHECK (age >= 0),
> 	sex CHAR(1) NOT NULL CHECK (sex IN ('M', 'F')),
> 	sDept VARCHAR(50) NOT NULL
> );
> CREATE TABLE C (
> 	cNo CHAR(10) PRIMARY KEY,
> 	cName VARCHAR(100) NOT NULL,
> 	cPreNo CHAR(10) NULL, -- 允许为空，表示无先修课程
> 	FOREIGN KEY (cPreNo) REFERENCES C(cNo)
> );
> CREATE TABLE SC (
> 	sNo CHAR(10) NOT NULL,
> 	cNo CHAR(10) NOT NULL,
> 	grade DECIMAL(4,3) CHECK (grade >= 0 AND grade <= 4),
> 	PRIMARY KEY (sNo, cNo), -- 复合主键
> 	FOREIGN KEY (sNo) REFERENCES S(sNo),
> 	FOREIGN KEY (cNo) REFERENCES C(cNo)
> );
> ```

#### 修改基本表

#### 删除基本表

### 索引的建立、删除与更新

#### 建立索引

#### 更新索引

#### 删除索引

## SQL 数据更新

### 数据插入

使用 `INSERT INTO` 语句向基本表中插入一个元组，基本语法为
```sql
INSERT INTO [<schema_name>.]<table_name> [(<column_list>)]
	VALUES (<value_list>);
```
其中，
+ `<schema_name>` 是模式名，`<table_name>` 是表名；
+ `<column_list>` 是可选的列名列表，指定要插入值的列，若省略则表示为表的所有列；
+ `<value_list>` 是**与 `<column_list>` 中列对应**的值列表。

也可使用 `INSERT INTO ... SELECT` 语句从另一个表中插入多个元组，基本语法为
```sql
INSERT INTO [<schema_name>.]<table_name> [(<column_list>)]
	<select_query>;
```
其中，`<select_query>` 是一个 `SELECT` 查询语句，其结果集中的每个元组将被插入到指定的表中。

### 数据更新

使用 `UPDATE` 语句修改基本表中的数据，基本语法为
```sql
UPDATE [<schema_name>.]<table_name>
	SET <column_name> = <new_value> [, <column_name> = <new_value> ...]
	[WHERE <search_condition>];
```
其中，
+ `<schema_name>` 是模式名，`<table_name>` 是表名；
+ `<column_name>` 是要更新的列名，`<new_value>` 是该列的新值；
+ `<search_condition>` 是可选的搜索条件，指定要更新的元组范围，若省略则表示更新表中的所有元组。

### 数据删除

使用 `DELETE FROM` 语句删除基本表中的数据，基本语法为
```sql
DELETE FROM [<schema_name>.]<table_name>
	[WHERE <search_condition>];
```
其中，
+ `<schema_name>` 是模式名，`<table_name>` 是表名；
+ `<search_condition>` 是可选的搜索条件，指定要删除的元组范围，若省略则表示删除表中的所有元组。

