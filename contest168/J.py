import datetime
def seconds_to_time_str(s: int) -> str:
    h=s//3600;s%=3600;m=s//60;s%=60;s=s;return datetime.datetime(1,1,1,h,m,s).strftime('%H:%M:%S')