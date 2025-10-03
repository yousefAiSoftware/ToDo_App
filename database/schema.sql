create database if not exists todo_app
	character set utf8mb4
    collate utf8mb4_0900_ai_ci;
use todo_app;
create table if not exists users(
	id int auto_increment primary key,
    username varchar (100) not null unique,
    password_hash varchar(255) not null,
    created_at timestamp default current_timestamp
);

create table if not exists tasks(
	id int auto_increment primary key,
    user_id int not null,
    title varchar (255) not null,
    task_description varchar (500) null,
    start_task_time timestamp null,
    duration time null,
    due_date timestamp null,
    is_completed boolean default false,
    created_at timestamp default current_timestamp,
    priority enum("Important AND Urgent", "Important AND Not Urgent", "Not Important AND Urgent", "Not Important AND Not Urgent") not null default "Important AND Not Urgent",
    foreign key (user_id) references users(id)
);





