create database [Ramen_Database]
go
use [Ramen_Database]
go

create table [dbo].[Admin]
(
	[ID_Admin] [int] not null identity(1,1),
	[FirstName_Admin] [varchar] (100) not null,
	[SecondName_Admin] [varchar] (100) not null,
	[MiddleName_Admin] [varchar] (100) null,
	[Balance_Admin] [float] null,
	[Login_Admin] [varchar] (100) not null,
	[Password_Admin] [varchar] (100) not null,
	constraint [PK_ID_Admin] primary key clustered 
		([ID_Admin] ASC) on [PRIMARY],
		constraint [UQ_Login_Admin] unique ([Login_Admin]),
		constraint [CH_Login_Admin] check (len([Login_Admin]) >= 7),
		constraint [CH_Password_Admin] check (len([Password_Admin]) >= 7)
)
delete from [Admin] where [ID_Admin] = 1

INSERT INTO [Admin] ([FirstName_Admin],[SecondName_Admin],[MiddleName_Admin],[Balance_Admin],[Login_Admin],[Password_Admin])   
VALUES ('Иванов', 'Иван','Иванович', '10000','Ivan0vIvan','Pa$$w0rd!!!'),
('Бензенко', 'Анастасия','Павловна', '10000','stellarul1t','Pa$$w0rdmy%')

select * from [Admin]

create table [dbo].[Users]
(
	[ID_Users] [int] not null identity(1,1),
	[Name_Users] [varchar] (100) not null,
	[Balance_Users] [float] null,
	[Phone_Users]  [varchar](17) not null,
	[Loyalty_Card_Users] [int] null,
	[Login_Users] [varchar] (100) not null,
	[Password_Users][varchar] (100) not null,
	constraint [PK_ID_Users] primary key clustered 
		([ID_Users] ASC) on [PRIMARY],
		constraint [UQ_Phone_Users] unique ([Phone_Users]),
		constraint [CH_Phone_Users] check ([Phone_Users] like ('+7([0-9][0-9][0-9])[0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9]')),
		constraint [UQ_Login_Users] unique ([Login_Users]),
		constraint [CH_Login_Users] check (len([Login_Users]) >= 7),
		constraint [CH_Password_Users] check (len([Password_Users]) >= 7)
)
select * from users

create table [dbo].[Dish]
(
	[ID_Dish] [int] not null identity(1,1),
	[Meat_Dish] [varchar] (8) null,
	[Bouillon_Dish] [varchar] (7) not null,
	[Noodles_Dish] [varchar] (9) not null,
	[Egg_Dish] [varchar] (9) null,
	[Carrot_Dish] [varchar] (7) null,
	[Cucumber_Dish] [varchar] (12) null,
	[Potato_Dish] [varchar] (17) null,
	constraint [PK_ID_Dish] primary key clustered 
		([ID_Dish] ASC) on [PRIMARY],
		constraint [CH_Meat_Dish] check ([Meat_Dish] in ('Говядина','Курица', 'Свинина')),
		constraint [CH_Bouillon_Dish] check ([Bouillon_Dish] in ('Говяжий','Куриный')),
		constraint [CH_Noodles_Dish] check ([Noodles_Dish] in ('Рисовая','Гречневая', 'Яичная')),
		constraint [CH_Egg_Dish] check ([Egg_Dish] in ('Сырое','Всмятку', 'В мешочек')),
		constraint [CH_Carrot_Dish] check ([Carrot_Dish] in ('Вареная','Свежая')),
		constraint [CH_Cucumber_Dish] check ([Cucumber_Dish] in ('Свежий','Маринованный')),
		constraint [CH_Potato_Dish] check ([Potato_Dish] in ('Сладкий картофель','Русский картофель'))
)

INSERT INTO [Dish] ([Meat_Dish],[Bouillon_Dish],[Noodles_Dish],[Carrot_Dish],[Cucumber_Dish])   
VALUES ('Говядина', 'Куриный','Гречневая','Свежая','Маринованный')

select * from [dbo].[Dish]

delete from [dbo].[Dish]

create table [dbo].[Order]
(
	[ID_Order] [int] not null identity(1,1),
	[Data_Order] [datetime] not null,
	[Users_ID] [int] not null,
	[Dish_ID] [int] not null
	constraint [PK_ID_Order] primary key clustered 
		([ID_Order] ASC) on [PRIMARY],
		constraint [FK_User_Order] foreign key ([Users_ID])
		references [dbo].[Users] ([ID_Users]),
		constraint [FK_Dish_Order] foreign key ([Dish_ID])
		references [dbo].[Dish] ([ID_Dish])
)

INSERT INTO [Order] ([Data_Order],[Users_ID],[Dish_ID])   
VALUES ('2023-03-10 13:58:32', 5,13)
INSERT INTO [Order] ([Data_Order],[Users_ID],[Dish_ID])   
VALUES (getdate(), 5,1)

delete  from [Order]

select [Data_Order] , [Phone_Users],[Name_Users],[Meat_Dish],[Bouillon_Dish],[Noodles_Dish],[Egg_Dish],[Carrot_Dish],[Cucumber_Dish],[Potato_Dish]  from [dbo].[Order]
inner join [dbo].[Users] on [Users_ID] = [ID_Users]
inner join [dbo].[Dish] on [Dish_ID] = [ID_Dish]
where [Phone_Users]='+7(925)888-88-88'
order by [Data_Order] ASC
go

create table [dbo].[Price_Quantity]
(
	[ID_Price_Quantity] [int] not null identity(1,1),
	[Total_Price] [float] null,
	[Meat_Price] [float] not null,
	[Meat_Quantity] [int] null,
	[Bouillon_Price]  [float] not null,
	[Bouillon_Quantity] [int] null,
	[Noodles_Price] [float] not null,
	[Noodles_Quantity] [int] null,
	[Egg_Price] [float] not null,
	[Egg_Quantity] [int] null,
	[Carrot_Price] [float] not null,
	[Carrot_Quantity] [int] null,
	[Cucumber_Price] [float] not null,
	[Cucumber_Quantity] [int] null,
	[Potato_Price] [float] not null,
	[Potato_Quantity] [int] null,
	constraint [PK_ID_Price_Quantity] primary key clustered 
		([ID_Price_Quantity] ASC) on [PRIMARY]
		
)

INSERT INTO [Price_Quantity] ([Total_Price],[Meat_Price],[Meat_Quantity],[Bouillon_Price],[Bouillon_Quantity],[Noodles_Price],[Noodles_Quantity],[Egg_Price],[Egg_Quantity],
[Carrot_Price],[Carrot_Quantity],[Cucumber_Price],[Cucumber_Quantity],[Potato_Price],[Potato_Quantity])   
VALUES ('345','100','500','50','500','100','1000','30','1000','20','1000','20','1000','25','1000')

SELECT [Meat_Quantity],[Bouillon_Quantity],[Noodles_Quantity],[Egg_Quantity],[Carrot_Quantity],[Cucumber_Quantity],[Potato_Quantity] FROM [Price_Quantity]
SELECT [Total_Price] FROM [Price_Quantity]


INSERT INTO [Order] ([Data_Order],[Users_ID],[Dish_ID]) VALUES (getdate(), 5,13)

select * from [Order]

UPDATE [Users] SET [Balance_Users]=[Balance_Users]-[Price_Quantity].[Total_Price]

UPDATE [Users] SET [Loyalty_Card_Users]=+1 where [Phone_Users] = '+7(925)888-88-88'

create table [dbo].[Toppings]
(
	[ID_Toppings] [int] not null identity(1,1),
	[SoySprouts_Toppings] [varchar] (3)  null,
	[Cheese_Toppings] [varchar] (3) null,
	[Narutomaki_Toppings] [varchar] (3)  null,
	constraint [PK_ID_Toppings] primary key clustered 
		([ID_Toppings] ASC) on [PRIMARY],
		constraint [CH_SoySprouts_Toppings] check ([SoySprouts_Toppings] in ('Да','Нет')),
		constraint [CH_Cheese_Toppings] check ([Cheese_Toppings] in ('Да','Нет')),
		constraint [CH_Narutomaki_Toppings] check ([Narutomaki_Toppings] in ('Да','Нет'))
)

UPDATE [Price_Quantity] SET [Bouillon_Quantity]=[Bouillon_Quantity]-1[Meat_Quantity] = [Bouillon_Quantity]- 1