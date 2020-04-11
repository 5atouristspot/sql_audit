>解压
```
tar zxvf SQLaudit.tar.gz
```
>修改sql_parse.cc
```
vim /SQLaudit/sql/sql_parse.cc
```
>>修改函数　mysql_get_remote_variables,添加
```
sprintf(set_format,"set session wait_timeout=3600;");
if (mysql_real_query(mysql, set_format, strlen(set_format)))
{
my_message(mysql_errno(mysql), mysql_error(mysql), MYF(0));
DBUG_RETURN(ER_NO);
}
```
>>延长超时时间,避免改表时间过长造成的`Execute: Got an error reading communication packets.`错误

>编译
```
rm -rf CMakeCache.txt
cmake -DWITH_DEBUG=OFF -DCMAKE_INSTALL_PREFIX=./mysql  -DMYSQL_DATADIR=./mysql/data -DWITH_SSL=bundled -DCMAKE_BUILD_TYPE=RELEASE -DWITH_ZLIB=bundled-DMY_MAINTAINER_CXX_WARNINGS="-Wall -Wextra -Wunused -Wno-dev -Wwrite-strings -Wno-strict-aliasing  -Wno-unused-parameter -Woverloaded-virtual" -DMY_MAINTAINER_C_WARNINGS="-Wall -Wextra -Wno-dev -Wunused -Wwrite-strings -Wno-strict-aliasing -Wdeclaration-after-statement"
make
make install
```

>启动
```
cd SQLaudit && nohup ./mysql/bin/Inception --defaults-file=inc.cnf &
```