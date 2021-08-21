from usim800.Communicate import communicate


class Call(communicate):
    pin_watch_active_call = None

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def call(self, number):
        self.check_pin_setted()
        cmd = "AT"
        self._send_cmd(cmd)
        cmd = "ATD{};".format(number)
        self._send_cmd(cmd)

    def hang(self):
        cmd = "ATH"
        self._send_cmd(cmd)

    def is_call_in_progress(self):
        cmd = "AT+CPAS"
        data = self._send_cmd(cmd,  return_data=True )
        try:
            stats = (data.decode().split())
            print(stats)  # TODO: check response statuses
            # Parameters
            # <pas>        0    Ready (MT allows commands from TA/TE)
            # 2    Unknown (MT is not guaranteed to respond to
            # tructions)
            #  3    Ringing (MT is ready for commands from TA/TE, but the
            # ringer is active)
            # 4    Call in progress (MT is ready for commands from TA/TE,
            # a call is in progress)
            if "OK" in stats:
                stats = True
        except:
            stats = False
        return stats

    def pin_watch_active_call(self, pin_number):
        self.pin_watch_active_call = pin_number

    def check_pin_setted(self):
        if self.pin_watch_active_call is None:
            raise ValueError('Unable to watch the call if the pin to watch is not defined, '
                             'please use pin_watch_active_call() method before invoke call')
