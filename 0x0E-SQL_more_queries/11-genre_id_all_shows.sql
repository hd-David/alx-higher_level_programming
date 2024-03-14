-- Select the title of TV shows and their corresponding genre IDs (or NULL if no genre)
SELECT tv_shows.title, IFNULL(tv_show_genres.genre_id, 'NULL') AS genre_id
-- From the tv_shows table
FROM tv_shows
-- Left join with tv_show_genres to include all shows even if they don't have a genre
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
-- Order the results by title and genre_id in ascending order
ORDER BY tv_shows.title ASC, genre_id ASC;
