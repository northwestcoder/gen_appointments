CREATE VIEW `available_times` AS 

select 
`Datetime`.`Key` AS `Key`,
`Datetime`.`Date` AS `Date`,
`Datetime`.`Name` AS `Name`,
`Datetime`.`Times` AS `Times` 
from 
`Datetime` 
where (not(`Datetime`.`Key` in (select `Bookings`.`TimeKey` from `Bookings`)));