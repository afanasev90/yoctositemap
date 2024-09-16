from enum import Enum

class Changefreq(Enum):
    ALWAYS = 1
    HOURLY = 2
    DAILY = 3
    WEEKLY = 4
    MONTHLY = 5
    YEARLY = 6
    NEVER = 7

    def __str__(self):
        r = ''
        match self.value:
            case 1:
                r = 'always'
            case 2:
                r = 'hourly'
            case 3:
                r = 'daily'
            case 4:
                r = 'weekly'
            case 5:
                r = 'monthly'
            case 6:
                r = 'yearly'
            case 7:
                r = 'never'
        return r