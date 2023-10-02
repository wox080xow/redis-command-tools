
import sys
import logging
import traceback
from argparse import ArgumentParser
from typing import Any

from django.core.management.base import BaseCommand
from say_hello.workers import Hello

logger = logging.getLogger(__name__)
class Command(BaseCommand):
    help = "Say Hello to Everyone"
    def add_arguments(self, parser: ArgumentParser) -> None:
        parser.add_argument("overloads", nargs="*")
    def handle(self, *args: Any, **options: Any) -> None:
    # def handle(self):
        # init worker
        worker = Hello.Worker(options)
        # worker = Hello.Worker()
        try:
            worker.run()
        except:
            logger.error(
                "Processor Group: {%s}, Process: {%s}",
                "say_hello",
                "Hello",
                exc_info=True,
            )
            logger.error(traceback.format_exc())
            sys.exit(1)
        finally:
            # close connections
            worker.finish()