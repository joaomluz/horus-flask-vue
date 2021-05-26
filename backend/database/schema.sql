drop table if exists contacts;

create table contacts (
  id integer primary key autoincrement,
  contact_name text not null,
  contact_phone text not null,
  deleted boolean not null default 1
);