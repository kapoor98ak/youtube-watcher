-- A views notification would be too chatty. Only send an alert if we
--  pass through a multiple of 1000 views.
INSERT INTO telegram_outbox
SELECT
  '<your chat id>' AS `chat_id`,
  CONCAT(
    'Views changed: ',
    CAST(views_previous AS STRING),
    ' => ',
    CAST(views_current AS STRING),
    '. ',
    title
  ) AS `text`
FROM youtube_changes_stream
WHERE
  round(views_current / 1000) * 1000
  <>
  round(views_previous / 1000) * 1000
  ;