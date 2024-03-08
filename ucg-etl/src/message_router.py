from datetime import datetime

from data_processor import (
    process_clicked_event,
    process_film_view_completed_event,
    process_filtered_event,
    process_seen_page_event,
    process_video_quality_event,
)
from src.core.config import settings


class MessageRouter:
    def __init__(self, clickhouse_client):
        self.clickhouse_client = clickhouse_client
        # Словарь для маппинга топиков к функциям обработки и вставки
        self.topic_to_handler = {
            settings.KAFKA_CLICK_TOPIC: (
                process_clicked_event,
                self.clickhouse_client.insert_clicked_event,
            ),
            settings.KAFKA_SEEN_TOPIC: (
                process_seen_page_event,
                self.clickhouse_client.insert_seen_page_event,
            ),
            settings.KAFKA_VIDEO_TOPIC: (
                process_video_quality_event,
                self.clickhouse_client.insert_video_quality_event,
            ),
            settings.KAFKA_FILM_TOPIC: (
                process_film_view_completed_event,
                self.clickhouse_client.insert_film_view_completed_event,
            ),
            settings.KAFKA_FILTER_TOPIC: (
                process_filtered_event,
                self.clickhouse_client.insert_filtered_event,
            ),
        }

    def route_message(self, message, topic_name, msg):
        _, timestamp_ms = msg.timestamp()
        timestamp = datetime.fromtimestamp(
            timestamp_ms / 1000.0
        )  # Преобразуем из миллисекунд в секунды
        if topic_name in self.topic_to_handler:
            process_function, insert_function = self.topic_to_handler[topic_name]
            data = process_function(message, timestamp)
            insert_function(data)
        else:
            print(f"No handler for topic {topic_name}")