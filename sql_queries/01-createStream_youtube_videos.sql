CREATE STREAM youtube_videos (
  video_id VARCHAR KEY,
  title VARCHAR,
  views INTEGER,
  comments INTEGER,
  likes INTEGER
) WITH (
  KAFKA_TOPIC = 'youtube_videos',
  PARTITIONS = 1,
  VALUE_FORMAT = 'avro'
);