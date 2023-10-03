
import sys
import logging
import traceback
from argparse import ArgumentParser
from typing import Any

from django.core.management.base import BaseCommand
from say_hello.workers import FunctionTest

logger = logging.getLogger(__name__)
class Command(BaseCommand):
    help = "Function Test"
    def add_arguments(self, parser: ArgumentParser) -> None:
        parser.add_argument("overloads", nargs="*")
    def handle(self, *args: Any, **options: Any) -> None:
        # init worker
        worker = FunctionTest.Worker(options)
        try:
            worker.run()
        except:
            logger.error(
                "Processor Group: {%s}, Process: {%s}",
                "say_hello",
                "FunctionTest",
                exc_info=False,
            )
            # logger.error(traceback.format_exc())
            sys.exit(1)
        finally:
            # close connections
            worker.end()