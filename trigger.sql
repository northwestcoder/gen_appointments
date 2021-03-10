DELIMITER $$
CREATE TRIGGER before_booking_update
BEFORE UPDATE
ON Bookings FOR EACH ROW
BEGIN
    DECLARE errorMessage VARCHAR(255);
    SET errorMessage = 'SOMEONE SLIPPED IN BEFORE YOU! APPOINTMENT NOT BOOKED! CLICK CANCEL AND CHOOSE `RESET CHANGES` FROM UPPER LEFT MENU!';                 
    IF new.CompositeKey in (select CompositeKey from RaceConditions.Bookings) THEN
        SIGNAL SQLSTATE '45000' 
            SET MESSAGE_TEXT = errorMessage;
    END IF;
END $$
DELIMITER ;
