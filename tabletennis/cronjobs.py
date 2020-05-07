from django_cron import CronJobBase, Schedule
from .playerscraper import get_match_data

class MatchCronJob(CronJobBase):
    RUN_EVERY_MINS = 30
    RETRY_AFTER_FAILURE_MINS = 110
    schedule = Schedule(run_every_mins=RUN_EVERY_MINS,retry_after_failure_mins=RETRY_AFTER_FAILURE_MINS)
    code = "tabletennis.match_cron_job"

    def do(self):
        get_match_data()
