# Strategy: Support break on BTC, short below min
from utils.notifier import notify_user

async def short_breakdown_support_check():
    notify_user("Strategy 'Support break on BTC, short below min' executed.")
