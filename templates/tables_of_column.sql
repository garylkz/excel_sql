DECLARE @columnName NVARCHAR(MAX) = '';

SELECT (SCHEMA_NAME(t.schema_id) + '.' + t.name) AS 'Table'
FROM sys.columns c
JOIN sys.tables t ON c.object_id = t.object_id
WHERE c.name LIKE '%' + @columnName + '%'
ORDER BY [Table];
