INSERT INTO telegram_outbox
SELECT
  '<your chat id>' AS `chat_id`,
  CONCAT(
    'Comments changed: ',
    CAST(comments_previous AS STRING),
    ' => ',
    CAST(comments_current AS STRING),
    '. ',
    title
  ) AS `text`
FROM youtube_changes_stream
WHERE comments_current <> likes_previous;