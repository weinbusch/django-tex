from django_tex.environment import environment


def hhmm_format(value):
    total_seconds = value.total_seconds()
    hours, remainder = divmod(total_seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    return '{:n}:{:02n}'.format(hours, minutes)


def test_environment(**options):
    env = environment(**options)
    env.filters.update({
        'hhmm_format': hhmm_format,
    })
    return env
