-- update value of column everywhere in database, meant to be used as a PK updator
-- stop all checkings
EXEC sp_MSforeachtable @command1="ALTER TABLE ? NOCHECK CONSTRAINT ALL"
GO
EXEC sp_MSforeachtable @command1="ALTER TABLE ? DISABLE TRIGGER ALL"
GO

-- parameters
DECLARE @columnName VARCHAR(MAX) = ''
-- same as `oldValue` and `newValue`
DECLARE @columnType VARCHAR(MAX) = 'VARCHAR(20)'
DECLARE @oldValue VARCHAR(20) = ''
DECLARE @newValue VARCHAR(20) = ''

-- generate update queries for each table that contains the column name
DECLARE @SQL NVARCHAR(MAX) = ''
SELECT @SQL = @SQL + 'UPDATE ' + quotename(object_name(c.object_id)) + ' SET ' + @columnName + ' = @newValue WHERE ' + @columnName + ' = @oldValue;'
FROM sys.columns c
WHERE c.name = @columnName

-- preview queries
SELECT @SQL

-- uncomment and execute after confirm queries are OK
-- NOTE: edit the data type as needed
-- DECLARE @values NVARCHAR(MAX) = '@newValue ' + @columnType + ', @oldValue ' + @columnType
-- EXEC sp_executesql @SQL, @values, @newValue = @newValue, @oldValue = @oldValue

-- restore all checkings
EXEC sp_MSforeachtable @command1="ALTER TABLE ? ENABLE TRIGGER ALL"
GO
EXEC sp_MSforeachtable @command1="ALTER TABLE ? CHECK CONSTRAINT ALL"
GO
