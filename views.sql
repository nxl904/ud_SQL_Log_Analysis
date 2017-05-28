
create view authart as select articles.title, authors.name, articles.slug from  articles, authors where articles.author = authors.id ;
create view logsubstr as  select "substring"(log.path, 10, 30) AS "substring" from log;
create view logauthart as select authart.title, authart.name, logsubstr."substring" from authart join logsubstr on authart.slug = logsubstr."substring";
create view titlecount as select logauthart.title, count(logauthart.title) as count from logauthart group by logauthart.title;
create view time2text as select log.path, log.ip, log.method, log.status, log."time", log.id, to_char(log."time", 'YYYY-MM-DD HH:MI:SS:MS'::text) AS to_char from log;
create view time2textss as select time2text.path, time2text.ip, time2text.method, time2text.status, time2text."time", time2text.id, time2text.to_char, "substring"(time2text.to_char, 0, 11) AS "substring" from time2text;
create view error as select time2textss."substring", count(time2textss."substring") as count from time2textss where time2textss.status <> '200 OK'::text group by time2textss."substring" order by  (count(time2textss."substring")) desc;
create view ok as select time2textss."substring", count(time2textss."substring") as count from time2textss where time2textss.status = '200 OK'::text group by time2textss."substring" order by (count(time2textss."substring")) desc;
create view errorok as select ok."substring" as date, error.count as error_count, ok.count as ok_count from ok join error on ok."substring" = error."substring";

