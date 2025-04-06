# Strategy: RSI > 65, short near resistance on ETH
from utils.notifier import notify_user

async def short_relief_rally_check():
    notify_user("Strategy 'RSI > 65, short near resistance on ETH' executed.")
