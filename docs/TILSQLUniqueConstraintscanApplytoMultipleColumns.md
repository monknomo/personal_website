Title: TIL SQL Unique Constraints can Apply to Multiple Columns
Slug: til-sql-unique-constraints-are-multi-column
Date: 6/30/2016 0830
Modified: 6/30/2016 0830
Category: TIL
Tags: til,sql, oracle, embarrassing
Authors: Gunnar Gissel
Summary: SQL unique constraints can apply to multiple columns.... duh!


This is a little embarrassing, considering how long I've been working with SQL, but it's important to never stop learning.


Apparently, you can have a unique constraint that encompasses multiple columns.  This is super useful!


I had a problem at work where I have two tables, a parent table


    PARENT
    --------------
    ID


And a child table


    CHILD
    -------------
    ID
    PARENT_ID
    NAME


I wanted to have each parent have children with unique names.  Children don't need to have unique names - you might have a classroom full of Aidens, but every family only has one Aiden.  I totally blanked on how to do this.  I thought I probably had to craft a check constraint with a query that looked up the parent, but [Stack Overflow to the rescue](https://stackoverflow.com/questions/38128466/crafting-a-check-constraint-that-depends-on-another-table/38128515#38128515)


You can just make a unique constraint that covers PARENT_ID and NAME _at the same time_


`ALTER TABLE child ADD CONSTRAINT multi_unique UNIQUE (parent_id, name)`


This probably saved future me from a real pain in the ass - I was worried I'd have to enforce this solely with business rules in the middle tier.