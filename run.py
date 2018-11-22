import sys

from rlbot.utils import logging_utils


if __name__ == "__main__":
    logger = logging_utils.get_logger('rlbot')

    if len(sys.argv) > 1 and sys.argv[1] == 'cli':
        from rlbot import runner
        runner.main()
    else:
        from rlbot.gui.qt_root import RLBotQTGui
        RLBotQTGui.main()