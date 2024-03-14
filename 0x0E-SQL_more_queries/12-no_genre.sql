-- Select the title of TV shows and their corresponding genre IDs
SELECT tv_shows.title, tv_show_genres.genre_id
-- From the tv_shows table
FROM tv_shows
-- Left join with tv_show_genres to include all shows even if they don't have a genre
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
-- Filter out rows where genre_id is NULL (shows without a genre linked)
WHERE tv_show_genres.genre_id IS NULL
-- Order the results by title in ascending order
ORDER BY tv_shows.title ASC;
