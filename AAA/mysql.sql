select a.s_id as s_id,score1,score2 from (select s_id,score as score1
from score where c_id="01") a inner join (select s_id,score as score2 from
score where c_id="02") b on a.s_id = b.s_id where score1>score2

查询01课程的成绩分数和学生信息
select s_id,score from score where c_id = "01"
查询02课程的成绩分数和学生信息
select s_id,score from score where c_id = "02"