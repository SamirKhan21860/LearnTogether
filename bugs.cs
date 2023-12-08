// bugs I have came across while building this web app
1. The problem is that the student variable, which is supposed 
to contain the newly inserted student's data, is assigned the 
result of the SELECT query before the student is inserted. As 
a result, session["user_id"] is assigned None.