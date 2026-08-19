## SQL 数据查询

查询即检索操作，是对已经存在的基本表及视图进行数据检索，不改变数据本身。数据查询是数据库的核心操作。 SQL 使用 `SELECT` 语句进行数据查询：
```sql
SELECT [DISTINCT | ALL] <select_list>
	FROM <table_references>
	[WHERE <search_condition>]
	[GROUP BY <group_by_list> [HAVING <search_condition>] ]
	[ORDER BY <order_by_list> [DESC] ]
	[LIMIT <limit_lines> [OFFSET <offset_number>] ];
```
`SELECT` 语句具有灵活的使用方式和丰富强大的功能。

### 简单查询

ORDER BY 子句用于对查询结果进行排序，默认按升序排序，可使用 `DESC` 指定降序排序。


### 连接查询


### 嵌套查询

**嵌套查询 (nested query)** 又称为**子查询 (subquery)**，是指在一个 SQL 查询语句中嵌套另一个 SQL 查询语句。嵌套查询通常用于需要多步查询才能得到结果的复杂查询。

> [!example] 简单的嵌套查询示例
> 求选修了《数据库》课程的学生的学号 `sNo` 和姓名 `sName`。
> 
> ```sql
> SELECT sNo, sName FROM S
> WHERE sNo IN (
> 	SELECT sNo FROM SC 
> 	WHERE cNo IN (
> 		SELECT cNo FROM C
> 		WHERE cName = '数据库'
> 	)
> );
> ```
^418cb9

这里，`IN` 谓词将子查询结果视为集合，执行**集合**运算；对子查询结果为单值的情形，也可使用比较运算符执行比较。

#### 相关嵌套查询

[[#^418cb9|上例]]中的子查询与主查询是**独立的**，即子查询的执行不依赖于主查询的处理，称为**不相关子查询 (non-correlated subquery)**。若子查询的执行依赖于主查询，则称为**相关子查询 (correlated subquery)**，整个查询语句称为**相关嵌套查询 (correlated nested query)**。

> [!example] 相关嵌套查询示例
> 查询每个学生**超过该学生自己平均成绩**的课程号 `cNo` 和成绩 `grade`。
> ```sql
> SELECT sNo, cNo, grade FROM SC x
> WHERE grade > (
> 	SELECT AVG(grade) FROM SC y
> 	WHERE x.sNo = y.sNo
> );
> ```

^d930b3

[[#^d930b3|上例]]中的子查询**依赖于主查询中当前处理的学生 `sNo`**，因此每处理一个学生，子查询就会执行一次。

#### 带有量词的嵌套查询

SQL 中可以使用**量词 (quantifier)** 来指定子查询结果与主查询条件的关系，从而允许**子查询返回多个元组**。常用的量词有：
+ **`ANY` (`SOME`)**：表示子查询结果中**至少有一个**值满足主查询条件，相当于在所有返回的元组之间加上逻辑「或」关系。
+ **`ALL`**：表示子查询结果中的**所有**值都满足主查询条件，相当于在所有返回的元组之间加上逻辑「且」关系。
+ **`EXISTS`**：表示子查询**至少返回一个元组**，用于检查子查询的条件是否能够成立。

> [!example] 带有量词 `ANY` 的嵌套查询示例
> 查询非电子系中比电子系某一个学生年龄小的学生学号 `sNo`、姓名 `sName`、年龄 `age`、系别 `sDept`。
> ```sql
> SELECT sNo, sName, age, sDept FROM S
> WHERE age < ANY (
> 	SELECT age FROM S
> 	WHERE sDept = '电子系'
> ) AND sDept <> '电子系';
> ```

> [!example] 带有量词 `ALL` 的嵌套查询示例
> 查询非电子系中比电子系所有学生年龄都小的学生学号 `sNo`、姓名 `sName`、年龄 `age`、系别 `sDept`。
> ```sql
> SELECT sNo, sName, age, sDept FROM S
> WHERE age < ALL (
> 	SELECT age FROM S
> 	WHERE sDept = '电子系'
> ) AND sDept <> '电子系';
> ```

> [!example] 带有量词 `EXISTS` 的嵌套查询示例
> 查询所有选修了《数据库》课程的学生学号 `sNo`、姓名 `sName`。
> ```sql
> SELECT sNo, sName FROM S
> WHERE EXISTS (
> 	SELECT * FROM SC
> 	WHERE S.sNo = SC.sNo AND SC.cNo = (
> 		SELECT cNo FROM C
> 		WHERE cName = '数据库'
> 	)
> );
> ```

一些带 `EXISTS` 或 `NOT EXISTS` 的子查询不能被其他形式的子查询等价替换，但其他形式的子查询通常都可以被等价地转换为带 `EXISTS` 或 `NOT EXISTS` 的子查询。尽管有意义的 `EXISTS` 子查询都是相关子查询，但其**只需返回是否存在元组的信息**，而不需要返回实际的元组数据，因此执行效率可能更高。

### 集合查询

`SELECT` 语句的结果是元组的集合，因此可以对多个 `SELECT` 语句的结果进行集合运算。SQL 支持以下几种集合运算：
+ **并 (UNION)**：返回两个查询结果的并集，结果中不包含重复元组。
+ **交 (INTERSECT)**：返回两个查询结果的交集。
+ **差 (EXCEPT)**：返回第一个查询结果中存在但第二个查询结果中不存在的元组。

参加集合操作的各查询结果必须具有**相同的列数**，且对应列的**数据类型必须兼容**。

### 派生查询

**派生表 (derived table)** 是指使用**子查询生成的临时表**作为 `FROM` 字句的数据源。派生表在查询执行过程中动态创建，并且只在该查询的生命周期内存在。

> [!example] 派生查询示例
> 同[[#^d930b3|相关嵌套查询示例]]，查询每个学生**超过该学生自己平均成绩**的课程号 `cNo` 和成绩 `grade`。
> ```sql
> SELECT sNo, cNo, grade 
> FROM SC, (
> 	SELECT sNo, AVG(grade) FROM SC
> 	GROUP BY sNo
> ) AS Avg_SC(avg_sNo, avg_grade)
> WHERE SC.sNo = Avg_SC.avg_sNo AND SC.grade > Avg_SC.avg_grade;
> ```

这种生成派生表的查询方式，有时可以提高查询效率，因为派生表只需计算一次，而相关子查询则可能需要为每个外层查询元组多次计算。

