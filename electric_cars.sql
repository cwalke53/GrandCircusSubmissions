SELECT * FROM public.ev_cars
ORDER BY carid ASC 

select * from electric_cars

--1)Some of the values for Brand and Model columns have an extra space at the end. Use the TRIM() function to update these values and remove the extra space.

Select TRIM(brand)
from electric_cars
--2) Convert values in the Powertrain column to "AWD", "RWD", or "FWD" using the following mappings:

--All-Wheel Drive → AWD
update electric_cars
set powertrain = 'AWD'
where powertrain = 'All Wheel Drive'

--Rear-Wheel Drive → RWD
update electric_cars
set powertrain = 'RWD'
where powertrain = 'Rear Wheel Drive'

--Front-Wheel Drive → FWD
update electric_cars
set powertrain = 'FWD'
where powertrain = 'Front Wheel Drive'

--3)Display current values of "TopSpeed" column.
select topspeed from electric_cars

--4) Add a TopSpeedKPH column: ALTER TABLE electric_cars ADD COLUMN "TopSpeedKPH" INT;
ALTER TABLE electric_cars ADD COLUMN "TopSpeedKPH" INT;

--5) Update this new column with cleaned values from "TopSpeed". Remove the km/h suffix and cast to INT. (Hint: You'll probably need to do some research on this one.)
ALTER TABLE electric_cars
ALTER COLUMN "TopSpeedKPH" TYPE integer
USING "TopSpeedKPH"::integer;

UPDATE electric_cars
SET "TopSpeedKPH" = REPLACE("TopSpeedKPH", ' km/h', '')::integer;

--6) With the newly cleaned data, write a GROUP BY query to show the count of cars and the average TopSpeedKPH for each PowerTrain category.
select count(*), avg("TopSpeedKPH"), powertrain
from electric_cars
group by powertrain
order by powertrain

--7) Write a query that retrieves the Models of cars where the TopSpeedKPH is above the average top speed across all cars.
--Use a subquery to calculate the average. (Hint: Expect 46 results.)

 select brand, model, avg("TopSpeedKPH") 
 from electric_cars
 where "TopSpeedKPH" > (
select avg("TopSpeedKPH") from electric_cars
 )
 group by brand, model

 --8) Find car Models where the sales price is higher than the average for their Brand. 
 --Use a correlated subquery to group by Brand and compare within each brand. (Hint: Expect 40 results.)
 
 model sales price > avg sales price for brand
select brand, model, priceeuro
from electric_cars ev1
where priceeuro > (
select avg(priceeuro) 
from electric_cars ev2
where ev1.brand = ev2.brand
) 
order by brand

--9) Use a CTE to break down a query into parts:
--First create a CTE named "PriceByBrand" that calculates the average car price per brand. Order the results with the most expensive average first.
--Then use that CTE to find the brands with average price exceeding a threshold 80,000 Euros. (Hint: Expect 5 results.)

with pricebybrand as (
select brand, avg(priceeuro) as avg_price
from electric_cars 
group by brand 
order by avg_price desc
)

select avg_price
from pricebybrand
where avg_price > 80000

--10) Create two additional tables: features and car_features to store this relationship. 
--The features table will store a list of all available features, and the car_features table 
--will record which cars have which features. Add several rows to the feature table, such as 
--"Autonomous Driving", "Adaptive Cruise Control", "Parking Assist", "Head-up display". 
--Then add some rows to the car_features table; you can arbitrarily assign features to cars.

CREATE TABLE features (
    feature_id SERIAL PRIMARY KEY,
    feature_name VARCHAR(100) NOT NULL UNIQUE
);
INSERT INTO features (feature_name) VALUES
('Autonomous Driving'),
('Adaptive Cruise Control'),
('Parking Assist'),
('Head-up Display'),
('Heated Seats'),
('Sunroof'),
('Bluetooth Connectivity'),
('Lane Departure Warning'),
('Blind Spot Monitoring'),
('360-Degree Camera')

--11) Write a query using the new tables to find all cars that have a specific 
--feature (e.g., "Autonomous Driving"):

select * 
from features 
where feature_name = 'Autonomous Driving'








