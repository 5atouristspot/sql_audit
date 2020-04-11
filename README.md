tf_sql_audit接口文档
===

>>返回字段含义
```
        "execute_time":"执行时间",
        "errormessage":"错误信息",
        "sequence":"'此次执行事务中sql序号'",
        "stagestatus":"此阶段状态",
        "ID":ID,
        "Affected_rows":"影响行数",
        "SQL":"SQL",
        "backup_dbname":"回滚语句所在库名",
        "sqlsha1":"sqlsha1",
        "errlevel":"错误等级",
        "stage":"阶段名称"
        errlevel为0,表示执行成功,除此之外都为失败;
        errormessage为报错信息
```

>审核接口
>>接口例子

```
curl -i -X GET http://192.168.74.95:3621/api/v1000/audit/alter?sql_statment=alter+TABLE+user_dept_relation+add+content_html13+longtext+COMMENT+%27H5%27%3B\&port=4450\&database=inception_test
```

>>成功执行返回json

```
[
    {
        "execute_time":"0",
        "errormessage":"None",
        "sequence":"'0_0_0'",
        "stagestatus":"Audit completed",
        "ID":1,
        "Affected_rows":0,
        "SQL":"use inception_test",
        "backup_dbname":"None",
        "sqlsha1":"",
        "errlevel":0,
        "stage":"CHECKED"
    },
    {
        "execute_time":"0",
        "errormessage":"None",
        "sequence":"'0_0_1'",
        "stagestatus":"Audit completed",
        "ID":2,
        "Affected_rows":2298233,
        "SQL":"alter TABLE user_dept_relation add content_html12 longtext COMMENT 'H5'",
        "backup_dbname":"10_20_4_44_4450_inception_test",
        "sqlsha1":"*911F0695FF2A3A9BEC077B1E6D91A1FFC13D14BD",
        "errlevel":0,
        "stage":"CHECKED"
    }
]
```

>执行接口
>>接口例子

```
curl -i -X GET http://192.168.74.95:3621/api/v1000/execute/alter?sql_statment=alter+TABLE+user_dept_relation+add+content_html13+longtext+COMMENT+%27H5%27%3B\&port=4450\&database=inception_test
```

>>成功执行返回例子

```
[
    {
        "execute_time":"0.000",
        "errormessage":"None",
        "sequence":"'1563861707_758021_0'",
        "stagestatus":"Execute Successfully",
        "ID":1,
        "Affected_rows":0,
        "SQL":"use inception_test",
        "backup_dbname":"None",
        "sqlsha1":"",
        "errlevel":0,
        "stage":"RERUN"
    },
    {
        "execute_time":"103.890",
        "errormessage":"None",
        "sequence":"'1563861811_758021_1'",
        "stagestatus":"Execute Successfully
Backup successfully",
        "ID":2,
        "Affected_rows":1,
        "SQL":"alter TABLE user_dept_relation add content_html13 longtext COMMENT 'H5'",
        "backup_dbname":"10_20_4_44_4450_inception_test",
        "sqlsha1":"*8262B258588A8D8536821B0D74DB0FCE95BA7403",
        "errlevel":0,
        "stage":"EXECUTED"
    }
]
```


