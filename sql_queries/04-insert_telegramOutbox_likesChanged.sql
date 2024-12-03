INSERT INTO telegram_outbox
SELECT
  '<your chat id>' AS `chat_id`,
  CONCAT(
    'Likes changed: ',
    CAST(likes_previous AS STRING),
    ' => ',
    CAST(likes_current AS STRING),
    '. ',
    title
  ) AS `text`
FROM youtube_changes_stream
WHERE likes_current <> likes_previous;