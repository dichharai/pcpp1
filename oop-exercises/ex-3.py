from readline import set_completion_display_matches_hook


class TimeInterval:
    def __init__(self, hours=0, minutes=0, seconds=0):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def convert_to_seconds(self, fti, sti):
        total_fti = fti.hours*60*60 + fti.minutes*60 + fti.seconds
        total_sti = sti.hours*60*60 + sti.minutes*60 + sti.seconds
        return total_fti, total_sti

    def __add__(self, other):
        if not isinstance(other, TimeInterval):
            raise TypeError(f"{other.__class__.__name__} is not of type {self.__class__.__name__}")
        
        fti, sti = self.convert_to_seconds(self, other)
        add_res = fti + sti

        h = add_res//(60*60)
        m = (add_res % (60*60))//60
        s = add_res - (h*60*60 + m*60)

        return f'{str(h).rjust(2, "0")}:{str(m).rjust(2, "0")}:{str(s).rjust(2, "0")}'


    def __sub__(self, other):
        if not isinstance(other, TimeInterval):
            raise TypeError(f"{other.__class__.__name__} is not of type {self.__class__.__name__}")

        fti, sti = self.convert_to_seconds(self, other)
        add_res = fti - sti

        h = add_res//(60*60)
        m = (add_res % (60*60))//60
        s = add_res - (h*60*60 + m*60)

        return f'{str(h).rjust(2, "0")}:{str(m).rjust(2, "0")}:{str(s).rjust(2, "0")}'


    def __str__(self):
        return f'{str(self.hours).rjust(2, "0")}:{str(self.minutes).rjust(2, "0")}:{str(self.seconds).rjust(2, "0")}'


fti = TimeInterval(21, 58, 50)
sti = TimeInterval(1, 45, 22)

print(fti + sti)
print(fti - sti)
print(fti)
