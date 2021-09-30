create table ユーザ(
	ユーザーコード varchar(50) primary key,
	ニックネーム varchar(50) not null,
	メールアドレス varchar(50) not null,
	名前 varchar(50) not null,
	性別 int,
	ポジション bit,
	パスワード varchar(50)
)
create table スキン(
	スキンのコード varchar(50) primary key not null,
	到達するラップ数 int not null,
)

create table マッチ(
	マッチコード varchar(50) primary key,
	ユーザーコード varchar(50) not null,
	スキンのコード varchar(50) not null,
	始まる時間 datetime,
	終了時間 datetime,
	スコア int
	constraint FK_ユーザーコード foreign key (ユーザーコード) references ユーザ(ユーザーコード),
	constraint FK_スキンのコード foreign key (スキンのコード) references スキン(スキンのコード)
)

create table スキル(
	スキルコード varchar(50) primary key,
	クールダウン時間 int
)

