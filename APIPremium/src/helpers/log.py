import logging
import sys
from pathlib import Path

class AppLogger:
    @staticmethod
    def init(log_level: str = "INFO", log_file: str = "app.log") -> None:
        log_level = getattr(logging, log_level.upper(), logging.INFO)
        log_format = "%(asctime)s | %(levelname)s | %(name)s | %(message)s"

        logger = logging.getLogger()
        logger.setLevel(log_level)

        # Evita duplicação de handlers se for reiniciado
        if logger.hasHandlers():
            logger.handlers.clear()

        # Handler para console
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setFormatter(logging.Formatter(log_format))
        logger.addHandler(console_handler)

        # Handler para arquivo
        Path(log_file).parent.mkdir(parents=True, exist_ok=True)
        file_handler = logging.FileHandler(log_file)
        file_handler.setFormatter(logging.Formatter(log_format))
        logger.addHandler(file_handler)