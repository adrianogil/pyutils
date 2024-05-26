import threading


class StoppableThread(threading.Thread):
    """
    A thread class that can be stopped externally.

    This class extends the `threading.Thread` class and provides a mechanism to stop the thread
    externally by setting a stop event.

    Attributes:
        _stop_event (threading.Event): An event object used to signal the thread to stop.

    Methods:
        stop(): Sets the stop event, indicating that the thread should stop.
        should_stop(): Checks if the stop event is set, indicating that the thread should stop.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._stop_event = threading.Event()

    def stop(self):
        """
        Sets the stop event, indicating that the thread should stop.
        """
        self._stop_event.set()

    def should_stop(self):
        """
        Checks if the stop event is set, indicating that the thread should stop.

        Returns:
            bool: True if the stop event is set, False otherwise.
        """
        return self._stop_event.is_set()
