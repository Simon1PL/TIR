from typing import List


class Pv:
    def __init__(self, nominal_current, nominal_voltage):
        self.nominal_current = nominal_current
        self.nominal_voltage = nominal_voltage

    def __str__(self):
        return f'\n\tcurrent: {self.nominal_current} \n\tvoltage: {self.nominal_voltage}'

    def get_voltage(self):
        return self.nominal_voltage  # TODO implement realistic output

    def get_current(self):
        return self.nominal_current  # TODO


class PvSeries:
    def __init__(self, pv: Pv, amount: int):
        self.pv = pv
        self.amount = amount

    def __str__(self):
        return f'Series contains {self.amount} panels with params: {self.pv}'

    def set_amount(self, amount: int):
        self.amount = amount

    def get_output_voltage(self):
        return self.pv.get_voltage() * self.amount

    def get_output_current(self):
        return self.pv.get_current()


class Inverter:
    def __init__(self, series_list: List[PvSeries]):
        self.series_list = series_list

    def __str__(self):
        return 'System contains:\n' + '\n'.join([x.__str__() for x in self.series_list])

    def add_series(self, series: PvSeries):
        self.series_list.append(series)


series = PvSeries(Pv(10, 20), 10)

print(series.get_output_current(), series.get_output_voltage())
