-- stop all checkings
EXEC sp_MSforeachtable @command1="ALTER TABLE ? NOCHECK CONSTRAINT ALL"
GO
EXEC sp_MSforeachtable @command1="ALTER TABLE ? DISABLE TRIGGER ALL"
GO

-- parameters
DECLARE @columnName VARCHAR(MAX) = ''
DECLARE @oldValue VARCHAR(MAX) = ''
DECLARE @newValue VARCHAR(MAX) = ''

-- generate update queries for each table that contains the column name
DECLARE @SQL NVARCHAR(MAX) = ''
SELECT @SQL = @SQL + 'UPDATE ' + quotename(object_name(c.object_id)) + ' SET ' + @columnName + ' = @newValue WHERE ' + @columnName + ' = @oldValue;'
FROM sys.columns c
WHERE c.name = @columnName

-- preview queries
SELECT @SQL

-- uncomment and execute after confirm queries are OK
--EXEC sp_executesql @SQL, N'@newValue varchar(10), @oldValue varchar(10)', @newValue = @newValue, @oldValue = @oldValue

-- restore all checkings
EXEC sp_MSforeachtable @command1="ALTER TABLE ? ENABLE TRIGGER ALL"
GO
EXEC sp_MSforeachtable @command1="ALTER TABLE ? CHECK CONSTRAINT ALL"
GO
