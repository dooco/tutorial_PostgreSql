from sqlalchemy import (
    create_engine, Table, Column, Float, ForeignKey, Integer, String, MetaData
)

# executing the instruction from our localhost "chinool" db
db = create_engine("postgresql:///chinook")

meta = MetaData(db)

# create variable for "Artist"
artist_table = Table(
    "Artist", meta,
    Column("ArtistId", Integer, primary_key=True),
    Column("Name", String)
)

album_table = Table(
    "Album", meta,
    Column("AlbumId", Integer, primary_key=True),
    Column("Title", String),
    Column("ArtistId", Integer, ForeignKey("artist_table.ArtistId"))
)

track_table = Table(
    "Track", meta,
    Column("TrackId", Integer, primary_key=True),
    Column("Name", String),
    Column("AlbumId", Integer, ForeignKey("album_table.AlbumId")),
    Column("MediaTypeId", Integer, primary_key=False),
    Column("GenreId", Integer, primary_key=False),
    Column("Composer", String),
    Column("Milliseconds", Integer),
    Column("Bytes", Integer),
    Column("UnitPrice", Float)
)

# makig the connection
with db.connect() as connection:

    
    
    # select_query = artist_table.select()

    # Query 2 select only "Name" column from "Artist" table
    # select_query = artist_table.select().with_only_columns([artist_table.c.Name])

    # Query 3 select only 'Queen' column from "Artist" Table
    # select_query = artist_table.select().where(artist_table.c.Name == "Queen")

    # Query 4 select only 'ArtistId' #51 from "Artist" Table
    # select_query = artist_table.select().where(artist_table.c.ArtistId == 51)

    # Query 5 select only albums with 'ArtistID' from "Album" Table
    select_query = album_table.select().where(album_table.c.ArtistId == 51)

    # Query 6 select only track with Composer is Queen from "Album" Table
    select_query = track_table.select().where(track_table.c.Composer == "Queen")

    results = connection.execute(select_query)
    for result in results:
        print(result)